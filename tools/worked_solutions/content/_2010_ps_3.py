from wslib import *

Y = 2010
Q = []

# ---------------------------------------------------------------- 18 (Q37)
def _sheets():
    parts, lab = [], []
    # basic info sheet: front and back
    parts += [rect(56, 46, 70, 96, k='ink', fill='paper', sw=1.8), rect(40, 58, 70, 96, k='ink', fill='b', sw=1.8)]
    lab += [text(75, 110, 'front', k='ink', size=14), text(116, 60, 'back', k='muted', size=12, rotate=90)]
    # price / booking sheet, both sides, cut in two
    for x, word, f in ((196, 'prices', 'y'), (276, 'booking', 'o')):
        parts += [rect(x, 52, 70, 96, k='ink', fill=f, sw=1.8), line(x - 4, 100, x + 74, 100, k='red', w=2, dash=True)]
        lab += [text(x + 35, 81, word, k='ink', size=13), text(x + 35, 129, word, k='ink', size=13)]
    lab += [text(231, 166, 'side 1', k='muted', size=13), text(311, 166, 'side 2', k='muted', size=13)]
    # amenities
    parts.append(rect(392, 52, 70, 96, k='ink', fill='g', sw=1.8))
    lab.append(text(427, 105, 'local info', k='ink', size=13))
    # brochure
    parts += [rect(520, 52, 70, 96, k='ink', fill='paper', sw=1.8), line(520, 52, 590, 148, k='red', w=2.4), line(590, 52, 520, 148, k='red', w=2.4)]
    lab += [text(83, 30, 'basic info', k='ink', size=17, font='scrawl'), text(271, 30, 'prices + booking form', k='ink', size=17, font='scrawl'),
            text(427, 30, 'amenities', k='ink', size=17, font='scrawl'), text(555, 30, 'brochure', k='ink', size=17, font='scrawl'),
            text(83, 194, '2 sides', k='pen', size=18), text(271, 194, '2 sides ÷ 2 packs = 1', k='pen', size=18),
            text(427, 194, '1 side', k='pen', size=18), text(555, 194, 'free: 0', k='pen', size=18),
            text(320, 234, '2 + 1 + 1 + 0 = 4 sides a pack × 2p = 8p', k='red', size=20, font='scrawl')]
    return svg(640, 248, rough(*parts) + ''.join(lab),
               'The four sheets in a pack: basic info 2 sides, prices and booking sheet shared by two packs so 1 side each, amenities 1 side, brochure free')

Q.append(dict(
    n=18, orig=37, answer='B', topic='Counting & costs',
    question=f"""<p>Maggie is preparing {hl('300 information packs', 'g', 1)} so that she can respond to enquiries for her
holiday cottages. Each pack contains:</p>
<ul><li>A basic information sheet - this is printed on A4 sized paper {hl('on both sides', 'y', 2)}
so that it may be {hl('folded to form 4 pages', 'p', 3)}.</li>
<li>A sheet with prices on one side and a booking form on the other - {hl('two of these are printed on a sheet of A4 paper which is then cut in two', 'p', 4)}.</li>
<li>An A4 information sheet giving details of some local amenities - this is
{hl('printed on one side only', 'y', 5)}.</li>
<li>A single A4 sheet colour brochure printed on both sides - this is {hl('provided free', 'p', 6)} by the local Angling Association.</li></ul>
<p>The local printer charges {hl('2p per side of A4', 'g', 7)} for reproduction.</p>
<p class="stem">How much will her 300 packs cost her?</p>""",
    options={'A': '£15', 'B': '£24', 'C': '£30', 'D': '£36', 'E': '£42'},
    notes=[(1, 'g', 'Work out one pack, then × 300.'),
           (2, 'y', 'Two printed sides.'),
           (3, 'p', 'Folding doesn’t print anything new: 4 pages, but still only 2 sides of A4.'),
           (4, 'p', 'One A4 sheet (2 sides) makes the sheets for <b>two</b> packs.'),
           (5, 'y', 'One side.'),
           (6, 'p', 'Free: costs her nothing.'),
           (7, 'g', 'Price per printed side of A4.')],
    steps=[
        f"""<p>Count the printed sides of A4 that <b>one pack</b> uses:</p>{_sheets()}""",
        f"""{calc('4 sides × 2p = 8p a pack', f'300 × 8p = 2400p = {boxed("£24")}')}
{note('Price per side, so count sides of A4 actually printed, not pages after folding.', 'trap')}""",
    ],
    answer_text='£24: 4 printed sides per pack at 2p, for 300 packs.',
    why={'A': '£15 means only 2½ sides a pack. The basic sheet (2) and the amenities sheet (1) already make 3.',
         'C': '£30 is 5 sides a pack: pays for both sides of the price/booking sheet for every pack, but one A4 sheet serves two packs.',
         'D': '£36 is 6 sides: counts the folded sheet as 4 sides (it’s 4 pages, but only 2 printed sides), or pays for the free brochure.',
         'E': '£42 is 7 sides: makes both mistakes, 4 for the folded sheet and 2 for the price/booking sheet.'},
    fast='Sides per pack: 2 + 1 + 1 + 0 = 4, so 8p. 300 × 8p = £24.',
))

# ---------------------------------------------------------------- 19 (Q38)
def _moon(cx, cy, d, r=17, k='ink'):
    R = r * 1.4
    if d == 'right':
        dd = f'M{cx - 5} {cy - r} A{r} {r} 0 0 1 {cx - 5} {cy + r} A{R} {R} 0 0 0 {cx - 5} {cy - r} Z'
    elif d == 'left':
        dd = f'M{cx + 5} {cy - r} A{r} {r} 0 0 0 {cx + 5} {cy + r} A{R} {R} 0 0 1 {cx + 5} {cy - r} Z'
    elif d == 'up':
        dd = f'M{cx - r} {cy + 5} A{r} {r} 0 0 1 {cx + r} {cy + 5} A{R} {R} 0 0 0 {cx - r} {cy + 5} Z'
    else:
        dd = f'M{cx - r} {cy - 5} A{r} {r} 0 0 0 {cx + r} {cy - 5} A{R} {R} 0 0 1 {cx - r} {cy - 5} Z'
    return path(dd, k=k, fill='y', sw=2.2)


def _blockarrow(cx, cy, L, down=True, k='ink'):
    pts = [(-4, -L / 2), (4, -L / 2), (4, L / 2 - 13), (11, L / 2 - 13), (0, L / 2), (-11, L / 2 - 13), (-4, L / 2 - 13)]
    s = 1 if down else -1
    return poly([(cx + x, cy + s * y) for x, y in pts], k=k, fill='paper', sw=2)


def _cube(x, y, s=100, d=40):
    return [rect(x, y, s, s, k='ink', fill='paper', sw=2.2),
            poly([(x, y), (x + d, y - d), (x + s + d, y - d), (x + s, y)], k='ink', fill='paper', sw=2.2),
            poly([(x + s, y), (x + s + d, y - d), (x + s + d, y + s - d), (x + s, y + s)], k='ink', fill='paper', sw=2.2)]


def _dice_net():
    parts, lab = [], []
    c, x0, y0 = 76, 30, 22
    cells = {'back': (1, 0), 'left': (0, 1), 'top': (1, 1), 'right': (2, 1), 'front': (1, 2), 'bottom': (1, 3)}
    ctr = {}
    for name, (i, j) in cells.items():
        parts.append(rect(x0 + i * c, y0 + j * c, c, c, k='ink', fill='paper', sw=2))
        ctr[name] = (x0 + i * c + c / 2, y0 + j * c + c / 2)
    cx, cy = ctr['top']
    parts += [line(cx - 24, cy - 20, cx + 24, cy + 20, k='ink', w=3), line(cx - 24, cy + 20, cx + 24, cy - 20, k='ink', w=3)]
    parts.append(line(ctr['back'][0], ctr['back'][1] - 20, ctr['back'][0], ctr['back'][1] + 20, k='ink', w=3))
    parts.append(circle(*ctr['right'], 22, k='ink', sw=2.4))
    parts.append(_blockarrow(*ctr['front'], 50, down=True))
    bx, by = ctr['bottom']
    parts += [line(bx - 24, by - 9, bx + 24, by - 9, k='ink', w=3), line(bx - 24, by + 9, bx + 24, by + 9, k='ink', w=3)]
    parts.append(_moon(*ctr['left'], 'right'))
    lab += [text(144, 364, 'the die opened out', k='ink', size=16, font='scrawl'),
            text(144, 386, '(X on top)', k='muted', size=14)]
    # cubes: E as drawn and as it should be
    for x, d, title, verdict, col in ((300, 'left', 'E as drawn', 'round side left ✗', 'red'),
                                      (480, 'up', 'what it should be', 'round side up to X ✓', 'green')):
        parts += _cube(x, 120)
        tx, ty = x + 70, 100
        parts += [line(tx - 34, ty - 7, tx + 34, ty + 7, k='ink', w=2.6), line(tx - 34, ty + 7, tx + 34, ty - 7, k='ink', w=2.6)]
        parts.append(_moon(x + 50, 172, d, k='red' if col == 'red' else 'green'))
        parts.append(_blockarrow(x + 120, 150, 46, down=True))
        lab += [text(x + 70, 52, title, k='ink', size=17, font='scrawl'), text(x + 62, 248, verdict, k=col, size=16)]
    lab += [text(470, 300, 'rules from the three views:', k='ink', size=16),
            text(470, 326, 'the arrow points away from X', k='pen', size=16),
            text(470, 352, 'the moon’s round side faces X', k='red', size=16),
            text(470, 378, 'X and = are opposite', k='pen', size=16)]
    return svg(660, 396, rough(*parts) + ''.join(lab),
               'Net of the die with X on top: slash behind, moon on the left with its round side towards X, circle on the right, arrow in front pointing away from X, equals sign underneath. Beside it, die E as drawn with the moon facing left, and as it should be with the moon facing up to the X')

Q.append(dict(
    n=19, orig=38, answer='E', topic='Dice & 3D views',
    question=f"""<p>{hl('Three views of the same die', 'y', 1)} with unusual symbols are shown below:</p>
{fig(Y, 'ps_q19_views', 'View 1: X on top, arrow pointing down on the front, circle on the right. View 2: slash on top, equals sign on the front, crescent moon on the right. View 3: equals sign on top seen as two slashes, circle on the front, arrow pointing up on the right', 420)}
<p class="stem">Which one of the following dice is {hl('<b>not</b>', 'b', 2)} identical to the die above?</p>
{fig(Y, 'ps_q19_options', 'Five dice A to E. A: equals on top, arrow up on front, moon on right. B: slash on top, X on front, circle on right. C: circle on top, two vertical lines on front, slash on right. D: moon on top, X on front, slash on right. E: X on top, moon facing left on front, arrow down on right', 420)}""",
    options={'A': 'die A', 'B': 'die B', 'C': 'die C', 'D': 'die D', 'E': 'die E'},
    notes=[(1, 'y', 'Six symbols: X, arrow, circle, slash, equals, moon. Check which touch and which way they point.'),
           (2, 'b', 'Four dice are the same die turned round. Find the odd one out.')],
    steps=[
        f"""<p><b>Opposite faces.</b> Views 1 and 3 both show the arrow and the circle. The third face is X in one and = in the other,
so X and = are on opposite sides (both sit against the same arrow-circle edge).</p>
<p>Views 1 and 2 share no symbols at all, so every face in view 1 is opposite a face in view 2: arrow and circle are opposite the slash and the moon.</p>
{note('Quick scan: none of A to E shows X with =, or two other opposite faces together. So the odd one out must have a symbol pointing the wrong way.', 'tip')}""",
        f"""<p><b>Directions.</b> Read them off the views:</p>
<ul><li>Arrow: view 1 has X on top and the arrow points <b>down</b>; view 3 has = on top and the arrow points <b>up</b>. So the arrow always points away from X (towards =).</li>
<li>Moon: in view 2 the = is in front and the moon’s round side points to the <b>back</b>, which is the face opposite =, i.e. X. So the moon’s round side always faces X.</li></ul>
{_dice_net()}""",
        f"""<p><b>Check E.</b> X is on top, the moon is on the front. Its round side should point <b>up</b> at the X. E draws it pointing left {cross()}
(E’s arrow is fine: it points down, away from X.) {ar()} {boxed('E')}</p>
{calc('A: = on top, X underneath: arrow up ' + tick() + ' moon round side down ' + tick(),
      'D: X in front: moon on top with its round side towards the front ' + tick(),
      'B, C: only circle, X, slash and = : all fit ' + tick())}""",
    ],
    answer_text='Die E: its moon is turned a quarter turn the wrong way (round side should face the X on top).',
    why={'A': 'A has = on top, so X is underneath. The arrow points up (away from X) and the moon’s round side points down (towards X). Correct.',
         'B': 'B shows slash, X and circle: three faces that do meet at a corner, with the slash running towards the X as in view 2.',
         'C': 'C shows circle, = and slash, which meet at a corner; the = lines run towards the circle, as in view 3.',
         'D': 'D has X in front and the moon on top with its round side towards the front, i.e. towards X. Correct.'},
    fast='Rules: arrow points away from X; moon’s round side faces X. In E the X is on top but the moon faces left: E.',
))

# ---------------------------------------------------------------- 20 (Q42)
def _coffee():
    parts, lab = [], []
    specs = ((2, 'coffee', 'regular, decaf'), (4, 'milk', 'black, full, semi, skimmed'), (5, 'sweetening', 'none, 1 or 2 sugar, 1 or 2 tablets'))
    for i, (n, name, sub) in enumerate(specs):
        x = 80 + i * 170
        parts.append(rect(x - 46, 34, 92, 86, k='ink', fill='paper', sw=2, rx=14))
        lab += [text(x, 98, n, k='pen', size=46, font='scrawl'), text(x, 24, name, k='ink', size=17, font='scrawl'),
                text(x, 146, sub, k='muted', size=13)]
        if i < 2:
            lab.append(text(x + 85, 88, '×', k='red', size=30))
    lab.append(text(560, 92, '= 40', k='green', size=38, font='scrawl', anchor='start'))
    return svg(660, 160, rough(*parts) + ''.join(lab), 'Three choices: 2 coffees times 4 milk options times 5 sweetening options makes 40')

Q.append(dict(
    n=20, orig=42, answer='D', topic='Counting choices',
    question=f"""<p>The coffee machine in our office offers a choice of {hl('regular or decaffeinated coffee', 'g', 1)}; {hl('black', 'p', 2)}
or with {hl('one of three sorts of milk', 'g', 2)} (full, semi-skimmed, skimmed); and, {hl('for those who want sweetening', 'p', 3)}, either {hl('one or two spoonfuls of sugar or one or two non-sugar sweetening tablets', 'g', 3)}.</p>
<p class="stem">How many different kinds of coffee can be made?</p>""",
    options={'A': '11', 'B': '24', 'C': '32', 'D': '40', 'E': '48'},
    notes=[(1, 'g', '2 choices.'),
           (2, 'p', 'Black counts as a choice too: 1 + 3 = <b>4</b> milk options.'),
           (3, 'p', '“For those who want it”: no sweetening is also allowed. 1 + 4 = <b>5</b> options.')],
    steps=[
        f"""<p>Three separate choices, made one after another, so <b>multiply</b>:</p>{_coffee()}
{calc(f'2 × 4 × 5 = {boxed("40")}')}
{note('The “nothing” options (black, no sweetener) are the easy ones to forget.', 'trap')}""",
    ],
    answer_text='40 = 2 coffees × 4 milk options × 5 sweetening options.',
    why={'A': '11 adds the choices (2 + 4 + 5). Every coffee can go with every milk option, so multiply.',
         'B': '24 = 2 × 3 × 4: forgets both black coffee and no sweetening.',
         'C': '32 = 2 × 4 × 4: forgets that you can have no sweetening.',
         'E': '48 = 2 × 4 × 6: counts “no sugar” and “no tablets” as two different choices, but they make the same coffee.'},
    fast='2 × (black + 3 milks) × (none + 4 sweeteners) = 2 × 4 × 5 = 40.',
))

# ---------------------------------------------------------------- 21 (Q43)
def _ladders():
    parts, lab = [], []
    rows = (('Indigo Iguanas', 44, 'pen', ['82', '125 − 41 = 84', '118 − 42 = 76'], ['41', '42', '38']),
            ('Orange Ocelots', 164, 'orange', ['76', '130 − 38 = 92', '128 − 46 = 82'], ['38', '46', '41']))
    boxes = ((10, 72, 'Round 1'), (178, 128, 'QF: total − carried'), (398, 128, 'SF: total − carried'))
    circles = (128, 348, 570)
    for title, y, col, texts, carries in rows:
        lab.append(text(10, y - 12, title, k=col, size=18, anchor='start', font='scrawl'))
        for (bx, bw, sub), t in zip(boxes, texts):
            parts.append(rect(bx, y, bw, 52, k=col, fill='paper', sw=2))
            lab += [text(bx + bw / 2, y + 18, sub, k='muted', size=12), text(bx + bw / 2, y + 42, t, k='ink', size=16)]
        for i, (cx, cval) in enumerate(zip(circles, carries)):
            bx, bw, _ = boxes[i]
            parts.append(arrow(bx + bw + 2, y + 26, cx - 22, y + 26, k='red', w=2))
            lab.append(text((bx + bw + cx - 20) / 2, y + 16, '½', k='red', size=16))
            parts.append(circle(cx, y + 26, 20, k=col, fill='g' if i == 2 else 'y', sw=2.2))
            lab.append(text(cx, y + 32, cval, k='ink', size=17))
            if i < 2:
                parts.append(arrow(cx + 21, y + 26, boxes[i + 1][0] - 2, y + 26, k='muted', w=1.8))
        lab.append(text(600, y + 22, 'into', k=col, size=14, anchor='start'))
        lab.append(text(600, y + 40, 'final', k=col, size=14, anchor='start'))
    lab += [text(330, 256, 'Final: Indigo starts on 38, Orange on 41, so Indigo is 3 behind', k='ink', size=16),
            text(330, 282, 'beat 3 using even scores only: at least 4 more', k='red', size=19, font='scrawl')]
    return svg(660, 296, rough(*parts) + ''.join(lab),
               'Carry-over ladders: Indigo 82 to 41, then 84 new to 42, then 76 new to 38; Orange 76 to 38, then 92 new to 46, then 82 new to 41')

Q.append(dict(
    n=21, orig=43, answer='A', topic='Rules & scoring',
    question=f"""<p>This is the draw for this year's end of season knockout trophy (and the results so far)
competed for by sixteen teams that take part in a quiz league:</p>
{fig(Y, 'ps_q21_draw', 'Knockout draw with scores. Indigo Iguanas: 82 in round 1, 125 in the quarter-final, 118 in the semi-final. Orange Ocelots: 76, 130 and 128. Amber Aardvarks: 78, 125 and 115', 540)}
<p>Although teams are drawn against each other, all participating teams in each round
answer the same set of {hl('50 questions, worth 2 points each', 'y', 1)}.</p>
<p>In the first round, each 'match' is won straightforwardly by the team with the higher
number of points. This team {hl('carries half of these points through to the next round', 'g', 2)}; then in
subsequent rounds winners {hl("carry through half of their 'new' points from the previous round", 'p', 3)}. {hl('For example, the Amber Aardvarks carried 39 points through to their quarter-final, then in the quarter-final itself they added 86, and so carried 43 through to their semi-final.', 'y', 4)}</p>
<p class="stem">How many more points {hl('(at least)', 'b', 5)} must the Indigo Iguanas score than the Orange Ocelots
in the final to win the trophy?</p>""",
    options={'A': '4', 'B': '6', 'C': '8', 'D': '10', 'E': '12'},
    notes=[(1, 'y', 'Every score is a multiple of 2: <b>scores are always even</b>.'),
           (2, 'g', 'Round 1: carry half the score.'),
           (3, 'p', '“New” points = this round’s total minus what was carried in. Only those get halved.'),
           (4, 'y', 'The example shows it: 125 total = 39 carried + 86 new; half of 86 = 43.'),
           (5, 'b', 'Smallest winning margin, so a tie isn’t enough.')],
    steps=[
        f"""<p>Use the example as a template: <b>new = round total − points carried in</b>, then carry half of new.</p>
{calc('Amber: 78 → 39; QF 125 − 39 = 86 new → 43 ' + tick() + ' matches the question')}""",
        f"""<p>Do the same for the two finalists:</p>{_ladders()}""",
        f"""<p>In the final, Indigo scores I and Orange scores O:</p>
{calc('38 + I &gt; 41 + O', 'I − O &gt; 3', f'scores are even, so I − O is even {ar()} at least {boxed("4")}')}
{note('Winning by 3 is impossible: two even numbers always differ by an even number.', 'check')}""",
    ],
    answer_text='4: Indigo carry 38 and Orange 41, and the gap must be even and more than 3.',
    why={'B': '6 halves the whole semi-final totals (59 against 64, a gap of 5) instead of the new points only.',
         'C': '8 forgets to halve: carries all the new semi-final points (76 against 82, a gap of 6).',
         'D': '10 is just the gap between the semi-final totals (128 − 118). Nothing that big carries over.',
         'E': '12 carries the full semi-final totals across and then beats the gap of 10 with an even number.'},
    fast='Carry-ins: Indigo 41 → 42 → 38, Orange 38 → 46 → 41. Need more than 3 extra, even, so 4.',
))

# ---------------------------------------------------------------- 22 (Q44)
def _park():
    N = {'L': (59, 152), 'T': (185, 82), 'C': (300, 128), 'BL': (134, 240), 'BM': (255, 250),
         'RT': (450, 52), 'RB': (450, 246), 'RM': (549, 200), 'R': (622, 162)}
    E = [('L', 'T', -0.25), ('T', 'C', -0.15), ('L', 'C', 0.12), ('L', 'BL', 0.25), ('BL', 'C', -0.12), ('BL', 'BM', 0.2),
         ('BM', 'C', 0.12), ('C', 'RT', -0.25), ('C', 'RB', 0.2), ('RT', 'RB', 0.08), ('RT', 'R', -0.3), ('R', 'RM', 0.3), ('RM', 'RB', -0.3)]
    parts, lab = [], []
    parts.append(path('M22 150 Q30 40 200 52 Q300 90 290 150 Q300 270 150 268 Q30 260 22 150 Z', k='pen', fill='b', sw=1.4))
    parts.append(path('M330 150 Q380 20 520 32 Q650 60 640 170 Q600 280 450 272 Q350 250 330 150 Z', k='orange', fill='o', sw=1.4))
    for a, b, bend in E:
        (x1, y1), (x2, y2) = N[a], N[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        cx, cy = mx - (y2 - y1) * bend, my + (x2 - x1) * bend
        parts.append(path(f'M{x1} {y1} Q{cx:.1f} {cy:.1f} {x2} {y2}', k='ink', sw=2))
    for name, (x, y) in N.items():
        star = name in ('L', 'T', 'C', 'BL', 'RB')
        parts.append(circle(x, y, 8 if star else 6, k='red' if name == 'C' else 'green' if name == 'RB' else 'orange' if star else 'ink',
                            fill='paper' if star else 'ink', sw=3 if star else 1.5))
    lab += [text(300, 104, 'bandstand', k='red', size=18, font='scrawl'),
            text(450, 280, 'fountain', k='green', size=18, font='scrawl'),
            text(59, 182, '?', k='orange', size=22, font='scrawl'), text(185, 62, '?', k='orange', size=22, font='scrawl'),
            text(134, 278, '?', k='orange', size=22, font='scrawl'),
            text(150, 314, 'statue, lake, bowling green: which is which?', k='orange', size=16),
            text(470, 314, 'only way across is through the bandstand', k='muted', size=14)]
    return svg(660, 326, rough(*parts) + ''.join(lab),
               'The path map in two halves joined only at the middle star, the bandstand; the bottom-right star is the fountain; the three left-hand stars can’t be told apart')

Q.append(dict(
    n=22, orig=44, answer='C', topic='Networks & logic',
    question=f"""<p>My local park has a network of paths linking various locations, as shown below. The stars
on the map represent {hl("five of the park's landmarks", 'g', 1)}: the fountain, lake, bandstand, statue
and bowling green.</p>
{fig(Y, 'ps_q22_map', 'Map of paths with nine junctions; five have stars: three on the left part, one in the middle where the left and right parts meet, and one at the bottom of the right part', 470)}
<p>When I walk round the park, I {hl('often vary my routes', 'p', 2)} and I do not always take the shortest
route from one place to another. I have noticed that {hl('when I go from the statue to the fountain, I always pass the bandstand', 'y', 3)}, but that {hl('going from the lake to the bowling green, I never pass the fountain unless I pass the bandstand twice', 'y', 4)}.</p>
<p class="stem">{hl('How many of the stars', 'b', 5)} on the diagram can be identified from the given information?</p>""",
    options={'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '5'},
    notes=[(1, 'g', 'Five stars, five names.'),
           (2, 'p', 'Any route at all, so “always” really means you <b>can’t</b> get round it.'),
           (3, 'y', 'The bandstand blocks every route from statue to fountain: a bottleneck.'),
           (4, 'y', 'To reach the fountain from lake/bowling green you must go through the bandstand and come back.'),
           (5, 'b', 'How many stars get a definite name?')],
    steps=[
        f"""<p>The map falls into two halves, joined at <b>one point</b>: the middle star. It is the only star you can’t walk round.</p>
{calc(f'“always pass the bandstand” on every route {ar()} bandstand = <b>middle star</b>')}""",
        f"""<p>So the statue and the fountain are in <b>different halves</b>. One of them is the bottom-right star, the other is on the left.</p>
<p>Lake → bowling green: you only pass the fountain by crossing the bandstand and coming back (twice). So the fountain is
alone in the other half from the lake and bowling green {ar()} <b>fountain = bottom-right star</b>.</p>
{note('If the fountain were on the left, you could walk to it from the lake without touching the bandstand at all.', 'check')}""",
        f"""{_park()}
<p>Statue, lake and bowling green are the three left-hand stars, but nothing tells them apart.</p>
{calc(f'identified: bandstand + fountain = {boxed("2")}')}""",
    ],
    answer_text='2: the bandstand (middle star) and the fountain (bottom-right star).',
    why={'A': '0 misses that the middle star is the only bottleneck, so it must be the bandstand.',
         'B': '1 finds the bandstand but not the fountain. The second clue puts the fountain alone in the right half.',
         'D': '3 would need one of the left-hand stars pinned down, but statue, lake and bowling green all play the same role there.',
         'E': '5 would need every star named. The three left-hand stars can be swapped round and both clues still hold.'},
    fast='Bottleneck star = bandstand; the lone star in the other half = fountain; the other three are interchangeable. 2.',
))

# ---------------------------------------------------------------- 23 (Q48)
def _boats():
    X = lambda t: 76 + (t - 8) * 102
    S, H = 76, 226
    ferry = [(8, H), (9.25, S), (9.75, S), (11, H), (11.5, H), (12.75, S), (13.25, S), (13.5, S + 30)]
    hover = [(8, H), (8.75, S), (9, S), (9.75, H), (10, H), (10.75, S), (11, S), (11.75, H), (12, H), (12.75, S), (13, S), (13.5, S + 100)]
    parts = [line(X(8), S, X(13.6), S, k='muted', w=1.2, dash=True), line(X(8), H, X(13.6), H, k='muted', w=1.2, dash=True),
             poly([(X(t), y) for t, y in ferry], k='pen', sw=3.2, closed=False),
             poly([(X(t), y) for t, y in hover], k='orange', sw=2.6, closed=False),
             circle(X(12.75), S, 12, k='green', sw=3)]
    lab = [text(66, S + 5, 'Selmer', k='ink', size=16, anchor='end'), text(66, H + 5, 'Harport', k='ink', size=16, anchor='end'),
           text(X(12.75), S - 22, '12:45 both at Selmer!', k='green', size=19, font='scrawl')]
    for h in range(8, 14):
        parts.append(line(X(h), H + 4, X(h), H + 14, k='ink', w=1.6))
        lab.append(text(X(h), H + 32, f'{h:02d}:00', k='muted', size=14))
    parts += [line(150, 290, 190, 290, k='pen', w=3.2), line(330, 290, 370, 290, k='orange', w=2.6)]
    lab += [text(196, 295, 'ferry', k='pen', size=16, anchor='start'), text(376, 295, 'hovercraft', k='orange', size=16, anchor='start')]
    return svg(660, 306, rough(*parts) + ''.join(lab),
               'Journey graph from 08:00: flat parts are time in port. The ferry and hovercraft are first in the same port together at Selmer at 12:45')

Q.append(dict(
    n=23, orig=48, answer='B', topic='Timetables & cycles',
    question=f"""<p>The ferry from Harport to Selmer is {hl('at sea for 1 hour 15 minutes', 'g', 1)} and {hl('at its berth at either end for 30 minutes', 'g', 1)}. The hovercraft service between the same ports {hl('takes only 45 minutes', 'g', 2)}
and is {hl('berthed for 15 minutes', 'g', 2)} before returning.</p>
<p class="stem">If both leave Harport at 08:00 what is the {hl('next time they will both be at the same port together', 'b', 3)}?</p>""",
    options={'A': '09:45', 'B': '12:45', 'C': '14:45', 'D': '15:00', 'E': '18:00'},
    notes=[(1, 'g', 'Ferry: sail 1 h 15, wait 30 min, repeat. Round trip 3½ h.'),
           (2, 'g', 'Hovercraft: sail 45 min, wait 15 min, repeat. Round trip 2 h.'),
           (3, 'b', 'Same port, at the same moment. Being in two different ports doesn’t count.')],
    steps=[
        f"""<p>List when each is in port (in → out):</p>
{table([['Ferry', 'Selmer 09:15 → 09:45', 'Harport 11:00 → 11:30', hl('Selmer 12:45 → 13:15', 'g')],
        ['Hovercraft', 'Selmer 08:45 → 09:00', 'Harport 09:45 → 10:00', 'Selmer 10:45 → 11:00'],
        ['Hovercraft (cont.)', 'Harport 11:45 → 12:00', hl('Selmer 12:45 → 13:00', 'g'), '']],
       head=['', 'in port', 'in port', 'in port'])}""",
        f"""<p>Draw both on one journey graph (flat lines = in port):</p>{_boats()}
{calc(f'first overlap: both reach Selmer at {boxed("12:45")}')}
{note('11:00 to 11:30 is a near miss: the ferry is in Harport, but the hovercraft left Harport at 10:00 and doesn’t return until 11:45.', 'check')}""",
    ],
    answer_text='12:45, when both arrive at Selmer.',
    why={'A': 'At 09:45 the hovercraft is back at Harport while the ferry is leaving Selmer: different ports.',
         'C': 'At 14:45 the hovercraft is at Selmer but the ferry is in Harport (14:30 to 15:00).',
         'D': 'At 15:00 both are leaving port, but different ones: the ferry leaves Harport, the hovercraft leaves Selmer.',
         'E': 'At 18:00 both really are in Harport, but that is later than 12:45.'},
    fast='Ferry is in Selmer 12:45 to 13:15 (after 08:00 → 11:30 round trip). Hovercraft arrives at Selmer at 12:45 too.',
))

# ---------------------------------------------------------------- 24 (Q49)
def _phone_rows():
    parts, lab = [], []
    rows = ((['5', '8', '0', '1', '1', '?'], 1, 'scrap starting on the 8 of 58', '? = 0 to 9: 10 numbers'),
            (['5', '8', '8', '0', '1', '1'], 2, 'scrap at the end', '1 number'),
            (['5', '8', '1', '1', '0', '8'], 2, 'scrap upside down (reads 1108)', '1 number'))
    for r, (digits, start, title, count) in enumerate(rows):
        y = 40 + r * 82
        lab.append(text(120, y - 10, title, k='ink', size=15, anchor='start'))
        for i, d in enumerate(digits):
            x = 120 + i * 48
            inside = start <= i < start + 4
            f = 'o' if inside else 'p' if d == '?' else 'paper'
            parts.append(rect(x, y, 44, 44, k='ink', fill=f, sw=1.6))
            lab.append(text(x + 22, y + 31, d, k='ink', size=24, font='print'))
        xa, xb = 120 + start * 48 - 6, 120 + (start + 4) * 48 + 2
        parts.append(poly([(xa, y - 5), (xb, y - 5), (xb + 5, y + 8), (xb - 2, y + 20), (xb + 5, y + 34), (xb, y + 50),
                           (xa, y + 50), (xa - 5, y + 36), (xa + 2, y + 22), (xa - 5, y + 8)], k='orange', sw=2.4))
        lab.append(text(430, y + 28, count, k='pen', size=17, anchor='start'))
    lab.append(text(330, 286, '10 + 1 + 1 = 12', k='red', size=24, font='scrawl'))
    return svg(660, 300, rough(*parts) + ''.join(lab),
               'Three ways the scrap fits a number starting 58: 58011 then any digit (10 numbers), 588011, and upside down 581108')

Q.append(dict(
    n=24, orig=49, answer='D', topic='Counting possibilities',
    question=f"""<p>All the telephone numbers in my village have {hl('six digits and begin with 58', 'y', 1)}. I have
accidentally {hl('torn up', 'p', 2)} and thrown away a piece of paper on which I had written the
telephone number of a friend who lives nearby. The only piece I can find is the scrap
shown below:</p>
{fig(Y, 'ps_q24_scrap', 'A torn scrap of paper showing the digits 8 0 1 1', 130)}
<p class="stem">How many different phone numbers in my village {hl('could be consistent', 'b', 3)} with this extract?</p>""",
    options={'A': '2', 'B': '10', 'C': '11', 'D': '12', 'E': '22'},
    notes=[(1, 'y', 'Every number looks like 5 8 _ _ _ _.'),
           (2, 'p', 'A torn scrap: it could come from anywhere in the number, and you can’t tell which way up it is!'),
           (3, 'b', 'Count every number the scrap could have come from.')],
    steps=[
        f"""<p>The scrap shows 4 digits in a row. Where can “8011” sit inside 5 8 _ _ _ _?</p>
<ul><li>It can’t start on the 5.</li>
<li>Start on the <b>8</b> of 58: 5 8 0 1 1 ? {ar()} last digit anything: <b>10</b> numbers.</li>
<li>Start at the 3rd digit: 5 8 8 0 1 1 {ar()} <b>1</b> number.</li></ul>""",
        f"""<p>Now turn the scrap upside down. 8, 0 and 1 all look the same turned round, so it reads <b>1108</b>.
It can’t start on the 8 of 58 (that would need a 1 there), so only: 5 8 1 1 0 8 {ar()} <b>1</b> number.</p>
{_phone_rows()}
{calc(f'10 + 1 + 1 = {boxed("12")}')}""",
    ],
    answer_text='12: 580110 to 580119, 588011, and 581108 (scrap upside down).',
    why={'A': '2 only puts the scrap at the very end (588011 and 581108), missing that it can start on the 8 of 58.',
         'B': '10 only counts 580110 to 580119.',
         'C': '11 forgets the scrap might be upside down.',
         'E': '22 thinks upside down gives another 11, but “1108” can’t start on the 8 of 58, so it adds only 1.'},
    fast='58011? gives 10, 588011 gives 1, and upside down 581108 gives 1. Total 12.',
))

# ---------------------------------------------------------------- 25 (Q50)
PIPS = {1: [(0.5, 0.5)], 3: [(0.24, 0.24), (0.5, 0.5), (0.76, 0.76)], -3: [(0.24, 0.76), (0.5, 0.5), (0.76, 0.24)],
        6: [(0.24, 0.3), (0.5, 0.3), (0.76, 0.3), (0.24, 0.7), (0.5, 0.7), (0.76, 0.7)],
        -6: [(0.3, 0.24), (0.3, 0.5), (0.3, 0.76), (0.7, 0.24), (0.7, 0.5), (0.7, 0.76)]}


def _face(x, y, n, s=88, fill='paper'):
    p = [rect(x, y, s, s, k='ink', fill=fill, sw=2.2, rx=8)]
    p += [circle(x + a * s, y + b * s, 7, k='ink', fill='ink', sw=1) for a, b in PIPS[n]]
    return p


def _die_turns():
    parts, lab = [], []
    for x, n, title, sub in ((30, 3, 'view 1: front', 'top is 1'), (190, -3, 'view 3: front', 'top is 4'),
                             (370, 6, 'view 2: top', 'front is 5'), (530, -6, 'view 4: top', 'front is 1')):
        parts += _face(x, 44, n, fill='y' if abs(n) == 3 else 'b')
        lab += [text(x + 44, 30, title, k='ink', size=15), text(x + 44, 156, sub, k='pen', size=16)]
    parts += [arrow(124, 70, 186, 70, k='red', bend=-0.3), arrow(464, 70, 526, 70, k='red', bend=-0.3)]
    lab += [text(155, 44, '¼ turn', k='red', size=15), text(495, 44, '¼ turn', k='red', size=15),
            text(155, 190, 'the 1 tipped to the side', k='ink', size=16), text(155, 212, 'so 1 touches 4', k='green', size=19, font='scrawl'),
            text(495, 190, 'the die spun round', k='ink', size=16), text(495, 212, 'so 1 touches 5', k='green', size=19, font='scrawl')]
    return svg(660, 226, rough(*parts) + ''.join(lab),
               'The 3 face in views 1 and 3 has its diagonal turned a quarter turn; the 6 face in views 2 and 4 has its rows turned a quarter turn')


def _neighbours():
    parts = [circle(170, 116, 34, k='ink', fill='y', sw=2.4)]
    lab = [text(170, 128, '1', k='ink', size=34, font='scrawl')]
    for (x, y), n, why in (((170, 30), 3, 'view 1'), ((290, 116), 4, '¼ turn'), ((170, 202), 5, '¼ turn'), ((50, 116), 6, 'view 4')):
        parts.append(line(170 + (x - 170) * 0.42, 116 + (y - 116) * 0.42, 170 + (x - 170) * 0.7, 116 + (y - 116) * 0.7, k='green', w=2.4))
        parts.append(circle(x, y, 24, k='green', fill='g', sw=2))
        lab.append(text(x, y + 9, n, k='ink', size=26, font='scrawl'))
    parts += [line(330, 116, 470, 116, k='red', w=2.4, dash=True), circle(510, 116, 34, k='red', fill='p', sw=2.4)]
    lab += [text(510, 128, '2', k='ink', size=34, font='scrawl'),
            text(400, 104, 'opposite', k='red', size=17, font='scrawl'),
            text(510, 180, 'the only face', k='red', size=16), text(510, 200, 'not touching 1', k='red', size=16)]
    return svg(640, 236, rough(*parts) + ''.join(lab), 'The 1 touches 3, 4, 5 and 6, so the only face that can be opposite it is the 2')

Q.append(dict(
    n=25, orig=50, answer='A', topic='Dice & 3D views',
    question=f"""<p>On a normal die, opposing faces add up to 7. Four views of the same die on which the
numbers are {hl('arranged differently from a normal die', 'p', 1)} are shown below. {hl('The unseen face has the number two on it.', 'y', 2)}</p>
{fig(Y, 'ps_q25_dice', 'Four views of the die, each showing a top and front face: 1 on top with 3 in front; 6 on top with 5 in front; 4 on top with 3 in front (diagonal the other way); 6 on top (rows running front to back) with 1 in front', 420)}
<p class="stem">How many spots are on the face {hl('opposite the two', 'b', 3)} on this die?</p>""",
    options={'A': '1', 'B': '3', 'C': '4', 'D': '5', 'E': '6'},
    notes=[(1, 'p', 'So “opposites add to 7” is useless here. Don’t answer 5!'),
           (2, 'y', 'The 2 never appears: we must find its opposite by elimination.'),
           (3, 'b', 'Opposite faces never touch. Find a face that touches four others: the one left over is its opposite.')],
    steps=[
        f"""<p>Faces seen together touch each other: 1 &amp; 3, 6 &amp; 5, 4 &amp; 3, 6 &amp; 1. Now look at how the pips are <b>turned</b>:</p>
{_die_turns()}
<ul><li>Views 1 and 3: the same 3 is in front, but its diagonal has flipped direction. The die was turned a quarter turn about the front face,
so the top (1) moved to a side and a side face (4) came to the top. So <b>1 touches 4</b>.</li>
<li>Views 2 and 4: the same 6 is on top, but its rows have turned from across to front-to-back. The die was spun a quarter turn,
so the new front (1) was beside the old front (5). So <b>1 touches 5</b>.</li></ul>""",
        f"""<p>So the 1 touches 3, 4, 5 and 6. A face touches 4 others and is opposite exactly 1:</p>{_neighbours()}
{calc(f'opposite the 2 = {boxed("1")}')}""",
    ],
    answer_text='1: the 1 touches 3, 4, 5 and 6, so it must be opposite the 2.',
    why={'B': 'The 3 and the 1 are seen together in view 1, so they touch.',
         'C': 'The quarter turn of the 3 shows the 4 was beside the 1, so they touch.',
         'D': '5 is the normal-die answer (2 + 5 = 7), but this die isn’t normal. The spin of the 6 shows 5 is beside the 1.',
         'E': 'The 6 and the 1 are seen together in view 4, so they touch.'},
    fast='1 touches 3 and 6 (seen together), 4 and 5 (the quarter turns). The only face left for it to face is the 2.',
))
