import sys, numpy as np, openpyxl
from scipy.stats import mannwhitneyu
SRC = sys.argv[1]
gm = lambda x: float(np.exp(np.log(np.array(x,dtype=float)).mean()))

def arms(ws, split):
    r1 = [c for c in ws.iter_rows(min_row=1,max_row=1,values_only=True)][0]
    return {"Fluarix": range(1, split), "mRNA-1010": range(split, len(r1))}

# ---- ELISA fold-change blocks (MOESM4 Fig 1d) ----
wb = openpyxl.load_workbook(f"{SRC}/41590_2026_2569_MOESM4_ESM.xlsx", data_only=True)
ws = wb["Fig 1d"]; rows = list(ws.iter_rows(values_only=True))
A = arms(ws, 39)
print("="*72); print("ELISA IgG FOLD CHANGE  (MOESM4 'Fig 1d')   [GM mRNA-1010 vs Fluarix]")
blocks = {"A/H1":(30,31), "A/H3":(35,36), "B/Yam":(40,41), "B/Vic":(45,46)}
for ag,(r4,rl) in blocks.items():
    for lbl, ri in (("wk4",r4), ("wk17/26",rl)):
        row = rows[ri]
        vals = {}
        for arm, cols in A.items():
            vals[arm] = [row[c] for c in cols if c < len(row) and isinstance(row[c],(int,float))]
        m, f = vals["mRNA-1010"], vals["Fluarix"]
        p = mannwhitneyu(m, f, alternative="two-sided")[1]
        flag = "  <-- " if ag.startswith("B/Vic") else ""
        print(f"  {ag:6s} {lbl:8s} n={len(m)}/{len(f)}  GM {gm(m):.2f} vs {gm(f):.2f}   p={p:.4f}{flag}")

# ---- HAI (MOESM9 XData Fig1c) ----
wb9 = openpyxl.load_workbook(f"{SRC}/41590_2026_2569_MOESM9_ESM.xlsx", data_only=True)
ws9 = wb9["XData Fig1c"]; r9 = list(ws9.iter_rows(values_only=True))
A9 = arms(ws9, 16)
print("\n"+"="*72); print("HAI  (MOESM9 'XData Fig1c')   fold change vs week 0")
hb = {"A/H1N1":2, "A/H3N2":9, "B/Yam":16, "B/Vic":23}   # 0-indexed row of 'wk0'
for ag, r0 in hb.items():
    base, wk4 = r9[r0], r9[r0+1]
    late26, late17 = r9[r0+2], r9[r0+3]
    for lbl, lr in (("wk4",[wk4]), ("wk17/26",[late26,late17])):
        out = {}
        for arm, cols in A9.items():
            fc = []
            for c in cols:
                b = base[c] if c < len(base) else None
                v = None
                for rr in lr:
                    if c < len(rr) and isinstance(rr[c],(int,float)): v = rr[c]; break
                if isinstance(b,(int,float)) and isinstance(v,(int,float)) and b>0: fc.append(v/b)
            out[arm] = fc
        m, f = out["mRNA-1010"], out["Fluarix"]
        p = mannwhitneyu(m, f, alternative="two-sided")[1]
        print(f"  {ag:8s} {lbl:8s} n={len(m)}/{len(f)}  GM {gm(m):.2f} vs {gm(f):.2f}   p={p:.4f}")
