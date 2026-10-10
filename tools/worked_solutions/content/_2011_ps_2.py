from wslib import *

Y = 2011
Q = []


# ---------------------------------------------------------------- 9 (Q19)
def _logo():
    c, ox, oy = 22, 230, 110
    P = lambda x, y: (ox + x * c, oy + y * c)
    outline = [(2, 0), (9, 0), (9, 1), (7, 1), (7, 3.5), (9, 3.5), (9, 4.5), (7, 4.5), (7, 7), (9, 7), (9, 8), (6, 8), (6, 1), (5, 1),
               (5, 8), (4, 8), (4, 1), (3, 1), (3, 8), (0, 8), (0, 6), (1, 6), (1, 7), (2, 7)]
    parts = [poly([P(x, y) for x, y in outline], k='ink', fill='b', sw=2.2)]
    lab = []
    for i in range(10):
        lab.append(text(ox + i * c, oy + 8 * c + 17, i, k='muted', size=13))
    for j in range(9):
        lab.append(text(ox - 6, oy + j * c + 5, j, k='muted', size=13, anchor='end'))
    sh = 14

    def hstrip(y, cuts):
        return [rect(ox, y, 9 * c, sh, k='red', sw=2)] + [line(ox + x * c, y, ox + x * c, y + sh, k='red', w=2) for x in cuts]

    def vstrip(x, cuts):
        return [rect(x, oy, sh, 8 * c, k='red', sw=2)] + [line(x, oy + y * c, x + sh, oy + y * c, k='red', w=2) for y in cuts]

    parts += hstrip(oy + 8 * c + 26, [3, 4, 5, 6]) + hstrip(oy - 40, [1, 2])
    parts += vstrip(ox - 50, [6]) + vstrip(ox + 9 * c + 36, [1, 3.5, 4.5, 7])
    cx, cy = ox + 4.5 * c, oy + 4 * c
    lab += [text(cx, oy - 50, 'from the back: 7 | 1 | 1 → D', k='red', size=17),
            text(cx, oy + 8 * c + 64, 'from the front: 3 | 1 | 1 | 1 | 3 → C', k='red', size=17),
            text(ox - 60, cy - 8, 'from the left:', k='red', size=17, anchor='end'),
            text(ox - 60, cy + 14, '6 | 2 → E', k='red', size=17, anchor='end'),
            text(ox + 9 * c + 60, cy - 8, 'from the right:', k='red', size=17, anchor='start'),
            text(ox + 9 * c + 60, cy + 14, '1 | 2½ | 1 | 2½ | 1 → A', k='red', size=17, anchor='start'),
            text(cx, oy + 8 * c + 96, 'B has 4 strips: no side gives 4!', k='pen', size=21, font='scrawl'),
            eye(ox - 26, oy + 8 * c + 33, facing='up'), eye(ox - 26, oy - 33, facing='down'),
            eye(ox - 90, oy + 8 * c - 16, facing='right'), eye(ox + 9 * c + 90, oy + 8 * c - 16, facing='left')]
    return svg(660, 412, rough(*parts) + ''.join(lab),
               'Plan of the logo (letters J, T, E) on a 9 by 8 grid with the strip pattern seen from each of the four sides')


Q.append(dict(
    n=9, orig=19, answer='B', topic='3D views',
    question=f"""<p>This is the {hl('view from above', 'y', 1)} of the large three-dimensional logo situated in the forecourt of
the head office of Justin Thyme Enterprises:</p>
{fig(Y, 'ps_q09_logo', 'Plan view of the logo: the outline of the letters J, T and E joined by a bar across the top', 230)}
<p>It was sculpted from a single cube of marble, and has a {hl('uniform cross-section from top to bottom', 'y', 2)}.</p>
<p class="stem">Which of the following is {hl('<b>not</b>', 'b', 3)} a possible side view of the logo?</p>
{fig(Y, 'ps_q09_opts', 'Five side views A to E: rectangles divided by vertical lines into strips of different widths', 420)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'A plan: the letters J, T, E (Justin Thyme Enterprises!) seen from the sky.'),
           (2, 'y', 'The shape is just pushed straight up, so each side view is a rectangle split by vertical lines.'),
           (3, 'b', 'There are 4 sides to look from. Four options match them; one doesn’t.')],
    steps=[
        f"""<p>From the side you see a vertical line wherever the nearest surface jumps forwards or backwards. So walk round the plan
and look from each of the four sides, marking the jumps:</p>{_logo()}""",
        f"""{calc('front (bottom of the plan): J foot, gap, T leg, gap, E base = 5 strips → C',
                  'back (top of the plan): long top bar, then the J’s hook in two steps = 3 strips → D',
                  'right: three arms of the E with two gaps = 5 strips → A',
                  'left: the J’s stem and its curled foot = 2 strips → E',
                  f'B: 4 strips (2 | 5 | 1 | 1) {cross()} no side gives that')}
{calc(f'not possible = {boxed("B")}')}""",
        f"""{note('Count the strips first. Only if two options tie do you need to measure widths.', 'tip')}""",
    ],
    answer_text='View B: it has 4 strips, but the four sides give 5, 3, 5 and 2.',
    why={'A': 'A is the view from the right: the three arms of the E stick out, with the gaps between them set back.',
         'C': 'C is the view from the front: the J’s foot, the T’s leg and the E’s base, with two gaps between them.',
         'D': 'D is the view from the back: the long top bar, then the J’s hook stepping back twice.',
         'E': 'E is the view from the left: the J’s tall stem and its curled-up foot.'},
    fast='Count strips from each side: front 5, back 3, right 5, left 2. B has 4, so it can’t be a side view.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _raoul():
    X = lambda v: 140 + v * 0.025
    parts, lab = [], []
    parts.append(rect(X(0), 40, X(18510) - X(0), 34, k='ink', fill='o', sw=1.8))
    parts.append(rect(X(0), 104, X(15940) - X(0), 34, k='ink', fill='b', sw=1.8))
    lab += [text(130, 63, 'new car', k='ink', size=17, anchor='end'), text(130, 127, 'savings', k='ink', size=17, anchor='end'),
            text(X(18510) - 8, 63, '$18 510', k='ink', size=17, anchor='end'), text(X(15940) - 8, 127, '$15 940', k='ink', size=17, anchor='end'),
            text(X(5000), 63, '8% for 8 years', k='ink', size=15), text(X(5000), 127, '6% for 8 years', k='ink', size=15)]
    parts.append(line(X(10000), 26, X(10000), 152, k='muted', w=2, dash=True))
    lab.append(text(X(10000), 170, 'today: $10 000', k='muted', size=15))
    parts.append(line(X(15940), 92, X(15940), 152, k='red', w=1.8))
    parts.append(line(X(18510), 80, X(18510), 152, k='red', w=1.8))
    parts.append(line(X(15940), 146, X(18510), 146, k='red', w=2.2, tail=True, head=True))
    lab.append(text((X(15940) + X(18510)) / 2, 172, 'short by $2 570', k='red', size=19, font='scrawl'))
    return svg(640, 186, rough(*parts) + ''.join(lab),
               'Bars: the new car costs 18 510 in 8 years but the savings only grow to 15 940, leaving a gap of 2 570')


Q.append(dict(
    n=10, orig=20, answer='B', topic='Reading tables',
    question=f"""<p>The table below, from a newspaper, shows how much money ($) you will need at various
points in the future to buy {hl('items costing $1000 today', 'p', 1)}, depending on the annual rate of
inflation.</p>
<p style="text-align:center;margin:0"><i>Average yearly rate of inflation</i></p>
{table([['5', '1217', '1338', '1469', '1611'], ['6', '1265', '1419', '1587', '1772'], ['7', '1316', '1504', '1714', '1949'],
        [hl('8', 'g'), '1369', hl('1594', 'g'), hl('1851', 'g'), '2144'], ['9', '1423', '1690', '1999', '2358'],
        ['10', '1480', '1791', '2159', '2594'], ['20', '2191', '3207', '4661', '6728'], ['30', '3423', '5743', '10063', '17449'],
        ['60', '10520', '32988', '101257', '304482']],
       head=['Years', '4 %', '6 %', '8 %', '10 %'])}
<p>Raoul has just bought a new car for $10 000. He expects this car to {hl('last him 8 years', 'g', 2)},
when he will buy another equivalent model. He puts $10 000 into a bank account ready
to pay for the next car. {hl('The price of cars rises with inflation at 8%', 'y', 3)} and {hl('his savings only earn interest of 6%', 'y', 4)}.</p>
<p class="stem">How much will he need to add to his savings when he needs to buy his new car?</p>""",
    options={'A': '$ 1612', 'B': '$ 2570', 'C': '$ 5338', 'D': '$ 5940', 'E': '$ 8510'},
    notes=[(1, 'p', 'The table is per $1000. Raoul has $10 000, so multiply by <b>10</b>.'),
           (2, 'g', 'Use the 8-year row.'),
           (3, 'y', 'The car price grows like the 8% column.'),
           (4, 'y', 'His money grows like the 6% column (interest works just like inflation here).')],
    steps=[
        f"""<p>Read both values from the 8-year row, then scale up from $1000 to $10 000:</p>
{calc(f'new car: 8% column {ar()} 1851 per $1000 {ar()} × 10 = <b>$18 510</b>',
      f'savings: 6% column {ar()} 1594 per $1000 {ar()} × 10 = <b>$15 940</b>')}""",
        f"""{_raoul()}
{calc(f'$18 510 − $15 940 = {boxed("$2 570")}')}
{note('Shortcut: subtract first, then scale. 1851 − 1594 = 257 per $1000, so $2570 for $10 000.', 'tip')}""",
    ],
    answer_text='$2570: the car will cost $18 510 but the savings will only be $15 940.',
    why={'A': '$1612 is too small. The 8-year gap is 1851 − 1594 = 257 per $1000, which is $2570.',
         'C': '$5338 doesn’t come from the 8-year row. It would need his savings to be worth only about $13 170.',
         'D': '$5940 is the <b>interest</b> his savings earn (15 940 − 10 000), not the amount he is short.',
         'E': '$8510 forgets the interest: it compares the new price with the original $10 000.'},
    fast='8-year row: (1851 − 1594) × 10 = 257 × 10 = $2570.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _routes():
    B, C, D = (110, 130), (340, 130), (570, 130)
    parts = [path(f'M{B[0]} {B[1]} Q225 30 {C[0]} {C[1]}', k='pen', sw=3.2),
             path(f'M{B[0]} {B[1]} Q225 230 {C[0]} {C[1]}', k='green', sw=3.2),
             path(f'M{C[0]} {C[1]} Q455 30 {D[0]} {D[1]}', k='pen', sw=3.2),
             path(f'M{C[0]} {C[1]} Q455 230 {D[0]} {D[1]}', k='green', sw=3.2),
             line(C[0], 38, C[0], 118, k='muted', w=1.4, dash=True)]
    for p in (B, C, D):
        parts.append(circle(p[0], p[1], 8, k='ink', fill='ink'))
    lab = [text(98, 136, 'Bowbridge', k='ink', size=18, anchor='end'),
           text(582, 136, 'Downland', k='ink', size=18, anchor='start'),
           text(C[0], 30, 'Clatterton', k='ink', size=18),
           text(225, 66, 'motorway 35 mi = 35 min', k='pen', size=15),
           text(225, 204, 'Buttercup 30 mi = 45 min', k='green', size=15),
           text(455, 66, 'motorway 35 mi = 35 min', k='pen', size=15),
           text(455, 204, 'Buttercup 20 mi = 30 min', k='green', size=15),
           text(225, 240, 'leg 1: motorway quicker by 10', k='red', size=17, font='scrawl'),
           text(455, 240, 'leg 2: Buttercup quicker by 5', k='red', size=17, font='scrawl')]
    return svg(660, 254, rough(*parts) + ''.join(lab),
               'Two legs, each with a motorway and a Buttercup Way option: leg 1 takes 35 or 45 minutes, leg 2 takes 35 or 30 minutes')


Q.append(dict(
    n=11, orig=24, answer='C', topic='Speed, time & routes',
    question=f"""<p>As part of a journey, I must travel from Bowbridge to Downland. I can choose either the
motorway (known locally as 'the road to hell') or the old road known as Buttercup
Way. {hl('On the motorway I average 60 mph', 'g', 1)}, {hl('on the old road I average 40 mph', 'g', 2)}. I can
{hl('change from one to the other at Clatterton', 'y', 3)} where they cross.</p>
{fig(Y, 'ps_q11_map', 'Map: the M49 motorway and the B1404 Buttercup Way both run from Bowbridge to Clatterton and on to Downland, crossing at Clatterton', 230)}
<p>The distances by the two roads are as follows:</p>
{table([['<i>Bowbridge / Clatterton</i>', '35 miles', '30 miles'], ['<i>Clatterton / Downland</i>', '35 miles', '20 miles']],
       head=['', '<i>Motorway</i>', '<i>Buttercup Way</i>'])}
<p class="stem">If I take the {hl('fastest route', 'b', 4)}, what will be the time saving over the {hl('slowest route', 'b', 5)}?</p>""",
    options={'A': '5 min', 'B': '10 min', 'C': '15 min', 'D': '20 min', 'E': '30 min'},
    notes=[(1, 'g', '60 mph = 1 mile a minute. Miles = minutes!'),
           (2, 'g', '40 mph = 2 miles every 3 minutes, so 1.5 minutes per mile.'),
           (3, 'y', 'You can swap roads half way, so there are <b>4</b> routes, not 2.'),
           (4, 'b', 'Best choice on each leg.'),
           (5, 'b', 'Worst choice on each leg.')],
    steps=[
        f"""<p>Time for each leg on each road:</p>
{calc('motorway: 35 miles at 60 mph = <b>35 min</b> (both legs)',
      'Buttercup, leg 1: 30 miles × 1.5 = <b>45 min</b>',
      'Buttercup, leg 2: 20 miles × 1.5 = <b>30 min</b>')}""",
        f"""{_routes()}""",
        f"""<p>All four routes:</p>
{calc('motorway + motorway = 35 + 35 = 70 min',
      f'motorway + Buttercup = 35 + 30 = <b>65 min</b> {ar("green")} fastest',
      f'Buttercup + motorway = 45 + 35 = <b>80 min</b> {ar()} slowest',
      'Buttercup + Buttercup = 45 + 30 = 75 min',
      f'saving = 80 − 65 = {boxed("15 min")}')}""",
    ],
    answer_text='15 minutes: 65 minutes (motorway then Buttercup Way) against 80 minutes (the other way round).',
    why={'A': '5 min compares only all-motorway (70) with all-Buttercup (75), forgetting you can switch at Clatterton.',
         'B': '10 min compares the fastest route with all-Buttercup (75), or all-motorway with the slowest (80). It misses one of the mixed routes.',
         'D': '20 min is the difference in <b>miles</b> (70 miles all-motorway against 50 miles all-Buttercup), not in time.',
         'E': '30 min is just the time for the 20-mile stretch of Buttercup Way, not a saving.'},
    fast='Leg 1: 35 v 45, leg 2: 35 v 30. Best minus worst = (45 − 35) + (35 − 30) = 10 + 5 = 15.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _made():
    parts, lab = [], []
    # D: a corner cut off
    parts += [rect(30, 40, 90, 90, k='ink', sw=2),
              poly([(145, 75), (225, 155), (145, 235), (65, 155)], k='pen', sw=2),
              poly([(120, 100), (120, 130), (90, 130)], k='ink', fill='y', sw=2.2)]
    lab.append(text(120, 262, 'D: corner cut off', k='ink', size=16))
    # C: corner over corner
    ox = 210
    parts += [rect(ox + 30, 40, 100, 100, k='ink', sw=2),
              poly([(ox + 95, 105), (ox + 181.6, 155), (ox + 131.6, 241.6), (ox + 45, 191.6)], k='pen', sw=2),
              poly([(ox + 95, 105), (ox + 130, 125.2), (ox + 130, 140), (ox + 74.8, 140)], k='ink', fill='y', sw=2.2)]
    lab.append(text(ox + 105, 262, 'C: corner over corner', k='ink', size=16))
    # A: one square turned
    ox = 430
    parts += [rect(ox + 30, 60, 100, 100, k='ink', sw=2),
              poly([(ox + 80, 39.3), (ox + 150.7, 110), (ox + 80, 180.7), (ox + 9.3, 110)], k='pen', sw=2),
              poly([(ox + 100.7, 60), (ox + 130, 89.3), (ox + 130, 130.7), (ox + 100.7, 160), (ox + 59.3, 160), (ox + 30, 130.7),
                    (ox + 30, 89.3), (ox + 59.3, 60)], k='ink', fill='y', sw=2.2)]
    lab.append(text(ox + 80, 262, 'A: one square turned', k='ink', size=16))
    return svg(620, 276, rough(*parts) + ''.join(lab),
               'Three ways two squares can overlap: a corner cut off gives a right-angled triangle, two corners overlapping give a four-sided shape, one square turned on another gives an octagon')


def _para():
    DX = 190
    sq = [(DX + 113.3, 57.5), (DX + 222.5, 93.3), (DX + 186.7, 202.5), (DX + 77.5, 166.7)]
    corners = [(DX + 119, 40), (DX + 240, 40), (DX + 181, 220), (DX + 60, 220)]
    pts = ' '.join(f'{x},{y}' for x, y in sq)
    parts = [poly(corners, k='ink', fill='p', sw=2.4),
             f'<polygon points="{pts}" class="k-red f-g" stroke-width="2.6" stroke-dasharray="8 6"/>',
             poly(corners, k='ink', sw=2.4),
             line(DX + 95.4, 112.1, DX + 204.6, 147.9, k='red', w=2.2, tail=True, head=True),
             line(DX + 40.7, 213.6, DX + 99.7, 33.6, k='pen', w=2.2, tail=True, head=True)]
    lab = [text(DX + 44, 112, 'slanting', k='pen', size=17, anchor='end'),
           text(DX + 44, 132, 'side: long', k='pen', size=17, anchor='end'),
           text(DX + 238, 150, 'gap between', k='red', size=17, anchor='start'),
           text(DX + 238, 170, 'them: short', k='red', size=17, anchor='start'),
           text(DX + 238, 192, '(= the square’s side)', k='red', size=15, anchor='start'),
           text(DX + 238, 56, '← sticks out', k='red', size=17, anchor='start'),
           text(DX + 196, 238, 'sticks out', k='red', size=17, anchor='start'),
           text(DX + 140, 264, 'green = inside that square, pink = outside it', k='ink', size=16)]
    return svg(640, 276, rough(*parts) + ''.join(lab),
               'Parallelogram B with the only square that could give its slanting sides shaded green; the pink ends of B stick out of that square')


Q.append(dict(
    n=12, orig=25, answer='B', topic='Shapes & overlaps',
    question=f"""<p>Various shapes may be made by {hl('overlapping two transparent squares', 'y', 1)}, for example the
{hl('dark shaded hexagon', 'y', 2)} shown below:</p>
{fig(Y, 'ps_q12_example', 'A square and a tilted square overlapping; the shared region is shaded', 170)}
<p class="stem">Which one of the following shapes {hl('cannot', 'b', 3)} be made as the overlap of two transparent
squares?</p>
{fig(Y, 'ps_q12_opts', 'Five grey shapes: A an eight-sided shape, B a slanted parallelogram, C a small four-sided shape, D a triangle, E a five-sided shape', 440)}""",
    options={'A': 'shape A', 'B': 'shape B', 'C': 'shape C', 'D': 'shape D', 'E': 'shape E'},
    notes=[(1, 'y', 'Every edge of the overlap is part of an edge of one of the two squares.'),
           (2, 'y', 'Count the sides: 6, though one is very short (on the left edge). Overlaps can have lots of sides.'),
           (3, 'b', 'Four shapes can be made. Find the impossible one.')],
    steps=[
        f"""<p>Two facts about the overlap of two squares:</p>
<ul><li>Its sides lie along the squares’ sides. Each square’s sides point in only <b>2 directions</b>, at right angles.</li>
<li>Each corner is either a corner of a square (a <b>right angle</b>) or a point where the two squares’ edges cross.</li></ul>
<p>A, C, D and E are all easy to build:</p>{_made()}
<p>E is the same idea as C, with one square’s corner poking a bit further in, giving 5 sides.</p>""",
        f"""<p>Now B. It has <b>no right angles</b> and two pairs of parallel sides. Parallel sides from the two different
squares would make the squares line up, giving a rectangle. So the two slanting sides must be <b>opposite sides of one
square</b>, and the two flat sides opposite sides of the other.</p>""",
        f"""<p>But a square is as long as it is wide. B’s slanting sides are much longer than the gap between them, so they can’t
both fit on one square:</p>{_para()}
{calc(f'cannot be made = {boxed("B")}')}
{note('This works for any slanted parallelogram: at least one pair of sides is always longer than the gap between them. Only rectangles (and squares) can be made.', 'check')}""",
    ],
    answer_text='Shape B: a slanted parallelogram can’t be the overlap of two squares.',
    why={'A': 'Possible: put one square on top of the other with the same middle and turn it. The overlap has 8 sides, like A.',
         'C': 'Possible: two squares overlapping corner to corner give a 4-sided shape with two right angles, like C.',
         'D': 'Possible: one straight edge of a square cutting off the corner of the other gives a right-angled triangle, like D.',
         'E': 'Possible: like C, but with one corner reaching further in, so you get 5 sides with two right angles.'},
    fast='B’s two slanting sides are parallel, so they would have to be opposite sides of one square. But they are far longer than the gap between them, and a square is as long as it is wide.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _households():
    X = lambda p: 120 + p * 7
    parts, lab = [], []
    for y, yr, a, b in ((40, '1971', 18, 32), (120, '1991', 27, 34)):
        parts.append(rect(X(0), y, X(a) - X(0), 38, k='ink', fill='b', sw=1.8))
        parts.append(rect(X(a), y, X(a + b) - X(a), 38, k='ink', fill='g', sw=1.8))
        lab += [text(108, y + 25, yr, k='ink', size=19, anchor='end'),
                text((X(0) + X(a)) / 2, y + 25, f'1 person: {a}', k='ink', size=15),
                text(X(a) + 12, y + 25, f'2 people: {b}', k='ink', size=15, anchor='start'),
                text(X(a + b) + 10, y + 25, f'= {a + b}%', k='pen', size=20, font='scrawl', anchor='start')]
    parts.append(line(X(50), 84, X(50), 168, k='red', w=1.8, dash=True))
    parts.append(line(X(50), 178, X(61), 178, k='red', w=2.2, tail=True, head=True))
    lab.append(text((X(50) + X(61)) / 2, 202, 'up 11', k='red', size=20, font='scrawl'))
    return svg(620, 214, rough(*parts) + ''.join(lab),
               'Bars of households with fewer than 3 people: 18 plus 32 makes 50 percent in 1971, 27 plus 34 makes 61 percent in 1991')


Q.append(dict(
    n=13, orig=26, answer='D', topic='Reading tables',
    question=f"""<p>This table shows how household sizes in Great Britain changed between 1961 and 1991.</p>
<p style="text-align:center;margin:0"><i>Percentages</i></p>
{table([['<i>Household size</i>', '', '', '', ''],
        [hl('<i>1 person</i>', 'g'), '14', hl('18', 'g'), '22', hl('27', 'g')],
        [hl('<i>2 people</i>', 'g'), '30', hl('32', 'g'), '32', hl('34', 'g')],
        ['<i>3 people</i>', '23', '19', '17', '16'], ['<i>4 people</i>', '18', '17', '18', '16'],
        ['<i>5 people</i>', '9', '8', '7', '5'], ['<i>6 or more people</i>', '7', '6', '4', '2'], ['', '', '', '', ''],
        [hl('<i>Total number of households (millions)</i>', 'p', 3), '16.2', '18.2', '19.5', '21.9'],
        ['<i>Average household size (number of people)</i>', '3.1', '2.9', '2.7', '2.5']],
       head=['', '<i>1961</i>', hl('<i>1971</i>', 'g', 2), '<i>1981</i>', hl('<i>1991</i>', 'g')])}
<p class="stem">What was the change in the percentage of households with {hl('fewer than 3 people', 'y', 1)} between
1971 and 1991?</p>""",
    options={'A': '7', 'B': '8', 'C': '10', 'D': '11', 'E': '17'},
    notes=[(1, 'y', 'Fewer than 3 = <b>1 person + 2 people</b>. Not 3!'),
           (2, 'g', 'Only the 1971 and 1991 columns. 1961 and 1981 are there to tempt you.'),
           (3, 'p', 'Red herring: the question asks about percentages, so the millions aren’t needed.')],
    steps=[
        f"""<p>Add the 1-person and 2-person rows in each year:</p>
{calc('1971: 18 + 32 = <b>50%</b>', '1991: 27 + 34 = <b>61%</b>')}""",
        f"""{_households()}
{calc(f'change = 61 − 50 = {boxed("11")}')}""",
    ],
    answer_text='11 (from 50% to 61%).',
    why={'A': '7 uses 1981 instead of 1971 (54% up to 61%).',
         'B': '8 wrongly includes 3-person households (69% up to 77%).',
         'C': '10 uses the wrong years, for example 1961 to 1981 (44% up to 54%).',
         'E': '17 starts from 1961 (44%) instead of 1971.'},
    fast='(27 + 34) − (18 + 32) = 61 − 50 = 11.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _united():
    games = [('United 0 – 1 Rovers', 'lost', 'p', 'Rovers won every game'),
             ('United 0 – 0 County', 'drew', 'y', 'County is in both draws'),
             ('United 1 – 0 Wanderers', 'won', 'g', 'clean sheet'),
             ('United 1 – 0 City', 'won', 'g', 'clean sheet')]
    parts, lab = [], []
    for i, (score, res, f, why) in enumerate(games):
        x, y = 20 + (i % 2) * 300, 26 + (i // 2) * 80
        parts.append(rect(x, y, 280, 56, k='ink', fill=f, sw=1.8, rx=8))
        lab.append(text(x + 14, y + 25, score, k='ink', size=18, anchor='start', font='print'))
        lab.append(text(x + 14, y + 47, res + (f': {why}' if why else ''), k='ink', size=15, anchor='start'))
    lab += [text(160, 210, 'goals for: 0 + 0 + 1 + 1 = 2 ✓', k='pen', size=17), text(460, 210, 'goals against: 1 + 0 + 0 + 0 = 1 ✓', k='pen', size=17)]
    return svg(620, 226, rough(*parts) + ''.join(lab),
               'United’s four games: lost 0-1 to Rovers, drew 0-0 with County, beat Wanderers and City 1-0; this gives 2 goals for and 1 against')


Q.append(dict(
    n=14, orig=30, answer='A', topic='Logic & league tables',
    question=f"""<p>All the teams in a local football league have now {hl('played each other once', 'y', 1)} this
season. Below is the current league table:</p>
{table([[hl('Rovers', 'g', 2), '4', hl('4', 'g'), '0', '0', '7', '2'],
        ['United', '4', '2', '1', '1', '2', hl('1', 'g', 3)],
        ['County', '4', '1', hl('2', 'y', 4), '1', '4', '4'],
        ['Wanderers', '4', '1', '0', '3', '3', '5'],
        ['City', '4', '0', '1', '3', '1', '5']],
       head=['', '<i>Played</i>', '<i>Won</i>', '<i>Drawn</i>', '<i>Lost</i>', '<i>Goals For</i>', '<i>Goals Against</i>'])}
<p class="stem">What was the result of the match {hl('between United and County', 'b', 5)}?</p>""",
    options={'A': 'United 0 County 0', 'B': 'United 1 County 0', 'C': 'United 0 County 1', 'D': 'United 1 County 1', 'E': 'United 2 County 1'},
    notes=[(1, 'y', '5 teams, each played the other 4 exactly once.'),
           (2, 'g', 'Rovers won all 4, so Rovers beat United.'),
           (3, 'g', 'United let in only <b>1 goal</b> all season.'),
           (4, 'y', 'County drew <b>2</b> games.'),
           (5, 'b', 'Work out United’s games one by one.')],
    steps=[
        f"""<p>Rovers won every game, so <b>United lost to Rovers</b>. That is United’s one defeat.</p>""",
        f"""<p>United only let in <b>1 goal</b> all season, and you can’t lose without letting one in. So they lost 0–1 to Rovers,
and kept a clean sheet in all their other games. Their draw must have been <b>0–0</b>.</p>""",
        f"""<p>Who was that draw against? Count the draws in the table: United 1, County 2, City 1.</p>
{calc(f'each drawn game gives 2 teams a draw {ar()} (1 + 2 + 1) ÷ 2 = 2 drawn games',
      f'County drew 2, so County is in <b>both</b> {ar()} County v United and County v City')}
{_united()}
{calc(f'United v County = {boxed("0 – 0")}')}""",
    ],
    answer_text='United 0 County 0.',
    why={'B': 'A United win over County is impossible: County is in both drawn games, so United v County was a draw.',
         'C': 'United’s only defeat was against Rovers, who won every match.',
         'D': '1–1 would mean United let in a goal against County as well as against Rovers: 2 against, but the table says 1.',
         'E': 'This is a United win (it was a draw) and it gives United 2 goals against (the table says 1).'},
    fast='United lost to Rovers and only conceded once, so every other United game was a clean sheet: their one draw was 0–0, and County is in both draws.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _grid(ox, oy, s, marks, ring=None, shade=(), nums=None, mark_cols=None):
    parts, lab = [], []
    for (r, c) in shade:
        parts.append(rect(ox + c * s, oy + r * s, s, s, k='muted', fill='p', sw=0.1))
    for i in range(4):
        parts.append(line(ox, oy + i * s, ox + 3 * s, oy + i * s, k='ink', w=2))
        parts.append(line(ox + i * s, oy, ox + i * s, oy + 3 * s, k='ink', w=2))
    for (r, c), m in marks.items():
        cx, cy, d = ox + c * s + s / 2, oy + r * s + s / 2, s * 0.26
        col = (mark_cols or {}).get((r, c), 'ink')
        if m == 'X':
            parts += [line(cx - d, cy - d, cx + d, cy + d, k=col, w=2.6), line(cx - d, cy + d, cx + d, cy - d, k=col, w=2.6)]
        else:
            parts.append(circle(cx, cy, d * 1.15, k=col, sw=2.6))
    if ring:
        r, c = ring
        parts.append(circle(ox + c * s + s / 2, oy + r * s + s / 2, s * 0.46, k='green', sw=2.4))
    if nums:
        for (r, c), n in nums.items():
            lab.append(text(ox + c * s + s / 2, oy + r * s + s / 2 + 8, n, k='red', size=24, font='scrawl'))
    return parts, lab


def _ttt_c():
    blanks = {(0, 0): 1, (0, 2): 2, (1, 1): 3, (1, 2): 4, (2, 0): 5, (2, 1): 6}
    p, l = _grid(40, 24, 72, {(0, 1): 'X', (1, 0): 'X', (2, 2): 'O'}, shade=list(blanks), nums=blanks,
                 mark_cols={(2, 2): 'orange'})
    l += [text(300, 60, 'C: O in the far corner', k='orange', size=20, font='scrawl', anchor='start'),
          text(300, 96, 'every blank square (pink) is', k='ink', size=16, anchor='start'),
          text(300, 118, 'on a line with one lonely X', k='pen', size=16, anchor='start'),
          text(300, 140, 'AND on a line with one lonely O', k='orange', size=16, anchor='start'),
          text(300, 180, 'so wherever the opponent goes,', k='ink', size=16, anchor='start'),
          text(300, 202, 'X or O, she makes a pair', k='ink', size=16, anchor='start'),
          text(300, 224, 'for you to finish!', k='red', size=18, font='scrawl', anchor='start')]
    return svg(600, 256, rough(*p) + ''.join(l), 'Grid C with the six blank squares numbered 1 to 6 and shaded as traps for the opponent')


def _ttt_replies():
    cases = [('A', {(0, 0): 'O', (0, 1): 'X', (1, 0): 'X'}, (0, 2), 'X', 'X top right'),
             ('B', {(0, 1): 'X', (1, 0): 'X', (1, 1): 'O'}, (2, 2), 'X', 'X bottom right'),
             ('D', {(0, 1): 'X', (1, 0): 'X', (2, 2): 'X'}, (1, 1), 'O', 'O in the middle'),
             ('E', {(0, 1): 'X', (1, 0): 'X', (0, 2): 'O'}, (2, 2), 'X', 'X bottom right')]
    P, L = [], []
    for i, (name, marks, reply, sym, desc) in enumerate(cases):
        ox = 24 + i * 150
        m = dict(marks)
        m[reply] = sym
        p, l = _grid(ox, 40, 38, m, ring=reply, mark_cols={reply: 'green'})
        P += p
        L += l
        L.append(text(ox + 57, 28, name, k='ink', size=19, font='print', weight='700'))
        L.append(text(ox + 57, 182, desc, k='green', size=15))
    L.append(text(300, 212, 'safe replies (green): no line has two the same, so no sure win', k='red', size=17))
    return svg(620, 224, rough(*P) + ''.join(L), 'For A, B, D and E the opponent has a safe reply, ringed in green, that leaves no pair anywhere')


Q.append(dict(
    n=15, orig=31, answer='C', topic='Logic games',
    question=f"""<p>In a modified form of a popular game, each of two players at any turn may put {hl("either 'O' or 'X' as she chooses", 'y', 1)} in any blank square of a 3 by 3 grid. She wins if she thereby
{hl('completes a line of three identical symbols', 'y', 2)}. A player is faced with this situation:</p>
{fig(Y, 'ps_q15_grid', 'A 3 by 3 grid with an X in the top middle square and an X in the middle left square', 110)}
<p class="stem">Which one of the following moves {hl('ensures that she can win at her next move', 'b', 3)}?</p>
{fig(Y, 'ps_q15_opts', 'Five grids A to E, each adding one symbol: A an O top left, B an O in the centre, C an O bottom right, D an X bottom right, E an O top right', 400)}""",
    options={'A': 'grid A', 'B': 'grid B', 'C': 'grid C', 'D': 'grid D', 'E': 'grid E'},
    notes=[(1, 'y', 'Both players can use both symbols. So a line with two the same and a gap is a win for <b>whoever moves next</b>.'),
           (2, 'y', 'Three Xs or three Os in a row, column or diagonal.'),
           (3, 'b', 'After her move the opponent plays. Whatever they do, she must then be able to win.')],
    steps=[
        f"""<p>Two things her move must do:</p>
<ul><li>Leave <b>no</b> line with two the same, or the opponent just wins.</li>
<li>Make every square the opponent could pick a trap: whichever symbol they put there must create a pair for her.</li></ul>""",
        f"""<p>Try C (O in the bottom right):</p>{_ttt_c()}
{calc('square 1: X makes X X _ along the top; O makes O _ O down the diagonal',
      'square 2: X makes _ X X along the top; O makes O _ O down the right side',
      'square 3: X makes X X _ across the middle; O makes _ O O down the diagonal',
      'square 4: X makes X _ X across the middle; O makes _ O O down the right side',
      'square 5: X makes _ X X down the left side; O makes O _ O along the bottom',
      'square 6: X makes X _ X down the middle; O makes _ O O along the bottom')}
<p>Every reply hands her a winning line. {tick()}</p>""",
        f"""<p>The other moves all leave the opponent a safe reply:</p>{_ttt_replies()}
{calc(f'only C forces a win = {boxed("C")}')}""",
    ],
    answer_text='C: O in the bottom-right corner turns every blank square into a trap.',
    why={'A': 'After O top left, the opponent puts X top right. No line then has two the same, so she has no winning move.',
         'B': 'After O in the middle, the opponent puts X bottom right. No pairs anywhere.',
         'D': 'After X bottom right, the opponent puts O in the middle, blocking both X lines through it and making no pair.',
         'E': 'After O top right, the opponent puts X bottom right. Again, no pairs.'},
    fast='She needs every blank to sit on a line with a lone X and on a line with a lone O. An O in the corner far from the two Xs (C) does exactly that.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _quit():
    X = lambda n: 120 + n * 4
    parts, lab = [], []
    rows = [(40, 'placebo', [(24, 'b', 'quit 24'), (96, 'p', 'failed 96')]),
            (120, 'nicotine', [(24, 'b', '24'), (32, 'g', '32'), (64, 'p', 'failed 64')])]
    for y, name, segs in rows:
        run = 0
        for n, f, t in segs:
            parts.append(rect(X(run), y, X(run + n) - X(run), 38, k='ink', fill=f, sw=1.8))
            lab.append(text((X(run) + X(run + n)) / 2, y + 25, t, k='ink', size=16))
            run += n
        lab.append(text(108, y + 25, name, k='ink', size=17, anchor='end'))
    parts.append(line(X(24), 30, X(24), 168, k='pen', w=2, dash=True))
    lab += [text(X(12), 186, 'would have', k='pen', size=15), text(X(12), 204, 'quit anyway', k='pen', size=15),
            text(X(40), 186, 'quit thanks', k='green', size=15), text(X(40), 204, 'to the tablets', k='green', size=15),
            text(X(24) + 6, 24, 'same 1 in 5 in both groups', k='pen', size=15, anchor='start')]
    return svg(620, 214, rough(*parts) + ''.join(lab),
               'Two bars of 120 people: placebo has 24 quitters; nicotine has 24 who would have quit anyway plus 32 who quit because of the tablets')


Q.append(dict(
    n=16, orig=32, answer='B', topic='Proportion',
    question=f"""<p>The following table shows the results of a test on smokers trying to quit. Of 240 people,
{hl('half were given nicotine tablets and half were given a placebo', 'g', 1)} (a substance containing no
medication).</p>
{table([['<i>Nicotine</i>', '64', hl('56', 'g'), '<b>120</b>'], ['<i>Placebo</i>', '96', hl('24', 'g'), '<b>120</b>'],
        ['<i>Total</i>', '<b>160</b>', '<b>80</b>', '<b>240</b>']],
       head=['', '<i>Failed to quit</i>', '<i>Succeeded in quitting</i>', '<i>Total</i>'])}
<p>The researchers assumed that: of the smokers given nicotine tablets, {hl('the same proportion would have quit without using them as would have quit using the placebo', 'y', 2)}.</p>
<p class="stem">How many of the smokers that were given the nicotine tablets can the researchers
conclude {hl('had quit due to taking the tablets', 'b', 3)}?</p>""",
    options={'A': '16', 'B': '32', 'C': '39', 'D': '40', 'E': '45'},
    notes=[(1, 'g', '120 people in each group: a fair comparison.'),
           (2, 'y', 'The placebo group shows how many quit with no medicine at all.'),
           (3, 'b', 'Only the extra quitters, above the “would have quit anyway” number.')],
    steps=[
        f"""<p>How many quit with no medicine? Look at the placebo group:</p>
{calc(f'24 out of 120 quit = {frac(1, 5)} (20%)')}""",
        f"""<p>The nicotine group is also 120 people, so the same {frac(1, 5)} of them would have quit anyway:</p>
{calc(f'{frac(1, 5)} of 120 = 24 would have quit anyway', f'56 quit on the tablets {ar()} 56 − 24 = {boxed("32")} thanks to the tablets')}
{_quit()}""",
    ],
    answer_text='32: 56 quit on the tablets, and 24 of them would have quit anyway.',
    why={'A': '16 = 56 − 40, which splits all 80 quitters evenly between the groups. That ignores what the placebo group tells us.',
         'C': '39 takes 30% off the 56 (because 24 is 30% of the 80 quitters). The right rate is 24 out of 120 people.',
         'D': '40 is half of all 80 quitters. It has nothing to do with the tablets’ effect.',
         'E': '45 takes 20% of the 56 quitters (about 11) away, instead of 20% of all 120 people on tablets.'},
    fast='Placebo: 24 of 120 quit anyway. Same-size group, so 24 of the 56 nicotine quitters would have quit anyway: 56 − 24 = 32.',
))


# ---------------------------------------------------------------- 17 (Q36)
def _pizza():
    parts, lab = [], []
    cols = [('mini', 1, '£2'), ('regular', 2, '£3'), ('large', 4, '£5')]
    base, bh = 250, 34
    for i, (name, n, price) in enumerate(cols):
        x = 60 + i * 170
        parts.append(rect(x, base - bh, 90, bh, k='ink', fill='v', sw=1.8))
        lab.append(text(x + 45, base - 11, 'fixed', k='ink', size=15))
        for j in range(n):
            parts.append(rect(x, base - bh * (j + 2), 90, bh, k='ink', fill='o', sw=1.8))
            lab.append(text(x + 45, base - bh * (j + 1) - 11, '1 lot', k='ink', size=15))
        lab.append(text(x + 45, base + 24, name, k='ink', size=18))
        lab.append(text(x + 45, base - bh * (n + 1) - 12, price, k='pen', size=24, font='scrawl'))
    parts.append(arrow(152, 170, 228, 150, k='red', bend=-0.2))
    parts.append(arrow(322, 140, 398, 84, k='red', bend=-0.2))
    lab += [text(190, 132, '+1 lot', k='red', size=17), text(352, 80, '+2 lots', k='red', size=17),
            text(504, 124, 'second jump', k='red', size=16, anchor='start'), text(504, 146, '= 2 × first jump', k='red', size=16, anchor='start')]
    return svg(630, 284, rough(*parts) + ''.join(lab),
               'Block columns: mini is the fixed amount plus 1 lot, regular plus 2 lots, large plus 4 lots; with option E each block is 1 pound, giving 2, 3 and 5 pounds')


Q.append(dict(
    n=17, orig=36, answer='E', topic='Patterns in prices',
    question=f"""<p>When my father ran a pizza shop he sold pizzas for {hl('a fixed amount plus an amount proportional to the ingredients used', 'y', 1)}. A regular pizza uses {hl('twice the ingredients of a mini one', 'g', 2)} and a large pizza {hl('twice those of a regular one', 'g', 3)}.</p>
<p class="stem">Which one of the following price scales could he have used for mini, regular and large
pizzas?</p>""",
    options={'A': '£0.49, £1.00, £1.96', 'B': '£1.00, £2.00, £3.00', 'C': '£1.10, £2.20, £3.30', 'D': '£1.70, £2.00, £2.40',
             'E': '£2.00, £3.00, £5.00'},
    notes=[(1, 'y', 'Price = fixed part + (ingredients × a rate). The fixed part is the same for every size.'),
           (2, 'g', 'Mini = 1 lot of ingredients, regular = 2 lots.'),
           (3, 'g', 'Large = 2 × 2 = <b>4</b> lots.')],
    steps=[
        f"""<p>Call one lot of ingredients a “block”:</p>
{calc('mini = fixed + 1 block', 'regular = fixed + 2 blocks', 'large = fixed + 4 blocks')}
<p>So mini → regular adds <b>1 block</b>, and regular → large adds <b>2 blocks</b>. The second price jump must be exactly
<b>double</b> the first.</p>""",
        f"""<p>Check the jumps in each option:</p>
{calc(f'A: +0.51, then +0.96 {cross()} (double would be +1.02)', f'B: +1.00, then +1.00 {cross()}',
      f'C: +1.10, then +1.10 {cross()}', f'D: +0.30, then +0.40 {cross()}', f'E: +1.00, then +2.00 {tick()}')}""",
        f"""<p>E works with a block costing £1 and a fixed amount of £1:</p>{_pizza()}
{calc(f'£1 + £1 = £2, £1 + £2 = £3, £1 + £4 = £5 {ar()} {boxed("E")}')}""",
    ],
    answer_text='£2.00, £3.00, £5.00: a fixed £1 plus £1 for each lot of ingredients (1, 2 and 4 lots).',
    why={'A': 'The jumps are 51p then 96p, not double. The fixed part would also have to be negative (49p − 51p).',
         'B': 'Equal jumps of £1 would mean a large uses 3 lots of ingredients, not 4.',
         'C': 'Equal jumps again, and no fixed part at all (just £1.10 a lot for 1, 2 and 3 lots).',
         'D': 'The jumps are 30p then 40p. The second must be double the first.'},
    fast='Second jump must be twice the first. Only E: +£1, then +£2.',
))
