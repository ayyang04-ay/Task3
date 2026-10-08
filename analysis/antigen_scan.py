import sys, re, openpyxl
from collections import Counter
BPAT = re.compile(r'\bB[/ ]', re.I)
VICYAM = re.compile(r'victoria|yamagata|b/bris|b/aus|b/phuket|b/colorado|b/wash', re.I)
for path in sys.argv[1:]:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    print("="*78); print("FILE:", path.split("/")[-1])
    for ws in wb.worksheets:
        # collect column-A labels and any 'virus' column values
        colA, viruses = [], []
        hdr = None
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if i == 0: hdr = [str(c) if c is not None else "" for c in row]
            if row and row[0] is not None: colA.append(str(row[0]))
            if hdr and "virus" in [h.lower() for h in hdr]:
                j = [h.lower() for h in hdr].index("virus")
                if len(row) > j and row[j] is not None: viruses.append(str(row[j]))
        pool = colA + viruses
        uniq = sorted(set(p for p in pool if re.search(r'/\d{4}|\(H\d\)|H\dN\d', p)))
        bhits = sorted(set(p for p in pool if BPAT.match(p.strip()) or VICYAM.search(p)))
        print(f"  SHEET '{ws.title}': {len(uniq)} antigen-like labels; B-LINEAGE HITS: {len(bhits)}")
        if bhits: print("     B:", bhits[:20])
        if uniq and len(uniq) <= 25: print("     labels:", uniq)
        elif uniq:
            sub = Counter()
            for u in uniq:
                m = re.search(r'(H\dN\d|\(H\d\))', u); sub[m.group(1) if m else 'unlabelled'] += 1
            print("     n_unique:", len(uniq), "subtype tally:", dict(sub), "| sample:", uniq[:3])
    wb.close()
