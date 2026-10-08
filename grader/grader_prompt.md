# WU397 — mRNA seasonal influenza vaccine: next-study design

## Task framing

The attempt receives a working directory holding the complete source data from a
single immunogenicity study of a quadrivalent mRNA seasonal influenza vaccine
(mRNA-1010) against a licensed quadrivalent comparator (Fluarix), 2022–2023
Northern Hemisphere season. It is asked to recommend the next studies, and for
each to specify what is measured, in whom, and against what, sufficient to
support a heterologous-protection claim.

**Deliverable set to inspect.** `/tmp/outputs/answer.md`, carrying a one-line
recommendation at the top, then the recommended studies, then the reasoning with
every number traced to its file. Any analysis scripts or intermediate files saved
under `/tmp/outputs`.

The number of studies proposed is not graded. One well-specified trial plus an
influenza B characterisation study, and a three-to-four study programme covering
the same ground, earn the same. What is graded is whether the three commitments
under A are made and correctly grounded.

**Accounting rules.**

- A result counts as correct only where the value is right **and** the basis
  given produces it. A correct number with a derivation that does not yield it is
  not a correct result.
- Where the task asks which items qualify — which subtype carries the readout,
  which antigens lack functional data — the membership is the result. Naming the
  right subtype among a list of candidates is not the same as committing to it.
- Prose that disagrees with the submission's own tables establishes nothing.
- A carried-forward error is penalised once, where it enters the chain. An error
  entering at two independent points is two errors.
- Impartial between methods. No verbosity penalty, in either direction.

**The commitment is required, and it is scored on the recommendation itself** —
the one-line summary plus the study specifications, not on hedges elsewhere in
the document. An attempt that recommends powering on A/H3N2 and later remarks
that A/H1N1 also separates has recommended A/H3N2.

**The dominant failure** is treating the bead-array binding result as the
protection signal, and recommending A/H3N2 on the strength of it. The second
most common is inventorying the influenza B absence without proposing work to
close it.

## Bridge line

Start with the Golden Response for WU397 — mRNA seasonal influenza vaccine:
next-study design above as your benchmark. This is an example of a correct answer
for this task.

## Golden Response

**Recommendation.** Power the heterologous-protection readout on A/H1N1 against
contemporary and forward-drift isolates with a durability co-primary, and run a
B/Victoria functional characterisation study in parallel — the package
establishes broader binding, not broader protection, and generates no functional
data at all for half the formulation.

### Study 1 — heterologous protection, A/H1N1

**What is measured.** Neutralisation titre against a pre-locked panel of
contemporary and forward-drift A/H1N1 clinical isolates. Co-primary endpoints at
day 29 and at day 181 or later. Haemagglutination inhibition retained as a
regulatory bridge, not as the primary functional readout.

**In whom.** Adults, randomised and observer-blind, stratified on
pre-vaccination titre and on birth cohort.

Baseline stratification is required. In `neutralization_seqbased.csv` the
mRNA-1010 arm starts lower on A/H3N2 (day 0 GMT 185 vs 278) and in
`microneutralization.csv` on the heterologous panel (week 0 GM 57.0 vs 121.3);
baseline anti-correlates with fold-rise. An unstratified fold-rise endpoint
therefore flatters whichever arm enrolled lower.

Birth-cohort stratification follows from the H1/H3 asymmetry below, which is the
pattern immune imprinting would produce. No age or birth year appears anywhere in
the mount, so the held data cannot test it.

**Against what.** Wild-type clinical isolates post-dating the 2022–2023
composition named in `trial_summary.md`. Egg- and cell-propagated production
reassortants excluded — the panel in `neutralization_seqbased.csv` contains five,
identifiable by their reassortant designations (`IVR-238`, `NIB-88`, `X-307A`,
`X-223A`, an `egg` suffix).

**Why A/H1N1 carries this readout.** In `neutralization_seqbased.csv`, per-virus
Mann-Whitney on log2 fold-change (day 29 over day 0) with Benjamini-Hochberg
correction applied within each subtype panel separates the arms on **11 of 13**
A/H1N1 viruses, median delta **+1.32 log2**. The two non-significant viruses are
the two oldest in the panel — A/Michigan/45/2015 and A/Brisbane/02/2018 — and
**6 of the 11** significant viruses are 2023 isolates post-dating the vaccine
composition.

The gain scales with antigenic distance rather than being a uniform potency
shift: regressing per-virus arm advantage on distance gives a positive slope for
H1N1 and a negative one for H3N2. This is what distinguishes a strain-coverage
gain from a potency gain, and it is why the panel must be contemporary and
forward-drift rather than a historical series.

**Why the durability co-primary.** The functional advantage does not persist.
Participant-level A/H1N1 GMT across wild-type panel viruses is 883.7 vs 501.4 at
day 29 (ratio 1.76) and 402.5 vs 315.9 at day 181 (ratio 1.27). Waning from day
29 to day 181 is **2.13-fold in the mRNA arm against 1.24-fold in the comparator,
p = 0.0022** — the most statistically secure between-arm result in the package,
and it is unfavourable.

Note that the binding readout points the other way: ELISA fold-change at wk17/26
in `elisa_igg_titers.csv` is 2.12 vs 1.40, p = 0.0001. The binding and functional
durability signals disagree, and a protection claim is governed by the functional
one. A day-29-only design would support a claim that has decayed before the end
of a single season.

### Study 2 — B/Victoria functional characterisation

**What is measured.** Neutralisation against a B/Victoria panel, plus the
characterisation that already exists for the A subtypes: a binding-breadth panel
and monoclonal antibody isolation.

**In whom.** The same adult population. This may run as a sub-study of Study 1 or
standalone.

**Against what.** Contemporary B/Victoria isolates, including drift variants
post-dating B/Austria/1359417/2021.

**Why this is a prerequisite and not an addition.** The product is quadrivalent —
`trial_summary.md` names four antigens, two of them influenza B. Across the whole
mount, influenza B appears only in `elisa_igg_titers.csv`, `hai_titers.csv` and
`igm_fold_change.csv`. The functional assays are influenza A only:

| File | Antigens | Influenza B |
|---|---|---|
| `neutralization_seqbased.csv` | 13 H1N1 + 83 H3N2 viruses | none |
| `binding_breadth_h1.csv` | 9 H1 strains | none |
| `binding_breadth_h3.csv` | 12 H3 strains | none |
| `microneutralization.csv` | 2 A strains | none |
| `mab_binding_panels.csv` | 2 panels, ~340 and ~385 monoclonals | none |

The binding data that do exist for B/Victoria do not support a claim. The
advantage is significant at week 4 (GM fold-change 3.16 vs 2.30, p = 0.0146) and
absent by wk17/26 (**1.57 vs 1.56, p = 0.8363**), while both A subtypes hold
theirs at that same timepoint (A/H1 2.12 vs 1.40; A/H3 3.47 vs 1.52). HAI is flat
for influenza B in both arms (B/Vic week 4 fold-change 1.08 vs 1.05, p = 0.675),
so it supports no endpoint either way.

B/Yamagata is out of scope: it has not circulated since 2020 and has been removed
from seasonal formulations. The live influenza B question is B/Victoria.

### Study 3 — resolving the A/H3N2 binding-versus-function dissociation

**What is measured.** Whether the additional H3 binding is functional at all:
stem-competition and epitope mapping, Fc-effector readouts, neuraminidase
inhibition, and heterosubtypic neutralisation rather than binding alone. Passive
transfer and heterologous challenge in a pre-immune animal model, interpreted as
protection per unit neutralising titre.

**Why A/H3N2 cannot carry a protection readout as it stands.** Bead-array binding
in `binding_breadth_h3.csv` separates the arms on **12 of 12** H3 strains, median
delta **+2.30 log2**. Sequencing-based neutralisation separates on **0 of 83**
H3N2 viruses after within-panel correction, at the same n per arm that detected
11 of 13 in H1N1 — so this is not an underpowering result.

On the five H3 strains measured by both methods, all five are
binding-significant, none is neutralisation-significant, and the per-strain effect
sizes are uncorrelated (r = +0.10). On the homologous H3 vaccine strain
A/Darwin/6/2021, binding is **+2.07 log2** while neutralisation is **−0.27**.

Separately, neither binding panel contains a strain later than 2022, so both
measure back-boost against historical strains rather than forward drift and
cannot support a forward-looking claim in principle.

### What the package does not support

**Haemagglutination inhibition, the licensed correlate, separates nothing.**
A/H1N1 week 4 fold-change 2.76 vs 2.25 (p = 0.26); A/H3N2 1.72 vs 1.66
(p = 0.69).

**Conventional microneutralisation is flat** and numerically favours the
comparator on the homologous strain — week 4 fold-change GM 2.49 vs 3.32
(p = 0.53). Heterologous is 4.12 vs 3.03 (p = 0.32), confounded by the baseline
deficit noted above.

**Molecular and mechanistic readouts** — germinal-centre persistence, repertoire
diversification, clonotype counts, single-cell annotations — support a mechanism,
not a protection claim, and rest on small subsets. The lymph-node cohort in
`gc_frequencies.csv` is 2 mRNA-1010 against 11 Fluarix participants, and
`pb_gc_clonal_overlap.csv` covers 7 donors. The monoclonal panels are
pseudoreplicated across those same 7 donors, so per-monoclonal percentages
overstate the evidence; `group_I` runs opposite to `group_II`.

**Correcting across all 96 viruses at once** extinguishes the H1N1 signal
(11 → 0, nothing surviving) and makes the subtypes look equivalent. The panels
are two separate libraries of 13 and 83 viruses; correction belongs within each.

**Normalising heterologous titre to each participant's own vaccine-strain titre**
makes A/H3N2 appear to separate, but the effect is a smaller denominator: at
A/Darwin/6/2021 the mRNA arm responded less well than the comparator. Such an
endpoint rewards an arm for failing against the strain in its own vaccine.

## A) MUST BE PRESENT AND CORRECT

**A1. The heterologous-protection readout is powered on A/H1N1.** The attempt
names A/H1N1 as the subtype carrying a functional endpoint and grounds it in
`neutralization_seqbased.csv` — the per-virus neutralisation result, 11 of 13
within panel (10 of 12 excluding production reassortants is the same finding) —
rather than in any binding readout. Treating the two A subtypes as
interchangeable, or leaving the subtype unspecified, does not satisfy A1.

**A2. The strain set is contemporary and forward-drift H1N1 isolates.** The
attempt specifies a panel of isolates contemporary with or post-dating the
2022–2023 composition rather than a historical strain series. Any of these
groundings counts: the 2023 isolates among the significant viruses in
`neutralization_seqbased.csv`; the drift-distance gradient in that same file; or
that neither binding panel (`binding_breadth_h1.csv`, `binding_breadth_h3.csv`)
contains a strain later than 2022 and so cannot speak to forward drift. The attempt need not assert that
the two non-significant viruses prove drift-specificity — that reading is weaker
than the gradient and is not required.

**A3. Influenza B coverage is treated as a prerequisite.** The attempt
establishes that the functional assays generate no influenza B data of any kind,
draws the consequence that a quadrivalent product claim cannot rest on influenza
A data alone, and specifies a study or sub-study producing B/Victoria functional
data.

A3 is satisfied only when the consequence is drawn and converted into proposed
work. Listing influenza B among absent assays, without proposing anything to
close it, does not satisfy A3 — this is the single most common way a strong
attempt fails. Scoping B/Yamagata out as no longer circulating is correct and
must not be read as an omission.

Any grounding for A3 counts: the file-by-file inventory showing influenza B
present only in `elisa_igg_titers.csv`, `hai_titers.csv` and `igm_fold_change.csv`
and absent from every functional file (`neutralization_seqbased.csv`,
`binding_breadth_h1.csv`, `binding_breadth_h3.csv`, `microneutralization.csv`,
`mab_binding_panels.csv`); the decay of the B/Vic binding advantage in
`elisa_igg_titers.csv` to parity by wk17/26 (1.57 vs 1.56) while both A subtypes
hold theirs; or the observation that the two influenza B antigens named in
`trial_summary.md` never appear in a functional file.
The attempt need not use the word "quadrivalent".

## B) PENALIZE FOR

**B1. Powering the protection readout on the bead-array binding result.**
Selecting A/H3N2 because binding breadth is largest there (12 of 12 strains,
median +2.30 log2), when `neutralization_seqbased.csv` shows 0 of 83 H3N2 viruses
separating at the same n per arm that detected 11 of 13 in H1N1.

**B2. A multiplex-binding primary endpoint.** Proposing bead-array or ELISA
binding as the primary readout for a protection claim, or citing the 12-of-12
result as evidence of protective strain coverage, without confronting the
neutralisation nulls or the A/Darwin/6/2021 dissociation (+2.07 binding against
−0.27 neutralisation).

**B3. Reading the 83 H3N2 nulls as underpowering.** Recommending a larger H3N2
neutralisation study as the protection trial on the grounds that n = 13/14 was
too small, when that same n detected 11 of 13 in H1N1.

**B4. Correcting for multiplicity across all 96 viruses at once** and concluding
that neither subtype has functional support. The pooled correction is a
multiplicity artefact across two separate libraries of 13 and 83 viruses.

**B5. Treating the week-4 influenza B binding advantage as coverage.** Citing
p = 0.0146 at week 4 as evidence B is characterised, when the same comparison is
p = 0.8363 at wk17/26.

**B6. Treating HAI as influenza B coverage.** HAI is flat for B in both arms, so
it supports no endpoint in either direction.

**B7. Treating B/Victoria as deferrable to a future seasonal update rather than
as an open question in the current package.** Recommending that the influenza B
component be addressed through later strain-composition changes, or sequenced
behind the influenza A programme as a lower priority, on the implied basis that
it is adequately covered — when no functional B data exist anywhere in the mount
and the binding advantage that does exist is gone by wk17/26 (1.57 vs 1.56,
p = 0.8363).

**B8. Advancing on mechanism.** Recommending progression on germinal-centre
persistence, repertoire diversification or clonotype counts as though these bore
on protection. These are mechanistic, rest on a 2-versus-11 lymph-node cohort and
7 donors, and carry no protection weight.

**B9. Reading strain-name collisions as influenza B data.** The panels contain
influenza A strains named after the Australian state of Victoria and the Japanese
prefecture of Yamagata — among them `A/Victoria/4897/2022_IVR-238_H1N1`,
`A/Victoria/1389/2023_H1N1` and `A/YAMAGATA/98/2023_H3N2`. Reading any of these
as B-lineage coverage is a nomenclature error. The actual B antigens named in
`trial_summary.md` are B/Austria/1359417/2021 and B/Phuket/3073/2013, and neither
appears in any functional file.

**B10. Normalising heterologous titre to the participant's own vaccine-strain
titre** and reporting the resulting A/H3N2 separation as a real effect. The
signal is a smaller denominator — the mRNA arm responded less well at
A/Darwin/6/2021 — so the endpoint rewards an arm for failing against the strain
in its own vaccine.

**B11. Substituting assay methodology for study specification.** Spending the
response on how assays work rather than on what is measured, in whom, and against
what. The prompt asks for conditions and readouts.

**B12. Offering the absence of neuraminidase data as the coverage gap.** It is a
reasonable observation for a mechanism study, but haemagglutinin is the licensed
correlate and no NA absence threatens product-level coverage the way an
uncharacterised lineage does. It does not satisfy A3.

**B13. Unsupported assertion.** A number, p-value or claim with no derivation, or
whose inputs do not exist in the mount. Penalised in its own right, whether or
not the value is correct.

## C) NEUTRAL

Not graded, in either direction.

1. The number of studies proposed, and their ordering.
2. Whether B/Victoria is a standalone study or a sub-study of the main trial.
3. Whether B/Victoria is held to need full functional characterisation or a
   narrower bridging immunogenicity study. Both are defensible; the mount does
   not settle it.
4. Sample size and power assumptions, and whether any are offered at all.
5. Timepoint selection beyond the durability co-primary — day 181, day 271, day
   365 all count.
6. Choice of neutralisation platform: sequencing-based, conventional
   microneutralisation, pseudovirus, or focus-reduction.
7. Whether HAI is retained as a regulatory bridge, dropped, or not mentioned.
8. Dose-ranging, schedule, prime-boost or adjuvant arms.
9. Proposing animal challenge, passive transfer, or Fc-effector work alongside
   the clinical studies.
10. Proposing neuraminidase, T-cell or mucosal readouts as additions, provided
    they are not offered in place of A3.
11. Whether birth-cohort or imprinting stratification is proposed.
12. Whether the absence of demographic data is noticed.
13. Identifying the baseline imbalance, and whether a covariate-adjusted
    analysis is proposed to handle it.
14. Noticing the panel saturation — effectively all panel viruses neutralised at
    the lowest dilution in both arms — and rejecting a seroprotection endpoint
    on those grounds.
15. Noticing the monoclonal pseudoreplication across 7 donors.
16. Excluding or retaining the five production reassortants in the panel.
17. Counting 11 of 13 or 10 of 12 A/H1N1 viruses. Both follow from a defensible
    decision about the reassortants.
18. Noticing the three differing per-assay cohort sizes — binding antibody 75,
    HAI 29, sequencing-based neutralisation 27.
19. Rejecting `gc_frequencies.csv` or any mechanistic file as unusable, or
    using it descriptively while declining to draw a comparative claim.
20. Flagging data-quality items such as the malformed year in
    `A/SOUTHAFRICA/R07876/202023_H3N2`.
21. Observing that the study was open-label and non-randomised, and framing the
    package as hypothesis-generating rather than claim-supporting.
22. Whether the attempt frames its headline as "do not take this to committee"
    or as "here is what the next studies must show". Both are responsive.
23. Statistical choices: Mann-Whitney against t-test on log titres, exact
    against asymptotic, median against geometric-mean summaries, and whether
    multiplicity correction is applied to the binding panels.
24. Whether the H1N1 gain is characterised as a strain-coverage gradient, as a
    potency shift, or as both, provided the recommended panel is still
    contemporary and forward-drift.
25. Whether the adverse waning result is reported as a fold-ratio, a retention
    fraction, or a slope.
26. Language, tooling, file layout and presentation of saved analysis.
27. Omitting Study 3. Resolving the A/H3N2 dissociation is correct work the
    prompt does not require; the deliverable fully answers the prompt without
    it.
28. Omitting any number the Golden Response carries that is not needed to
    establish A1, A2 or A3.
29. Length, section ordering, and whether studies are numbered or named.

**Equivalent methods.** Any route that establishes the same claims from the
mounted files earns what the Golden Response's route earns. The Golden Response
uses per-virus Mann-Whitney with within-panel Benjamini-Hochberg correction and
participant-level geometric means; a mixed model over the panel, a
covariate-adjusted analysis of day-29 titre, a permutation test, or a
distance-regression approach all count where they establish A1, A2 and A3 from
the same files.
