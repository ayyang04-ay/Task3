"""Absence anchors, asserted mechanically against the shipped data room.

The influenza B evidence gap is the spine of this task. The assert must
therefore be exact in both directions:

  * It must FIND a B lineage written mid-string, e.g. a column header
    'Fold change B/Vic'.  A pattern anchored with ^B/ misses those.
  * It must NOT match influenza A strains named after the Australian state
    of Victoria or the Japanese prefecture of Yamagata, e.g.
    'A/Victoria/4897/2022_IVR-238_H1N1' or 'A/YAMAGATA/98/2023_H3N2'.
    A substring search for 'victoria' or 'yamagata' matches those and
    fails the build on legitimate data.

The negative lookbehind below satisfies both. Do not simplify it.
"""
import sys, os, re, csv

ROOM = sys.argv[1]
B_LINEAGE = re.compile(r'(?<![A-Za-z])B\s*/\s*[A-Za-z]')

# B lineages may appear ONLY in these files. Every other file in the room
# must be free of them -- that absence is what the task is built on.
ALLOWED = {
    "trial_summary.md",          # names the quadrivalent composition
    "elisa_igg_titers.csv",
    "hai_titers.csv",
    "igm_fold_change.csv",
}

# No file may state the gap in prose. Saying it destroys the basin.
FORBIDDEN_PROSE = [
    re.compile(r'no\s+(influenza\s+)?B[\s-]+(lineage\s+)?(functional|neutral)', re.I),
    re.compile(r'B\s+lineage.{0,30}(not\s+(assessed|measured|characteri))', re.I),
    re.compile(r'(lacks?|missing|absent|without).{0,30}B[\s/-]+(Vic|Yam|lineage)', re.I),
    re.compile(r'uncharacteri[sz]ed', re.I),
]

failures = []
checked = 0

for name in sorted(os.listdir(ROOM)):
    path = os.path.join(ROOM, name)
    if not os.path.isfile(path):
        continue
    checked += 1
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()

    found = sorted({m.group(0) for m in B_LINEAGE.finditer(text)})
    if found and name not in ALLOWED:
        ctx = sorted({ln.strip()[:70] for ln in text.splitlines()
                      if B_LINEAGE.search(ln)})[:3]
        failures.append(f"{name}: B lineage present but not permitted -> {ctx}")
    if name in ALLOWED and not found and name != "trial_summary.md":
        failures.append(f"{name}: expected a B lineage and found none "
                        f"(extraction may have dropped a block)")

    for pat in FORBIDDEN_PROSE:
        m = pat.search(text)
        if m:
            failures.append(f"{name}: states the evidence gap in prose -> "
                            f"{m.group(0)[:60]!r}")

# The collision controls must behave, or the pattern above is not doing its job.
MUST_NOT_MATCH = ["A/Victoria/4897/2022_IVR-238_H1N1", "A/YAMAGATA/98/2023_H3N2",
                  "A/Victoria/361/2011", "A/Victoria/1389/2023_H1N1"]
MUST_MATCH = ["B/Vic", "EC50 B/Vic", "Fold change B/Yam",
              "B/Austria/1359417/2021", "B/Phuket/3073/2013"]
for s in MUST_NOT_MATCH:
    if B_LINEAGE.search(s):
        failures.append(f"PATTERN CONTROL: matched influenza A strain {s!r}")
for s in MUST_MATCH:
    if not B_LINEAGE.search(s):
        failures.append(f"PATTERN CONTROL: missed B lineage {s!r}")

# Functional assays must be influenza A only.
FUNCTIONAL = ["neutralization_seqbased.csv", "binding_breadth_h1.csv",
              "binding_breadth_h3.csv", "microneutralization.csv",
              "mab_binding_panels.csv"]
for name in FUNCTIONAL:
    p = os.path.join(ROOM, name)
    if not os.path.exists(p):
        failures.append(f"{name}: missing from the room")
        continue
    with open(p, encoding="utf-8") as fh:
        if B_LINEAGE.search(fh.read()):
            failures.append(f"{name}: functional assay contains a B lineage")

print(f"checked {checked} files in {ROOM}")
print(f"B lineages permitted only in: {sorted(ALLOWED)}")
if failures:
    print("\nFAIL")
    for f in failures:
        print("  - " + f)
    sys.exit(1)
print("\nPASS - absence anchors hold; collision controls behave")
