# Scoping analysis

Exploratory scripts from the build, kept as provenance for the corrections
recorded in `GRADING.md`. `build/verify_room.py` supersedes them for routine
re-verification; these are the working versions that established the numbers.

| Script | What it established |
|---|---|
| `inventory.py`, `inventory_xlsb.py` | sheet inventory across the eleven workbooks |
| `antigen_scan.py` | antigen labels per sheet; first pass at the B-lineage scan |
| `b_assert.py`, `b_assert_all.py` | B-lineage assert, including the two failed naive patterns |
| `dump_blocks.py` | stacked-block structure of the ELISA and HAI sheets |
| `elisa_hai.py` | the eight ELISA and HAI anchors |
| `verify_anchors.py` | seqneut FDR, binding breadth, binding-vs-neutralisation join |
| `metric_decomp.py` | why 11/13 holds — paired fold-change against absolute titre |
| `durability.py` | the adverse waning result |
| `extract.py` | stand-in room used for the five floor probes |
