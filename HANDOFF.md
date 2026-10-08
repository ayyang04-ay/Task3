# Handoff — WU397 mRNA influenza next-study design task

Task `jp2x8c9f` · campaign `camp_0589d1e96758477586df0e43dd8eeec1`
Repo `ayyang04-ay/Task3` · **continue on branch `claude/amazing-wright-20gzza`**

## Status: Phase 4 (Grader) in progress

Phases 0–3 complete. Phase 4b authoring substantially done. Not yet piloted.

## What is done

**Corpus (Phase 1).** All eleven source workbooks MOESM4–14 inventoried.
Ten staged in `sources/`. MOESM10 deliberately excluded — 20 MB `.xlsb`
holding only single-cell GEX coordinates and marker-gene tables, no bearing
on any graded commitment; it is gitignored with the reason recorded.

**World (Phase 3).** `data_room/` holds 15 files, assay-keyed names.
`build/build_room.py` assembles it from `sources/`.
`build/verify_room.py` recomputes 17 graded anchors — all pass.
`build/assert_absence.py` asserts the influenza B absence anchors — passes.

**Grader (Phase 4).** `grader/grader_prompt.md`, five sections, 359 lines:
header, task framing with accounting rules, verbatim bridge line, Golden
Response (3 studies), A) 3 items, B) 13 items, C) 29 items plus the
equivalent-method catch-all.

`task_prompt.txt` carries the prompt and the safety out-of-scope constraint.

## Corrections made to the scoping spine — all recomputed from source

1. **H1 binding breadth is 7 of 9, not 8 of 9.** The ninth strain sits at
   q = 0.053 under both exact and asymptotic Mann-Whitney. The count is
   dropped as an anchor; the median (+1.16 log2) and the H3 12-of-12 hold.
2. **The binding-versus-neutralisation foreclosure conflated the two panels.**
   The spine's "10 strains both ways: 9 binding-sig, 0 neut-sig, r = −0.30"
   does not reproduce at any slicing. Correct form is H3-only: 5 of 5
   binding-significant, 0 of 5 neutralisation-significant, r = +0.10. The
   three neut-significant shared strains are all H1, where neutralisation
   genuinely separates.
3. **The A/H1N1 functional advantage does not persist.** Day 181 GMT ratio
   1.27 (p = 1.000) against 1.76 at day 29. Waning day 29 to day 181 is
   2.13-fold against 1.24-fold in the comparator, **p = 0.0022** — the most
   secure between-arm result in the package, and adverse. The spine argued
   persistence from an ELISA anchor, which is a binding readout; that is the
   same inference the spine penalises elsewhere. A durability co-primary is
   now required under A1.
4. **Three per-assay cohort sizes**, not one: binding antibody 75, HAI 29,
   sequencing-based neutralisation 27. The spine's single "n = 14/15" line is
   wrong for ELISA.
5. **`elispot_pb_frequencies` has no source** in any of the eleven workbooks.
   Dropped from the manifest; the absence rule now names three real files.
6. **`gc_frequencies` sourced from MOESM6 `Fig 3d`**, not MOESM11 `Fig 4b`.
   The MOESM11 sheet ships without arm labels and cannot support a
   comparative claim — all five floor probes independently rejected it.
7. **The 11/13 anchor survives scrutiny.** Participant-level absolute day-29
   titre gives p = 0.27, which initially looked like a contradiction. It is
   not: H1 baselines are balanced (p = 0.942), and fold-change is a paired
   within-participant contrast removing the dominant variance component
   (between-participant SD 1.11 log2 against 1.63 on absolute titre). Point
   estimates agree (1.76x absolute, 2.03x fold-rise); only precision differs.
   The baseline critique lands on H3N2 (d0 ratio 0.66), where fold-rise
   flatters mRNA and still returns 0 of 83.

## New findings added to the design

- **Strain-name collision kept deliberately.** The panels contain influenza A
  strains named for the Australian state of Victoria and the Japanese
  prefecture of Yamagata (`A/Victoria/4897/2022_IVR-238_H1N1`,
  `A/YAMAGATA/98/2023_H3N2`). Standard nomenclature; a competent attempt
  distinguishes them. Scored as B9.
- **A false optimum the spine did not list:** normalising heterologous titre
  to each participant's own vaccine-strain titre makes A/H3N2 separate
  significantly (2.21x vs 1.22x, p = 0.0125) because the mRNA arm responded
  *worse* at A/Darwin/6/2021. It yields a clean p-value pointing at the wrong
  subtype. Scored as B10.
- **Neither binding panel contains a strain later than 2022**, so both measure
  back-boost rather than forward drift. Independent foreclosure, needs no
  cross-assay comparison.
- **The absence assert needed two attempts.** Anchoring on `^B/` misses the
  mid-string block labels `EC50 B/Vic` and `Fold change B/Vic`; substring
  matching `victoria` matches influenza A strains. The shipped pattern is a
  negative lookbehind with controls in both directions. Do not simplify it.

## Floor probe result — read the caveat

Five independent attempts were run against a **stand-in** room, before MOESM4
and MOESM9 arrived. Outcome on the influenza B commitment:

| Probe | Influenza B | Behaviour |
|---|---|---|
| A | noticed, inert | one clause in a trailing gap list; no study proposed |
| B | found | folded into Study A as "a gap Study A must fill" |
| C | found | built both B lineages into Study A's panel |
| D | noticed | bundled into a mechanism study with NA and Fc |
| E | **missed** | never mentioned |

**0 of 5 proposed a dedicated B/Victoria characterisation study.**

**The caveat.** That stand-in room had no ELISA and no HAI file. Both ship four
antigen blocks including `B/Vic` and `B/Yam`, so in the shipped room an attempt
sees influenza B in the first column it reads. The real notice rate is
therefore probably higher and the real miss rate lower than the table shows.
The spine's known-risk #1 — that the influenza B floor is untested and is the
single largest risk to the design — is **still live**. Do not treat it as
retired.

What does survive, independent of discoverability: noticing influenza B and
acting on it are different behaviours, and four of five attempts that noticed
it proposed nothing to close it. That is what A3 and the bridge line are built
on. Probe C also included B/Yamagata, which is the scorable error rather than
the omission.

Probe outputs are **not** in the repo — they were written to a session
scratchpad and are gone. Re-probing produces fresh ones.

## Next steps, in order

1. **Re-probe against the shipped `data_room/`.** Five or more draws on the
   real 15-file mount. This is the only open item that could still change a
   build decision. Use `task_prompt.txt` verbatim, pointing the mount at
   `data_room/` and outputs at a scratch directory. Record whether each draw
   (a) misses influenza B, (b) notices it inertly, or (c) proposes work to
   close it. That three-way split is the diagnostic, not a score.

2. **Finish the Phase 4 checklist.** Audited and passing: five sections, no
   forbidden vocabulary, no term naming two mistakes, accounting rules
   present, commitment and scored sentence identified, neutral list long with
   catch-all, absence anchors mechanical. **Not yet done:**
   - Every A item should name its file. A1 names
     `neutralization_seqbased.csv`; A2 and A3 currently do not name theirs.
   - Confirm no B item mirrors or negates an A item. B1 was rewritten to name
     the designed trap rather than negate A1; the rest should get the same
     read.
   - Confirm the Golden Response would earn full marks under its own A/B/C.

3. **Write `reviewer_data/problem_card.md`.** Required component, not yet
   started. Lab notes: why this task, how it developed, what did not work.
   Source material is this file plus the corrections list above.

4. **Grader axis validation.** Run `grader/grader_prompt.md` against a
   deliberately flawed attempt. Probe E's answer was the natural candidate and
   is gone; a re-probe will supply another. The point is not whether a weak
   attempt loses — it is whether a *strong* attempt that passes A1 and A2 and
   fails only A3 is held to A3, or waved through on the strength of the rest.
   That halo risk is what the bridge line exists to prevent and it has never
   been exercised.

5. **Panel calibration (Phase 8).** Sixteen independent samples at T = 0.7–1.0.
   Target: mean 0.40–0.55, losses over at least three independent causes, no
   attempt above 0.75. **Cannot be run from a Claude Code session** — no API
   key, and the spine is explicit that subagent fanout is not a substitute
   because fanout arms share parent-context conditioning. Needs the Anton
   harness.

## Known open questions

- Whether the shipped room makes influenza B too discoverable. Item 1 answers
  this. If the notice rate goes high and the act-on-it rate stays low, the
  design holds. If attempts start proposing B work unprompted, the primary
  basin is weakened and the FDR-scope thread (pooled correction across 96
  extinguishing the H1N1 signal, 11 to 0) has to carry more weight.
- Whether `data_room/` is served at `/tmp/world/filesystem` by the harness
  automatically or needs a mapping step. The skill's `workflow.md` names
  `data_room/` as the model-facing component, which implies no manual bind,
  but this was not confirmed.

## Context prompt for a new session

Paste this to resume.

---

Continue building an Anton task in `ayyang04-ay/Task3`, on the existing branch
`claude/amazing-wright-20gzza`. Do not create a new branch and do not push
anywhere else.

Read `HANDOFF.md` at the repo root first — it has full status, the corrections
already made to the scoping spine, the floor-probe result and its caveat, and
the ordered next steps. Then read `grader/grader_prompt.md`, `task_prompt.txt`
and `README.md`. The scoping spine itself is the `anton-scope` skill; its
reference files are `SKILL.md` and `references/{workflow,grading,design-laws,
prompt-craft,traps}.md`, and `references/grading.md` carries the
grading-document spec and checklist this task is being built against.

The task is at Phase 4 (Grader). The data room is built and both gates pass:

```
python3 build/verify_room.py   data_room     # 17 anchors, all must pass
python3 build/assert_absence.py data_room    # absence anchors must hold
```

Start with next step 1 in `HANDOFF.md`: re-probe against the shipped
`data_room/`. The earlier probes ran against an incomplete room missing the two
files that most advertise influenza B, so the floor result is provisional and
this is the only open item that could still change a build decision.

Hold to these, they were settled in the previous session:

- The three graded commitments are A/H1N1 as the subtype, contemporary and
  forward-drift H1N1 isolates as the strain set, and B/Victoria coverage as a
  prerequisite rather than an addition.
- A durability co-primary is required under the first commitment. The
  functional advantage is gone by day 181 and the waning is adverse at
  p = 0.0022. Do not revert to arguing persistence from the ELISA anchor —
  that is a binding readout and the functional one governs.
- The strain-name collision (influenza A strains named for Victoria and
  Yamagata) stays in. It is standard nomenclature and is scored as B9.
- MOESM10 stays unmounted.
- Do not add an out-of-scope line that names an antigen, subtype, endpoint,
  gap or completeness check. The safety constraint already in
  `task_prompt.txt` is deliberately generic.
- No caps, weights, ceilings, bands, ladders, multipliers or severity
  rankings anywhere in the grading document.
- Use "binding breadth" for the bead-array result and "strain coverage" for
  panel composition. Never "breadth" alone for either.

Panel calibration cannot be run from a Claude Code session; it needs the Anton
harness. Flag it rather than approximating it with subagents.
