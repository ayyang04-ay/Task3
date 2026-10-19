# WU397 — first-in-class immunogenicity study, summary document

## Design

Open-label, parallel-arm immunogenicity study conducted over the 2022–2023
Northern Hemisphere influenza season.

| | |
|---|---|
| Investigational product | mRNA-1010, quadrivalent mRNA seasonal influenza vaccine |
| Comparator | Fluarix Quadrivalent (inactivated split-virion) |
| Dose | Single intramuscular dose, day 0 |
| Allocation | Non-randomised; participants assigned by enrolment site |

## Antigenic composition

Both products carried the 2022–2023 Northern Hemisphere seasonal strains. The
sponsor records the two arms as differing in the H3N2 component only:

| Component | mRNA-1010 | Fluarix |
|---|---|---|
| A(H1N1)pdm09 | A/Wisconsin/588/2019 | A/Wisconsin/588/2019 |
| A(H3N2) | A/Darwin/6/2021 | A/Darwin/9/2021 |
| B/Victoria lineage | B/Austria/1359417/2021 | B/Austria/1359417/2021 |
| B/Yamagata lineage | B/Phuket/3073/2013 | B/Phuket/3073/2013 |

Where a file labels an antigen or panel `homologous` or `heterologous`, the
designation is anchored to the mRNA-1010 components above, for participants of
both arms.

## Sampling schedule

Peripheral blood at baseline (pre-dose) and at weeks 1, 2, 4, 8, 17 and 26.
Fine-needle aspiration of the draining ipsilateral axillary lymph node was
performed in a consented subset at baseline and at weeks 2, 8, 17 and 26.

Not every assay was run at every timepoint. Files labelled in days map to the
visit weeks as day 0 (baseline), day 7 (week 1), day 29 (week 4), day 121
(week 17) and day 181 (week 26).

Attendance at the two later visits was not uniform across assays. In the serum
assays — ELISA, microneutralisation and sequencing-based neutralisation — each
participant contributes a week-17 or a week-26 sample but not both; in HAI and
in the cellular assays some participants contribute both. Where a file reports
the two visits together it is labelled `wk17/26`.

## Assay cohorts

Participant numbers differ by assay according to sample availability and consent
for the sub-studies:

| Assay family | mRNA-1010 | Fluarix |
|---|---|---|
| Binding antibody (ELISA) | 38 | 37 |
| IgM fold change | 14 | 15 |
| Haemagglutination inhibition | 14 | 15 |
| Bead-array binding, microneutralisation | 14 | 15 |
| Sequencing-based neutralisation | 13 | 14 |
| Plasmablast frequencies | 13 | 15 |
| Lymph-node fine-needle aspiration | 6 | 11 |
| Monoclonal antibody isolation, clonal overlap | 4 donors | 3 donors |

## Identifier conventions

Participant identifiers are not formatted consistently across files:

| File | Form |
|---|---|
| `binding_breadth_h1.csv`, `binding_breadth_h3.csv`, `microneutralization.csv` | `397-0NN` |
| `neutralization_seqbased.csv` | `<arm>_397-0NN_d<day>` in the `serum` column |
| `hai_titers.csv`, `gc_frequencies.csv`, `plasmablast_frequencies.csv` | numeric, zero-padded, no prefix |
| `igm_fold_change.csv` | numeric, zero-padded, no prefix, except participant `20` |
| `elisa_igg_titers.csv` | numeric, unpadded, no prefix |
| `pb_gc_clonal_overlap.csv` | `397-NN`, two digits |
| `mab_binding_panels.csv` | `397.DD.CCC`, where `DD` is the donor and `CCC` the clone |

Joining participants across files therefore requires normalising the numeric
part rather than matching the strings as written.

## Notes on the virus panels

Virus names generally follow influenza nomenclature
`<type>/<location>/<isolate>/<year>`, with exceptions in both the year and
isolate fields, and location spelling and capitalisation differ between files.
Panel members include both wild-type clinical isolates and egg- or
cell-propagated production preparations; the latter carry a designation in the
name — `IVR-238`, `NIB-88`, `X-307A`, `X-223A`, or an `egg` suffix.
