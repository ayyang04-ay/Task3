# Failure analysis — WU397 mRNA seasonal influenza vaccine

Submitted FA, reviewer-side record. Nothing here is mounted or served to an attempt.

## Provenance

| Field | Value |
|---|---|
| Problem | `task_bde3387a94ec468c9418692ce01ec01d` |
| Panel | Taiga job `8bb3b16d-6eb6-4bf9-9ace-152b80153f07` ("Studio Regrade"), created 2026-10-26 |
| Problem version scored | `1a49c39e-9409-4d67-9094-75a7f1a667a7` (A1–A4, B1–B17; grading guidance byte-identical to `grader/grader_prompt_flat.md` modulo trailing newline) |
| Panel result | 16/16 scored, mean 0.306, min 0.18, max 0.77, pass@0.5 1/16, gate (≤0.55) cleared |
| Run cited | attempt 14, `a740fa31` (full id `a740fa31-0893-4bf7-a05e-cb8a635d443e`), score 0.18 — joint lowest with attempt 11 `d277d01d` |
| FA submitted | 2026-10-30 |

Score distribution was unimodal across 15 runs (0.18–0.40, mean 0.275, SD 0.073) plus one
detached outlier at 0.77; the largest gap in the sorted scores is 0.37 (0.40 to 0.77) against
0.06 for the next largest. A14 was chosen over A11 on attributability: it misses A1, A2 and A3
where A11 misses A1 and A3, and its A1 failure sits in the bolded headline recommendation
rather than inside a study table.

The run export for this job is not committed — it arrived as two complementary uploads
(`outputs/` in one, `transcripts/` + `grading/` in the other) and lives only in the session
scratchpad. `task_files/` and `grader_files/` were excluded by export selection, so data-room
figures below were checked against `data_room/` at this commit, which is the as-scored room:
the only post-run data-room changes (2026-10-19) touched `trial_summary.md` and
`gc_frequencies.csv`, both of which predate this panel.

## Paragraph 1 — What did the model do wrong?

A14 and A11 are tied for the lowest performing runs, with A14 being the most notable because its failure modes are more noteworthy than A11. The task is built upon 4 crucial pillars:

A1: A1 requires models to recognize that H1N1 is the only subtype with a statistically significant functional readout in the data room, and to put that as the primary endpoint rather than the binding dataset (which favors H3N2). A14 fails this criterion against its own analysis: the run verbatim states "the only functional advantage is for H1N1, and it is short-lived", yet Study 1's primary endpoint is "neutralisation of a locked panel of drifted H3N2 viruses", demoting H1N1 to a secondary behind H3N2. A14 set its per-virus estimates aside as "exploratory" and "descriptive only", basing its conclusions on a panel-level ANCOVA instead. The ANCOVA shows H1N1 separating its arms whereas H3N2 does not, and its evidence table grades H3N2 neutralization as "not shown" at 30% power against "moderate" for H1N1. Despite this, A14 advocates for H3N2 because of the bead-binding dataset, which notably does not necessitate protection. A14 stated reason for proceeding is that H3N2 as open-ended and "inconclusive, not negative", opting to investigate it further rather than utilizing the presented data.

A2: A2 requires a proposed panel of contemporary or later isolates for H1N1. As A14 opted to make H3N2 the primary, it writes a composition rule only for H3N2 and does not include a H1N1 panel composition in its study design. A historical strain series would not satisfy this criterion, as historical strains are unlikely to recirculate in the relevant timescale.

A3: A3 has 3 key tenets, all of which A14 failed. It did analyze the B/Victoria data it found but treated it as a data-quality problem rather than a coverage gap, failing to recognize that no antigen-specific functional data existed for B/Victoria. As a result, it never draws the consequence for the quadrivalent formulation (which should hold 2 IAV and 2 IBV strains). This run currently correctly scopes B/Yamagata, which is treated neutral as WHO confirmed it no longer circulates, and proposes no B/Victoria endpoint of its own.

A4: all models correctly passed the A4 criterion, and so it does not discriminate.

## Paragraph 2 — What should the model have done?

A14 reached most of the golden's numbers and then declined to build on them, and so what it needed was moreover a change of commitment/discretion rather than a difference in analysis per se.

A1: The primary functional readout should have rested on H1N1 alone, with H3N2 carried a secondary or kept out of the primary altogether (no co-primary) - a structure that still stands if H3N2 turns out negative. A14 already had the relevant grounding in its own tables: its panel ANCOVA puts the drifted H1N1 advantage at 2.08 against 1.17 for H3N2, and the golden's per-virus route reaches the same conclusion, with 11 of 13 H1N1 viruses showing statistically significant neutralization advantage after multiple test correction against 0 of 83 for H3N2. The 0/83 result should have been treated as the bona fide relevant functional data, not the condition to be re-tested. Noting that the H3 nulls are an absence of evidence or proposing a larger H3N2 exploratory study alongside an H1N1 primary would have been reasonable; however, the current analysis fails to motivate on the H1N1 data, which is the only statistically significant neutralization data. Its own observation that the H3 antigens varied between arms should have counted in favor of H1N1, which is the commonly shared subtype. Additionally, A14 should have added a durability gate at 4-6 months for H1N1, which is the relevant timescale for flu season (notably it does so for H3N2 but fails to do so for H1N1 as well).

A2: The H1N1 panel composition should be appropriately specified for the proposal, comprising isolates from 2022-2023 or later. Contemporary or newer strains are relevant since historical strains are unlikely to recirculate in such a short time, and the goal is to produce a vaccine that protects against contemporary and future drift.

A3: A14 failed to recognize that B/Victoria has no antigen-specific functional data, and so it doesn't reach the design at all. A proper design for the quadrivalent vaccine necessitates showing that all strains are efficacious, and therefore the IAV data alone is insufficient to carry forward. A strong model should propose an experiment to characterize B/Victoria functionally with its own endpoint. A14 correctly scoped out B/Yamagata but B/Victoria requires the opposite approach: B/Victoria remains in circulation and so requires adequate characterization rather then exclusion.

A4: No change is needed here, as A14 (and all runs) correctly achieved this criteria.

## Supporting evidence for the cited run

All line references are to `outputs/attempt_14_a740fa31/answer.md` (576 lines) from the
job `8bb3b16d` export. Each was read and verified verbatim.

| Line | Content |
|---|---|
| 9 | Headline: "Study 1's primary endpoint is neutralisation of a locked panel of drifted H3N2 viruses" |
| 22 | "**The only functional advantage is for H1N1, and it is short-lived.**" |
| 25 | H1N1: "By months 4-6 it had waned to 1.18 (0.78-1.80)." |
| 28 | "The H3 antigens differed between arms (Darwin/6 from cell culture vs Darwin/9 from eggs)." |
| 29-30 | "It had only 30% power to detect a 1.5-fold difference. / The result is therefore inconclusive, not negative." (under the heading "WU397 cannot settle the question either way") |
| 37 | Study 1: n = 640, "D29 neutralising GMT ratio ... across >=40 locked drifted H3N2 viruses. 90% power for a 1.5-fold ratio." |
| 44 | GO rule gated on H3: "H3 drift-panel ratio >= 1.5 with lower 95% bound > 1.0 at D29, lower bound > 1.0 at D181" |
| 47 | "**Do not use** binding titres, binding breadth or GC size as primary endpoints." |
| 98, 106, 553 | Per-virus estimates called "exploratory" / "descriptive only" / unadjusted |
| 116 | B/Vic ELISA adjusted ratio 1.35 (wk4) falling to 0.98 (wk17/26) |
| 119 | B-lineage ELISA effect confined to arm-segregated ID block, interaction p = 0.011 |
| 124 | B/Vic HAI wk4 adjusted ratio 1.05 |
| 143 | H1N1 subsequent drift 2022-23 (7 viruses): 2.08 (1.25-3.44) at D29, 1.18 (0.78-1.80) late |
| 144 | H1N1 A/Wisconsin/588/2019 (vaccine strain): 6.1 vs 2.3 fold, GMR 2.44 (1.18-5.05) |
| 161 | "the baseline-adjusted ratio is 1.17. Neither estimate is significant." |
| 216 | Evidence table: broader H3 **binding** graded "Moderate" |
| 217 | Evidence table: H3N2 neutralisation 1.17 (0.64-2.12) graded "**Not shown**" (30% power), "Underpowered; site confounding" |
| 218 | Evidence table: H1N1 neutralisation 2.08 (1.25-3.44) graded "Moderate" |
| 295 | "B/Yamagata has been removed from current recommendations" (sole use of "quadrivalent") |
| 321 | Panel composition rule, H3N2 only: "all HA clades/subclades with >=5% global frequency in the 12 months before the trial" |
| 330 | "**H1N1** drift score at D29, A vs B." — key secondary, no panel defined |
| 336 | "HAI GMT ratio and seroconversion for every vaccine strain" — the only B-touching endpoint |

## Data-room figures, independently recomputed

Recomputed from `data_room/` at this commit with a hand-rolled Mann-Whitney (normal
approximation, continuity and tie correction) and Benjamini-Hochberg, since the container
has no scipy. Every figure matches the golden; the lone exception is noted.

| Figure | Golden | Recomputed |
|---|---|---|
| H1N1 separation, BH within panel | 11 of 13 | 11 of 13 |
| Median between-arm delta, 13 viruses | +1.32 log2 | +1.318 |
| H3N2 separation | 0 of 83 | 0 of 83 |
| Non-significant H1N1 viruses | Michigan/45/2015, Brisbane/02/2018 | same two |
| A/California/07/2009 (oldest isolate) | q = 0.036 | q = 0.036 |
| 2023 isolates among the significant | 6 of 11 | 6 of 11 |
| Excluding the vaccine strain | 10 of 12 at +1.24 | 10 of 12, median over 12 = +1.244 |
| Excluding the production reassortant instead | (same finding) | 10 of 12, +1.244 |
| H1N1 waning d29 to d181 | 2.13 vs 1.24, p = 0.0022 | 2.13 (n=11) vs 1.24 (n=10), p = 0.0022 |
| Arm-level GMT d29 / d181 | 883.7 / 402.5 and 501.4 / 315.9 | 883.7 / 402.5 and **499.8** / 315.9 |
| H3 bead array | 12 of 12, median +2.30 log2 | 12 of 12, +2.30 |
| A/Darwin/6/2021 dissociation | +2.07 binding / -0.27 neutralisation | +2.07 / -0.27 |
| B/Vic ELISA wk4 | 3.16 vs 2.30, p = 0.0146 | same |
| B/Vic ELISA wk17/26 | 1.57 vs 1.56, p = 0.8363 | same |
| A subtypes at wk17/26 | A/H1 2.12 vs 1.40; A/H3 3.47 vs 1.52 | same |
| HAI B/Vic wk4 | 1.08 vs 1.05, p = 0.675 | 1.082 vs 1.047, p = 0.6754 |
| A/Wisconsin/588/2019 homologous fold-rise | 6.15 vs 2.34 | 6.15 vs 2.34 |
| Binding panels' year ceiling | no strain later than 2022 | h1: 9 strains, h3: 12 strains, both max 2022 |
| Production reassortants in the neut panel | six | 1 H1N1 (IVR-238) + 5 H3N2 (NIB-88, X-307A, X-223A, 2 egg-suffixed) |

The Fluarix day-29 arm-level GMT differs by 0.3% (499.8 against 501.4), which is reduction
order — participant-level geometric means first against pooling observations. The golden flags
this class of difference itself, the ratio is unchanged (1.77 against 1.76), and neither
paragraph quotes the number.

## Panel-wide context

Not used in the submitted FA, which the reviewer required to be about a single run. Recorded
because it was verified and bears on calibration.

| Item | Count |
|---|---|
| A1 not met | 15 of 16 (only attempt 15 `ad915246` met it) |
| A1 failure shape (a): H3N2 primary, H1N1 demoted behind it | attempts 03, 04, 05, 09, 11, 12, 14 |
| A1 failure shape (b): co-primaries, success reachable on H3N2 alone | attempts 01, 02, 06, 07, 08, 10, 13, 16 |
| A2 missed | 3 of 16 (attempts 04, 12, 14) |
| A3 not met or partial | 15 of 16 |
| A4 met | 16 of 16 — does not discriminate on this panel |
| B3 fired (H3N2 null treated as a sample-size problem) | 14 of 16 |
| B17 fired | attempt 15 only |

Thirteen of the sixteen grading records note the run identifying H1N1 as the only functional
signal in its analysis and then recommending against it. Five runs quantified their own odds
and proceeded regardless: attempt 04 gave H1 96% assurance against 35% for H3, attempt 05 a
15% GO probability, attempt 09 P(Go) = 0.18, attempt 12 an 18% chance of a >=1.5-fold H3
advantage, and attempt 16 conceded the H3 endpoint "is unlikely to be met". Four stated an
epidemiological prior as the reason for choosing H3N2: attempt 12 called it "the subtype that
defines heterologous protection", attempt 09 "H3N2 drives mismatch", attempt 06 that an
H1-only positioning "would not address where mismatch failures mostly occur", and attempt 02
"H3 is gating".

Two notes for calibration rather than for the FA. A4 was met by every run and discriminates
nothing. Attempt 15 at 0.77 is the only A1 pass and the first run on this task to trip
pass@0.5; its A1 is met on the specification while its summary gate demands both subtypes,
which is what B17 recorded.
