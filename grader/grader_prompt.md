# WU397 - mRNA seasonal influenza vaccine: next-study design

## A) MUST BE PRESENT AND CORRECT

The following are the key requirements of a correct answer. Use your judgment
to identify any additional required content not listed here.

An item below is met only where the attempt gives its grounding and that
grounding recomputes by the route the attempt describes, which need not be the
route named here. Prose that disagrees with the attempt's own tables
establishes nothing.

**A1. A/H1N1 alone carries the primary functional readout.** The attempt names
A/H1N1 as the subtype carrying the functional endpoint and grounds it in
`neutralization_seqbased.csv`, where 11 of 13 viruses separate within panel (10
of 12 excluding production reassortants is the same finding), rather than in
any binding readout.

A1 is scored on the recommended primary endpoint, not on hedges elsewhere. An
attempt that recommends powering on A/H3N2 and later remarks that A/H1N1 also
separates has recommended A/H3N2. Naming A/H1N1 as the only functional signal
in the analysis and then recommending a NOT-MET structure does not satisfy A1:
the commitment is the recommendation, not the analysis. Where the opening
summary and the study specification disagree, the specification governs; a
submission that contradicts itself is still either met or not met, and the
contradiction is penalised under B17.

Designs are judged on testing structure, not the label used. A MET row does not
discharge the grounding requirement above.

| Recommended primary design | A1 |
|---|---|
| A/H1N1 the sole functional primary | MET |
| A/H1N1 primary, A/H3N2 secondary or gated behind it | MET |
| A/H1N1 first in a testing hierarchy or gatekeeping procedure, whatever it is labelled, its claim standing alone if A/H3N2 fails | MET |
| Any other structure where programme success requires A/H1N1 to pass and the A/H1N1 claim stands alone if A/H3N2 fails | MET |
| Both A subtypes as equal co-primaries - shared alpha, success requiring both, no hierarchy | NOT MET |
| Co-primaries with programme success if either A subtype passes | NOT MET |
| A "≥2-of-3 families" or "at least one A subtype" go rule | NOT MET |
| A/H3N2 tested first, with A/H1N1 reached only if A/H3N2 passes | NOT MET |
| A single pooled multi-subtype primary panel | NOT MET |
| Subtype unspecified, or the two A subtypes treated as interchangeable | NOT MET |
| Any other structure where success can be reached without A/H1N1 passing, or that would read the same way had A/H1N1 failed | NOT MET |

The table settles which subtype carries the primary. A1 also requires that
programme success depend on a heterologous demonstration: a go rule the
programme can satisfy without one does not meet A1, whatever row it lands on.
A matched-strain readout alone does not demonstrate heterologous protection;
running one alongside a required heterologous endpoint is neutral (C7).

**A2. The proposed H1N1 panel uses contemporary and later isolates, not a
historical series.** The attempt specifies a panel of isolates contemporary
with or post-dating the 2022–2023 composition. Either grounding counts: the
2023 isolates among the significant viruses in `neutralization_seqbased.csv`,
or that neither binding panel
(`binding_breadth_h1.csv`, `binding_breadth_h3.csv`) contains a strain later
than 2022 and so cannot speak to forward drift.

**A3. B/Victoria needs its own functional study before a quadrivalent claim.**
The attempt establishes that no antigen-resolved B/Victoria neutralisation or
characterisation data exist, draws the consequence that a quadrivalent product
claim cannot rest on influenza A data alone, and specifies a study or
sub-study with a B/Victoria functional endpoint of its own.

"Functional" means neutralisation, inhibition or in-vivo protection, not
bead-array or ELISA binding. HAI is the one functional assay that resolves
influenza B by antigen (`hai_titers.csv`) and it is flat for B/Vic in both arms
(week-4 fold-change 1.08 vs 1.05, p = 0.675), so it establishes no B coverage
either way; an attempt that says so is correct.

Two things do not satisfy A3: listing influenza B among absent assays without
proposing anything to close it, which is the most common way a strong attempt
fails; and writing B/Victoria isolates into a panel whose endpoint is defined
around A/H1N1 with no B-specific readout.

Any grounding counts. Influenza B is absent from the panels that name their
antigens (`neutralization_seqbased.csv`, `binding_breadth_h1.csv`,
`binding_breadth_h3.csv`, `mab_binding_panels.csv`) and present only as titres
in `elisa_igg_titers.csv`, `hai_titers.csv` and `igm_fold_change.csv`; the
B/Vic binding advantage decays to parity by wk17/26 (1.57 vs 1.56) while both A
subtypes hold theirs; the two influenza B antigens named in the trial summary
appear in no neutralisation or characterisation file. The
`microneutralization.csv` panels are labelled only `homologous` and
`heterologous` and do not resolve by antigen, so they neither satisfy A3 nor
count against an inventory reporting the absence.

## B) PENALIZE FOR

The following are common errors observed on this task. This list is not
exhaustive - apply your judgment to any other issues you identify. A
carried-forward error is penalised once, where it enters the chain; an error
entering at two independent points is two errors.

**B1. Powering the protection readout on the bead-array binding result.**
Selecting A/H3N2 because binding breadth is largest there (12 of 12 strains,
per-strain median between-arm delta +2.30 log2), when
`neutralization_seqbased.csv` shows 0 of 83 H3N2 viruses separating on the one
functional assay run against them and 11 of 13 in H1N1.

**B2. Bead-array or ELISA binding as the primary endpoint.** Proposing either
as the primary readout for a protection claim, or citing the 12-of-12
result as evidence of protective strain coverage, without confronting the
neutralisation nulls or the A/Darwin/6/2021 dissociation (per-strain median
between-arm deltas, +2.07 binding against −0.27 neutralisation).

**B3. Powering the protection trial on A/H3N2 by treating the 83 nulls as a
sample-size problem.** Recommending a larger H3N2 neutralisation study *as the
heterologous-protection trial*. With 0 of 83 viruses separating, the package
carries no functional H3 effect estimate to power against.

B3 fires on the recommendation, not the observation. Absence of evidence rather
than evidence of absence, wide confidence intervals, a smaller true H3 effect
going undetected at this n, and a larger H3N2 study proposed as exploratory work
alongside an A/H1N1 primary are all correct reasoning and are not penalised.
What is penalised is staking the protection readout on it.

**B4. Correcting for multiplicity across all 96 viruses at once.** The 13
A/H1N1 and 83 A/H3N2 viruses are two separately assembled libraries, and
pooling them drops the A/H1N1 count from 11 to 0 — the correction extinguishes
the signal, not the data. Penalised where the pooled result is the basis
offered for the verdict. Reporting it alongside the within-panel result, with
the choice of family reasoned through, is not B4, nor is any other test.

**B5. Treating the week-4 influenza B binding advantage as coverage.** Citing
p = 0.0146 at week 4 as evidence B is characterised, when the same comparison is
p = 0.8363 at wk17/26.

**B6. Treating HAI as influenza B coverage.** HAI is flat for B in both arms, so
it supports no endpoint in either direction.

**B7. Treating B/Victoria as deferrable to a future seasonal update.**
Addressing the influenza B component through later strain-composition changes,
or sequencing it behind the influenza A programme as lower priority, on the
implied basis that it is adequately covered — when no functional B data exist
anywhere in the mount and the binding advantage that does exist is gone by
wk17/26.

**B8. Advancing the programme on mechanistic data.** Recommending progression
on germinal-centre
persistence, repertoire diversification or clonotype counts as though these
bore on protection. These rest on a 6-versus-11 lymph-node cohort and 7 donors
and carry no protection weight.

**B9. Reading strain-name collisions as influenza B data.** The panels contain
influenza A strains named after the Australian state of Victoria and the
Japanese prefecture of Yamagata — among them `A/Victoria/4897/2022_IVR-238_H1N1`,
`A/Victoria/1389/2023_H1N1` and `A/YAMAGATA/98/2023_H3N2`. The actual B
antigens named in the trial summary are B/Austria/1359417/2021 and
B/Phuket/3073/2013, and neither appears in any functional file.

**B10. Reporting the vaccine-strain-normalised A/H3N2 separation as a real
effect.** Normalising heterologous titre to the participant's own
vaccine-strain titre and taking the resulting separation at face value. The
mRNA arm responded less well at A/Darwin/6/2021, so the signal is a smaller
denominator and the endpoint rewards an arm for failing against the strain in
its own vaccine.

**B11. The study specification is missing.** A recommended study is offered
without its endpoints, population, comparator and readouts. The prompt requires
these for each study it asks for, so their absence is the error, whatever the
response spent its space on instead and whether or not the gap is filled by
methodological material. Where the specification is present, what else the
response carries is not scored here (C30).

**B12. Offering the absence of neuraminidase data as the coverage gap.**
Reasonable as a mechanism observation, but the four antigens
`trial_summary.md` names are all
haemagglutinin and neuraminidase is not among them, so no NA absence threatens
the product's coverage claim the way an uncharacterised encoded antigen does.
It does not satisfy A3.

**B13. Unsupported assertion.** A number, p-value or claim with no derivation,
or whose inputs do not exist in the mount. Penalised in its own right, whether
or not the value is correct.

**B14. A day-29-only functional primary.** Recommending a protection readout
with no durability timepoint reaching roughly the length of an influenza season
(~4–6 months post-dose; day 121 or day 181), when the A/H1N1 functional
advantage wanes 2.13-fold against 1.24-fold in the Fluarix comparator from day
29 to day 181 (p = 0.0022, per-participant geometric-mean folds; reducing by
arm GMT instead gives 2.20-fold against 1.59-fold, same direction) — a claim
the data
show has already decayed within one season. Any durability timepoint at or
beyond ~4-6 months avoids B14; its exact value is neutral (C5).

**B15. Discarding the A/H1N1 neutralisation result as confounded by vaccine
composition.** Treating the arms as non-comparable on A/H1N1 and so declining
to power on it. The trial summary assigns the same A(H1N1)pdm09 component to both arms and records
the difference as H3N2 only. The data refute it independently: the per-virus
gain is uniform across the 13-virus panel and largest on A/Wisconsin/588/2019
(+1.61 log2, same reduction), the stated H1 component itself, where a
newer-antigen explanation predicts the opposite. Questioning the comparator's
stated formulation is neutral (C31); using that question to set the A/H1N1
result aside is not.

**B16. A derivation that does not produce its own value.** A figure given with a named file and a described route, where
recomputing by that route yields a materially different value. Distinct from
B13, which covers an assertion carrying no derivation at all or whose inputs do
not exist in the mount. Whether the commitment it supports still stands is
governed by the A items; this records the misstatement.

**B17. The recommendation contradicts the study specification.** Where A1 is
met on the specification, the opening summary states a different success
condition - most often a programme gate on both A subtypes where the
specification lets the A/H1N1 claim stand alone. A1 is decided on the
specification; this records the contradiction, and does not apply where the
contradiction is itself the reason A1 fails.

## C) NEUTRAL

The following are examples of acceptable variations that should not affect the
score. Other variations may also be neutral - use your judgment.

1. The number of studies proposed, and their ordering.
2. Whether B/Victoria is a standalone study or a sub-study of the main trial.
3. The scale of the B/Victoria work — full functional characterisation or a
   narrower bridging study. A3 still requires a functional B/Victoria
   endpoint, so a narrower study satisfies A3 only if it carries one.
4. Sample size and power assumptions, and whether any are offered at all.
5. Timepoint selection beyond the durability timepoint B14 requires - day 181,
   day 271, day 365 all count.
6. Choice of neutralisation platform: sequencing-based, conventional
   microneutralisation, pseudovirus, or focus-reduction.
7. Whether HAI is retained as a regulatory bridge, dropped, or not mentioned.
   Retaining it is neutral; offering it as the route by which the
   heterologous-protection claim succeeds is not.
8. Dose-ranging, schedule, prime-boost or adjuvant arms.
9. Proposing animal challenge, passive transfer, or Fc-effector work alongside
   the clinical studies.
10. Proposing neuraminidase, T-cell or mucosal readouts as additions, provided
    they are not offered in place of A3.
11. Whether birth-cohort or imprinting stratification is proposed.
12. Whether the absence of demographic data is noticed.
13. Identifying the baseline imbalance, and whether a covariate-adjusted
    analysis is proposed to handle it.
14. Noticing the panel saturation — effectively all panel viruses neutralised
    at the lowest dilution in both arms — and rejecting a seroprotection
    endpoint on those grounds.
15. Noticing the monoclonal pseudoreplication across 7 donors.
16. Excluding or retaining the six production reassortants in the panel.
17. Counting 11 of 13 or 10 of 12 A/H1N1 viruses, or another count reached by
    a defensible alternative analysis such as a baseline-adjusted model.
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
    potency shift, or as both.
25. Whether the adverse waning result is reported as a fold-ratio, a retention
    fraction, or a slope.
26. Language, tooling, file layout and presentation of saved analysis.
27. Omitting work on the A/H3N2 binding-versus-neutralisation dissociation.
28. Omitting any number that is not needed to establish A1, A2 or A3.
29. Length, section ordering, and whether studies are numbered or named.
    Whether the word "quadrivalent" is used.
30. Appended methodological, assay or bench-level detail, where the
    specification is already complete. Scope is enforced on substitution (B11),
    not on addition: a complete specification with extra material appended
    scores as one without it.
31. How the attempt handles the antigenic composition in the trial summary.
    Taking the stated composition at face value, and questioning whether an
    egg-based comparator would in fact have carried the H1 component the summary
    assigns to both arms, both count (B15 covers the one use of the composition
    that is scored).
32. Scoping B/Yamagata out as no longer circulating, and whether it is
    mentioned at all. Leaving it aside is not an omission.
33. Whether the `microneutralization.csv` panels are read as unidentifiable by
    lineage or, on the trial summary's anchoring convention, as touching the
    B/Victoria component. Neither reading resolves them by antigen.

**Equivalent methods.** Any route that establishes the same claims from the
mounted files earns what any other route earns. Per-virus Mann-Whitney with
within-panel Benjamini-Hochberg correction and participant-level geometric
means, a mixed model over the panel, a covariate-adjusted analysis of day-29
titre, a permutation test, and a distance-regression approach all count where
they establish A1, A2 and A3 from the same files.
