import sys, numpy as np, pandas as pd
from scipy.stats import mannwhitneyu
PR = sys.argv[1]
sn = pd.read_csv(f"{PR}/neutralization_seqbased.csv")
m = sn["serum"].str.extract(r'^(?P<arm>[^_]+)_(?P<pid>[^_]+)_d(?P<day>\d+)$')
sn = pd.concat([sn, m], axis=1); sn["day"] = sn["day"].astype(int)
sn["subtype"] = sn["virus"].str.extract(r'(H1N1|H3N2)$')
# exclude egg/cell production variants
PROD = r'egg|X-307A|NIB-88|X-223A|IVR-238'
sn = sn[~sn.virus.str.contains(PROD, case=False, na=False)]
gm = lambda x: float(np.exp(np.log(x).mean()))
print("Production variants excluded. Viruses per subtype:",
      sn.groupby("subtype").virus.nunique().to_dict())
for st in ("H1N1","H3N2"):
    g = sn[sn.subtype==st]
    print(f"\n=== {st} ===")
    for d in sorted(g.day.unique()):
        gd = g[g.day==d]
        per = gd.groupby(["arm","pid"]).titer.apply(gm).reset_index()
        a = per.loc[per.arm=="mRNA-1010","titer"]; b = per.loc[per.arm=="Fluarix","titer"]
        if len(a)<3 or len(b)<3:
            print(f"  d{d:<4} n={len(a)}/{len(b)}  (too few)"); continue
        p = mannwhitneyu(a,b,alternative="two-sided")[1]
        print(f"  d{d:<4} n={len(a)}/{len(b)}  GMT mRNA {gm(a):7.1f} vs Fluarix {gm(b):7.1f}"
              f"  ratio {gm(a)/gm(b):.2f}  p={p:.4f}")
    # waning d29 -> latest available per participant
    w = g.pivot_table(index=["arm","pid"], columns="day", values="titer", aggfunc=gm)
    late = w[181] if 181 in w else None
    if late is not None:
        r = (w[29]/late).dropna()
        a = r[r.index.get_level_values("arm")=="mRNA-1010"]
        b = r[r.index.get_level_values("arm")=="Fluarix"]
        p = mannwhitneyu(a,b,alternative="two-sided")[1]
        print(f"  WANING d29/d181: mRNA {gm(a):.2f}x drop (n={len(a)}) vs Fluarix {gm(b):.2f}x"
              f" (n={len(b)})  p={p:.4f}")
