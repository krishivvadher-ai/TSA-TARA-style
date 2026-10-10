from wslib import *

Y = 2011
Q = []


def _grey(points):
    """Grey shading like the paper's (ink at low opacity, so it works in both themes)."""
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in points)
    return f'<polygon points="{pts}" class="k-ink f-ink" fill-opacity="0.32" stroke-width="0"/>'


# ---------------------------------------------------------------- 18 (Q37)
def _receipt(x, top, bottom, title, rows, total, total_col):
    zig = ' '.join(f'L{x + 260 - i * 13} {bottom + (12 if i % 2 else 0)}' for i in range(21))
    parts = [path(f'M{x} {top} L{x + 260} {top} L{x + 260} {bottom} {zig} L{x} {bottom} Z', k='ink', fill='paper', sw=1.8)]
    lab = [text(x + 130, top + 28, title, k='ink', size=17, font='print')]
    y = top + 60
    for name, amt, col in rows:
        lab.append(text(x + 16, y, name, k=col, size=16, anchor='start'))
        lab.append(text(x + 244, y, amt, k=col, size=16, anchor='end'))
        y += 26
    parts.append(line(x + 16, bottom - 44, x + 244, bottom - 44, k='ink', w=1.4, dash=True))
    lab.append(text(x + 16, bottom - 16, 'TOTAL', k='ink', size=17, anchor='start', font='print'))
    lab.append(text(x + 244, bottom - 14, total, k=total_col, size=22, anchor='end', font='scrawl'))
    return parts, lab


def _receipts():
    p1, l1 = _receipt(30, 20, 196, '7 ITEMS (before)', [('order', '£74.60', 'ink'), ('P&P, £50–£74.99 band', '£12.00', 'ink')],
                      '£86.60', 'red')
    p2, l2 = _receipt(340, 20, 196, '8 ITEMS (after)', [('order + £1.25', '£75.85', 'ink'), ('P&P, £75–£99.99 band', '£15.00', 'ink'),
                                                         ('half price P&P', '£7.50', 'green')], '£83.35', 'green')
    lab = [text(320, 246, '£86.60 − £83.35 = £3.25 cheaper', k='pen', size=21, font='scrawl')]
    return svg(630, 258, rough(*p1, *p2) + ''.join(l1 + l2 + lab),
               'Two receipts: before, 74.60 plus 12.00 postage makes 86.60; after, 75.85 plus half of 15.00 makes 83.35')


Q.append(dict(
    n=18, orig=37, answer='A', topic='Tables & bands',
    question=f"""<p>I often order items from a mail order catalogue. The charges for postage and packing ({hl('to be added to the order value', 'y', 1)}) are as follows:</p>
{table([['less than £25.00', '£4.50'], ['£25.00 to £49.99', '£8.50'], [hl('£50.00 to £74.99', 'g'), hl('£12.00', 'g')],
        [hl('£75.00 to £99.99', 'p'), hl('£15.00', 'p')], ['£100.00 and over', '£17.50']], head=['Order value:', ''])}
<p>Just before sending off my latest order, I noticed that the current catalogue offers {hl('half price postage and packing for orders of 8 or more items', 'y', 2)}. My order was for {hl('7 items', 'g', 3)}, with
an order value of {hl('£74.60', 'g', 4)}. I could not find anything else I wanted, so I just added the
cheapest item in the catalogue ({hl('priced at £1.25', 'p', 5)}) to my order.</p>
<p class="stem">By how much did adding the extra item to my order {hl('reduce the total cost', 'b', 6)}?</p>""",
    options={'A': '£3.25', 'B': '£4.50', 'C': '£4.75', 'D': '£5.75', 'E': '£6.25'},
    notes=[(1, 'y', 'Total cost = order value + postage and packing (P&amp;P).'),
           (2, 'y', '8 items or more: P&amp;P is halved.'),
           (3, 'g', '7 items: one short of the deal.'),
           (4, 'g', 'In the £50.00–£74.99 band: P&amp;P £12.00.'),
           (5, 'p', 'Adding it pushes the order to £75.85: into a <b>dearer</b> band!'),
           (6, 'b', 'Old total − new total. Remember you also pay for the extra item.')],
    steps=[
        f"""<p><b>Before</b> (7 items, no discount):</p>
{calc(f'£74.60 {ar()} £50–£74.99 band {ar()} P&amp;P £12.00', 'total = 74.60 + 12.00 = <b>£86.60</b>')}""",
        f"""<p><b>After</b> (8 items, half-price P&amp;P):</p>
{calc(f'74.60 + 1.25 = £75.85 {ar()} £75–£99.99 band {ar()} P&amp;P £15.00',
      'half price: £15.00 ÷ 2 = £7.50', 'total = 75.85 + 7.50 = <b>£83.35</b>')}
{note('The extra item moves the order up a band (£15, not £12) before the halving. Easy to miss!', 'trap')}""",
        f"""{_receipts()}{calc(f'86.60 − 83.35 = {boxed("£3.25")}')}""",
    ],
    answer_text='£3.25: £86.60 before against £83.35 after.',
    why={'B': '£4.50 = 12.00 − 7.50: the drop in P&amp;P only. It forgets you pay £1.25 for the extra item.',
         'C': '£4.75 keeps the old £12 band and halves it to £6 (86.60 − 81.85). But £75.85 is in the £15 band.',
         'D': '£5.75 = 12.00 − 7.50 + 1.25: it <b>adds</b> the item’s price to the saving instead of taking it off.',
         'E': '£6.25 = 7.50 − 1.25: it treats half of £15 as the saving, but before the change you were paying £12, not £15.'},
    fast='Before: 74.60 + 12 = 86.60. After: 75.85 + 15 ÷ 2 = 83.35. Saved 3.25.',
))


# ---------------------------------------------------------------- 19 (Q38)
def _structures():
    O = (70, 240)
    xN, yN = 355.7, 123.4
    parts = [line(O[0], O[1], 610, O[1], k='ink', head=True), line(O[0], O[1], O[0], 24, k='ink', head=True),
             line(70, 240, 560, 40, k='orange', w=3), line(70, 170, 560, 90, k='pen', w=3),
             line(xN, yN, xN, 240, k='red', w=2, dash=True), circle(xN, yN, 6, k='red', fill='paper', sw=2.4)]
    lab = [text(568, 44, 'structure 1', k='orange', size=17, anchor='start'),
           text(568, 96, 'structure 2', k='pen', size=17, anchor='start'),
           text(62, 175, 'fixed', k='pen', size=15, anchor='end'), text(62, 193, 'cost', k='pen', size=15, anchor='end'),
           text(40, 130, 'total cost', k='muted', size=15, rotate=-90),
           text(600, 262, 'number of brochures', k='muted', size=15, anchor='end'),
           text(xN, 262, 'N = same cost (option A)', k='red', size=16),
           text(210, 214, '1 cheaper here', k='orange', size=17, font='scrawl'),
           text(470, 214, '2 cheaper here', k='pen', size=17, font='scrawl'),
           text(xN, 290, 'is 500 left or right of N? That decides it.', k='ink', size=17)]
    return svg(660, 304, rough(*parts) + ''.join(lab),
               'Cost graph: structure 1 is a steep line from zero, structure 2 starts at a fixed cost and rises slowly; they cross at the break-even number N')


Q.append(dict(
    n=19, orig=38, answer='A', topic='Comparing deals',
    question=f"""<p>John wishes to have {hl('500 copies', 'g', 1)} of a brochure printed and is offered a choice of two price
structures:</p>
<p>1. {hl('An equal cost for each brochure printed, regardless of number.', 'y', 2)}<br>
2. {hl('An initial fixed cost followed by a lower cost than structure 1 for each brochure.', 'y', 3)}</p>
<p class="stem">Which one of the following sets of information would be {hl('sufficient', 'b', 4)} for him to be able to
decide which of the two price structures would be least expensive?</p>""",
    options={'A': 'The number of brochures for which the total bill would be the same by both structure 1 and structure 2.',
             'B': 'An example showing the cost of 500 brochures for structure 1 and 200 brochures using structure 2.',
             'C': 'The cost per brochure using structure 1 and the initial cost using structure 2.',
             'D': 'An example showing the cost of 200 brochures using structure 1 and 200 brochures using structure 2.',
             'E': 'The cost of 1 brochure using structure 1 and 2 brochures using structure 2.'},
    notes=[(1, 'g', 'The number that matters: 500.'),
           (2, 'y', 'Structure 1: cost = price × number. A line from 0, fairly steep.'),
           (3, 'y', 'Structure 2: starts higher (the fixed cost) but climbs more slowly.'),
           (4, 'b', 'It must settle the question <b>whatever</b> the actual prices turn out to be.')],
    steps=[
        f"""<p>Sketch both structures as cost lines:</p>{_structures()}
<p>Structure 2 starts higher but grows more slowly, so the lines cross exactly once, at some number N. Below N structure 1
is cheaper; above N structure 2 is cheaper.</p>""",
        f"""<p>So knowing N is all John needs: compare it with 500. That is option {boxed('A')}.</p>""",
        f"""<p>Check the others really aren’t enough:</p>
<ul><li>B: structure 2’s cost for 200 doesn’t tell you its cost for 500, because you can’t split the fixed part from the per-brochure part.</li>
<li>C: structure 2’s per-brochure price is missing.</li>
<li>D: tells you which is cheaper at 200 only. If structure 1 wins at 200, structure 2 could still win at 500.</li>
<li>E: 2 brochures by structure 2 mixes up the fixed cost and the price per brochure.</li></ul>""",
    ],
    answer_text='A: the break-even number tells you which structure is cheaper on each side of it, so you just compare it with 500.',
    why={'B': 'One cost for structure 2 (at 200) can’t be split into fixed cost and price per brochure, so its cost for 500 is unknown.',
         'C': 'Structure 2’s price per brochure is missing, so its total for 500 can’t be found.',
         'D': 'This only compares the two at 200 brochures. If structure 1 is cheaper there, structure 2 might still be cheaper at 500.',
         'E': 'The cost of 2 brochures by structure 2 is fixed cost + 2 × price: one total, two unknowns. Not enough.'},
    fast='Two straight lines cross once. Know the crossing point and you know which is cheaper on each side of it. A.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _net_labels():
    s = 2.0
    T = lambda x, y: (40 + (x - 216.8) * s, 20 + (y - 89.8) * s)
    R = lambda x0, y0, x1, y1: [T(x0, y0), T(x1, y0), T(x1, y1), T(x0, y1)]
    parts = [_grey([T(251.6, 89.8), T(251.6, 135.0), T(363.8, 135.0)]), _grey(R(307.7, 135.0, 363.8, 180.1)),
             _grey(R(251.6, 202.7, 363.8, 225.3)),
             _grey([T(251.6, 135.0), T(240.1, 157.6), T(251.6, 180.1)]), _grey([T(363.8, 180.1), T(375.3, 202.7), T(363.8, 225.3)])]
    outline = [poly(R(251.6, 89.8, 363.8, 225.3), k='ink', sw=2), poly([T(251.6, 89.8), T(363.8, 135.0)], k='ink', sw=1.8, closed=False),
               poly([T(251.6, 135.0), T(363.8, 135.0)], k='ink', sw=1.8, closed=False),
               poly([T(251.6, 180.1), T(363.8, 180.1)], k='ink', sw=1.8, closed=False),
               poly([T(251.6, 202.7), T(363.8, 202.7)], k='ink', sw=1.8, closed=False),
               poly([T(307.7, 135.0), T(307.7, 180.1)], k='ink', sw=1.8, closed=False),
               poly([T(251.6, 135.0), T(216.8, 157.6), T(251.6, 180.1)], k='ink', sw=1.8, closed=False),
               poly([T(251.6, 135.0), T(240.1, 157.6), T(251.6, 180.1)], k='ink', sw=1.2, closed=False),
               poly([T(363.8, 180.1), T(398.7, 202.7), T(363.8, 225.3)], k='ink', sw=1.8, closed=False),
               poly([T(363.8, 180.1), T(375.3, 202.7), T(363.8, 225.3)], k='ink', sw=1.2, closed=False)]
    lx = 432
    lab = [text(lx, T(0, 112)[1] + 6, 'P: diagonal face', k='pen', size=18, anchor='start'),
           text(lx, T(0, 157.5)[1] + 6, 'Q: half and half', k='pen', size=18, anchor='start'),
           text(lx, T(0, 203)[1] - 4, 'R: striped face', k='pen', size=18, anchor='start'),
           text(lx, T(0, 203)[1] + 18, '(white next to Q,', k='muted', size=15, anchor='start'),
           text(lx, T(0, 203)[1] + 36, ' grey at the card’s edge)', k='muted', size=15, anchor='start'),
           text(100, 236, 'left end:', k='red', size=16, anchor='end'), text(100, 256, 'sliver on Q', k='red', size=16, anchor='end'),
           text(lx, 304, 'right end: sliver on R', k='red', size=16, anchor='start'),
           text(40, 318, 'P’s top edge folds round to meet R’s bottom edge', k='muted', size=16, anchor='start')]
    parts.append(arrow(lx - 4, 298, T(385, 214)[0] + 4, T(385, 214)[1] + 8, k='red', bend=0.2))
    return svg(660, 328, rough(*outline) + ''.join(parts) + ''.join(lab),
               'The net with its long faces named: P with a diagonal grey triangle, Q half white half grey, R a white strip and a grey strip; the left end triangle has its grey sliver on Q and the right end on R')


def _view(ox, oy, s, shade):
    """B/E-style view: right-hand end triangle and the striped face. shade 'top' (B) or 'bottom' (E)."""
    P = lambda x, y: (ox + x * s, oy + y * s)
    BL, Tp, BR, T2, BR2 = P(0, 83.5), P(25.8, 43.7), P(51.6, 83.5), P(111.5, 0), P(137.3, 39.8)
    m1, m2, ap = P(38.7, 63.6), P(124.4, 19.9), P(25.8, 70.3)
    g = [_grey([Tp, ap, BR])]
    g.append(_grey([Tp, m1, m2, T2] if shade == 'top' else [m1, BR, BR2, m2]))
    ol = [poly([BL, Tp, BR], k='ink', sw=2), poly([Tp, T2, BR2, BR], k='ink', sw=2, closed=False),
          line(*m1, *m2, k='ink', w=1.6), poly([BR, ap, Tp], k='ink', sw=1.2, closed=False)]
    return ol, g


def _unfold():
    parts, grey, lab = [], [], []
    # the turned piece: right flap + R, upside down
    x0, y0, w, h = 150, 50, 250, 30
    grey += [_grey([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)]), _grey([(x0, y0), (x0 - 24, y0 + h), (x0, y0 + 2 * h)])]
    parts += [rect(x0, y0, w, 2 * h, k='ink', sw=2), line(x0, y0 + h, x0 + w, y0 + h, k='ink', w=1.6),
              poly([(x0, y0), (x0 - 72, y0 + h), (x0, y0 + 2 * h)], k='ink', sw=2, closed=False),
              poly([(x0, y0), (x0 - 24, y0 + h), (x0, y0 + 2 * h)], k='ink', sw=1.2, closed=False)]
    lab += [text(x0 + w + 10, y0 + 20, '← grey half (meets P)', k='ink', size=15, anchor='start'),
            text(x0 + w + 10, y0 + 50, '← white half (meets Q)', k='ink', size=15, anchor='start'),
            text(x0 + 60, 32, 'right-hand flap + R, turned upside down', k='pen', size=17),
            text(x0 - 36, y0 + 2 * h + 22, 'end', k='red', size=15)]
    # B and E
    for ox, shade, title, col in ((70, 'top', 'B: grey along the top edge ✓', 'green'), (380, 'bottom', 'E: grey along the bottom edge ✗', 'red')):
        ol, g = _view(ox, 170, 1.45, shade)
        parts += ol
        grey += g
        lab.append(text(ox + 100, 318, title, k=col, size=17, font='scrawl'))
    parts.append(arrow(260, 130, 200, 196, k='green', bend=0.15))
    lab.append(text(300, 160, 'same layout, just tilted', k='green', size=15, anchor='start'))
    return svg(640, 332, rough(*parts) + ''.join(grey) + ''.join(lab),
               'The right-hand flap and striped face turned upside down have the grey stripe on top; view B matches this, view E has the stripe on the wrong side')


Q.append(dict(
    n=20, orig=42, answer='E', topic='Nets & folding',
    question=f"""<p>The piece of card shown below is {hl('folded to make a box with a triangular cross-section', 'y', 1)}.</p>
{fig(Y, 'ps_q20_net', 'The net: three long strips (a diagonally shaded strip, a half-shaded strip and a strip of two thin bands, white then grey) with a triangular end flap on each side, each flap with a thin grey sliver along its fold', 280)}
<p class="stem">Which one of the views below can {hl('<b>not</b>', 'b', 2)} be of this box?</p>
{fig(Y, 'ps_q20_opts', 'Five drawings A to E of the triangular box, each showing one end triangle and one long face with different grey shading', 440)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'The three long strips become the three long faces; the two triangles become the ends.'),
           (2, 'b', 'Four views are real. Find the fake.')],
    steps=[
        f"""<p>Name the parts of the net. Each end triangle has a thin grey sliver along the edge where it is attached, so the
sliver tells you which long face it touches:</p>{_net_labels()}""",
        f"""<p>B and E show the same two faces: an end whose sliver sits on the striped face R (so it’s the <b>right-hand end</b>)
and R itself. They are mirror images, so at most one of them is right.</p>""",
        f"""<p>Folding never flips a face over: you always see the printed side. So two faces that share an edge look just like
they do in the net, only turned round. Turn the right-hand flap and R upside down, so the end is on the left as in the
views. The grey stripe is now on <b>top</b>:</p>{_unfold()}""",
        f"""<p>Quick check of the rest:</p>
<ul><li>A: right-hand end (sliver on R, here the bottom) with P. P’s grey triangle comes to a point at the right-hand end and is widest at the far end. {tick()}</li>
<li>C: right-hand end (sliver on the hidden face R) with Q. Q’s grey half is its right-hand half, next to that end. {tick()}</li>
<li>D: left-hand end (sliver on Q, here the bottom) with P. P’s grey is widest at the left end and runs along the edge it shares with Q. {tick()}</li></ul>
{calc(f'cannot be this box = {boxed("E")}')}""",
    ],
    answer_text='View E: its striped face has the grey band on the wrong side (it is B mirrored).',
    why={'A': 'Real: the right-hand end with the diagonal face P, whose grey triangle is a point at that end and widest at the far end.',
         'B': 'Real: the right-hand end with the striped face R, grey band along the top edge, exactly as the turned net shows.',
         'C': 'Real: the right-hand end (its sliver on the hidden striped face) with face Q, whose grey half is next to that end.',
         'D': 'Real: the left-hand end (sliver on Q, the bottom) with the diagonal face P, grey widest at that end.'},
    fast='B and E are mirror images (end + striped face), so one is fake. Turn the net upside down so the right-hand flap is on the left: R’s grey stripe is on top. That’s B, so E is impossible.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _spanish():
    X = lambda n: 50 + n * 13.5
    segs = [(14, 'French 14', 'b'), (9, 'German 9', 'g'), (13, 'Italian 13', 'o'), (4, 'M 4', 'v')]
    parts, lab, run = [], [], 0
    for n, t, f in segs:
        parts.append(rect(X(run), 60, X(run + n) - X(run), 40, k='ink', fill=f, sw=1.8))
        lab.append(text((X(run) + X(run + n)) / 2, 86, t, k='ink', size=15))
        run += n
    parts.append(brace(X(0), X(14), 108, '14 out of 40', k='red', size=18))
    lab += [text(X(20), 40, 'all 40 pupils who take Spanish', k='pen', size=17),
            text(X(38), 132, 'M = Mandarin', k='muted', size=14),
            text(X(20), 168, '14 ÷ 40 = 0.35 = 35%', k='pen', size=21, font='scrawl')]
    return svg(620, 182, rough(*parts) + ''.join(lab),
               'Bar of the 40 Spanish pupils split into French 14, German 9, Italian 13 and Mandarin 4; 14 out of 40 is 35 percent')


Q.append(dict(
    n=21, orig=43, answer='C', topic='Percentages from tables',
    question=f"""<p>At Marland College, all 120 pupils in year 11 take two languages at GCSE. The table
below shows the numbers of pupils taking each language combination.</p>
{table([['<i>Mandarin</i>', '9', '3', '2', hl('4', 'p', 3)], [hl('<i>Spanish</i>', 'g'), hl('14', 'g', 2), hl('9', 'g'), hl('13', 'g'), ''],
        ['<i>Italian</i>', '13', '19', '', ''], ['<i>German</i>', '24', '', '', '']],
       head=['', '<i>French</i>', '<i>German</i>', '<i>Italian</i>', hl('<i>Spanish</i>', 'p')])}
<p class="stem">What percentage {hl('of those taking Spanish', 'b', 1)} are also taking French? (Give your answer to
the nearest 1% if necessary).</p>""",
    options={'A': '12%', 'B': '23%', 'C': '35%', 'D': '39%', 'E': '54%'},
    notes=[(1, 'b', 'The whole (100%) is <b>everyone who takes Spanish</b>, not all 120 pupils.'),
           (2, 'g', 'The part: Spanish with French = 14.'),
           (3, 'p', 'Spanish appears twice in the table, as a row <b>and</b> as a column. Don’t miss Mandarin + Spanish = 4.')],
    steps=[
        f"""<p>Find everyone taking Spanish: the Spanish row and the Spanish column.</p>
{calc('Spanish row: 14 (French) + 9 (German) + 13 (Italian) = 36', 'Spanish column: 4 (Mandarin)',
      'total taking Spanish = 36 + 4 = <b>40</b>')}""",
        f"""{_spanish()}
{calc(f'{frac(14, 40)} = {frac(35, 100)} = {boxed("35%")}')}
{note('Dividing by 40 is the same as multiplying by 2.5: 14 × 2.5 = 35.', 'tip')}
{note('The table only adds up to 110, not 120. That doesn’t matter: we only need the Spanish pupils.', 'check')}""",
    ],
    answer_text='35%: 14 of the 40 Spanish pupils also take French.',
    why={'A': '12% is 14 out of all 120 pupils. The question only asks about the Spanish pupils.',
         'B': '23% is 14 out of the 60 French pupils: the wrong way round.',
         'D': '39% is 14 out of 36: it misses the 4 Mandarin + Spanish pupils hiding in the Spanish column.',
         'E': '54% would mean more than half the Spanish pupils take French: about 22 of the 40. Only 14 do.'},
    fast='Spanish = 14 + 9 + 13 + 4 = 40. 14 ÷ 40 = 35%.',
))


# ---------------------------------------------------------------- 22 (Q44)
PTS = {'A': (209.4, 426.5), 'B': (399.9, 427.3), 'C': (301.5, 568.5), 'D': (345.1, 506.5), 'E': (259.1, 503.9), 'O': (301.5, 481.0)}
EDGES = [('A', 'B'), ('B', 'D'), ('D', 'C'), ('C', 'E'), ('E', 'A'), ('A', 'O'), ('O', 'D'), ('B', 'O'), ('O', 'E'), ('C', 'O')]


def _paths_labelled():
    s = 1.6
    P = {k: (30 + (x - 209.4) * s, 34 + (y - 426.5) * s) for k, (x, y) in PTS.items()}
    parts = [line(*P[a], *P[b], k='ink', w=2.4) for a, b in EDGES]
    parts.append(circle(*P['O'], 7, k='red', fill='paper', sw=2.6))
    parts.append(rect(P['O'][0] - 10, P['O'][1] - 46, 20, 10, k='ink', fill='ink', sw=1))
    lab = [text(P['A'][0] - 4, P['A'][1] - 10, 'A', k='pen', size=20, font='print'),
           text(P['B'][0] + 4, P['B'][1] - 10, 'B', k='pen', size=20, font='print'),
           text(P['C'][0], P['C'][1] + 24, 'C', k='pen', size=20, font='print'),
           text(P['D'][0] + 12, P['D'][1] + 4, 'D', k='pen', size=20, font='print', anchor='start'),
           text(P['E'][0] - 12, P['E'][1] + 4, 'E', k='pen', size=20, font='print', anchor='end'),
           text(P['O'][0], P['O'][1] - 14, 'O', k='red', size=18, font='print'),
           text(380, 70, 'O = front door (start and finish)', k='red', size=16, anchor='start'),
           text(380, 100, 'A, B, C = corners of the grounds', k='ink', size=16, anchor='start'),
           text(380, 130, 'D, E = where the long paths', k='ink', size=16, anchor='start'),
           text(380, 150, 'meet the sides', k='ink', size=16, anchor='start'),
           text(380, 190, 'lines through O: A–O–D, B–O–E,', k='muted', size=15, anchor='start'),
           text(380, 210, 'and C–O (stops at the door)', k='muted', size=15, anchor='start')]
    return svg(660, 290, rough(*parts) + ''.join(lab),
               'The path network labelled: corners A, B, C; D on side BC, E on side CA; O the front door where A-D, B-E and C-O meet')


def _triangles():
    s = 0.64
    tris = [('ABO', 'y', 'corner'), ('AEO', 'y', 'corner'), ('CEO', 'y', 'corner'), ('CDO', 'y', 'corner'),
            ('BDO', 'y', 'corner'), ('ACO', 'y', 'corner'), ('BCO', 'y', 'corner'), ('ABD', 'g', 'side'),
            ('ABE', 'g', 'side'), ('ACD', 'g', 'side'), ('BCE', 'g', 'side'), ('ABC', 'p', 'no O')]
    parts, lab = [], []
    for i, (name, f, kind) in enumerate(tris):
        ox, oy = 28 + (i % 4) * 152, 34 + (i // 4) * 142
        P = {k: (ox + (x - 209.4) * s, oy + (y - 426.5) * s) for k, (x, y) in PTS.items()}
        parts.append(poly([P[c] for c in name], k='red' if f == 'p' else 'ink', fill=f, sw=2.2))
        parts += [line(*P[a], *P[b], k='muted', w=1.2) for a, b in EDGES]
        parts.append(circle(*P['O'], 4, k='red', fill='paper', sw=2))
        ok = '✗' if f == 'p' else '✓'
        lab.append(text(ox + 61, oy + 112, f'{name} {ok}', k='red' if f == 'p' else 'ink', size=16, font='print'))
        lab.append(text(ox + 61, oy + 130, {'corner': 'O at a corner', 'side': 'O on a side', 'no O': 'misses the door'}[kind],
                        k='red' if f == 'p' else ('pen' if kind == 'corner' else 'green'), size=14))
    return svg(620, 466, rough(*parts) + ''.join(lab),
               'Twelve small copies of the paths, each with one triangle shaded: seven with the door at a corner, four with the door on a side, and the big triangle ABC which misses the door')


Q.append(dict(
    n=22, orig=44, answer='D', topic='Counting shapes',
    question=f"""<p>The diagram below shows Morden Hall and the network of paths within the grounds.</p>
{fig(Y, 'ps_q22_paths', 'A large triangle of paths with three inner paths meeting just below Morden Hall', 260)}
<p>When the owner takes his dog for a walk he always {hl('starts and finishes at the intersection outside the front door', 'y', 1)} and (keeping to the paths) walks {hl('one complete triangular route', 'y', 2)}.</p>
<p class="stem">{hl('How many different routes', 'b', 4)} does he have to choose from? ({hl('Clockwise and anticlockwise around the same triangle counts as one route only.', 'p', 3)})</p>""",
    options={'A': '5', 'B': '7', 'C': '10', 'D': '11', 'E': '12'},
    notes=[(1, 'y', 'The front door is the point where the three inside paths meet. Every route must pass through it.'),
           (2, 'y', 'A route = walking right round one triangle in the picture.'),
           (3, 'p', 'So just count triangles. Don’t double them.'),
           (4, 'b', 'Triangles the door lies on: at a corner <b>or</b> part way along a side.')],
    steps=[
        f"""<p>Label the points so the triangles are easy to name:</p>{_paths_labelled()}""",
        f"""<p>Triangles with the door O <b>at a corner</b>:</p>
{calc('the 5 small ones: ABO, AEO, CEO, CDO, BDO', 'two small ones joined: ACO, BCO', '= <b>7</b>')}
<p>Triangles with O <b>part way along a side</b> (he starts in the middle of a side and walks all the way round):</p>
{calc('side A–D passes through O: ABD, ACD', 'side B–E passes through O: ABE, BCE', '= <b>4</b>')}""",
        f"""{_triangles()}
{calc(f'7 + 4 = {boxed("11")}', 'the big triangle ABC never passes the door, so it doesn’t count')}
{note('Shortcut: count every triangle in the picture (12), then take off any that miss the door (only ABC).', 'tip')}""",
    ],
    answer_text='11 triangles: 7 with the door at a corner and 4 with the door on a side.',
    why={'A': '5 counts only the small triangles the paths cut the grounds into.',
         'B': '7 counts only triangles with the door at a corner. He can also walk round a triangle with the door half way along a side.',
         'C': '10 misses one triangle. List them in groups (door at a corner, door on a side) so none slips through.',
         'E': '12 also counts the big outer triangle ABC, which never passes the front door.'},
    fast='There are 12 triangles in the picture. Only the big outer one misses the door: 12 − 1 = 11.',
))


# ---------------------------------------------------------------- 23 (Q48)
def _probe():
    X = lambda d: 60 + d * 70
    parts = [rect(X(0), 50, X(2.5) - X(0), 40, k='ink', fill='o', sw=1.8),
             rect(X(2.5), 50, X(6.7) - X(2.5), 40, k='ink', fill='b', sw=1.8),
             brace(X(0), X(5), 98, '$5 minimum covers this', k='pen', size=16),
             brace(X(5), X(6.7), 98, 'extra $1.70', k='red', size=16),
             rect(360, 150, 250, 60, k='muted', fill='paper', sw=1.6, rx=6)]
    lab = [text((X(0) + X(2.5)) / 2, 76, '5 × 50c = $2.50', k='ink', size=15),
           text((X(2.5) + X(6.7)) / 2, 76, '42 × 10c = $4.20', k='ink', size=15),
           text(X(3.35), 36, 'usage = $6.70', k='pen', size=18, font='scrawl'),
           text(485, 176, 'phone calls $4.95', k='muted', size=16), text(485, 198, '(paid to the phone company)', k='muted', size=14),
           text(485, 232, '✗ not on Probe’s bill', k='red', size=17),
           text(60, 196, 'Probe bills:', k='ink', size=18, anchor='start'), text(60, 222, '$5 + $1.70 = $6.70', k='green', size=22, font='scrawl', anchor='start')]
    return svg(640, 248, rough(*parts) + ''.join(lab),
               'Usage bar: 2.50 for detailed information plus 4.20 for other enquiries makes 6.70; the 5 dollar minimum covers the first 5, so the bill is 6.70; phone calls are crossed out')


Q.append(dict(
    n=23, orig=48, answer='B', topic='Bills & charges',
    question=f"""<p>Megan pays a subscription to Probe Information Services. This is an internet service
which allows her to access up-to-date information relevant to her job. The leaflet which
came with her application form is reproduced below.</p>
<p style="text-align:center;margin:0"><i>Probe Information Services - Serving you in the Internet Age</i></p>
<p style="margin:.3em 0"><i>Minimum monthly charge $5 - this gives access to all services and {hl('a $5 credit which will be set against the actual use made', 'y', 1)}</i></p>
{table([['Financial Markets (updated every 20 minutes)', '10c', '30 seconds'], ['Exchange Rates (updated hourly)', '10c', '30 seconds'],
        ['Company News (updated twice a day)', '10c', '1 minute 30 seconds'], [hl('Detailed Information', 'g'), hl('50c', 'g'), '2 minutes 30 seconds'],
        ['Commodities in World Markets', '10c', '30 seconds']],
       head=['<i>Information category</i>', '<i>Cost per enquiry</i>', '<i>Average access and download time</i>'])}
<p style="margin:.3em 0"><i>{hl("Probe's charges do not include the cost of phone calls", 'p', 2)}. All calls are at local rates</i></p>
<p>Megan's call charges are at local rates of 10c for up to 2 minutes and 5c per additional
minute or part of a minute. In the first month, Megan seeks {hl('detailed information on 5 companies', 'g', 3)} and {hl('uses the other services a total of 42 times', 'g', 4)}.</p>
<p class="stem">{hl('How much will Probe bill her?', 'b', 5)}</p>""",
    options={'A': '$ 5.00', 'B': '$ 6.70', 'C': '$ 7.50', 'D': '$ 9.95', 'E': '$ 11.65'},
    notes=[(1, 'y', 'The $5 isn’t on top of her usage: it pays for the first $5 of it.'),
           (2, 'p', 'Phone calls are not on Probe’s bill. All the call-charge detail is a red herring!'),
           (3, 'g', 'Detailed information: 50c each.'),
           (4, 'g', 'Every other service: 10c each.'),
           (5, 'b', 'Probe’s bill only.')],
    steps=[
        f"""<p>Add up her usage:</p>
{calc('detailed information: 5 × 50c = $2.50', 'other services: 42 × 10c = $4.20', 'usage = <b>$6.70</b>')}""",
        f"""<p>The $5 minimum comes with $5 of credit. Her usage is more than $5, so she pays the $5 plus the extra:</p>{_probe()}
{calc(f'$5 + ($6.70 − $5) = {boxed("$6.70")}')}
{note('If her usage had been under $5, she would still pay $5. Above $5, the bill is simply her usage.', 'check')}""",
    ],
    answer_text='$6.70: her usage is $6.70, which is more than the $5 minimum.',
    why={'A': '$5.00 would only be right if her usage were $5 or less. It is $6.70.',
         'C': '$7.50 = $5 + $2.50: it treats the $5 as a fee on top of the detailed enquiries and forgets the 42 other enquiries.',
         'D': '$9.95 = $5 + $4.95 of phone calls (5 × 15c + 42 × 10c). Probe doesn’t charge for calls.',
         'E': '$11.65 = $6.70 + $4.95 of phone calls. The leaflet says Probe’s charges don’t include calls.'},
    fast='5 × 0.50 + 42 × 0.10 = 2.50 + 4.20 = 6.70. That is over the $5 minimum, so the bill is $6.70. Ignore the phone calls.',
))


# ---------------------------------------------------------------- 24 (Q49)
def _pairs():
    names = ['B', 'Dp', 'F', 'J', 'P', 'R']
    bad = {('B', 'Dp'): 'Dp', ('B', 'J'): 'J', ('Dp', 'J'): 'J', ('Dp', 'P'): 'Dp', ('J', 'P'): 'J', ('J', 'R'): 'J'}
    c, ox, oy = 58, 110, 64
    parts, lab = [], []
    rows, cols = names[:-1], names[1:]
    for j, n in enumerate(cols):
        lab.append(text(ox + j * c + c / 2, oy - 12, n, k='ink', size=19, font='print'))
    for i, n in enumerate(rows):
        lab.append(text(ox - 12, oy + i * c + c / 2 + 7, n, k='ink', size=19, font='print', anchor='end'))
    for i, a in enumerate(rows):
        for j, b in enumerate(cols):
            if j < i:
                continue
            x, y = ox + j * c, oy + i * c
            why = bad.get((a, b))
            parts.append(rect(x + 2, y + 2, c - 4, c - 4, k='ink', fill='p' if why else 'g', sw=1.6, rx=4))
            lab.append(text(x + c / 2, y + c / 2 + (4 if why else 8), '✗' if why else '✓', k='red' if why else 'green', size=24))
            if why:
                lab.append(text(x + c / 2, y + c - 6, ('J' if why == 'J' else 'Dp') + ' rule', k='red', size=14))
    lab += [text(ox, 28, 'Drainage + …', k='pen', size=20, font='scrawl', anchor='start'),
            text(430, 120, 'B Bricklaying, Dp Damp-proofing', k='muted', size=15, anchor='start'),
            text(430, 140, 'F Flooring, J Joinery,', k='muted', size=15, anchor='start'),
            text(430, 160, 'P Plastering, R Roofing', k='muted', size=15, anchor='start'),
            text(430, 210, '✗ J rule: Joinery, no Flooring (4)', k='red', size=15, anchor='start'),
            text(430, 234, '✗ Dp rule: Dp + Drainage with', k='red', size=15, anchor='start'),
            text(430, 254, '   Bricklaying or Plastering (2)', k='red', size=15, anchor='start'),
            text(430, 300, '15 − 4 − 2 = 9 ✓', k='green', size=24, font='scrawl', anchor='start')]
    return svg(660, 362, rough(*parts) + ''.join(lab),
               'Grid of the 15 pairs that can go with Drainage: 6 crossed out (4 have Joinery without Flooring, 2 have Damp-proofing with Bricklaying or Plastering), 9 allowed')


Q.append(dict(
    n=24, orig=49, answer='C', topic='Counting combinations',
    question=f"""<p>A group of Construction students must choose their specialist options from the following
list:</p>
<p>Bricklaying, Damp-proofing, Drainage, Flooring, Joinery, Plastering, Roofing</p>
<p>Each student must {hl('choose three options', 'g', 1)}. The available options may be combined with
each other in any way, with the exception of the restrictions that {hl('Damp-proofing and Drainage together may not be combined with Bricklaying or Plastering', 'p', 2)} because of
timetable constraints, and that {hl('students choosing Joinery must also choose Flooring', 'y', 3)}.</p>
<p class="stem">How many possible combinations {hl('including Drainage', 'b', 4)} could the students choose from?</p>""",
    options={'A': '7', 'B': '8', 'C': '9', 'D': '10', 'E': '11'},
    notes=[(1, 'g', 'Drainage plus 2 others from the remaining 6.'),
           (2, 'p', 'Read it carefully: only the <b>pair</b> Damp-proofing + Drainage is banned with Bricklaying or Plastering. Drainage on its own is fine with them.'),
           (3, 'y', 'Joinery needs Flooring. (Flooring without Joinery is fine.)'),
           (4, 'b', 'Count the trios that contain Drainage.')],
    steps=[
        f"""<p>Drainage is in, so choose 2 more from the other 6 options. Number of pairs:</p>
{calc(f'6 × 5 ÷ 2 = <b>15</b> pairs')}""",
        f"""<p>Now cross out the pairs that break a rule:</p>{_pairs()}""",
        f"""{calc(f'Joinery without Flooring: J + B, J + Dp, J + P, J + R {ar()} 4 out',
                  f'Damp-proofing (with Drainage) and Bricklaying or Plastering: Dp + B, Dp + P {ar()} 2 out',
                  f'15 − 4 − 2 = {boxed("9")}')}
{note('The 9: B+F, B+P, B+R, Dp+F, Dp+R, F+J, F+P, F+R, P+R (each with Drainage).', 'check')}""",
    ],
    answer_text='9 combinations.',
    why={'A': '7 also throws out pairs like Bricklaying + Plastering, which are allowed: the ban only applies when Damp-proofing is there too.',
         'B': '8 misses one allowed trio, often Drainage + Flooring + Joinery (Joinery is fine when Flooring is there).',
         'D': '10 bans only one of Damp-proofing + Bricklaying and Damp-proofing + Plastering.',
         'E': '11 ignores the Damp-proofing rule completely and only uses the Joinery rule.'},
    fast='15 pairs go with Drainage. Take off 4 with Joinery but no Flooring and 2 with Damp-proofing plus Bricklaying or Plastering: 9.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _savings():
    base, u = 236, 16
    parts, lab = [line(60, base, 560, base, k='ink', w=2), line(70, base + 6, 70, 50, k='ink', head=True)], []
    for v in (0, 2, 4, 6, 8, 10):
        lab.append(text(62, base - v * u + 5, f'£{v}', k='muted', size=14, anchor='end'))
    for n in range(1, 6):
        x = 100 + (n - 1) * 92
        parts.append(f'<rect x="{x}" y="{base - 2 * n * u}" width="48" height="{2 * n * u}" class="k-muted f-none" stroke-width="2" stroke-dasharray="6 5"/>')
        if n > 1:
            parts.append(rect(x, base - (2 * n - 2) * u, 48, (2 * n - 2) * u, k='ink', fill='g', sw=1.8))
        lab.append(text(x + 24, base + 20, n, k='ink', size=16))
        lab.append(text(x + 24, base - (2 * n - 2) * u - 8 if n > 1 else base - 8, f'£{2 * n - 2}', k='green', size=15))
        parts.append(line(x + 56, base - 2 * n * u, x + 56, base - (2 * n - 2) * u, k='red', w=2, head=True))
    lab += [text(560, base + 20, 'books', k='muted', size=14, anchor='end'),
            text(330, 24, 'dashed: £2 × books, no postage (that’s graph E)', k='muted', size=16),
            text(330, 46, 'solid: £2 postage off every bar (graph C)', k='green', size=16),
            text(124, 190, '− £2 postage', k='red', size=15)]
    return svg(600, 270, rough(*parts) + ''.join(lab),
               'Bar chart: dashed bars at 2, 4, 6, 8, 10 pounds for 1 to 5 books, and solid bars 2 pounds lower at 0, 2, 4, 6, 8')


Q.append(dict(
    n=25, orig=50, answer='C', topic='Graphs',
    question=f"""<p>I am a member of a book club. Every month I must choose {hl('at least one book', 'y', 1)}. All books
are sold at a {hl('discount of £2.00', 'g', 2)} on shop prices. I pay {hl('a fixed charge for postage regardless of which books I order', 'p', 3)}.</p>
<p class="stem">Which one of the following graphs could show the relationship between the number of
books ordered in a month and the {hl('total saving on shop prices (allowing for postage charge)', 'b', 4)}?</p>
{fig(Y, 'ps_q25_graphs', 'Five bar charts A to E of savings in pounds against number of books ordered, 1 to 5', 440)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'y', 'Bars for 1, 2, 3, … books.'),
           (2, 'g', 'Each extra book saves exactly £2 more: the bars rise in equal steps of <b>£2</b>.'),
           (3, 'p', 'Postage is paid once, the same every month, so the same amount comes off <b>every</b> bar.'),
           (4, 'b', 'Saving = £2 × books − postage.')],
    steps=[
        f"""<p>Write the saving as a rule:</p>
{calc(f'saving = £2 × (number of books) − postage', f'one more book {ar()} exactly £2 more saving',
      f'postage {ar()} every bar sits the same amount below 2, 4, 6, 8, 10')}""",
        f"""<p>Read the bars on each graph:</p>
{calc(f'A: 1.5, 3, 4.5, 6, 7.5 {ar()} steps of £1.50 {cross()}',
      f'B: 0, 3, 6, 9, 12 {ar()} steps of £3 {cross()}',
      f'C: 0, 2, 4, 6, 8 {ar()} steps of £2, and £2 below 2, 4, 6… {tick()}',
      f'D: up, down, then up again {cross()}',
      f'E: 2, 4, 6, 8, 10 {ar()} steps of £2, but nothing taken off for postage {cross()}')}""",
        f"""{_savings()}
{calc(f'C fits with postage = £2 {ar()} {boxed("C")}')}""",
    ],
    answer_text='Graph C: savings of 0, 2, 4, 6, 8, which is £2 a book with £2 postage taken off.',
    why={'A': 'A rises by £1.50 a book, but every book saves £2.',
         'B': 'B rises by £3 a book.',
         'D': 'D goes down and then up again. Each extra book always adds £2 to the saving.',
         'E': 'E is exactly £2 per book with nothing taken off. The fixed postage charge has to come off every bar.'},
    fast='Steps must be exactly £2, and the bars must sit below 2, 4, 6… because of postage. Only C (0, 2, 4, 6, 8).',
))
