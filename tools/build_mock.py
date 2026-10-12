"""Build the mock TSA papers from the questions chosen in tools/mock_selection.json (Mock 1) and
tools/mock2_selection.json (Mock 2).

    python tools/build_mock.py --papers <folder of question papers> --answers <folder of answer keys> [--mock Mock2]

Each mock set is 25 real past TSA Section 1 questions. Mock 1: the hardest question of every question type, with
the other places going to the next-hardest questions. Mock 2 (Problem Solving only): the hardest questions not in
Mock 1, whatever their type. Mock 3 (Problem Solving only): the questions that keep you thinking hard for longest,
none of them in Mock 1 or 2. Each question is cut from its original paper
exactly as printed, renumbered 1-25 with its source in brackets, e.g. "7 (2019 Q32)". Writes
TSA_Papers/TSA_<Mock>_<Set>.pdf and TSA_Answers/TSA_<Mock>_<Set>_Mark_Scheme.pdf.
"""

import argparse
import io
import json
from pathlib import Path

import fitz
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

import build_tsa_sets as B

HERE = Path(__file__).resolve().parent
MOCKS = {'Mock': ('mock_selection.json', 'Mock 1'), 'Mock2': ('mock2_selection.json', 'Mock 2'),
         'Mock3': ('mock3_selection.json', 'Mock 3')}
COPYRIGHT = '© UCLES 2008–2021 and © Cambridge University Press & Assessment 2022–2023'


class Source:
    """One original paper, prepared the same way as in build_tsa_sets.py."""

    def __init__(self, papers, year):
        path = papers / f'TSA-{year}-Section-1-Question-Paper.pdf'
        src = fitz.open(path)
        self.pages = [B.page_spans(p, year in B.SHIFTED_YEARS) for p in src]
        self.starts = B.find_question_starts(self.pages)
        self.regions, self.left, self.right = B.question_regions(src, self.pages, self.starts)
        bodies = sorted(b for b in (B.body_x(self.pages, s) for s in self.starts) if b)
        self.default_body = bodies[len(bodies) // 2]
        self.clean = fitz.open(path)
        for st in self.starts:
            r = fitz.Rect(st['span']['bbox'])
            r.y0 += 1
            r.y1 -= 1
            self.clean[st['page']].add_redact_annot(r)
        for p in self.clean:
            p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE)


def cover_pdf(kind, items, mock):
    st = B.styles()
    name = B.SETS[kind]['name']
    n = len(items)
    exact, mins = B.time_limit(kind, n)
    tara = B.TARA[kind]
    types = sorted({it['type'] for it in items})
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm,
                            topMargin=26 * mm, bottomMargin=18 * mm,
                            title=f'TSA {MOCKS[mock][1]} {name}', author='TSA practice set')
    story = [
        Paragraph(f'TSA {MOCKS[mock][1]}', st['year']),
        Spacer(1, 4),
        Paragraph(name, st['title']),
        Spacer(1, 8),
        Paragraph({'Mock': f'The hardest past TSA {name} question of every type, from all 16 papers (2008–2023)',
                   'Mock2': f'The hardest past TSA {name} questions not in Mock 1, any type, from all 16 papers (2008–2023)',
                   'Mock3': f'The longest, most sustained past TSA {name} questions, from all 16 papers (2008–2023)'}[mock],
                  st['sub']),
        Spacer(1, 22),
        B.summary_table([('Questions', str(n)), ('Total marks', str(n)), ('Time limit', f'{mins} minutes')],
                        [52 * mm, 52 * mm, 52 * mm]),
        Spacer(1, 20),
        Paragraph('Instructions', st['h']),
        Spacer(1, 4),
    ]
    bullets = [
        f'You have <b>{mins} minutes</b> to answer all <b>{n} questions</b>.',
        'Each question is worth <b>one mark</b>. There are no penalties for incorrect answers, '
        'so attempt every question.',
        'Each question has five options, A to E. Choose the one option you consider correct.',
        'Calculators are <b>not</b> permitted. You may use this paper for rough working.',
        'Every question is a real past TSA question. The year and number in brackets show where it '
        'comes from, e.g. <b>7 (2019 Q32)</b>.',
    ]
    story += [Paragraph(b, st['bullet'], bulletText='•') for b in bullets]
    story += [
        Spacer(1, 12),
        Paragraph('What is in this paper', st['h']),
        Spacer(1, 4),
        Paragraph({'Mock': f'At least one question of each of the {len(types)} {name} question types that have come up '
                           f'in past papers, chosen as the hardest of its type: ' + ', '.join(types) + '.',
                   'Mock2': f'The {n} {name} questions judged hardest of all those not already in Mock 1. Type does not '
                            'matter here, so questions that do not fit neatly into one type are included too.',
                   'Mock3': f'The {n} {name} questions judged to keep a strong candidate thinking hard for longest, '
                            'none of them in Mock 1 or Mock 2. Each needs several minutes of sustained reasoning, far more '
                            'than the 1¾ minutes a question gets on average, so expect not to finish: the paper trains '
                            'stamina and choosing which questions to leave.'}[mock], st['body']),
        Spacer(1, 10),
        Paragraph('How the time limit was set', st['h']),
        Spacer(1, 4),
        Paragraph(
            f'The time limit follows the TARA {name} module ({tara["questions"]} questions in '
            f'{tara["minutes"]} minutes), scaled to {n} questions: '
            f'{n} × {tara["minutes"]} ÷ {tara["questions"]} = {exact:.2f} minutes, '
            f'rounded to the nearest minute ({mins} minutes). These are hard questions, so expect to '
            'run short of time.', st['body']),
        Spacer(1, 22),
        Paragraph('Score: ________ / ' + str(n), st['h']),
        Spacer(1, 24),
        Paragraph(f'Questions {COPYRIGHT}. Reproduced from the TSA Oxford Section 1 question papers '
                  'for practice purposes.', st['small']),
    ]
    doc.build(story)
    return fitz.open('pdf', buf.getvalue())


def build_mock(kind, items, sources, mock):
    """Place each chosen question, cut from its own paper, one after another."""
    name = B.SETS[kind]['name']
    n = len(items)
    _, mins = B.time_limit(kind, n)
    out = cover_pdf(kind, items, mock)
    usable = B.BOTTOM - B.TOP
    left = min(sources[it['year']].left for it in items)
    right = max(sources[it['year']].right for it in items)
    page, y = None, None

    def new_page():
        nonlocal page, y
        page = out.new_page(width=B.PAGE_W, height=B.PAGE_H)
        y = B.TOP

    for new_no, it in enumerate(items, 1):
        s = sources[it['year']]
        q = it['orig']
        segs = s.regions[q - 1]
        heights = [(y1 - y0) + 6 for _, y0, y1 in segs]
        total = sum(heights) + 8 * (len(segs) - 1)
        if page is None or (y + total > B.BOTTOM and total <= usable) or y + heights[0] > B.BOTTOM:
            new_page()
        first = True
        for (p, y0, y1), h in zip(segs, heights):
            if y + h > B.BOTTOM and y > B.TOP:
                new_page()
            scale = min(1.0, usable / h, (right - left) / (s.right - s.left))
            clip = fitz.Rect(s.left, y0 - 3, s.right, y1 + 3)
            target = fitz.Rect(left, y, left + (s.right - s.left) * scale, y + h * scale)
            page.show_pdf_page(target, B.isolated_segment(s.clean, p, clip), 0, clip=clip)
            if first:
                st = s.starts[q - 1]
                base = y + (st['span']['origin'][1] - (y0 - 3)) * scale
                bx = min(B.body_x(s.pages, st) or s.default_body, s.default_body)
                label_no, label_src = str(new_no), f'({it["year"]} Q{q})'
                w_no = fitz.get_text_length(label_no, fontname='hebo', fontsize=11)
                w_src = fitz.get_text_length(label_src, fontname='helv', fontsize=8)
                x_end = left + (bx - 5 - s.left) * scale
                x0 = max(x_end - max(w_no, w_src), 12)
                page.insert_text((x0, base), label_no, fontname='hebo', fontsize=11)
                page.insert_text((x0, base + 10), label_src, fontname='helv', fontsize=8, color=B.GREY)
                first = False
            y += h * scale + 8
        y += B.GAP - 8

    if y + 30 > B.BOTTOM:
        new_page()
    end = 'END OF TEST'
    w = fitz.get_text_length(end, fontname='hebo', fontsize=11)
    page.insert_text(((B.PAGE_W - w) / 2, y + 16), end, fontname='hebo', fontsize=11)
    total_pages = out.page_count
    for i in range(1, total_pages):
        pg = out[i]
        pg.insert_text((left, 30), f'TSA {MOCKS[mock][1]} {name}', fontname='hebo', fontsize=9, color=B.GREY)
        right_txt = f'{n} questions  •  {n} marks  •  {mins} minutes'
        w = fitz.get_text_length(right_txt, fontname='helv', fontsize=9)
        pg.insert_text((B.PAGE_W - 40 - w, 30), right_txt, fontname='helv', fontsize=9, color=B.GREY)
        pg.draw_line((left, 36), (B.PAGE_W - 40, 36), color=(0.7, 0.7, 0.7), width=0.5)
        foot = f'Page {i + 1} of {total_pages}'
        w = fitz.get_text_length(foot, fontname='helv', fontsize=9)
        pg.insert_text((B.PAGE_W - 40 - w, 826), foot, fontname='helv', fontsize=9, color=B.GREY)
        pg.insert_text((left, 826), COPYRIGHT, fontname='helv', fontsize=7.5, color=B.GREY)
    out.set_metadata({'title': f'TSA {MOCKS[mock][1]} {name}', 'subject': f'{n} questions, {n} marks, {mins} minutes'})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--papers', required=True, type=Path)
    ap.add_argument('--answers', required=True, type=Path)
    ap.add_argument('--out', default=HERE.parent, type=Path)
    ap.add_argument('--mock', default='Mock', choices=list(MOCKS))
    args = ap.parse_args()
    selection = json.loads((HERE / MOCKS[args.mock][0]).read_text())
    years = sorted({it['year'] for kind in ('CT', 'PS') for it in selection.get(kind, [])})
    sources = {y: Source(args.papers, y) for y in years}
    keys = {y: B.read_answer_key(args.answers / f'TSA {y} Section 1 Answer Key.pdf') for y in years}
    for kind in ('CT', 'PS'):
        if kind not in selection:
            continue
        items = selection[kind]
        slug = B.SETS[kind]['slug']
        paper = build_mock(kind, items, sources, args.mock)
        paper.save(args.out / 'TSA_Papers' / f'TSA_{args.mock}_{slug}.pdf', garbage=4, deflate=True)
        answers = [keys[it['year']][it['orig']] for it in items]
        (args.out / 'TSA_Answers' / f'TSA_{args.mock}_{slug}_Mark_Scheme.pdf').write_bytes(
            B.mark_scheme_pdf(MOCKS[args.mock][1], kind, answers))
        print(kind, len(items), 'questions,', paper.page_count, 'pages, answers', ''.join(answers))


if __name__ == '__main__':
    main()
