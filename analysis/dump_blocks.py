import sys, openpyxl
wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
ws = wb[sys.argv[2]]
rows = list(ws.iter_rows(values_only=True))
print(f"sheet={sys.argv[2]} rows={len(rows)} cols={max(len(r) for r in rows)}")
print("ROW1:", [ (i,str(v)) for i,v in enumerate(rows[0]) if v not in (None,"") ])
print("ROW2:", [ (i,str(v)) for i,v in enumerate(rows[1]) if v not in (None,"") ][:40])
print("COL A by row:")
for i,r in enumerate(rows):
    print(f"  r{i+1:3d}: {r[0]!r}")
