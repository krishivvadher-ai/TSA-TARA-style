"""Pull one year's questions out of the original TSA paper so solutions can be written.

    python tools/worked_solutions/extract_year.py dump 2017 --papers <dir> --out <scratch dir>
        writes, for every question in both sets:
          <out>/PS01.txt ... text line by line with positions, plus the images on that page region
          <out>/PS01.png ... a picture of the whole question (for reading diagrams)
        and <out>/index.json (page and region of each question)

    python tools/worked_solutions/extract_year.py crop 2017 --papers <dir> --page 6 --rect 90 60 290 260 --name q04_weight
        saves a crop of the original paper to figures/<year>/<name>.png for use with fig(year, name, alt)
"""

import argparse
import io
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import build_tsa_sets as b  # noqa: E402

FIXES = {'¢': '£', 'Î': '–'}


def paper(papers, year):
    return fitz.open(Path(papers) / f'TSA-{year}-Section-1-Question-Paper.pdf')


def decode(t, shifted):
    if shifted:
        t = ''.join(chr(ord(c) + 29) for c in t)
        for k, v in FIXES.items():
            t = t.replace(k, v)
    return t


def dump(args):
    year = str(args.year)
    shifted = year in b.SHIFTED_YEARS
    src = paper(args.papers, year)
    pages = [b.page_spans(p, shifted) for p in src]
    starts = b.find_question_starts(pages)
    regions, left, right = b.question_regions(src, pages, starts)
    cls = json.loads((HERE.parent / 'classification.json').read_text())[year]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    index = {}
    for kind in ('PS', 'CT'):
        for n, q in enumerate(cls[kind], 1):
            tag = f'{kind}{n:02d}'
            lines = [f'{kind} {n} = original Q{q}']
            imgs = []
            for (p, y0, y1) in regions[q - 1]:
                lines.append(f'--- page {p}, region y {y0:.0f}-{y1:.0f}, x {left:.0f}-{right:.0f}')
                rows = []
                for blk in src[p].get_text('dict')['blocks']:
                    for l in blk.get('lines', []):
                        for s in l['spans']:
                            if not (y0 - 1 <= s['bbox'][1] < y1 + 1):
                                continue
                            t = decode(s['text'], shifted)
                            if not t.strip():
                                continue
                            st = ('B' if 'Bold' in s['font'] else '') + ('I' if 'Italic' in s['font'] else '')
                            rows.append((round(s['bbox'][1]), round(s['bbox'][0]), st, t))
                rows.sort()
                cur, buf = None, []
                for y, x, st, t in rows:
                    if cur is not None and abs(y - cur) > 3:
                        lines.append(' | '.join(buf)); buf = []
                    cur = y if not buf else cur
                    buf.append(f'[{x},{y}{"," + st if st else ""}] {t}')
                if buf:
                    lines.append(' | '.join(buf))
                for im in src[p].get_image_info():
                    r = im['bbox']
                    if r[1] >= y0 - 3 and r[3] <= y1 + 3:
                        imgs.append((p, [round(v) for v in r]))
                pix = src[p].get_pixmap(dpi=110, clip=fitz.Rect(left, y0 - 4, right, y1 + 4))
                pix.save(out / f'{tag}{"" if p == regions[q - 1][0][0] else "_p" + str(p)}.png')
            if imgs:
                lines.append('--- images (page, [x0 y0 x1 y1]): ' + ', '.join(f'{p} {r}' for p, r in imgs))
            (out / f'{tag}.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
            index[tag] = dict(orig=q, regions=[[p, round(a), round(c)] for p, a, c in regions[q - 1]],
                              x=[round(left), round(right)])
    (out / 'index.json').write_text(json.dumps(index, indent=1))
    print(f'wrote {len(index)} questions to {out}')


def crop(args):
    year = str(args.year)
    src = paper(args.papers, year)
    pix = src[args.page].get_pixmap(dpi=200, clip=fitz.Rect(*args.rect))
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    if args.colour:
        im = im.quantize(colors=64)
    else:
        im = im.convert('L').point(lambda v: 255 if v > 245 else v).quantize(colors=16)
    dest = HERE / 'figures' / year
    dest.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    im.save(buf, 'PNG', optimize=True)
    (dest / f'{args.name}.png').write_bytes(buf.getvalue())
    print(f'saved figures/{year}/{args.name}.png ({im.width}x{im.height}, {len(buf.getvalue()) // 1024} KB)')


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    d = sub.add_parser('dump')
    d.add_argument('year')
    d.add_argument('--papers', required=True)
    d.add_argument('--out', required=True)
    c = sub.add_parser('crop')
    c.add_argument('year')
    c.add_argument('--papers', required=True)
    c.add_argument('--page', type=int, required=True)
    c.add_argument('--rect', type=float, nargs=4, required=True)
    c.add_argument('--name', required=True)
    c.add_argument('--colour', action='store_true', help='keep colour (default is greyscale)')
    args = ap.parse_args()
    {'dump': dump, 'crop': crop}[args.cmd](args)


if __name__ == '__main__':
    main()
