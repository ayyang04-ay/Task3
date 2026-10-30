# Error taxonomy

Classes of trajectory error, each with a definition and the tells that find it.
The list is not exhaustive — add classes when a trajectory shows one that does not
fit. Errors are worth recording whether or not they changed the final answer; the
client asked for errors large and small, impactful and benign.

Read with `prevalence.md`: a class is a place to look, not a mode. A countable
mode is specific.

---

## 1. Conclusion-action gap

The trajectory states a finding and then acts against it.

**Tells.** A summary or analysis section asserting X, and a recommendation
premised on not-X. Internal evidence tables that rank the options differently from
the choice made. Hedges that read as though a decision was deferred when it was in
fact taken.

**Why it matters.** This is a failure of commitment rather than of analysis, and it
is invisible to any check that only verifies the numbers. It is also one of the
easiest to evidence: both halves are in the trajectory's own text.

---

## 2. Unjustified inference

A conclusion that does not follow from the material in front of the model.

**Sub-kinds worth separating:**

- **Prior over evidence.** A domain generalisation, often correct in the world,
  overriding a specific result in the mount. Tell: a confident claim about how the
  field works, offered in place of a figure.
- **Surrogate as endpoint.** Treating a proxy measure as the thing it proxies for.
- **Correlation carried as mechanism.** An association described in causal terms.
- **Scope creep on a sample.** A claim broader than the population or panel that
  produced it.

---

## 3. Hallucinated feature

An entity, field, value or relationship that is not in the inputs.

**Sub-kinds:**

- **Phantom data.** A column, file, timepoint or arm that does not exist.
- **Imported fact.** Outside knowledge asserted as though it came from the mount.
  Often true in the world, which is what makes it slip past. Tell: a specific
  external claim — a guideline, a product property, a regulatory precedent — with
  no file behind it.
- **Fabricated figure.** A number with no derivation, or whose inputs do not exist.
- **Name collision.** Two distinct entities merged because their labels resemble
  each other.

**How to confirm.** Try to reproduce it from the data room. Failure to reproduce
is the evidence. This is why recomputation matters even where there is no
reference solution to reconcile against.

---

## 4. Derivation that does not produce its value

A figure given with a named source and a described route, where following that
route yields something else.

**Tells.** Recomputation lands outside rounding. A stated method whose inputs
could not produce the quoted precision. A value consistent with a different
reduction than the one described.

Distinguish from a fabricated figure, which carries no derivation at all. Both are
errors; they are different errors.

---

## 5. Null misread

A result treated as absence of information rather than as information.

**Tells.** "Inconclusive, not negative." "Underpowered." A confidence interval
described as spanning an effect without acknowledging it also spans no effect.
Then, decisively: the trajectory proceeds to build on the null — powering a study,
gating a decision, carrying the hypothesis forward.

**The boundary.** Noting that a null is absence of evidence rather than evidence of
absence is correct reasoning and is not an error. Proposing further exploratory
work on it is not an error. *Staking the primary conclusion on it* is the error.
Record the distinction explicitly or the mode cannot be counted.

---

## 6. Statistical framing error

The test is executed correctly but asked the wrong question.

**Sub-kinds:**

- **Wrong multiplicity family.** Correcting across heterogeneous groups that
  answer separate questions, so one group's nulls dilute another's signal. Tell: a
  single correction spanning panels of very different size.
- **Unit confusion.** Reducing over the wrong unit — observations where
  participants were meant, or the reverse.
- **Baseline imbalance ignored.** A fold-change endpoint where arms started
  unequal.
- **Ceiling or floor effects.** Saturated readouts treated as quantitative.
- **Pseudoreplication.** Repeated measures on few subjects counted as independent.

---

## 7. Proceeding against own assessment

The trajectory quantifies its chance of success, finds it poor, and proceeds.

**Tells.** An explicit probability, assurance or power figure attached to the
chosen path, visibly worse than the figure attached to a path not chosen. Phrases
conceding the endpoint is unlikely to be met.

Related to class 1 but distinct and worth separating: here the trajectory has done
the comparison numerically rather than merely stated a finding.

---

## 8. Gap misclassified

A structural gap in the evidence treated as a problem of a different kind — most
often as a data-quality issue to be cleaned rather than as something missing that
must be generated.

**Tells.** A defect log that contains the gap as an entry. Analysis effort spent
characterising a confound in the available data while the absence of other data
goes unremarked. No proposed work to close it.

---

## 9. Specification failure

An output that does not answer in the form the prompt required.

**Tells.** A recommendation with no endpoint, population, comparator or readout
where those were asked for. Methodology substituted for specification. A
requirement answered in prose but absent from the structured deliverable.

---

## 10. Self-contradiction

Two parts of the output cannot both be true.

**Tells.** A summary and a specification stating different success conditions.
Prose disagreeing with the trajectory's own tables. A decision rule inconsistent
between sections.

**Note.** Where a contradiction exists, decide which part governs before judging
the trajectory on it, and say which you used.

---

## 11. Tooling and environment friction

Effort or failure caused by the harness rather than by the problem — hand-written
parsers, missing libraries worked around, truncated context, file-format fights.

**Treat differently.** Difficulty must live in the problem. Friction-driven failure
is weak FA material and may indicate a task defect. Record it, label it, and raise
it as a task issue rather than a model error.
