# run data

Panel and QA output for this task, as exported from RL Studio / Taiga.

Suggested layout, one folder per calibration round so rounds stay comparable:

```
run data/
  round1_<problem-version>/     # 16-solver panel, mean 0.669
  round2_1327834d/              # 32 runs, mean 0.302, QA tagged Failed QA
  round3_<problem-version>/     # the pilot after the round-2 fixes
```

Worth keeping per round: the score list or run export, the QA export
(`qa_report.md` plus the JSON files), and the problem-version id the runs were
scored against. The version id matters — scores are only comparable within one
grading document, since a changed accounting rule moves the mean without the
task moving.

Nothing here is mounted or served to an attempt. The data room is `data_room/`;
this folder is reviewer-side only.
