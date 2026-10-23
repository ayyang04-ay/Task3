# WU397 - mRNA seasonal influenza vaccine: next-study design

You are grading a proposal recommending the next studies for a quadrivalent mRNA
seasonal influenza vaccine (mRNA-1010), written from the complete data of one
immunogenicity study against a licensed comparator (Fluarix) over the 2022-2023
Northern Hemisphere season. The submission carries a summary of its
recommendation, the recommended studies with their endpoints, populations,
comparators and readouts, the reasoning with the numbers cited to their files,
and any analysis the attempt saved. The weight sits in how the numbers were
reached rather than in the final preference, and the work is judged as a
pharmaceutical company would judge it, across the roles that would read it.

**Accounting rules.**

- Prose that disagrees with the submission's own tables establishes nothing.
- A carried-forward error is penalised once, where it enters the chain. An error
  entering at two independent points is two errors.
- Impartial between methods. No verbosity penalty, in either direction.

## A) MUST BE PRESENT AND CORRECT

The following are the key requirements of a correct answer. Use your judgment
to identify any additional required content not listed here.

**A1. The heterologous-protection readout is powered on A/H1N1.** The attempt
names A/H1N1 as the subtype carrying the functional endpoint and grounds it in
`neutralization_seqbased.csv` — the per-virus neutralisation result, 11 of 13
within panel (10 of 12 excluding production reassortants is the same finding) —
rather than in any binding readout. A1 is met on the attempt's own grounding,
traced to that file: a commitment asserted without it, or resting on figures the
attempt's stated route does not reproduce, is not met however correct the
recommendation reads. The most common way this task goes wrong is recommending
A/H3N2 on the strength of the bead-array binding result.

A1 is scored on the recommended **primary** endpoint, not on hedges elsewhere.
An attempt that recommends powering on A/H3N2 and later remarks that A/H1N1 also
separates has recommended A/H3N2.
The test: **if A/H3N2 fails, does the A/H1N1 claim still stand on its own?** If
the A/H1N1 result survives as a claim in its own right, the design has committed
to A/H1N1 and A1 is met; if a negative A/H3N2 result takes the A/H1N1 claim down
with it, or if the design would read the same way had A/H1N1 been the subtype
that failed, it has not committed and A1 is not met. The package shows A/H3N2
at 0 of 83 on neutralisation, so a design that stakes the primary on H3N2
stakes it on a readout the data already show is dead.

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

The table is read on the testing structure, not the label an attempt uses.
"Equal co-primaries" means the two endpoints share the alpha and programme
success requires both, with no hierarchy between them - staking success on a
readout the package shows at 0 of 83, and spending type-I error budget on it at
the expense of the endpoint that separates. An attempt that writes "co-primary"
but describes a hierarchical or gatekeeping procedure, under which the A/H1N1
claim stands alone if A/H3N2 fails, is judged under the gated row and is MET.

Proposing A/H3N2 work alongside a committed A/H1N1 primary is not penalised
here or anywhere (B3, C27). What A1 tests is whether programme success is
gated on the dead readout.

Naming A/H1N1 as the only functional signal in the analysis and then
recommending one of the NOT-MET structures does not satisfy A1 - the commitment
is the recommendation, not the analysis. Nor does a MET row discharge the
grounding requirement: a recommendation in a MET row still fails A1 where the
figures it rests on are not reproducible by the route the attempt states. A
different route that is stated and does reproduce its own figures is the
equivalent-methods case, not this one - a count other than 11 of 13 arrived at
by a defensible alternative is governed by C17 and C23.

**A2. The strain set is contemporary and forward-drift H1N1 isolates.** The
attempt specifies a panel of isolates contemporary with or post-dating the
2022–2023 composition rather than a historical strain series. Any of these
groundings counts: the 2023 isolates among the significant viruses in
`neutralization_seqbased.csv`; or
that neither binding panel (`binding_breadth_h1.csv`, `binding_breadth_h3.csv`)
contains a strain later than 2022 and so cannot speak to forward drift. A2 is
met on the attempt's own grounding, traced to a mounted file: asserted without
it, or resting on figures the attempt's stated route does not reproduce, not
met.

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
justified in its own right. A3 is met on the attempt's own grounding, traced to
a mounted file: asserted without it, or resting on figures the attempt's stated
route does not reproduce, not met.

Any grounding for A3 counts: the file-by-file inventory showing influenza B
absent from the panels that name their antigens
(`neutralization_seqbased.csv`, `binding_breadth_h1.csv`, `binding_breadth_h3.csv`,
`mab_binding_panels.csv`) and present only as titres in
`elisa_igg_titers.csv`, `hai_titers.csv` and `igm_fold_change.csv` — the one
functional assay among these, HAI, being flat for B/Vic; the decay of the B/Vic
binding advantage in `elisa_igg_titers.csv` to parity by wk17/26 (1.57 vs 1.56)
while both A subtypes hold theirs; or the observation that the two influenza B
antigens named in the trial summary never appear in a neutralisation or
characterisation file.

The two panels in `microneutralization.csv` are labelled only `homologous` and
`heterologous`, with no breakdown by antigen. The trial summary anchors those
designations to the mRNA-1010 components, which include the B/Victoria antigen,
so an attempt that reads the homologous panel as touching B/Victoria is reading
the mount correctly, and so is one that records the panels as unidentifiable by
lineage. Either way no B/Victoria-specific result can be recovered from an
aggregate that does not resolve by antigen, so the panels neither supply the
functional endpoint A3 requires nor refute an inventory reporting its absence.

## B) PENALIZE FOR

The following are common errors observed on this task. This list is not
exhaustive - apply your judgment to any other issues you identify.

**B1. Powering the protection readout on the bead-array binding result.**
Selecting A/H3N2 because binding breadth is largest there (12 of 12 strains,
per-strain median between-arm delta +2.30 log2), when `neutralization_seqbased.csv` shows 0 of 83 H3N2 viruses
separating on the one functional assay run against them, while the same file
shows 11 of 13 in H1N1.

**B2. A multiplex-binding primary endpoint.** Proposing bead-array or ELISA
binding as the primary readout for a protection claim, or citing the 12-of-12
result as evidence of protective strain coverage, without confronting the
neutralisation nulls or the A/Darwin/6/2021 dissociation (per-strain median
between-arm deltas, +2.07 binding against −0.27 neutralisation).

**B3. Powering the protection trial on A/H3N2 by treating the 83 nulls as a
sample-size problem.** Recommending a larger H3N2 neutralisation study *as the
heterologous-protection trial*, on the grounds that the nulls reflect n rather
than absence of effect. The package contains no functional H3 effect estimate to
power against: 0 of 83 viruses separate, and the large H3 signal that does exist
is a binding signal the neutralisation data contradict at A/Darwin/6/2021
(+2.07 binding against −0.27 neutralisation, per-strain medians).

B3 fires on the recommendation, not the observation. Absence of evidence rather
than evidence of absence, wide confidence intervals, a smaller true H3 effect
going undetected at this n, and a larger H3N2 study proposed as exploratory work
alongside an A/H1N1 primary are all correct reasoning and are not penalised.

**B4. Correcting for multiplicity across all 96 viruses at once.** The 13
A/H1N1 and 83 A/H3N2 viruses are two separately assembled libraries screened for
different questions, so one correction across both lets the 83 largely null
A/H3N2 tests set the threshold for the 13 A/H1N1 ones; the A/H1N1 count falls
from 11 to 0 on the pooling alone. Penalised where the pooled correction is the
basis offered for the verdict, usually with the conclusion that neither subtype
has functional support. Reporting it alongside the within-panel result, with the
choice of family reasoned through, is not B4.

**B5. Treating the week-4 influenza B binding advantage as coverage.** Citing
p = 0.0146 at week 4 as evidence B is characterised, when the same comparison is
p = 0.8363 at wk17/26.

**B6. Treating HAI as influenza B coverage.** HAI is flat for B in both arms, so
it supports no endpoint in either direction.

**B7. Treating B/Victoria as deferrable to a future seasonal update.**
Addressing the influenza B component through later strain-composition changes,
or sequencing it behind the influenza A programme as lower priority, on the
implied basis that it is adequately covered - when no functional B data exist
anywhere in the mount and the binding advantage that does exist is gone by
wk17/26 (1.57 vs 1.56, p = 0.8363).

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
without its endpoints, population, comparator and readouts. The prompt requires
these for each study it asks for, so their absence is the error, whatever the
response spent its space on instead. Where the specification is present, what
else the response carries is not scored here (C30).

**B12. Offering the absence of neuraminidase data as the coverage gap.**
Reasonable as a mechanism observation, and haemagglutinin carries the dominant
antibody response, but the four antigens `trial_summary.md` names are all
haemagglutinin and neuraminidase is not among them. No NA absence threatens the
product's coverage claim the way an uncharacterised encoded antigen does. It
does not satisfy A3.

**B13. Unsupported assertion.** A number, p-value or claim with no derivation, or
whose inputs do not exist in the mount. Penalised in its own right, whether or
not the value is correct.

**B14. A day-29-only functional primary.** Recommending a protection readout with
no durability timepoint reaching roughly the length of an influenza season (~4–6
months post-dose; day 121 or day 181), when the package shows the A/H1N1
functional advantage waning 2.13-fold against 1.24-fold in the comparator from
day 29 to day 181 (p = 0.0022; per-participant geometric-mean folds, or
2.20-fold against 1.59-fold reducing by arm GMT, same direction). A day-29-only
design backs a claim the data show has already decayed within one season. Any
durability timepoint at or beyond ~4-6 months avoids B14; its exact value is
neutral (C5).

**B15. Discarding the A/H1N1 neutralisation result as confounded by vaccine
composition.** Treating the arms as non-comparable on A/H1N1, and so declining to
power on it, on the grounds that the two products' antigens differ. The trial
summary assigns the same A(H1N1)pdm09 component to both arms and records the
difference as H3N2 only. The data refute it independently: the per-virus gain is
largest on A/Wisconsin/588/2019 (+1.61 log2, same reduction), the stated H1
component itself,
where a newer-antigen explanation predicts the opposite. Questioning the
comparator's stated formulation is neutral (C31); using that question to set the
A/H1N1 result aside is not.

**B16. A stated derivation that does not produce the value it is offered as
producing.** A figure given with a named file and a described route, where
recomputing by that route yields a materially different value. Distinct from
B13, which covers an assertion carrying no derivation at all or whose inputs do
not exist in the mount; here the derivation is stated and does not yield the
number. Whether the commitment it supports still stands is governed by the A
items; this records the misstatement, once per independent point at which it
enters.

## C) NEUTRAL

The following are examples of acceptable variations that should not affect the
score. Other variations may also be neutral - use your judgment.

1. The number of studies proposed, and their ordering.
2. Whether B/Victoria is a standalone study or a sub-study of the main trial.
3. The scale of the B/Victoria work — full functional characterisation or a
   narrower bridging study. Both are defensible and the mount does not settle
   it. The readout is not neutral in the same way: A3 still requires a
   functional B/Victoria endpoint, so a narrower study satisfies A3 only if it
   carries one.
4. Sample size and power assumptions, and whether any are offered at all.
5. Timepoint selection beyond the durability timepoint B14 requires - day 181,
   day 271, day 365 all count.
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
27. Omitting work on the A/H3N2 binding-versus-neutralisation dissociation.
    Resolving it is correct work the prompt does not require, and the
    deliverable fully answers the prompt without it.
28. Omitting any number that is not needed to establish A1, A2 or A3.
29. Length, section ordering, and whether studies are numbered or named.
    Whether the word "quadrivalent" is used.
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
32. Scoping B/Yamagata out as no longer circulating, and whether it is
    mentioned at all. The live influenza B question is B/Victoria, and leaving
    B/Yamagata aside is not an omission.
33. Whether the `microneutralization.csv` panels are read as unidentifiable by
    lineage or, on the trial summary's anchoring convention, as touching the
    B/Victoria component. The mount supports both and neither resolves the
    panels by antigen.

**Equivalent methods.** Any route that establishes the same claims from the
mounted files earns what any other route earns. Per-virus Mann-Whitney with
within-panel Benjamini-Hochberg correction and participant-level geometric
means, a mixed model over the panel, a covariate-adjusted analysis of day-29
titre, a permutation test, and a distance-regression approach all count where
they establish A1, A2 and A3 from the same files.
