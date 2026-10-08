import sys, re, glob, openpyxl
# 'B/' must be immediately preceded by a word boundary and NOT by 'A' — so
# 'EC50 B/Vic' and 'Fold change B/Vic' match, while 'A/Victoria/...' does not.
BLIN = re.compile(r'(?<![A-Za-z])B\s*/\s*[A-Za-z]')
FUNCTIONAL = {"MOESM8","MOESM12","MOESM13","MOESM14","MOESM5","MOESM6","MOESM7"}
ALLOWED    = {"MOESM4","MOESM9","MOESM11"}
hits, fails = {}, []
for path in sorted(glob.glob(sys.argv[1]+"/*.xlsx")):
    f = path.split("/")[-1]; tag = re.search(r'(MOESM\d+)', f).group(1)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for ws in wb.worksheets:
        found = set()
        for row in ws.iter_rows(values_only=True):
            for v in row:
                if isinstance(v,str) and BLIN.search(v): found.add(v.strip())
        if found:
            hits.setdefault(f, {})[ws.title] = sorted(found)
            if tag not in ALLOWED: fails.append((f, ws.title, sorted(found)))
    wb.close()
print("B-LINEAGE OCCURRENCES  (corrected pattern)"); print("="*70)
for f in sorted(hits):
    print(f"  {f}")
    for sh, vals in hits[f].items(): print(f"      '{sh}': {vals}")
print("\nFILES WITH NO B LINEAGE:")
for p in sorted(glob.glob(sys.argv[1]+"/*.xlsx")):
    f=p.split("/")[-1]
    if f not in hits: print(f"  {f}")
print("\nASSERT: B must appear ONLY in", sorted(ALLOWED))
print("  RESULT:", "PASS — no B outside the allowed set" if not fails else f"FAIL: {fails}")
# sanity: the pattern must still reject A/ strain names
ctl = ["A/Victoria/4897/2022_IVR-238_H1N1","A/YAMAGATA/98/2023_H3N2","A/Victoria/361/2011"]
print("  control (must all be False):", [bool(BLIN.search(c)) for c in ctl])
print("  control (must all be True): ", [bool(BLIN.search(c)) for c in
      ["EC50 B/Vic","Fold change B/Yam","B/Vic","B/Austria/1359417/2021"]])
