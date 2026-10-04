"""Split TSA Oxford Section 1 papers into Critical Thinking and Problem Solving sets.

For every year this produces four PDFs:

    TSA_Papers/TSA_<year>_Critical_Thinking.pdf
    TSA_Papers/TSA_<year>_Problem_Solving.pdf
    TSA_Answers/TSA_<year>_Critical_Thinking_Mark_Scheme.pdf
    TSA_Answers/TSA_<year>_Problem_Solving_Mark_Scheme.pdf

Questions are cropped (as vector content) from the original papers, renumbered
1, 2, 3 ... within each set, and labelled with their original number in
brackets, e.g. "1 (Q3)". The mark schemes use the new numbering only.

Usage:
    python tools/build_tsa_sets.py --papers <dir of question papers> \
        --answers <dir of answer keys> --out <repo root>

Question papers must be named TSA-<year>-Section-1-Question-Paper.pdf and
answer keys TSA <year> Section 1 Answer Key.pdf.
"""

import argparse
import io
import json
import math
import re
import subprocess
from pathlib import Path

import pymupdf as fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).resolve().parent

# TARA (Test of Academic Reasoning for Admissions) module timings used to set
# the time limit for each set: Critical Thinking and Problem Solving are each
# 22 multiple-choice questions in 40 minutes.
TARA = {
    'CT': {'questions': 22, 'minutes': 40},
    'PS': {'questions': 22, 'minutes': 40},
}

SETS = {
    'CT': {'name': 'Critical Thinking', 'slug': 'Critical_Thinking'},
    'PS': {'name': 'Problem Solving', 'slug': 'Problem_Solving'},
}

# 2012-2014 papers use fonts whose character codes are offset by 29.
SHIFTED_YEARS = {'2012', '2013', '2014'}

HEADER_FOOTER = re.compile(
    r'UCLES|Cambridge University Press|Cambridge Assessment|Turn [Oo]ver|^TSA$|'
    r'TSAOxford|BLANK PAGE|^¨$|^PV\d|^Page \d+ / \d+|^END OF TEST$')

PAGE_W, PAGE_H = 595.0, 842.0
TOP, BOTTOM = 52.0, 806.0          # usable band for questions on output pages
GAP = 20.0                         # vertical gap between questions
GREY = (0.35, 0.35, 0.35)


def time_limit(kind, n):
    """Minutes allowed for n questions at the TARA rate, to the nearest minute."""
    exact = n * TARA[kind]['minutes'] / TARA[kind]['questions']
    return exact, int(math.floor(exact + 0.5))


def copyright_line(year):
    return f'© Cambridge University Press & Assessment {year}' if int(year) >= 2022 else f'© UCLES {year}'


# ---------------------------------------------------------------- extraction

def decode(text):
    if any(ord(c) < 32 and c not in '\n\t' for c in text):
        return ''.join(chr(ord(c) + 29) for c in text)
    return text


def page_spans(page, shifted):
    out = []
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for s in line['spans']:
                out.append(dict(text=decode(s['text']) if shifted else s['text'],
                                bbox=fitz.Rect(s['bbox']), font=s['font'], origin=s['origin']))
    return out


def is_header_footer(span):
    t = span['text'].strip()
    r = span['bbox']
    if not t:
        return True
    if HEADER_FOOTER.search(t) and (r.y0 > 770 or r.y1 < 60 or t in ('BLANK PAGE', 'END OF TEST')):
        return True
    if re.fullmatch(r'\d{1,2}', t) and (r.y1 < 58 or r.y0 > 785) and 200 < r.x0 < 400:
        return True
    return False


def visible_drawing(d):
    def white(c):
        return c is None or all(v > 0.98 for v in c)
    return not (white(d.get('fill')) and white(d.get('color')))


def find_question_starts(pages):
    """Bold question numbers 1..50 in the left margin, in reading order."""
    starts, want = [], 1
    for pno, spans in enumerate(pages):
        for s in sorted(spans, key=lambda s: (round(s['bbox'].y0), s['bbox'].x0)):
            t = s['text'].strip()
            if (re.fullmatch(r'\d{1,2}', t) and s['bbox'].x0 < 80 and 'Bold' in s['font']
                    and int(t) == want):
                starts.append(dict(q=want, page=pno, span=s))
                want += 1
    if len(starts) != 50:
        raise SystemExit(f'found {len(starts)} questions, expected 50')
    return starts


def question_regions(doc, pages, starts):
    """For each question, the list of (page, rect) segments that hold it."""
    items_by_page = []
    for pno, page in enumerate(doc):
        items = [s['bbox'] for s in pages[pno] if not is_header_footer(s)]
        items += [fitz.Rect(d['rect']) for d in page.get_drawings()
                  if visible_drawing(d) and d['rect'].width < 560 and d['rect'].height < 780]
        items += [fitz.Rect(i['bbox']) for i in page.get_image_info()]
        items_by_page.append([r for r in items if not r.is_empty or r.width or r.height])

    # Items up to this far above a question number (e.g. the top border of a
    # table level with the number) belong to that question.
    lead = 4.0
    regions, xs0, xs1 = [], [], []
    for i, st in enumerate(starts):
        nxt = starts[i + 1] if i + 1 < len(starts) else None
        # The final question never runs on: later pages hold only notices.
        last_page = nxt['page'] if nxt else st['page']
        segs = []
        for p in range(st['page'], last_page + 1):
            ytop = st['span']['bbox'].y0 - lead if p == st['page'] else 0
            ybot = nxt['span']['bbox'].y0 - lead if (nxt and p == nxt['page']) else PAGE_H
            inside = [r for r in items_by_page[p] if r.y0 >= ytop and r.y0 < ybot]
            if not inside:
                continue
            if p != st['page'] and max(r.y1 for r in inside) - min(r.y0 for r in inside) < 5:
                continue
            xs0 += [r.x0 for r in inside]
            xs1 += [r.x1 for r in inside]
            y0 = min(r.y0 for r in inside)
            y1 = max(r.y1 for r in inside)
            segs.append([p, y0, min(y1, ybot)])
        regions.append(segs)

    left = max(min(xs0) - 6, 20)
    right = min(max(xs1) + 6, PAGE_W - 15)
    return regions, left, right


def body_x(pages, st):
    nb = st['span']['bbox']
    line = [s['bbox'].x0 for s in pages[st['page']]
            if abs(s['bbox'].y0 - nb.y0) < 4 and s['bbox'].x0 > nb.x1 and s['text'].strip()]
    return min(line) if line else None


# ---------------------------------------------------------------- PDF parts

def styles():
    base = dict(fontName='Helvetica', leading=15, fontSize=11)
    return {
        'year': ParagraphStyle('year', fontName='Helvetica', fontSize=20, leading=26,
                               alignment=TA_CENTER, textColor=colors.HexColor('#444444')),
        'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=30, leading=36,
                                alignment=TA_CENTER),
        'sub': ParagraphStyle('sub', fontName='Helvetica', fontSize=11, leading=15,
                              alignment=TA_CENTER, textColor=colors.HexColor('#555555')),
        'h': ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=12, leading=16, spaceBefore=6),
        'body': ParagraphStyle('body', **base),
        'bullet': ParagraphStyle('bullet', leftIndent=14, bulletIndent=2, spaceAfter=4, **base),
        'small': ParagraphStyle('small', fontName='Helvetica', fontSize=9, leading=12,
                                textColor=colors.HexColor('#555555')),
        'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=12, leading=15, alignment=TA_CENTER),
        'cellb': ParagraphStyle('cellb', fontName='Helvetica-Bold', fontSize=12, leading=15,
                                alignment=TA_CENTER),
    }


def summary_table(rows, widths):
    st = styles()
    data = [[Paragraph(f'<b>{k}</b>', st['cell']) for k, _ in rows],
            [Paragraph(v, st['cell']) for _, v in rows]]
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#888888')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E8E8E8')),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    return t


def cover_pdf(year, kind, n):
    st = styles()
    name = SETS[kind]['name']
    exact, mins = time_limit(kind, n)
    tara = TARA[kind]
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm,
                            topMargin=28 * mm, bottomMargin=20 * mm,
                            title=f'TSA {year} {name}', author='TSA practice set')
    story = [
        Paragraph(f'TSA {year}', st['year']),
        Spacer(1, 4),
        Paragraph(name, st['title']),
        Spacer(1, 8),
        Paragraph(f'Questions taken from the TSA Oxford {year} Section 1 question paper', st['sub']),
        Spacer(1, 26),
        summary_table([('Questions', str(n)), ('Total marks', str(n)), ('Time limit', f'{mins} minutes')],
                      [52 * mm, 52 * mm, 52 * mm]),
        Spacer(1, 26),
        Paragraph('Instructions', st['h']),
        Spacer(1, 4),
    ]
    bullets = [
        f'You have <b>{mins} minutes</b> to answer all <b>{n} questions</b>.',
        'Each question is worth <b>one mark</b>. There are no penalties for incorrect answers, '
        'so attempt every question.',
        'Each question has five options, A to E. Choose the one option you consider correct.',
        'Calculators are <b>not</b> permitted. You may use this paper for rough working.',
        f'Questions are numbered 1 to {n} for this set. The number in brackets shows the '
        f'question’s number in the original TSA {year} paper, e.g. <b>1 (Q3)</b>.',
    ]
    story += [Paragraph(b, st['bullet'], bulletText='•') for b in bullets]
    story += [
        Spacer(1, 14),
        Paragraph('How the time limit was set', st['h']),
        Spacer(1, 4),
        Paragraph(
            f'The time limit follows the TARA {name} module ({tara["questions"]} questions in '
            f'{tara["minutes"]} minutes), scaled to the {n} questions in this set: '
            f'{n} × {tara["minutes"]} ÷ {tara["questions"]} = {exact:.2f} minutes, '
            f'rounded to the nearest minute ({mins} minutes).', st['body']),
        Spacer(1, 30),
        Paragraph('Score: ________ / ' + str(n), st['h']),
        Spacer(1, 40),
        Paragraph(f'Questions {copyright_line(year)}. Reproduced from the TSA Oxford {year} '
                  'Section 1 question paper for practice purposes.', st['small']),
    ]
    doc.build(story)
    return fitz.open('pdf', buf.getvalue())


def mark_scheme_pdf(year, kind, answers):
    st = styles()
    name = SETS[kind]['name']
    n = len(answers)
    _, mins = time_limit(kind, n)
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm,
                            topMargin=20 * mm, bottomMargin=16 * mm,
                            title=f'TSA {year} {name} Mark Scheme', author='TSA practice set')
    rows = [[Paragraph('<b>Question</b>', st['cell']), Paragraph('<b>Correct answer</b>', st['cell'])]]
    rows += [[Paragraph(str(i), st['cell']), Paragraph(a, st['cellb'])] for i, a in enumerate(answers, 1)]
    table = Table(rows, colWidths=[40 * mm, 50 * mm], repeatRows=1)
    style = [
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#888888')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D9D9D9')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]
    style += [('BACKGROUND', (0, r), (-1, r), colors.HexColor('#F3F3F3')) for r in range(2, n + 1, 2)]
    table.setStyle(TableStyle(style))
    story = [
        Paragraph(f'TSA {year} {name}', ParagraphStyle('t', parent=st['title'], fontSize=22, leading=28)),
        Paragraph('Mark Scheme', ParagraphStyle('t2', parent=st['year'], fontSize=16, leading=22)),
        Spacer(1, 8),
        Paragraph(f'Total marks: <b>{n}</b>  |  Time limit: <b>{mins} minutes</b>  |  '
                  'One mark for each correct answer; no marks deducted for incorrect answers.', st['sub']),
        Spacer(1, 12),
        table,
        Spacer(1, 12),
        Paragraph(f'Total: ________ / {n}', ParagraphStyle('tot', parent=st['h'], alignment=TA_CENTER)),
    ]
    doc.build(story)
    return buf.getvalue()


# ---------------------------------------------------------------- assembly

def isolated_segment(src, pno, clip):
    """One-page copy of src[pno] with everything outside clip removed.

    Cropping alone only hides the rest of the page; redacting it stops text
    from neighbouring questions surviving invisibly in the output.
    """
    seg = fitz.open()
    seg.insert_pdf(src, from_page=pno, to_page=pno)
    page = seg[0]
    w, h = page.rect.width, page.rect.height
    for r in (fitz.Rect(0, 0, w, clip.y0), fitz.Rect(0, clip.y1, w, h),
              fitz.Rect(0, clip.y0, clip.x0, clip.y1), fitz.Rect(clip.x1, clip.y0, w, clip.y1)):
        if not r.is_empty:
            page.add_redact_annot(r)
    page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_PIXELS,
                          graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED)
    return seg


def build_paper(year, kind, qnums, src, pages, starts, regions, left, right, default_body):
    name = SETS[kind]['name']
    n = len(qnums)
    _, mins = time_limit(kind, n)
    out = cover_pdf(year, kind, n)
    usable = BOTTOM - TOP

    page, y = None, None
    placed = []          # (output page index, new number, original number)

    def new_page():
        nonlocal page, y
        page = out.new_page(width=PAGE_W, height=PAGE_H)
        y = TOP

    for new_no, q in enumerate(qnums, 1):
        segs = regions[q - 1]
        heights = [(y1 - y0) + 6 for _, y0, y1 in segs]
        total = sum(heights) + 8 * (len(segs) - 1)
        if page is None or (y + total > BOTTOM and total <= usable):
            new_page()
        elif y + heights[0] > BOTTOM:
            new_page()
        first = True
        for (p, y0, y1), h in zip(segs, heights):
            if y + h > BOTTOM and y > TOP:
                new_page()
            scale = min(1.0, usable / h)
            clip = fitz.Rect(left, y0 - 3, right, y1 + 3)
            target = fitz.Rect(left, y, left + (right - left) * scale, y + h * scale)
            page.show_pdf_page(target, isolated_segment(src, p, clip), 0, clip=clip)
            if first:
                st = starts[q - 1]
                nb = st['span']['bbox']
                base = y + (st['span']['origin'][1] - (y0 - 3)) * scale
                bx = body_x(pages, st) or default_body
                bx = min(bx, default_body)
                label_no, label_orig = str(new_no), f'(Q{q})'
                w_no = fitz.get_text_length(label_no, fontname='hebo', fontsize=11)
                w_orig = fitz.get_text_length(label_orig, fontname='helv', fontsize=9.5)
                x_end = left + (bx - 5 - left) * scale
                x0 = max(x_end - (w_no + 3 + w_orig), 16)
                page.insert_text((x0, base), label_no, fontname='hebo', fontsize=11)
                page.insert_text((x0 + w_no + 3, base), label_orig, fontname='helv',
                                 fontsize=9.5, color=GREY)
                placed.append((out.page_count - 1, new_no, q))
                first = False
            y += h * scale + 8
        y += GAP - 8

    if y + 30 > BOTTOM:
        new_page()
    end = 'END OF TEST'
    w = fitz.get_text_length(end, fontname='hebo', fontsize=11)
    page.insert_text(((PAGE_W - w) / 2, y + 16), end, fontname='hebo', fontsize=11)

    total_pages = out.page_count
    for i in range(1, total_pages):
        pg = out[i]
        pg.insert_text((left, 30), f'TSA {year} {name}', fontname='hebo', fontsize=9, color=GREY)
        right_txt = f'{n} questions  •  {n} marks  •  {mins} minutes'
        w = fitz.get_text_length(right_txt, fontname='helv', fontsize=9)
        pg.insert_text((PAGE_W - 40 - w, 30), right_txt, fontname='helv', fontsize=9, color=GREY)
        pg.draw_line((left, 36), (PAGE_W - 40, 36), color=(0.7, 0.7, 0.7), width=0.5)
        foot = f'Page {i + 1} of {total_pages}'
        w = fitz.get_text_length(foot, fontname='helv', fontsize=9)
        pg.insert_text((PAGE_W - 40 - w, 826), foot, fontname='helv', fontsize=9, color=GREY)
        pg.insert_text((left, 826), copyright_line(year), fontname='helv', fontsize=7.5, color=GREY)
    out.set_metadata({'title': f'TSA {year} {name}', 'subject': f'{n} questions, {n} marks, {mins} minutes'})
    return out, placed


def read_answer_key(path):
    txt = subprocess.run(['pdftotext', '-layout', str(path), '-'], capture_output=True, text=True,
                         check=True).stdout
    txt = txt.split('score conversion')[0]
    key = {}
    for num, letter in re.findall(r'(?<![\d.])(\d{1,2})\s+([A-E])\b', txt):
        num = int(num)
        if num in key:
            raise SystemExit(f'{path}: question {num} appears twice')
        key[num] = letter
    if sorted(key) != list(range(1, 51)):
        raise SystemExit(f'{path}: expected answers for questions 1-50')
    return key


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--papers', required=True, type=Path)
    ap.add_argument('--answers', required=True, type=Path)
    ap.add_argument('--out', default=HERE.parent, type=Path)
    ap.add_argument('--years', nargs='*')
    args = ap.parse_args()

    classification = json.loads((HERE / 'classification.json').read_text())
    papers_dir = args.out / 'TSA_Papers'
    answers_dir = args.out / 'TSA_Answers'
    papers_dir.mkdir(parents=True, exist_ok=True)
    answers_dir.mkdir(parents=True, exist_ok=True)
    report = {}

    for year in args.years or sorted(classification):
        src_path = args.papers / f'TSA-{year}-Section-1-Question-Paper.pdf'
        key = read_answer_key(args.answers / f'TSA {year} Section 1 Answer Key.pdf')
        src = fitz.open(src_path)
        pages = [page_spans(p, year in SHIFTED_YEARS) for p in src]
        starts = find_question_starts(pages)
        regions, left, right = question_regions(src, pages, starts)
        bodies = sorted(b for b in (body_x(pages, s) for s in starts) if b)
        default_body = bodies[len(bodies) // 2]

        # Remove the original question numbers so they can be replaced.
        clean = fitz.open(src_path)
        for st in starts:
            r = fitz.Rect(st['span']['bbox'])
            r.y0 += 1
            r.y1 -= 1
            clean[st['page']].add_redact_annot(r)
        for p in clean:
            p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,
                               graphics=fitz.PDF_REDACT_LINE_ART_NONE)

        cls = classification[year]
        assert sorted(cls['CT'] + cls['PS']) == list(range(1, 51)), year
        report[year] = {}
        for kind in ('CT', 'PS'):
            qnums = cls[kind]
            slug = SETS[kind]['slug']
            paper, placed = build_paper(year, kind, qnums, clean, pages, starts, regions, left, right,
                                        default_body)
            paper.save(papers_dir / f'TSA_{year}_{slug}.pdf', garbage=4, deflate=True)
            answers = [key[q] for q in qnums]
            (answers_dir / f'TSA_{year}_{slug}_Mark_Scheme.pdf').write_bytes(
                mark_scheme_pdf(year, kind, answers))
            report[year][kind] = dict(questions=qnums, answers=answers, pages=paper.page_count,
                                      placed=placed, minutes=time_limit(kind, len(qnums))[1])
        print(year, {k: (len(v['questions']), v['pages'], v['minutes']) for k, v in report[year].items()})
    return report


if __name__ == '__main__':
    main()
