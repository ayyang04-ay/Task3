"""Recompute every graded anchor from the shipped data room."""
import sys, re, numpy as np, pandas as pd
from scipy.stats import mannwhitneyu, pearsonr
from statsmodels.stats.multitest import multipletests
R = sys.argv[1]
gm = lambda x: float(np.exp(np.log(np.asarray(x, float)).mean()))
mw = lambda a, b: mannwhitneyu(a, b, alternative="two-sided")[1]
ok = lambda c: "OK " if c else "XX "
fails = []
def check(label, cond, detail):
    print(f"  {ok(cond)}{label:52s} {detail}")
    if not cond: fails.append(label)

print("ELISA IgG fold change  (elisa_igg_titers.csv)")
e = pd.read_csv(f"{R}/elisa_igg_titers.csv")
fc = e[e.measure == "fold_change"]
for ag, tp, exp in (("A/H1","wk17/26",(2.12,1.40)), ("A/H3","wk17/26",(3.47,1.52)),
                    ("B/Vic","wk4",(3.16,2.30)), ("B/Vic","wk17/26",(1.57,1.56)),
                    ("B/Yam","wk17/26",(1.46,1.41))):
    g = fc[(fc.antigen == ag) & (fc.timepoint == tp)]
    m = g.loc[g.arm == "mRNA-1010", "value"]; f = g.loc[g.arm == "Fluarix", "value"]
    p = mw(m, f)
    check(f"{ag} {tp}", abs(gm(m)-exp[0]) < 0.02 and abs(gm(f)-exp[1]) < 0.02,
          f"GM {gm(m):.2f} vs {gm(f):.2f}  p={p:.4f}  n={len(m)}/{len(f)}")

print("\nHAI  (hai_titers.csv)  fold change vs wk0")
h = pd.read_csv(f"{R}/hai_titers.csv")
w = h.pivot_table(index=["antigen","arm","participant"], columns="timepoint",
                  values="hai_titer", aggfunc="first")
w["late"] = w.get("wk26").fillna(w.get("wk17"))
for ag, exp in (("A/H1N1",(2.76,2.25)), ("A/H3N2",(1.72,1.66)), ("B/Vic",None)):
    g = w.xs(ag, level="antigen").dropna(subset=["wk0","wk4"])
    r = (g.wk4 / g.wk0)
    m = r[r.index.get_level_values("arm")=="mRNA-1010"]
    f = r[r.index.get_level_values("arm")=="Fluarix"]
    p = mw(m, f)
    cond = True if exp is None else (abs(gm(m)-exp[0])<0.02 and abs(gm(f)-exp[1])<0.02)
    check(f"{ag} wk4 fold change", cond, f"GM {gm(m):.2f} vs {gm(f):.2f}  p={p:.4f}")

print("\nSequencing-based neutralization  (neutralization_seqbased.csv)")
sn = pd.read_csv(f"{R}/neutralization_seqbased.csv")
m_ = sn.serum.str.extract(r'^(?P<arm>[^_]+)_(?P<pid>[^_]+)_d(?P<day>\d+)$')
sn = pd.concat([sn, m_], axis=1); sn["day"] = sn.day.astype(int)
sn["subtype"] = sn.virus.str.extract(r'(H1N1|H3N2)$')
piv = sn.pivot_table(index=["arm","pid","virus","subtype"], columns="day",
                     values="titer", aggfunc="first").reset_index().dropna(subset=[0,29])
piv["l2fc"] = np.log2(piv[29] / piv[0])
res = {}
for st, g in piv.groupby("subtype"):
    rec = []
    for v, gv in g.groupby("virus"):
        a = gv.loc[gv.arm=="mRNA-1010","l2fc"]; b = gv.loc[gv.arm=="Fluarix","l2fc"]
        rec.append(dict(virus=v, delta=a.median()-b.median(), p=mw(a,b)))
    d = pd.DataFrame(rec); d["q"] = multipletests(d.p, method="fdr_bh")[1]
    res[st] = d
check("H1N1 significant within panel", (res["H1N1"].q<0.05).sum()==11,
      f"{(res['H1N1'].q<0.05).sum()} of {len(res['H1N1'])}  median delta {res['H1N1'].delta.median():+.2f} log2")
check("H3N2 significant within panel", (res["H3N2"].q<0.05).sum()==0,
      f"{(res['H3N2'].q<0.05).sum()} of {len(res['H3N2'])}  median delta {res['H3N2'].delta.median():+.2f} log2")
nulls = sorted(res["H1N1"][res["H1N1"].q>=0.05].virus)
check("H1N1 nulls are the two oldest isolates",
      nulls == ["A/Brisbane/02/2018_H1N1","A/Michigan/45/2015_H1N1"], str(nulls))
sig = res["H1N1"][res["H1N1"].q<0.05]
check("H1N1 significant dated 2023",
      sum(bool(re.search(r'/2023', v)) for v in sig.virus)==6,
      f"{sum(bool(re.search(r'/2023', v)) for v in sig.virus)} of {len(sig)}")
pooled = pd.concat(res.values()); pooled["qp"] = multipletests(pooled.p, method="fdr_bh")[1]
check("pooled FDR across 96 extinguishes H1N1", (pooled.qp<0.05).sum()==0,
      f"{(pooled.qp<0.05).sum()} of 96 survive pooled correction")

print("\nBinding breadth  (binding_breadth_h*.csv)")
bb = {}
for tag, f_ in (("H1","binding_breadth_h1.csv"), ("H3","binding_breadth_h3.csv")):
    d = pd.read_csv(f"{R}/{f_}"); rec=[]
    for s, g in d.groupby("strain"):
        a = g.loc[g.arm=="mRNA-1010","log2_fold_change_mfi"]
        b = g.loc[g.arm=="Fluarix","log2_fold_change_mfi"]
        rec.append(dict(strain=s, delta=a.median()-b.median(), p=mw(a,b)))
    r = pd.DataFrame(rec); r["q"] = multipletests(r.p, method="fdr_bh")[1]; bb[tag]=r
check("H3 binding breadth 12 of 12", (bb["H3"].q<0.05).sum()==12,
      f"{(bb['H3'].q<0.05).sum()} of 12  median delta {bb['H3'].delta.median():+.2f} log2")
check("H1 binding breadth 7 of 9 (NOT 8)", (bb["H1"].q<0.05).sum()==7,
      f"{(bb['H1'].q<0.05).sum()} of 9  median delta {bb['H1'].delta.median():+.2f} log2")

print("\nBinding vs neutralization, H3 strains measured both ways")
def norm(s):
    s = re.sub(r'_(H1N1|H3N2)$','',s); s = re.sub(r'_IVR-\d+','',s)
    return re.sub(r'/0+(\d)/','/\\1/',s).lower().strip()
nb = bb["H3"].assign(key=bb["H3"].strain.map(norm))
nn = res["H3N2"].assign(key=res["H3N2"].virus.map(norm))
j = nb.merge(nn, on="key", suffixes=("_bind","_neut"))
check("H3 shared: all binding-sig, none neut-sig",
      (j.q_bind<0.05).sum()==len(j) and (j.q_neut<0.05).sum()==0,
      f"{len(j)} shared | binding-sig {(j.q_bind<0.05).sum()} | neut-sig {(j.q_neut<0.05).sum()}"
      f" | r={pearsonr(j.delta_bind, j.delta_neut)[0]:+.2f}")
dar = j[j.key.str.contains("darwin")]
check("homologous A/Darwin/6/2021 dissociation", len(dar)==1,
      f"binding {dar.delta_bind.iloc[0]:+.2f} / neut {dar.delta_neut.iloc[0]:+.2f}")

print("\nConventional microneutralization  (microneutralization.csv)")
mn = pd.read_csv(f"{R}/microneutralization.csv")
f_ = mn[(mn.measure=="fold_change")]
for pan, exp in (("homologous",(2.49,3.32)), ("heterologous",(4.12,3.03))):
    g = f_[(f_.panel==pan) & (f_.timepoint=="wk4")]
    m = g.loc[g.arm=="mRNA-1010","value"]; fl = g.loc[g.arm=="Fluarix","value"]
    check(f"{pan} wk4", abs(gm(m)-exp[0])<0.02 and abs(gm(fl)-exp[1])<0.02,
          f"GM {gm(m):.2f} vs {gm(fl):.2f}  p={mw(m,fl):.3f}")

print("\nDurability of the H1N1 functional advantage")
prod = r'egg|X-307A|NIB-88|X-223A|IVR-238'
g = sn[(sn.subtype=="H1N1") & (~sn.virus.str.contains(prod, case=False, na=False))]
pm = g.pivot_table(index=["arm","pid"], columns="day", values="titer", aggfunc=gm)
for d in (29, 181):
    a = pm[d].dropna()
    mm = a[a.index.get_level_values("arm")=="mRNA-1010"]
    ff = a[a.index.get_level_values("arm")=="Fluarix"]
    print(f"      d{d:<4} GMT {gm(mm):7.1f} vs {gm(ff):7.1f}  ratio {gm(mm)/gm(ff):.2f}  p={mw(mm,ff):.4f}")
r = (pm[29]/pm[181]).dropna()
mm = r[r.index.get_level_values("arm")=="mRNA-1010"]; ff = r[r.index.get_level_values("arm")=="Fluarix"]
check("adverse waning d29->d181 is significant", mw(mm,ff) < 0.01,
      f"mRNA {gm(mm):.2f}x drop vs Fluarix {gm(ff):.2f}x  p={mw(mm,ff):.4f}")

print()
print("ALL ANCHORS PASS" if not fails else f"FAILED: {fails}")
sys.exit(1 if fails else 0)
