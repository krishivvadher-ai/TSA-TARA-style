from wslib import *

Y = 2017
Q = []


def _cells(cells, x0, y0, c, fill, k='ink', sw=1.4):
    """Unit squares at grid positions (col, row)."""
    return [rect(x0 + cx * c, y0 + cy * c, c, c, k=k, fill=fill, sw=sw) for cx, cy in cells]


# ---------------------------------------------------------------- 1 (Q2)
def _cafe():
    s = 10
    x0 = 100
    parts, lab = [], []

    def bar(y, segs, name, total):
        x = x0
        lab.append(text(x0 - 10, y + 25, name, k='ink', size=19, anchor='end'))
        for n, f, inside, below in segs:
            w = n * s
            parts.append(rect(x, y, w, 36, k='ink', fill=f, sw=1.6))
            if inside:
                lab.append(text(x + w / 2, y + 24, inside, k='ink', size=16))
            if below:
                lab.append(text(x + w / 2, y + 60, below, k='pen', size=18))
            x += w
        lab.append(text(x + 14, y + 26, total, k='red', size=24, anchor='start', font='scrawl'))
        return x

    end = bar(46, [(40, 'g', '40 sold at $2', '$80'), (8, 'y', '8 at $1', '$8'), (2, 'p', '', '')], 'pizzas', '= $88')
    lab.append(text(end - 10, 38, '2 free', k='red', size=15))
    end = bar(140, [(35, 'g', '35 sold at $1', '$35'), (14, 'y', '14 at 50c', '$7'), (1, 'p', '', '')], 'flapjacks', '= $42')
    lab.append(text(end - 5, 132, '1 free', k='red', size=15))
    # legend
    parts += [rect(100, 236, 18, 14, k='ink', fill='g', sw=1.2), rect(246, 236, 18, 14, k='ink', fill='y', sw=1.2),
              rect(420, 236, 18, 14, k='ink', fill='p', sw=1.2)]
    lab += [text(124, 248, 'lunchtime, full price', k='ink', size=15, anchor='start'),
            text(270, 248, 'afternoon, half price', k='ink', size=15, anchor='start'),
            text(444, 248, 'given away', k='ink', size=15, anchor='start')]
    return svg(660, 262, rough(*parts) + ''.join(lab),
               'Two bars: pizzas split 40 sold at 2 dollars, 8 at 1 dollar, 2 free; flapjacks split 35 at 1 dollar, 14 at 50 cents, 1 free')


Q.append(dict(
    n=1, orig=2, answer='A', topic='Money & profit',
    question=f"""<p>A café owner makes {hl('50 mini pizzas and 50 flapjacks', 'g', 1)} for sale during the day. The pizzas are
sold for $2.00 each and the flapjacks are sold for $1.00 each. However, by the end of
lunchtime there are {hl('10 mini pizzas still unsold and 15 flapjacks unsold', 'y', 2)}, so the {hl('price of each is halved', 'y', 3)} for the afternoon. At the end of the day there are still {hl('2 mini pizzas and 1 flapjack left
which are given away free', 'p', 4)} to the last customer.</p>
<p class="stem">If the original 50 mini pizzas and 50 flapjacks had a combined production cost of $30.00, how
much {hl('<b>profit</b>', 'b', 5)} is made on the sale of the mini pizzas and flapjacks for the day?</p>""",
    options={'A': '$100.00', 'B': '$102.50', 'C': '$115.00', 'D': '$120.00', 'E': '$130.00'},
    notes=[(1, 'g', 'Start with 50 of each.'),
           (2, 'y', 'These are the ones <b>left over</b>. So 50 − 10 = 40 pizzas and 50 − 15 = 35 flapjacks sold at lunchtime.'),
           (3, 'y', 'Afternoon prices: pizza $1, flapjack 50c.'),
           (4, 'p', 'Trap! These 3 are part of the 10 and 15 above, and they earn <b>nothing</b>.'),
           (5, 'b', 'Profit = money taken − $30 cost. Don’t stop at the takings.')],
    steps=[
        f"""<p>Split each food into three groups: sold at full price, sold at half price, given away.</p>
<ul><li>Pizzas: 40 full price, 10 − 2 = <b>8</b> half price, 2 free.</li>
<li>Flapjacks: 35 full price, 15 − 1 = <b>14</b> half price, 1 free.</li></ul>
{_cafe()}""",
        f"""<p>Add up the money taken:</p>
{calc(f'pizzas: 40 × $2 + 8 × $1 = $80 + $8 = $88',
      f'flapjacks: 35 × $1 + 14 × 50c = $35 + $7 = $42',
      f'takings = $88 + $42 = <b>$130</b>')}
{note('14 × 50c: half of 14 = 7, so $7.', 'tip')}""",
        f"""<p>Now take off the cost:</p>
{calc(f'$130 − $30 = {boxed("$100")}')}""",
    ],
    answer_text='$100: takings of $130 minus the $30 cost.',
    why={'B': '$102.50 charges for the free food: it sells all 10 pizzas and all 15 flapjacks in the afternoon ($10 + $7.50).',
         'C': '$115 forgets to halve the prices: 48 pizzas at $2 + 49 flapjacks at $1 = $145, then − $30.',
         'D': '$120 sells all 100 items at full price ($150 − $30). It ignores the leftovers and the price cut.',
         'E': '$130 is the money taken. It forgets to take off the $30 cost, so it isn’t the profit.'},
    fast='Sold: 40 × 2 + 8 × 1 + 35 × 1 + 14 × 0.5 = 80 + 8 + 35 + 7 = 130. Profit 130 − 30 = $100.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _frame():
    s = 4.4
    X0, Y0 = 70, 30
    fx, fy, fw, fh = X0, Y0, 46 * s, 59 * s
    mx, my = X0 + 2 * s, Y0 + 2 * s
    px, py, pw, ph = X0 + 8 * s, Y0 + 8 * s, 30 * s, 40 * s
    parts = [rect(fx, fy, fw, fh, k='orange', fill='o', sw=2.4),
             rect(mx, my, 42 * s, 55 * s, k='ink', fill='paper', sw=1.6),
             rect(px, py, pw, ph, k='pen', fill='b', sw=2),
             # a little landscape inside the picture
             poly([(px + 6, py + ph - 8), (px + 46, py + 70), (px + 74, py + 112), (px + 100, py + 82), (px + pw - 6, py + ph - 8)],
                  k='green', fill='g', sw=2),
             circle(px + pw - 30, py + 34, 14, k='orange', fill='y', sw=2)]
    lab = [text(px + pw / 2, py + ph + 26, 'mount', k='muted', size=14),
           text(fx + fw / 2, fy - 8, 'frame (wood)', k='orange', size=15)]
    # height stack on the right
    sx = fx + fw + 34
    ys = [Y0, Y0 + 2 * s, Y0 + 8 * s, Y0 + 48 * s, Y0 + 57 * s, Y0 + 59 * s]
    cols = ['orange', 'ink', 'pen', 'ink', 'orange']
    for i in range(5):
        parts.append(line(sx, ys[i] + 1, sx, ys[i + 1] - 1, k=cols[i], w=5))
    for y in ys:
        parts.append(line(sx - 9, y, sx + 9, y, k='ink', w=1.8))
        parts.append(line(fx + fw + 4, y, sx - 12, y, k='muted', w=1, dash=True))
    labels = [(18, '2 cm wood', 'orange'), (52, '6 cm mount (top)', 'ink'), (160, '40 cm picture', 'pen'),
              (266, '9 cm mount (bottom)', 'ink'), (306, '2 cm wood', 'orange')]
    for (ly, t, k), i in zip(labels, range(5)):
        mid = (ys[i] + ys[i + 1]) / 2
        lab.append(text(sx + 40, ly + 5, t, k=k, size=18, anchor='start'))
        parts.append(line(sx + 6, mid, sx + 36, ly, k='muted', w=1.2))
    # overall height arrow on the left
    parts.append(line(36, Y0, 36, Y0 + fh, k='red', w=2.4, head=True, tail=True))
    lab.append(text(26, Y0 + fh / 2, 'overall height = 59 cm', k='red', size=20, font='scrawl', rotate=-90))
    lab.append(text(sx + 40, 230, '2 + 6 + 40 + 9 + 2', k='red', size=20, anchor='start', font='scrawl'))
    lab.append(text(sx + 40, 252, '= 59 cm', k='red', size=22, anchor='start', font='scrawl'))
    return svg(620, 330, rough(*parts) + ''.join(lab),
               'Framed picture drawn front-on with the heights stacked on the right: 2 cm wood, 6 cm mount, 40 cm picture, 9 cm mount, 2 cm wood, total 59 cm')


Q.append(dict(
    n=2, orig=6, answer='D', topic='Measures & diagrams',
    question=f"""<p>A picture {hl('40 cm high', 'g', 1)} by {hl('30 cm wide', 'p', 2)} is to be framed. There will be a mount between the edge of
the picture and the frame. This mount will be {hl('6 cm wide at the top and sides, and 9 cm wide at
the bottom', 'y', 3)}. The width of the wood used for the frame is {hl('2 cm', 'p', 4)}.</p>
<p class="stem">What is the {hl('<b>overall height</b>', 'b', 5)} of the framed picture?</p>""",
    options={'A': '46 cm', 'B': '49 cm', 'C': '56 cm', 'D': '59 cm', 'E': '62 cm'},
    notes=[(1, 'g', 'The picture’s height: this is the number you build on.'),
           (2, 'p', 'Not needed! Height only. The width is there to tempt you.'),
           (3, 'y', 'Top and bottom are <b>different</b>: 6 cm above, 9 cm below. The sides don’t affect the height.'),
           (4, 'p', 'The wood goes all the way round, so it adds 2 cm at the top <b>and</b> 2 cm at the bottom.'),
           (5, 'b', 'Measure from the very top of the frame to the very bottom.')],
    steps=[
        f"""<p>Imagine it hanging on the wall. Go from the top edge down to the bottom edge and list every layer you pass through.</p>
{_frame()}""",
        f"""{calc('wood + mount + picture + mount + wood', f'2 + 6 + 40 + 9 + 2 = {boxed("59 cm")}')}
{note('Each layer of frame and mount appears <b>twice</b> in a height: once above the picture, once below.', 'trap')}""",
    ],
    answer_text='59 cm: 2 + 6 + 40 + 9 + 2.',
    why={'A': '46 cm is the overall <b>width</b>: 2 + 6 + 30 + 6 + 2.',
         'B': '49 cm uses the picture’s width (30) instead of its height (40): 2 + 6 + 30 + 9 + 2.',
         'C': '56 cm uses a 6 cm mount at the bottom too, but the bottom mount is 9 cm.',
         'E': '62 cm uses a 9 cm mount at the top too, but the top mount is 6 cm.'},
    fast='Height only: 40 + 6 + 9 + 2 + 2 = 59.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _sales():
    v = [123, 106, 87, 114, 90, 106, 124, 113, 131, 77, 92, 75]
    m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    X = lambda i: 70 + i * 48
    Yv = lambda val: 262 - (val - 70) * 3
    parts = [line(50, 262, 610, 262, k='ink', w=1.6), line(50, 262, 50, 40, k='ink', w=1.6)]
    lab = []
    for t in (80, 100, 120):
        parts.append(line(46, Yv(t), 610, Yv(t), k='muted', w=0.8, dash=True))
        lab.append(text(42, Yv(t) + 5, t, k='muted', size=13, anchor='end'))
    parts.append(poly([(X(i), Yv(val)) for i, val in enumerate(v)], k='ink', sw=1.8, closed=False))
    for i, val in enumerate(v):
        parts.append(circle(X(i), Yv(val), 4, k='ink', fill='paper', sw=1.6))
        lab.append(text(X(i), 284, m[i], k='ink', size=15))
    jumps = {3: ('+27', 'red'), 5: ('+16', 'pen'), 6: ('+18', 'pen'), 8: ('+18', 'pen'), 10: ('+15', 'pen')}
    for i, (t, k) in jumps.items():
        y0, y1 = Yv(v[i - 1]), Yv(v[i])
        parts.append(line(X(i - 1), y0, X(i) - 10, y0, k='muted', w=1.2, dash=True))
        parts.append(line(X(i) - 10, y0, X(i) - 10, y1 + 4, k=k, w=3, head=True))
        lab.append(text(X(i) - 16, (y0 + y1) / 2 + 6, t, k=k, size=19 if k == 'red' else 16, anchor='end',
                        font='scrawl' if k == 'red' else 'hand'))
    parts.append(circle(X(3) - 22, (Yv(87) + Yv(114)) / 2, 24, k='red', sw=2))
    lab.append(text(330, 30, '2013 sales, with the jump into each option month', k='ink', size=17))
    return svg(640, 300, rough(*parts) + ''.join(lab),
               'Line graph of 2013 monthly car sales with the rise into each option month marked: April +27, June +16, July +18, September +18, November +15')


Q.append(dict(
    n=3, orig=7, answer='A', topic='Tables & differences',
    question=f"""<p>Below is a summary of all the second-hand cars sold by Bargain Cars during 2012 and 2013:</p>
{table([['2012', '85', '83', '98', '102', '118', '135', '88', '97', '116', '83', '125', '128'],
        [hl('2013', 'y', 1), '123', '106', hl('87', 'g'), hl('114', 'g', 2), '90', '106', '124', '113', '131', '77', '92', '75']],
       head=['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])}
<p class="stem">Which month of 2013 saw the {hl('<b>biggest increase</b>', 'b', 3)} in sales compared with the {hl('previous month', 'p', 4)}?</p>""",
    options={'A': 'April', 'B': 'June', 'C': 'July', 'D': 'September', 'E': 'November'},
    notes=[(1, 'y', 'Only the 2013 row matters. The 2012 row is a distraction (except December 2012, which nobody needs here).'),
           (2, 'g', 'Example: April is compared with <b>March</b> of the same year: 87 → 114.'),
           (3, 'b', 'Biggest jump <b>up</b>. Falls don’t count, and the highest month isn’t automatically the biggest jump.'),
           (4, 'p', 'Previous <b>month</b>, not the same month the year before.')],
    steps=[
        f"""<p>Only check the five option months. For each, take away the month just before it (2013 row):</p>
{calc(f'April: 114 − 87 = <b>+27</b>', 'June: 106 − 90 = +16', 'July: 124 − 106 = +18',
      'September: 131 − 113 = +18', 'November: 92 − 77 = +15')}""",
        f"""<p>See it on a sketch of 2013: April’s jump is clearly the tallest.</p>{_sales()}
{calc(f'biggest increase = +27 in {boxed("April")}')}
{note('Even as a percentage, April wins: 27 on 87 is about 31%, the next best is November (15 on 77, about 19%).', 'check')}""",
    ],
    answer_text='April: up 27 cars on March (87 → 114).',
    why={'B': 'June only rises by 16 (90 → 106).',
         'C': 'July rises by 18 on June. It is the biggest rise on the <b>year before</b> (88 → 124), which is the wrong comparison.',
         'D': 'September has the highest sales of 2013 (131), but it only rose by 18 on August.',
         'E': 'November rises by just 15 (77 → 92).'},
    fast='Five subtractions, 2013 row only: Apr 27, Jun 16, Jul 18, Sep 18, Nov 15. April.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _lawn():
    s = 18
    x0, y0 = 70, 40
    parts = [rect(x0, y0, 25 * s, 10 * s, k='green', fill='g', sw=2.4)]
    for i in range(1, 9):
        parts.append(line(x0 + 4, y0 + i * 20, x0 + 25 * s - 4 - (3 * s if i <= 1 else 0), y0 + i * 20, k='green', w=1, dash=True))
    parts.append(rect(x0 + 22 * s, y0, 3 * s, 2 * s, k='orange', fill='o', sw=2.2))
    parts.append(line(x0, y0 + 10 * s + 18, x0 + 25 * s, y0 + 10 * s + 18, k='ink', w=1.6, head=True, tail=True))
    parts.append(line(x0 - 18, y0, x0 - 18, y0 + 10 * s, k='ink', w=1.6, head=True, tail=True))
    lab = [text(x0 + 12.5 * s, y0 + 10 * s + 40, '25 m', k='ink', size=19),
           text(x0 - 26, y0 + 5 * s + 6, '10 m', k='ink', size=19, anchor='end'),
           text(x0 + 23.5 * s, y0 + 2 * s + 20, 'patio 3 × 2', k='orange', size=15),
           text(x0 + 23.5 * s, y0 + 2 * s + 38, '= 6 m²', k='orange', size=15),
           text(x0 + 11 * s, y0 + 5 * s - 4, 'grass: 250 − 6 = 244 m²', k='ink', size=22, font='scrawl'),
           text(x0 + 11 * s, y0 + 5 * s + 26, 'old 1 m²/min → 244 min', k='pen', size=18),
           text(x0 + 11 * s, y0 + 5 * s + 50, 'new 2 m²/min → 122 min', k='pen', size=18)]
    return svg(600, 290, rough(*parts) + ''.join(lab),
               'Lawn 25 m by 10 m with a 3 m by 2 m patio in the corner; grass area 244 square metres')


Q.append(dict(
    n=4, orig=8, answer='A', topic='Area & rates',
    question=f"""<p>Rosie needs to mow her lawn. She has just bought a new lawn mower, and believes she can
mow at a rate of {hl('2 m² a minute', 'g', 1)}. With her old mower, she could only mow the lawn at a rate of
{hl('1 m² a minute', 'g', 2)}. Her lawn is {hl('10 m by 25 m', 'g', 3)}. There is a {hl('patio in one corner which is 2 m by 3 m and
which she does not need to mow', 'p', 4)}.</p>
<p class="stem">How much {hl('<b>time does she save</b>', 'b', 5)} with her new lawn mower?</p>""",
    options={'A': '122 minutes', 'B': '125 minutes', 'C': '128 minutes', 'D': '244 minutes', 'E': '250 minutes'},
    notes=[(1, 'g', 'New: twice as fast.'),
           (2, 'g', 'Old: 1 m² a minute, so minutes = square metres.'),
           (3, 'g', 'Whole lawn = 10 × 25 = 250 m².'),
           (4, 'p', 'Take the patio <b>off</b>: 2 × 3 = 6 m² less to mow.'),
           (5, 'b', 'The saving is the <b>difference</b> between the two times, not either time on its own.')],
    steps=[
        f"""<p>Sketch the garden and find the grass that actually gets mown:</p>{_lawn()}""",
        f"""{calc('old time: 244 ÷ 1 = 244 minutes', 'new time: 244 ÷ 2 = 122 minutes',
                  f'saving: 244 − 122 = {boxed("122 minutes")}')}
{note('Twice as fast means the new time is half the old time, so the saving is also half: 244 ÷ 2 = 122.', 'tip')}""",
    ],
    answer_text='122 minutes saved.',
    why={'B': '125 forgets the patio: 250 ÷ 2 = 125.',
         'C': '128 adds the patio on instead of taking it off: 256 ÷ 2 = 128.',
         'D': '244 is the old mowing time, not the time saved.',
         'E': '250 is the old time with the patio forgotten.'},
    fast='(250 − 6) = 244 m². Twice as fast saves half the old time: 122 minutes.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _coupons():
    vals = [(19, 'y'), (19, 'y'), (19, 'y'), (12, 'g'), (12, 'g'), (12, 'g'), (7, 'b')]
    parts, lab = [], []
    for i, (v, f) in enumerate(vals):
        x = 22 + i * 86
        parts.append(rect(x, 40, 74, 50, k='ink', fill=f, sw=1.8, rx=6))
        parts.append(rect(x + 5, 45, 64, 40, k='muted', fill='none', sw=1, rx=4).replace('/>', ' stroke-dasharray="4 3"/>'))
        lab.append(text(x + 37, 73, f'{v}p', k='ink', size=22, font='scrawl'))
    parts.append(brace(22, 22 + 3 * 86 - 12, 98, '3 × 19 = 57', k='red'))
    parts.append(brace(22 + 3 * 86, 22 + 6 * 86 - 12, 98, '3 × 12 = 36', k='red'))
    lab += [text(22 + 6 * 86 + 37, 130, '7', k='red', size=17),
            text(320, 168, '57 + 36 + 7 = 100p = £1  ✓', k='green', size=22, font='scrawl'),
            text(320, 24, 'seven coupons', k='muted', size=16)]
    return svg(640, 184, rough(*parts) + ''.join(lab),
               'Seven coupons: three 19p, three 12p and one 7p, totalling 100p')


Q.append(dict(
    n=5, orig=12, answer='C', topic='Combinations & totals',
    question=f"""<p>Tasty Crisps are currently running a promotion in which there is one money-off coupon inside
every packet. Some coupons are worth 19p, some are worth 12p and others are worth 7p.</p>
<p>My friend tells me that he has {hl('at least one of each value', 'y', 1)} and his {hl('seven coupons', 'g', 2)} have a total
value of {hl('exactly £1', 'g', 3)}.</p>
<p class="stem">How many of my friend’s coupons are {hl('<b>worth 19p</b>', 'b', 4)}?</p>""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'y', 'Free information! Put one 19p, one 12p and one 7p aside straight away.'),
           (2, 'g', 'Exactly 7 coupons, no more, no fewer.'),
           (3, 'g', '£1 = 100p.'),
           (4, 'b', 'Only the number of 19p coupons is wanted, but you’ll find all three.')],
    steps=[
        f"""<p>Use the free information first: take one of each out.</p>
{calc('19 + 12 + 7 = 38p used', f'left: 4 coupons worth 100 − 38 = <b>62p</b>')}""",
        f"""<p>Now find 4 coupons that make 62p. Try different numbers of extra 19s:</p>
{calc(f'no 19s: 4 × 12 = 48 at most {ar()} too small {cross()}',
      f'one 19: 62 − 19 = 43 from three 12s/7s, but 3 × 12 = 36 at most {cross()}',
      f'two 19s: 62 − 38 = 24 = 12 + 12 {tick()}',
      f'three 19s: 62 − 57 = 5 from one coupon {cross()}')}""",
        f"""<p>So he has 1 + 2 = <b>three</b> 19p coupons, 1 + 2 = three 12p coupons and one 7p coupon.</p>
{_coupons()}
{calc(f'number of 19p coupons = {boxed("3")}')}""",
    ],
    answer_text='3 coupons are worth 19p (3 × 19 + 3 × 12 + 1 × 7 = 100).',
    why={'A': 'With one 19p, the other six coupons (12p and 7p) would have to make 81p. Even six 12s only make 72p.',
         'B': 'With two 19s, five 12p/7p coupons must make 62p. That needs 12 × b + 7 × c = 62 with b + c = 5, which has no whole-number answer (it gives b = 5.4).',
         'D': 'With four 19s (76p), three coupons must make 24p and include a 12 and a 7. 12 + 7 + anything is at least 26p.',
         'E': 'With five 19s (95p), only 5p is left for two coupons, but you need a 12p and a 7p.'},
    fast='Remove one of each (38p): 4 coupons make 62p. 19 + 19 + 12 + 12 = 62, so 3 × 19p in total.',
))


# ---------------------------------------------------------------- 6 (Q13)
TEAMS = ['Amazon', 'Danube', 'Ganges', 'Hudson', 'Nile', 'Orinoco', 'Rhine', 'Tigris', 'Volga', 'Yangtze']
RES = {
    'Amazon': ['', '2–2', '2–1', '4–0', '1–1', '2–1', '1–3', '2–0', '1–2', '1–1'],
    'Danube': ['1–3', '', '1–4', '2–1', '2–3', '0–1', '2–1', '0–0', '2–5', '0–1'],
    'Ganges': ['2–2', '3–1', '', '2–0', '1–2', '2–3', '1–3', '1–2', '3–1', '2–0'],
    'Hudson': ['1–2', '0–1', '2–1', '', '0–1', '1–3', '2–1', '1–0', '1–4', '0–0'],
    'Nile': ['2–0', '3–0', '1–2', '3–1', '', '1–0', '3–3', '2–3', '2–0', '1–2'],
    'Orinoco': ['4–1', '0–0', '3–1', '2–0', '3–2', '', '2–2', '3–1', '1–2', '2–0'],
    'Rhine': ['2–3', '2–1', '1–1', '3–0', '1–2', '2–0', '', '3–0', '2–2', '3–1'],
    'Tigris': ['1–1', '2–2', '1–3', '1–0', '2–0', '0–2', '0–3', '', '2–4', '1–0'],
    'Volga': ['3–2', '3–0', '2–1', '4–1', '2–2', '1–0', '1–2', '4–0', '', '1–1'],
    'Yangtze': ['0–2', '1–2', '2–0', '2–1', '3–1', '0–3', '0–2', '2–0', '1–3', ''],
}


def _vert(t):
    return f'<span style="writing-mode:vertical-rl;transform:rotate(180deg);display:inline-block">{t}</span>'


def _league_table():
    rows = []
    for t in TEAMS:
        rows.append([f'<b>{t}</b>'] + [c if c else '<span style="color:#9a9a9a">▓</span>' for c in RES[t]])
    head = ['<i>home team</i> ↓ &nbsp; <i>away team</i> →'] + [_vert(t) for t in TEAMS]
    return table(rows, head=head)


def _rhine():
    c = 40
    x0, y0 = 110, 64
    r = TEAMS.index('Rhine')
    parts, lab = [], []
    for i, t in enumerate(TEAMS):
        lab.append(text(x0 - 8, y0 + i * c + 26, t, k='green' if i == r else 'muted', size=14, anchor='end',
                        weight='700' if i == r else None))
        lab.append(text(x0 + i * c + c / 2 + 5, y0 - 8, t, k='pen' if i == r else 'muted', size=14, anchor='start', rotate=-90,
                        weight='700' if i == r else None))
    for i in range(10):
        for j in range(10):
            fill = 'g' if i == r else ('b' if j == r else 'none')
            if i == j:
                fill = 'paper'
            parts.append(rect(x0 + j * c, y0 + i * c, c, c, k='muted', fill=fill, sw=1))
    for j, t in enumerate(TEAMS):
        if j == r:
            continue
        h, a = RES['Rhine'][j].split('–')
        lab.append(text(x0 + j * c + c / 2, y0 + r * c + 26,
                        f'<tspan class="c-red" font-weight="700">{h}</tspan>–{a}', k='ink', size=15, font='print'))
    for i, t in enumerate(TEAMS):
        if i == r:
            continue
        h, a = RES[t][r].split('–')
        lab.append(text(x0 + r * c + c / 2, y0 + i * c + 26,
                        f'{h}–<tspan class="c-red" font-weight="700">{a}</tspan>', k='ink', size=15, font='print'))
    lab += [text(x0 + 200, y0 + 10 * c + 32, 'Rhine’s ROW = home games: Rhine’s goals are the FIRST number', k='green', size=17),
            text(x0 + 200, y0 + 10 * c + 56, 'Rhine’s COLUMN = away games: Rhine’s goals are the SECOND number', k='pen', size=17),
            text(x0 + 200, y0 + 10 * c + 84, 'red numbers: no 0 anywhere, so Rhine always scored', k='red', size=20, font='scrawl')]
    return svg(560, 560, rough(*parts) + ''.join(lab),
               'Grid of the league with only Rhine’s row and column filled in; Rhine’s own goals are shown in red and none is zero')


Q.append(dict(
    n=6, orig=13, answer='D', topic='Tables & checking',
    question=f"""<p>The following table summarises the results of all the matches played last season in a football
league. {hl('(The home team’s score is always given first.)', 'y', 1)} Each team plays every other team in the
league twice; {hl('once at home and once away', 'p', 2)}.</p>
{_league_table()}
<p class="stem">Which was the {hl('only', 'g', 3)} team that {hl('<b>scored at least one goal in every match</b>', 'b', 4)} they played last season?</p>""",
    options={'A': 'Amazon', 'B': 'Ganges', 'C': 'Nile', 'D': 'Rhine', 'E': 'Volga'},
    notes=[(1, 'y', 'Row = home team, so in a team’s <b>row</b> its goals are the <b>first</b> number.'),
           (2, 'p', 'Every team is in the table twice: its row (home) <b>and</b> its column (away). Check both!'),
           (3, 'g', 'Exactly one option survives. Four of them must have a 0 somewhere.'),
           (4, 'b', 'You are hunting for a 0 next to the team’s name. One 0 knocks a team out.')],
    steps=[
        f"""<p>How to read the table for one team (here Rhine):</p>{_rhine()}""",
        f"""<p>Home rows first: Amazon, Ganges, Nile, Rhine and Volga have <b>no</b> 0 as their first number. So the away games decide it.
Look down each option’s column at the <b>second</b> numbers:</p>
{calc(f'Amazon: away at Nile 2–<b>0</b> {cross()}', f'Ganges: away at Yangtze 2–<b>0</b> {cross()}',
      f'Nile: away at Tigris 2–<b>0</b> {cross()}', f'Volga: away at Nile 2–<b>0</b> {cross()}',
      f'Rhine: 3, 1, 3, 1, 3, 2, 3, 2, 2 {ar()} no 0 {tick()}')}
{calc(f'only team always scoring = {boxed("Rhine")}')}
{note('Scanning a column, cover the first number with your finger and only read the second.', 'tip')}""",
    ],
    answer_text='Rhine: it scored in every home game and every away game.',
    why={'A': 'Amazon lost 2–0 away at Nile (Nile’s row, Amazon’s column).',
         'B': 'Ganges lost 2–0 away at Yangtze.',
         'C': 'Nile lost 2–0 away at Tigris.',
         'E': 'Volga lost 2–0 away at Nile.'},
    fast='All five options score in every home game, so only check columns (second numbers). Every option except Rhine has a 2–0 away defeat.',
))


# ---------------------------------------------------------------- 7 (Q14)
P1 = [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)]
P2 = [(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2)]
P3 = [(0, 0), (1, 0), (2, 0)] + [(c, r) for r in (1, 2) for c in range(5)]
P4 = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (1, 2)]
P5 = [(2, 0)] + [(c, r) for r in (1, 2, 3) for c in range(3)]


def _pieces():
    c = 20
    parts, lab = [], []
    x = 20
    for name, cells, w, f in (('1', P1, 3, 'g'), ('2', P2, 4, 'b'), ('3', P3, 5, 'v'), ('4', P4, 3, 'y'), ('5', P5, 3, 'o')):
        h = max(r for _, r in cells) + 1
        y0 = 40 + (4 - h) * c
        parts += _cells(cells, x, y0, c, f)
        lab.append(text(x + w * c / 2, 22, f'piece {name}', k='ink', size=16))
        lab.append(text(x + w * c / 2, 144, f'{len(cells)} squares', k='red', size=18, font='scrawl'))
        x += w * c + 30
    return svg(560, 156, rough(*parts) + ''.join(lab),
               'The five pieces drawn on a grid: piece 1 has 7 squares, 2 has 10, 3 has 13, 4 has 7, 5 has 10')


def _gap_and_fit():
    c = 32
    parts, lab = [], []
    # left: the gap seen from above
    gx, gy = 40, 50
    for i in range(6):
        for j in range(6):
            pill = i < 3 and j < 3
            parts.append(rect(gx + i * c, gy + j * c, c, c, k='muted', fill='paper' if pill else 'p', sw=1))
    for d in range(0, 3 * c + 1, 12):
        parts.append(line(gx + d, gy, gx, gy + d, k='muted', w=1))
        parts.append(line(gx + 3 * c, gy + d, gx + d, gy + 3 * c, k='muted', w=1))
    parts.append(poly([(gx + 3 * c, gy), (gx + 6 * c, gy), (gx + 6 * c, gy + 6 * c), (gx, gy + 6 * c), (gx, gy + 3 * c),
                       (gx + 3 * c, gy + 3 * c)], k='red', sw=2.6))
    lab += [text(gx + 1.5 * c, gy + 1.5 * c + 6, 'pillar', k='ink', size=17, weight='700'),
            text(gx + 3 * c, 30, 'the gap, seen from above', k='ink', size=17),
            text(gx + 3 * c, gy + 6 * c + 26, '6 × 6 − 3 × 3 = 27 squares', k='red', size=19, font='scrawl'),
            text(gx + 4.5 * c, gy - 6, '3', k='muted', size=14), text(gx + 6 * c + 10, gy + 4.5 * c, '6', k='muted', size=14)]
    # right: the fit with 1, 2 and 5
    fx = 360
    two = [(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2), (4, 3)]
    five = [(0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
    one = [(3, 3), (5, 3), (3, 4), (4, 4), (5, 4), (4, 5), (5, 5)]
    parts += _cells(two, fx, gy, c, 'b') + _cells(five, fx, gy, c, 'o') + _cells(one, fx, gy, c, 'g')
    lab += [text(fx + 4.5 * c, gy + 1.5 * c + 8, '2', k='pen', size=34, font='scrawl'),
            text(fx + 1.5 * c, gy + 4.5 * c + 8, '5', k='orange', size=34, font='scrawl'),
            text(fx + 4.5 * c, gy + 4.5 * c + 10, '1', k='green', size=30, font='scrawl'),
            text(fx + 3 * c, 30, 'pieces 1, 2 and 5 fill it', k='ink', size=17),
            text(fx + 3 * c, gy + 6 * c + 26, '2 and 5 turned a quarter turn', k='ink', size=16),
            text(fx + 3 * c, gy + 6 * c + 46, '1 as drawn', k='ink', size=16)]
    parts.append(arrow(gx + 6 * c + 30, gy + 3 * c, fx - 24, gy + 3 * c, k='red', bend=-0.15))
    return svg(620, 300, rough(*parts) + ''.join(lab),
               'Left: the gap is a 6 by 6 square with a 3 by 3 corner under the pillar, 27 squares. Right: piece 2 fills one arm, piece 5 the other and piece 1 the corner')


Q.append(dict(
    n=7, orig=14, answer='A', topic='Shapes & fitting',
    question=f"""<p>A tiler has encountered a problem when tiling a kitchen floor. He is {hl('one tile short', 'y', 1)} of completing
the job. This is indicated by the greyed-out area in the diagram below which shows part of the
kitchen floor:</p>
{fig(Y, 'ps_q07_floor', 'A square pillar stands on the floor; the grey area is one square tile with the pillar base taking up its back corner', 300)}
<p>There are some odd pieces of tile left over that could be used to complete the job. {hl('Three of
these, if combined, would fit the area exactly', 'g', 2)}.</p>
{fig(Y, 'ps_q07_pieces', 'Five tile pieces numbered 1 to 5, each made of small squares', 480)}
<p class="stem">Which three pieces of tile could be pieced together to fit into the {hl('<b>remaining corner area</b>', 'b', 3)}? ({hl('The
tiles are shown face up and cannot be laid face down', 'p', 4)}.)</p>""",
    options={'A': '1, 2 and 5', 'B': '1, 3 and 5', 'C': '1, 4 and 5', 'D': '2, 3 and 4', 'E': '2, 4 and 5'},
    notes=[(1, 'y', 'The gap is one square tile, minus the bit the pillar stands on.'),
           (2, 'g', '“Exactly” = the areas must add up to the gap’s area. Great for ruling options out fast.'),
           (3, 'b', 'An L shape: the tile with a square bitten out of one corner.'),
           (4, 'p', 'You may <b>turn</b> a piece round, but you may not flip it over.')],
    steps=[
        f"""<p>Look down on the grey tile from above. The pillar’s base covers one corner and is half as wide as the tile.
On a grid of small squares (the size of the bumps on the pieces) the gap is an L:</p>{_gap_and_fit()}""",
        f"""<p>Count the small squares in each piece (each one is a 3 × 3 block with squares added or bitten out):</p>{_pieces()}""",
        f"""<p>The three pieces must add up to <b>27</b>:</p>
{calc(f'A: 7 + 10 + 10 = 27 {tick()}', f'B: 7 + 13 + 10 = 30 {cross()}', f'C: 7 + 7 + 10 = 24 {cross()}',
      f'D: 10 + 13 + 7 = 30 {cross()}', f'E: 10 + 7 + 10 = 27 {tick()}')}
<p>Only A and E are left. Try A: pieces 2 and 5 are both “3 × 3 plus a bump”, so they make the two arms of the L. Their bumps poke
into the corner square, and piece 1 fits the hole that is left (see the sketch in Step 1).</p>
{calc(f'1, 2 and 5 fit exactly {ar()} {boxed("A")}')}""",
        f"""{note('Honest warning: 2, 4 and 5 also make 27, and they can be fitted too if every piece is turned half a turn (2 and 5 in the arms with different bump positions, 4 in the corner). So this question really has two fits. The official answer is A, the fit the question was built around. In the exam, once the area check leaves two options, try the first one; as soon as it fits, choose it and move on.', 'trap')}""",
    ],
    answer_text='Pieces 1, 2 and 5 (7 + 10 + 10 = 27 squares) fit the L-shaped gap.',
    why={'B': '1, 3 and 5 make 30 squares, 3 too many. Piece 3 is too big.',
         'C': '1, 4 and 5 make only 24 squares, 3 too few.',
         'D': '2, 3 and 4 make 30 squares, too many.',
         'E': '2, 4 and 5 have the right area (27) and the official key does not accept them. Strictly, they can also be fitted with half turns, so this option is a flaw in the question rather than a mistake you could spot. Go with A.'},
    fast='Gap = 6 × 6 − 3 × 3 = 27 squares. Pieces: 7, 10, 13, 7, 10. Only A and E make 27; A fits (2 and 5 in the arms, 1 in the corner).',
))


# ---------------------------------------------------------------- 8 (Q18)
def _room():
    s = 18
    x0, y0 = 60, 40
    parts = [rect(x0, y0, 8 * s, 4 * s, k='pen', fill='b', sw=2.2)]
    xs = [x0, x0 + 8 * s, x0 + 12 * s, x0 + 20 * s, x0 + 24 * s]
    wy = y0 + 4 * s
    for a, b in zip(xs, xs[1:]):
        parts.append(rect(a, wy, b - a, 3 * s, k='green', fill='g', sw=2.2))
    # door and windows (not painted)
    parts += [rect(x0 + 9.2 * s, wy + 0.8 * s, 1.4 * s, 2.2 * s, k='orange', fill='o', sw=1.6),
              rect(x0 + 13.5 * s, wy + 0.7 * s, 2 * s, 1.2 * s, k='muted', fill='paper', sw=1.6),
              rect(x0 + 17 * s, wy + 0.7 * s, 2 * s, 1.2 * s, k='muted', fill='paper', sw=1.6),
              rect(x0 + 21 * s, wy + 0.7 * s, 2 * s, 1.2 * s, k='muted', fill='paper', sw=1.6)]
    lab = [text(x0 + 4 * s, y0 + 2 * s - 2, 'ceiling', k='pen', size=17),
           text(x0 + 4 * s, y0 + 2 * s + 18, '8 × 4 = 32 m²', k='pen', size=17)]
    for (a, b), t in zip(zip(xs, xs[1:]), ('8', '4', '8', '4')):
        lab.append(text((a + b) / 2, wy + 3 * s + 20, f'{t} m', k='ink', size=16))
    lab += [text(x0 - 8, wy + 1.5 * s + 6, '3 m', k='ink', size=16, anchor='end'),
            text(x0 + 4 * s, wy + 1.5 * s + 14, 'walls', k='green', size=17),
            text(x0 + 12 * s, wy + 3 * s + 46, 'walls unrolled: (8 + 4 + 8 + 4) × 3 = 24 × 3 = 72 m²', k='green', size=17),
            text(x0 + 16 * s, y0 + 2 * s + 6, 'door + windows: −10 m²', k='orange', size=17)]
    # paint tin
    tx = 535
    parts += [rect(tx, 100, 70, 84, k='ink', fill='y', sw=2.2, rx=6), line(tx, 116, tx + 70, 116, k='ink', w=1.6),
              path(f'M{tx + 12} 100 Q{tx + 35} 70 {tx + 58} 100', k='ink', sw=2)]
    lab += [text(tx + 35, 146, '8 litres', k='ink', size=16), text(tx + 35, 168, '= 96 m²', k='red', size=17, font='scrawl')]
    return svg(640, 280, rough(*parts) + ''.join(lab),
               'Room unfolded: ceiling 8 by 4 above four walls of lengths 8, 4, 8, 4 and height 3; door and windows marked; an 8 litre tin covers 96 square metres')


Q.append(dict(
    n=8, orig=18, answer='A', topic='Area & rounding up',
    question=f"""<p>I am planning to repaint the {hl('walls and the ceiling', 'y', 1)} of my dining room. The room has the shape of
a rectangular box and is {hl('8 m long, 4 m wide and 3 m high', 'g', 2)}. I do not need to paint the door and
the three windows, the combined surface area of which is {hl('10 m²', 'p', 3)}. Paint is sold in {hl('8-litre tins', 'p', 4)} and
{hl('1 litre of paint is sufficient for a surface area of 12 m²', 'g', 5)}.</p>
<p class="stem">How many {hl('<b>tins</b>', 'b', 6)} of paint do I need to buy?</p>""",
    options={'A': '1', 'B': '2', 'C': '6', 'D': '8', 'E': '17'},
    notes=[(1, 'y', 'Four walls + ceiling. <b>Not</b> the floor.'),
           (2, 'g', 'Walls: two are 8 × 3, two are 4 × 3. Ceiling: 8 × 4.'),
           (3, 'p', 'Take this off the total.'),
           (4, 'p', 'One tin = 8 litres. The answer is in tins, not litres!'),
           (5, 'g', 'So one tin covers 8 × 12 = 96 m².'),
           (6, 'b', 'Whole tins only, so round up at the end.')],
    steps=[
        f"""<p>Unfold the room: the four walls make one long strip, with the ceiling on top.</p>{_room()}""",
        f"""{calc('walls: 24 × 3 = 72 m²', 'ceiling: 8 × 4 = 32 m²', 'paint: 72 + 32 − 10 = <b>94 m²</b>')}""",
        f"""{calc(f'litres: 94 ÷ 12 = 7.8… {ar()} 8 litres', f'one 8-litre tin covers 96 m² ≥ 94 m² {ar()} {boxed("1 tin")}')}
{note('Quicker: find what one tin covers (8 × 12 = 96 m²) and compare it with 94 m². No division needed.', 'tip')}""",
    ],
    answer_text='1 tin: 94 m² needs 7.8 litres, and one tin holds 8 litres.',
    why={'B': '2 tins: you only need that if you paint the floor too (126 m² needs 10.5 litres).',
         'C': '6 is the litres for the walls alone (72 ÷ 12), and it’s litres, not tins.',
         'D': '8 is the number of <b>litres</b> needed, not tins.',
         'E': '17 is all six faces (136 m²) ÷ 8: it paints the floor and mixes up the tin size with the coverage.'},
    fast='Walls 72 + ceiling 32 − 10 = 94 m². One tin covers 8 × 12 = 96 m². So 1 tin.',
))
