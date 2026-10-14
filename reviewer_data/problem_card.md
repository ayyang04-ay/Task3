# Problem card — WU397 mRNA influenza, next-study design

Task `jp2x8c9f` · campaign `camp_0589d1e96758477586df0e43dd8eeec1`.
Lane: clinical/translational evidence appraisal and study specification.
Non-model-facing. Reviewer notes on why this task exists, how it was built,
and what did not work along the way.

## What the task tests

The attempt is handed the complete first-round immunogenicity package for a
quadrivalent mRNA seasonal influenza vaccine against a licensed comparator, and
asked to recommend the next studies — for each, what is measured, in whom, and
against what, sufficient to support a heterologous-protection claim.

The hidden basin is a single distinction the package is built to blur: it
establishes broader **binding**, not broader **protection**, and it does so for
only half the formulation.

- The functional readout (sequencing-based neutralisation) separates the arms
  on A/H1N1 — 11 of 13 viruses within panel, 6 of them 2023 isolates
  post-dating the vaccine composition.
- A/H3N2 separates on 12 of 12 strains by bead-array **binding** and on 0 of 83
  viruses by neutralisation — the one functional assay run against them, which
  leaves no functional H3 effect estimate to power on. Binding is not functional
  here, and the binding panels contain no strain later than 2022.
- The two influenza B antigens have no functional data of any kind. Across all
  eleven source workbooks, influenza B appears only in the ELISA, HAI and IgM
  tables, and the binding advantage there is gone by wk17/26 (1.57 vs 1.56,
  p = 0.8363).

So the forced answer has three limbs: power the protection readout on A/H1N1;
specify a contemporary and forward-drift strain set; treat B/Victoria coverage
as a prerequisite, not an addition. Each is a place a confident, shallow
attempt lands wrong — by reading the largest binding signal (A/H3N2) as the
protection signal, by proposing a historical strain panel, and above all by
never converting the influenza B absence into proposed work.

## Why it is hard

The dominant failure is treating the bead-array binding result as the
protection signal and recommending A/H3N2 on the strength of it — the largest,
cleanest-looking effect in the package points at the wrong subtype. The second
is inventorying the influenza B absence without proposing anything to close it:
noticing a gap and acting on it are different behaviours, and the task is built
on that difference.

Three false optima are mounted and foreclosed:

1. **A/H3N2 binding breadth.** 12 of 12 strains, median +2.30 log2, refuted by
   0 of 83 on neutralisation at the same n that found 11 of 13 in H1N1, and by
   the homologous A/Darwin/6/2021 dissociation (+2.07 binding, −0.27 neut).
2. **Pooled multiplicity correction** across all 96 viruses, which extinguishes
   the H1N1 signal (11 → 0) and makes the subtypes look equivalent — a
   multiplicity artefact across two separate libraries of 13 and 83 viruses.
3. **Self-normalised heterologous titre**, dividing each participant's
   heterologous titre by their own vaccine-strain titre, which makes A/H3N2
   separate (p = 0.0125) only because the mRNA arm responded *worse* at its own
   vaccine strain — a clean p-value pointing at the wrong subtype.

A fourth trap is nomenclature: the panels contain influenza A strains named for
the Australian state of Victoria and the Japanese prefecture of Yamagata. A
competent attempt distinguishes these from the influenza B lineages; reading
them as B coverage is the scorable error.

## How it developed

Source: the WU397 / mRNA-1010 immunogenicity dataset, eleven supplementary
workbooks (MOESM4–14). Ten are staged in `sources/`; the data room is assembled
from them by `build/build_room.py` into 15 assay-keyed files. Every graded value
is real-sourced — there is no `generator/`, nothing synthetic or simulated.

The task arrived as a scoping spine (an `anton-scope` zip upload, not in the
repo). Re-deriving every anchor from source before authoring the grader turned
up seven places the spine was wrong. All are recomputed and corrected; the
exploratory scripts are kept in `analysis/` as provenance.

### Corrections to the spine — all recomputed from source

1. **H1 binding breadth is 7 of 9, not 8 of 9.** The ninth strain sits at
   q = 0.053 under both exact and asymptotic Mann-Whitney. Dropped as an anchor;
   the median (+1.16 log2) and the H3 12-of-12 hold.
2. **The binding-vs-neutralisation foreclosure conflated the two panels.** The
   spine's "10 strains both ways, 9 binding-sig, 0 neut-sig, r = −0.30" does not
   reproduce. Correct form is H3-only: 5 of 5 binding-significant, 0 of 5
   neutralisation-significant, r = +0.10. The neut-significant shared strains
   are all H1, where neutralisation genuinely separates.
3. **The A/H1N1 functional advantage does not persist.** Day 181 GMT ratio 1.27
   (p = 1.000) against 1.76 at day 29. Waning day 29 → 181 is 2.13-fold against
   1.24-fold in the comparator, p = 0.0022 — the most secure between-arm result
   in the package, and adverse. The spine argued persistence from an ELISA
   (binding) anchor, the same inference it penalises elsewhere. A durability
   co-primary is now required under the first commitment, and the functional
   readout governs the claim, not the binding one.
4. **Three per-assay cohort sizes, not one:** binding antibody 75, HAI 29,
   sequencing-based neutralisation 27. The spine's single "n = 14/15" is wrong
   for ELISA.
5. **`elispot_pb_frequencies` has no source** in any workbook. Dropped from the
   manifest; the absence rule now names three real files.
6. **`gc_frequencies` is sourced from MOESM6 Fig 3d**, not MOESM11 Fig 4b. The
   MOESM11 sheet ships without arm labels and cannot support a comparative
   claim — every floor probe independently rejected it.
7. **The 11/13 anchor survives scrutiny.** Participant-level absolute day-29
   titre gives p = 0.27, which first looked like a contradiction. It is not: H1
   baselines are balanced (p = 0.942), and fold-change is a paired
   within-participant contrast removing the dominant variance component
   (between-participant SD 1.11 log2 against 1.63 on absolute titre). Point
   estimates agree (1.76x absolute, 2.03x fold-rise); only precision differs.
   The baseline critique lands instead on H3N2 (d0 ratio 0.66), where fold-rise
   flatters mRNA and still returns 0 of 83.

An eighth correction was made this session: the Golden Response cited an A/H3N2
day-0 GMT of 160 vs 243 that reproduces under no aggregation. Corrected to the
participant-level GM the Golden says it uses (185 vs 278), and both baseline
imbalances (this one and the heterologous microneutralisation 57.0 vs 121.3) are
now machine-checked in `verify_room.py`.

## What did not work

- **Two naive influenza-B asserts.** Anchoring on `^B/` misses the mid-string
  block labels (`EC50 B/Vic`, `Fold change B/Vic`); substring-matching
  `victoria` matches the influenza A Victoria-named strains. The shipped
  `assert_absence.py` is a negative-lookbehind pattern with controls in both
  directions — it must not be simplified back toward either naive form.
- **The MOESM11 germinal-centre sheet.** Arm-unlabelled, so it cannot carry a
  comparative claim; germinal-centre data is sourced from MOESM6 instead.
- **The ungrounded H3N2 baseline** in the Golden (see correction 8).
- **MOESM10 was left unmounted** — a 20 MB `.xlsb` of single-cell GEX
  coordinates and marker-gene tables with no bearing on any graded commitment.
- **The first floor result was provisional.** Five probes ran against a stand-in
  room built before MOESM4 and MOESM9 arrived; it lacked the ELISA and HAI files
  that most advertise the influenza B lineage. That room and those probe outputs
  no longer exist. The result is superseded by the shipped-room re-probe below.

## Floor behaviour on the shipped room

Five blind draws on the shipped 15-file room, verbatim prompt, no hint of the
basin. Classified on the three-way split (misses the B gap / notices it inertly
/ proposes work to close it):

| Draw | Influenza B | Also |
|---|---|---|
| 1 | noticed, folded inertly into a dose-optimisation seroconversion readout | also dragged in the out-of-scope B/Yamagata lineage |
| 2 | noticed, folded inertly into a general "all four strains" endpoint | leaned into the H3N2 binding basin |
| 3 | missed entirely | got the H1N1-vs-H3N2 functional asymmetry closest to right |
| 4 | missed entirely | proposed chasing heterosubtypic H5/H7 breadth instead |
| 5 | missed entirely | fell fully into the H3N2 binding basin |

**0 of 5 proposed a dedicated B/Victoria characterisation study.** Three missed
the gap, two folded it into something inert, and one of those also committed the
B/Yamagata error. This supersedes and strengthens the provisional stand-in
result: the shipped room is the one that most advertises the B lineage (ELISA
and HAI both carry explicit B blocks), yet the act-on-it rate stayed at zero.
The handoff's known-risk #1 — that the shipped room might make influenza B too
discoverable and collapse the basin — did not materialise. Noticing and acting
are different behaviours, and that is what A3 and the bridge line are built on.

These are subagent draws, not independent API samples, so they share
parent-context conditioning and are a qualitative floor diagnostic only — not a
substitute for the Taiga panel. The direction is unambiguous regardless.

## Grader axis validation

A strong attempt was constructed to pass A1 and A2 (correct subtype, correct
grounding, correct strain set, correct H3N2 handling) and fail only A3 — it
inventoried the influenza B absence accurately by file but proposed no B work
and closed by deferring B to "the next composition review." Scored blind against
`grader/grader_prompt.md` with no other context, the grader marked A3 NOT
SATISFIED, tripped the recast B7, and declined to call the attempt correct on
the strength of its strong A/H1N1 limb. The halo risk the bridge line exists to
prevent was exercised for the first time, and the bridge held.

## Current state

- Data room built; `verify_room.py` passes 26 anchors; `assert_absence.py`
  holds.
- Grader is the five-section v4 (no caps, weights or severity rankings). Phase 4
  checklist closed: every A item names its file, no B item negates an A (B7 was
  recast from a bare negation of A3 into a distinct false optimum with its own
  refuting fact), and the Golden recomputes clean under its own A/B/C.
- Not yet done: the final Phase 5 audit pass, and the Taiga 16-solver panel plus
  the three QA jobs — both of which run on the Anton harness, not from a Claude
  Code session.

## Calibration round 1 (2026-10-09)

First 16-solver panel (claude-opus-5 grader) returned **mean 0.669** — too high
(<0.55 target), six attempts >0.75. QA was clean on reward-hacking, difficulty,
and grader hack-robustness (no-read answers scored 0.05–0.07, a planted
verification block 0.0), so the high scores are genuine solves, not exploits.

**Root cause: A1 under-specified.** It named only two failure modes
(interchangeable / unspecified) and said nothing about the designs attempts
actually submit — H1N1-first hierarchy, equal co-primaries, pooled panel,
≥2-of-3 go rule. Graders scored materially identical designs MET / PARTIAL /
NOT MET, and re-grades of one fixed answer flipped the A1 label. Since A1 drives
most of the score, this both inflated the mean and produced the variance. Fix:
A1 now carries the "would it still succeed if A/H3N2 were negative?" test and an
explicit MET/NOT-MET table; hedged designs are NOT MET.

**Golden factual errors (QA-found, all confirmed and fixed).** The gate had been
asserting the Golden's own expected values rather than testing them, so it missed
them. (1) "two oldest" — A/California/07/2009 is the oldest H1N1 and is
significant (q=0.036), so the two nulls are not the oldest; 11/13 holds. (2) gc
cohort is 6-vs-11, not 2-vs-11 (2-vs-11 is the `trial_summary.md` figure). (3)
six reassortant-tagged viruses, not five. (4) six shared H3 strains, r=−0.22, not
five at +0.10 (the conclusion "uncorrelated" survives). (5) the antigenic-distance
gradient does not reproduce — no distance field is mounted and the year-proxy
H1N1 slope is flat (p=0.86); that A2 grounding was dropped. `verify_room.py` now
tests each independently (22 anchors at round 1; 26 after round 2).

**Other fixes.** Durability is now graded (B14; season-length window ~4–6 months
— the day-181 figure was arbitrary). A3 "functional" was wrong: it called
bead-array/mAb binding "functional" and omitted HAI, which is a functional assay
that does cover B/Victoria (flat); A3 now means neutralisation/inhibition/in-vivo
and requires a B/Victoria-specific functional endpoint, not B strains in an
H1N1-powered panel. B11 is a binary substitution test (appended bench detail is
neutral, consistent with the no-verbosity-penalty rule). Study 3 states orthogonal
in-vitro + in-vivo confirmation as the standard for a heterologous-protection
claim. `trial_summary.md` was de-attributed from a WHO 2022–23 composition — the
listed strains and all measurements (the real experimental data) are unchanged;
only the editorial season label we had authored was corrected.

**Env note — closed, not a defect.** 14/16 runs hand-rolled ANCOVA, which read as
a missing dependency. It is not: `scipy` and `statsmodels` are present in the
image's `core` micromamba environment, confirmed by the round-2 env-linter and by
the author. Only the default `PATH` interpreter lacks them, so the first analysis
call fails once before a run switches environments. No image change is needed and
the earlier escalation is withdrawn.

Not yet re-piloted after these edits.

## Calibration round 2 and QA (2026-10-13/14) — v1 `1327834d`, tagged Failed QA

32 production runs, scores 0.15–0.42, mean 0.302, **17 of 32 at exactly 0.30**,
10 distinct scores across 3 A and 14 B criteria. All 32 placed the primary
endpoint on A/H3N2, so A1 was missed universally. Mean is inside target; the
compression is not, and the open question is whether it comes from A1 being the
only live gate or from the document giving graders nowhere to put an A1 miss.
**Before reading the distribution as difficulty, rescore `172b19f3` (0.42) and
`bfd0c3ae` (0.15) under the revised document** — a changed accounting rule moves
the mean without the task moving.

QA returned 17 findings across 7 checks. Seven sit in the author-visible tabs
(env linter 5, reward hacking 1, data quality 1); the rest are ClaudeScope and
harness items outside the writing scope. Disposition:

**Fixed, grader-only (re-gradeable, no rerun).**

- An A item is met only where the attempt's own grounding traces to a mounted
  file. The prompt requires the reasoning, every number relied on and its
  source, so an ungrounded commitment is not met. This closes the reward-hacking
  probe: a 20-line answer with no file reads and no numbers scored 0.30 three
  times, tying or beating 24 of the 32 genuine runs.
- C30 — appended methodological or bench-level detail is neutral where the
  specification is complete. B11 already implied this, but graders were
  improvising a deduction anyway (0.97 against 0.80 across one rollout pair that
  differed only by an appended protocol appendix).
- C31 — either reading of the antigenic composition is neutral, sensitivity
  analysis over both included.
- C32 — either lymph-node cohort figure may be cited; the Golden no longer
  attempts a reconciliation that cannot hold.
- The Golden headline no longer says influenza B has "no functional data at
  all", which contradicted A3 naming HAI a functional assay covering B/Victoria.
- Study 3 reads "neutralisation against drifted H3 isolates" rather than
  "heterosubtypic", which named a different concept from the task's claim and
  sits next to the floor draw that went chasing H5/H7 breadth.
- A1's near-miss table gained a hierarchical-testing row and a paragraph saying
  the table is read on testing structure rather than on the label. See the
  rationale below.
- The trial summary is cited by description rather than filename, with a framing
  note that an upload suffix is not evidence the file went unread. This closes
  the `trial_summary_(1).md` mismatch without a re-upload.

**Fixed, requires a model rerun** (staged on `claude/qa-round2-rerun`).

- The prompt's "It is a working directory rather than a curated one, so some of
  what is in there will not bear on the decision" is cut. The sentence states
  its own consequence, telling the solver that irrelevant files exist and
  pre-empting the triage judgement the room is built to require. Note this is a
  hardening change and should be decided together with A1, not independently.
- The trial summary's lymph-node row and the claim that Fluarix was formulated
  for this study.

### Why "equal co-primaries" stays NOT MET

A next-study recommendation is a funding decision — the prompt has it going to a
committee. Co-primary endpoints are conjunctive, so making A/H3N2 neutralisation
a co-primary designs a trial whose success condition includes a readout the
package shows at 0 of 83; the programme halts at its first gate, and the alpha
spent protecting that endpoint comes out of the one endpoint that separates. A
design that succeeds only if both subtypes separate has not committed to either.

Two boundaries, because the argument proves more than the criterion should
claim. A1 tests whether programme success is **gated** on the dead readout, not
whether H3N2 work is **included** — C9 and C10 keep additional readouts neutral,
and scope is enforced on substitution rather than addition, so a criterion
penalising the inclusion of H3 work would collide with the neutral list. And the
funding argument is the author's rationale, not a mounted fact: the prompt
implies committee approval but never mentions cost, so the criterion cites 0 of
83 and the conjunctive failure rather than the economics.

Commitment is rewarded under A1 alone and the absence of commitment is punished
only by A1 failing to be met. There is deliberately no B item for hedging: that
would mirror an A item, which the grading spec prohibits, and would double-count
one failure.

## Deferred — recorded as not fixed

Read this list at calibration before diagnosing an odd score, so a soft defect
is not mistaken for a design signal.

| Item | Why not fixed |
|---|---|
| B11 scores appended bench detail neutral, against the prompt's scope line (env linter, error) | The grading spec names "penalise substitution, never addition" as a required authoring rule and says scope constraints are enforced on substitution. Penalising addition is a verbosity penalty the accounting rules forbid in either direction, and the Golden's own Study 3 proposes challenge work. Rebutted; C30 makes the neutrality explicit so graders stop improvising a deduction. |
| Guidance never states how grave an A1 miss is (env linter, warning) | Severity rankings are on the spec's "what never goes in" list. The grounding half of the finding was implemented; the gravity half is refused. |
| Prompt leaves the claim's scope open (env linter, info) | A domain judgement the task intends to test. Commitment is prompt-grounded ("make your recommendations", "a one-line summary of your recommendation"), project-mandated and data-forced. A scope clause would be directive and brushes the no-answer-taxonomy rule. |
| Grader requires a committed subtype without announcing it (data quality, warning) | Withdrawn by the env-linter itself on re-check: the commitment is derivable from `neutralization_seqbased.csv`, so it is not a hidden rule. QA's own probes support the hedging penalty — their committed probe scored 0.30 against 0.25 for the conditional hedge. |
| Bridge line says "above" where the Golden sits below (problem linter, info) | The bridge line is verbatim mandated boilerplate; the spec says do not reword it. |
| External domain facts (WHO compositions, B/Yamagata withdrawal, CBER margins) are needed but unverifiable in the sandbox (ClaudeScope, error) | Partly intrinsic to the lane. B/Yamagata scoping is already "correct, not required", so no A item depends on the unmounted fact. The rest affects polish only. |
| ClaudeScope "recommendation contradicts own evidence" (error) | Not a defect. ClaudeScope itself calls it the capability under evaluation, correctly reflected in low grades. It is positive evidence the basin works. |
| `column` and `file` absent from the image; default `PATH` python lacks the scientific stack; grading justification truncated in run metadata | Harness-side, outside the writing scope. The scientific stack is present in the `core` environment. |
