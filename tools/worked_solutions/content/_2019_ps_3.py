import math
from wslib import *

Y = 2019
Q = []

# ---------------------------------------------------------------- 17 (Q36)
def _cloth():
    s, x0 = 2.1, 20
    parts, lab = [], []
    rows = [(100, 30, [(0, 0), (38, 0), (0, 15), (38, 15)], '100 cm wide, 30 cm long', '0.3 × £2.00 = 60p', 'ink'),
            (120, 30, [(0, 0), (38, 0), (76, 0), (0, 15)], '120 cm wide, 30 cm long', '0.3 × £2.20 = 66p', 'ink'),
            (160, 20, [(0, 0), (38, 0), (76, 0), (114, 0)], '160 cm wide, 20 cm long', '0.2 × £2.80 = 56p ✓', 'green')]
    y = 34
    for wdt, ln, pieces, t1, t2, k in rows:
        parts.append(rect(x0, y, wdt * s, ln * s, k='ink', fill='paper', sw=2))
        for px, py in pieces:
            parts.append(rect(x0 + px * s + 1, y + py * s + 1, 38 * s - 2, 15 * s - 2, k='pen', fill='b', sw=1.4))
        lab += [text(x0 + 360, y + ln * s / 2 - 2, t1, k='ink', size=16, anchor='start'),
                text(x0 + 360, y + ln * s / 2 + 20, t2, k=k, size=18 if k == 'green' else 16, font='scrawl' if k == 'green' else 'hand', anchor='start')]
        y += ln * s + 34
    lab += [text(x0, 22, 'width across →  (each blue piece is 38 cm across, 15 cm along)', k='muted', size=14, anchor='start'),
            text(x0 + 5, 34 + 2 * (30 * s + 34) + 20 * s + 22, '15 cm used, but must buy 20 cm', k='red', size=15, anchor='start')]
    return svg(680, 300, rough(*parts) + ''.join(lab),
               'Four 38 by 15 pieces laid on each width: 100 cm needs 30 cm (60p), 120 cm needs 30 cm (66p), 160 cm fits all four in one row and needs 20 cm (56p)')

Q.append(dict(
    n=17, orig=36, answer='B', topic='Area & best buy',
    question=f"""<p>Nathan is making a pair of trousers for his young son. The diagram shows the pattern for one
piece. {hl('Four such pieces are needed', 'g', 1)}.</p>
{fig(Y, 'ps_q17_pattern', 'Pattern piece about 15 cm wide and 38 cm long', 190)}
<p>[diagram not to scale]</p>
<p>For simplicity he assumes that he will need a {hl('15 cm × 38 cm rectangle for each piece', 'g', 2)}. The
material comes in three widths with prices as shown:</p>
{table([['100 cm', '£2.00'], ['120 cm', '£2.20'], ['160 cm', '£2.80']], head=['<i>width</i>', f'<i>{hl("price / metre", "y", 3)}</i>'])}
<p>{hl('Material may be bought in lengths which are exact multiples of 10 cm', 'p', 4)}.</p>
<p class="stem">What is the {hl('lowest price', 'b', 5)} he can pay?</p>""",
    options={'A': '42p', 'B': '56p', 'C': '60p', 'D': '66p', 'E': '80p'},
    notes=[(1, 'g', '4 rectangles to cut out.'),
           (2, 'g', 'Each piece is 15 by 38. Turn them whichever way fits best.'),
           (3, 'y', 'You pay for the <b>length</b> you buy; the width comes free with the roll.'),
           (4, 'p', 'Round the length up: 15 cm needed means buying 20 cm.'),
           (5, 'b', 'Try every width and find the cheapest.')],
    steps=[
        f"""<p>Lay the 38 cm side <b>across</b> the roll so the length you buy stays short:</p>
{calc('100 cm: 2 × 38 = 76 fits, 3 × 38 = 114 doesn’t → 2 per row → 2 rows',
      '120 cm: 3 × 38 = 114 fits → 3 in row 1, 1 in row 2 → 2 rows',
      '160 cm: 4 × 38 = 152 fits → all 4 in one row!')}""",
        f"""{_cloth()}
{calc('100 cm: 2 rows × 15 = 30 cm → 0.3 × £2.00 = 60p',
      '120 cm: 30 cm → 0.3 × £2.20 = 66p',
      f'160 cm: 15 cm → buy 20 cm → 0.2 × £2.80 = {boxed("56p")}')}
{note('Turning the pieces the other way (15 cm across) is worse: you need 38 cm of length, so 40 cm must be bought (80p, 88p or £1.12).', 'check')}""",
    ],
    answer_text='56p: 20 cm of the 160 cm wide material, with all four pieces side by side.',
    why={'A': '42p = 0.15 × £2.80: it forgets that you must buy a multiple of 10 cm (15 cm → 20 cm).',
         'C': '60p is the best you can do with the 100 cm material (30 cm long).',
         'D': '66p is the best with the 120 cm material (30 cm long).',
         'E': '80p uses the 100 cm material with the pieces the other way round (6 across, 40 cm long).'},
    fast='160 cm roll: 4 × 38 = 152 fits in one row 15 cm long. Buy 20 cm: 0.2 × 2.80 = 56p.',
))

# ---------------------------------------------------------------- 18 (Q37)
def _bath_line():
    X = lambda v: 40 + (v - 120) * 17
    parts = [line(X(120), 70, X(151), 70, k='ink', head=True)]
    lab = []
    for v in range(120, 151, 5):
        parts.append(line(X(v), 64, X(v), 76, k='ink', w=1.5))
        lab.append(text(X(v), 94, f'£{v}', k='muted', size=14))
    for v, k in ((126, 'pen'), (128, 'pen'), (130, 'orange'), (149, 'orange')):
        parts.append(circle(X(v), 70, 6, k=k, fill='paper', sw=2.4))
    lab += [text(X(126) + 4, 50, 'Europa (steel)', k='pen', size=15, anchor='end'),
            text(X(130) - 4, 50, 'Carola (acrylic)', k='orange', size=15, anchor='start'),
            text(X(128), 118, 'Sierra (steel)', k='pen', size=15),
            text(X(149) + 6, 50, 'Victory (acrylic)', k='orange', size=15, anchor='end')]
    parts.append(line(X(126), 26, X(130), 26, k='green', w=2.2, head=True, tail=True))
    lab.append(text(X(128), 16, 'save £4', k='green', size=18, font='scrawl'))
    return svg(600, 128, rough(*parts) + ''.join(lab),
               'Number line of the baths that pass: Europa 126 and Sierra 128 (steel), Carola 130 and Victory 149 (acrylic); the saving is 4 pounds')


BATHS = [('Balmoral', 'acrylic', '1600', '750', '590', 'yes', 'no', '159'),
         ('Carola', 'acrylic', '1600', '700', '610', 'yes', 'no', '130'),
         ('Dalton', 'steel', '1600', '700', '580', 'no', 'no', '112'),
         ('Europa', 'steel', '1600', '700', '590', 'yes', 'no', '126'),
         ('Gamma', 'steel', '1600', '700', '580', 'yes', 'yes', '135'),
         ('Oporto', 'acrylic', '1600', '700', '585', 'no', 'no', '115'),
         ('Polar', 'steel', '1500', '700', '600', 'yes', 'no', '120'),
         ('Rocca', 'acrylic', '1600', '700', '590', 'no', 'no', '126'),
         ('Sierra', 'steel', '1600', '700', '580', 'yes', 'no', '128'),
         ('Victory', 'acrylic', '1600', '700', '580', 'yes', 'no', '149')]


def _bath_check():
    rows = []
    for name, mat, ln, wd, ht, grip, drill, price in BATHS:
        why = []
        if ln != '1600' or wd != '700':
            why.append(f'size {ln} × {wd}')
        if grip == 'no':
            why.append('no grips')
        if drill == 'yes':
            why.append('pre-drilled')
        ok = not why
        rows.append([name, mat, f'£{price}', (tick() + ' fits') if ok else (cross() + ' ' + ', '.join(why))])
    return table(rows, head=['bath', 'material', 'price', 'check'])

Q.append(dict(
    n=18, orig=37, answer='C', topic='Tables & filtering',
    question=f"""<p>Arthur plans to modernise his bathroom. His design requires a {hl('1600 mm × 700 mm', 'g', 1)} bath. He
wants {hl('side grips', 'y', 2)} to help him get out of the bath, and because he doesn’t want to choose the
taps before ordering the bath he must have one which {hl('doesn’t have pre-drilled tap holes', 'y', 3)}.</p>
<p>A list from the bath catalogue is shown below:</p>
{table([list(r) for r in BATHS],
       head=['<i>name</i>', '<i>material</i>', '<i>length</i>', '<i>width</i>', f'<i>{hl("height", "p", 4)}</i>', '<i>side-grips</i>',
             '<i>pre-drilled tap holes</i>', '<i>price</i> (£)'])}
<p class="stem">How much will Arthur save by choosing the {hl('cheapest steel bath', 'b', 5)} that fits his requirements rather
than the {hl('cheapest acrylic bath', 'b')} that fits his requirements?</p>""",
    options={'A': '£2', 'B': '£3', 'C': '£4', 'D': '£10', 'E': '£18'},
    notes=[(1, 'g', 'Length 1600 <b>and</b> width 700. Check both columns.'),
           (2, 'y', 'Side-grips must be “yes”.'),
           (3, 'y', 'Pre-drilled tap holes must be “no”.'),
           (4, 'p', 'Height isn’t part of his design: ignore it.'),
           (5, 'b', 'Two winners: the cheapest steel bath that passes and the cheapest acrylic one that passes. Then subtract.')],
    steps=[
        f"""<p>Run every bath through the three checks (size, grips, no holes):</p>{_bath_check()}""",
        f"""<p>Four baths pass. Put them on a price line:</p>{_bath_line()}
{calc('cheapest steel: Europa £126', 'cheapest acrylic: Carola £130', f'saving = 130 − 126 = {boxed("£4")}')}""",
    ],
    answer_text='£4: Europa (steel, £126) against Carola (acrylic, £130).',
    why={'A': '£2 uses Sierra (£128), which passes but isn’t the cheapest steel bath.',
         'B': '£3 compares Oporto (£115) with Dalton (£112), the cheapest of each if you forget the side grips.',
         'D': '£10 uses Polar (£120), but Polar is only 1500 mm long.',
         'E': '£18 uses Dalton (£112), which has no side grips.'},
    fast='Cross out wrong size (Balmoral, Polar), no grips (Dalton, Oporto, Rocca), pre-drilled (Gamma). Cheapest left: steel 126, acrylic 130. £4.',
))

# ---------------------------------------------------------------- 19 (Q38)
def _pie_clock():
    cx, cy, r = 170, 160, 118
    slices = [('steam', 77, 'v'), ('adventure', 86, 'b'), ('farm', 49, 'g'), ('museum', 33, 'y'), ('theme park', 115, 'paper')]
    parts, lab = [], []
    a0 = -90.0
    for name, deg, f in slices:
        a1 = a0 + deg
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        big = 1 if deg > 180 else 0
        parts.append(path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z', k='ink', fill=f, sw=1.8))
        am = math.radians((a0 + a1) / 2)
        lr = r * 0.62
        lab.append(text(cx + lr * math.cos(am), cy + lr * math.sin(am) + 5, name, k='ink', size=15))
        a0 = a1
    for h in range(12):
        a = math.radians(h * 30 - 90)
        parts.append(line(cx + (r + 4) * math.cos(a), cy + (r + 4) * math.sin(a), cx + (r + 14) * math.cos(a), cy + (r + 14) * math.sin(a), k='red', w=2))
    for h, lbl in ((0, '12'), (3, '3'), (6, '6'), (9, '9')):
        a = math.radians(h * 30 - 90)
        lab.append(text(cx + (r + 28) * math.cos(a), cy + (r + 28) * math.sin(a) + 6, lbl, k='red', size=16))
    tx = 350
    lab += [text(tx, 50, 'read it like a clock face:', k='red', size=17, anchor='start'),
            text(tx, 84, 'steam: 12 to about half past 2', k='ink', size=16, anchor='start'),
            text(tx, 106, '→ just under ¼', k='pen', size=17, font='scrawl', anchor='start'),
            text(tx, 140, 'steam + adventure: to before 6', k='ink', size=16, anchor='start'),
            text(tx, 162, '→ just under ½', k='pen', size=17, font='scrawl', anchor='start'),
            text(tx, 196, 'theme park: about 8 round to 12', k='ink', size=16, anchor='start'),
            text(tx, 218, '→ just under ⅓', k='pen', size=17, font='scrawl', anchor='start'),
            text(tx, 252, 'farm clearly bigger than museum,', k='ink', size=16, anchor='start'),
            text(tx, 274, '→ but not double it', k='pen', size=17, font='scrawl', anchor='start')]
    return svg(660, 320, rough(*parts) + ''.join(lab),
               'Pie redrawn with clock ticks: steam just under a quarter, steam plus adventure just under half, theme park just under a third, farm about one and a half times museum')

Q.append(dict(
    n=19, orig=38, answer='E', topic='Pie charts & proportion',
    question=f"""<p>The Head of Year 6 is planning an end-of-term treat for her students. The pie chart represents the
numbers of votes cast by the children for each of the five possible outings.</p>
{fig(Y, 'ps_q19_pie', 'Pie chart: steam train excursion, adventure playground, farm, museum and theme park slices', 420)}
<p class="stem">Which one of the following rows (<b>A–E</b>) {hl('could show the actual number of votes', 'b', 1)} cast by the children
for each of the options?</p>
{table([['<b>A</b>', '35', '45', '30', '15', '55', '180'], ['<b>B</b>', '24', '28', '20', '16', '32', '120'],
        ['<b>C</b>', '45', '55', '20', '15', '65', '200'], ['<b>D</b>', '22', '28', '15', '15', '40', '120'],
        ['<b>E</b>', '32', '36', '20', '14', '48', '150']],
       head=['', '<i>steam train excursion</i>', '<i>adventure playground</i>', '<i>farm</i>', '<i>museum</i>', '<i>theme park</i>', f'<i>{hl("total", "p", 2)}</i>'])}""",
    options={'A': 'row A', 'B': 'row B', 'C': 'row C', 'D': 'row D', 'E': 'row E'},
    notes=[(1, 'b', 'Each row must have the same <b>shares</b> as the pie. No angles are given, so compare fractions by eye.'),
           (2, 'p', 'Every total is correct (check: they all add up), so the totals can’t separate the rows. Look at the shares.')],
    steps=[
        f"""<p>Pull out the key facts from the pie:</p>{_pie_clock()}""",
        f"""<p>Test each row against those facts:</p>
{table([['A', '35/180 ≈ 19%', '80/180 ≈ 44%', '55/180 ≈ 31%', f'30 : 15 = <b>2</b> {cross()}'],
        ['B', '24/120 = 20%', '52/120 ≈ 43%', f'32/120 ≈ <b>27%</b> {cross()}', '20 : 16'],
        ['C', '45/200 ≈ 23%', f'100/200 = <b>50%</b> {cross()}', '65/200 ≈ 33%', '20 : 15'],
        ['D', '22/120 ≈ 18%', '50/120 ≈ 42%', '40/120 ≈ 33%', f'15 : 15 = <b>1</b> {cross()}'],
        ['E', f'32/150 ≈ 21% {tick()}', f'68/150 ≈ 45% {tick()}', f'48/150 = 32% {tick()}', f'20 : 14 ≈ 1.4 {tick()}']],
       head=['row', 'steam (under ¼)', 'steam + adventure (under ½)', 'theme park (under ⅓)', 'farm : museum (about 1½)'])}""",
        f"""<p>Only row E fits everything. Final check in degrees (× 360 ÷ 150 = × 2.4):</p>
{calc('32 × 2.4 ≈ 77°, 36 × 2.4 ≈ 86°, 20 × 2.4 = 48°, 14 × 2.4 ≈ 34°, 48 × 2.4 ≈ 115°',
      f'these match the slices {ar()} {boxed("E")}')}""",
    ],
    answer_text='Row E: 32, 36, 20, 14, 48 out of 150 gives slices of about 77°, 86°, 48°, 34° and 115°, just like the pie.',
    why={'A': 'Farm (30) is double the museum (15), but the farm slice is only about 1½ times the museum slice.',
         'B': 'Theme park would be only 32 out of 120 (just over a quarter), but its slice is nearly a third.',
         'C': 'Steam + adventure = 100 out of 200, exactly half, so that boundary would be at 6 o’clock. In the pie it is clearly before 6.',
         'D': 'Farm and museum both 15, but the farm slice is clearly bigger than the museum slice.'},
    fast='Farm > museum (D out), but not double (A out); steam + adventure under half (C out); theme park nearly a third (B out). E.',
))

# ---------------------------------------------------------------- 20 (Q42)
def _walls():
    s, x0, base = 84, 50, 250
    parts, lab = [], []
    walls = [('front', 2.5, 2.5, 'y', '1 × 2.5', '= 2.5'), ('side', 2.5, 2, 'g', '(2.5 + 2) ÷ 2', '= 2.25'),
             ('back', 2, 2, 'b', '1 × 2', '= 2'), ('side', 2, 2.5, 'g', '(2 + 2.5) ÷ 2', '= 2.25')]
    for i, (name, hl_, hr, f, a1, a2) in enumerate(walls):
        x = x0 + i * (s + 56)
        pts = [(x, base), (x + s, base), (x + s, base - hr * s), (x, base - hl_ * s)]
        parts.append(poly(pts, k='ink', fill=f, sw=2))
        lab += [text(x + s / 2, base + 22, name, k='ink', size=16),
                text(x + s / 2, base - 72, a1, k='ink', size=14),
                text(x + s / 2, base - 50, a2, k='pen', size=16)]
        lab.append(text(x - 6, base - hl_ * s / 2, f'{hl_}', k='muted', size=13, anchor='end'))
    parts.append(rect(x0 + 12, base - 2.2 * s, s - 24, 2.0 * s, k='muted', sw=1.4))
    lab += [text(x0 + s / 2, base - 2.2 * s - 6, 'door', k='muted', size=13),
            text(x0 + 0.5 * s, base + 44, 'each wall is 1 m wide', k='muted', size=14, anchor='start'),
            text(x0 + 3 * (s + 56) + s / 2, base + 44, 'total = 9 m²', k='red', size=20, font='scrawl')]
    return svg(620, 304, rough(*parts) + ''.join(lab),
               'The four walls unfolded: front 2.5 square metres, sides 2.25 each, back 2; total 9 square metres')

Q.append(dict(
    n=20, orig=42, answer='E', topic='Area & time',
    question=f"""<p>The drawing below shows an allotment shed.</p>
{fig(Y, 'ps_q20_shed', 'Lean-to shed: front 2.5 m high with a door, back 2 m high, 1 m wide and 1 m deep, sloping metal roof', 270)}
<p>[diagram not to scale]</p>
<p>The {hl('four outside wood surfaces', 'y', 1)} of the shed, including the door, need to be painted with {hl('three coats', 'g', 2)} of paint. {hl('It takes 4 minutes to paint 1 square metre', 'g', 3)}.</p>
<p>I have {hl('two identical sheds', 'g', 4)} to paint and will take just {hl('one 20-minute tea break', 'p', 5)}.</p>
<p class="stem">{hl('How long will it take to paint the two sheds?', 'b', 6)}</p>""",
    options={'A': '36 minutes', 'B': '1 hour and 48 minutes', 'C': '2 hours and 8 minutes', 'D': '3 hours and 36 minutes',
             'E': '3 hours and 56 minutes'},
    notes=[(1, 'y', 'Four walls: front, back and two sides. The roof is metal, so not painted.'),
           (2, 'g', 'Every square metre gets painted 3 times.'),
           (3, 'g', '4 minutes per square metre per coat.'),
           (4, 'g', 'Double everything.'),
           (5, 'p', 'The break is part of the total time: add 20 minutes at the end.'),
           (6, 'b', 'Total time from start to finish.')],
    steps=[
        f"""<p>The roof slopes, so the front is 2.5 m tall, the back 2 m, and the sides are trapeziums. Unfold the walls:</p>{_walls()}
{calc('front 2.5 + back 2 + sides 2.25 + 2.25 = <b>9 m²</b>')}
{note('Side wall: a 1 × 2 rectangle plus a triangle ½ × 1 × 0.5 = 0.25, so 2.25. Same as the trapezium rule.', 'tip')}""",
        f"""{calc('3 coats: 9 × 3 = 27 m² per shed', '2 sheds: 27 × 2 = 54 m²', 'time: 54 × 4 = 216 minutes = 3 h 36 min',
                  f'+ 20 min tea break = {boxed("3 h 56 min")}')}""",
    ],
    answer_text='3 hours 56 minutes: 54 m² × 4 min = 216 min, plus the 20-minute break.',
    why={'A': '36 minutes is one coat on one shed (9 × 4), with no break.',
         'B': '1 h 48 min is three coats on <b>one</b> shed (27 × 4 = 108 min).',
         'C': '2 h 8 min is one shed plus the tea break (108 + 20).',
         'D': '3 h 36 min is right for the painting but forgets the 20-minute tea break.'},
    fast='Walls 2.5 + 2 + 2.25 + 2.25 = 9 m². × 3 coats × 2 sheds × 4 min = 216 min. + 20 = 236 min = 3 h 56.',
))

# ---------------------------------------------------------------- 21 (Q43)
def _groups():
    parts, lab = [], []
    groups = [(5, 3), (5, 3), (6, 2)]
    for g, (a, c) in enumerate(groups):
        y = 70 + g * 78
        x = 60
        parts.append(rect(40, y - 52, 8 * 34 + 20, 62, k='muted', fill='paper', sw=1.4, rx=12))
        for i in range(a):
            lab.append(stick_person(x, y, k='pen'))
            x += 34
        for i in range(c):
            lab.append(stick_person(x, y, k='orange', s=0.75))
            x += 34
        lab.append(text(350, y - 18, f'group {g + 1}: {a} adults + {c} children', k='ink', size=16, anchor='start'))
        lab.append(text(350, y + 4, '$175 ✓ (2+ children)', k='green', size=16, anchor='start'))
    lab += [text(60, 284, 'blue = adult (16 or over), orange = child (15)', k='muted', size=14, anchor='start'),
            text(560, 284, '3 × $175 = $525', k='red', size=20, font='scrawl')]
    return svg(660, 296, rough(*parts) + ''.join(lab),
               'Three groups of eight: 5 adults and 3 children, 5 adults and 3 children, 6 adults and 2 children; each is a 175 dollar group ticket')

Q.append(dict(
    n=21, orig=43, answer='A', topic='Tickets & best deal',
    question=f"""<p>A school party consisting of {hl('4 teachers and 20 students', 'g', 1)} is visiting the theatre. Of the students,
8 are aged 15 years and {hl('12 are aged 16 years', 'p', 2)}. The following table shows the entry prices to
the theatre.</p>
{table([[hl('Adult (16 years and over)', 'y', 3), '$30'], ['Child (5–15 years)', '$20'], ['Under 5 years', 'free'],
        ['Family ticket (2 adults and up to 2 children under 16 years)', '$90'],
        [hl('Group ticket (8 people including at least 2 children under 16 years)', 'y', 4), '$175'],
        ['Supergroup ticket (any 8 people)', '$200']], head=['<i>category</i>', '<i>price</i>'])}
<p class="stem">What is the {hl('least amount', 'b', 5)} that the school party must pay for entry to the theatre?</p>""",
    options={'A': '$525', 'B': '$530', 'C': '$545', 'D': '$550', 'E': '$560'},
    notes=[(1, 'g', '24 people in total.'),
           (2, 'p', '16-year-olds pay as <b>adults</b>!'),
           (3, 'y', 'So adults = 4 teachers + 12 students = 16. Children = 8.'),
           (4, 'y', 'The best deal per person, but each group needs at least 2 children.'),
           (5, 'b', 'Cheapest way to get all 24 in.')],
    steps=[
        f"""<p>Sort the party: <b>16 adults</b> (4 teachers + 12 aged 16) and <b>8 children</b> (aged 15).</p>
<p>Cost per person on each ticket:</p>
{calc('adult $30, child $20', 'family: 90 ÷ 4 = $22.50 each', 'group: 175 ÷ 8 ≈ $21.88 each ← cheapest for adults', 'supergroup: 200 ÷ 8 = $25 each')}""",
        f"""<p>24 people = exactly 3 groups of 8. Each group needs 2 children, and we have 8 to share out:</p>{_groups()}""",
        f"""<p>Could a mix be cheaper? Try the obvious rivals:</p>
{calc('2 groups (12 adults + 4 children) + 2 family tickets = 350 + 180 = $530',
      '2 groups + 4 adult + 4 child tickets = 350 + 120 + 80 = $550',
      '2 supergroups (16 adults) + 8 child tickets = 400 + 160 = $560',
      f'all dearer {ar()} least = {boxed("$525")}')}""",
    ],
    answer_text='$525: three group tickets, each with at least 2 of the 15-year-olds.',
    why={'B': '$530 is 2 group tickets + 2 family tickets. Close, but $5 more.',
         'C': '$545 is e.g. a group + a supergroup + a family ticket + 4 child tickets (175 + 200 + 90 + 80).',
         'D': '$550 is 2 group tickets with the other 4 adults and 4 children paying single prices.',
         'E': '$560 puts the 16 adults in 2 supergroups and buys 8 child tickets.'},
    fast='16 adults + 8 children = 24 = 3 groups of 8, each with 2+ children. 3 × 175 = 525.',
))

# ---------------------------------------------------------------- 22 (Q44)
def _hexmap(cx, cy, edges, phi, letter, title, r=50):
    parts, lab = [], []
    pts = [(cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))) for a in range(0, 360, 60)]
    parts.append(poly(pts, k='ink', fill='paper', sw=2))
    for ang, num in edges.items():
        d = r * 0.87 + 16
        lab.append(text(cx + d * math.cos(math.radians(ang)), cy - d * math.sin(math.radians(ang)) + 6, num, k='pen', size=17, font='print'))
    vx, vy = cx + r * math.cos(math.radians(phi)), cy - r * math.sin(math.radians(phi))
    parts.append(circle(vx, vy, 6, k='red', fill='p', sw=2))
    parts.append(line(cx + 14 * math.cos(math.radians(phi)), cy - 14 * math.sin(math.radians(phi)),
                      cx + (r - 12) * math.cos(math.radians(phi)), cy - (r - 12) * math.sin(math.radians(phi)), k='red', w=2, head=True))
    lab.append(text(cx, cy + 9, letter, k='ink', size=26, font='print', rotate=90 - phi))
    lab.append(text(cx, cy - r - 30, title, k='ink', size=15))
    return parts, lab


def _hexmaps():
    T = {270: '1', 330: '2', 30: '3', 90: '4', 150: '5', 210: '6'}
    B = {90: '1', 30: '2', 330: '3', 270: '4', 210: '5', 150: '6'}
    CB = {90: '6', 30: '1', 330: '2', 270: '3', 210: '4', 150: '5'}
    parts, lab = [], []
    for cx, edges, phi, letter, title in ((90, T, 0, 'T', 'original: T'), (250, B, 180, 'B', 'original: B'),
                                          (440, T, 0, 'T', 'net C: T'), (600, CB, 120, 'B', 'net C: B')):
        p, l = _hexmap(cx, 120, edges, phi, letter, title)
        parts += p
        lab += l
    parts.append(line(345, 30, 345, 210, k='muted', w=1.5, dash=True))
    lab += [text(170, 224, 'T points at the 2|3 corner, B at the 5|6 corner', k='red', size=15),
            text(520, 224, 'same corners ✓', k='green', size=18, font='scrawl')]
    return svg(680, 236, rough(*parts) + ''.join(lab),
               'Hexagon maps: in the original, T has sides 1 to 6 round it and points at the corner of 2 and 3; B points at the corner of 5 and 6. Net C gives the same')

Q.append(dict(
    n=22, orig=44, answer='C', topic='Nets & folding',
    question=f"""<p>Consider the following net, which forms a {hl('hexagonal prism', 'y', 1)}:</p>
{fig(Y, 'ps_q22_net', 'Net: a row of squares 4 5 6 1 2 3, with hexagon T above square 1 and hexagon B below it; T and B are written sideways', 230)}
<p class="stem">Which one of the following nets will form an {hl('identical prism', 'b', 2)}?</p>
{fig(Y, 'ps_q22_opts', 'Five nets A to E with the squares 1 to 6 and hexagons T and B in different places and turned different ways', 520)}""",
    options={'A': 'net A', 'B': 'net B', 'C': 'net C', 'D': 'net D', 'E': 'net E'},
    notes=[(1, 'y', 'Six squares wrap round the sides; the hexagons T and B are the two ends.'),
           (2, 'b', 'Identical = every face in the same place <b>and</b> pointing the same way. Numbers and letters must match too.')],
    steps=[
        f"""<p>First, what does the original prism look like?</p>
<ul><li>The strip 4 5 6 1 2 3 wraps round, so the sides go 1, 2, 3, 4, 5, 6 in order. Opposite pairs: 1–4, 2–5, 3–6.</li>
<li>Every number stands upright with its top towards T.</li>
<li>Each hexagon’s edges meet the squares in strip order, starting from the square it hangs on. Then see where each letter’s top points:</li></ul>
{_hexmaps()}""",
        f"""<p>Now knock out the wrong nets:</p>
<ul><li><b>A</b>: squares 1 and 6 are fixed to <b>opposite</b> edges of T, so they would end up on opposite sides. In the original they are neighbours. {cross()}</li>
<li><b>D</b>: the strip 5 4 3 has B along its top edge, so those numbers would point at B: upside down on the prism. {cross()}</li>
<li><b>E</b>: going 1 → 2 → 3 round B is anticlockwise; in the original (also seen from outside) it is clockwise. E folds into the mirror image. {cross()}</li>
<li><b>B</b>: the faces are in the right order, but turn the net round so the numbers are upright: T sits on 5 and is upside down, pointing at face 5, not at the 2|3 corner. {cross()}</li></ul>""",
        f"""<p><b>C</b>: T sits between 4 (above) and 1 (below) with 2 and 3 on the right, and the T points right, at the 2|3 corner {tick()}.
B hangs under 6, so round B go 6, 1, 2, 3, 4, 5 and the leaning B points at the 5|6 corner {tick()}. The 5 4 3 numbers are upside down in the net, so they point at T too {tick()}.</p>
{calc(f'identical prism {ar()} {boxed("C")}')}""",
    ],
    answer_text='Net C: same order of sides, numbers all pointing to T, and T and B pointing at the same corners as the original.',
    why={'A': '1 and 6 are on opposite edges of T, so they would be opposite sides, but they should be next to each other.',
         'B': 'Faces in the right order, but the letters point the wrong way: T would point straight at face 5, not at the 2|3 corner.',
         'D': 'The 5 4 3 strip is attached to B along the top of its numbers, so those numbers would be upside down on the prism.',
         'E': 'The numbers run the wrong way round B, so it folds into a mirror image of the prism.'},
    fast='Kill A (1 opposite 6), D (5 4 3 upside down), E (mirror order), then compare letter directions: B’s T points at a face, C’s at the 2|3 corner.',
))

# ---------------------------------------------------------------- 23 (Q48)
def _sourdough():
    x0, base, sy, dx = 70, 260, 0.24, 110
    pts = [(0, 100), (1, 76), (1, 152), (2, 128), (2, 256), (3, 232), (3, 464), (4, 440), (4, 880)]
    P = lambda d, g: (x0 + d * dx, base - g * sy)
    parts = [line(x0, base, x0 + 4.6 * dx, base, k='ink', head=True), line(x0, base, x0, 20, k='ink', head=True),
             poly([P(d, g) for d, g in pts], k='pen', sw=3, closed=False),
             line(x0, base - 550 * sy, x0 + 4.5 * dx, base - 550 * sy, k='red', w=2.2, dash=True)]
    lab = [text(x0 + 8, base - 550 * sy - 8, 'need 550 g', k='red', size=16, anchor='start')]
    for d, name in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri']):
        lab.append(text(x0 + d * dx, base + 22, name, k='muted', size=15))
    for d, g in pts:
        x, y = P(d, g)
        parts.append(circle(x, y, 4, k='pen', fill='paper', sw=2))
    for (d, g, dxl, dyl) in ((0, 100, -6, -8), (1, 76, 8, 16), (1, 152, -8, 4), (2, 128, 8, 16), (2, 256, -8, 4),
                             (3, 232, 8, 16), (3, 464, -8, 4), (4, 440, 8, 16), (4, 880, 10, 6)):
        x, y = P(d, g)
        lab.append(text(x + dxl, y + dyl, g, k='green' if g == 880 else 'ink', size=14, anchor='start' if dxl > 0 else 'end'))
    lab += [text(x0 + 4 * dx + 14, base - 880 * sy + 26, 'Friday 8 am ✓', k='green', size=17, font='scrawl', anchor='start'),
            text(x0 + 1.5 * dx, base - 360 * sy, '−24 g a day, then double', k='orange', size=16)]
    return svg(640, 292, rough(*parts) + ''.join(lab),
               'Saw-tooth graph of sourdough weight: 100, drops to 76 then doubles to 152, 128 to 256, 232 to 464, 440 to 880 on Friday, passing the 550 g line')

Q.append(dict(
    n=23, orig=48, answer='D', topic='Step-by-step growth',
    question=f"""<p>Sourdough, an ingredient of many bread products, is a fermented mixture of flour and water. At
8:00 am on Monday morning, I start with a mixture of {hl('50 g flour and 50 g water', 'g', 1)}. Each morning at
8:00 am I {hl('double the weight of the sourdough', 'y', 2)} by adding equal weights of flour and water.
{hl('I know that 1 g of the water content evaporates every hour', 'p', 3)}.</p>
<p>The bread recipe that I would like to use requires {hl('500 g of sourdough', 'g', 4)}. I also want {hl('at least 50 g', 'g')}
of sourdough left over so that I can continue growing it for next week’s bread.</p>
<p class="stem">{hl('On which day', 'b', 5)} am I going to have the necessary amount of sourdough?</p>""",
    options={'A': 'Tuesday', 'B': 'Wednesday', 'C': 'Thursday', 'D': 'Friday', 'E': 'Saturday'},
    notes=[(1, 'g', 'Start: 100 g on Monday at 8 am.'),
           (2, 'y', 'Each 8 am: whatever is there is doubled.'),
           (3, 'p', '1 g an hour = <b>24 g lost</b> between one 8 am and the next. Take it off before doubling.'),
           (4, 'g', 'Need 500 + 50 = <b>550 g</b>.'),
           (5, 'b', 'The first morning it reaches 550 g.')],
    steps=[
        f"""<p>Each day: lose 24 g overnight, then double at 8 am.</p>
{calc('Mon 8 am: 100', 'Tue: 100 − 24 = 76 → × 2 = 152', 'Wed: 152 − 24 = 128 → × 2 = 256',
      'Thu: 256 − 24 = 232 → × 2 = 464 (not enough)', f'Fri: 464 − 24 = 440 → × 2 = 880 ≥ 550 {tick()}')}""",
        f"""{_sourdough()}
{calc(f'first day with 550 g {ar()} {boxed("Friday")}')}
{note('Without evaporation you get 100, 200, 400, 800, which reaches 550 on Thursday. The 24 g a day is what pushes it to Friday.', 'trap')}""",
    ],
    answer_text='Friday: Thursday only reaches 464 g, but after Friday’s 8 am feed there is 880 g.',
    why={'A': 'Tuesday only has 152 g.',
         'B': 'Wednesday only has 256 g. (You get Wednesday if you double on Monday morning as well.)',
         'C': 'Thursday is the answer if you ignore the evaporation (800 g). With it, Thursday only reaches 464 g.',
         'E': 'Saturday is a day late: Friday’s 8 am feed already gives 880 g.'},
    fast='Need 550. Lose 24, then double: 100 → 152 → 256 → 464 → 880. Friday.',
))

# ---------------------------------------------------------------- 24 (Q49)
def _nuts():
    s, x0 = 2, 60
    parts, lab = [], []
    y1, y2 = 40, 140
    segs1 = [(50, 'almonds 50 g', 'o'), (100, 'peanuts 100 g', 'y'), (100, 'others 100 g', 'b')]
    x = x0
    for g, name, f in segs1:
        parts.append(rect(x, y1, g * s, 40, k='ink', fill=f, sw=1.8))
        lab.append(text(x + g * s / 2, y1 + 26, name, k='ink', size=15))
        x += g * s
    lab += [text(x0, y1 - 10, 'before: 250 g (almonds at their 20% minimum, peanuts at their 40% maximum)', k='muted', size=14, anchor='start'),
            text(x0 + 25 * s, y1 + 60, 'eaten!', k='red', size=17, font='scrawl')]
    parts.append(line(x0 + 4, y1 + 4, x0 + 50 * s - 4, y1 + 36, k='red', w=2.4))
    x = x0 + 50 * s
    for g, name, f in segs1[1:]:
        parts.append(rect(x, y2, g * s, 40, k='ink', fill=f, sw=1.8))
        lab.append(text(x + g * s / 2, y2 + 26, name, k='ink', size=15))
        x += g * s
    parts.append(brace(x0 + 50 * s, x0 + 150 * s, y2 + 46, 'half of the 200 g left = 50%', k='green'))
    lab.append(text(x0 + 50 * s, y2 - 10, 'after: 200 g', k='muted', size=14, anchor='start'))
    return svg(640, 240, rough(*parts) + ''.join(lab),
               'Bag of 250 g: almonds 50, peanuts 100, others 100. After eating the almonds, 200 g remain and peanuts are half')

Q.append(dict(
    n=24, orig=49, answer='C', topic='Percentages',
    question=f"""<p>A {hl('250 g', 'g', 1)} bag of mixed nuts lists the contents on the packet as follows:</p>
{table([[hl('almonds', 'y'), hl('20-30%', 'y')], ['brazil nuts', '10-20%'], ['hazelnuts', '5-15%'],
        [hl('peanuts', 'g'), hl('30-40%', 'g')], ['pecans', '10-20%']], head=['<i>nut</i>', '<i>content</i>'])}
<p>As they are my favourite, I eat all the almonds in the packet and then re-weigh it. I find that the
{hl('almond content was the minimum it could have been', 'y', 2)} whilst being consistent with the labelling.</p>
<p class="stem">What is the {hl('largest possible peanut content', 'b', 3)} {hl('of the nuts remaining in the bag', 'p', 4)} after I have eaten
the almonds?</p>""",
    options={'A': '40%', 'B': '48%', 'C': '50%', 'D': '57%', 'E': '60%'},
    notes=[(1, 'g', 'Turn percentages into grams of this 250 g bag.'),
           (2, 'y', 'Almonds were 20% of 250 g = 50 g.'),
           (3, 'b', 'Peanuts as big as the label allows: 40% of the original bag.'),
           (4, 'p', 'The percentage is of the <b>new, smaller</b> amount, not the original 250 g.')],
    steps=[
        f"""<p>Work in grams:</p>
{calc('almonds: 20% of 250 = 50 g → 200 g left',
      'peanuts at most 40% of 250 = 100 g')}""",
        f"""{_nuts()}
{calc(f'100 ÷ 200 = ½ = {boxed("50%")}')}
{note('Do the other nuts still fit the label? Brazils, hazelnuts and pecans make the other 100 g = 40% of the bag, and their limits allow anything from 25% to 55%. Yes.', 'check')}""",
    ],
    answer_text='50%: 100 g of peanuts out of the 200 g left.',
    why={'A': '40% is the label’s maximum for the full bag. Taking the almonds out makes the peanuts a bigger share.',
         'B': '48% = 40% × 1.2: adding 20% on instead of dividing by the 80% that is left.',
         'D': '57% = 40 ÷ 70: this assumes the almonds were at their <b>maximum</b> (30%), not the minimum.',
         'E': '60% just adds the almonds’ 20% to the peanuts’ 40%.'},
    fast='Almonds 50 g out, 200 g left. Peanuts max 100 g. 100/200 = 50%.',
))

# ---------------------------------------------------------------- 25 (Q50)
def _dice_map():
    c, cx, cy = 84, 230, 150
    parts, lab = [], []
    for dx, dy, f in ((0, 0, 'y'), (0, -1, 'paper'), (1, 0, 'paper'), (0, 1, 'paper'), (-1, 0, 'paper')):
        parts.append(rect(cx + dx * c - c / 2, cy + dy * c - c / 2, c, c, k='ink', fill=f, sw=2))
    parts.append(line(cx, cy - 26, cx, cy + 26, k='ink', w=4))
    for ox in (-16, 0, 16):
        parts.append(line(cx + ox, cy - c - 26, cx + ox, cy - c + 26, k='ink', w=4))
    for ox in (-9, 9):
        parts.append(line(cx - c + ox, cy - 26, cx - c + ox, cy + 26, k='ink', w=4))
    vx = cx + c
    parts += [line(vx - 22, cy - 24, vx + 20, cy, k='ink', w=4), line(vx - 22, cy + 24, vx + 20, cy, k='ink', w=4)]
    ix, iy = cx, cy + c
    parts += [line(ix - 24, iy - 26, ix - 24, iy + 26, k='ink', w=4),
              line(ix - 8, iy - 26, ix + 8, iy + 26, k='ink', w=4), line(ix + 24, iy - 26, ix + 8, iy + 26, k='ink', w=4)]
    lab += [text(cx + c / 2 + 8, cy - c - 30, 'III: lines point at I', k='red', size=15, anchor='start'),
            text(vx + c / 2 + 8, cy - 20, 'V: opens', k='red', size=15, anchor='start'),
            text(vx + c / 2 + 8, cy, 'towards I', k='red', size=15, anchor='start'),
            text(cx + c / 2 + 8, cy + c + 30, 'IV: its top', k='red', size=15, anchor='start'),
            text(cx + c / 2 + 8, cy + c + 50, 'points at I', k='red', size=15, anchor='start'),
            ]
    rx = 470
    lab += [text(rx, 70, 'I on the right, line upright:', k='ink', size=17, anchor='start'),
            text(rx, 104, 'top III, left II', k='pen', size=20, font='scrawl', anchor='start'),
            text(rx, 132, 'or (turned over)', k='muted', size=16, anchor='start'),
            text(rx, 162, 'top IV, left V', k='pen', size=20, font='scrawl', anchor='start'),
            text(rx, 210, 'opposite faces:', k='ink', size=16, anchor='start'),
            text(rx, 234, 'I–VI, II–V, III–IV', k='green', size=18, font='scrawl', anchor='start'),
            text(rx, 258, '(each pair adds to 7!)', k='green', size=15, anchor='start')]
    return svg(680, 300, rough(*parts) + ''.join(lab),
               'Map of the faces round I as seen from outside: III above with lines pointing at I, V on the right opening towards I, IV below with its top towards I, II on the left')

Q.append(dict(
    n=25, orig=50, answer='D', topic='Nets & dice',
    question=f"""<p>The net below can be folded to make a {hl('Roman numerical dice', 'y', 1)}.</p>
{fig(Y, 'ps_q25_net', 'Net: V and III on the top row; VI, II, I on the middle row; IV under I', 260)}
<p class="stem">Which one of the following dice {hl('could have been made', 'b', 2)} as a result of folding the net?</p>
{fig(Y, 'ps_q25_dice', 'Five dice A to E, each showing three faces with Roman numerals at different angles; every die has I on the right face', 470)}""",
    options={'A': 'dice A', 'B': 'dice B', 'C': 'dice C', 'D': 'dice D', 'E': 'dice E'},
    notes=[(1, 'y', 'The numerals are drawings: the way their lines point matters, not just which number it is.'),
           (2, 'b', 'Four of the dice are impossible. Check which faces are next to each other <b>and</b> which way they point.')],
    steps=[
        f"""<p>Fold the net with VI facing you: III folds up to the top, II to the right, I round to the back, IV under I to the bottom, and V to the left.
So the opposite pairs are VI–I, II–V, III–IV.</p>""",
        f"""<p>Every die shows I on its right face. Look at the ring of faces round I, laid out flat as in the net (seen from outside):</p>{_dice_map()}
<p>With I upright on the right, the face <b>above</b> I is on top and the face to I’s <b>left</b> is on the left: top III, left II. Turn the die over (I looks the same) and you get top IV, left V.</p>""",
        f"""{calc(f'A: top III, left V {cross()} (III on top needs II on the left)',
                  f'B: left II, but the top is not III {cross()}',
                  f'E: V on top {cross()} (then I’s line would lie flat)',
                  'C: top III, left II: right faces, check the directions…',
                  'D: top IV, left V: right faces, check the directions…')}""",
        f"""<p><b>C</b>: III’s lines must point straight at the I face, but in C they run alongside I’s edge {cross()}<br>
<b>D</b>: IV’s top points at I, and V opens towards I {tick()}</p>
{calc(f'could have been made {ar()} {boxed("D")}')}""",
    ],
    answer_text='Dice D: IV on top pointing at I, V on the left opening towards I, I on the right.',
    why={'A': 'With III on top and I on the right, the left face must be II. V is on the far side. (Its V also opens away from I.)',
         'B': 'II on the left with I on the right means III must be on top, but B has a different numeral there.',
         'C': 'The right three faces, but the III is turned: its lines should run towards the I face, not parallel to the edge they share.',
         'E': 'V can’t be on top when I is upright on the right: the faces above and below I are III and IV.'},
    fast='I upright on the right forces top III/left II or top IV/left V. That leaves C and D; III’s lines must point at I, so C fails. D.',
))
