# WU397 - mRNA seasonal influenza vaccine: next-study design

## Golden Response

**Methods.** Between-arm comparisons are two-sided Mann-Whitney on log2
values, scipy 1.18.1 `mannwhitneyu` at its default settings, which for these
group sizes is the asymptotic approximation with the continuity correction
applied. A within-arm comparison of two timepoints in the same participants is
a two-sided paired Wilcoxon signed-rank test, scipy `wilcoxon` at its
defaults. Multiplicity is controlled by Benjamini-Hochberg within each virus
panel. Summaries are
geometric means. Where a figure depends on the unit it is reduced over, the unit
is named at the figure.

**Recommendation.** Power the heterologous-protection readout on A/H1N1 against
contemporary and forward-drift isolates with a durability co-primary, and run a
B/Victoria functional characterisation study in parallel. The package
establishes broader binding, not broader protection, and for half the
formulation it generates no antigen-resolved neutralisation or characterisation
data at all and only a flat HAI result.

### Study 1. Heterologous protection, A/H1N1

**What is measured.** Neutralisation titre against a pre-locked panel of
contemporary and forward-drift A/H1N1 clinical isolates. Co-primary endpoints at
day 29 and at a durability timepoint covering the influenza season (about 4 to 6 months
post-dose; day 121 or day 181). Haemagglutination inhibition retained as a
regulatory bridge, not as the primary functional readout.

**In whom.** Adults, randomised and observer-blind against Fluarix as the
active comparator, stratified on pre-vaccination titre and on birth cohort.

Baseline stratification is required. In `neutralization_seqbased.csv` the
mRNA-1010 arm starts lower on A/H3N2 (day 0 GMT 185.3 vs 277.7, participant-level
geometric means over all 83 H3N2 viruses; pooling rows instead gives 186.8 vs
278.4) and in
`microneutralization.csv` on the heterologous panel (week 0 GM 57.0 vs 121.3);
baseline anti-correlates with fold-rise. An unstratified fold-rise endpoint
therefore flatters whichever arm enrolled lower.

Birth-cohort stratification follows from the H1/H3 asymmetry below, which is the
pattern immune imprinting would produce. No age or birth year appears anywhere in
the mount, so the held data cannot test it.

**Against what.** Wild-type clinical isolates post-dating the 2022-2023
composition named in the trial summary. Egg- and cell-propagated production
reassortants excluded. The panel in `neutralization_seqbased.csv` contains six,
identifiable by their reassortant designations (`IVR-238` on the one H1N1 strain;
`NIB-88`, `X-307A`, `X-223A` and two `egg`-suffixed strains on H3N2).

**Why A/H1N1 carries this readout.** In `neutralization_seqbased.csv`, per-virus
Mann-Whitney on log2 fold-change (day 29 over day 0) with Benjamini-Hochberg
correction applied within each subtype panel separates the arms on **11 of 13**
A/H1N1 viruses, median delta **+1.32 log2** - the median across the 13 viruses
of each virus's between-arm difference in median log2 fold-change. Every
per-strain delta below is reduced the same way. The two non-significant viruses are
A/Michigan/45/2015 and A/Brisbane/02/2018; the oldest isolate in the panel,
A/California/07/2009, is itself significant (q = 0.036), so the separation is not
a simple old-versus-new split. **6 of the 11** significant viruses are 2023
isolates post-dating the vaccine composition.

One of the 13 is A/Wisconsin/588/2019, the H1 component `trial_summary.md`
assigns to both arms, so the contrast there measures homologous response rather
than breadth. Both arms clear that bar: mRNA-1010 rises 6.15-fold from day 0 to
day 29 (p = 0.0002) and the comparator 2.34-fold (p = 0.0009), so the
precondition for advancing either product is met and the open question is
breadth. Setting that strain aside, 10 of the remaining 12 separate at a median
delta of +1.24 log2, which is the figure the heterologous claim rests on.

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
p = 0.0022** - per-participant day-29/day-181 titre ratios over the wild-type
panel, n = 11 against 10, asymptotic with the continuity correction. The exact
test on the same inputs gives p = 0.0011; both reject, and the direction is unfavourable to the investigational arm.

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

### Study 2. B/Victoria functional characterisation

**What is measured.** Neutralisation against a B/Victoria panel, plus the
characterisation that already exists for the A subtypes: a binding-breadth panel
and monoclonal antibody isolation.

**In whom.** The same adult population, against the same Fluarix comparator.
This may run as a sub-study of Study 1 or standalone.

**Against what.** Contemporary B/Victoria isolates, including drift variants
post-dating B/Austria/1359417/2021.

**Why this is a prerequisite and not an addition.** The product is quadrivalent:
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

### Study 3. Resolving the A/H3N2 binding-versus-function dissociation

**What is measured.** Whether the additional H3 binding is functional at all:
stem-competition and epitope mapping, Fc-effector readouts, neuraminidase
inhibition, and neutralisation against drifted H3 isolates rather than binding
alone. Passive
transfer and heterologous challenge in a pre-immune animal model, interpreted as
protection per unit neutralising titre. This orthogonal pairing of in-vitro
neutralisation with in-vivo protection is what substantiates a
heterologous-protection claim; HAI tracks only matched strains and a binding
readout cannot carry it.

**In whom, and against what.** Non-clinical. Stored sera from the trial
participants for the in-vitro work, and a pre-immune ferret or mouse model for
passive transfer and challenge, comparing mRNA-1010 against Fluarix sera at
matched neutralising titre. No new clinical cohort is needed.

**Why A/H3N2 cannot carry a protection readout as it stands.** Bead-array binding
in `binding_breadth_h3.csv` separates the arms on **12 of 12** H3 strains, median
delta **+2.30 log2**, per-strain medians as above. Sequencing-based neutralisation separates on **0 of 83**
H3N2 viruses after within-panel correction. There is therefore no functional H3
signal in the package to carry a protection endpoint: the large H3 effect that
does exist is a binding effect, and the one functional readout that has been run
against these viruses finds nothing. A larger H3N2 neutralisation study might
yet detect something, but that is a hypothesis to be generated, not a protection
trial to be powered: the effect it would be powered to find has no estimate in
the package at all.

On the six H3 strains measured by both methods, all six are
binding-significant, none is neutralisation-significant, and the per-strain effect
sizes are uncorrelated (Pearson r = -0.22 on the six paired per-strain
between-arm deltas, pairing each binding strain to its wild-type neutralisation
entry where the panel also carries an egg or reassortant preparation; the two
Darwin strains are kept separate, and pooling them collapses the figure to
about zero). On A/Darwin/6/2021, mRNA-1010's own H3
component, binding is **+2.07 log2** while neutralisation is **-0.27**, both
per-strain medians.

Separately, neither bead-array breadth panel, `binding_breadth_h1.csv` or
`binding_breadth_h3.csv`, contains a strain later than 2022, so both measure
back-boost against historical strains rather than forward drift and cannot
support a forward-looking claim in principle.

### What the package does not support

**Haemagglutination inhibition separates nothing.**
A/H1N1 week 4 fold-change 2.76 vs 2.25 (p = 0.26); A/H3N2 1.72 vs 1.66
(p = 0.69).

**Conventional microneutralisation is flat** and numerically favours the
comparator on the homologous panel: week 4 fold-change GM 2.49 vs 3.32
(p = 0.53). Heterologous is 4.12 vs 3.03 (p = 0.32), confounded by the baseline
deficit noted above.

**Molecular and mechanistic readouts.** Germinal-centre persistence, repertoire
diversification, clonotype counts and single-cell annotations support a mechanism,
not a protection claim, and rest on small subsets. The lymph-node cohort in
`gc_frequencies.csv` is 6 mRNA-1010 against 11 Fluarix participants, and
`pb_gc_clonal_overlap.csv` covers the same 7 donors as the monoclonal panels,
four in one arm and three in the other. Either way the mechanistic files carry no protection weight.
The monoclonal panels are
pseudoreplicated across those same 7 donors, so per-monoclonal percentages
overstate the evidence; `group_I` runs opposite to `group_II`.

**Correcting across all 96 viruses at once** extinguishes the H1N1 signal
(11 down to 0, nothing surviving) and makes the subtypes look equivalent. The panels
are two separate libraries of 13 and 83 viruses; correction belongs within each.

**Normalising heterologous titre to each participant's own vaccine-strain titre**
makes A/H3N2 appear to separate, but the effect is a smaller denominator: at
A/Darwin/6/2021 the mRNA arm responded less well than the comparator. Such an
endpoint rewards an arm for failing against the strain in its own vaccine.
