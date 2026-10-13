"""Reflow the grading document into the form the RL Studio grader field accepts.

RLS mangles hard-wrapped markdown: a paragraph broken across source lines comes
back with the breaks preserved as line breaks mid-sentence. This emits a flat
copy - one line per paragraph, one line per list item, one line per table row -
and replaces dashes that have previously rendered badly in that field.

    python3 build/flatten_grader.py grader/grader_prompt.md grader/grader_prompt_flat.md

What is preserved deliberately: standard markdown pipe tables, and the C-list
`1.`-`29.` numbering. An earlier over-flattened variant (C1.-C29. headings and
`=>` tables) was rejected - do not reintroduce it.
"""
import re
import sys

DASHES = {"—": "-", "–": "-", "−": "-", "→": "->"}

# Lines that must stand alone rather than being joined into a paragraph.
STANDALONE = re.compile(r"^\s*(#|\||>|```)")
# Lines that begin a new list item (ordered or bulleted), at any indent.
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def despace(text):
    for bad, good in DASHES.items():
        text = text.replace(bad, good)
    return text


def flatten(src):
    out = []
    for block in re.split(r"\n\s*\n", src.strip("\n")):
        lines = [ln.rstrip() for ln in block.split("\n") if ln.strip()]
        if not lines:
            continue
        buf = []
        for ln in lines:
            if STANDALONE.match(ln):
                if buf:
                    out.append(" ".join(buf))
                    buf = []
                out.append(ln.strip())
            elif LIST_ITEM.match(ln):
                if buf:
                    out.append(" ".join(buf))
                buf = [ln.strip()]
            else:
                buf.append(ln.strip())
        if buf:
            out.append(" ".join(buf))
        out.append("")
    return despace("\n".join(out).rstrip("\n") + "\n")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src = open(sys.argv[1], encoding="utf-8").read()
    flat = flatten(src)
    open(sys.argv[2], "w", encoding="utf-8").write(flat)
    longest = max(len(l) for l in flat.split("\n"))
    print(f"wrote {sys.argv[2]}  "
          f"{len(flat.splitlines())} lines, longest {longest} chars")
    for bad in DASHES:
        assert bad not in flat, f"unreplaced {bad!r}"
    print("no em/en dashes remain")


if __name__ == "__main__":
    main()
