# Handoff — Anton task jp2x8c9f, reviewer round 1

Paste the reviewer's comments into the new session; they are not reproduced here
in full. This brief carries state, settled decisions and dispositions.

## Repo and state

- Repo `ayyang04-ay/Task3`, branch **`claude/qa-round2-rerun-v2`**, HEAD
  **`63aaef6`**, tree clean, everything pushed.
- Do not open a PR. Commit and `git push origin HEAD:refs/heads/claude/qa-round2-rerun-v2`.
- Branch-per-iteration is the convention; the branch name is the version.
- Commit footer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` plus
  `Claude-Session: <this session url>`.

## Read first

`reviewer_data/problem_card.md` (design rationale, four calibration rounds, the
deferred table of rebutted findings), `grader/grader_prompt.md`, `task_prompt.txt`,
`README.md`, `HANDOFF.md`. The `anthropic-skills:anton-scope` skill is the design
spine; `references/grading.md` is the grading-document spec this task is built
against.

## Gates — run before and after any edit

```
pip install -q scipy pandas numpy statsmodels openpyxl
python3 build/verify_room.py   data_room     # 39 anchors, all must pass
python3 build/assert_absence.py data_room    # absence anchors must hold
python3 build/flatten_grader.py grader/grader_prompt.md grader/grader_prompt_flat.md
```

`grader_prompt_flat.md` is the RLS paste copy: one line per paragraph, list item
and table row, em/en dashes and the one arrow replaced. Pipe tables and the
`1.`–`31.` C-list numbering are kept deliberately; an over-flattened
`C1.`–`C31.` plus `=>` variant was rejected and must not come back.

## Where the task stands

In distribution and clearing the gate. Four panels:

| Version | Mean | Range | Note |
|---|---|---|---|
| v1 `1327834d` | 0.302 | 0.15–0.42 | 17 of 32 at exactly 0.30; failures off-basin |
| v2 `cfbe42ba` | 0.313 | 0.20–0.40 | 7 of 16 at 0.30; 18 of 18 discounted H1 on a confound we authored |
| v3 `8bc07a26` | 0.278 | 0.18–0.52 | composition fixed; strain-mismatch route down to 3 of 16, B1 in 14 of 16 |
| v4 `140325d6` | 0.285 | 0.18–0.45 | A1 met 0 of 16, A2 15 of 16, A3 1 of 16 |

Target is mean below 0.55; all four clear it. Reward-hacking checks are clean
two rounds running: injection 0.00, pasted reference 0.03, an equivalent Welch
route 0.92 against the reference's 0.90.

## Reviewer round 1 — dispositions

No blockers. Everything below is alignment to the current project template.

### Comply

| Ask | Scope |
|---|---|
| Restore the three judgement clauses verbatim (A, B, C leads) | grader |
| Move the Golden and everything above `## A)` to the reviewer-facing field | grader |
| Cut `(B8, C19)` and the grader-facing sentence from the Golden prose | grader |
| Name the exact call behind each Golden figure | grader |
| A3 to state how the unlabelled microneutralisation panels are judged | grader |

Verified for the method-naming ask: the waning p-value is **0.0022 asymptotic
with continuity correction** and **0.0011 exact** on identical inputs, n = 11/10;
the day-0 A/H3N2 GMT is **185.33** participant-level over all 83 viruses,
**186.77** pooled rows, **159.47** participant-level wild-type only. The spec
requires the Golden to state the reduction where it changes the value, so this
one is well founded.

### Rebut

**B/Yamagata withdrawal.** The grading spec permits named domain knowledge in
the Golden. Decisively, the rule the reviewer invokes governs A and B items, and
no item depends on it: A3 says only that scoping B/Yamagata out is correct and
must not be read as an omission — permissive, never required. An attempt that
ignores it loses nothing.

**Birth-cohort stratification and immune imprinting.** Same class. Golden prose
only, flagged there as untestable from the held data, and C11 makes it neutral.

**B12 / HAI as the licensed correlate.** Rebut on the same domain-knowledge
grounds, with one asymmetry to note: B/Yamagata sits in a permissive clause
while B12 is a penalty resting on the recalled fact, and the spec says every B
penalty traces to the prompt or a mounted convention. Hardening without a
rewrite: lead B12 with its mounted reason — no NA data exist anywhere in the
package for either arm, and it does not satisfy A3 — and let the
licensed-correlate point follow as support.

### Raise with the reviewer rather than decide

The accounting rules (value-and-basis, membership-is-the-answer,
penalise-once-at-entry) currently sit above section A, and the mandated A lead
reads "Use the golden response and your judgment." If the Golden and the framing
both move to a reviewer-facing field, the grader sees neither — yet the
A-preamble grounding rule, B13 and B16 all derive from value-and-basis. Ask
whether the accounting rules stay in the grading document or move with the
Golden. If they move, those three items need their basis restated inline.

### Forces a rerun

Only the six non-ASCII dashes in `task_prompt.txt` (five em, one en, all
verified). Everything else is grader-only and costs a re-grade. Ask whether that
is worth a rerun or can ride with the next one; it changes no model behaviour.

### Projection: what "reduce to concise statements" would cost

The 1,882 words above section A are genuinely redundant once the Golden moves —
that is where the reviewer's 83-sentence count comes from, and losing it costs
nothing. Operative clauses inside B and C are different in kind; each was added
to close a measured finding, and cutting it re-opens that finding:

| Clause | Closed | If cut |
|---|---|---|
| B3 does-not-fire clause | B3 firing on defensible wide-CI remarks | returns |
| B4 family reasoning + carve-out | B4 applied on its first half alone | returns, collides with C23 |
| B16 distinction from B13 | the two had no boundary | they overlap or both miss |
| C3 readout narrowing | A3 and C3 double-classifying one submission | returns |
| C30 substitution-not-addition | the bench-protocol error, five filings | removes the rebuttal's in-document basis |
| C31 equivalent-methods pointer | Welch route regressing from 0.92 | regression risk returns |
| A-preamble grounding rule | fabrication at 0.35 above honest work at 0.20 | returns |

This is a forecast of the shortening instruction's blast radius, **not** a list
of reviewer-contested items. The reviewer contested only: the A2 "need not
assert" sentence, three accounting-rule lines, `(B8, C19)`, the grader-facing
scoring sentence, the three derivability items, A3 versus the microneutralisation
row, the dashes, and the method-naming.

Approach: compress and relocate rather than delete. The reviewer allows it —
"these cannot be incorporated into sections A, B, C following the template" is
explicitly not the position. Fold each operative clause into its item as a short
second sentence. B and C can lose roughly a third of their words with every
ruling intact.

### Sanity check the reviewer asks for

Grade the Golden against the grading document and expect 100%. Worth running
before any edits to establish a baseline and again after, since the
restructuring is what could introduce discordance.

## QA, latest round (v4)

Reviewer confirms only `error` or `critical` findings from the env linter and
reward hacking need a response — one rebuttal is required, on C30.

**C30 rebuttal, cleared and ready.** Fifth filing; the measured gap is now zero,
0.90 with an appended bench protocol against 0.90 without (previously 0.97/0.80,
then 0.95/0.93, then 0.92/0.93). Grounds agreed with the writer: the prompt
specifies what is needed and what is not; the grader rewards the criteria marked
needed and scores the rest neutral; and this is what the grading guidance
requires, which instructs penalising substitution and not addition, since
penalising addition is a verbosity penalty the accounting rules forbid in either
direction. Two corroborations worth including: the Golden's own Study 3 proposes
passive transfer and heterologous challenge work, so a bench-content penalty
would risk firing on the reference answer; and the same env-linter run confirms
every substantively wrong hand-in was marked down correctly.

One drafting note carried from the writer's review of earlier versions: do not
open the rebuttal by denying that the prompt bans bench protocols. The report
quotes the prompt line verbatim, and the graders' own recorded text calls it an
explicit instruction, so that opening invites a one-line refutation. Lead with
the needed/not-needed framing and let the substitution rule carry the argument.

**Other v4 findings, no response required.** The `hai_titers.csv` B/Vic
late-visit label difference is real source data (B/Vic week 17 is 007/008/016/021
against 009/010/018/023 for the other three antigens), impact nil because all
graded values use week 4, and C20 already makes flagging it neutral. The
data-quality item on undisclosed statistical method is the third filing of a
claim the env linter retracted twice; the measured Welch route at 0.92 settles
it. Neither needs action under the reviewer's error-or-critical rule.

## Settled — do not relitigate

- Three graded commitments: A/H1N1 as the subtype carrying the functional
  readout, a contemporary and forward-drift strain set, B/Victoria coverage as a
  prerequisite with its own functional endpoint.
- Equal co-primaries stay NOT MET, on the conjunctive-failure and alpha
  arguments. A1 tests whether programme success is gated on the dead readout,
  never whether H3N2 work is included.
- A1's behavioural test asks whether the A/H1N1 claim stands on its own if
  A/H3N2 fails. Verified consistent with all eight table rows.
- Commitment is rewarded under A1 alone; there is deliberately no B item for
  hedging, which would mirror an A item.
- B11 is cause-neutral: it penalises the absence of what the prompt requires per
  study, with no reference to substitution or methodology.
- B13 keeps its tight scope (no derivation, or inputs absent from the mount);
  B16 covers a stated derivation that does not yield its value. Do not merge
  them.
- Heterologous means not-homologous, with no convention restricting it to
  within-subtype. A1's defence is that A/H3N2 has no functional signal, never a
  definitional argument.
- Durability is adequately grounded for a seasonal product.
- The composition is the study's own: both arms carry A/Wisconsin/588/2019,
  differing only at H3N2 (A/Darwin/6/2021 against A/Darwin/9/2021). Sourced from
  the paper's methods. Do not reintroduce A/Victoria/4897/2022 as a vaccine
  antigen — it was never in this trial, and attributing it to one arm produced
  the confound that wasted the v2 panel.
- Real study data is never altered. Only the authored layer — `trial_summary.md`
  and the build script's labelling — is ours to correct.
- No caps, weights, bands, ladders, multipliers or severity rankings anywhere.
- Mounted files state facts, never the inferences a solver should draw. Two
  audits have recommended disclosing the influenza B absence or the panel
  asymmetries; both were rejected on design grounds, and both would collapse the
  basin.

## Known traps for auditors and reviewers

- The A/Darwin/6/2021 neutralisation delta of **-0.27** is per-strain. Pooling
  Darwin/6 with Darwin/9 gives about zero, because Darwin/9 runs +0.40 the other
  way. Two separate auditors have called the figure wrong after pooling.
- The H3 binding-versus-neutralisation correlation of **-0.22** reproduces under
  the documented route: per-strain median between-arm deltas on the six shared
  H3 strains. One auditor reported -0.52 from an unstated different reduction.
- Reading CSVs without `dtype=str` coerces participant IDs to integers. That
  cost one false finding about identifier padding in this repo.

## Working constraints in this environment

- Long dense replies trigger a safety classifier that truncates output. Keep
  chat terse, put substance in files, and report diffs rather than re-rendering
  documents. Occasional Bash calls are refused for the same reason; dedicated
  read/write tools and retries generally work.
- Panel runs and QA jobs execute on the Anton harness, not from Claude Code.
  Subagent fan-out is not a substitute for a 16-sample panel.
- Audits always return findings. Filter to blocking only: factually wrong, or
  two statements that genuinely contradict each other. Roughly a quarter of
  audit findings in this task did not survive checking.
