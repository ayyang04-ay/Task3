import sys
from pyxlsb import open_workbook
path = sys.argv[1]
with open_workbook(path) as wb:
    print("SHEETS:", wb.sheets)
    for name in wb.sheets:
        with wb.get_sheet(name) as sh:
            n = 0; head = []
            for row in sh.rows():
                if n < 6: head.append([c.v for c in row][:12])
                n += 1
            print(f"\n  SHEET '{name}'  rows={n}")
            for i, h in enumerate(head):
                print(f"     r{i+1} | " + " | ".join("" if v is None else str(v)[:30] for v in h))
