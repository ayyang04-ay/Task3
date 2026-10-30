---
name: anton-fa
description: Failure analysis for Project Anton tasks. Enumerates prevalent error modes across solver trajectories, ranks them by prevalence and consequence, and QAs the writer's FA paragraphs for factual and citation accuracy. Use when the user says "anton-fa", "run FA", "failure analysis", "identify error modes", "what did the model do wrong", or pastes solver runs / a Taiga export for analysis. Also use when QAing or revising FA paragraphs already drafted.
---

# anton-fa: Anton Failure Analysis

The writer types the final FA in Studio himself (paste disabled, AI detection runs
before submission). His reasoning is the deliverable. This skill compiles and
verifies evidence, supports probing, checks his findings, and supplies drop-in
corrections for claims that do not hold.

## What the FA is for

The client wants **prevalent error modes in model trajectories**. A small error
shared across six trajectories matters more than a large error in one, because
fixing common errors moves model development further. Scores are secondary and,
on tasks graded by a default grader with no writer-authored grading document,
scores carry almost no information at all.

So the unit of analysis is **the error mode**, not the run. Runs are where you
find modes and where you establish how widespread they are.

Two modes of operation, decided in Phase 0:

| | **Graded** | **Trajectory-only** |
|---|---|---|
| When | A writer-authored grading document scored the runs | Default grader, or no meaningful grading document |
| Scores | Meaningful; rank runs by them | Uninformative; do not rank by them |
| Error identification | Intrinsic, then mapped to A/B/C items where one applies | Intrinsic only |
| Reading order | Weakest and median in full | Any 2-3 in full, selection documented |
| See | `references/graded-mode.md` | — |

Prevalence ranking, the error taxonomy and the evidence standard are identical in
both modes.

## Non-negotiables

**Never invent.** Not a transcript ID, a score, a quote, a file name, a line
number or a value. If something cannot be found, say so and name what is missing.
This rule has caught real errors: a job id absent from a repo turned out to be a
real batch that existed only in the user's uploads, and reporting it missing is
what surfaced that.

**Conduct, not motive.** What a trajectory *did* is verifiable from its output and
its transcript. *Why* it did so is almost never stated, and guessing is the single
most common source of retracted FA claims. Assert a motive only with the
trajectory's own stated reason, quoted. Otherwise say what it did and what it did
not do, and stop. In graded mode, a B-item the grader recorded as *avoided* is
positive evidence against the motive that item describes.

**Every claim carries its evidence.** A verbatim quote with a location, a value
recomputed from the data room, or a named section of the reference solution.
Paraphrase inside quotation marks is never acceptable.

**Audit citations on first print.** The first time a citation reaches output the
writer will read, verify it: the quote is verbatim, the location resolves, the
surrounding context supports the attribution, and the right table row is cited.
This costs one or two tool calls for a whole paragraph. It catches citation and
context errors; it does not catch inference errors, so never report a clean audit
as evidence that the claims are sound. See `references/verification.md`.

**State reading coverage.** Which trajectories were read in full, and which were
searched for specific modes. Any prevalence count depends on this.

## Phase 0: Inputs

Scan for: the task prompt; the grading document, if any; the reference solution or
golden, if any; the data room mounted to the solver; and the run export
(transcripts, scores, per-run output files, grader records).

Build a parse manifest and **do not start Phase 1 until every row passes or is
explicitly waived by the user.** Each row is pass/fail with the blocker named.

| Row | Check |
|---|---|
| Run export located | Including batches that live outside the repo — ask rather than concluding none exists |
| Export complete | Taiga exports split across several archives. Read `export_selection` in each `job_info.json` and merge; identical `all_runs.csv` with differing `export_selection` means complementary halves, not duplicates |
| Clusters present | Check `task_files/_ERROR.txt` and the manifests. A 413 or 404 there means the data room did not download |
| Trajectory IDs | Obtain the label verbatim as the Hub displays it, from the user. Never construct one |
| Run count and status | Note any run that errored, truncated or was blocked by Trust & Safety; T&S is a void, not a zero |
| Data room | The room **as the runs saw it**. If the export lacks it, reconstruct from version control at the run date and report which files changed after it |
| Grading document | Graded mode only. See `references/graded-mode.md` |
| Stats availability | `python3 -c "import scipy"` — containers often lack it. If absent, implement the test by hand; Mann-Whitney with continuity and tie correction plus Benjamini-Hochberg is enough for most panels |

## Phase 1: Enumerate error modes

### 1a. Read for candidates

Read 2-3 trajectories end to end. In graded mode take the weakest and the median
by score; on a tie or a score cluster, prefer the run whose errors are most
numerous and most visible in its headline output. In trajectory-only mode choose
any and record why.

**Read the deliverable before the transcript.** The output file the grader judged
(`outputs/<run>/answer.md` or equivalent) is typically 30-50 KB against 1-4 MB of
transcript JSON, it is the artifact that was assessed, and it yields citable line
numbers. Use the transcript to confirm a quote exists there too, and to see
reasoning that never reached the output.

Work through `references/error-taxonomy.md` as you read. The goal of this pass is
a list of *candidate* modes, stated tightly enough to be counted.

### 1b. Define each mode so it can be counted

A mode must be stated so another reader can decide yes/no per trajectory without
exercising judgment. "Misread the data" cannot be counted. "Treated a null result
as underpowered and then powered a trial on it" can.

This matters more than it looks: prevalence is only informative if the thing being
counted is the same thing each time. See `references/prevalence.md`.

### 1c. Establish prevalence

Search every remaining trajectory for each candidate mode. Record the trajectories
affected, with a quote and location for each. Do not infer presence from a score or
from a grader rationale — confirm it in the trajectory.

Also run the **coverage screen**: for each file in the data room, which
trajectories referenced it. A file that most trajectories ignored is a candidate
mode, and a valuable one under a prevalence brief. The screen generates candidates
only — confirm every apparent non-use against the transcript before recording it,
because trajectories routinely read a file without naming it in their output. See
`references/verification.md`.

### 1d. The error-mode ledger

One row per mode, ordered by prevalence first and consequence second.

| # | Mode | Class | Prevalence | Consequence | Evidence per trajectory | Correct move | Graded? |
|---|---|---|---|---|---|---|---|

- **Class** — from `references/error-taxonomy.md`.
- **Prevalence** — `k of n`, with the trajectory IDs listed.
- **Consequence** — does it change the final answer, or is it present but benign?
  Record benign modes; the client asked for errors large and small.
- **Evidence** — per affected trajectory: verbatim quote plus location.
- **Correct move** — what the trajectory should have done, grounded in the data
  room or the reference solution, with any figure recomputed.
- **Graded?** — in graded mode, the item id; `not in grader` where the error is
  real but ungraded; `n/a` in trajectory-only mode. An ungraded error is still FA
  material and may be the more interesting finding.

### 1e. Item matrix (graded mode)

A grid the writer can read at a glance: trajectories down, items across. It shows
which requirements the panel met and how penalties were distributed, which is the
fastest way to see where the common errors sit.

| Trajectory | Score | A1 | A2 | A3 | A4 | B items fired |
|---|---|---|---|---|---|---|

Then a summary row per item: how many trajectories met each A item, how many times
each B item fired, and how many cells are uncertain. Mark a B item's severity where
the rationale qualifies it — minor, partial, marginal — because a penalty recorded
as minor in twelve trajectories is a different finding from one recorded in full.

**Build it semi-automatically.** Parse to generate the grid, then read every cell
marked fired or uncertain in the rationale itself before reporting it. Automated
extraction from rationale prose fails systematically and in the direction that
invents penalties; see `references/verification.md`. Report uncertain cells as
uncertain rather than resolving them by guess.

In trajectory-only mode there are no items, so the equivalent grid is modes down,
trajectories across, built from the ledger.

### 1f. Per-trajectory profile

For each trajectory read in full: which modes it carries, which are unique to it,
and whether it is a poor exemplar — a low score driven by truncation or tooling
friction, an idiosyncratic mode, or a panel-wide mode that shows more clearly
elsewhere. Name the better trajectory to cite if so.

Difficulty must live in the problem, not in the tooling. A failure caused by the
solver hand-writing a file parser is weak FA material and may indicate a task
defect — say so.

### 1g. Epistemic labels

Mark every claim: **[transcript]** observed directly, **[computed]** recomputed
from the data room, **[inference]** analytic judgment.

Write to `fa/<task-id>/error_modes.md`. Keep working files **tabular**. Prose in
these files becomes prose the writer's draft can collide with, and an overlap check
runs before submission.

## Phase 2: Probe

Writer-directed work on the modes he selects. Typical moves: pull fuller context
around a quote; recompute a value; test whether an error is upstream (wrong input)
or downstream (right input, wrong reasoning); separate a reasoning failure from
tooling friction; count a named mode across every trajectory.

If the writer's reading is not supported by the evidence, say so with the evidence
and hold the position. Do not defer, and do not fold on a correct position under
pushback absent new evidence. This is the most valuable thing the skill does.

Append to `fa/<task-id>/probe_notes.md`, marking the writer's conclusions as his.

## Phase 3: QC the writer's findings

Input: the writer's bullets or his typed paragraphs.

**3a. Claim verification** — one row per claim: supported / partial / unsupported,
the evidence, and the correction stated as fact. Do not supply replacement wording
here; that is Phase 4.

**3b. Citations** — every trajectory ID exists exactly as written; quoted text is
verbatim and attributed to the right trajectory; every prevalence count is
reproducible from the ledger; cited scores match.

**3c. Consistency** — the two paragraphs must not contradict each other about the
same trajectory. Check this explicitly; it is a common failure and a reviewer
reading both will catch it.

**3d. Correct-move consistency** — what the draft says the model should have done
matches the data room and the reference solution, and any number in it recomputes.

**3e. Format** — paragraph 1 covers what went wrong, paragraph 2 what should have
happened; each 5-15 sentences (report counts); at least one trajectory cited by ID.
Do not flag grammar or rough English; both are explicitly acceptable.

**3f. Overlap** — flag any run of roughly six or more consecutive words matching
this skill's own output, or a close paraphrase of a Claude-written sentence, quoting
both sides. Propose no alternative wording here.

Write to `fa/<task-id>/qc.md` and end with the must-fix list, ranked.

## Phase 4: Revision support

Only when the writer asks. He rewrites in his own words; this phase exists so he
can see precisely what was wrong and what the accurate version is.

Deliver **drop-in replacements**: location, the original text, the replacement, and
one line on why. Prefer minimal edits — a clause, not a paragraph — and preserve
the writer's structure, register and vocabulary. Keep the sentence count unchanged
unless a cut is needed for the limit, and say so when it is.

State once that the text must be retyped rather than transcribed, because the
overlap and AI-detection checks target exactly this. Say it once; do not repeat it
every turn.

## Phase 5: Calibration notes (optional)

Panel-level observations that are not FA material but bear on task quality: items
no trajectory failed and which therefore discriminate nothing; items nearly every
trajectory failed; a high scorer that may indicate a grader gap rather than a model
success; inconsistencies between grader rationales on materially similar
trajectories. Write to `fa/<task-id>/calibration.md` and keep it out of the FA
unless the reviewer asks for panel context.

## Reference files

- `references/error-taxonomy.md` — error classes, definitions, and the tells for each
- `references/prevalence.md` — defining modes so they can be counted; counting defensibly
- `references/graded-mode.md` — grading-document checks; verdict and rationale handling
- `references/verification.md` — citation audit, figure recomputation, coverage screen, and why rationale parsing is a screen only
- `references/worked-example-wu397.md` — a complete verified example
