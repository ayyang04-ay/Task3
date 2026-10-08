import sys, re, numpy as np, pandas as pd
from scipy.stats import mannwhitneyu, spearmanr, pearsonr
from statsmodels.stats.multitest import multipletests
PR = sys.argv[1]
pd.set_option("display.width", 200)

# ---------- 1. sequencing-based neutralization ----------
sn = pd.read_csv(f"{PR}/neutralization_seqbased.csv")
m = sn["serum"].str.extract(r'^(?P<arm>[^_]+)_(?P<pid>[^_]+)_d(?P<day>\d+)$')
sn = pd.concat([sn, m], axis=1); sn["day"] = sn["day"].astype(int)
sn["subtype"] = sn["virus"].str.extract(r'(H1N1|H3N2)$')

w = sn.pivot_table(index=["arm","pid","virus","subtype"], columns="day",
                   values="titer", aggfunc="first").reset_index()
w = w.dropna(subset=[0, 29])
w["l2fc"] = np.log2(w[29] / w[0])

rows = []
for st, g in w.groupby("subtype"):
    recs = []
    for v, gv in g.groupby("virus"):
        a = gv.loc[gv.arm == "mRNA-1010", "l2fc"].dropna()
        b = gv.loc[gv.arm == "Fluarix",   "l2fc"].dropna()
        if len(a) < 3 or len(b) < 3: continue
        u, p = mannwhitneyu(a, b, alternative="two-sided")
        recs.append(dict(subtype=st, virus=v, n_mrna=len(a), n_flu=len(b),
                         med_mrna=a.median(), med_flu=b.median(),
                         delta=a.median()-b.median(), p=p))
    d = pd.DataFrame(recs)
    d["q_within_panel"] = multipletests(d["p"], method="fdr_bh")[1]
    rows.append(d)
neut = pd.concat(rows, ignore_index=True)

print("="*78); print("SEQ-BASED NEUTRALIZATION — log2 FC (d29/d0), Mann-Whitney, BH within subtype panel")
for st, g in neut.groupby("subtype"):
    sig = (g.q_within_panel < 0.05).sum()
    print(f"  {st}: {sig} of {len(g)} viruses q<0.05 | median delta = {g.delta.median():+.3f} log2"
          f" | n per arm = {g.n_mrna.max()}/{g.n_flu.max()}")
    if st == "H1N1":
        print(g.sort_values("q_within_panel")[["virus","delta","p","q_within_panel"]].to_string(index=False))

print("\n  H1N1 non-significant viruses:",
      list(neut[(neut.subtype=="H1N1") & (neut.q_within_panel>=0.05)].virus))
h1sig = neut[(neut.subtype=="H1N1") & (neut.q_within_panel<0.05)]
print("  of the significant H1N1, dated 2023:",
      sum(bool(re.search(r'/2023', v)) for v in h1sig.virus), "of", len(h1sig))
print(f"  H1N1 significant delta range: {h1sig.delta.min():+.2f} to {h1sig.delta.max():+.2f} log2")

# pooled FDR across all 96
pooled = neut.copy()
pooled["q_pooled"] = multipletests(pooled["p"], method="fdr_bh")[1]
print("\n  POOLED FDR across all 96 viruses:")
for st, g in pooled.groupby("subtype"):
    print(f"    {st}: {(g.q_pooled<0.05).sum()} of {len(g)} q<0.05")

# ---------- 2. binding breadth ----------
print("\n"+"="*78); print("BINDING BREADTH (bead array, log2 FC MFI)")
bb = {}
for tag, f in (("H1","binding_breadth_h1.csv"), ("H3","binding_breadth_h3.csv")):
    d = pd.read_csv(f"{PR}/{f}")
    recs = []
    for s, g in d.groupby("strain"):
        a = g.loc[g.arm=="mRNA-1010","log2_fold_change_mfi"].dropna()
        b = g.loc[g.arm=="Fluarix","log2_fold_change_mfi"].dropna()
        u, p = mannwhitneyu(a, b, alternative="two-sided")
        recs.append(dict(strain=s, delta=a.median()-b.median(), p=p, n_m=len(a), n_f=len(b)))
    r = pd.DataFrame(recs); r["q"] = multipletests(r["p"], method="fdr_bh")[1]
    bb[tag] = r
    print(f"  {tag}: {(r.q<0.05).sum()} of {len(r)} strains q<0.05 | median delta = {r.delta.median():+.3f} log2"
          f" | n = {r.n_m.max()}/{r.n_f.max()}")

# ---------- 3. binding vs neutralization on shared strains ----------
print("\n"+"="*78); print("BINDING vs NEUTRALIZATION on strains measured BOTH ways")
def norm(s):
    s = s.replace("\xa0"," ").strip()
    s = re.sub(r'_(H1N1|H3N2)$','',s); s = re.sub(r'_IVR-\d+','',s)
    s = re.sub(r'/0+(\d)/','/\\1/',s)
    return s.lower()
nb = pd.concat([bb["H1"].assign(panel="H1"), bb["H3"].assign(panel="H3")])
nb["key"] = nb.strain.map(norm); neut["key"] = neut.virus.map(norm)
j = nb.merge(neut, on="key", suffixes=("_bind","_neut"))
print(f"  shared strains: {len(j)}")
print(j[["key","delta_bind","q","delta_neut","q_within_panel"]]
      .rename(columns={"q_within_panel":"q_neut"}).to_string(index=False))
print(f"  binding-significant: {(j.q<0.05).sum()} | neut-significant: {(j.q_within_panel<0.05).sum()}")
if len(j) > 2:
    print(f"  Pearson r(delta_bind, delta_neut) = {pearsonr(j.delta_bind, j.delta_neut)[0]:+.3f}"
          f" | Spearman = {spearmanr(j.delta_bind, j.delta_neut)[0]:+.3f}")
dar = j[j.key.str.contains("darwin")]
if len(dar): print("  HOMOLOGOUS H3 A/Darwin/6/2021:",
                   f"binding {dar.delta_bind.iloc[0]:+.3f} / neut {dar.delta_neut.iloc[0]:+.3f}")

# ---------- 4. conventional microneutralization ----------
print("\n"+"="*78); print("CONVENTIONAL MICRONEUTRALIZATION (fold change)")
for tag, f in (("homologous A/Darwin/9/2021","microneut_fc_homologous.csv"),
               ("heterologous A/Thailand/8/2022","microneut_fc_heterologous.csv")):
    d = pd.read_csv(f"{PR}/{f}")
    for tp, g in d.groupby("timepoint"):
        a = pd.to_numeric(g.loc[g.arm=="mRNA-1010","value"], errors="coerce").dropna()
        b = pd.to_numeric(g.loc[g.arm=="Fluarix","value"], errors="coerce").dropna()
        gm = lambda x: float(np.exp(np.log(x).mean()))
        u, p = mannwhitneyu(a, b, alternative="two-sided")
        print(f"  {tag:32s} wk{tp:<6} GM mRNA-1010 {gm(a):.2f} vs Fluarix {gm(b):.2f}  p={p:.3f}")

# ---------- 5. binding/neut join split BY PANEL ----------
print("\n"+"="*78); print("BINDING vs NEUT, SPLIT BY PANEL")
for pan, g in j.groupby("panel"):
    print(f"  {pan} panel: {len(g)} shared strains | binding-sig {(g.q<0.05).sum()} "
          f"| neut-sig {(g.q_within_panel<0.05).sum()}")
    if len(g) > 2:
        print(f"     Pearson r = {pearsonr(g.delta_bind,g.delta_neut)[0]:+.3f} "
              f"| Spearman = {spearmanr(g.delta_bind,g.delta_neut)[0]:+.3f}")
