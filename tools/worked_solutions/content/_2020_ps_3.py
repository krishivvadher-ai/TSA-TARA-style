import math
from wslib import *
from _2020_ps_1 import _tk, _cx

Y = 2020
Q = []


# ---------------------------------------------------------------- 17 (Q36)
def _patio():
    s, x0, y0 = 0.28, 44, 30
    b = 25 * s
    W, H = 1250 * s, 1050 * s
    parts, lab = [], []
    # brick border: top and bottom rows run the full width, sides fit between the corners
    for i in range(50):
        f = 'o' if i in (0, 49) else 'y'
        parts.append(rect(x0 + i * b, y0, b, b, k='ink', fill=f, sw=0.8))
        parts.append(rect(x0 + i * b, y0 + H - b, b, b, k='ink', fill=f, sw=0.8))
    for j in range(1, 41):
        parts.append(rect(x0, y0 + j * b, b, b, k='ink', fill='b', sw=0.8))
        parts.append(rect(x0 + W - b, y0 + j * b, b, b, k='ink', fill='b', sw=0.8))
    # slab grid inside: 40 across (30 cm) by 50 down (20 cm)
    ix, iy, iw, ih = x0 + b, y0 + b, W - 2 * b, H - 2 * b
    grid = [rect(ix, iy, iw, ih, k='ink', fill='paper', sw=1.4)]
    for i in range(1, 40):
        grid.append(line(ix + i * 30 * s, iy, ix + i * 30 * s, iy + ih, k='muted', w=0.5))
    for j in range(1, 50):
        grid.append(line(ix, iy + j * 20 * s, ix + iw, iy + j * 20 * s, k='muted', w=0.5))
    lab.append(brace(ix, ix + iw, y0 + H + 4, '1200 cm ÷ 30 = 40 slabs', k='pen', size=16))
    lab.append(text(x0 - 12, iy + ih / 2, '1000 cm ÷ 20 = 50 slabs', k='pen', size=16, rotate=-90))
    tx = 420
    lab += [text(tx, 54, 'Bricks (25 cm squares):', k='ink', size=18, font='scrawl', anchor='start'),
            text(tx, 84, 'top row: 1250 ÷ 25 = 50', k='ink', size=16, anchor='start'),
            text(tx, 108, 'bottom row: 50', k='ink', size=16, anchor='start'),
            text(tx, 138, 'each side: 1050 ÷ 25 = 42,', k='ink', size=16, anchor='start'),
            text(tx, 160, 'minus the 2 corners = 40', k='orange', size=16, anchor='start'),
            text(tx, 192, '50 + 50 + 40 + 40 = 180', k='red', size=18, anchor='start'),
            text(tx, 236, 'Slabs:', k='ink', size=18, font='scrawl', anchor='start'),
            text(tx, 262, '40 × 50 = 2000', k='pen', size=18, anchor='start'),
            text(tx, 306, 'total = 2180', k='green', size=24, font='scrawl', anchor='start'),
            text(tx, 330, 'orange = corner bricks', k='orange', size=14, anchor='start')]
    return svg(660, 380, rough(*parts) + ''.join(grid) + ''.join(lab),
               'Scale drawing of the patio: 50 bricks along the top and bottom, 40 down each side, and a 40 by 50 grid of slabs inside')


Q.append(dict(
    n=17, orig=36, answer='B', topic='Area & tiling',
    question=f"""{fig(Y, 'ps_q17_patio', 'A rectangle 12.5 metres by 10.5 metres with a grey border all the way round', 260)}
<p>The whole of my garden is a patio, which is {hl('12.5 by 10.5 metres', 'g', 1)}. I intend to resurface my patio. I would like my patio to include a {hl('25 cm border of bricks', 'y', 2)} and the remainder of the patio inside the border to be covered with paving slabs.</p>
<p>The bricks I will use for the border are {hl('25 cm x 25 cm', 'g', 3)} and the paving slabs I will use for the remainder are {hl('30 cm x 20 cm', 'g', 4)}.</p>
<p class="stem">What is the {hl('total number of bricks and paving slabs', 'b', 5)} that I will need for my patio?</p>""",
    options={'A': '2000', 'B': '2180', 'C': '2184', 'D': '2268', 'E': '2272'},
    notes=[(1, 'g', 'Work in cm: 1250 cm by 1050 cm.'),
           (2, 'y', 'The border is exactly one brick wide all the way round.'),
           (3, 'g', 'Each brick is one 25 cm square.'),
           (4, 'g', 'Slab = 30 cm by 20 cm. Check they fit the inside exactly.'),
           (5, 'b', 'Add bricks and slabs together.')],
    steps=[
        f"""<p>Draw it to scale and count the bricks. The top and bottom rows run the full length; the sides fit <b>between</b> the corners:</p>{_patio()}""",
        f"""<p>The inside is 25 cm smaller at each edge, so 50 cm smaller each way:</p>
{calc('1250 − 50 = 1200 cm and 1050 − 50 = 1000 cm', '1200 ÷ 30 = 40 slabs across, 1000 ÷ 20 = 50 slabs down', '40 × 50 = <b>2000 slabs</b> (they fit exactly)')}""",
        f"""{calc('bricks: 50 + 50 + 40 + 40 = <b>180</b>', f'total = 180 + 2000 = {boxed("2180")}')}
{note('Area check for the bricks: 1250 × 1050 − 1200 × 1000 = 1 312 500 − 1 200 000 = 112 500 cm². One brick is 625 cm², and 112 500 ÷ 625 = 180 ✓', 'check')}""",
    ],
    answer_text='2180: 180 bricks round the edge and 2000 slabs inside.',
    why={'A': '2000 is just the slabs. The 180 bricks are forgotten.',
         'C': 'Counts every corner brick twice: 2 × 50 + 2 × 42 = 184 bricks.',
         'D': 'Has 88 slabs too many: the inside is exactly 40 by 50, so it takes exactly 2000 slabs.',
         'E': 'Counts the corners twice (184 bricks) and also has 88 slabs too many.'},
    fast='Inside 12 m × 10 m: 40 × 50 = 2000 slabs. Border: 50 + 50 + 40 + 40 = 180 bricks. 2180.',
))


# ---------------------------------------------------------------- 18 (Q37)
def _fruit_marm():
    years = list(range(2006, 2013))
    fruit = [10, 15, 15, 20, 25, 30, 35]
    marm = [5, 10, 15, 20, 25, 30, 35]
    X = lambda i: 116 + i * 76
    Yv = lambda v: 250 - v * 5
    parts, lab = [], []
    parts.append(line(80, Yv(0), 600, Yv(0), k='ink', w=2))
    parts.append(line(80, Yv(0), 80, Yv(40), k='ink', w=2))
    for v in (0, 10, 20, 30, 40):
        lab.append(text(72, Yv(v) + 5, f'{v}%', k='muted', size=14, anchor='end'))
        if v:
            parts.append(line(80, Yv(v), 600, Yv(v), k='muted', w=0.7, dash=True))
    for i, y in enumerate(years):
        lab.append(text(X(i), Yv(0) + 22, y, k='ink', size=14))
    parts.append(poly([(X(i), Yv(v)) for i, v in enumerate(fruit)], k='green', sw=3, closed=False))
    parts.append(poly([(X(i), Yv(v)) for i, v in enumerate(marm)], k='orange', sw=3, closed=False))
    for i in (0, 1):
        mid = Yv((fruit[i] + marm[i]) / 2)
        parts.append(f'<ellipse cx="{X(i)}" cy="{mid}" rx="15" ry="22" class="k-red f-none" stroke-width="2.2"/>')
        lab.append(text(X(i), Yv(fruit[i]) - 22, f'{fruit[i]} vs {marm[i]}', k='red', size=17, font='scrawl'))
    lab += [text(130, 92, 'green: fresh fruit (row 5)', k='green', size=17, anchor='start'),
            text(130, 116, 'orange: marmalade (row 2)', k='orange', size=17, anchor='start'),
            text(440, 176, 'the same from 2008 on', k='ink', size=16),
            text(90, 22, 'not equal in 2006 and 2007!', k='red', size=19, font='scrawl', anchor='start')]
    return svg(620, 284, rough(*parts) + ''.join(lab),
               'Line graph: fresh fruit 10, 15, 15, 20, 25, 30, 35 and marmalade 5, 10, 15, 20, 25, 30, 35; they differ in 2006 and 2007')


Q.append(dict(
    n=18, orig=37, answer='D', topic='Tables & percentages',
    question=f"""<p>The table below shows the popularity of different breakfasts served in a hotel from 2006 to 2012.</p>
{table([['bacon, egg, sausage and fried bread', '70%', '60%', '50%', '40%', '30%', '20%', '10%'],
        ['porridge, toast and marmalade', '5%', '10%', '15%', '20%', '25%', '30%', '35%'],
        ['toast and jam', '5%', '5%', '5%', '5%', '5%', '5%', '5%'],
        ['boiled egg and toast', '10%', '10%', '15%', '15%', '15%', '15%', '15%'],
        ['fresh fruit and cereals', '10%', '15%', '15%', '20%', '25%', '30%', '35%']],
       head=['<i>breakfasts</i>', '<i>2006</i>', '<i>2007</i>', '<i>2008</i>', '<i>2009</i>', '<i>2010</i>', '<i>2011</i>', '<i>2012</i>'])}
<p class="stem">From the figures in the table, which one of the following statements is <b>{hl('not', 'b', 1)}</b> true?</p>""",
    options={'A': 'Breakfasts of toast and jam have never been more popular than in 2006.',
             'B': f'The popularity of breakfasts that include porridge overtook the popularity of breakfasts that {hl("include eggs", "p", 2)} in 2012.',
             'C': 'The popularity of breakfasts that include porridge or cereals has gone up 10 percentage points, year on year, for the last four years shown in the table.',
             'D': f'In every year between 2006 and 2012, the popularity of breakfasts that include {hl("fresh fruit", "y", 4)} was the same as the popularity of breakfasts that include {hl("marmalade", "y")}.',
             'E': f'The popularity of breakfasts that {hl("include toast", "p", 3)} has increased year on year.'},
    notes=[(1, 'b', 'Four statements are true. Find the false one.'),
           (2, 'p', '“Include eggs” = <b>two</b> rows: bacon, egg… and boiled egg and toast.'),
           (3, 'p', '“Include toast” = <b>three</b> rows: porridge, toast…; toast and jam; boiled egg and toast. (Fried bread isn’t toast.)'),
           (4, 'y', 'Marmalade is in the porridge row, fruit is in the cereals row. Compare those two rows.')],
    steps=[
        f"""<p>Group the rows by ingredient and add them up:</p>
{table([['eggs (rows 1 + 4)', '80', '70', '65', '55', '45', hl('35', 'g'), hl('25', 'g')],
        ['porridge = marmalade (row 2)', '5', '10', '15', '20', '25', hl('30', 'g'), hl('35', 'g')],
        ['porridge or cereals (rows 2 + 5)', '15', '25', '30', '40', '50', '60', '70'],
        ['toast (rows 2 + 3 + 4)', '20', '25', '35', '40', '45', '50', '55'],
        ['fresh fruit (row 5)', hl('10', 'p'), hl('15', 'p'), '15', '20', '25', '30', '35']],
       head=['%', '2006', '2007', '2008', '2009', '2010', '2011', '2012'])}""",
        f"""<p>Fruit and marmalade only match from 2008:</p>{_fruit_marm()}
<p>So “in every year … the same” is false {ar()} {boxed('D')}</p>""",
        f"""<p>Check the rest really are true:</p>
{calc(f'A: toast and jam is 5% every year {tick()}', f'B: 2011 porridge 30 &lt; eggs 35; 2012 porridge 35 &gt; eggs 25 {tick()}',
      f'C: 30 → 40 → 50 → 60 → 70 (2008 to 2012) {tick()}', f'E: toast 20, 25, 35, 40, 45, 50, 55 {tick()}')}""",
    ],
    answer_text='D is not true: in 2006 fruit was 10% and marmalade 5%; in 2007 it was 15% against 10%.',
    why={'A': 'True: toast and jam is 5% every year, so it was never more popular than in 2006.',
         'B': 'True: eggs (two rows) 35% against porridge 30% in 2011, then 25% against 35% in 2012.',
         'C': 'True: porridge + cereals goes 30, 40, 50, 60, 70 from 2008 to 2012.',
         'E': 'True: the three toast rows add to 20, 25, 35, 40, 45, 50, 55, rising every year.'},
    fast='Fruit is row 5, marmalade row 2. In 2006: 10% against 5%. Not the same, so D is false.',
))


# ---------------------------------------------------------------- 19 (Q38)
def _pie(cx, cy, r, shares, fills, labels):
    parts, lab, a0 = [], [], -90.0
    for s_, f, l in zip(shares, fills, labels):
        a1 = a0 + 3.6 * s_
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        big = 1 if a1 - a0 > 180 else 0
        parts.append(path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z', k='ink', fill=f, sw=1.8))
        am = math.radians((a0 + a1) / 2)
        lr = r * 0.58 if s_ > 12 else r + 30
        lab.append(text(cx + lr * math.cos(am), cy + lr * math.sin(am) + 6, l, k='ink', size=16))
        a0 = a1
    return parts, lab


def _smoothie():
    p1, l1 = _pie(150, 172, 96, [70, 20, 10], ['y', 'o', 'g'], ['banana 70', 'orange 20', 'apple 10'])
    p2, l2 = _pie(480, 172, 96, [77, 18, 5], ['y', 'o', 'g'], ['banana 77', 'orange 18', 'apple 5'])
    lab = [text(60, 24, 'old recipe (%)', k='ink', size=18, font='scrawl'),
           text(590, 24, 'new recipe (%)', k='ink', size=18, font='scrawl'),
           text(315, 150, '+10% of 70', k='green', size=16), text(315, 170, '−10% of 20', k='red', size=16),
           text(315, 304, 'apple: 10 → 5, it halves!', k='pen', size=19, font='scrawl')]
    arrows = [arrow(268, 188, 362, 188, k='pen', bend=-0.2)]
    return svg(640, 316, rough(*p1, *p2, *arrows) + ''.join(l1 + l2 + lab),
               'Two pie charts: old recipe banana 70, orange 20, apple 10; new recipe banana 77, orange 18, apple 5')


Q.append(dict(
    n=19, orig=38, answer='B', topic='Percentages & pie charts',
    question=f"""<p>At a smoothie factory, a tropical smoothie mixture contains banana, orange and apple in the proportions shown in the pie chart below.</p>
{fig(Y, 'ps_q19_pie', 'Pie chart: banana about 70 percent, orange about 20 percent, apple about 10 percent', 130)}
<p>The chief taster requested a new recipe, in which {hl('every litre contained 10% more banana than was present in the original mixture', 'y', 1)}, and {hl('10% less orange than was present in the original mixture', 'y', 2)}. {hl('This change also affected the proportion of apple in the mixture.', 'p', 3)}</p>
<p class="stem">Which one of the following graphs shows the {hl('content of the new smoothie mixture', 'b', 4)}?</p>
{fig(Y, 'ps_q19_opts', 'Five pie charts A to E with different banana, orange and apple slices', 520)}""",
    options={'A': 'pie A', 'B': 'pie B', 'C': 'pie C', 'D': 'pie D', 'E': 'pie E'},
    notes=[(1, 'y', '10% <b>of the banana</b>, not 10 percentage points: 70% × 1.1 = 77%.'),
           (2, 'y', '10% of the orange: 20% × 0.9 = 18%.'),
           (3, 'p', 'Apple is whatever is left in the litre.'),
           (4, 'b', 'Each pie is one whole litre (100%).')],
    steps=[
        f"""<p>Read the original pie. Banana is a bit less than three quarters, orange about a fifth, apple a thin slice:</p>
{calc('banana ≈ 70%, orange ≈ 20%, apple ≈ 10%')}""",
        f"""<p>Apply the changes to each fruit’s own amount:</p>
{calc('banana: 70 + 10% of 70 = 70 + 7 = 77%', 'orange: 20 − 10% of 20 = 20 − 2 = 18%', 'apple: 100 − 77 − 18 = 5%')}
{_smoothie()}""",
        f"""<p>So look for: banana just over three quarters, orange a little smaller, apple about <b>half</b> its old slice {ar()} {boxed('B')}</p>
{note('“10% more” is 10% of what was there. Adding 10 percentage points (70 → 80) is the trap that leads to E.', 'trap')}""",
    ],
    answer_text='Pie B: banana 77%, orange 18%, apple 5%.',
    why={'A': 'Banana 77% but orange went <b>up</b> to 22%, which leaves almost no apple (1%).',
         'C': 'Banana shrank to about 63%: it takes 10% off the banana instead of adding it.',
         'D': 'Swaps the changes: banana down to 63%, orange up to 22%.',
         'E': 'Uses 10 percentage points: banana 80%, orange 10%, apple 10%. The question means 10% of each amount.'},
    fast='70 → 77, 20 → 18, so apple 10 → 5. Banana a bit bigger, apple half as big: B.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _sports_grid():
    bad = {26, 30, 31, 33, 34, 35, 37, 38, 39}
    opt = {22: 'A', 26: 'B', 30: 'C', 33: 'D', 37: 'E'}
    cw, ch, x0, y0 = 54, 38, 40, 40
    parts, lab = [], []
    for n in range(40):
        r, c = divmod(n, 10)
        x, y = x0 + c * cw, y0 + r * 62
        parts.append(rect(x + 2, y, cw - 4, ch, k='ink', fill='p' if n in bad else 'g', sw=1.4, rx=3))
        lab.append(text(x + cw / 2, y + 26, n, k='red' if n in bad else 'ink', size=18, font='print',
                        weight='bold' if n in opt else None))
        if n in opt:
            lab.append(text(x + cw / 2, y + ch + 20, opt[n], k='pen', size=18, font='scrawl'))
    parts.append(circle(x0 + 6 * cw + cw / 2, y0 + 2 * 62 + ch / 2, 27, k='red', sw=2.6))
    lab.append(text(x0, 26, 'green = possible with up to 3 events, pink = impossible', k='muted', size=15, anchor='start'))
    return svg(640, 290, rough(*parts) + ''.join(lab),
               'Grid of totals 0 to 39; every total up to 25 is possible and 26 is the first impossible one')


Q.append(dict(
    n=20, orig=42, answer='B', topic='Scores & combinations',
    question=f"""<p>On sports day at Thiska Academy points are awarded in each event as follows:</p>
{table([['winner', hl('12 points', 'g', 1)], ['2<sup>nd</sup> place', hl('8 points', 'g')], ['3<sup>rd</sup> place', hl('5 points', 'g')],
        ['4<sup>th</sup> place', hl('3 points', 'g')], ['5<sup>th</sup> place', hl('1 point', 'g')]])}
<p>Each student may enter {hl('no more than three events', 'y', 2)}.</p>
<p class="stem">What is the {hl('smallest points total that it is <b>not</b> possible', 'b', 3)} for an individual student to score?</p>""",
    options={'A': '22', 'B': '26', 'C': '30', 'D': '33', 'E': '37'},
    notes=[(1, 'g', 'Each event scores 12, 8, 5, 3 or 1 (or 0 if not placed).'),
           (2, 'y', 'Up to three scores added together. The same place can repeat (e.g. win twice).'),
           (3, 'b', 'Smallest impossible total: test the options from the smallest up.')],
    steps=[
        f"""<p>Test the options from the smallest:</p>
{calc(f'22 = 12 + 5 + 5 {tick()} possible, so not the answer')}""",
        f"""<p>Now 26. Sort by how many 12s you use:</p>
{calc(f'two 12s: 24, need 2 more {ar()} no score of 2 {cross()}',
      f'one 12: need 14 from two scores {ar()} 8 + 5 = 13, 8 + 8 = 16 {cross()}',
      f'no 12s: biggest is 8 + 8 + 8 = 24 {cross()}', f'26 is impossible {ar()} {boxed("26")}')}""",
        f"""<p>Make sure nothing smaller is impossible. Everything up to 25 can be made (e.g. 23 = 12 + 8 + 3, 24 = 12 + 12, 25 = 12 + 12 + 1):</p>{_sports_grid()}""",
    ],
    answer_text='26: two 12s leave 2, one 12 leaves 14 (not makeable from two scores), and without a 12 the most is 24.',
    why={'A': '22 is possible: win once and come 3rd twice (12 + 5 + 5).',
         'C': '30 is impossible too, but 26 is smaller.',
         'D': '33 is impossible, but 26 is smaller.',
         'E': '37 is more than the maximum of 36 (three wins), so impossible, but far from the smallest.'},
    fast='22 = 12 + 5 + 5. 26: 12 + 12 + 2? no. 12 + 14? 14 isn’t two scores. 8 + 8 + 8 = 24 max without a 12. So 26.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _close_calls():
    rows = [('Doggie Doo', '49.98', '&lt;', '50.00', 'just over ✓', 'green'),
            ('Fireman Sam', '59.98', '&lt;', '59.99', 'just over ✓', 'green'),
            ('Monster High', '59.98', '=', '59.98', 'exactly 100% ✗', 'red'),
            ('Lego Falcon', '265.98', '=', '265.98', 'exactly 100% ✗', 'red')]
    parts, lab = [], []
    lab += [text(214, 30, 'double the RRP', k='muted', size=15), text(392, 30, 'online', k='muted', size=15)]
    for i, (name, dbl, sign, online, verdict, col) in enumerate(rows):
        y = 44 + i * 52
        parts.append(rect(20, y, 600, 42, k=col, fill='g' if col == 'green' else 'p', sw=1.6, rx=8))
        lab += [text(34, y + 28, name, k='ink', size=17, anchor='start'),
                text(214, y + 28, f'${dbl}', k='ink', size=18),
                text(303, y + 30, sign, k=col, size=26, weight='bold'),
                text(392, y + 28, f'${online}', k='ink', size=18),
                text(600, y + 28, verdict, k=col, size=18, font='scrawl', anchor='end')]
    return svg(640, 260, rough(*parts) + ''.join(lab),
               'Close calls: Doggie Doo and Fireman Sam are just over double; Monster High and Lego are exactly double, which is not more than 100 percent')


Q.append(dict(
    n=21, orig=43, answer='C', topic='Percentages',
    question=f"""<p>Every Christmas the most popular children’s toys become scarce. Many people turn to online auction sites to buy them instead. The table below shows the recommended retail price and the price that the listed toys have sold for online.</p>
{table([['Moshling Tree House', '18.99', '198.98'], ['LeapPad Explorer', '79.99', '225.00'],
        ['Doggie Doo', hl('24.99', 'p', 2), hl('50.00', 'p')], ['Fireman Sam Pontypandy Rescue set', '29.99', '59.99'],
        ['Fijit Friends', '54.99', '99.95'], ["Monster High Lagoona’s Station", hl('29.99', 'p', 3), hl('59.98', 'p')],
        ['Nerf Vortex Nitron Blaster', '44.99', '59.99'], ['Kidizoom Twist', '49.99', '65.95'],
        ['Milky the Bunny', '59.99', '74.99'], ['Star Wars Ultimate Force Lightsaber', '39.99', '49.95'],
        ['Lets Rock Elmo', '69.99', '84.99'], ['Ninjago Fire Temple', '91.99', '96.99'],
        ['Sylvanian Families', '79.95', '192.29'], ['Vtech Innotab', '79.99', '150.99'],
        ['Lego Star Wars Millennium Falcon', '132.99', '265.98']],
       head=['<i>children’s toy</i>', '<i>recommended retail price</i> ($)', '<i>online auction site</i> ($)'])}
<p class="stem">How many of the toys above have {hl('increased in price by more than 100%', 'b', 1)}?</p>""",
    options={'A': '3', 'B': '4', 'C': '5', 'D': '6', 'E': '7'},
    notes=[(1, 'b', 'Up by more than 100% = online price <b>more than double</b> the RRP. Exactly double is only 100%: doesn’t count.'),
           (2, 'p', 'Double 24.99 = 49.98. 50.00 beats it by 2 cents: it counts!'),
           (3, 'p', 'Double 29.99 = 59.98 exactly. That’s 100%, not more.')],
    steps=[
        f"""<p>Double each RRP and compare with the online price. Doubling 18.99: think 19 × 2 = 38, minus 2 cents = 37.98.</p>
{table([['Moshling', '37.98', '198.98', tick()], ['LeapPad', '159.98', '225.00', tick()], ['Doggie Doo', '49.98', '50.00', tick()],
        ['Fireman Sam', '59.98', '59.99', tick()], ['Fijit Friends', '109.98', '99.95', cross()], ['Monster High', '59.98', '59.98', cross() + ' equal'],
        ['Nerf', '89.98', '59.99', cross()], ['Kidizoom', '99.98', '65.95', cross()], ['Milky', '119.98', '74.99', cross()],
        ['Lightsaber', '79.98', '49.95', cross()], ['Elmo', '139.98', '84.99', cross()], ['Ninjago', '183.98', '96.99', cross()],
        ['Sylvanian', '159.90', '192.29', tick()], ['Vtech', '159.98', '150.99', cross()], ['Lego Falcon', '265.98', '265.98', cross() + ' equal']],
       head=['toy', '2 × RRP', 'online', 'more than double?'])}""",
        f"""<p>The four close calls decide it:</p>{_close_calls()}
{calc(f'Moshling, LeapPad, Sylvanian, Doggie Doo, Fireman Sam {ar()} {boxed("5")}')}""",
    ],
    answer_text='5 toys: Moshling Tree House, LeapPad Explorer, Sylvanian Families, Doggie Doo and Fireman Sam.',
    why={'A': 'Only the 3 obvious ones. Misses Doggie Doo and Fireman Sam, which are just over double.',
         'B': 'Misses one of the two just-over toys (Doggie Doo by 2 cents or Fireman Sam by 1 cent).',
         'D': 'Counts one of the exactly-double toys (Monster High or Lego) as more than 100%.',
         'E': 'Counts both exactly-double toys, Monster High and Lego. Exactly double is a 100% increase, not more.'},
    fast='Double the RRP. Clear: Moshling, LeapPad, Sylvanian. Just over: Doggie Doo, Fireman Sam. Exactly double (no): Monster High, Lego. Total 5.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _tv_price():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sold = [2.5, 4, 2, 3.5, 4.5, 3.5]
    inc = [1.5, 2.4, 1.2, 2.8, 3.6, 2.8]
    base, s = 306, 220
    parts, lab = [], []
    parts.append(line(40, base, 600, base, k='ink', w=2))
    for i, (m, n, v) in enumerate(zip(months, sold, inc)):
        x = 64 + i * 90
        p = v / n
        parts.append(rect(x, base - p * s, 52, p * s, k='ink', fill='b' if p < 0.7 else 'o', sw=1.6))
        lab.append(text(x + 26, base + 22, m, k='ink', size=16))
        lab.append(text(x + 26, base - p * s - 30, f'{v:g} ÷ {n:g}', k='muted', size=15))
        lab.append(text(x + 26, base - p * s - 9, f'= {p:.1f}', k='ink', size=17))
    parts.append(arrow(64 + 2 * 90 + 52, base - 0.6 * s - 50, 64 + 3 * 90 + 6, base - 0.8 * s - 52, k='red', bend=-0.3))
    lab.append(text(64 + 2.5 * 90 + 26, base - 0.8 * s - 76, 'price up!', k='red', size=22, font='scrawl'))
    lab.append(text(40, 24, 'income ÷ number sold = price per TV (grid units)', k='muted', size=15, anchor='start'))
    return svg(620, 336, rough(*parts) + ''.join(lab),
               'Price per TV each month: 0.6 in January, February and March; 0.8 in April, May and June')


Q.append(dict(
    n=22, orig=44, answer='C', topic='Reading graphs',
    question=f"""<p>A store sells a particular type of television. The graphs below show the {hl('number of these televisions sold per month', 'g', 1)} and the {hl('total income from their sales per month', 'g', 2)}, over a six-month period.</p>
{fig(Y, 'ps_q22_charts', 'Two bar charts for January to June: number sold, and total monthly income', 300)}
<p>The price at which these televisions were sold was {hl('increased at the beginning of one of the six months', 'y', 3)}.</p>
<p class="stem">At the beginning of {hl('which month', 'b', 4)} was the price increased?</p>""",
    options={'A': 'February', 'B': 'March', 'C': 'April', 'D': 'May', 'E': 'June'},
    notes=[(1, 'g', 'Read the bar heights in grid lines.'),
           (2, 'g', 'Income = price × number sold, so price = income ÷ number sold.'),
           (3, 'y', 'One price before the change, a higher one after it.'),
           (4, 'b', 'The first month where income ÷ number jumps up.')],
    steps=[
        f"""<p>Read both charts in grid lines:</p>
{table([['number sold', '2½', '4', '2', '3½', '4½', '3½'], ['income', '1.5', '2.4', '1.2', '2.8', '3.6', '2.8']],
       head=['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])}
<p>Two quick spots: Feb → Mar, sales halve and income halves (same price). April and June are identical (same price).</p>""",
        f"""<p>Work out income ÷ number for every month:</p>{_tv_price()}
<p>The price is the same for Jan to Mar, then higher from April {ar()} {boxed('April')}</p>
{note('Don’t just look for the month where income rises. Income also rises when more TVs are sold (Jan → Feb).', 'trap')}""",
    ],
    answer_text='April: income ÷ number sold is 0.6 for January to March and 0.8 from April onwards.',
    why={'A': 'February’s income rose only because more were sold: 2.4 ÷ 4 = 0.6, the same as January (1.5 ÷ 2.5).',
         'B': 'March’s income fell, but so did sales, by the same fraction: 1.2 ÷ 2 = 0.6, the old price.',
         'D': 'May has the biggest income, but it also sold the most: 3.6 ÷ 4.5 = 0.8, the same as April.',
         'E': 'June is identical to April (3½ sold, 2.8 income), so the price didn’t change between them.'},
    fast='Price = income ÷ number. Jan–Mar: 1.5 ÷ 2.5 = 2.4 ÷ 4 = 1.2 ÷ 2 = 0.6. April: 2.8 ÷ 3.5 = 0.8. April.',
))


# ---------------------------------------------------------------- 23 (Q46)
def _tablets():
    parts, lab = [], []
    # one week
    lab.append(text(20, 28, 'One new week (start with the 4s):', k='ink', size=17, font='scrawl', anchor='start'))
    for i, t in enumerate([4, 4, 4, 4, 4, 6, 6]):
        parts.append(rect(30 + i * 46, 40, 42, 36, k='ink', fill='y' if t == 4 else 'o', sw=1.5, rx=3))
        lab.append(text(30 + i * 46 + 21, 65, t, k='ink', size=18))
    lab.append(text(370, 65, '= 32 tablets a week', k='pen', size=19, anchor='start'))
    # bars
    s, x0 = 7.6, 120
    lab.append(text(x0 - 10, 132, '6 a day', k='ink', size=16, anchor='end'))
    parts.append(rect(x0, 112, 50 * s, 30, k='ink', fill='o', sw=1.6))
    lab.append(text(x0 + 25 * s, 133, '50 days', k='ink', size=17))
    lab.append(text(x0 - 10, 192, 'new plan', k='ink', size=16, anchor='end'))
    for w in range(9):
        parts.append(rect(x0 + w * 7 * s, 172, 7 * s, 30, k='ink', fill='b' if w % 2 == 0 else 'paper', sw=1.4))
    parts.append(rect(x0 + 63 * s, 172, 3 * s, 30, k='green', fill='g', sw=2))
    lab.append(text(x0 + 31.5 * s, 222, '9 full weeks = 63 days (288 tablets)', k='pen', size=16))
    lab.append(text(x0 + 64.5 * s, 162, '+3', k='green', size=17))
    lab.append(text(x0 + 66 * s - 4, 246, '12 left = 4 + 4 + 4', k='green', size=16, anchor='end'))
    parts.append(line(x0 + 50 * s, 104, x0 + 50 * s, 210, k='red', w=2, dash=True))
    parts.append(line(x0 + 66 * s, 160, x0 + 66 * s, 210, k='red', w=2, dash=True))
    lab.append(text(x0 + 58 * s, 104, '+16 days', k='red', size=20, font='scrawl'))
    return svg(640, 260, rough(*parts) + ''.join(lab),
               'A week of 4, 4, 4, 4, 4, 6, 6 tablets; the old plan lasts 50 days and the new plan 9 weeks plus 3 days, 66 days')


Q.append(dict(
    n=23, orig=46, answer='C', topic='Rates & weeks',
    question=f"""<p>My dog’s coat had been looking dull, so I bought some conditioning tablets. The pet shop stocks these in {hl('boxes of 300 tablets', 'g', 1)}, and for a dog the size of mine the recommendation (which I have followed) is {hl('6 tablets per day', 'g', 2)}.</p>
<p>Now, several months later, his coat is much shinier. Opening a new box of tablets today, I have decided to reduce his dosage. I shall just give him {hl('6 tablets per day, twice a week, and on the remaining days each week he can have 4 tablets each day', 'y', 3)}.</p>
<p class="stem">What is the {hl('maximum number of extra days', 'b', 4)} that this box of conditioning tablets will now last?</p>""",
    options={'A': '10 days', 'B': '15 days', 'C': '16 days', 'D': '24 days', 'E': '25 days'},
    notes=[(1, 'g', '300 tablets in the box.'),
           (2, 'g', 'Old way: 300 ÷ 6 = 50 days.'),
           (3, 'y', 'Two 6-days + five 4-days each week = 32 tablets a week.'),
           (4, 'b', '“Maximum”: you choose which days are the 6-days, so put the 4-days where they help. Then compare with 50.')],
    steps=[
        f"""{calc('old: 300 ÷ 6 = <b>50 days</b>', 'new week: 2 × 6 + 5 × 4 = 12 + 20 = <b>32 tablets</b>')}""",
        f"""<p>How many full weeks fit in 300?</p>
{calc('9 × 32 = 288 (10 × 32 = 320 is too many)', '9 weeks = 63 days, with 300 − 288 = 12 tablets left')}
<p>To make the last 12 last as long as possible, use the 4-tablet days: 4 + 4 + 4 = 3 more days.</p>
{_tablets()}""",
        f"""{calc('63 + 3 = 66 days', f'extra = 66 − 50 = {boxed("16 days")}')}
{note('If the leftover 12 went on 6-tablet days (6 + 6), it would last only 2 days: 65 days, 15 extra. “Maximum” means start the week with the 4s.', 'trap')}""",
    ],
    answer_text='16 extra days: 66 days (9 weeks + three 4-tablet days) instead of 50.',
    why={'A': 'Uses an average of 5 a day ((6 + 4) ÷ 2): 300 ÷ 5 = 60, so 10 extra. But there are five 4-days and only two 6-days a week.',
         'B': 'Spends the last 12 tablets on two 6-tablet days, so 65 days. That’s not the maximum.',
         'D': '24 extra means 74 days, but even 10 weeks would need 320 tablets.',
         'E': 'Gives 4 a day every day: 300 ÷ 4 = 75, so 25 extra. Forgets the two 6-tablet days each week.'},
    fast='32 a week. 9 weeks = 288 = 63 days. 12 left = three 4-days. 66 − 50 = 16.',
))


# ---------------------------------------------------------------- 24 (Q48)
def _george():
    parts, lab = [], []
    xs = [60, 220, 470, 600]
    names = ['home', 'Beetown', 'Exbay', 'cinema']
    for x, nm in zip(xs, names):
        parts.append(circle(x, 70, 12, k='ink', fill='paper', sw=2))
        lab.append(text(x, 40, nm, k='ink', size=18, weight='bold'))
    segs = [(0, 1, 'walk 14 min'), (1, 2, 'train 37 min'), (2, 3, 'walk 5')]
    for a, b, l in segs:
        parts.append(line(xs[a] + 14, 70, xs[b] - 14, 70, k='muted', w=3, dash=(a != 1)))
        lab.append(text((xs[a] + xs[b]) / 2, 96, l, k='muted', size=15))
    good = ['17:51', '18:05', '18:42', '18:47']
    late = ['18:31', '18:45', '19:22', '19:27']
    for x, g, l in zip(xs, good, late):
        lab.append(text(x, 140, g, k='green', size=20))
        lab.append(text(x, 196, l, k='red', size=20))
    lab.append(text(20, 122, 'the 18:05 train:', k='green', size=16, anchor='start'))
    lab.append(text(20, 178, 'the next one, 18:45:', k='red', size=16, anchor='start'))
    lab.append(text(600, 164, 'in time ✓', k='green', size=16))
    lab.append(text(600, 220, '7 min late ✗', k='red', size=16))
    lab.append(text(330, 236, 'He may arrive by 19:25 at the latest (film 19:20 + 5)', k='pen', size=17))
    return svg(650, 250, rough(*parts) + ''.join(lab),
               'Journey home to Beetown to Exbay to cinema: leaving 17:51 for the 18:05 train arrives 18:47; the 18:45 train arrives 19:27, too late')


Q.append(dict(
    n=24, orig=48, answer='B', topic='Timetables',
    question=f"""<p>Trains run regularly between Ayton and Exbay, stopping at Beetown, Chalton and Deeford, according to the following timetable.</p>
<div class="tbl-wrap"><table class="ptable"><thead><tr><th colspan="4"><i>Departures</i></th></tr></thead><tbody>
<tr><td>Ayton</td><td>7:10</td><td rowspan="5">{hl('and<br>every<br>40<br>minutes<br>until', 'y', 1)}</td><td>21:10</td></tr>
<tr><td>{hl('Beetown', 'g')}</td><td>{hl('7:25', 'g')}</td><td>21:25</td></tr>
<tr><td>Chalton</td><td>7:30</td><td>21:30</td></tr>
<tr><td>Deeford</td><td>7:44</td><td>21:44</td></tr>
<tr><td>{hl('Exbay', 'g')}</td><td>{hl('8:02', 'g')}</td><td>22:02</td></tr>
</tbody></table></div>
<p>George lives a {hl('14-minute walk away from Beetown station', 'g', 2)}. He is going to the cinema in Exbay to watch a film that {hl('starts at 19:20', 'g', 3)}. It will take him {hl('five minutes to walk from the station at Exbay to the cinema', 'g', 4)}. George wants to make sure that he will {hl('miss no more than the first five minutes', 'p', 5)} of the film.</p>
<p class="stem">What is the {hl('latest time George should leave home', 'b', 6)}?</p>""",
    options={'A': '17:36', 'B': '17:51', 'C': '18:05', 'D': '18:19', 'E': '18:31'},
    notes=[(1, 'y', 'Every 40 minutes. Beetown to Exbay always takes 8:02 − 7:25 = 37 minutes.'),
           (2, 'g', 'He gets on at Beetown, not Ayton.'),
           (3, 'g', 'Film at 19:20.'),
           (4, 'g', 'Exbay station → cinema: 5 minutes.'),
           (5, 'p', 'He can be in his seat by 19:25 at the latest. So off the train at Exbay by 19:20.'),
           (6, 'b', 'Latest train that works, then take off the walk.')],
    steps=[
        f"""<p>Deadline at Exbay station:</p>{calc('19:20 + 5 min late allowed = 19:25 at the cinema', '19:25 − 5 min walk = <b>19:20</b> at Exbay')}""",
        f"""<p>Trains reach Exbay at 8:02 and then every 40 minutes. The minutes go :02, :42, :22, :02 … (every 2 hours = 3 trains):</p>
{calc(f'… 18:02, 18:42, 19:22 …', f'19:22 is 2 minutes too late {ar()} take the <b>18:42</b> arrival')}""",
        f"""<p>That train leaves Beetown 37 minutes earlier, then take off the walk:</p>
{calc('18:42 − 37 min = 18:05 from Beetown', f'18:05 − 14 min walk = {boxed("17:51")}')}
{_george()}""",
    ],
    answer_text='17:51: walk 14 minutes to catch the 18:05 from Beetown, which reaches Exbay at 18:42.',
    why={'A': 'Uses the Ayton time of the same train (17:50) instead of Beetown: 17:50 − 14 = 17:36.',
         'C': '18:05 is when the train leaves Beetown. He still has a 14-minute walk to get there.',
         'D': 'Adds the 14-minute walk (18:05 + 14) instead of taking it away.',
         'E': 'Catches the 18:45, which reaches Exbay at 19:22. Walking 5 minutes, he reaches the cinema at 19:27 and misses 7 minutes.'},
    fast='Must be at Exbay by 19:20. Arrivals …18:02, 18:42, 19:22. Take 18:42 → Beetown 18:05 → leave 17:51.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _gold():
    data = [('Amber', 8, 21), ('Emerald', 5, 21), ('Garnet', 6, 22), ('Jade', 6, 16), ('Sapphire', 11, 28)]
    base, s = 272, 4.4
    parts, lab = [], []
    for v in range(0, 51, 10):
        parts.append(line(70, base - v * s, 600, base - v * s, k='muted', w=0.8, dash=v > 0))
        lab.append(text(62, base - v * s + 5, f'{v}%', k='muted', size=14, anchor='end'))
    for i, (name, g, t) in enumerate(data):
        x = 100 + i * 100
        p = 100 * g / t
        parts.append(rect(x, base - p * s, 40, p * s, k='ink', fill='y', sw=1.6))
        lab.append(text(x + 20, base + 22, name, k='ink', size=16))
        lab.append(text(x + 20, base - p * s - 26, f'{g}/{t}', k='muted', size=15))
        lab.append(text(x + 20, base - p * s - 8, f'{p:.0f}%', k='ink', size=16))
    lab.append(text(70, 20, 'gold ÷ all medals, with gridlines every 10%', k='muted', size=15, anchor='start'))
    return svg(620, 304, rough(*parts) + ''.join(lab),
               'Bar chart of gold proportions: Amber 38, Emerald 24, Garnet 27, Jade 38, Sapphire 39 percent')


Q.append(dict(
    n=25, orig=50, answer='D', topic='Fractions & bar charts',
    question=f"""<p>The table below shows the medal count by the top five teams in a recent Mini Olympics.</p>
{table([['Amber', '8', '7', '6'], ['Emerald', '5', '10', '6'], ['Garnet', '6', '6', '10'], ['Jade', '6', '5', '5'], ['Sapphire', '11', '8', '9']],
       head=['<i>teams</i>', '<i>gold medals</i>', '<i>silver medals</i>', '<i>bronze medals</i>'])}
<p>Each team calculated the {hl('proportion of their medals that were gold', 'y', 1)}.</p>
<p class="stem">Which one of the following charts, {hl('with appropriate labelling', 'p', 2)}, {hl('shows this proportion', 'b', 3)} for each of the five teams?</p>
{fig(Y, 'ps_q25_charts', 'Five bar charts A to E, each with bars for Amber, Emerald, Garnet, Jade and Sapphire and no axis numbers', 560)}""",
    options={'A': 'chart A', 'B': 'chart B', 'C': 'chart C', 'D': 'chart D', 'E': 'chart E'},
    notes=[(1, 'y', 'Proportion = gold ÷ (gold + silver + bronze) for that team.'),
           (2, 'p', 'No numbers on the axes, so only the <b>shape</b> matters: the bar heights must be in the right proportion (from 0).'),
           (3, 'b', 'Work out the five fractions, then compare heights.')],
    steps=[
        f"""<p>Total medals and the gold fraction for each team:</p>
{calc('Amber 8 + 7 + 6 = 21: 8/21 ≈ 0.38', 'Emerald 5 + 10 + 6 = 21: 5/21 ≈ 0.24', 'Garnet 6 + 6 + 10 = 22: 6/22 ≈ 0.27',
      'Jade 6 + 5 + 5 = 16: 6/16 = 0.375', 'Sapphire 11 + 8 + 9 = 28: 11/28 ≈ 0.39')}""",
        f"""<p>Draw what the right chart should look like:</p>{_gold()}
<p>Look for: Sapphire, Amber and Jade almost level at the top; Garnet just above Emerald; Emerald about 60% of Sapphire’s height (0.24 ÷ 0.39).</p>""",
        f"""<p>Run through the charts:</p>
{calc(f'A: Garnet shorter than Emerald {cross()}', f'B: these are the gold counts 8, 5, 6, 6, 11 {cross()}',
      f'C: these are the total medals 21, 21, 22, 16, 28 {cross()}', f'E: Emerald under half of Sapphire {cross()}',
      f'D: matches, with each gridline worth 10% {tick()} {ar()} {boxed("D")}')}""",
    ],
    answer_text='Chart D: bars of about 38%, 24%, 27%, 38% and 39% (gridlines 10% apart).',
    why={'A': 'Garnet is drawn shorter than Emerald, but 6/22 ≈ 27% beats 5/21 ≈ 24%.',
         'B': 'Shows the number of golds (8, 5, 6, 6, 11), not the proportion. Sapphire towers over the rest.',
         'C': 'Shows each team’s total number of medals (21, 21, 22, 16, 28).',
         'E': 'Right order, but Emerald’s bar is less than half of Sapphire’s; it should be about 60% of it. The heights only fit if the axis started at about 11%, not 0.'},
    fast='Fractions ≈ 38, 24, 27, 38, 39%. Top three nearly level, Garnet a bit above Emerald, Emerald about ⅗ of Sapphire. Only D.',
))
