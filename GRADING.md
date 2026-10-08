# WU397 next-study design — grading guidelines

Task ID: jp2x8c9f · camp_0589d1e96758477586df0e43dd8eeec1
Lane: clinical/translational evidence appraisal and study specification.

---

## Task framing

The attempt is given a working directory holding the complete source data from a
single immunogenicity study of a quadrivalent mRNA influenza vaccine against a
licensed quadrivalent comparator, and asked to recommend the next studies, each
specified to the level of what is measured, in whom, and against what.

The data support a claim of broader **binding**, not broader **protection**, and
they do so for only half the formulation. Both facts have to be established from
the files; neither is stated anywhere in the mount.

The number of studies proposed is not graded. An attempt may propose one
well-specified trial plus an influenza B characterisation study, or a three-to-
four study programme covering the same ground. What is graded is whether the
three commitments below are made and correctly grounded.

---

## Bridge line

Credit the consequence, not the phrasing. An attempt that lists influenza B among
missing assays but proposes no study for it has inventoried the gap without
reaching it; an attempt that never uses the word "quadrivalent" but specifies a
B/Victoria characterisation study as a prerequisite has reached it. Grade which of
those happened.

---

## Golden Response

**One-line recommendation.** Power the heterologous-protection readout on A/H1N1
against contemporary and forward-drift isolates with a durability co-primary, and
run a B/Victoria functional characterisation study in parallel — the package
establishes broader binding, not broader protection, and generates no functional
data at all for half the formulation.

### Study 1 — heterologous protection, A/H1N1

*What is measured.* Sequencing-based or live-virus neutralisation titre against a
pre-locked panel of contemporary and forward-drift A/H1N1 clinical isolates.
Co-primary endpoints at day 29 and at day 181 or later. Haemagglutination
inhibition retained as a regulatory bridge, not as the primary functional readout.

*In whom.* Adults, randomised and observer-blind, stratified on pre-vaccination
titre and on birth cohort. Baseline stratification is required: the mRNA arm
started lower on A/H3N2 (d0 GMT 160 vs 243) and on heterologous
microneutralisation (57.0 vs 121.3), and baseline anti-correlates with fold-rise,
so an unstratified fold-rise endpoint flatters whichever arm enrolled lower.
Birth-cohort stratification is motivated by the H1/H3 asymmetry, which is the
pattern imprinting would produce and which the held data cannot test — no age or
birth year appears anywhere in the mount.

*Against what.* Wild-type clinical isolates post-dating the 2022–2023 vaccine
composition. Egg- and cell-propagated production reassortants excluded.

*Why A/H1N1 carries this readout.* In `neutralization_seqbased.csv`, per-virus
Mann-Whitney on log2 fold-change with Benjamini-Hochberg correction applied
within each subtype panel separates the arms on **11 of 13** A/H1N1 viruses,
median delta **+1.32 log2**. The two non-significant viruses are the two oldest
in the panel, A/Michigan/45/2015 and A/Brisbane/02/2018; **6 of the 11**
significant viruses are 2023 isolates post-dating the vaccine composition. The
effect scales with antigenic distance rather than being uniform: regressing
per-virus arm advantage on distance gives a positive slope for H1N1 and a
negative slope for H3N2.

*Why the durability co-primary.* The functional advantage does not persist.
Participant-level A/H1N1 GMT across wild-type panel viruses is 883.7 vs 501.4 at
day 29 (ratio 1.76) and 402.5 vs 315.9 at day 181 (ratio 1.27). Waning from day
29 to day 181 is 2.13-fold in the mRNA arm against 1.24-fold in the comparator,
**p = 0.0022** — the most statistically secure between-arm result in the package,
and it is unfavourable. A day-29-only design would support a claim that has
decayed before the end of a single season. Note that the binding readout points
the other way (ELISA fold-change at wk17/26, 2.12 vs 1.40, p = 0.0001); the
functional and binding durability signals disagree, and the functional one
governs a protection claim.

### Study 2 — B/Victoria functional characterisation

*What is measured.* Neutralisation against a B/Victoria panel, plus the
antigen-specific B-cell and monoclonal characterisation that exists for the A
subtypes — a binding-breadth panel and monoclonal isolation.

*In whom.* The same population; this can run as a sub-study of Study 1 or as a
standalone immunogenicity study.

*Against what.* Contemporary B/Victoria isolates, including drift variants
post-dating B/Austria/1359417/2021.

*Why this is a prerequisite rather than an addition.* The product is
quadrivalent. Across all eleven source workbooks, influenza B appears only in
`elisa_igg_titers.csv`, `hai_titers.csv` and `igm_fold_change.csv`. There is no
B neutralisation, no B binding-breadth panel and no B monoclonal characterisation: the
functional assays — `neutralization_seqbased.csv` (13 H1N1 + 83 H3N2 viruses),
`binding_breadth_h1.csv` (9 strains), `binding_breadth_h3.csv` (12 strains),
`microneutralization.csv`, `mab_binding_panels.csv` (two panels, ~340 and ~385
monoclonals) — are influenza A only.

What binding data exist for B/Victoria do not support a claim. The advantage is
significant at week 4 (GM fold-change 3.16 vs 2.30, p = 0.0146) and absent by
wk17/26 (1.57 vs 1.56, **p = 0.8363**), while both A subtypes hold their
advantage at the same timepoint (A/H1 2.12 vs 1.40; A/H3 3.47 vs 1.52). HAI is
flat for B in both arms (B/Vic wk4 fold-change 1.08 vs 1.05, p = 0.675). A
product-level claim cannot rest on an antigen with no functional data and a
binding advantage that decays to parity.

B/Yamagata is correctly out of scope: it has not circulated since 2020 and has
been removed from seasonal formulations. The live influenza B question is
B/Victoria.

### Study 3 — resolving the A/H3N2 binding-versus-function dissociation

*What is measured.* Whether the additional H3 binding is functional at all:
stem-competition and epitope mapping, Fc-effector assays (ADCC, ADCP),
neuraminidase inhibition, and heterosubtypic neutralisation rather than binding
alone. Passive transfer and heterologous challenge in a pre-immune animal model,
analysed as protection per unit neutralising titre.

*Why H3N2 cannot carry a protection readout as it stands.* Bead-array binding
separates the arms on **12 of 12** H3 strains, median delta **+2.30 log2**.
Sequencing-based neutralisation separates on **0 of 83** H3N2 viruses after
within-panel correction — at the same n per arm that detected 11 of 13 in H1N1,
so this is not an underpowering result. On the five H3 strains measured by both
methods, all five are binding-significant, none is neutralisation-significant,
and the per-strain effect sizes are uncorrelated (r = +0.10). On the homologous
H3 vaccine strain A/Darwin/6/2021, binding is **+2.07 log2** while
neutralisation is **−0.27**. Separately, the binding panels contain no strain
later than 2022, so they measure back-boost against historical strains rather
than forward drift, and cannot support a forward-looking claim even in
principle.

### What the package does not support, and why

*Haemagglutination inhibition, the licensed correlate, separates nothing.*
A/H1N1 wk4 fold-change 2.76 vs 2.25 (p = 0.26), A/H3N2 1.72 vs 1.66 (p = 0.69).

*Conventional microneutralisation is flat and numerically favours the comparator
on the homologous strain* — wk4 fold-change GM 2.49 vs 3.32 (p = 0.53);
heterologous 4.12 vs 3.03 (p = 0.32), the latter confounded by the 2.1-fold
baseline deficit noted above.

*Molecular and mechanistic readouts* — sustained germinal-centre responses,
repertoire diversification, clonotype counts, single-cell annotations — support a
mechanism, not a protection claim, and come from a small subset: the lymph-node
cohort is 2 mRNA-1010 and 11 Fluarix participants, and the clonal-overlap table
covers 7 donors. The monoclonal panels are pseudoreplicated across 7 donors, so
per-monoclonal percentages overstate the evidence; `group_I` runs opposite to
`group_II`.

*Correcting across all 96 viruses at once* extinguishes the H1N1 signal (11 → 0,
nothing surviving pooled correction) and makes both subtypes look equivalent.
The panels are two separate libraries of 13 and 83 viruses; correction belongs
within each.

*Normalising heterologous titre to each participant's own vaccine-strain titre*
makes H3N2 appear to separate, but the effect is a smaller denominator: at
A/Darwin/6/2021 the mRNA arm responded less well than the comparator. Such an
endpoint rewards an arm for failing against the strain in its own vaccine and
must not be used.

---

## A) Required

The attempt makes these three commitments and grounds them in the files.

**A1 — The heterologous-protection readout is powered on A/H1N1.** The attempt
identifies A/H1N1, not A/H3N2, as the subtype carrying a functional endpoint, and
grounds it in the sequencing-based neutralisation result (11 of 13 viruses
separating within panel) rather than in binding data. An attempt that recommends
powering on A/H3N2, or that treats the two A subtypes as interchangeable, has not
made this commitment.

**A2 — The strain set is contemporary and forward-drift H1N1 isolates.** The
attempt specifies that the panel comprises isolates contemporary with or
post-dating the 2022–2023 vaccine composition, rather than a historical strain
series. Any reasonable grounding counts: the 2023 isolates among the significant
viruses, the drift-distance gradient, or the observation that the binding panels
stop at 2022 and so cannot speak to forward drift. The attempt need not assert
that the two non-significant viruses prove drift-specificity.

**A3 — Influenza B coverage is treated as a prerequisite.** The attempt
establishes that no functional data of any kind exist for influenza B, draws the
consequence that a quadrivalent product claim cannot be supported on influenza A
data alone, and specifies a study or sub-study that generates B/Victoria
functional data. Scoping B/Yamagata out as no longer circulating is correct and
must not be treated as an omission.

A3 is reached only when the consequence is drawn. Noting influenza B among a
list of absent assays, without proposing work to close it, does not satisfy A3.

## B) Penalised

**B1 — Recommending A/H3N2 as the heterologous-protection readout** on the
strength of the binding-breadth result, where the matched functional data in the
same participants show no separation on any of 83 viruses.

**B2 — Treating binding breadth as a protection signal.** Proposing a
multiplex-binding primary endpoint, or citing the 12-of-12 bead-array result as
evidence of protective strain coverage, without confronting the neutralisation nulls.

**B3 — Reading the 83 H3N2 nulls as underpowering** and recommending a larger
H3N2 neutralisation study as the protection trial, when the same n per arm
detected 11 of 13 in H1N1.

**B4 — Correcting for multiplicity across all 96 viruses** and concluding that
neither subtype has functional support, when the panels are separate libraries.

**B5 — Treating influenza B as covered** by the week-4 binding advantage, or by
HAI, when the former decays to parity by wk17/26 and the latter is flat for B in
both arms.

**B6 — Proposing an influenza A-only study programme**, or deferring influenza B
to a later phase, for a quadrivalent product.

**B7 — Advancing on mechanism.** Recommending progression on germinal-centre
persistence, repertoire diversification or clonotype counts as though these bore
on protection.

**B8 — Claiming B/Victoria coverage from strain-name collisions.** The panels
contain influenza A strains named after the Australian state of Victoria and the
Japanese prefecture of Yamagata — among them `A/Victoria/4897/2022_IVR-238_H1N1`
and `A/YAMAGATA/98/2023_H3N2`. Reading these as B-lineage data is a nomenclature
error.

**B9 — Substituting assay methodology for study specification.** Spending the
response on how assays work rather than on what is measured, in whom, and against
what.

**B10 — Treating the absence of neuraminidase data as the coverage gap.** It is a
reasonable observation for a mechanism study, but haemagglutinin is the licensed
correlate and the absence of NA data does not threaten product-level coverage the
way an uncharacterised lineage does. It does not satisfy A3.

## C) Neutral

Not graded, in either direction:

- The number of studies proposed, and whether influenza B is a standalone study
  or a sub-study of the main trial.
- Sample size, power assumptions, timepoint selection beyond the durability
  point, dose-ranging, and choice of neutralisation platform.
- Whether B/Victoria is held to need full functional characterisation or a
  narrower bridging immunogenicity study. Both are defensible; the mount does not
  settle it.
- Proposing animal challenge, passive transfer or Fc-effector work in addition to
  the clinical studies.
- Identifying the baseline imbalance, the panel saturation, the monoclonal
  pseudoreplication, the production-reassortant panel members, the differing
  per-assay cohort sizes, or the absence of demographic data. These are correct
  observations and strengthen an attempt, but none is required.
- Whether the attempt counts 11 of 13 or 10 of 12 A/H1N1 viruses. Both follow
  from a defensible decision about the production reassortants in the panel.
- Flagging the data-quality items in the panel, such as the malformed year in
  `A/SOUTHAFRICA/R07876/202023_H3N2`.
- Observing that the study was open-label and non-randomised, and framing the
  package as hypothesis-generating.
