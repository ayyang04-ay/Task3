import sys, csv, re, os, openpyxl
SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

def arm_map(ws):
    """row1 = arm group labels (sparse), row2 = participant ids -> dict col->arm"""
    rows = list(ws.iter_rows(min_row=1, max_row=2, values_only=True))
    arms, cur = {}, None
    for j, v in enumerate(rows[0]):
        if v not in (None, ""): cur = str(v).strip()
        arms[j] = cur
    ids = {j: (str(v).strip() if v not in (None,"") else None) for j, v in enumerate(rows[1])}
    return arms, ids

def wide_to_long(ws, label_name, out_path, value_name):
    arms, ids = arm_map(ws)
    with open(out_path, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow([label_name, "arm", "participant", value_name])
        for row in ws.iter_rows(min_row=3, values_only=True):
            if not row or row[0] in (None, ""): continue
            lab = str(row[0]).replace("\xa0", " ").strip()
            for j in range(1, len(row)):
                if ids.get(j) and row[j] not in (None, ""):
                    w.writerow([lab, arms.get(j), ids[j], row[j]])

wb8 = openpyxl.load_workbook(f"{SRC}/41590_2026_2569_MOESM8_ESM.xlsx", data_only=True)
wide_to_long(wb8["Fig 5b"], "strain", f"{OUT}/binding_breadth_h1.csv", "log2_fold_change_mfi")
wide_to_long(wb8["Fig 5c"], "strain", f"{OUT}/binding_breadth_h3.csv", "log2_fold_change_mfi")
ws = wb8["Fig 5d and e"]
with open(f"{OUT}/neutralization_seqbased.csv","w",newline="") as fh:
    w = csv.writer(fh)
    for row in ws.iter_rows(values_only=True):
        if row and any(v not in (None,"") for v in row): w.writerow(row)

wb13 = openpyxl.load_workbook(f"{SRC}/41590_2026_2569_MOESM13_ESM.xlsx", data_only=True)
for sheet, tag in (("XData Fig 6c","group1"), ("XData Fig 6d","group2")):
    wide_to_long(wb13[sheet], "antigen", f"{OUT}/mab_binding_{tag}.csv", "fold_over_control")

wb14 = openpyxl.load_workbook(f"{SRC}/41590_2026_2569_MOESM14_ESM.xlsx", data_only=True)
for sheet, nm in (("XData Fig 7a","titer_homologous"),("XData Fig 7b","titer_heterologous"),
                  ("XData Fig 7c","fc_homologous"),("XData Fig 7d","fc_heterologous")):
    wide_to_long(wb14[sheet], "timepoint", f"{OUT}/microneut_{nm}.csv", "value")

wb11 = openpyxl.load_workbook(f"{SRC}/41590_2026_2569_MOESM11_ESM.xlsx", data_only=True)
ws = wb11["XData Fig 4b"]
with open(f"{OUT}/gc_pb_frequencies.csv","w",newline="") as fh:
    w = csv.writer(fh); w.writerow(["antigen","w1_PB","w26_GC"])
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row and row[0] not in (None,""): w.writerow([row[0], row[1], row[2]])

for f in sorted(os.listdir(OUT)):
    p = f"{OUT}/{f}"; n = sum(1 for _ in open(p)) - 1
    print(f"{f:42s} {n:7d} data rows")
