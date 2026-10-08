import sys, numpy as np, pandas as pd
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests
PR = sys.argv[1]
sn = pd.read_csv(f"{PR}/neutralization_seqbased.csv")
m = sn["serum"].str.extract(r'^(?P<arm>[^_]+)_(?P<pid>[^_]+)_d(?P<day>\d+)$')
sn = pd.concat([sn, m], axis=1); sn["day"]=sn["day"].astype(int)
sn["subtype"]=sn["virus"].str.extract(r'(H1N1|H3N2)$')
sn = sn[~sn.virus.str.contains(r'egg|X-307A|NIB-88|X-223A|IVR-238', case=False, na=False)]
w = sn.pivot_table(index=["arm","pid","virus","subtype"], columns="day", values="titer", aggfunc="first").reset_index()
w = w.dropna(subset=[0,29]); w["l2fc"]=np.log2(w[29]/w[0]); w["l2d29"]=np.log2(w[29]); w["l2d0"]=np.log2(w[0])
gm=lambda x: float(np.exp(np.log(x).mean()))

for st in ("H1N1","H3N2"):
    g=w[w.subtype==st]; print("="*74); print(st, f"({g.virus.nunique()} wild-type viruses)")
    # (1) per-virus tests on fold change
    r=[]
    for v,gv in g.groupby("virus"):
        a=gv.loc[gv.arm=="mRNA-1010","l2fc"]; b=gv.loc[gv.arm=="Fluarix","l2fc"]
        r.append(mannwhitneyu(a,b,alternative="two-sided")[1])
    q=multipletests(r,method="fdr_bh")[1]
    print(f"  (1) PER-VIRUS tests on log2 fold-change : {(q<0.05).sum()} of {len(q)} q<0.05")
    # (2) participant-level panel mean, fold change
    per=g.groupby(["arm","pid"]).l2fc.mean().reset_index()
    a=per.loc[per.arm=="mRNA-1010","l2fc"]; b=per.loc[per.arm=="Fluarix","l2fc"]
    print(f"  (2) PARTICIPANT-level mean log2 FC      : {a.mean():+.2f} vs {b.mean():+.2f}"
          f"  ({2**a.mean():.2f}x vs {2**b.mean():.2f}x)  p={mannwhitneyu(a,b,alternative='two-sided')[1]:.4f}")
    # (3) participant-level panel mean, absolute d29
    per=g.groupby(["arm","pid"]).l2d29.mean().reset_index()
    a=per.loc[per.arm=="mRNA-1010","l2d29"]; b=per.loc[per.arm=="Fluarix","l2d29"]
    print(f"  (3) PARTICIPANT-level mean log2 d29     : GMT {2**a.mean():.0f} vs {2**b.mean():.0f}"
          f"  ratio {2**(a.mean()-b.mean()):.2f}  p={mannwhitneyu(a,b,alternative='two-sided')[1]:.4f}")
    # (4) baseline balance
    per=g.groupby(["arm","pid"]).l2d0.mean().reset_index()
    a=per.loc[per.arm=="mRNA-1010","l2d0"]; b=per.loc[per.arm=="Fluarix","l2d0"]
    print(f"  (4) BASELINE balance d0                 : GMT {2**a.mean():.0f} vs {2**b.mean():.0f}"
          f"  ratio {2**(a.mean()-b.mean()):.2f}  p={mannwhitneyu(a,b,alternative='two-sided')[1]:.4f}")
    # (5) variance components
    pm = g.groupby(["arm","pid"])[["l2d29","l2fc"]].mean()
    print(f"  (5) between-participant SD: d29 titer {pm.l2d29.std():.2f} log2  |  fold-change {pm.l2fc.std():.2f} log2")
