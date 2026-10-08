# Anton task — mRNA influenza vaccine, next-study design

Task ID `jp2x8c9f` · campaign `camp_0589d1e96758477586df0e43dd8eeec1`.
Lane: clinical/translational evidence appraisal and study specification.

A program developing a quadrivalent mRNA seasonal influenza vaccine for
heterologous protection has completed a first immunogenicity study against a
licensed quadrivalent comparator over the 2022–2023 season. The attempt is asked
to recommend the next studies, specifying for each what is measured, in whom, and
against what.

## Layout

| Path | Contents |
|---|---|
| `PROMPT.md` | the prompt given to the attempt |
| `GRADING.md` | grading guidelines, including the Golden Response |
| `data-room/` | the mount, served to the attempt at `/tmp/world/filesystem` |
| `sources/` | the source-data workbooks the room is derived from |
| `build/build_room.py` | assembles the room from `sources/` |
| `build/verify_room.py` | recomputes every graded anchor from the shipped room |
| `build/assert_absence.py` | asserts the absence anchors mechanically |

## Reproducing

```
python3 build/build_room.py    sources data-room
python3 build/verify_room.py   data-room      # all anchors must pass
python3 build/assert_absence.py data-room     # absence anchors must hold
```

Requires `pandas`, `numpy`, `scipy`, `statsmodels`, `openpyxl`.

## What the task turns on

The package establishes broader **binding**, not broader **protection**, and it
does so for only half the formulation.

- **A/H1N1** carries the functional readout: sequencing-based neutralisation
  separates the arms on 11 of 13 viruses after within-panel correction, six of
  them 2023 isolates post-dating the vaccine composition. The advantage does not
  persist — waning from day 29 to day 181 is 2.13-fold against 1.24-fold in the
  comparator, p = 0.0022.
- **A/H3N2** separates on 12 of 12 strains by bead-array binding and on 0 of 83
  viruses by neutralisation, at the same n per arm. Binding is not functional
  here, and the binding panels contain no strain later than 2022.
- **B/Victoria** has no functional data of any kind. Across all eleven source
  workbooks, influenza B appears only in the ELISA, HAI and IgM tables. The
  binding advantage is significant at week 4 and gone by wk17/26 (1.57 vs 1.56,
  p = 0.8363). The product is quadrivalent, so a programme covering only
  influenza A does not support the claim.
- **B/Yamagata** is correctly out of scope — not in circulation since 2020.

## A note on the absence assert

The influenza B gap is the spine of the task, and it is asserted by script rather
than by eye. The assert must find a lineage written mid-string
(`Fold change B/Vic`) while rejecting influenza A strains named after the
Australian state of Victoria and the Japanese prefecture of Yamagata
(`A/Victoria/4897/2022_IVR-238_H1N1`, `A/YAMAGATA/98/2023_H3N2`). Both naive
formulations — anchoring on `^B/`, or substring-matching `victoria` — fail, in
opposite directions. `build/assert_absence.py` carries controls for both and
should not be simplified.
