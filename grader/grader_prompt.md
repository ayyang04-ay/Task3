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

References below to "the trial summary" mean the summary document mounted in the
input folder, which carries the study design, the antigenic composition, the
per-assay cohort table and the identifier conventions. Its mounted filename may
carry an upload suffix; cite it as the attempt found it, and do not treat a
filename difference as evidence the file was not read.

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
establishes broader binding, not broader protection, and for half the
formulation it generates no neutralisation or characterisation data at all and
only a flat HAI result.

### Study 1 — heterologous protection, A/H1N1

**What is measured.** Neutralisation titre against a pre-locked panel of
contemporary and forward-drift A/H1N1 clinical isolates. Co-primary endpoints at
day 29 and at a durability timepoint covering the influenza season (~4–6 months
post-dose; day 121 or day 181). Haemagglutination inhibition retained as a
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
composition named in the trial summary. Egg- and cell-propagated production
reassortants excluded — the panel in `neutralization_seqbased.csv` contains six,
identifiable by their reassortant designations (`IVR-238` on the one H1N1 strain;
`NIB-88`, `X-307A`, `X-223A` and two `egg`-suffixed strains on H3N2).

**Why A/H1N1 carries this readout.** In `neutralization_seqbased.csv`, per-virus
Mann-Whitney on log2 fold-change (day 29 over day 0) with Benjamini-Hochberg
correction applied within each subtype panel separates the arms on **11 of 13**
A/H1N1 viruses, median delta **+1.32 log2**. The two non-significant viruses are
A/Michigan/45/2015 and A/Brisbane/02/2018; the oldest isolate in the panel,
A/California/07/2009, is itself significant (q = 0.036), so the separation is not
a simple old-versus-new split. **6 of the 11** significant viruses are 2023
isolates post-dating the vaccine composition.

The advantage is broadly uniform across the panel rather than concentrated in the
contemporary strains: the median per-virus delta on the 2023 isolates is
essentially the same as on the pre-2023 ones, so this is a potency gain across
the subtype and not a drift gradient. It nonetheless extends to the 2023 isolates
that post-date the composition, and that is why the panel must be contemporary
and forward-drift rather than a historical series: a forward-looking claim has to
be demonstrated against forward-drifted strains, and neither bead-array breadth
panel contains a strain later than 2022. No antigenic-distance field is mounted, so
this rests on isolation date, not a computed distance.

**Why the durability co-primary.** The functional advantage does not persist.
Participant-level A/H1N1 GMT across wild-type panel viruses is 883.7 vs 501.4 at
day 29 (ratio 1.76) and 402.5 vs 315.9 at day 181 (ratio 1.27). Waning from day
29 to day 181 is **2.13-fold in the mRNA arm against 1.24-fold in the comparator,
p = 0.0022** — significant, and unfavourable to the investigational arm.

Those waning figures are per-participant geometric-mean folds: for each
participant, the geometric-mean titre across the wild-type panel viruses at each
timepoint, then that participant's day-29-over-day-181 ratio, then the geometric
mean of those ratios within arm. Taking the ratio of the two arm-level GMTs
quoted above instead gives 2.20-fold and 1.59-fold. Both reductions are
defensible and both show the same direction; an attempt that reaches either pair
by a stated route has the result right.

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
the trial summary names four antigens, two of them influenza B. Across the whole
mount, influenza B appears only in `elisa_igg_titers.csv`, `hai_titers.csv` and
`igm_fold_change.csv`. The functional assays are influenza A only:

| File | Antigens | Influenza B |
|---|---|---|
| `neutralization_seqbased.csv` | 13 H1N1 + 83 H3N2 viruses | none |
| `binding_breadth_h1.csv` | 9 H1 strains | none |
| `binding_breadth_h3.csv` | 12 H3 strains | none |
| `microneutralization.csv` | 2 panels, named only `homologous`/`heterologous` | not identifiable |
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
inhibition, and neutralisation against drifted H3 isolates rather than binding
alone. Passive
transfer and heterologous challenge in a pre-immune animal model, interpreted as
protection per unit neutralising titre. This orthogonal pairing — in-vitro
neutralisation plus in-vivo protection — is what substantiates a
heterologous-protection claim; HAI tracks only matched strains and a binding
readout cannot carry it.

**Why A/H3N2 cannot carry a protection readout as it stands.** Bead-array binding
in `binding_breadth_h3.csv` separates the arms on **12 of 12** H3 strains, median
delta **+2.30 log2**. Sequencing-based neutralisation separates on **0 of 83**
H3N2 viruses after within-panel correction. There is therefore no functional H3
signal in the package to carry a protection endpoint: the large H3 effect that
does exist is a binding effect, and the one functional readout that has been run
against these viruses finds nothing. A larger H3N2 neutralisation study might
yet detect something, but that is a hypothesis to be generated, not a protection
trial to be powered — the effect it would be powered to find has no estimate in
the package at all.

On the six H3 strains measured by both methods, all six are
binding-significant, none is neutralisation-significant, and the per-strain effect
sizes are uncorrelated (r = −0.22). On A/Darwin/6/2021, mRNA-1010's own H3
component, binding is **+2.07 log2** while neutralisation is **−0.27**.

Separately, neither bead-array breadth panel — `binding_breadth_h1.csv` or
`binding_breadth_h3.csv` — contains a strain later than 2022, so both measure
back-boost against historical strains rather than forward drift and cannot
support a forward-looking claim in principle.

### What the package does not support

**Haemagglutination inhibition, the licensed correlate, separates nothing.**
A/H1N1 week 4 fold-change 2.76 vs 2.25 (p = 0.26); A/H3N2 1.72 vs 1.66
(p = 0.69).

**Conventional microneutralisation is flat** and numerically favours the
comparator on the homologous panel — week 4 fold-change GM 2.49 vs 3.32
(p = 0.53). Heterologous is 4.12 vs 3.03 (p = 0.32), confounded by the baseline
deficit noted above.

**Molecular and mechanistic readouts** — germinal-centre persistence, repertoire
diversification, clonotype counts, single-cell annotations — support a mechanism,
not a protection claim, and rest on small subsets. The lymph-node cohort in
`gc_frequencies.csv` is 6 mRNA-1010 against 11 Fluarix participants, and
`pb_gc_clonal_overlap.csv` covers the same 7 donors as the monoclonal panels,
four in one arm and three in the other. Either way the mechanistic files carry no protection weight
(B8, C19). The monoclonal panels are
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

An A item is met only where the attempt's own grounding, traced to a mounted
file, establishes it. The prompt requires the reasoning, every number relied on
and where each came from; a commitment asserted with no such grounding is not
met, however correct the recommendation reads.

A commitment whose grounding contradicts the mounted files, or contradicts the
attempt's own saved analysis, is not met for the same reason: a derivation that
does not produce the value it is offered as producing has established nothing.
So where the figures an A item rests on are not reproducible from the files **by
the route the attempt states**, that item is not met even though the
recommendation it supports is the correct one — and an attempt whose A1 to A3
figures are all of that kind has grounded none of the three.

A different but stated route reaching different figures is not this case. It is
the equivalent-methods case: any route that establishes the same claims from the
mounted files earns what the Golden Response's route earns, and a count that
differs because the attempt chose a different test is governed by C17 and C23,
not by this paragraph. What is at issue here is only whether the commitment was
established; B13 and B16 record the unsupported assertion and the misstated
derivation in their own right.

This is the value-and-basis accounting rule applied to the A items, not a
judgement about how grave any one miss is.

**A1. The heterologous-protection readout is powered on A/H1N1.** The attempt
names A/H1N1 as the subtype carrying the functional endpoint and grounds it in
`neutralization_seqbased.csv` — the per-virus neutralisation result, 11 of 13
within panel (10 of 12 excluding production reassortants is the same finding) —
rather than in any binding readout.

A1 is scored on the recommended **primary** endpoint, not on hedges elsewhere.
The test: **if A/H3N2 fails, does the A/H1N1 claim still stand on its own?** If
the A/H1N1 result survives as a claim in its own right, the design has committed
to A/H1N1 and A1 is met; if a negative A/H3N2 result takes the A/H1N1 claim down
with it, or if the design would read the same way had A/H1N1 been the subtype
that failed, it has not committed and A1 is not met. This is a scientific
judgement, not a prompt-vagueness one — the package shows A/H3N2 at 0 of 83 on
neutralisation, so a design that stakes the primary on H3N2 stakes it on a
readout the data already show is dead.

How specific designs are judged:

| Recommended primary design | A1 |
|---|---|
| A/H1N1 the sole functional primary | MET |
| A/H1N1 primary, A/H3N2 explicitly secondary or gated (tested only if H1N1 wins) | MET |
| Equal co-primaries on both A subtypes | NOT MET |
| Two primaries tested hierarchically, A/H1N1 first, its claim standing alone if A/H3N2 fails | MET |
| A single pooled multi-subtype primary panel | NOT MET |
| A/H3N2 first, or H3N2 co-equal with H1N1 | NOT MET |
| A "≥2-of-3 families" or "at least one A subtype" go rule | NOT MET |
| Subtype left unspecified, or the two A subtypes treated as interchangeable | NOT MET |

The table is read on the testing structure, not on the label an attempt uses.
"Equal co-primaries" means the two endpoints share the alpha and programme
success requires both, with no testing hierarchy between them — a design that
stakes success on a readout the package shows at 0 of 83, and that spends
type-I error budget protecting it at the expense of the one endpoint that
separates. An attempt that writes "co-primary" but describes a hierarchical or
gatekeeping procedure, under which the A/H1N1 claim stands on its own if
A/H3N2 fails, is judged under the gated row above and is MET.

Proposing A/H3N2 work alongside a committed A/H1N1 primary is not penalised
here or anywhere (C9, C10). What A1 tests is whether programme success is
gated on the dead readout.

Naming A/H1N1 as the only functional signal in the analysis and then proposing
one of the NOT-MET structures as the recommendation does not satisfy A1 — the
commitment is the recommendation, not the analysis.

That clause runs one way only. The table resolves which testing structures can
satisfy A1; it does not discharge the grounding requirement in the preamble to
this section, which applies to A1 independently. A recommendation sitting in a
MET row still fails A1 where the per-virus neutralisation figures it rests on
are not reproducible by the route the attempt states.

**A2. The strain set is contemporary and forward-drift H1N1 isolates.** The
attempt specifies a panel of isolates contemporary with or post-dating the
2022–2023 composition rather than a historical strain series. Any of these
groundings counts: the 2023 isolates among the significant viruses in
`neutralization_seqbased.csv`; or
that neither binding panel (`binding_breadth_h1.csv`, `binding_breadth_h3.csv`)
contains a strain later than 2022 and so cannot speak to forward drift. The
attempt need not assert that the two non-significant viruses prove
drift-specificity, and need not characterise the H1N1 gain as drift-specific at
all — the gain is uniform across the panel, and reading it as a potency shift is
correct (C24). What A2 requires is the contemporary and forward-drift panel,
which follows from the forward-looking claim and the 2022 ceiling on the
mounted panels rather than from any gradient.

**A3. Influenza B coverage is treated as a prerequisite.** The attempt
establishes that no B/Victoria neutralisation or characterisation data
exist, draws the consequence that a quadrivalent product claim cannot rest on
influenza A data alone, and specifies a study or sub-study with a B/Victoria
functional endpoint of its own.

"Functional" here means a neutralisation, inhibition or in-vivo protection
readout — not bead-array or ELISA binding. HAI is the one functional assay in the
package that includes influenza B (`hai_titers.csv`), and it is flat for B/Vic in
both arms (week-4 fold-change 1.08 vs 1.05, p = 0.675), so it establishes no B
coverage either way; an attempt that says exactly this is correct, not in error.

A3 is satisfied only when the consequence is drawn and converted into proposed
work carrying a B/Victoria-specific functional endpoint. Two things do not
satisfy A3: listing influenza B among absent assays without proposing anything to
close it (the single most common way a strong attempt fails); and writing
B/Victoria isolates into a panel whose endpoint is defined around A/H1N1 with no
B-specific readout — that is cosmetic coverage, not characterisation. B/Victoria
is one of the four antigens the product encodes, so its coverage must be
justified in its own right. Scoping B/Yamagata out as no longer circulating is
correct and must not be read as an omission.

Any grounding for A3 counts: the file-by-file inventory showing influenza B
absent from the panels that name their antigens
(`neutralization_seqbased.csv`, `binding_breadth_h1.csv`, `binding_breadth_h3.csv`,
`mab_binding_panels.csv`) and present only as titres in
`elisa_igg_titers.csv`, `hai_titers.csv` and `igm_fold_change.csv` — the one
functional assay among these, HAI, being flat for B/Vic; the decay of the B/Vic
binding advantage in `elisa_igg_titers.csv` to parity by wk17/26 (1.57 vs 1.56)
while both A subtypes hold theirs; or the observation that the two influenza B
antigens named in the trial summary never appear in a neutralisation or
characterisation file. The attempt need not use the word "quadrivalent".

## B) PENALIZE FOR

**B1. Powering the protection readout on the bead-array binding result.**
Selecting A/H3N2 because binding breadth is largest there (12 of 12 strains,
median +2.30 log2), when `neutralization_seqbased.csv` shows 0 of 83 H3N2 viruses
separating on the one functional assay run against them, while the same file
shows 11 of 13 in H1N1.

**B2. A multiplex-binding primary endpoint.** Proposing bead-array or ELISA
binding as the primary readout for a protection claim, or citing the 12-of-12
result as evidence of protective strain coverage, without confronting the
neutralisation nulls or the A/Darwin/6/2021 dissociation (+2.07 binding against
−0.27 neutralisation).

**B3. Powering the protection trial on A/H3N2 by treating the 83 nulls as a
sample-size problem.** Recommending a larger H3N2 neutralisation study *as the
heterologous-protection trial*, on the grounds that the nulls reflect n rather
than absence of effect. The package contains no functional H3 effect estimate to
power against: 0 of 83 viruses separate, and the large H3 signal that does exist
is a binding signal the neutralisation data contradict at A/Darwin/6/2021 (+2.07
binding against −0.27 neutralisation).

B3 fires on the *recommendation*, not on the observation. Noting that the H3N2
nulls are an absence of evidence rather than evidence of absence, that the
confidence intervals are wide, that a smaller true H3 effect would not have been
detected at this n, or proposing a larger H3N2 neutralisation study as
exploratory or hypothesis-generating work alongside an A/H1N1 primary, is correct
scientific reasoning and is not penalised. What is penalised is staking the
protection readout on it.

**B4. Correcting for multiplicity across all 96 viruses at once.** The 13
A/H1N1 and 83 A/H3N2 viruses are two separately assembled libraries screened for
two different questions, so one correction spanning both controls error over a
family no programme is asking about, and the 83 largely null A/H3N2 tests set
the threshold for the 13 A/H1N1 ones. The A/H1N1 count falls from 11 to 0 on the
pooling alone. Penalised where the pooled correction is the basis offered for
the verdict, most often paired with the conclusion that neither subtype has
functional support. Reporting the pooled result alongside the within-panel
result, with the choice of family reasoned through, is not B4 — nor is any other
test, which C23 and the equivalent-methods clause leave open.

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
on protection. These are mechanistic, rest on a 6-versus-11 lymph-node cohort and
7 donors, and carry no protection weight.

**B9. Reading strain-name collisions as influenza B data.** The panels contain
influenza A strains named after the Australian state of Victoria and the Japanese
prefecture of Yamagata — among them `A/Victoria/4897/2022_IVR-238_H1N1`,
`A/Victoria/1389/2023_H1N1` and `A/YAMAGATA/98/2023_H3N2`. Reading any of these
as B-lineage coverage is a nomenclature error. The actual B antigens named in
the trial summary are B/Austria/1359417/2021 and B/Phuket/3073/2013, and neither
appears in any functional file.

**B10. Normalising heterologous titre to the participant's own vaccine-strain
titre** and reporting the resulting A/H3N2 separation as a real effect. The
signal is a smaller denominator — the mRNA arm responded less well at
A/Darwin/6/2021 — so the endpoint rewards an arm for failing against the strain
in its own vaccine.

**B11. The study specification is missing.** A recommended study is offered
without specifying what is measured, in whom, and against what. The prompt
requires these three for each study it asks for, so their absence is the error —
whatever the response spent its space on instead, and whether or not the gap is
filled by methodological material. Where the specification is present, what else
the response carries is not scored here (C30).

**B12. Offering the absence of neuraminidase data as the coverage gap.** It is a
reasonable observation for a mechanism study, but haemagglutinin is the licensed
correlate and no NA absence threatens product-level coverage the way an
uncharacterised lineage does. It does not satisfy A3.

**B13. Unsupported assertion.** A number, p-value or claim with no derivation, or
whose inputs do not exist in the mount. Penalised in its own right, whether or
not the value is correct.

**B14. A day-29-only functional primary.** Recommending a protection readout with
no durability timepoint reaching roughly the length of an influenza season (~4–6
months post-dose; day 121 or day 181), when the package shows the A/H1N1
functional advantage waning 2.13-fold against 1.24-fold in the comparator from
day 29 to day 181 (p = 0.0022; per-participant geometric-mean folds — 2.20-fold
against 1.59-fold on the arm-GMT reduction, same direction) — a day-29-only
design backs a claim the data show
has already decayed within one season. Including a durability timepoint at or
beyond ~4–6 months avoids B14; its exact value beyond that is neutral (C5).

**B15. Discarding the A/H1N1 neutralisation result as confounded by vaccine
composition.** Treating the arms as non-comparable on A/H1N1, and so declining to
power on it, on the grounds that the two products' antigens differ. The trial
summary assigns the same A(H1N1)pdm09 component to both arms and records the
difference as H3N2 only, so the confound does not apply to the subtype the
result rests on. The mounted data refute it independently: the per-virus gain is
uniform across the 13-virus panel and largest on A/Wisconsin/588/2019 (+1.61
log2), the stated H1 component itself, where a newer-antigen explanation
predicts the opposite. Questioning the comparator's stated formulation is
neutral (C31); using that question to set the A/H1N1 result aside is not.

**B16. A stated derivation that does not produce the value it is offered as
producing.** A figure given with a named file and a described route, where
recomputing by that route yields a materially different value. This is distinct
from B13, which covers an assertion carrying no derivation at all or whose
inputs do not exist in the mount; here the derivation is stated and simply does
not yield the number. Whether the commitment the figure supports still stands is
governed by the preamble to section A; this item records the misstatement
itself, once per independent point at which it enters.

## C) NEUTRAL

Not graded, in either direction.

1. The number of studies proposed, and their ordering.
2. Whether B/Victoria is a standalone study or a sub-study of the main trial.
3. The scale of the B/Victoria work — full functional characterisation or a
   narrower bridging study. Both are defensible and the mount does not settle
   it. The readout is not neutral in the same way: A3 still requires a
   functional B/Victoria endpoint, so a narrower study satisfies A3 only if it
   carries one.
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
16. Excluding or retaining the six production reassortants in the panel.
17. Counting 11 of 13 or 10 of 12 A/H1N1 viruses. Both follow from a defensible
    decision about the reassortants.
18. Noticing that per-assay cohort sizes differ — binding antibody 75,
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
    contemporary and forward-drift. The gain is in fact uniform across eras, so
    the potency-shift reading is the better-supported one, but neither reading
    changes what A2 requires and neither is scored.
25. Whether the adverse waning result is reported as a fold-ratio, a retention
    fraction, or a slope.
26. Language, tooling, file layout and presentation of saved analysis.
27. Omitting Study 3. Resolving the A/H3N2 dissociation is correct work the
    prompt does not require; the deliverable fully answers the prompt without
    it.
28. Omitting any number the Golden Response carries that is not needed to
    establish A1, A2 or A3.
29. Length, section ordering, and whether studies are numbered or named.
30. Appended methodological, assay or bench-level detail, where the
    what/whom/against-what specification is already complete. The prompt's
    scope line is enforced on substitution (B11), not on addition: a complete
    specification with extra material appended scores as one without it.
31. How the attempt handles the antigenic composition in the trial summary.
    Taking the stated composition at face value, and questioning whether an
    egg-based comparator would in fact have carried the H1 component the summary
    assigns to both arms, both count. The mount states the composition and
    nothing in it corroborates or refutes the comparator's formulation, so no
    reading is scored (B15 covers the one use of the composition that is).

**Equivalent methods.** Any route that establishes the same claims from the
mounted files earns what the Golden Response's route earns. The Golden Response
uses per-virus Mann-Whitney with within-panel Benjamini-Hochberg correction and
participant-level geometric means; a mixed model over the panel, a
covariate-adjusted analysis of day-29 titre, a permutation test, or a
distance-regression approach all count where they establish A1, A2 and A3 from
the same files.
