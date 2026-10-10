from wslib import *

Y = 2009
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _box():
    s, x0, y0 = 4, 30, 46
    W, c = 50 * s, 5 * s
    outline = [(x0 + c, y0), (x0 + W - c, y0), (x0 + W - c, y0 + c), (x0 + W, y0 + c), (x0 + W, y0 + W - c),
               (x0 + W - c, y0 + W - c), (x0 + W - c, y0 + W), (x0 + c, y0 + W), (x0 + c, y0 + W - c),
               (x0, y0 + W - c), (x0, y0 + c), (x0 + c, y0 + c)]
    parts = [rect(x0 + c, y0 + c, W - 2 * c, W - 2 * c, k='none', fill='b', sw=0),
             poly(outline, k='ink', sw=2.2)]
    for cx, cy in ((x0, y0), (x0 + W - c, y0), (x0, y0 + W - c), (x0 + W - c, y0 + W - c)):
        parts.append(rect(cx, cy, c, c, k='muted', fill='p', sw=1.2))
    for a, b, d, e in ((x0 + c, y0 + c, x0 + W - c, y0 + c), (x0 + c, y0 + W - c, x0 + W - c, y0 + W - c),
                       (x0 + c, y0 + c, x0 + c, y0 + W - c), (x0 + W - c, y0 + c, x0 + W - c, y0 + W - c)):
        parts.append(line(a, b, d, e, k='pen', w=1.8, dash=True))
    lab = [text(x0 + W / 2, y0 + W / 2 - 6, 'base', k='pen', size=20, font='scrawl'),
           text(x0 + W / 2, y0 + W / 2 + 18, '40 × 40', k='pen', size=18),
           text(x0 + W / 2, y0 + 15, 'flap 5', k='ink', size=14),
           text(x0 + W / 2, y0 - 12, 'card 50 cm wide', k='muted', size=15),
           text(x0 + c / 2, y0 - 12 + W + 34, 'cut-out corners', k='red', size=14, anchor='start'),
           text(x0 + W / 2, y0 + W + 54, 'dashed lines: fold up', k='pen', size=15)]
    # 3D box
    F0, F1 = (300, 250), (460, 250)
    h, dx, dy = 22, 64, -48
    F2, F3 = (F0[0], F0[1] - h), (F1[0], F1[1] - h)
    B2, B3 = (F2[0] + dx, F2[1] + dy), (F3[0] + dx, F3[1] + dy)
    B0, B1 = (B2[0], B2[1] + h), (B3[0], B3[1] + h)
    parts += [poly([F2, F3, B3, B2], k='ink', fill='paper', sw=2),
              poly([B2, B3, B1, B0], k='ink', fill='b', sw=1.6),
              poly([F2, B2, B0, (F0[0], F0[1])], k='ink', fill='b', sw=1.6),
              poly([F2, F3, F1, F0], k='ink', fill='o', sw=2.2),
              poly([F3, B3, B1, F1], k='ink', fill='o', sw=2.2),
              arrow(250, 150, 296, 200, k='red', bend=0.25)]
    lab += [text(380, 274, '40 cm', k='ink', size=17),
            text(500, 240, '40 cm', k='ink', size=17, anchor='start'),
            text(292, 246, '5 cm', k='red', size=17, anchor='end'),
            text(400, 140, 'open top', k='muted', size=16),
            text(250, 138, 'fold', k='red', size=18, font='scrawl'),
            text(420, 310, 'V = 40 × 40 × 5 = 8000 cm³', k='green', size=20, font='scrawl')]
    return svg(600, 330, rough(*parts) + ''.join(lab),
               'The 50 cm card with 5 cm corners cut out folds into an open box 40 cm by 40 cm by 5 cm deep')


Q.append(dict(
    n=1, orig=2, answer='C', topic='Nets & volume',
    question=f"""<p>A manufacturer wishes to make an {hl('open-topped box', 'y', 1)} out of the piece of cardboard shown
below by {hl('folding up its sides', 'y', 2)}.</p>
{fig(Y, 'ps_q01_card', 'A 50 cm by 50 cm square of card with a 5 cm by 5 cm square cut from each corner', 400)}
<p class="stem">What is the {hl('volume', 'b', 3)} of this box in cubic centimetres?</p>""",
    options={'A': '1 600', 'B': '2 400', 'C': '8 000', 'D': '10 125', 'E': '12 500'},
    notes=[(1, 'y', 'No lid: the card is just a base plus four walls.'),
           (2, 'y', 'The 5 cm flaps between the cut corners fold up to make the walls. So the box is <b>5 cm deep</b>.'),
           (3, 'b', 'Volume = length × width × height.')],
    steps=[
        f"""<p>The card is 50 cm across, but a 5 cm flap folds up on <b>each</b> side:</p>
{calc(f'50 − 5 − 5 = 40 cm {ar()} base is 40 cm × 40 cm', 'height = the flap = 5 cm')}""",
        f"""{_box()}""",
        f"""{calc('V = 40 × 40 × 5', f'= 1600 × 5 = {boxed("8000 cm³")}')}
{note('× 5 is the same as × 10 then halve: 1600 × 10 = 16 000, half is 8000.', 'tip')}""",
    ],
    answer_text='8000 cm³: a 40 cm × 40 cm base, 5 cm deep.',
    why={'A': '1600 is only the base area (40 × 40). It forgets to multiply by the 5 cm height.',
         'B': '2400 is the area of the card: 2500 − 4 corners of 25. That is an area, not a volume.',
         'D': '10 125 = 45 × 45 × 5: takes 5 cm off only one side. There is a flap on both sides.',
         'E': '12 500 = 50 × 50 × 5 uses the whole card as the base. The flaps fold up, so they are not part of the base.'},
    fast='Base 50 − 2 × 5 = 40 each way, height 5. 40 × 40 × 5 = 8000.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _tanks():
    states = [(5, 0, 'light comes on'), (15, 0, 'after $6'), (11, 0, 'after 50 km'), (11, 39, 'filled up')]
    parts, lab = [], []
    top, bot, per = 54, 204, 3
    for i, (old, new, cap) in enumerate(states):
        x = 40 + i * 150
        parts.append(rect(x, top, 64, bot - top, k='ink', fill='paper', sw=2.2))
        parts.append(rect(x + 3, bot - old * per, 58, old * per, k='none', fill='o', sw=0))
        if new:
            parts.append(rect(x + 3, bot - (old + new) * per, 58, new * per, k='none', fill='g', sw=0))
            lab.append(text(x + 32, bot - (old + new / 2) * per + 6, f'+{new} L', k='green', size=18, font='scrawl'))
        if i == 0:
            parts.append(line(x - 8, bot - 5 * per, x + 72, bot - 5 * per, k='red', w=1.6, dash=True))
        lab.append(text(x + 32, bot - old * per - 10 if not new else bot - old * per / 2 + 6, f'{old} L', k='ink', size=17))
        lab.append(text(x + 32, bot + 24, cap, k='ink', size=16))
    lab.append(text(40 + 32, top - 10, '50 L tank', k='muted', size=15))
    hops = [('+10 L', '$6 ÷ 60c'), ('−4 L', '50 km'), ('+39 L', 'at 50c')]
    for i, (a, b) in enumerate(hops):
        x1, x2 = 40 + i * 150 + 70, 40 + (i + 1) * 150 - 6
        parts.append(arrow(x1, 120, x2, 120, k='red', bend=-0.25))
        lab.append(text((x1 + x2) / 2, 90, a, k='red', size=18, font='scrawl'))
        lab.append(text((x1 + x2) / 2, 148, b, k='muted', size=14))
    lab.append(text(310, 262, 'orange = fuel already in the tank, green = new fuel at 50c', k='ink', size=15))
    return svg(620, 276, rough(*parts) + ''.join(lab),
               'Four tanks: 5 litres when the light comes on, 15 after $6, 11 after 50 km, then 39 litres added to fill it')


Q.append(dict(
    n=2, orig=6, answer='C', topic='Fuel & rates',
    question=f"""<p>The petrol tank of Jenny's car {hl('holds 50 litres', 'g', 1)} of petrol. A warning light comes on when
{hl('only 5 litres are left', 'g', 2)}. She always fills it as soon as she can after the warning light comes
on. {hl('The car travels 100km on 8 litres of petrol.', 'g', 3)} Last time she put petrol in, which she was
able to do {hl('immediately after the light came on', 'y', 4)}, she only had {hl('$6 with her so she spent it all on fuel at 60c per litre', 'g', 5)}. She then {hl('drove 50km', 'p', 6)} and saw a new garage offering petrol at {hl('50c per litre', 'g')} - an offer too good to miss. She {hl('filled the tank completely', 'b', 7)} and paid with her credit
card.</p>
<p class="stem">How much did it cost?</p>""",
    options={'A': '$ 15.50', 'B': '$ 17.50', 'C': '$ 19.50', 'D': '$ 22.50', 'E': '$ 24.50'},
    notes=[(1, 'g', 'Full tank = 50 litres.'),
           (2, 'g', 'Light on = 5 litres still in the tank.'),
           (3, 'g', '8 litres per 100 km, so 4 litres per 50 km.'),
           (4, 'y', 'So the tank still had exactly 5 litres when she bought the $6 of fuel.'),
           (5, 'g', '$6 = 600c. At 60c a litre that buys 10 litres.'),
           (6, 'p', 'The drive burns some fuel: take it off before filling up.'),
           (7, 'b', 'She pays 50c a litre for the empty space in the tank.')],
    steps=[
        f"""<p>Follow the litres in the tank:</p>
{calc('light on: 5 L', f'$6 ÷ 60c = 600 ÷ 60 = 10 L {ar()} 5 + 10 = 15 L',
      f'50 km uses half of 8 L = 4 L {ar()} 15 − 4 = 11 L')}""",
        f"""{_tanks()}""",
        f"""{calc('space to fill: 50 − 11 = 39 L', f'39 × 50c = 1950c = {boxed("$19.50")}')}
{note('× 50c is just halving: 39 ÷ 2 = 19.5, so $19.50.', 'tip')}""",
    ],
    answer_text='$19.50: 11 litres left in the tank, so 39 litres at 50c.',
    why={'A': '$15.50 buys 31 litres. That happens if you <b>add</b> the 4 litres used (5 + 10 + 4 = 19 in the tank).',
         'B': '$17.50 buys 35 litres: forgets the 4 litres burnt on the 50 km drive (tank at 15).',
         'D': '$22.50 buys 45 litres: fills up from the 5-litre warning level, ignoring both the $6 top-up and the drive.',
         'E': '$24.50 buys 49 litres: forgets the 10 litres bought with $6 (5 − 4 = 1 litre left).'},
    fast='5 + 10 − 4 = 11 litres in the tank. 50 − 11 = 39 litres at 50c = $19.50.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _halves():
    rows = [('France', 5.4, 3.0, 2.6), ('UK', 3.6, 1.5, 2.4), ('Germany', 4.5, 3.1, 1.6),
            ('Denmark', 4.3, 2.6, 1.7), ('Belgium', 3.3, 2.8, 2.3)]
    X = lambda v: 140 + v * 120
    parts, lab = [], []
    lab += [text(X(0), 26, '0', k='muted', size=14), text(X(1), 26, '1', k='muted', size=14),
            text(X(2), 26, '2', k='muted', size=14), text(X(3), 26, '3', k='muted', size=14),
            text(X(3.5) - 4, 26, '%', k='muted', size=14)]
    for i, (name, p1, p2, p3) in enumerate(rows):
        y = 58 + i * 50
        half = p1 / 2
        parts.append(rect(X(0), y - 9, X(half) - X(0), 18, k='none', fill='p', sw=0))
        parts.append(rect(X(half), y - 9, X(3.5) - X(half), 18, k='none', fill='g', sw=0))
        parts.append(line(X(half), y - 16, X(half), y + 16, k='red', w=2.6))
        lab.append(text(X(half), y + 32, f'½ × {p1} = {half:g}', k='red', size=14))
        for v, kk, f, tag, dy in ((p2, 'pen', 'b', '2', -14), (p3, 'violet', 'v', '3', -14)):
            parts.append(circle(X(v), y, 10, k=kk, fill=f, sw=2))
            lab.append(text(X(v), y + 5, tag, k=kk, size=14, font='print', weight='bold'))
        ok = p2 > half and p3 > half
        lab.append(text(130, y + 6, name, k='ink', size=17, anchor='end'))
        lab.append(text(X(3.5) + 14, y + 7, '✓' if ok else '✗', k='green' if ok else 'red', size=24, anchor='start'))
    lab.append(text(330, 316, 'circles: period 2 and period 3; they must both sit in the green part', k='ink', size=15))
    return svg(620, 330, rough(*parts) + ''.join(lab),
               'For each option country, a line with half of Period 1 marked in red; only Belgium has both later periods above it')


Q.append(dict(
    n=3, orig=7, answer='E', topic='Tables & percentages',
    question=f"""<p>The following table gives figures for the {hl('percentage growth per year', 'y', 1)} of labour productivity
per person per year in various countries during three periods.</p>
{table([['<i>Japan</i>', '8.5', '3.0', '3.2'], ['<i>France</i>', '5.4', '3.0', '2.6'], ['<i>United Kingdom</i>', '3.6', '1.5', '2.4'],
        ['<i>Belgium</i>', '3.3', '2.8', '2.3'], ['<i>Sweden</i>', '4.1', '1.5', '1.8'], ['<i>Denmark</i>', '4.3', '2.6', '1.7'],
        ['<i>Italy</i>', '6.3', '3.0', '1.6'], ['<i>Netherlands</i>', '4.8', '2.7', '1.6'], ['<i>Germany</i>', '4.5', '3.1', '1.6'],
        ['<i>United States</i>', '2.2', '0.0', '0.8']], head=['', '<i>Period 1</i>', '<i>Period 2</i>', '<i>Period 3</i>'])}
<p class="stem">Which country's percentage growth per year remained {hl('consistently greater than half of its Period 1 level', 'b', 2)} {hl('throughout the following periods', 'p', 3)}?</p>""",
    options={'A': 'France', 'B': 'United Kingdom', 'C': 'Germany', 'D': 'Denmark', 'E': 'Belgium'},
    notes=[(1, 'y', 'These are growth rates. Just compare the numbers along each row.'),
           (2, 'b', 'Halve the Period 1 number. The later numbers must be <b>bigger</b> than that.'),
           (3, 'p', 'Both Period 2 <b>and</b> Period 3. Lots of countries pass Period 2 and then fail Period 3.')],
    steps=[
        f"""<p>Only the five countries in the options matter. Halve Period 1, then test Periods 2 and 3:</p>
{calc(f'France: ½ of 5.4 = 2.7 {ar()} 3.0 ✓, 2.6 ✗',
      f'UK: ½ of 3.6 = 1.8 {ar()} 1.5 ✗',
      f'Germany: ½ of 4.5 = 2.25 {ar()} 3.1 ✓, 1.6 ✗',
      f'Denmark: ½ of 4.3 = 2.15 {ar()} 2.6 ✓, 1.7 ✗',
      f'Belgium: ½ of 3.3 = 1.65 {ar()} 2.8 ✓, 2.3 ✓')}""",
        f"""{_halves()}
{calc(f'only one country passes both {ar()} {boxed("Belgium")}')}
{note('No halving needed: double the later figure and compare it with Period 1. Belgium: 2.3 × 2 = 4.6, bigger than 3.3 ✓. France: 2.6 × 2 = 5.2, smaller than 5.4 ✗.', 'tip')}""",
    ],
    answer_text='Belgium: half of 3.3 is 1.65, and both 2.8 and 2.3 are above it.',
    why={'A': 'France fails in Period 3: 2.6 is just under half of 5.4 (2.7). Close, but not greater.',
         'B': 'The UK fails in Period 2: 1.5 is below 1.8. Its Period 3 figure (2.4) passes, but too late.',
         'C': 'Germany fails in Period 3: 1.6 is well below 2.25.',
         'D': 'Denmark fails in Period 3: 1.7 is below 2.15.'},
    fast='Double the later figures and compare with Period 1: only Belgium (5.6 and 4.6, both above 3.3) passes both.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _trap(p, q, s):
    (px, py), (qx, qy) = p, q
    dx, dy = qx - px, qy - py
    nx, ny = -dy / 4 * s, dx / 4 * s
    return [(px, py), (px + dx / 4 + nx, py + dy / 4 + ny), (qx - dx / 4 + nx, qy - dy / 4 + ny), (qx, qy)]


def _place(pts, ox, oy, u):
    return [(round(ox + x * u, 1), round(oy + y * u, 1)) for x, y in pts]


def _table_pieces():
    u, ox, oy = 34, 120, 70
    M = _place(_trap((0, 0), (4, 0), -1), ox, oy, u)
    L = _place(_trap((0, 0), (0, 4), 1), ox, oy, u)
    R = _place(_trap((4, 0), (4, 4), -1), ox, oy, u)
    parts = [poly(M, k='ink', fill='y', sw=2.2), poly(L, k='ink', fill='b', sw=2.2), poly(R, k='ink', fill='g', sw=2.2),
             circle(ox, oy, 6, k='red', fill='paper', sw=2.4), circle(ox + 4 * u, oy, 6, k='red', fill='paper', sw=2.4)]
    lab = [text(ox + 2 * u, oy - u - 8, 'short edge 2', k='ink', size=15),
           text(ox + 2 * u, oy + 22, 'long edge 4', k='ink', size=15),
           text(ox + 2 * u, oy - 12, 'middle', k='ink', size=16, font='scrawl'),
           text(ox - u / 2, oy + 2 * u + 6, 'side', k='ink', size=16, font='scrawl'),
           text(ox + 4.5 * u, oy + 2 * u + 6, 'side', k='ink', size=16, font='scrawl'),
           text(ox - 8, oy - 12, 'hinge', k='red', size=15, anchor='end'),
           text(ox + 4 * u + 8, oy - 12, 'hinge', k='red', size=15, anchor='start'),
           text(ox + 2 * u, oy + 4 * u + 30, 'all three pieces are the same shape', k='pen', size=17)]
    rx = 360
    lab += [text(rx, 70, 'The rules:', k='red', size=20, font='scrawl', anchor='start'),
            text(rx, 100, '• each hinge is at the end of a', k='ink', size=16, anchor='start'),
            text(rx, 120, '   LONG edge on both pieces', k='ink', size=16, anchor='start'),
            text(rx, 146, '• the hinges are the two ends', k='ink', size=16, anchor='start'),
            text(rx, 166, '   of the middle piece’s long edge', k='ink', size=16, anchor='start'),
            text(rx, 192, '• side pieces swing round,', k='ink', size=16, anchor='start'),
            text(rx, 212, '   but never come loose', k='ink', size=16, anchor='start')]
    return svg(640, 250, rough(*parts) + ''.join(lab),
               'The table drawn as three identical trapezium pieces: a middle piece with a side piece hinged at each end of its long edge')


def _hinge_options():
    u = 22
    r3 = 3 ** 0.5
    panels = [
        ('A', 20 + 0.866 * u, 30 + u, [(_trap((0, 0), (4, 0), -1), 'y'), (_trap((0, 0), (2, 2 * r3), 1), 'b'),
                                       (_trap((4, 0), (2, 2 * r3), -1), 'g')], [(0, 0), (4, 0)], [], True),
        ('B', 168, 30, [(_trap((0, 4), (4, 4), -1), 'y'), (_trap((4, 0), (4, 4), 1), 'b'),
                        (_trap((0, 4), (4, 4), 1), 'g')], [(4, 4), (0, 4)], [], True),
        ('C', 290, 36, [(_trap((0, 4), (4, 4), -1), 'y'), (_trap((0, 4), (0, 0), 1), 'b'),
                        (_trap((4, 4), (4, 0), -1), 'g')], [(0, 4), (4, 4)], [], True),
        ('D', 410, 50, [(_trap((0, 2), (4, 2), -1), 'y'), (_trap((0, 2), (4, 2), 1), 'g'),
                        (_trap((0, 0), (4, 0), 1), 'p')], [(0, 2), (4, 2)], [(0, 0), (4, 0)], False),
        ('E', 530, 36, [(_trap((0, 1), (4, 1), 1), 'y'), (_trap((0, 1), (4, 1), -1), 'b'),
                        (_trap((0, 1), (2 * 2 ** 0.5, 1 + 2 * 2 ** 0.5), 1), 'g')], [(4, 1), (0, 1)], [], True),
    ]
    parts, lab = [], []
    for name, ox, oy, pieces, hinges, bad, ok in panels:
        for pts, f in pieces:
            parts.append(poly(_place(pts, ox, oy, u), k='ink', fill=f, sw=2))
        for hx, hy in hinges:
            lab.append(circle(ox + hx * u, oy + hy * u, 5, k='red', fill='paper', sw=2.4))
        for bx, by in bad:
            X, Yy = ox + bx * u, oy + by * u
            parts += [line(X - 7, Yy - 7, X + 7, Yy + 7, k='red', w=3), line(X - 7, Yy + 7, X + 7, Yy - 7, k='red', w=3)]
        cx = ox + 2 * u
        lab.append(text(cx, 168, f'{name} {"✓" if ok else "✗"}', k='green' if ok else 'red', size=22, font='scrawl'))
    lab += [text(410 + 2 * u, 194, 'top piece: nothing', k='red', size=15),
            text(410 + 2 * u, 212, 'at its long-edge corners', k='red', size=15),
            text(150, 200, 'yellow = middle piece, red circles = hinges', k='ink', size=15)]
    return svg(650, 222, rough(*parts) + ''.join(lab),
               'Each option split into the three pieces with the hinges marked; in D the top piece cannot be attached')


Q.append(dict(
    n=4, orig=8, answer='D', topic='Shapes & hinges',
    question=f"""<p>The diagram below shows a rather unusual conference table which may take up a range
of configurations. {hl('The three pieces are hinged together at the points shown by the circles', 'y', 1)}:</p>
{fig(Y, 'ps_q04_table', 'The table: a trapezium-shaped top piece with a long thin piece hanging down from each end, joined by small circles', 230)}
<p class="stem">Which of the following shapes {hl('could <b>NOT</b> be made', 'b', 2)} from this table?</p>
{fig(Y, 'ps_q04_opts', 'Five shapes A to E made of trapezium pieces', 470)}""",
    options={'A': 'shape A', 'B': 'shape B', 'C': 'shape C', 'D': 'shape D', 'E': 'shape E'},
    notes=[(1, 'y', 'Two hinges, three pieces. The pieces can swing round but can’t come apart or slide along.'),
           (2, 'b', 'Odd one out: four of the shapes are possible.')],
    steps=[
        f"""<p>Look closely at the pieces. All three are the <b>same trapezium</b>: long edge 4, short edge 2, sloping ends.
The hinges sit at the two ends of the middle piece’s long edge, and each side piece is hinged at an end of <b>its</b> long edge.</p>
{_table_pieces()}""",
        f"""<p>So in every possible shape, one piece (the middle) has another piece attached at <b>each end of its long edge</b>.
Split each option into its three pieces and look for the two hinge points:</p>
{_hinge_options()}""",
        f"""{calc(f'A: the long edges make a triangle; hinges at the top corners {tick()}',
      f'B: one side piece stands up at the right hinge; the other lies against the long edge {tick()}',
      f'C: both side pieces swung right round to rest on the sloping ends {tick()}',
      f'E: one piece folds against the long edge, the other swings off at 45° {tick()}',
      f'D: the top piece only touches the others along its <b>short</b> edge {cross()}')}
<p>In D, nothing meets the ends of the top piece’s long edge, so it has nowhere to be hinged {ar()} {boxed('D')}</p>""",
    ],
    answer_text='Shape D: its top piece touches the rest only along its short edge, so it cannot be hinged on.',
    why={'A': 'Possible: both side pieces swing inwards until their long edges and the middle’s long edge make a triangle.',
         'B': 'Possible: the right-hand piece points straight up from its hinge, and the left-hand piece swings round under the middle piece’s long edge.',
         'C': 'Possible: it is the original table turned upside down, with both side pieces swung round onto the middle piece’s sloping ends.',
         'E': 'Possible: one side piece folds flat against the middle’s long edge; the other hangs from the opposite hinge at 45°.'},
    fast='In every real shape, two pieces meet the two ends of one piece’s long edge. D’s top piece only touches along its short edge, so it can’t be attached.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _hill():
    parts = [path('M20 236 L120 236 L420 92 L520 92 L620 236 Z', k='green', fill='g', sw=2),
             line(20, 236, 620, 236, k='ink', w=2),
             poly([(54, 236), (54, 206), (74, 188), (94, 206), (94, 236)], k='ink', fill='paper', sw=2),
             rect(66, 216, 14, 20, k='ink', fill='o', sw=1.4),
             rect(432, 52, 70, 40, k='ink', fill='paper', sw=2),
             poly([(426, 54), (467, 30), (508, 54)], k='ink', fill='p', sw=2),
             arrow(112, 200, 402, 62, k='red', bend=-0.04),
             arrow(434, 121, 215, 226, k='pen', bend=0.03)]
    lab = [text(74, 256, 'home', k='ink', size=16),
           text(467, 78, 'PO', k='ink', size=20, font='print', weight='bold'),
           text(196, 108, 'up: 2 km/h', k='red', size=20, font='scrawl'),
           text(196, 130, '½ hour per km', k='red', size=16),
           text(410, 182, 'down: 4 km/h', k='pen', size=20, font='scrawl'),
           text(410, 204, '¼ hour per km', k='pen', size=16)]
    X = lambda h: 60 + h * 110
    parts += [rect(X(0), 300, X(3) - X(0), 30, k='ink', fill='p', sw=1.8),
              rect(X(3), 300, X(4.5) - X(3), 30, k='ink', fill='b', sw=1.8)]
    lab += [text((X(0) + X(3)) / 2, 321, 'up 6 km: 3 h', k='ink', size=16),
            text((X(3) + X(4.5)) / 2, 321, 'down: 1½ h', k='ink', size=16),
            text(X(4.5) + 10, 322, '= 4½ h ✓', k='green', size=20, font='scrawl', anchor='start'),
            text(60, 290, 'test 6 km:', k='muted', size=15, anchor='start')]
    return svg(640, 344, rough(*parts) + ''.join(lab),
               'A steep hill from home to the post office: up at 2 km per hour, down at 4 km per hour; 6 km takes 3 hours up and 1.5 hours down')


Q.append(dict(
    n=5, orig=12, answer='B', topic='Speed, distance & time',
    question=f"""<p>Ionnais lives at the bottom of a very steep hill. Worse than that, the post office is at the
top. Every Thursday he must go there to collect his pension. He can only walk at {hl('2 km per hour uphill', 'g', 1)} but manages {hl('4 km per hour downhill', 'g', 2)}. The {hl('round trip', 'y', 3)}, excluding the wait at
the post office, takes him {hl('4½ hours', 'g', 4)}.</p>
<p class="stem">How far is it {hl('from his house to the post office', 'b', 5)}?</p>""",
    options={'A': '3.00 km', 'B': '6.00 km', 'C': '6.75 km', 'D': '12.00 km', 'E': '13.50 km'},
    notes=[(1, 'g', 'Slow going up: each km takes half an hour.'),
           (2, 'g', 'Twice as fast coming down: each km takes a quarter of an hour.'),
           (3, 'y', 'Up AND back down: the same distance twice, at two different speeds.'),
           (4, 'g', 'Total walking time for both legs.'),
           (5, 'b', 'One way only, not the round trip.')],
    steps=[
        f"""<p>Work out the time for <b>each km</b> of the trip:</p>
{calc('up: 1 km ÷ 2 km/h = ½ hour', 'down: 1 km ÷ 4 km/h = ¼ hour', f'1 km there and back = ½ + ¼ = <b>¾ hour</b>')}""",
        f"""{calc(f'4½ hours ÷ ¾ hour = 6 {ar()} distance = {boxed("6 km")}')}
{_hill()}""",
        f"""{note('Don’t average the speeds! (2 + 4) ÷ 2 = 3 km/h is wrong, because he spends twice as long on the slow leg. That trap gives 3 × 4½ = 13.5 km for the round trip, or 6.75 km each way.', 'trap')}""",
    ],
    answer_text='6 km: 3 hours up plus 1½ hours down = 4½ hours.',
    why={'A': '3 km would take only 1½ + ¾ = 2¼ hours, half the time given.',
         'C': '6.75 km comes from averaging the speeds to 3 km/h. He spends longer going slowly, so his real average is lower.',
         'D': '12 km is the whole round trip (6 + 6), not the distance to the post office.',
         'E': '13.5 km = 3 km/h × 4½ h: the averaged-speed trap, and it is a round trip too.'},
    fast='Each km costs ½ h up + ¼ h down = ¾ h. 4½ ÷ ¾ = 6 km. (Check: 3 h + 1½ h = 4½ h.)',
))


# ---------------------------------------------------------------- 6 (Q13)
def _bills():
    rows = [('Activering', 50), ('Bellaphone', 45), ('Canconnect', 55), ('Dialfast', 50), ('Engaged', 50)]
    X = lambda v: 150 + v * 6.5
    parts, lab = [], []
    for i, (name, v) in enumerate(rows):
        y = 30 + i * 38
        best = v == 45
        parts.append(rect(X(0), y, X(v) - X(0), 26, k='ink', fill='g' if best else 'b', sw=1.6))
        lab.append(text(140, y + 19, name, k='ink', size=17, anchor='end'))
        lab.append(text(X(v) + 8, y + 19, f'£{v}', k='green' if best else 'ink', size=18, anchor='start'))
    lab.append(text(X(45) + 60, 30 + 38 + 19, '← cheapest', k='green', size=20, font='scrawl', anchor='start'))
    return svg(620, 228, rough(*parts) + ''.join(lab),
               'Best monthly bill for each company: Activering 50, Bellaphone 45, Canconnect 55, Dialfast 50, Engaged 50')


Q.append(dict(
    n=6, orig=13, answer='B', topic='Tables & best deal',
    question=f"""<p>Telephone network operators offer customers a choice of tariffs, with the tariff broken into
two parts: (a) {hl('a fixed monthly rental charge regardless of use', 'y', 1)}, and (b) {hl('a charge per minute of call time used', 'y', 2)}. The table below shows the tariffs offered by five companies; all
figures are given in £. I am considering taking a contract with one of these and estimate
that I will use {hl('100 minutes of call-time each month', 'g', 3)}.</p>
{table([['<i>Activering</i>', '50', '0.05', '20', '0.30', '0', '0.60'],
        ['<i>Bellaphone</i>', '55', '0.05', '20', '0.25', '0', '0.60'],
        ['<i>Canconnect</i>', '60', '0.05', '20', '0.35', '0', '0.55'],
        ['<i>Dialfast</i>', '65', '0.05', '10', '0.45', '5', '0.45'],
        ['<i>Engaged</i>', '70', '0.05', '10', '0.40', '0', '0.70']],
       head=['', '<i>High user</i><br>Rental', '<i>High user</i><br>Call charge', '<i>Medium user</i><br>Rental',
             '<i>Medium user</i><br>Call charge', '<i>Low user</i><br>Rental', '<i>Low user</i><br>Call charge'])}
<p class="stem">Which company should I use to receive the {hl('lowest telephone bill', 'b', 4)}?</p>""",
    options={'A': 'Activering', 'B': 'Bellaphone', 'C': 'Canconnect', 'D': 'Dialfast', 'E': 'Engaged'},
    notes=[(1, 'y', 'Paid every month whatever you use.'),
           (2, 'y', 'Call charge × minutes used.'),
           (3, 'g', '× 100 just moves the decimal point two places: 0.30 → £30.'),
           (4, 'b', 'Each company has three tariffs: you would take its cheapest. Then compare the companies.')],
    steps=[
        f"""<p>Monthly bill = rental + 100 × call charge. Work out all 15:</p>
{table([['Activering', '50 + 5 = 55', '20 + 30 = <b>50</b>', '0 + 60 = 60', '£50'],
        ['Bellaphone', '55 + 5 = 60', f'20 + 25 = <b>45</b>', '0 + 60 = 60', boxed('£45')],
        ['Canconnect', '60 + 5 = 65', '20 + 35 = <b>55</b>', '0 + 55 = <b>55</b>', '£55'],
        ['Dialfast', '65 + 5 = 70', '10 + 45 = 55', '5 + 45 = <b>50</b>', '£50'],
        ['Engaged', '70 + 5 = 75', '10 + 40 = <b>50</b>', '0 + 70 = 70', '£50']],
       head=['', 'High', 'Medium', 'Low', 'Best'])}""",
        f"""{_bills()}
{calc(f'lowest bill = £45 {ar()} {boxed("Bellaphone")}')}
{note('Every high-user tariff is rental + £5, so the cheapest is 50 + 5 = £55. That already loses to £45, so you only really need the medium and low columns.', 'tip')}""",
    ],
    answer_text='Bellaphone: its medium-user tariff costs £20 + £25 = £45 a month.',
    why={'A': 'Activering’s best is £50 (medium). It also has the cheapest high-user tariff, which tempts you if you only read the first columns.',
         'C': 'Canconnect’s best is £55 (medium or low). It has the cheapest low call rate of the £0-rental tariffs, but that isn’t enough.',
         'D': 'Dialfast’s best is £50 (low: 5 + 45), the best low-user deal, but still £5 more than Bellaphone.',
         'E': 'Engaged’s best is £50 (medium: 10 + 40).'},
    fast='Bill = rental + call charge × 100. Medium column: 50, 45, 55, 55, 50. High is never under £55 and low never under £50. Bellaphone.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _chickens():
    L, S, x0 = 80, 40, 150
    rows = [('fact 1', 'LSS', '100'), ('fact 2', 'LLSSS', '175'), ('fact 1 × 2', 'LLSSSS', '200')]
    parts, lab = [], []
    for i, (name, seq, tot) in enumerate(rows):
        y = 34 + i * 64
        x = x0
        for j, ch in enumerate(seq):
            w = L if ch == 'L' else S
            extra = i == 2 and j == len(seq) - 1
            parts.append(rect(x, y, w - 4, 38, k='red' if extra else 'ink', fill='p' if extra else ('o' if ch == 'L' else 'y'), sw=2 if extra else 1.6))
            lab.append(text(x + (w - 4) / 2, y + 26, 'large' if ch == 'L' else 'S', k='ink', size=15 if ch == 'L' else 17))
            x += w
        lab.append(text(x0 - 12, y + 25, name, k='ink', size=17, anchor='end'))
        lab.append(text(x + 10, y + 26, f'= {tot}', k='ink', size=20, anchor='start'))
    xe = x0 + 2 * L + 3 * S
    parts.append(brace(xe, xe + S - 4, 34 + 2 * 64 + 44, '', k='red'))
    lab.append(text(xe + 18, 34 + 2 * 64 + 84, 'the extra small chicken = 200 − 175 = 25', k='red', size=17))
    return svg(620, 270, rough(*parts) + ''.join(lab),
               'Bar model: one large plus two small is 100; two large plus three small is 175; doubling the first gives 200, so one small chicken eats 25')


Q.append(dict(
    n=7, orig=14, answer='E', topic='Two facts, two unknowns',
    question=f"""<p>{hl('100 pellets of chicken food will feed one large and two small chickens for a day.', 'g', 1)}</p>
<p>{hl('175 pellets of food will feed two large and three small chickens for a day.', 'g', 2)}</p>
<p class="stem">Which of the following statements is {hl('<b>not</b> true', 'b', 3)}?</p>""",
    options={'A': 'A small chicken can be fed for longer than a day with 30 pellets of food.',
             'B': '70 pellets of food are sufficient to feed a large chicken for a day.',
             'C': 'A large chicken needs twice as many pellets as a small chicken.',
             'D': 'Two large and four small chickens will need 200 pellets of food for a day.',
             'E': 'Three large and ten small chickens will need 450 pellets of food for a day.'},
    notes=[(1, 'g', '1 large + 2 small = 100.'),
           (2, 'g', '2 large + 3 small = 175.'),
           (3, 'b', 'Four statements are true. Work out each chicken’s daily amount, then find the false one.')],
    steps=[
        f"""<p>Double fact 1 so both facts have <b>2 large</b> chickens. Then compare:</p>
{calc(f'1 large + 2 small = 100 {ar()} 2 large + 4 small = 200', '2 large + 3 small = 175',
      f'difference: 1 small = 200 − 175 = <b>25</b>', f'1 large = 100 − 2 × 25 = <b>50</b>')}
{_chickens()}""",
        f"""<p>Now test each statement with large = 50, small = 25:</p>
{calc(f'A: 30 is more than 25 {tick()} true', f'B: 70 is more than 50 {tick()} true', f'C: 50 = 2 × 25 {tick()} true',
      f'D: 2 × 50 + 4 × 25 = 100 + 100 = 200 {tick()} true',
      f'E: 3 × 50 + 10 × 25 = 150 + 250 = <b>400</b>, not 450 {cross()}')}
{calc(f'the false one {ar()} {boxed("E")}')}""",
    ],
    answer_text='E: three large and ten small chickens need 400 pellets, not 450.',
    why={'A': 'True: a small chicken eats 25 a day, so 30 pellets last a bit longer than a day.',
         'B': 'True: a large chicken eats 50, and 70 is more than enough.',
         'C': 'True: 50 is exactly twice 25.',
         'D': 'True: it is just fact 1 doubled (2 × 100 = 200).'},
    fast='Double fact 1: 2L + 4S = 200. Take away fact 2 (175): S = 25, so L = 50. E gives 150 + 250 = 400, not 450.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _sweets():
    X = lambda c: 50 + c * 5.4
    parts, lab = [], []
    bars = [('fewest gum: 5 pieces', [(50, 'b', 'gobstoppers ≥ 50c'), (27, 'o', 'chews ≥ 27c'), (10, 'g', 'gum 10c'),
                                      (13, 'paper', 'rest 13c')]),
            ('most gum: 11 pieces', [(50, 'b', '10 gobstoppers 50c'), (27, 'o', '9 chews 27c'), (22, 'g', '11 gum 22c'),
                                     (1, 'paper', '')])]
    for i, (title, segs) in enumerate(bars):
        y = 46 + i * 96
        lab.append(text(50, y - 12, title, k='red', size=20, font='scrawl', anchor='start'))
        c = 0
        for amt, f, name in segs:
            parts.append(rect(X(c), y, X(c + amt) - X(c), 44, k='ink', fill=f, sw=1.6))
            if name:
                lab.append(text((X(c) + X(c + amt)) / 2, y + 28, name, k='ink', size=16 if amt > 15 else 15))
            c += amt
    parts.append(brace(X(0), X(100), 46 + 96 + 52, '', k='muted'))
    lab += [text(X(100) + 6, 46 + 96 + 28, '1c', k='muted', size=15, anchor='start'),
            text(X(50), 46 + 96 + 92, '100c altogether', k='muted', size=16)]
    return svg(620, 250, rough(*parts) + ''.join(lab),
               'Two 100 cent bars: the fewest gum is 5 pieces for 10 cents; the most is 11 pieces after 50 cents of gobstoppers and 27 cents of chews')


Q.append(dict(
    n=8, orig=18, answer='B', topic='Money & ranges',
    question=f"""<p>A boy is given $1.00 by his grandparents to buy sweets. He decides to spend {hl('at least half', 'y', 1)} his money on gobstoppers at 5c each, {hl('at least a quarter', 'p', 2)} of his money on fruit chews
at {hl('3c each', 'p')} and {hl('at least one tenth', 'y', 3)} of his money on pieces of bubble gum at 2c each. He
will decide how to spend the rest of the money when he gets to the shop.</p>
<p class="stem">What is the {hl('possible range of number of pieces of bubble gum', 'b', 4)} he can buy?</p>""",
    options={'A': 'From 5 to 9', 'B': 'From 5 to 11', 'C': 'From 5 to 13', 'D': 'From 6 to 12', 'E': 'From 10 to 22'},
    notes=[(1, 'y', 'At least 50c on gobstoppers: 10 of them at 5c is exactly 50c.'),
           (2, 'p', 'At least 25c on chews, but chews cost 3c. 8 chews = 24c is <b>not</b> enough: he needs 9 (27c).'),
           (3, 'y', 'At least 10c on gum: at least 5 pieces.'),
           (4, 'b', 'Smallest and largest number of gum pieces (pieces, not cents!).')],
    steps=[
        f"""<p><b>Fewest</b> gum: one tenth of 100c is 10c.</p>
{calc(f'10c ÷ 2c = <b>5 pieces</b>')}""",
        f"""<p><b>Most</b> gum: spend as little as allowed on the other two sweets.</p>
{calc('gobstoppers: 50c (10 × 5c, exactly half)', f'chews: need 25c, but 8 × 3c = 24c is too little {ar()} 9 chews = 27c',
      '100 − 50 − 27 = 23c left', f'23c ÷ 2c = 11 pieces (22c), with 1c spare')}""",
        f"""{_sweets()}
{calc(f'range {ar()} {boxed("from 5 to 11")}')}
{note('The quarter is the trap: 25 isn’t a multiple of 3, so the least he can spend on chews is 27c. Using 25c gives 25c for gum and 12 pieces.', 'trap')}""",
    ],
    answer_text='From 5 to 11 pieces of bubble gum.',
    why={'A': '9 comes from spending more than half on gobstoppers (55c), leaving only 18c. Exactly half (50c) is allowed.',
         'C': '13 pieces cost 26c, which leaves only 24c for chews: less than a quarter.',
         'D': '12 comes from spending exactly 25c on chews, which is impossible at 3c each. And 5 pieces already make one tenth, so the minimum is 5, not 6.',
         'E': '10 to 22 are amounts of money in cents (10c to 22c), not numbers of pieces.'},
    fast='Min: 10c ÷ 2 = 5. Max: 100 − 50 − 27 (nine 3c chews) = 23c, so 11 pieces.',
))
