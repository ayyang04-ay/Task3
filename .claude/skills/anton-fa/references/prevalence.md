# Prevalence

The client's ranking: a small error shared across six trajectories outranks a
large error in one, because fixing common errors moves model development further.
Prevalence is therefore the primary sort key and consequence the secondary one.

That only holds if the thing being counted is genuinely the same thing each time.
Loose mode definitions produce high counts that mean nothing, and an FA built on
them will not survive review.

## Defining a countable mode

A mode is countable when another reader, given the definition and a trajectory,
reaches the same yes/no without exercising judgment.

| Not countable | Countable |
|---|---|
| "Misread the data" | "Reported the pooled-correction result as the basis for rejecting a subtype's signal" |
| "Chose the wrong endpoint" | "Made the primary endpoint a readout for which the mount holds no positive functional result" |
| "Over-interpreted binding" | "Cited a binding-breadth result as evidence of protective coverage without addressing the neutralisation nulls" |
| "Weak on influenza B" | "Proposed no endpoint specific to the uncharacterised antigen" |

Write the definition as a predicate before counting anything. If you find yourself
deciding borderline cases by feel, the definition is too loose — split it.

## Splitting and merging

**Split** when trajectories satisfy a definition for different reasons, because the
correct fix differs. Two structures that both fail an item are two modes if one
demotes a readout and the other makes success reachable without it.

**Merge** only when the underlying error and its fix are the same, and say in the
ledger that you merged.

A mode present in one trajectory is still worth recording. It ranks lower; it is
not excluded. Record the singletons.

## Counting

1. Define the predicate.
2. Read 2-3 trajectories in full to generate candidates.
3. Search **every** remaining trajectory for each candidate, and record the quote
   and location that decides each one.
4. Report `k of n`, list the trajectory IDs, and state which were read in full and
   which were searched.

Never infer presence from a score, a rank, or a grader rationale. Confirm it in
the trajectory. A rationale may characterise a trajectory in terms the trajectory
does not support — in graded mode this is specifically something to check.

## Reporting

Order the ledger by prevalence, then by consequence. For each mode report:

- `k of n` with IDs
- whether the error changed the conclusion in each affected trajectory, or was
  present but benign
- the shared root where several modes trace to one cause — a single root with
  several surface forms is a more valuable finding than the forms counted
  separately, so report both

## Honest limits

With a panel of 16, a count of 3 is not a reliable rate — report it as what was
observed, not as a frequency estimate. Say how many trajectories were read in full
versus searched, because a searched trajectory can hide a mode that a full read
would have found. Where a mode's definition was tightened mid-analysis, recount
from the start rather than mixing definitions.
