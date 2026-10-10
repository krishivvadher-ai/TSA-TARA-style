from wslib import *

Y = 2019
Q = []

# ---------------------------------------------------------------- 9 (Q19)
RECYCLE = [('Ambrosia', 52, 64, 65), ('Buranda', 60, 72, 80), ('Carbonda', 20, 27, 40), ('Elbonia', 32, 34, 40),
           ('Friponia', 36, 39, 45), ('Grandia', 20, 35, 60), ('Hoollasia', 50, 56, 60), ('Ishlapia', 33, 41, 44),
           ('Jackaran', 36, 44, 48), ('Killumpa', 40, 55, 70), ('Lateralia', 50, 57, 60), ('Moodle', 80, 98, 90),
           ('Nalpha', 32, 44, 48), ('Oritan', 72, 81, 90), ('Phillim', 66, 69, 70), ('Quaratus', 80, 90, 100),
           ('Rutalia', 75, 76, 90), ('Samalam', 88, 96, 99), ('Tuddle', 50, 56, 60), ('Ukliam', 50, 56, 60)]


def _triple():
    u = 5
    parts, lab = [], []
    for i, (name, a, c) in enumerate((('Grandia', 20, 60), ('Carbonda', 20, 40), ('Killumpa', 40, 70))):
        y = 30 + i * 62
        lab.append(text(110, y + 30, name, k='ink', size=17, anchor='end'))
        parts.append(rect(120, y, a * u, 20, k='ink', fill='b', sw=1.6))
        lab.append(text(120 + a * u / 2, y + 15, f'year 1: {a}', k='ink', size=13))
        x = 120
        parts.append(rect(x, y + 24, a * u, 20, k='ink', fill='b', sw=1.6))
        x += a * u
        inc = c - a
        while inc > 0:
            step = min(a, inc)
            parts.append(rect(x, y + 24, step * u, 20, k='red', fill='p', sw=1.6))
            lab.append(text(x + step * u / 2, y + 39, f'+{step}', k='red', size=14))
            x += step * u
            inc -= step
        pct = round((c - a) / a * 100)
        lab.append(text(x + 10, y + 39, f'= {c}  →  +{pct}%', k='green' if pct == 200 else 'ink', size=16, anchor='start'))
    lab.append(text(120, 222, 'each extra pink block the size of year 1 = +100%', k='muted', size=15, anchor='start'))
    return svg(640, 232, rough(*parts) + ''.join(lab),
               'Grandia 20 grows by two more 20s to 60, a 200% increase; Carbonda 20 to 40 is 100%; Killumpa 40 to 70 is 75%')

Q.append(dict(
    n=9, orig=19, answer='E', topic='Percentage change',
    question=f"""<p>The table below shows the amount of waste recycled each year, in thousands of tonnes, over a
three-year period in 20 countries.</p>
{table([[c, str(a), str(b), str(d)] for c, a, b, d in RECYCLE],
       head=['<i>country</i>', f'<i>{hl("recycling year 1", "g", 1)}</i>', f'<i>{hl("recycling year 2", "p", 2)}</i>', f'<i>{hl("recycling year 3", "g")}</i>'])}
<p class="stem">What is the {hl('biggest percentage increase', 'b', 3)} in recycling in the table from year 1 to year 3?</p>""",
    options={'A': '50%', 'B': '75%', 'C': '100%', 'D': '150%', 'E': '200%'},
    notes=[(1, 'g', 'Only the year 1 and year 3 columns matter.'),
           (2, 'p', 'Year 2 is a distraction. Skip it.'),
           (3, 'b', 'Percentage increase = increase ÷ start × 100. A <b>small start</b> that grows a lot wins, not the biggest numbers.')],
    steps=[
        f"""<p>Quick scan: which countries at least <b>double</b> (year 3 ≥ 2 × year 1)? Only two:</p>
{calc('Carbonda: 20 → 40, exactly double', 'Grandia: 20 → 60, three times as much!')}""",
        f"""<p>Picture the growth in blocks the size of year 1:</p>{_triple()}""",
        f"""{calc('Grandia: increase = 60 − 20 = 40', f'40 ÷ 20 = 2 = 200% {ar()} {boxed("200%")}')}
{note('Tripling means the amount is 300% <b>of</b> the start, but the <b>increase</b> is only 200%. Always subtract the start first.', 'trap')}""",
    ],
    answer_text='200%: Grandia goes from 20 to 60, an increase of 40, which is twice its starting value.',
    why={'A': '50% is Nalpha (32 → 48), nowhere near the biggest.',
         'B': '75% is Killumpa (40 → 70), the biggest <b>actual</b> rise after Grandia, but its start is larger.',
         'C': '100% is Carbonda (20 → 40), which only doubles. Grandia triples.',
         'D': '150% would need a country to go up 2.5 times (like 20 → 50). None does.'},
    fast='Look for small year-1 values: Grandia 20 → 60 triples. Increase 40 on 20 = 200%.',
))

# ---------------------------------------------------------------- 10 (Q20)
def _glass():
    c, px, py = 28, 40, 54
    parts, lab = [], []
    parts.append(poly([(px, py), (px + 2 * c, py), (px + 2 * c, py + c), (px + 4 * c, py + c), (px + 4 * c, py),
                       (px + 7 * c, py), (px + 7 * c, py + 3 * c), (px, py + 3 * c)], k='muted', fill='b', sw=1))
    parts.append(rect(px, py + 3 * c, 7 * c, 2 * c, k='muted', fill='y', sw=1))
    for i in range(1, 7):
        parts.append(line(px + i * c, py + 5 * c - 6, px + i * c, py + 5 * c + 6, k='ink', w=1.6))
    for j in range(1, 5):
        parts.append(line(px - 6, py + j * c, px + 6, py + j * c, k='ink', w=1.6))
    outline = [(0, 0), (2, 0), (2, 1), (4, 1), (4, 0), (7, 0), (7, 5), (0, 5)]
    parts.append(poly([(px + x * c, py + y * c) for x, y in outline], k='ink', sw=2.6))
    parts.append(line(px, py + 3 * c, px + 7 * c, py + 3 * c, k='ink', w=2.2))
    lab += [text(px + 3.5 * c, py - 26, 'BACK', k='muted', size=15),
            text(px + 3 * c, py - 6, 'slot', k='red', size=15),
            text(px + 3.5 * c, py + 1.6 * c + 6, '4 high', k='pen', size=18),
            text(px + 3.5 * c, py + 4 * c + 6, '2 high (step)', k='orange', size=17),
            text(px + 3.5 * c, py + 5 * c + 24, 'FRONT', k='muted', size=15),
            text(px + 3.5 * c, py + 5 * c + 44, 'plan from above: 7 long, 5 deep', k='ink', size=15),
            text(px + 3.5 * c, py + 5 * c + 64, 'slot goes right down to the floor', k='red', size=15)]
    u = 13

    def view(x, y, pts, extra, label, k='green'):
        p = [poly([(x + a * u, y + b * u) for a, b in pts], k='ink', sw=2.2)]
        p += [line(x + a * u, y + b * u, x + c2 * u, y + d * u, k='ink', w=1.8) for a, b, c2, d in extra]
        return p, text(x + 3 * u, y - 8, label, k=k, size=15)

    vx = 330
    for pts, extra, x, y, label in (
            ([(0, 0), (7, 0), (7, 4), (0, 4)], [(0, 2, 7, 2), (3, 0, 3, 4), (5, 0, 5, 4)], vx, 40, 'from back = B ✓'),
            ([(0, 0), (3, 0), (3, 2), (5, 2), (5, 4), (0, 4)], [(1, 0, 1, 4)], vx + 150, 40, 'from left = A ✓'),
            ([(0, 2), (2, 2), (2, 0), (5, 0), (5, 4), (0, 4)], [(4, 0, 4, 4)], vx, 150, 'from right = D ✓'),
            ([(0, 0), (3, 0), (3, 1), (5, 1), (5, 0), (7, 0), (7, 5), (0, 5)], [(0, 3, 7, 3)], vx + 150, 150, 'from below = C ✓')):
        p, t = view(x, y, pts, extra, label)
        parts += p
        lab.append(t)
    ex, ey = vx + 100, 262
    parts += [rect(ex, ey, 5 * u, 6 * u, k='red', sw=2.2), rect(ex + u, ey, 2 * u, u, k='red', sw=1.8),
              line(ex, ey + 3 * u, ex + 5 * u, ey + 3 * u, k='red', w=1.8)]
    lab += [text(ex + 5 * u + 12, ey + 22, 'E: 5 × 6? nothing is 6 long', k='red', size=15, anchor='start'),
            text(ex + 5 * u + 12, ey + 44, 'slot boxed in? it is open', k='red', size=15, anchor='start'),
            text(ex + 5 * u + 12, ey + 66, 'at the back ✗', k='red', size=15, anchor='start')]
    return svg(660, 350, rough(*parts) + ''.join(lab),
               'Plan of the block: 7 by 5 with a front step 2 deep and a slot in the back; the views from back, left, right and below match B, A, D and C; E does not fit')

Q.append(dict(
    n=10, orig=20, answer='E', topic='3D views',
    question=f"""<p>The {hl('see-through', 'y', 1)} glass block below can be viewed from {hl('six sides, including from above and below', 'y', 2)}.</p>
{fig(Y, 'ps_q10_block', 'A glass block: a long low step at the front, a taller block behind it, with a narrow slot cut into the back', 330)}
<p class="stem">Which one of the following is {hl('<b>not</b>', 'b', 3)} a possible view?</p>
{fig(Y, 'ps_q10_views', 'Five line drawings A to E: A and D are L-shapes, B is a rectangle split into six, C has a notch in its top edge, E has a small box inside its top edge', 470)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'See-through: hidden edges show as lines too. So the view from the back is just the front view flipped, and so on.'),
           (2, 'y', 'Six views: front, back, left, right, top, bottom. Find which drawing matches none.'),
           (3, 'b', 'Four drawings are real views; find the odd one out.')],
    steps=[
        f"""<p>Measure the block using the drawing’s edges as units: <b>7</b> long, <b>5</b> deep, <b>4</b> tall.
At the front is a step <b>2</b> deep and <b>2</b> high. Behind it the block is 4 high, with a slot <b>2</b> wide and <b>1</b> deep cut into the back, all the way down.</p>
{_glass()}""",
        f"""<p>Now match each pair of views (opposite views are mirror images, because it is see-through):</p>
{calc(f'front / back: 7 × 4, a line across halfway (the step), two lines up (the slot sides) {ar()} B {tick()}',
      f'left / right: an L-shape 5 wide, tall part 3, step 2, and a line 1 in (the slot) {ar()} A and D {tick()}',
      f'top / bottom: 7 × 5 with a 2 × 1 notch in the back edge and a line 2 from the front {ar()} C {tick()}')}""",
        f"""<p>E is 5 wide and <b>6</b> tall, and draws the slot as a closed box. No edge of the block is 6 long, and the slot is cut through
the back face, so it must be a gap in the outline (as in C), not a box inside it.</p>
{calc(f'not possible {ar()} {boxed("E")}')}""",
    ],
    answer_text='E: wrong shape (5 × 6) and the slot is drawn boxed in, but it is open at the back.',
    why={'A': 'A is the view from the left: L-shape with the tall part on the left and the slot’s face 1 unit in.',
         'B': 'B is the view from the back: the step line across the middle and the two slot sides (3, 2, 2).',
         'C': 'C is the view from below: 7 × 5, the slot as a notch in the back edge, the step line 2 from the front.',
         'D': 'D is the view from the right: A’s mirror image.'},
    fast='Side views are L-shapes (A, D), front/back is the 2 × 3 grid (B), top/bottom has the notch (C). E has a size the block doesn’t have.',
))

# ---------------------------------------------------------------- 11 (Q24)
SEGS = {1: 'bc', 2: 'abged', 3: 'abgcd', 4: 'fgbc', 5: 'afgcd', 6: 'afgecd', 7: 'abc', 8: 'abcdefg', 9: 'abcdfg'}


def _seg_lines(x, y, w, h):
    return {'a': (x, y, x + w, y), 'b': (x + w, y, x + w, y + h / 2), 'c': (x + w, y + h / 2, x + w, y + h),
            'd': (x, y + h, x + w, y + h), 'e': (x, y + h / 2, x, y + h), 'f': (x, y, x, y + h / 2),
            'g': (x, y + h / 2, x + w, y + h / 2)}


def _segments():
    parts, lab = [], []
    for i in range(1, 10):
        x, y = 28 + (i - 1) * 52, 36
        for s, (x1, y1, x2, y2) in _seg_lines(x, y, 26, 52).items():
            if s in SEGS[i]:
                parts.append(line(x1, y1, x2, y2, k='ink', w=5))
            else:
                parts.append(line(x1, y1, x2, y2, k='muted', w=1, dash=True))
        lab.append(text(x + 13, 116, i, k='muted', size=16))
    counts = {s: sum(s in v for v in SEGS.values()) for s in 'abcdefg'}
    bx, by, bw, bh = 560, 26, 60, 120
    for s, (x1, y1, x2, y2) in _seg_lines(bx, by, bw, bh).items():
        k = 'green' if s == 'c' else 'red' if s == 'e' else 'ink'
        parts.append(line(x1, y1, x2, y2, k=k, w=6))
    pos = {'a': (bx + bw / 2, by - 8), 'b': (bx + bw + 16, by + bh / 4 + 6), 'c': (bx + bw + 16, by + 3 * bh / 4 + 6),
           'd': (bx + bw / 2, by + bh + 22), 'e': (bx - 16, by + 3 * bh / 4 + 6), 'f': (bx - 16, by + bh / 4 + 6),
           'g': (bx + bw / 2, by + bh / 2 - 6)}
    for s, (x, y) in pos.items():
        k = 'green' if s == 'c' else 'red' if s == 'e' else 'pen'
        lab.append(text(x, y, counts[s], k=k, size=20, font='scrawl', weight='700'))
    lab += [text(bx + bw + 30, by + 3 * bh / 4 + 26, 'max', k='green', size=15, anchor='start'),
            text(bx - 30, by + 3 * bh / 4 + 26, 'min', k='red', size=15, anchor='end'),
            text(270, 150, 'digits 1 to 9 (thick = lit)', k='muted', size=15)]
    return svg(680, 180, rough(*parts) + ''.join(lab),
               'Digits 1 to 9 on seven-segment displays, and a big display showing how often each segment lights: top 7, top right 7, bottom right 8, bottom 6, bottom left 3, top left 5, middle 7')

Q.append(dict(
    n=11, orig=24, answer='C', topic='Counting',
    question=f"""<p>A digital display consists of seven segments which light up in different combinations to produce
digits. For example, to display the digit ‘1’ the two right-hand segments light up as shown:</p>
{fig(Y, 'ps_q11_display', 'Seven-segment display with only the two right-hand segments lit, showing 1', 70)}
<p>The display is used to show, in sequence, {hl('each of the digits 1 to 9', 'g', 1)}.</p>
<p class="stem">What is the {hl('maximum and minimum', 'b', 2)} number of times that {hl('any one segment', 'y', 3)} lights up during this
sequence?</p>""",
    options={'A': 'maximum 7, minimum 4', 'B': 'maximum 7, minimum 5', 'C': 'maximum 8, minimum 3',
             'D': 'maximum 8, minimum 5', 'E': 'maximum 9, minimum 4'},
    notes=[(1, 'g', 'Nine digits: 1, 2, … 9. No 0!'),
           (2, 'b', 'Two answers: the busiest segment and the laziest segment.'),
           (3, 'y', 'Count for each of the 7 segments separately.')],
    steps=[
        f"""<p>Draw the nine digits as they appear on the display, then count how often each segment is lit:</p>{_segments()}""",
        f"""{calc('top 7, top-right 7, middle 7, bottom 6, top-left 5',
                  f'bottom-right: every digit except 2 {ar()} <b>8</b>',
                  f'bottom-left: only 2, 6 and 8 {ar()} <b>3</b>',
                  f'maximum 8, minimum 3 {ar()} {boxed("C")}')}
{note('Whether your 7 has a top-left bar or your 9 has a bottom bar, the bottom-right still scores 8 and the bottom-left 3.', 'check')}""",
    ],
    answer_text='Maximum 8 (bottom-right, every digit except 2), minimum 3 (bottom-left, only 2, 6 and 8).',
    why={'A': '7 is the count for the top, top-right and middle segments; the bottom-right beats it with 8.',
         'B': 'Both wrong: max is 8 (bottom-right), and 5 is the top-left count, not the smallest.',
         'D': 'Max 8 is right, but 5 (top-left) isn’t the minimum: the bottom-left only lights 3 times.',
         'E': '9 would need a segment lit in every digit. 1 uses only the two right-hand segments, and 2 doesn’t use the bottom-right.'},
    fast='Bottom-right is in everything except 2 → 8. Bottom-left is only in 2, 6, 8 → 3.',
))

# ---------------------------------------------------------------- 12 (Q25)
def _stays():
    days = ['Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue']
    w, x0 = 66, 120
    parts, lab = [], []
    for i, d in enumerate(days):
        parts.append(rect(x0 + i * w, 20, w, 34, k='ink', fill='y' if d == 'Sat' else 'paper', sw=1.6))
        lab.append(text(x0 + i * w + w / 2, 43, d, k='ink', size=17))
    for j, (name, f) in enumerate((('Wed–Sat', 'b'), ('Thu–Sun', 'g'), ('Fri–Mon', 'o'), ('Sat–Tue', 'v'))):
        y = 68 + j * 30
        parts.append(rect(x0 + j * w + 4, y, 4 * w - 8, 20, k='ink', fill=f, sw=1.4))
        lab.append(text(x0 - 10, y + 16, name, k='ink', size=15, anchor='end'))
    lab.append(text(x0 + 3.5 * w, 200, 'only 4 ways to stay 4 nights in a row and include Saturday', k='muted', size=15))
    return svg(620, 210, rough(*parts) + ''.join(lab),
               'Week strip Wednesday to Tuesday with Saturday highlighted and the four possible four-night stays drawn as bars')


def _best_hotels():
    rows = [('Grand', 170, 'Fri–Mon'), ('Majestic', 165, 'Fri–Mon'), ('Palace', 140, 'Fri–Mon'), ('Palms', 160, 'Thu–Sun'), ('Plaza', 180, 'Thu–Sun')]
    X = lambda v: 110 + v * 2.2
    parts, lab = [], []
    for i, (name, v, when) in enumerate(rows):
        y = 18 + i * 34
        parts.append(rect(X(0), y, X(v) - X(0), 22, k='ink', fill='g' if v == 140 else 'paper', sw=1.6))
        lab.append(text(100, y + 17, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 8, y + 17, f'€{v} ({when})', k='green' if v == 140 else 'ink', size=16, anchor='start'))
    return svg(640, 190, rough(*parts) + ''.join(lab),
               'Cheapest stay at each hotel: Grand 170, Majestic 165, Palace 140, Palms 160, Plaza 180')

Q.append(dict(
    n=12, orig=25, answer='C', topic='Best deal',
    question=f"""<p>Sandi is planning a trip to the old city of Pordson. She wants to stay for {hl('four nights', 'g', 1)} in order to
visit all of the attractions, and {hl('one of the nights must be the Saturday', 'y', 2)} so that she can attend a
special music concert.</p>
<p>The table below shows the prices per night and details of the deals for the five main hotels in
Pordson.</p>
{table([['Grand', '€60', '€70', '€70', '€70', '€50', '€60', '€60', '3F2'],
        ['Majestic', '€40', '€90', '€70', '€70', '€40', '€90', '€40', 'SFSHP'],
        ['Palace', '€60', '€90', '€90', '€70', '€50', '€90', '€80', hl('50%', 'p')],
        ['Palms', '€60', '€80', '€80', '€50', '€40', '€60', '€50', '4FP3'],
        ['Plaza', '€70', '€90', '€90', '€60', '€50', '€70', '€50', 'CBK']],
       head=['<i>Hotel</i>', '<i>Mon</i>', '<i>Tues</i>', '<i>Weds</i>', '<i>Thurs</i>', '<i>Fri</i>', f'<i>{hl("Sat", "y")}</i>', '<i>Sun</i>', '<i>Deal</i>'])}
<p>Deals:</p>
{table([['3F2', 'Stay 2 nights and get the 3<sup>rd</sup> night free.'],
        ['SFSHP', 'Stay Friday and get the Saturday night half price.'],
        ['50%', hl('50% discount on all stays of 3 or more nights.', 'p', 3)],
        ['4FP3', 'Stay 4 nights and get the cheapest night free.'],
        ['CBK', '€50 discount on stays of 3 or more nights.']])}
<p class="stem">What is the {hl('minimum', 'b', 4)} that Sandi will need to spend on a hotel bill for her stay in Pordson?</p>""",
    options={'A': '€110', 'B': '€120', 'C': '€140', 'D': '€145', 'E': '€160'},
    notes=[(1, 'g', 'Four nights in a row.'),
           (2, 'y', 'Saturday must be one of the four, so there are only four possible stays.'),
           (3, 'p', 'Half off everything is the monster deal. The others save one night at most.'),
           (4, 'b', 'Cheapest total over every hotel and every possible stay.')],
    steps=[
        f"""<p>List the possible stays first:</p>{_stays()}""",
        f"""<p>Start with the biggest saving, Palace’s 50%. Add the four nights, then halve:</p>
{calc('Wed–Sat: 90 + 70 + 50 + 90 = 300 → 150', 'Thu–Sun: 70 + 50 + 90 + 80 = 290 → 145',
      '<b>Fri–Mon: 50 + 90 + 80 + 60 = 280 → 140</b>', 'Sat–Tue: 90 + 80 + 60 + 90 = 320 → 160')}""",
        f"""<p>Check the other hotels’ best stays can’t beat €140:</p>
{calc('Grand Fri–Mon: 50 + 60 + (Sun free) + 60 = 170',
      'Majestic Fri–Mon: 40 + 45 (half price Sat) + 40 + 40 = 165',
      'Palms Thu–Sun: 50 + 40 + 60 + 50 = 200, minus cheapest 40 = 160',
      'Plaza Thu–Sun: 60 + 50 + 70 + 50 = 230, minus 50 = 180')}
{_best_hotels()}
{calc(f'minimum = Palace, Friday to Monday = {boxed("€140")}')}""",
    ],
    answer_text='€140: four nights at the Palace from Friday to Monday (€280, half price).',
    why={'A': '€110 is the Palace for only <b>three</b> nights (Fri–Sun: 220 ÷ 2). She needs four.',
         'B': '€120 can’t be made: at the Palace it would need four nights costing €240, but the cheapest run including Saturday is €280.',
         'D': '€145 is the Palace from Thursday to Sunday. Fri–Mon is €5 cheaper.',
         'E': '€160 is the best at the Palms (Thu–Sun), or the Palace from Saturday to Tuesday.'},
    fast='Halving beats one free night. Palace: cheapest 4-night run with Sat is Fri–Mon = 280. Half = 140.',
))

# ---------------------------------------------------------------- 13 (Q26)
def _tri(cx, cy, s=14, k='ink'):
    return poly([(cx - s, cy), (cx + s * 0.8, cy - s * 0.9), (cx + s * 0.8, cy + s * 0.9)], k=k, fill='ink', sw=1)


def _bar(cx, cy, k='ink'):
    return rect(cx - 6, cy - 15, 12, 30, k=k, fill='ink', sw=1)


def _roll_path():
    c, x0, y0 = 62, 40, 30
    cells = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2)]
    parts, lab = [], []
    for i, (cx, cy) in enumerate(cells):
        f = 'y' if i in (0, 4) else 'g' if i in (2, 6) else 'paper'
        parts.append(rect(x0 + cx * c, y0 + cy * c, c, c, k='ink', fill=f, sw=2))
        mx, my = x0 + cx * c + c / 2, y0 + cy * c + c / 2
        if i in (0, 4):
            parts.append(_tri(mx, my - 4))
        elif i in (2, 6):
            parts.append(_bar(mx, my - 4))
        else:
            lab.append(text(mx, my, 'side', k='muted', size=14))
        if i:
            lab.append(text(x0 + cx * c + 10, y0 + cy * c + c - 6, i, k='red', size=14, anchor='start'))
    lab += [text(x0 + c / 2, y0 + c + 20, 'start', k='ink', size=15),
            text(x0 + 2.5 * c + 80, y0 + 26, 'after 2 rolls:', k='green', size=16, anchor='start'),
            text(x0 + 2.5 * c + 80, y0 + 48, 'bar on top', k='green', size=16, anchor='start'),
            text(x0 + 2 * c - 10, y0 + 2.5 * c + 4, 'after 4:', k='orange', size=16, anchor='end'),
            text(x0 + 2 * c - 10, y0 + 2.5 * c + 24, 'triangle again', k='orange', size=16, anchor='end'),
            text(x0 + 4.5 * c, y0 + 3 * c + 24, 'after 6: bar', k='green', size=18, font='scrawl'),
            text(x0 + 4 * c + 60, y0 + 1.2 * c, 'red numbers =', k='red', size=14, anchor='start'),
            text(x0 + 4 * c + 60, y0 + 1.2 * c + 18, 'rolls so far', k='red', size=14, anchor='start')]
    return svg(560, 260, rough(*parts) + ''.join(lab),
               'The path: 2 rolls right, 2 rolls down, 2 rolls right; the triangle is on top at the start and after 4 rolls, the bar after 2 and after 6')


def _flip():
    parts, lab = [line(10, 120, 570, 120, k='muted', w=1.4)], []
    s = 76
    specs = [('top', 'bottom', 'start: ▲ on top'), ('right', 'left', '1 roll: ▲ on the side'), ('bottom', 'top', '2 rolls: bar on top')]
    for i, (tri, bar, cap) in enumerate(specs):
        x, y = 40 + i * 190, 44
        parts.append(rect(x, y, s, s, k='ink', fill='paper', sw=2.2))
        spot = {'top': (x + s / 2, y + 18), 'bottom': (x + s / 2, y + s - 6), 'right': (x + s - 14, y + s / 2 + 6), 'left': (x + 14, y + s / 2 + 6)}
        tx, ty = spot[tri]
        lab.append(text(tx, ty, '▲', k='pen', size=18))
        bx, by = spot[bar]
        if bar in ('top', 'bottom'):
            parts.append(rect(bx - 12, by - 12, 24, 7, k='ink', fill='ink', sw=1))
        else:
            parts.append(rect(bx - 4, by - 18, 7, 24, k='ink', fill='ink', sw=1))
        lab.append(text(x + s / 2, 144, cap, k='pen' if i < 2 else 'green', size=16))
        if i < 2:
            parts.append(arrow(x + s + 20, 36, x + 170, 36, k='red', bend=-0.25))
            lab.append(text(x + s + 57, 18, 'roll →', k='red', size=15))
    lab.append(text(300, 176, 'two rolls the same way = upside down', k='green', size=19, font='scrawl'))
    return svg(600, 188, rough(*parts) + ''.join(lab),
               'Side view of a cube rolled twice: the triangle goes from the top to the side to the bottom, and the bar comes up to the top')


Q.append(dict(
    n=13, orig=26, answer='D', topic='Rolling a cube',
    question=f"""<p>A solid cube has 6 different shapes drawn on each of its 6 faces. A plan view showing all the
shapes is given below. It is placed on the path drawn below with the {hl('triangular shape facing up', 'g', 1)}.
The cube is rolled, {hl('one face at a time', 'y', 2)}, forward along the route shown, from start position until it
reaches the end position.</p>
{fig(Y, 'ps_q13_cube', 'The cube, its net (bar, square, triangle, cross in a row, with a dotted circle above and a black circle below the triangle) and the path: 3 squares right, 2 down, 2 right', 560)}
<p class="stem">Which one of the following shapes is {hl('facing up', 'b', 3)} when it reaches the end position?</p>
{fig(Y, 'ps_q13_opts', 'Options: A square, B black circle, C triangle, D tall bar, E circle with a white dot', 400)}""",
    options={'A': 'square', 'B': 'black circle', 'C': 'triangle', 'D': 'tall bar', 'E': 'circle with a white dot'},
    notes=[(1, 'g', 'Start: triangle on top. So the face opposite the triangle is on the bottom.'),
           (2, 'y', 'Each move tips the cube over one edge: count the moves along the path.'),
           (3, 'b', 'Only the top face matters at the end.')],
    steps=[
        f"""<p>Opposite faces from the net: in a straight row of four, faces two apart are opposite.</p>
{calc('bar ↔ triangle', 'square ↔ cross', 'dotted circle ↔ black circle (above and below the triangle)')}
<p>So at the start the <b>bar</b> is underneath.</p>""",
        f"""<p>Key trick: rolling <b>twice in the same direction</b> turns the cube upside down.</p>{_flip()}""",
        f"""<p>The path is 2 rolls right, 2 rolls down, 2 rolls right: three “double rolls”, so the cube flips three times.</p>
{_roll_path()}
{calc(f'triangle → bar → triangle → bar {ar()} {boxed("D")}')}""",
    ],
    answer_text='The tall bar: three double rolls flip the cube three times, so the face that started underneath ends on top.',
    why={'A': 'The square starts on a side. Double rolls only swap top and bottom, so a side face can’t finish on top.',
         'B': 'The black circle also starts on a side, so it can’t finish on top either.',
         'C': 'The triangle is back on top after 4 rolls. You get this if you miss one of the straight pairs, or think 6 rolls bring you back to the start.',
         'E': 'The dotted circle starts on a side (it is opposite the black circle), so it can’t be on top at the end.'},
    fast='Opposite triangle = bar. Path = three pairs of rolls; each pair flips the cube. Odd number of flips → bar on top.',
))

# ---------------------------------------------------------------- 14 (Q30)
def _cards():
    g = [[5, 1, 8], [3, 6, 2], [9, 7, 4]]
    c, x0, y0 = 62, 40, 24
    parts, lab = [], []
    for r in range(3):
        for col in range(3):
            parts.append(rect(x0 + col * c, y0 + r * c, c, c, k='ink', fill='paper', sw=2))
            lab.append(text(x0 + col * c + c / 2, y0 + r * c + c / 2 + 9, g[r][col], k='ink', size=26, font='print'))
    parts.append(rect(x0 + 6, y0 + 2 * c + 8, 2 * c - 12, c - 16, k='green', sw=3, rx=22))
    parts.append(rect(x0 + c + 8, y0 + 6, 2 * c - 16, c - 12, k='orange', sw=3, rx=22))
    lab += [text(x0 + 3 * c + 30, y0 + 30, '1 and 8: best difference = 7', k='orange', size=18, anchor='start'),
            text(x0 + 3 * c + 30, y0 + 2.5 * c + 4, '9 and 7: average = 8', k='green', size=18, anchor='start'),
            text(x0 + 3 * c + 30, y0 + 2.5 * c + 28, 'beats ANY difference', k='green', size=18, font='scrawl', anchor='start'),
            text(x0 + 3 * c + 30, y0 + 1.5 * c + 6, 'pairs must touch side to side', k='muted', size=15, anchor='start')]
    return svg(560, 220, rough(*parts) + ''.join(lab),
               'Card grid 5 1 8, 3 6 2, 9 7 4 with 1 and 8 circled (difference 7) and 9 and 7 circled (average 8)')

Q.append(dict(
    n=14, orig=30, answer='E', topic='Games & strategy',
    question=f"""<p>Alex and Sue are playing a game with a set of nine cards, numbered from 1 to 9. A 3 × 3 grid of
cards is dealt onto the table. The cards for the next round have just been dealt and are as
shown below.</p>
{table([['5', '1', '8'], ['3', '6', '2'], ['9', '7', '4']], cls='grid3')}
<p>{hl('The first player chooses two cards and scores the difference between the two numbers', 'g', 1)}. {hl('The second player then chooses two cards from the seven that are left and scores the average of the two numbers', 'g', 2)}. The highest score wins the round. {hl('Both players must choose cards that are either horizontally or vertically next to each other', 'y', 3)} in the grid.</p>
<p>For this round of the game Alex has to decide whether to play first or second. She wants to
{hl('make sure that she wins the round', 'b', 4)}. {hl('If she has more than one possible winning move then she wants to achieve the highest score possible', 'p', 5)}.</p>
<p class="stem">What should Alex choose to do?</p>""",
    options={'A': 'play first and choose the 1 and 8', 'B': 'play first and choose the 3 and 9',
             'C': 'play first and choose the 6 and 7', 'D': 'play first and choose the 7 and 9', 'E': 'play second'},
    notes=[(1, 'g', 'First player: difference (big gap wins).'),
           (2, 'g', 'Second player: average (two big cards win).'),
           (3, 'y', 'Only touching pairs, side by side or up and down. No diagonals.'),
           (4, 'b', 'She must win <b>whatever</b> Sue does.'),
           (5, 'p', 'Only a tie-breaker between winning moves. Winning comes first.')],
    steps=[
        f"""<p>Find the best pairs:</p>{_cards()}
{calc('biggest difference: 1 and 8 → 7', 'biggest average: 9 and 7 → 8')}""",
        f"""<p><b>If Alex plays first</b>, 9 and 7 (average 8) beat her unless she takes the 9 or the 7. Check every option:</p>
{calc(f'1 and 8 → 7, Sue takes 9 and 7 → 8 {cross()}',
      f'3 and 9 → 6, Sue takes 6 and 7 → 6.5 {cross()}',
      f'7 and 4 → 3, Sue takes 3 and 9 → 6 {cross()}',
      f'7 and 9 → 2, Sue takes 8 and 2 → 5 {cross()}',
      f'6 and 7 → 1, Sue takes 3 and 9 → 6 {cross()}')}
<p>Playing first <b>always loses</b>.</p>""",
        f"""<p><b>If Alex plays second</b>: if Sue leaves 9 and 7, Alex scores 8, more than any difference. If Sue takes the 9 or the 7, Sue scores at most 6, and Alex still has a better pair (6 and 7 → 6.5, or 3 and 9 → 6, or 8 and 2 → 5) every time.</p>
{calc(f'second always wins {ar()} {boxed("play second")}')}""",
    ],
    answer_text='Play second: whatever Sue picks, Alex can find a touching pair with a higher average.',
    why={'A': '1 and 8 scores 7, but Sue replies with 9 and 7 for an average of 8.',
         'B': '3 and 9 scores 6, but Sue takes 6 and 7 for 6.5.',
         'C': '6 and 7 scores only 1; Sue takes 3 and 9 for 6.',
         'D': '7 and 9 scores only 2; Sue takes 8 and 2 for 5.'},
    fast='9 and 7 average 8 beats the best difference (7). Blocking them leaves you a tiny difference. So go second.',
))

# ---------------------------------------------------------------- 15 (Q31)
def _ferry_days():
    x0 = 110
    parts, lab = [], []

    def day(y, n, gap, start, end, title):
        x = x0
        for i in range(n):
            parts.append(rect(x, y, 50, 30, k='ink', fill='b', sw=1.4))
            lab.append(text(x + 25, y + 21, 50, k='ink', size=14))
            x += 50
            if i < n - 1:
                parts.append(rect(x, y, gap, 30, k='ink', fill='o', sw=1.4))
                x += gap
        lab.extend([text(x0, y - 8, start, k='muted', size=15), text(x, y - 8, end, k='muted', size=15),
                    text(x0 - 10, y + 21, title, k='ink', size=17, anchor='end')])
        return x

    e1 = day(40, 6, 20, '9:30', '4:10', 'long day')
    e2 = day(130, 4, 10, '10:30', '2:20', 'short day')
    lab += [text(e1 + 12, 61, '6 crossings', k='pen', size=17, anchor='start'),
            text(e1 - 200, 98, '6 × 50 + 5 × 20 = 400 min ✓ exactly', k='pen', size=15),
            text(e2 + 12, 151, '4 crossings', k='pen', size=17, anchor='start'),
            text(x0 + 115, 188, '4 × 50 + 3 × 10 = 230 min ✓ exactly', k='pen', size=15),
            text(x0, 214, 'blue = crossing (50 min), orange = stopover', k='muted', size=14, anchor='start')]
    return svg(640, 224, rough(*parts) + ''.join(lab),
               'Timelines: a long day fits 6 crossings with 20-minute stops in 400 minutes; a short day fits 4 crossings with 10-minute stops in 230 minutes')


def _may():
    c, x0, y0 = 50, 20, 40
    parts, lab = [], []
    for i, d in enumerate('MTWTFSS'):
        lab.append(text(x0 + i * c + c / 2, y0 - 10, d, k='muted', size=16))
    for day in range(1, 32):
        col, row = (day - 1) % 7, (day - 1) // 7
        long_ = col >= 5 or day in (1, 29)
        parts.append(rect(x0 + col * c + 2, y0 + row * 38 + 2, c - 4, 34, k='ink', fill='o' if long_ else 'b', sw=1.3))
        lab.append(text(x0 + col * c + c / 2, y0 + row * 38 + 25, day, k='ink', size=15, font='print'))
    tx = x0 + 7 * c + 20
    lab += [text(tx, 70, 'orange = long day', k='orange', size=17, anchor='start'),
            text(tx, 92, '8 weekend + 2 bank hols', k='orange', size=16, anchor='start'),
            text(tx, 114, '= 10 days', k='orange', size=18, font='scrawl', anchor='start'),
            text(tx, 148, 'blue = short day', k='pen', size=17, anchor='start'),
            text(tx, 170, '31 − 10 = 21 days', k='pen', size=18, font='scrawl', anchor='start')]
    return svg(640, 240, rough(*parts) + ''.join(lab),
               'May calendar: Saturdays, Sundays and the bank holidays on the 1st and 29th are long days (10); the other 21 are short days')

Q.append(dict(
    n=15, orig=31, answer='B', topic='Timetables & calendars',
    question=f"""<p>The single ferry to Pepper Island starts each day from mainland Seatown and crosses to the
island port of Kaysville. It runs back and forth from {hl('9:30 am to 4:10 pm on Saturdays, Sundays and Bank Holidays', 'g', 1)}, and {hl('from 10:30 am to 2:20 pm from Monday to Friday', 'g', 2)}.</p>
{fig(Y, 'ps_q15_may', 'May calendar starting on Monday 1st; the 1st and the 29th (both Mondays) are shaded as Bank Holidays', 260)}
<p>{hl('Each crossing takes 50 minutes', 'g', 3)}. Between crossings, there is a {hl('10-minute stopover', 'y', 4)} for cleaning
and refuelling. This is {hl('extended to 20 minutes on Saturdays, Sundays and Bank Holidays', 'p', 5)} to
allow for the increased cleaning requirements.</p>
<p class="stem">What is the {hl('maximum number of crossings', 'b', 6)} the ferry can make in May?</p>""",
    options={'A': '140', 'B': '144', 'C': '154', 'D': '166', 'E': '186'},
    notes=[(1, 'g', 'Long day: 6 h 40 min = 400 minutes.'),
           (2, 'g', 'Short day: 3 h 50 min = 230 minutes.'),
           (3, 'g', 'Every crossing is 50 minutes.'),
           (4, 'y', 'Stops come <b>between</b> crossings: one fewer stop than crossings.'),
           (5, 'p', 'Bank Holidays (the 1st and 29th) count as long days, even though they are Mondays.'),
           (6, 'b', 'Fit in as many as possible each day, then add up the whole month.')],
    steps=[
        f"""<p>How many crossings fit into each kind of day? Remember: n crossings need only n − 1 stops.</p>{_ferry_days()}""",
        f"""<p>Now count the days in May (it starts on a Monday and has 31 days):</p>{_may()}""",
        f"""{calc('long days: 10 × 6 = 60', 'short days: 21 × 4 = 84', f'60 + 84 = {boxed("144")}')}
{note('Both timetables fit exactly, with no spare minutes. That is a sign you have used the right stopover lengths.', 'check')}""",
    ],
    answer_text='144: 10 long days × 6 crossings + 21 short days × 4 crossings.',
    why={'A': '140 forgets the Bank Holidays: 8 × 6 + 23 × 4 = 48 + 92.',
         'C': '154 gives the long days 7 crossings, but 7 crossings need 7 × 50 + 6 × 20 = 470 minutes, more than the 400 available.',
         'D': '166 would need extra crossings on most days, e.g. 5 on weekdays, but 5 × 50 + 4 × 10 = 290 minutes is more than 230.',
         'E': '186 = 31 × 6: it uses the long timetable every day.'},
    fast='Long day 400 min = 6 crossings (6×50 + 5×20). Short day 230 = 4 (4×50 + 3×10). 10 long, 21 short: 60 + 84 = 144.',
))

# ---------------------------------------------------------------- 16 (Q32)
def _votes():
    parts, lab = [], []
    pos = {'Andrew': (100, 110), 'James': (330, 40), 'Roger': (330, 190)}
    for name, (x, y) in pos.items():
        parts.append(rect(x - 55, y - 20, 110, 40, k='ink', fill='paper', sw=2, rx=18))
        lab.append(text(x, y + 6, name, k='ink', size=18))
    parts += [arrow(158, 98, 270, 44, k='pen', bend=-0.12), arrow(158, 122, 270, 186, k='red', bend=0.12),
              arrow(320, 64, 320, 166, k='orange', bend=0.0), arrow(345, 166, 345, 64, k='green', bend=0.0)]
    lab += [text(200, 56, '3', k='pen', size=20, font='scrawl'), text(200, 172, '5', k='red', size=20, font='scrawl'),
            text(305, 120, '2', k='orange', size=20, font='scrawl'), text(362, 120, '1', k='green', size=20, font='scrawl'),
            text(430, 70, 'Andrew: −3 − 5 = −8', k='ink', size=18, anchor='start'),
            text(430, 116, 'James: +3 − 2 + 1 = +2', k='ink', size=18, anchor='start'),
            text(430, 162, 'Roger: +2 + 5 − 1 = +6', k='ink', size=18, anchor='start')]
    return svg(660, 230, rough(*parts) + ''.join(lab),
               'Arrows: 3 votes Andrew to James, 5 Andrew to Roger, 2 James to Roger, 1 Roger to James; net Andrew minus 8, James plus 2, Roger plus 6')

Q.append(dict(
    n=16, orig=32, answer='C', topic='Charts & change',
    question=f"""<p>In March, {hl('20 people', 'g', 1)} voted for the position of chair of a committee. There were three potential
candidates: Andrew, James and Roger.</p>
<p>In April, 11 of these people changed their votes, as follows:</p>
<p style="text-align:center">{hl('3 people changed their vote from Andrew to James', 'y', 2)}<br>
2 people changed their vote from James to Roger<br>
5 people changed their vote from Andrew to Roger<br>
1 person changed their vote from Roger to James</p>
<p class="stem">Which one of these bar charts {hl('could <b>not</b>', 'b', 3)} show the number of votes for the three candidates in
March and April?</p>
{fig(Y, 'ps_q16_charts', 'Five bar charts A to E, each showing March and April votes for Andrew, James and Roger', 560)}""",
    options={'A': 'chart A', 'B': 'chart B', 'C': 'chart C', 'D': 'chart D', 'E': 'chart E'},
    notes=[(1, 'g', 'Each month’s bars must add up to 20.'),
           (2, 'y', 'Turn the four moves into a <b>net change</b> for each person: that is all a chart can show.'),
           (3, 'b', 'Four charts fit the moves; find the one that can’t.')],
    steps=[
        f"""<p>Work out each candidate’s net change from March to April:</p>{_votes()}""",
        f"""<p>Now read each chart (March → April) and check the changes are −8, +2, +6:</p>
{calc(f'A: 10 → 2, 5 → 7, 5 → 11 {ar()} −8, +2, +6 {tick()}',
      f'B: 12 → 4, 7 → 9, 1 → 7 {ar()} −8, +2, +6 {tick()}',
      f'C: 9 → 1, 8 → 9, 3 → 10 {ar()} −8, <b>+1</b>, <b>+7</b> {cross()}',
      f'D: 12 → 4, 2 → 4, 6 → 12 {ar()} −8, +2, +6 {tick()}',
      f'E: 10 → 2, 8 → 10, 2 → 8 {ar()} −8, +2, +6 {tick()}')}
{calc(f'could not {ar()} {boxed("C")}')}
{note('Also check March has enough voters to move: Andrew needs at least 8, James 2, Roger 1. B (Roger 1) and D (James 2) just make it.', 'check')}""",
    ],
    answer_text='Chart C: James only goes up by 1 and Roger by 7, but the moves give James +2 and Roger +6.',
    why={'A': 'A fits: −8, +2, +6, and both months total 20.',
         'B': 'B fits: −8, +2, +6. Roger has only 1 vote in March, but only 1 person leaves Roger, so that works.',
         'D': 'D fits: −8, +2, +6. James has 2 in March, exactly enough for the 2 who leave him.',
         'E': 'E fits: −8, +2, +6.'},
    fast='Net change: Andrew −8, James +2, Roger +6. Check the James bars: C goes 8 → 9, only +1.',
))
