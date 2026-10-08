import sys, re, glob, openpyxl
from pyxlsb import open_workbook
BLIN = re.compile(r'(?<![A-Za-z])B\s*/\s*[A-Za-z]')
ALLOWED = {"MOESM4","MOESM9","MOESM11"}
hits, fails, scanned = {}, [], []

def scan_xlsx(path):
    out = {}
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for ws in wb.worksheets:
        f = {v.strip() for row in ws.iter_rows(values_only=True) for v in row
             if isinstance(v,str) and BLIN.search(v)}
        if f: out[ws.title] = sorted(f)
    wb.close(); return out

def scan_xlsb(path):
    out = {}
    with open_workbook(path) as wb:
        for name in wb.sheets:
            f = set()
            with wb.get_sheet(name) as sh:
                for row in sh.rows():
                    for c in row:
                        if isinstance(c.v,str) and BLIN.search(c.v): f.add(c.v.strip())
            if f: out[name] = sorted(f)
    return out

for path in sorted(glob.glob(sys.argv[1]+"/*.xls*")):
    f = path.split("/")[-1]; tag = re.search(r'(MOESM\d+)', f).group(1)
    scanned.append(tag)
    got = scan_xlsb(path) if path.endswith(".xlsb") else scan_xlsx(path)
    if got:
        hits[f] = got
        if tag not in ALLOWED: fails.append((f, got))

print(f"SCANNED {len(scanned)} workbooks: {sorted(scanned, key=lambda s:int(s[5:]))}")
print("="*70)
print("B LINEAGE FOUND IN:")
for f in sorted(hits):
    print(f"  {f}")
    for sh,v in hits[f].items(): print(f"      '{sh}': {v}")
print("\nNO B LINEAGE:")
for p in sorted(glob.glob(sys.argv[1]+"/*.xls*")):
    if p.split("/")[-1] not in hits: print("  "+p.split("/")[-1])
print(f"\nASSERT (B only in {sorted(ALLOWED)}):",
      "PASS" if not fails else f"FAIL {fails}")
