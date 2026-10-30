# Worked example: WU397 mRNA influenza vaccine, round 3

A complete graded-mode pass. Every figure here was verified in the session that
produced it — line references read verbatim, data-room statistics recomputed
independently. Use it as a template for the method, not as a source of findings.

## Inputs

Problem `task_bde3387a94ec468c9418692ce01ec01d`, Taiga job `8bb3b16d`, problem
version `1a49c39e`. 16 trajectories, all completed, none refused. Scores: mean
0.306, min 0.18, max 0.77.

Phase 0 surfaced four things the skill now checks for explicitly:

- The job id appeared nowhere in the repository. It was real; the export existed
  only in the user's uploads. Reporting it missing is what surfaced that.
- The export arrived as **two archives**, one carrying `outputs/`, the other
  `transcripts/` and `grading/`. Identical `all_runs.csv`, differing
  `export_selection` — complementary halves, not duplicates.
- `task_files/` and `grader_files/` failed to download (Taiga 413 and 404). The
  as-scored data room was rebuilt from version control at the run date; only two
  files had changed after it, neither load-bearing.
- No scipy in the container. Mann-Whitney with continuity and tie correction plus
  Benjamini-Hochberg, implemented by hand, reproduced the reference solution
  exactly, including `p = 0.0022` on the durability test.

The as-scored guidance, extracted from `grading_config.json`, was byte-identical
to the repository's flattened grading document apart from a trailing newline.

## Four-question check

1. **Binary.** "An item is met only where…", and A1 carried a MET / NOT MET table
   with no middle row. The grader rationales nonetheless used "partial" and "weak
   or partial" — verdicts the document does not define.
2. **Accepted routes.** An equivalent-methods clause permitted "a mixed model over
   the panel, a covariate-adjusted analysis of day-29 titre, a permutation test, a
   distance-regression approach." This single line invalidated a draft FA claim
   (see retracted claims below).
3. **Conjunctive items.** A3 required three things — establish the absence, draw
   the consequence, specify an endpoint — and named two non-satisfiers, which was
   the sharpest adjudication tool in the document.
4. **Accounting rules.** "A carried-forward error is penalised once" sat under the
   penalty section, so it governed penalties and did not merge pass/fail verdicts.

## Reference figures, recomputed

| Figure | Reference | Recomputed |
|---|---|---|
| Per-virus separation, correction within each panel | 11 of 13 H1N1 | 11 of 13 |
| | 0 of 83 H3N2 | 0 of 83 |
| Median between-arm delta, 13 viruses | +1.32 log2 | +1.318 |
| Excluding the vaccine strain | 10 of 12 at +1.24 | 10 of 12, +1.244 |
| Durability, day 29 to day 181 | 2.13 vs 1.24, p = 0.0022 | identical, n = 11 vs 10 |
| Bead-array breadth | 12 of 12, median +2.30 log2 | identical |
| Binding / neutralisation dissociation, one strain | +2.07 vs -0.27 log2 | identical |
| Absent-antigen binding, week 4 then late | 3.16 vs 2.30 (p = 0.0146); 1.57 vs 1.56 (p = 0.8363) | identical |
| Homologous fold-rise | 6.15 vs 2.34 | identical |
| Breadth panels' latest isolate | none later than 2022 | 9 and 12 strains, both max 2022 |

One 0.3% difference on an arm-level summary, traced to reduction order
(participant-level geometric means against pooled observations). Recorded as
agreement.

## Error-mode ledger

Ordered by prevalence. Trajectory IDs abbreviated to attempt numbers.

| # | Mode | Class | Prevalence | Consequence |
|---|---|---|---|---|
| 1 | Named one subtype as the only functional signal, then recommended a design built on the other | Conclusion-action gap | 13 of 16 | Changes the recommendation |
| 2 | Treated a 0-of-83 null as underpowered rather than negative, then powered a trial on it | Null misread | 14 of 16 | Changes the recommendation |
| 3 | Left the uncharacterised antigen without an endpoint of its own | Gap misclassified | 15 of 16 | Changes the programme |
| 4 | Quantified its own odds on the chosen path, found them poor, proceeded | Proceeding against own assessment | 5 of 16 (04, 05, 09, 12, 16) | Compounds mode 2 |
| 5 | Offered a domain generalisation in place of the in-mount result | Unjustified inference, prior over evidence | 4 of 16 (02, 06, 09, 12) | Stated reason for mode 1 |
| 6 | Corrected for multiplicity across two heterogeneous panels at once | Statistical framing | 2 of 16 (03, 16) | Demoted a real signal in 16 |
| 7 | Asserted external facts with no file behind them | Hallucinated feature, imported fact | 2 of 16 (10, 14) | Benign — recorded anyway |

Modes 1, 2 and 5 share a root: a prior about which subtype matters, held against
the one functional assay in the mount. Reported both ways — as one root and as
three surface forms — because the root is the more useful finding and the forms
are what can be counted.

## Item matrix

Hand-verified against all 16 rationales. An automated parse of the rationale prose
was run first and was wrong in both directions — see `verification.md` — so every
cell below was confirmed by reading.

A items: met (`Y`) or not (`N`). Verdicts of "partial" appear in the rationales but
the grading document defines no such category, so they are recorded as `N*`.

| att | run | score | A1 | A2 | A3 | A4 | B items fired |
|---|---|---|---|---|---|---|
| 01 | `db4b920a` | 0.30 | N | Y | N | Y | B3, B8 (minor) |
| 02 | `353cc8b9` | 0.30 | N | Y | N | Y | B3, B12 (mild) |
| 03 | `611abb1c` | 0.30 | N | Y | N* | Y | B3, B4 (minor) |
| 04 | `116ccee3` | 0.30 | N | N* | N* | Y | B3 |
| 05 | `1ac235a0` | 0.20 | N | Y | N | Y | B3, B4 (minor), B7 (partial), B15 (partial) |
| 06 | `7180713f` | 0.36 | N | Y | N* | Y | B3, B15 (marginal) |
| 07 | `9c1e496a` | 0.40 | N | Y | Y | Y | B3, B4 (minor) |
| 08 | `5547370d` | 0.28 | N | Y | N | Y | B3 |
| 09 | `73c6bfc5` | 0.25 | N | Y | N* | Y | B3, B1 (partial), B7 (mild) |
| 10 | `27c5b83c` | 0.40 | N | Y | N* | Y | none — B3 folded into A1, "not penalised twice"; B4 minor |
| 11 | `d277d01d` | 0.18 | N | Y | N | Y | B3, B4 (minor), B7 (partial) |
| 12 | `08b24a99` | 0.25 | N | N* | N | Y | B3, B15 (partial) |
| 13 | `cfe9669b` | 0.22 | N | Y | N | Y | B3, B8 (touch) |
| 14 | `a740fa31` | 0.18 | N | N* | N | Y | B3 |
| 15 | `ad915246` | 0.77 | **Y** | Y | Y | Y | B17, B8 (minor framing) |
| 16 | `4f6de858` | 0.20 | N | Y | N* | Y | B3 (in full), B1 (partial), B4 (partial) |

**A items**

| Item | Met | Not met |
|---|---|---|
| A1 | 1 | **15** |
| A2 | 13 | 3 |
| A3 | 2 | **14** |
| A4 | **16** | 0 |

**B items**

| Item | Fired | Note |
|---|---|---|
| B3 | **14** | The dominant penalty. Folded into A1 in att 10, not triggered in att 15 |
| B4 | 6 | All minor or partial — reported alongside the main result, not the basis of a verdict |
| B7 | 3 | All partial or mild |
| B8 | 3 | All minor |
| B15 | 3 | All partial or marginal |
| B1 | 2 | Both partial |
| B12 | 1 | Mild |
| B17 | 1 | att 15 only |
| B2, B5, B6, B9, B10, B11, B13, B14, B16 | 0 | |

What the grid shows at a glance: the panel is near-degenerate on A1 and A3, A4
discriminates nothing, and of seventeen penalties exactly one fires broadly while
the rest are scattered and mostly qualified as minor. Score variance therefore
comes from A3's gradations and from B-item counts rather than from A1 — which is
why 0.18 and 0.30 trajectories read so similarly.

## Coverage screen

All 15 data-room files, against the four trajectories read in full. The screen
flagged two apparent non-uses — one trajectory never referencing a breadth panel,
another never referencing the trial summary. **Both were false**: checked against
the transcripts, six and three references respectively. They used the files and did
not name them in their outputs. Recorded here because reporting the screen without
the confirmation step would have produced two error modes that do not exist.

## Mode definitions as predicates

- **Mode 1.** The output states that subtype A carries the only functional
  advantage, and its primary endpoint is on subtype B.
- **Mode 2.** The output characterises the null as a power or precision problem
  *and* sizes a study or defines a decision gate on the subtype that produced it.
  Noting the null is absence of evidence, or proposing exploratory work on it, does
  **not** satisfy this — that distinction is what makes it countable.
- **Mode 3.** No endpoint in the proposed programme is specific to the antigen for
  which the mount holds no antigen-resolved functional data.

## The cited trajectory

Attempt 14, score 0.18, joint lowest with attempt 11. Chosen on attributability:
it missed three items against attempt 11's two, and its central error sits in its
bolded headline rather than inside a study table.

Its own deliverable supplies the whole chain:

| Line | Content |
|---|---|
| 22 | "**The only functional advantage is for H1N1, and it is short-lived.**" |
| 9 | Primary endpoint: "neutralisation of a locked panel of drifted H3N2 viruses" |
| 216 | Evidence table: broader H3 **binding** graded "Moderate" |
| 217 | Evidence table: H3N2 **neutralisation** graded "**Not shown**" (30% power) |
| 218 | Evidence table: H1N1 **neutralisation** graded "Moderate" |
| 29-30 | "only 30% power… The result is therefore inconclusive, not negative" |
| 37 | 640 participants, "90% power for a 1.5-fold ratio" on the H3N2 panel |
| 161 | "the baseline-adjusted ratio is 1.17. Neither estimate is significant." |
| 44 | GO rule gated on the H3 ratio reaching 1.5 |

Three adjacent table rows grading a binding result level with the one functional
result that separated the arms, while marking the chosen subtype's functional
result unproven, is the clearest single piece of evidence in the panel. It was
found by reading the deliverable, not the transcript.

## Retracted claims — the instructive part

Three FA claims were drafted and had to be withdrawn. All three asserted **why**
the trajectory acted, and all three were refuted from material already in hand.

**"Demoting its per-virus analysis to 'descriptive only' is what cost it the
result."** Refuted by the equivalent-methods clause: the panel-level route it used
instead was explicitly permitted, and the grader confirmed the numbers reproduced.
The trajectory's analysis was sound; only its commitment failed. Caught only
because the clause was read — hence the four-question check.

**"It chose that subtype because of the attractive binding data."** Refuted by the
trajectory's own line 47: "**Do not use** binding titres, binding breadth or GC
size as primary endpoints." The grader had recorded the corresponding penalty
items as *avoided*. The defensible version was the table-grading observation above
— conduct, not motive.

**"It concluded the arm antigen mismatch was a reason not to use that subtype."**
Inverted. The trajectory filed that observation under the study being unable to
settle the question either way. The "reason not to use it" was the analyst's
inference, attributed back to the trajectory.

Pattern: every retraction was a motive claim, and every refutation came from the
trajectory's own text or the grader record. Hence the conduct-not-motive rule.

## Calibration notes

Not FA material; recorded because they bear on task quality.

- One item was met by all 16 trajectories and discriminated nothing.
- Another was failed or partially met by 15 of 16, leaving the panel nearly
  degenerate on the two items that carried the score — which is why 0.18 and 0.30
  trajectories read so similarly.
- The single high scorer (0.77) was the only pass on the decisive item and the
  first on this task to trip pass@0.5; its item was met on the specification while
  its summary contradicted it. Worth checking whether that is a near-solve or a
  grader gap.
- Grader rationales were internally inconsistent on one penalty item: 14 of 16
  fired it separately, one folded it into another item as "not penalised twice" on
  a materially identical design.
