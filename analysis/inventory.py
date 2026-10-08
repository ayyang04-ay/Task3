import sys, openpyxl
for path in sys.argv[1:]:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    print("="*78)
    print("FILE:", path.split("/")[-1])
    for ws in wb.worksheets:
        rows = ws.max_row; cols = ws.max_column
        print(f"  SHEET '{ws.title}'  dims~{rows}x{cols}")
        for i, row in enumerate(ws.iter_rows(min_row=1, max_row=min(6, rows or 6), values_only=True)):
            vals = ["" if v is None else str(v)[:34] for v in row[:14]]
            print("     r%d | %s" % (i+1, " | ".join(vals)))
    wb.close()
