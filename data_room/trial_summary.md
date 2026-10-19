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

Both products carry the 2022–2023 Northern Hemisphere seasonal strains. The arms
differ only in the H3N2 component, where the two products use cell- and
egg-propagated preparations of the same strain:

| Component | mRNA-1010 | Fluarix |
|---|---|---|
| A(H1N1)pdm09 | A/Wisconsin/588/2019 | A/Wisconsin/588/2019 |
| A(H3N2) | A/Darwin/6/2021 (cell) | A/Darwin/9/2021 (egg) |
| B/Victoria lineage | B/Austria/1359417/2021 | B/Austria/1359417/2021 |
| B/Yamagata lineage | B/Phuket/3073/2013 | B/Phuket/3073/2013 |

Homologous and heterologous panel designations refer to these components.

## Sampling schedule

Peripheral blood at baseline (pre-dose) and at weeks 1, 2, 4, 8, 17 and 26.
Fine-needle aspiration of the draining ipsilateral axillary lymph node was
performed in a consented subset at baseline and at weeks 2, 8, 17 and 26.

Not every assay was run at every timepoint, and not all participants attended
both later visits. Where a file reports week 17 and week 26 together it is
labelled `wk17/26`.

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

## Identifier conventions

- Serology and cellular assay files: participant IDs of the form `397-0NN`. In
  `igm_fold_change.csv` the numeric part appears unpadded and without the
  `397-` prefix.
- Monoclonal antibodies: `397.DD.CCC`, where `DD` is the donor and `CCC` the clone.
- Sequencing-based neutralisation sera: `<arm>_<participant>_d<day>`.

## Notes on the virus panels

Virus names follow standard influenza nomenclature
`<type>/<location>/<isolate>/<year>`. Panel members include both wild-type
clinical isolates and egg- or cell-propagated production reassortants; the
latter carry a reassortant designation in the name (for example `IVR-238`,
`NIB-88`, `X-307A`, `X-223A`, or an `egg` suffix).
