# Session handoff — WU397 Anton task, QA-fix round

Paste this into a fresh Claude Code session. The prior session kept hitting
safety-classifier (T&S) blocks on long dense replies; work was unaffected, only
chat output was truncated. Nothing below is blocked at the tool level.

## Repo / branch / state
- Repo `ayyang04-ay/Task3`, branch **`claude/amazing-wright-20gzza`**, HEAD **`3e17400`**, tree clean.
- Do NOT create a new branch. Do NOT open a PR. Commit + `git push origin claude/amazing-wright-20gzza`.
- Commit attribution footer: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` + `Claude-Session: <this session url>`.

## What the task is
Anton task `jp2x8c9f` (problem `task_bde3387a94ec468c9418692ce01ec01d`), mRNA
influenza next-study-design, document-appraisal lane. Hidden basin: the package
shows broader *binding*, not broader *protection*, and only for half the
quadrivalent (B/Victoria has no functional data). Three graded commitments:
A1 = power on A/H1N1 (functional), A2 = contemporary/forward-drift strain set,
A3 = B/Victoria coverage as a prerequisite with its own functional endpoint.

## Status: IN DISTRIBUTION, resolving QA
- Two Taiga panels run. Latest is well-distributed (~30% mean, bimodal) — a
  working task. First panel was too easy (0.669) and was fixed (see commits).
- Current version in RLS (1327834d) is tagged **Failed QA**; we are addressing
  the QA findings. Most are rebutted; one technical finding is legitimate and
  its fixes are **not yet applied** (below).

## First steps in the new session
1. Read `HANDOFF.md`, `reviewer_data/problem_card.md`, `grader/grader_prompt.md`, `task_prompt.txt`, `README.md`.
2. Install deps and confirm gates:
   `pip install -q scipy pandas numpy statsmodels openpyxl`
   `python3 build/verify_room.py data_room`   (22 anchors, all must pass)
   `python3 build/assert_absence.py data_room` (absence anchors hold)
3. anton-scope skill is the design spine; `references/{workflow,grading,design-laws,prompt-craft,traps}.md`.

## QA findings — disposition (jp2x8c9f v1 1327834d, 17 findings)

### REBUTTED (keep as designed — rationale already written, do not change)
- **B11 / appended bench protocols scored neutral** (env-linter + problem-linter).
  Deliberate. Prompt doesn't mandate "provide X/Y/Z"; bench detail is neither
  required nor forbidden as a deliverable, so it's neutral. Penalising it is a
  verbosity penalty, which the accounting rules forbid, and a noisy RL signal.
  B11 still penalises *substitution* (bench detail instead of the spec).
- **Hedging / "undisclosed constraint that subtype is graded"** (data-quality).
  Rebutted. The commitment is data-forced (11/13 vs 0/83, derivable), not a
  hidden rule; a strong model gives a decisive recommendation, and the prompt
  asks for one. Not telegraphing it is correct Anton design (no answer taxonomy
  in prompt).
- **Score-band / A1-miss gravity / 0.30 compression** (several warnings). These
  are grader-consistency observations; the directional verdicts are correct. Low
  priority; optionally add one line to guidance on how grave an A1 miss is, but
  not a validity failure.

### LEGITIMATE — fixes NOT yet applied. Apply all of these.
Source: env-linter finding "Golden response/B3 rest on claims the data contradict".
Every Golden *number* recomputes correctly (verified); these are interpretation
+ mechanical errors. All independently reverified this session.

1. **Drift-gradient claim is false — the H1N1 gain is uniform across eras.**
   Recomputed: participant-level mRNA−Fluarix log2 fold-rise is **+1.02 on 2023
   isolates and +1.02 on pre-2023** (interaction p=0.80). It is a uniform potency
   gain, not a drift/breadth gradient.
   - `grader_prompt.md` line ~45 (Study 1): replace "The separation is carried by
     contemporary and forward-drift strains rather than by a uniform potency
     shift: ..." with a uniform-gain reading, e.g.: *"The arm advantage is broadly
     uniform across the panel (~+1.0 log2 on both 2023 and pre-2023 isolates) and
     extends to the 2023 isolates post-dating the composition — which is why the
     panel must be contemporary and forward-drift: a forward-looking claim must be
     demonstrated against forward-drifted strains, and neither binding panel
     contains a strain later than 2022."*
   - A2 line ~115: delete the clause "— that reading is weaker than the gradient
     and is not required" (there is no gradient). A2's other groundings stand
     (2023 isolates among significant; binding panels stop at 2022), so A2 holds.
   - Note C24 (line ~182) already lists "potency shift" as neutral — after the
     fix, Study 1 and C24 agree.

2. **B3 / B1 / Study 3 "same n ⇒ not underpowering" is a flawed argument.**
   H3N2 effect is genuinely smaller (participant fold-rise 1.35×, p=0.20 vs H1N1
   2.02×), so equal n does not prove adequate power. Re-base on "no functional H3
   signal to power on" (0/83 neutralisation; the large binding signal is
   non-functional), NOT "same n."
   - B3 line ~131: reword so it penalises recommending a larger H3N2
     neutralisation study as *the protection trial* because there is no functional
     H3 signal — and narrow it so it does NOT fire on a defensible wide-CI /
     absence-of-evidence remark (this also closes the separate
     `minor_penalty_applied_to_defensible_scientific_rationale` warning).
   - Remove/replace the "so this is not an underpowering result" phrasing in
     Study 3 (line ~77) and B1 (line ~127); keep the 0/83-vs-11/13 contrast as a
     statement of *effect absence*, not of adequate power.

3. **Filename mismatch — UPLOAD SIDE (user action).** Grader cites
   `trial_summary.md` (lines 41, 59, 123); the RLS mount serves
   `trial_summary_(1).md` (a duplicate-suffix upload artifact). Repo is correct.
   FIX ON UPLOAD: ensure the mounted data room contains exactly one summary file
   named `trial_summary.md` carrying the de-attributed season content (delete any
   stale `trial_summary.md` and the `(1)` dup; re-upload clean). Also confirm the
   mount isn't carrying a pre-de-attribution copy.

4. **"2 A strains" overstated.** `microneutralization.csv` has only
   `homologous`/`heterologous` panels, no strain names.
   - line ~66 table: change `2 A strains` → `2 panels (homologous/heterologous), both influenza A`.

5. **C16 count residual.** Golden says six reassortants (line 41); C16 (line ~174)
   still says "the five production reassortants" → change "five" → "six".

6. **Durability arithmetic basis unstated (internal inconsistency).** Quoted GMTs
   (883.7/501.4 at d29; 402.5/315.9 at d181) imply per-arm waning 2.20× and 1.59×,
   but the text states 2.13× and 1.24× (lines ~47 and B14 ~153). Both are real but
   from different reductions: 2.13/1.24 is the participant-level paired per-person
   fold (what the gate checks); 2.20/1.59 is the ratio of arm GMTs. FIX: state the
   basis explicitly — e.g. "per-participant geometric-mean fold (participants with
   both timepoints)" — so a solver recomputing by that route lands on 2.13/1.24 and
   is not marked wrong against the Golden.

### After applying 1,2,4,5,6
- Re-run `verify_room.py` + `assert_absence.py` (should stay green; these are
  grader-text edits, not anchor changes — but run anyway).
- Regenerate paste copies for RLS (see below), commit, push.
- User re-uploads: the corrected grader AND the clean `trial_summary.md` mount
  (fix #3). Prompt is UNCHANGED.

## Paste-format rules the user needs (RLS grader field mangles markdown)
Deliver the grader as a **flat** copy: one line per paragraph (no mid-sentence
wraps), **em dashes replaced with hyphens**, keep standard markdown pipe tables
and the C-list `1.`–`29.` numbering (an earlier over-flattened "C1.–C29. + `=>`
tables" version was rejected — do NOT do that). The flat+no-emdash form is what
the user accepts. A reflow script pattern is in the prior session's scratchpad;
re-deriving it is trivial (join lines within blank-delimited paragraphs; keep
lines starting with `#`, `|`, list markers standalone; `s/ — / - /`).

## Settled design decisions — do NOT relitigate
- Three A-commitments: A/H1N1 subtype, contemporary/forward-drift strain set,
  B/Victoria as prerequisite with its own functional endpoint.
- Durability is graded (B14); day-29-only penalised, ~4–6 month timepoint (day
  121 or 181) accepted; "reward 181 / penalise d29-only" are the same lever (no
  bonus points in the scheme).
- "Functional" = neutralisation/inhibition/in-vivo, never binding; HAI is
  functional and does cover B/Vic (flat).
- B11 appended-bench-detail = neutral (see rebuttal). Substitution = penalised.
- Prompt stays generic/data-forced; no "pick a subtype" language, no answer
  taxonomy. go/no-go as an answer contract is banned (this task doesn't use it).
- No caps/weights/bands/ladders/severity rankings anywhere in the grader.
- MOESM10 stays unmounted. Real study data (panels/measurements) is never
  altered; only our authored synopsis/editorial layer (e.g. the season label) is
  fixable.
- Verification gates must TEST each Golden claim independently from the mount,
  never assert the Golden's own expected values (this caused the earlier
  five-false-claims miss).

## Panel calibration / QA jobs = user's side (Anton harness), not Claude Code.
No API key here; subagent fanout is not a substitute. Claude Code authors the
fixes; the user re-uploads and re-runs Taiga + QA.

## Side artifacts in the prior session's scratchpad (not in repo)
- `anton-scope-patch.md` — 9 generalizable skill patches from this task.
- `template-review.md` — review of a "decision-under-evidence" prompt template.
- These are advisory, not task deliverables.

## Context prompt to open the new session
> Continue an Anton task in `ayyang04-ay/Task3` on branch
> `claude/amazing-wright-20gzza` (HEAD 3e17400). Read `HANDOFF.md`,
> `reviewer_data/problem_card.md`, `grader/grader_prompt.md`, `task_prompt.txt`,
> and this brief. The task is in distribution (~30%); we are applying the
> legitimate QA fixes 1,2,4,5,6 listed here (fix 3 is the user's upload). Install
> deps, confirm both gates, apply the grader edits, re-run gates, give me the
> grader as a flat no-em-dash markdown copy to re-upload, then commit+push. Hold
> every "settled design decision". Keep replies concise — a prior session hit
> frequent safety-classifier truncation on long dense vaccine-content messages.
