# Verification

Two separate problems. **Accuracy** is whether the claims made are right.
**Coverage** is whether a point was missed. Checking the first cannot surface the
second, so they need different mechanisms.

## Citation audit — default, on first print

Run this the first time any citation appears in output the writer will read. It is
cheap: one call dumps every cited line at once, a second covers context.

1. **Verbatim.** The quoted string matches the source exactly. Paraphrase inside
   quotation marks is never acceptable, and neither is silently normalising
   capitalisation or punctuation.
2. **Location resolves.** The file has that line; the line holds that text.
3. **Context supports the attribution.** Read roughly three lines either side. A
   verbatim quote can still be mis-attributed — a sentence sitting under a heading
   that frames it differently will not mean what it appears to mean in isolation.
   This is the failure this check exists for.
4. **Table rows.** Where a citation points at a row, confirm which row. Adjacent
   rows in an evidence table are easy to transpose and the error is invisible once
   quoted.

**What this does not catch.** Inference errors. A claim can rest on flawless
citations and still be wrong — the quote is accurate, the conclusion drawn from it
is not. Those are addressed by the conduct-not-motive rule and, in graded mode, by
the accepted-routes question. A clean citation audit must not be reported as "the
claims are sound."

## Figure recomputation — once, at Phase 1

Recompute every figure the FA will quote, from the data room, and record the file,
the reduction and the result. Scope it to figures the FA uses; recomputing the
whole data room is not worth it.

Where a reference solution exists, reconcile against it. Reductions differ
defensibly — participant-level geometric means against pooled observations will
disagree slightly — so record which route reproduces and treat a sub-percent
difference traceable to reduction order as agreement.

In trajectory-only mode this step carries more weight, not less: with no reference
solution, **attempting to reproduce a figure is how you prove it was hallucinated**.
Failure to reproduce is the evidence.

## Coverage screen — Phase 1

For each file in the data room, check whether each trajectory references it. A file
no trajectory touched, or that most trajectories ignored, is a candidate error mode
and under a prevalence brief a valuable one.

**The screen produces candidates, never findings.** Grep the trajectory's output
files for each data-room filename, then **confirm every apparent non-use against
the transcript before recording it**. A trajectory routinely reads a file and never
names it in its output.

This is not hypothetical. On one panel the screen flagged two trajectories as never
touching a file each; both were false, with six and three references respectively in
their transcripts. Reported without the confirmation step, the screen would have
manufactured two error modes that did not exist.

## Parsing grader rationales — screen only

Rationales are prose and resist automated extraction. The failure mode is
systematic: a sentence such as "Not triggered: B1, B2, B4, B5, B9…" puts the
negation next to the first item only, so a window-based parser reads the rest as
fired. On one panel a naive parse reported eleven penalties against a trajectory
whose rationale had explicitly cleared all but one.

So: parse to generate the grid, then **read each cell marked fired or uncertain in
the rationale itself** before the grid is reported as data. Determine polarity per
segment rather than per mention, and treat a segment containing both a negation and
a positive term as uncertain rather than guessing.

Report uncertain cells as uncertain. A matrix with honest gaps is more useful than
a complete one that is partly invented.
