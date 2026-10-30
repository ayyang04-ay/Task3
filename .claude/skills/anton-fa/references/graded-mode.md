# Graded mode

Applies only where a writer-authored grading document scored the runs. Where a
default grader scored them, scores carry almost no information: stay in
trajectory-only mode, identify errors intrinsically, and do not rank runs by score.

## Which document scored the run

Do not assume the repository's current grading document is the one that scored the
export. It frequently is not — grading documents are revised between rounds, and
items added later cannot be attributed to earlier runs.

This is determinable, so do not ask:

1. The export carries the document that scored it, in `grading_config.json` →
   `grader_guidance`. **That string is the contract** for that job.
2. Diff it against the repository's current document and report the result. A
   byte-identical match is the confirmation you want, reached mechanically.
3. Where they differ, record which items exist in the as-scored version. An item
   absent there is unavailable for attribution — a failure cannot be charged
   against a rule that did not yet exist.
4. Only if the export has no `grading_config` should you ask the user which
   document applies.

## The four-question check

The writer audits the grading document himself, repeatedly. Do not re-audit it.
Read it once for the four things that, left unchecked, produce wrong FA claims:

**1. Are the items binary?** Most A-sections read "an item is met only where…"
and carry no partial-credit category. If so, a grader rationale saying "partial"
is using a verdict the document does not define. Note it; do not adopt it.

**2. Which analytical routes are accepted?** Grading documents commonly carry an
equivalent-methods clause listing alternative valid derivations. **Read it before
asserting that a trajectory's method was the problem.** A method the document
permits cannot be the error, and a claim that it was will be refuted from the
document alone.

**3. Which items are conjunctive?** An item requiring several things — establish
X, draw consequence Y, specify Z — fails if any one is missing, and the FA should
say which. Items also often name what does *not* satisfy them; those named
non-satisfiers are usually the sharpest adjudication tool available.

**4. Where do the accounting rules apply?** A rule such as "a carried-forward
error is penalised once" may sit under the penalty section and govern penalties
only, not the pass/fail items. Note which section each rule governs.

Record the answers in four lines. That is the whole step.

## Verdicts and rationales

**The verdict is ground truth.** The score and the item-level outcome stand. The
FA does not re-adjudicate them, does not argue a run should have scored
differently, and does not contradict the grading document.

**The rationale is auditable.** It is per-run output generated at scoring time and
is not necessarily audited to the standard of the document. Before repeating
anything it says:

- verify any figure it cites against the data room;
- verify any characterisation of the trajectory against the trajectory;
- check it against the document's own semantics — a verdict the document does not
  define is a rationale artifact.

**Surface conflicts; do not resolve them silently.** Where rationales disagree
with the document, or with each other across materially similar trajectories, that
is a grader-quality signal. Report it to the writer and record it in
`calibration.md`. As grading documents receive less audit over time this check is
the early warning, so run it even when the rationales look clean.

## Mapping modes to items

In the ledger, tag each mode with the item it engages, or `not in grader` where
the error is real but ungraded. Ungraded errors are still FA material and are
often the more interesting finding, particularly under a brief that asks for error
modes rather than scores.

A B-item recorded as **avoided** is positive evidence that the trajectory did not
make the error that item describes. Check this before asserting any motive the
item would cover.

## Reference solution

Where a golden or reference solution exists, recompute each figure it carries that
the FA will rely on, and record the file, the reduction and the reproduction.
Reductions differ defensibly — participant-level geometric means against pooled
observations will disagree slightly — so record which route reproduces, and treat
a sub-percent difference traceable to reduction order as agreement.

Note whether the golden was present in the as-scored guidance or excluded from it.
If the graders never saw it, the FA must not claim they rewarded conformity to it.
