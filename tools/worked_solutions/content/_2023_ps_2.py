import math
from wslib import *

Y = 2023
Q = []


def _sector(cx, cy, r, a0, a1, fill):
    """Pie slice from angle a0 to a1 (degrees, clockwise from 12 o'clock)."""
    p = lambda a: (cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    big = 1 if a1 - a0 > 180 else 0
    return path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z', k='ink', fill=fill, sw=1.8)


# ---------------------------------------------------------------- 9 (Q19)
def _fruit():
    parts, lab = [], []
    x0, c = 130, 46
    for j, d in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri']):
        lab.append(text(x0 + c * j + c / 2, 24, d, k='muted', size=15))
    for i, (name, f) in enumerate((('Jessica', 'o'), ('Bruce', 'o'), ('Victoria', 'g'))):
        y = 34 + c * i
        lab.append(text(x0 - 12, y + c / 2 + 6, name, k='ink', size=17, anchor='end'))
        for j in range(5):
            parts.append(rect(x0 + c * j, y, c, c, k='muted', sw=1.2))
            parts.append(circle(x0 + c * j + c / 2, y + c / 2, 13, k='ink', fill=f, sw=1.6))
    lab += [text(x0 + 5 * c + 24, 76, '10 oranges', k='orange', size=22, anchor='start', font='scrawl'),
            text(x0 + 5 * c + 24, 106, '(2 children × 5 days)', k='muted', size=15, anchor='start'),
            text(x0 + 5 * c + 24, 152, '5 apples', k='green', size=22, anchor='start', font='scrawl')]

    def bag(x, y, fills, name):
        out = [rect(x, y, 96, 58, k='ink', fill='paper', sw=1.8, rx=10)]
        t = [text(x + 48, y + 76, name, k='muted', size=14)]
        for n, f in enumerate(fills):
            cx, cy = x + 18 + 30 * (n % 3), y + 16 + 26 * (n // 3)
            out.append(circle(cx, cy, 10, k='ink' if f != 'paper' else 'muted', fill=f, sw=1.4))
            if f == 'paper':
                t.append(text(cx, cy + 5, '?', k='muted', size=14))
        return out, t

    rows = [([('o' * 6, 'orange bag'), ('o' * 6, 'orange bag'), ('g' * 6, 'apple bag')], '109 + 109 + 99 = 317p', 'sure', 'green'),
            ([('o' * 6, 'orange bag'), ('ooo' + 'ggg', 'half & half'), ('ooo' + 'ggg', 'half & half')], '109 + 105 + 105 = 319p', 'sure, but dearer', 'ink'),
            ([('og' + '????', 'lucky dip'), ('og' + '????', 'lucky dip'), ('og' + '????', 'lucky dip')], '95 + 95 + 95 = 285p', 'NOT sure', 'red')]
    for i, (bags, cost, verdict, k) in enumerate(rows):
        y = 206 + 100 * i
        for j, (fills, name) in enumerate(bags):
            fl = ['paper' if ch == '?' else ch for ch in fills]
            o, t = bag(20 + 110 * j, y, fl, name)
            parts += o
            lab += t
        lab.append(text(366, y + 26, cost, k=k, size=18, anchor='start'))
        lab.append(text(366, y + 52, verdict, k=k, size=20, anchor='start', font='scrawl'))
    return svg(640, 500, rough(*parts) + ''.join(lab),
               'A week grid: Jessica and Bruce need 10 oranges, Victoria 5 apples; then three ways to buy bags: two orange bags and an apple bag for 317p (sure), an orange bag and two half-and-half bags for 319p, three lucky dips for 285p (not sure)')


Q.append(dict(
    n=9, orig=19, answer='D', topic='Best buy & worst case',
    question=f"""<p>I need to make sure that my {hl('three children', 'g', 1)} all have a piece of fruit to take to school on each of
the {hl('five days', 'g')} next week. {hl('Jessica and Bruce will not eat apples and Victoria will not eat oranges', 'y', 2)}.
My local shop sells a variety of bags containing either just apples, just oranges or different
mixtures of the two fruits. The options available are shown below:</p>
{table([['apple bag', '6', '0', '99', '6'], ['orange bag', '0', '6', '109', '6'],
        ['lucky dip', hl('at least 1', 'p', 3), hl('at least 1', 'p'), '95', '6'], ['half and half', '3', '3', '105', '6']],
       head=['option', 'apples', 'oranges', 'price (p)', 'total number in bag'])}
<p class="stem">What is the {hl('<b>minimum</b>', 'b', 4)} that I could spend to be {hl('<b>sure</b>', 'p', 5)} that I have enough fruit for all three children
next week?</p>""",
    options={'A': '£2.85', 'B': '£2.99', 'C': '£3.04', 'D': '£3.17', 'E': '£3.19'},
    notes=[(1, 'g', '3 children × 5 days = 15 pieces. But the <b>type</b> of fruit matters.'),
           (2, 'y', 'Two children want oranges: 2 × 5 = <b>10 oranges</b>. One wants apples: <b>5 apples</b>.'),
           (3, 'p', 'A lucky dip only promises 1 apple and 1 orange. The other 4 could be anything.'),
           (4, 'b', 'Cheapest.'),
           (5, 'p', '“Sure” means it must work even if every lucky dip is as unhelpful as possible.')],
    steps=[
        f"""<p>What do we actually need? Draw the week:</p>
{_fruit()}""",
        f"""<p>Lucky dips only guarantee 1 orange each, so they are a poor way to get 10 oranges. Build from the guaranteed bags:</p>
{calc(f'2 orange bags + 1 apple bag {ar()} 12 oranges, 6 apples {tick()} 109 + 109 + 99 = <b>317p</b>',
      f'1 orange bag + 2 half and half {ar()} 12 oranges, 6 apples {tick()} 109 + 105 + 105 = 319p',
      f'3 half and half {ar()} only 9 oranges {cross()}, a 4th bag pushes it over £4')}
{calc(f'minimum = 317p = {boxed("£3.17")}')}
{note('Count only what each bag <b>promises</b>: orange bag 6 oranges, half and half 3 + 3, lucky dip 1 + 1. Just two sets of 3 bags promise 10 oranges and 5 apples (317p and 319p). Any 4 bags cost at least 4 × 95p = £3.80.', 'check')}""",
    ],
    answer_text='£3.17: two orange bags and one apple bag.',
    why={'A': '£2.85 is three lucky dips. 18 fruit, but you can only be sure of 3 oranges and 3 apples.',
         'B': '£2.99 (for example an orange bag + two lucky dips) only guarantees 8 oranges and 2 apples. It might work, but you can’t be sure.',
         'C': '£3.04 isn’t the price of any set of bags: no mix of 95p, 99p, 105p and 109p adds to 304p.',
         'E': '£3.19 (an orange bag + two half-and-half bags) does work, but it costs 2p more than £3.17.'},
    fast='Need 10 oranges + 5 apples. Lucky dips are useless when you must be sure. Two orange bags + an apple bag = 109p + 109p + 99p = £3.17.',
))


# ---------------------------------------------------------------- 10 (Q20)
_BLOCKS = [(0, 0, 1, 1), (0, 1, 2, 1), (0, 2, 1, 2), (0, 4, 2, 2), (0, 6, 1, 1), (0, 7, 1, 1), (0, 8, 2, 1), (1, 0, 2, 1),
           (1, 2, 1, 1), (1, 3, 2, 1), (1, 6, 2, 2), (2, 1, 2, 2), (2, 4, 1, 1), (2, 5, 2, 1), (2, 8, 2, 1), (3, 0, 2, 1),
           (3, 3, 2, 2), (3, 6, 1, 1), (3, 7, 2, 1), (4, 1, 1, 1), (4, 2, 2, 1), (4, 5, 2, 2), (4, 8, 1, 1), (5, 0, 2, 2),
           (5, 3, 1, 1), (5, 4, 2, 1), (5, 7, 2, 2), (6, 2, 2, 2), (6, 5, 1, 1), (6, 6, 2, 1), (7, 0, 1, 1), (7, 1, 1, 1),
           (7, 4, 1, 2), (7, 7, 1, 1), (7, 8, 1, 1)]


def _paving():
    c, x0, y0 = 36, 20, 34
    parts, lab = [], []
    count = {1: 0, 2: 0, 4: 0}
    fills = {1: 'y', 2: 'b', 4: 'g'}
    for r, col, h, w in _BLOCKS:
        size = h * w
        count[size] += 1
        parts.append(rect(x0 + col * c + 2, y0 + r * c + 2, w * c - 4, h * c - 4, k='ink', fill=fills[size], sw=1.6))
        lab.append(text(x0 + col * c + w * c / 2, y0 + r * c + h * c / 2 + 5, count[size], k='ink', size=14 if size == 1 else 16))
    lab.append(text(x0, 22, 'numbered as you count them', k='muted', size=14, anchor='start'))
    lx = 380
    for i, (size, name) in enumerate(((1, 'small squares'), (2, 'rectangles'), (4, 'big squares'))):
        y = 40 + 34 * i
        parts.append(rect(lx, y, 24, 24, k='ink', fill=fills[size], sw=1.4))
        lab.append(text(lx + 34, y + 19, f'{name}: {count[size]}', k='ink', size=18, anchor='start'))
    lab.append(text(lx, 166, 'total 35 blocks', k='red', size=20, anchor='start', font='scrawl'))
    lab.append(text(lx, 190, 'check: 14 + 13 × 2 + 8 × 4 = 72 = 9 × 8', k='muted', size=14, anchor='start'))
    # our pie
    cx, cy, r = 510, 284, 54
    a = 0
    for n, f in ((14, 'y'), (13, 'b'), (8, 'g')):
        parts.append(_sector(cx, cy, r, a, a + 360 * n / 35, f))
        a += 360 * n / 35
    lab += [text(cx + r + 10, cy - 18, '40%', k='ink', size=15, anchor='start'),
            text(cx - 30, cy + r + 18, '37%', k='ink', size=15),
            text(cx - r - 10, cy - 20, '23%', k='ink', size=15, anchor='end'),
            text(cx, cy - r - 10, '14 : 13 : 8', k='pen', size=17)]
    return svg(640, 362, rough(*parts) + ''.join(lab),
               'The paving redrawn: 14 small squares, 13 rectangles and 8 big squares, 35 blocks, and a pie of 14 to 13 to 8')


Q.append(dict(
    n=10, orig=20, answer='B', topic='Counting & pie charts',
    question=f"""<p>The block paved area shown below is laid using {hl('three different-sized blocks', 'y', 1)}.</p>
{fig(Y, 'ps_q10_paving', 'A rectangle of paving made of small squares, rectangles twice as long, and big squares four times the size', 300)}
<p class="stem">Which one of the following charts shows the relative comparison of the {hl('<b>number</b> of each size of block', 'b', 2)} used in this paved area?</p>
{fig(Y, 'ps_q10_pies', 'Five pie charts A to E, each with a dark, a mid-grey and a light-grey slice of different sizes', 520)}""",
    options={'A': 'chart A', 'B': 'chart B', 'C': 'chart C', 'D': 'chart D', 'E': 'chart E'},
    notes=[(1, 'y', 'Small squares, rectangles (2 small squares long) and big squares (2 × 2).'),
           (2, 'b', 'Count <b>blocks</b>, not area. A big square counts as 1, even though it covers 4 small squares.')],
    steps=[
        f"""<p>Count carefully, numbering each block as you go so you never count one twice:</p>
{_paving()}
{calc('small squares 14, rectangles 13, big squares 8', f'total = <b>35</b>')}
{note('Check your count with area: the paving is 9 × 8 = 72 small squares, and 14 + 13 × 2 + 8 × 4 = 72. It fits!', 'check')}""",
        f"""<p>Turn the counts into shares of the circle:</p>
{calc('14 out of 35 = 40% (a bit less than half)', '13 out of 35 ≈ 37% (almost the same as 40%)', '8 out of 35 ≈ 23% (about a quarter)')}
<p>So we need <b>two big, nearly equal slices</b> and <b>one slice of about a quarter</b>.</p>""",
        f"""<p>Check the charts:</p>
{calc(f'A: one slice is more than half {cross()}', f'B: about 40%, 37%, 23% {tick()}', f'C: three equal slices {cross()}',
      f'D: one tiny slice, one nearly half {cross()}', f'E: 40%, then two similar slices of about 30% {cross()}')}
{calc(f'{boxed("B")}')}""",
    ],
    answer_text='Chart B: 14 small squares, 13 rectangles and 8 big squares (40%, 37%, 23%).',
    why={'A': 'A has one slice bigger than half the circle. No block type is more than half of the 35.',
         'C': 'C has three equal slices, which would need about 12 of each type.',
         'D': 'D has a tiny slice (about 16%) and one nearly half. That looks more like the share of <b>area</b> (big squares cover the most ground), not the number of blocks.',
         'E': 'E gets the biggest slice right (40%) but makes the other two nearly equal (about 32% and 28%). We need 37% and 23%.'},
    fast='Count: 14 small, 13 rectangles, 8 big. Two nearly equal large slices plus one quarter-ish slice: only B.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _rink():
    cw, ch, x0, y0 = 80, 54, 40, 40
    parts, lab = [], []
    for j, d in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        lab.append(text(x0 + cw * j + cw / 2, 30, d, k='muted', size=16))
    dates = []
    day = 12
    for w in range(5):
        row = []
        for j in range(7):
            if w == 4 and j > 0:
                row.append(None)
                continue
            if day <= 31:
                lbl = str(day)
            else:
                lbl = f'{day - 31} Jan' if day - 31 == 1 else str(day - 31)
            row.append(lbl)
            day += 1
        dates.append(row)
    for w, row in enumerate(dates):
        for j, lbl in enumerate(row):
            if lbl is None:
                continue
            x, y = x0 + cw * j, y0 + ch * w
            sun = j == 6
            parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='muted' if sun else 'ink', fill='paper' if sun else 'none', sw=1.4))
            lab.append(text(x + 8, y + 19, lbl, k='muted' if sun else 'ink', size=14, anchor='start', font='print'))
            if sun:
                parts.append(line(x + 10, y + ch - 8, x + cw - 10, y + 10, k='muted', w=1.4))
                if lbl == '25':
                    lab.append(text(x + cw - 8, y + 19, 'Xmas', k='red', size=16, font='scrawl', anchor='end'))
            elif j == 5:
                parts.append(circle(x + cw / 2 - 8, y + 38, 8, k='orange', fill='o', sw=2.2))
                parts.append(circle(x + cw / 2 + 14, y + 38, 8, k='pen', fill='b', sw=2.2))
            else:
                parts.append(circle(x + cw / 2 + 14, y + 38, 8, k='pen', fill='b', sw=2.2))
    ly = y0 + 5 * ch + 22
    parts += [circle(x0 + 10, ly - 5, 8, k='pen', fill='b', sw=2.2), circle(x0 + 250, ly - 5, 8, k='orange', fill='o', sw=2.2)]
    lab += [text(x0 + 26, ly, '2 pm–5 pm session', k='ink', size=16, anchor='start'),
            text(x0 + 266, ly, 'Saturday 10 am–1 pm extra', k='ink', size=16, anchor='start'),
            text(x0, ly + 34, '25 blue + 4 orange = 29 sessions, each 2 h × £2 = £4', k='red', size=20, anchor='start', font='scrawl')]
    return svg(640, ly + 50, rough(*parts) + ''.join(lab),
               'Calendar from Monday 12 December to Monday 9 January: Sundays crossed out (Christmas Day is one of them), one session each weekday and Saturday afternoon, plus a Saturday morning session; 29 sessions')


Q.append(dict(
    n=11, orig=24, answer='E', topic='Calendars & counting',
    question=f"""<p>Every Christmas season, an ice-skating rink is laid in the central square in Boland. The rink is
open to the public {hl('from 12th December to 9th January inclusive', 'g', 1)}, between 2 pm and 5 pm. It is
{hl('closed on Sundays and Christmas Day (25th December)', 'p', 2)}, but there is an {hl('extra session on Saturdays', 'y', 3)} between 10 am and 1 pm. The charge is {hl('£2 an hour', 'g', 4)}.</p>
<p>When Jimmy was learning to skate, he went to the rink {hl('for two hours every session', 'y', 5)} that it was
open. That year, {hl('12th December was on a Monday', 'g', 6)}.</p>
<p class="stem">What is the total amount that Jimmy had to pay?</p>""",
    options={'A': '£100', 'B': '£104', 'C': '£108', 'D': '£112', 'E': '£116'},
    notes=[(1, 'g', 'Inclusive: count both end days. 12–31 Dec is 20 days, plus 9 in January = 29 days.'),
           (2, 'p', 'Check which day Christmas falls on! If it is a Sunday, the rink is shut anyway. Don’t take it off twice.'),
           (3, 'y', 'Saturdays have two sessions.'),
           (4, 'g', '2 hours × £2 = £4 per session.'),
           (5, 'y', 'He pays for 2 hours, not the whole 3-hour session.'),
           (6, 'g', 'Lets you find the weekday of every date.')],
    steps=[
        f"""<p>Find Christmas Day: 12 Dec is a Monday, so 18 Dec and 25 Dec are <b>Sundays</b>. Christmas is already a closed day.</p>
{_rink()}""",
        f"""<p>Count the sessions:</p>
{calc('29 days = 4 full weeks + Monday 9 Jan', f'Sundays: 18, 25 Dec, 1, 8 Jan = 4 closed {ar()} 29 − 4 = 25 afternoon sessions',
      f'Saturdays: 17, 24, 31 Dec, 7 Jan {ar()} 4 extra morning sessions', '25 + 4 = <b>29 sessions</b>')}""",
        f"""{calc(f'29 sessions × £4 = {boxed("£116")}')}
{note('29 × 4: do 30 × 4 = 120, then take off 4.', 'tip')}""",
    ],
    answer_text='£116: 29 two-hour sessions at £4 each.',
    why={'A': '£100 is 25 sessions: it forgets the 4 extra Saturday-morning sessions.',
         'B': '£104 is 26 sessions: three sessions too few, for example by losing 9 January (not counting inclusively), taking Christmas off again and missing a Saturday morning.',
         'C': '£108 is 27 sessions: takes Christmas off as an extra closed day <b>and</b> forgets that 9 January counts.',
         'D': '£112 is 28 sessions: takes Christmas Day off as well, but it is a Sunday, so it was already closed.'},
    fast='29 days from Mon 12 Dec, 4 Sundays (Christmas is one of them): 25 days + 4 Saturday extras = 29 sessions × £4 = £116.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _gift():
    parts, lab = [], []
    x0 = 120
    lab.append(text(x0 - 12, 50, 'sweets', k='ink', size=18, anchor='end'))
    for i in range(6):
        parts.append(rect(x0 + 52 * i, 30, 46, 32, k='ink', fill='y', sw=1.5, rx=4))
        lab.append(text(x0 + 52 * i + 23, 52, '20', k='ink', size=15))
    lab.append(text(x0 + 52 * 6 + 8, 44, '115 needed: 6 packs', k='ink', size=16, anchor='start'))
    lab.append(text(x0 + 52 * 6 + 8, 64, '6 × $0.45 = $2.70', k='pen', size=16, anchor='start'))
    lab.append(text(x0 - 12, 112, 'balloons', k='ink', size=18, anchor='end'))
    for i in range(2):
        parts.append(rect(x0 + 52 * i, 92, 46, 32, k='ink', fill='v', sw=1.5, rx=4))
        lab.append(text(x0 + 52 * i + 23, 114, '20', k='ink', size=15))
    lab.append(text(x0 + 116, 106, '23 needed: 2 packs', k='ink', size=16, anchor='start'))
    lab.append(text(x0 + 116, 126, '2 × $0.90 = $1.80', k='pen', size=16, anchor='start'))
    lab.append(text(x0 - 12, 178, 'toys', k='ink', size=18, anchor='end'))
    for i in range(23):
        f = 'o' if i < 10 else 'b'
        parts.append(rect(x0 + 21 * i, 160, 17, 28, k='ink', fill=f, sw=1.3, rx=2))
    parts.append(brace(x0, x0 + 21 * 10 - 4, 194, '', k='orange'))
    parts.append(brace(x0 + 21 * 10, x0 + 21 * 23 - 4, 194, '', k='pen'))
    lab += [text(x0 + 105, 236, 'first 10 × $3.50 = $35', k='orange', size=16),
            text(x0 + 21 * 16.5, 236, 'next 13 × $3.00 = $39', k='pen', size=16),
            text(x0, 276, '$2.70 + $1.80 + $35 + $39 = $78.50', k='red', size=22, anchor='start', font='scrawl')]
    return svg(640, 290, rough(*parts) + ''.join(lab),
               'Packs needed: 6 packs of sweets, 2 packs of balloons, 23 toys of which the first 10 cost 3.50 dollars and the next 13 cost 3 dollars')


Q.append(dict(
    n=12, orig=25, answer='B', topic='Tiered pricing',
    question=f"""<p>I need to create gift bags for the guests who are coming to my party this weekend. Each bag
will contain {hl('5 sweets, a small toy and a balloon', 'g', 1)}. The prices for the items are shown in the table
below.</p>
<p style="text-align:center;margin-bottom:0"><i>price per pack</i></p>
{table([[f'sweets<br>{hl("(20 in a pack)", "y", 2)}', '$0.45', '$0.40', '$0.35'],
        [f'balloons<br>{hl("(20 in a pack)", "y")}', '$0.90', '$0.80', '$0.70'],
        [f'toys<br>{hl("(1 in a pack)", "y")}', '$3.50', '$3.00', '$2.50']],
       head=['', hl('first 10 packs', 'p', 3), 'next 20 packs', 'any further packs'])}
<p>I need {hl('23 gift bags', 'g', 4)} for my party and {hl('do not wish to buy any more of any item than is necessary', 'y', 5)}.</p>
<p class="stem">What will be the total price I will pay for the items in my gift bags?</p>""",
    options={'A': '$73.00', 'B': '$78.50', 'C': '$85.50', 'D': '$95.10', 'E': '$103.10'},
    notes=[(1, 'g', 'Per bag: 5 sweets, 1 toy, 1 balloon.'),
           (2, 'y', 'Sweets and balloons come 20 to a pack. Toys come one at a time.'),
           (3, 'p', 'The first 10 packs are at the top price. Only packs 11 to 30 get the lower price.'),
           (4, 'g', '23 bags: 23 × 5 = 115 sweets, 23 toys, 23 balloons.'),
           (5, 'y', 'Buy the fewest packs that cover what you need.')],
    steps=[
        f"""<p>How many packs?</p>
{calc(f'sweets: 23 × 5 = 115 {ar()} 115 ÷ 20 = 5.75 {ar()} <b>6 packs</b>', f'balloons: 23 {ar()} <b>2 packs</b> (40 balloons)', 'toys: <b>23 packs</b>')}""",
        f"""<p>Price them using the bands. Only the toys go past 10 packs:</p>
{_gift()}
{calc('sweets 6 × $0.45 = $2.70', 'balloons 2 × $0.90 = $1.80', 'toys 10 × $3.50 + 13 × $3.00 = $35 + $39 = $74',
      f'total = 2.70 + 1.80 + 74 = {boxed("$78.50")}')}""",
    ],
    answer_text='$78.50: sweets $2.70 + balloons $1.80 + toys $74.',
    why={'A': '$73.00 charges every pack at the “next 20 packs” price (23 × $3 + 6 × $0.40 + 2 × $0.80). The first 10 packs are always full price.',
         'C': '$85.50 buys a whole pack of sweets for every bag (23 packs, $9.70) instead of 6 packs.',
         'D': '$95.10 buys far too many balloons: a pack for every bag (23 packs at $0.80) instead of 2 packs.',
         'E': '$103.10 buys a whole pack of sweets <b>and</b> a whole pack of balloons for every bag.'},
    fast='6 packs sweets ($2.70) + 2 packs balloons ($1.80) + 23 toys (10 at $3.50 + 13 at $3 = $74) = $78.50.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _roof():
    c, x0, y0 = 30, 50, 24
    parts, lab = [], []
    for col in range(10):
        for row in range(6):
            parts.append(rect(x0 + col * c, y0 + row * c, c, c, k='muted', sw=1.1))
    for col in range(1, 11):
        lab.append(text(x0 + (col - 0.5) * c, y0 + 6 * c + 20, col, k='pen', size=15))
    for row in range(1, 7):
        lab.append(text(x0 - 10, y0 + (6 - row + 0.5) * c + 5, row, k='orange', size=15, anchor='end'))
    lab += [text(x0 + 5 * c, y0 + 6 * c + 42, 'col: count from the LEFT', k='pen', size=15),
            text(16, y0 - 8, 'row', k='orange', size=15, anchor='start')]
    for col, row in ((2, 2), (3, 2), (5, 3), (8, 2), (9, 5)):
        x, y = x0 + (col - 1) * c, y0 + (6 - row) * c
        parts += [line(x + 4, y + 4, x + c - 4, y + c - 4, k='red', w=2.4), line(x + c - 4, y + 4, x + 4, y + c - 4, k='red', w=2.4)]
    lab.append(text(x0 + 5 * c, 14, 'diagram E', k='ink', size=17))
    tx = x0 + 10 * c + 30
    rows = [('E uses columns', '2, 3, 5, 8, 9', 'red'), ('W:', '2, 4, 6, 8, 10', 'ink'), ('X:', '2, 5, 6, 8, 9', 'ink'),
            ('Y:', '2, 3, 4, 7, 10', 'ink'), ('Z:', '1, 3, 4, 6, 8', 'ink')]
    for i, (a, b, k) in enumerate(rows):
        y = 50 + 34 * i + (10 if i else 0)
        lab.append(text(tx, y, a, k=k, size=17, anchor='start'))
        lab.append(text(tx + (126 if i == 0 else 30), y, b, k=k, size=17, anchor='start'))
    lab.append(text(tx, 50 + 34 * 5 + 18, 'no house matches!', k='red', size=21, anchor='start', font='scrawl'))
    return svg(640, 300, rough(*parts) + ''.join(lab),
               'Diagram E on a 10 by 6 grid with columns numbered from the left and rows from the bottom; its X columns 2, 3, 5, 8, 9 match no house')


Q.append(dict(
    n=13, orig=26, answer='E', topic='Coordinates & grids',
    question=f"""<p>A roofer is looking at the front-facing roofs of four houses. The survey finds five broken tiles on
the roof of each house. The positions of the broken tiles are shown in the table below, with the
{hl('column (col) and row numbers starting from the bottom left-hand tile', 'y', 1)} on each roof.</p>
{table([['house W', '2, 2', '4, 5', '6, 2', '8, 5', '10, 2'], ['house X', '2, 3', '5, 4', '6, 3', '8, 5', '9, 2'],
        ['house Y', '2, 5', '3, 1', '4, 3', '7, 5', '10, 1'], ['house Z', '1, 2', '3, 5', '4, 2', '6, 4', '8, 5']],
       head=['', 'broken tile 1<br><i>col, row</i>', 'broken tile 2<br><i>col, row</i>', 'broken tile 3<br><i>col, row</i>',
             'broken tile 4<br><i>col, row</i>', 'broken tile 5<br><i>col, row</i>'])}
<p>The roofer also draws a diagram for each of the roofs, showing the position of each of the
broken tiles marked with an X, {hl('with the bottom left-hand tile of the roof in the bottom left-hand corner of the diagram', 'y', 2)}.</p>
<p class="stem">Which one of the diagrams shown below does {hl('<b>not</b>', 'b', 3)} correspond to one of the four houses?</p>
{fig(Y, 'ps_q13_grids', 'Five grids A to E, each 10 tiles wide and 6 tall, with five tiles marked X', 560)}""",
    options={'A': 'diagram A', 'B': 'diagram B', 'C': 'diagram C', 'D': 'diagram D', 'E': 'diagram E'},
    notes=[(1, 'y', 'Like coordinates: col = across from the <b>left</b>, row = up from the <b>bottom</b>. (2, 5) = 2 across, 5 up.'),
           (2, 'y', 'The diagrams are not flipped or turned: read them straight.'),
           (3, 'b', 'Four diagrams match a house. Find the odd one out.')],
    steps=[
        f"""<p>Shortcut: give each house a “fingerprint” using just its column numbers:</p>
{calc('W: 2, 4, 6, 8, 10', 'X: 2, 5, 6, 8, 9', 'Y: 2, 3, 4, 7, 10', 'Z: 1, 3, 4, 6, 8')}""",
        f"""<p>Now read the columns of the X’s in each diagram (count from the left):</p>
{calc(f'A: 2, 3, 4, 7, 10 {ar()} house Y', f'B: 2, 4, 6, 8, 10 {ar()} house W', f'C: 1, 3, 4, 6, 8 {ar()} house Z',
      f'D: 2, 5, 6, 8, 9 {ar()} house X', f'E: 2, 3, 5, 8, 9 {ar()} no match {cross()}')}
{_roof()}""",
        f"""<p>Check the rows for one match to be safe, e.g. A against house Y: (2, 5), (3, 1), (4, 3), (7, 5), (10, 1) {tick()}</p>
{calc(f'odd one out = {boxed("E")}')}""",
    ],
    answer_text='Diagram E: its X’s are at (2, 2), (3, 2), (5, 3), (8, 2), (9, 5), which is no house.',
    why={'A': 'A is house Y: (2, 5), (3, 1), (4, 3), (7, 5), (10, 1).',
         'B': 'B is house W: (2, 2), (4, 5), (6, 2), (8, 5), (10, 2).',
         'C': 'C is house Z: (1, 2), (3, 5), (4, 2), (6, 4), (8, 5).',
         'D': 'D is house X: (2, 3), (5, 4), (6, 3), (8, 5), (9, 2).'},
    fast='Compare only the column numbers of the X’s. E uses columns 2, 3, 5, 8, 9: no house has that set.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _cheese():
    u = 22
    fx, fy = 50, 130                      # front face top-left
    W, H = 12 * u, 5 * u
    dx, dy = 10 * 7.8, -10 * 7.8          # depth offset
    parts, lab = [], []
    F = [(fx, fy), (fx + W, fy), (fx + W, fy + H), (fx, fy + H)]
    B = [(x + dx, y + dy) for x, y in F]
    parts.append(poly(F, k='ink', fill='y', sw=1.6))
    parts.append(poly([F[0], F[1], B[1], B[0]], k='ink', fill='o', sw=1.6))
    parts.append(poly([F[1], F[2], B[2], B[1]], k='ink', fill='y', sw=1.6))
    for a, b in ((B[3], B[0]), (B[3], B[2]), (B[3], F[3])):
        parts.append(line(*a, *b, k='muted', w=1.4, dash=True))
    for a, b in ((F[0], F[1]), (F[1], F[2]), (F[2], F[3]), (F[3], F[0]), (F[0], B[0]), (F[1], B[1]), (F[2], B[2]), (B[0], B[1]), (B[1], B[2])):
        parts.append(line(*a, *b, k='red', w=4))
    for x, y in F + B[:3]:
        parts.append(circle(x, y, 6, k='green', fill='g', sw=2))
    # cube ticks on three edges
    for i in range(1, 12):
        parts.append(line(fx + i * u, fy + H - 6, fx + i * u, fy + H + 6, k='ink', w=1.2))
    for i in range(1, 5):
        parts.append(line(fx - 6, fy + i * u, fx + 6, fy + i * u, k='ink', w=1.2))
    lab += [text(fx + W / 2, fy + H + 28, '12 cm: 2 corners + 10 middle', k='ink', size=16),
            text(fx - 10, fy + H / 2, '5', k='ink', size=18, anchor='end'),
            text(fx + W + dx / 2 + 12, fy + H + dy / 2 + 6, '10', k='ink', size=18, anchor='start'),
            text(fx + W / 2, 30, 'red edges: rind on 2 faces', k='red', size=17)]
    tx = 440
    rows = [('4 edges of 12:', '4 × 10 = 40'), ('4 edges of 10:', '4 × 8 = 32'), ('4 edges of 5:', '4 × 3 = 12'), ('8 corners:', '8')]
    for i, (a, b) in enumerate(rows):
        lab.append(text(tx, 120 + 30 * i, a, k='ink', size=16, anchor='start'))
        lab.append(text(tx + 106, 120 + 30 * i, b, k='pen', size=16, anchor='start'))
    lab += [text(tx, 250, 'total = 92', k='red', size=24, anchor='start', font='scrawl'),
            text(tx, 92, 'green dots: 3 faces', k='green', size=16, anchor='start')]
    return svg(640, 300, rough(*parts) + ''.join(lab),
               'The 12 by 10 by 5 cheese block with its 12 edges in red and 8 corners in green; edge cubes 40 + 32 + 12 plus 8 corners = 92')


Q.append(dict(
    n=14, orig=30, answer='B', topic='3D counting',
    question=f"""<p>Tabatha has a block of cheese with the dimensions {hl('12 x 10 x 5 cm', 'g', 1)}. She cuts it into 1 cm cubes
for a party. She forgets to cut the {hl('rind (tough outside layer)', 'y', 2)} off before she cuts the block into
cubes. As she doesn’t have a lot of time before her guests start to arrive she only removes the
rind from cheese cubes which have {hl('rind on two or more faces', 'p', 3)}.</p>
<p class="stem">From how many cheese cubes will she remove rind?</p>""",
    options={'A': '84', 'B': '92', 'C': '100', 'D': '108', 'E': '192'},
    notes=[(1, 'g', '12 cubes long, 10 deep, 5 high.'),
           (2, 'y', 'Rind covers all six outside faces.'),
           (3, 'p', 'Two or more = cubes on the <b>edges</b> (2 faces) and at the <b>corners</b> (3 faces). Cubes in the middle of a face only have 1.')],
    steps=[
        f"""<p>Which cubes have rind on 2 or more faces? The ones along the 12 edges of the block, including the 8 corners.</p>
{_cheese()}""",
        f"""<p>Count each edge without its two corner cubes, then add the 8 corners once:</p>
{calc('edges of 12: 12 − 2 = 10 each, × 4 = 40', 'edges of 10: 10 − 2 = 8 each, × 4 = 32', 'edges of 5: 5 − 2 = 3 each, × 4 = 12',
      '40 + 32 + 12 = 84 (2 faces)', f'84 + 8 corners = {boxed("92")}')}
{note('If you add the full edges, 4 × (12 + 10 + 5) = 108, every corner is counted 3 times (it sits on 3 edges). Take off 2 × 8 = 16 to get 92.', 'trap')}""",
    ],
    answer_text='92: 84 edge cubes (2 faces of rind) + 8 corner cubes (3 faces).',
    why={'A': '84 forgets the 8 corner cubes, which have rind on 3 faces.',
         'C': '100 is 108 − 8: it notices the corners were over-counted but only takes them off once. Each corner was counted 3 times, so take off 16.',
         'D': '108 is 4 × (12 + 10 + 5): every corner cube is counted three times.',
         'E': '192 adds up the outside ring of every face (40 + 40 + 30 + 30 + 26 + 26), so each edge cube is counted twice.'},
    fast='4 × (10 + 8 + 3) + 8 = 84 + 8 = 92.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _hotel():
    days = [('Mon', 15, 30), ('Tue', 16, 40), ('Wed', 17, 60), ('Thu', 18, 40), ('Fri', 19, 30), ('Sat', 20, 40),
            ('Sun', 21, 40), ('Mon', 22, 30), ('Tue', 23, 20), ('Wed', 24, 50)]
    cw, x0, y0 = 60, 20, 40
    parts, lab = [], []
    for i, (d, dt, p) in enumerate(days):
        x = x0 + cw * i
        f = 'g' if d == 'Sun' else 'paper'
        parts.append(rect(x, y0, cw - 4, 56, k='ink', fill=f, sw=1.5, rx=4))
        lab += [text(x + (cw - 4) / 2, y0 - 10, d, k='muted', size=15),
                text(x + (cw - 4) / 2, y0 + 22, dt, k='ink', size=15, font='print'),
                text(x + (cw - 4) / 2, y0 + 46, f'£{p}', k='ink', size=17)]
    # stay 1: Fri 19 - Mon 22, Fri free
    xa, xb = x0 + cw * 4, x0 + cw * 8 - 4
    parts.append(brace(xa, xb, y0 + 64, '', k='pen'))
    lab.append(text((xa + xb) / 2, y0 + 106, 'Fri–Mon: Fri free, pay 40 + 40 + 30 = £110', k='pen', size=17))
    xa2, xb2 = x0 + cw * 5, x0 + cw * 9 - 4
    parts.append(brace(xa2, xb2, y0 + 120, '', k='orange'))
    lab.append(text((xa2 + xb2) / 2 - 10, y0 + 162, 'Sat–Tue: Tue free, pay 40 + 40 + 30 = £110', k='orange', size=17))
    parts.append(line(x0 + cw * 4 + 6, y0 + 6, x0 + cw * 5 - 10, y0 + 50, k='pen', w=2))
    parts.append(line(x0 + cw * 8 + 6, y0 + 6, x0 + cw * 9 - 10, y0 + 50, k='orange', w=2))
    lab += [text(x0 + cw * 4 + 28, y0 - 26, 'free', k='pen', size=15, font='scrawl'),
            text(x0 + cw * 8 + 28, y0 - 26, 'free', k='orange', size=15, font='scrawl')]
    return svg(640, 222, rough(*parts) + ''.join(lab),
               'Nights from Monday 15 to Wednesday 24 May with prices; the cheapest stays are Friday 19 to Monday 22 with Friday free, or Saturday 20 to Tuesday 23 with Tuesday free, both 110 pounds')


Q.append(dict(
    n=15, orig=31, answer='B', topic='Calendars & offers',
    question=f"""<p>Imani is looking to book a {hl('four-night stay in May', 'g', 1)} at the Highgate Hotel, to {hl('include a Sunday night', 'y', 2)} so that she can attend an evening orchestral concert.</p>
<p>The table below shows the daily rates for the Highgate Hotel.</p>
<p style="text-align:center"><b>Highgate Hotel</b><br>Daily rates for a single room with breakfast<br><b>May</b></p>
{table([['1st<br><b>£30</b>', '2nd<br><b>£40</b>', '3rd<br><b>£50</b>', '4th<br><b>£50</b>', '5th<br><b>£20</b>', '6th<br><b>£50</b>', '7th<br><b>£40</b>'],
        ['8th<br><b>£30</b>', '9th<br><b>£40</b>', '10th<br><b>£50</b>', '11th<br><b>£50</b>', '12th<br><b>£20</b>', '13th<br><b>£50</b>', '14th<br><b>£40</b>'],
        ['15th<br><b>£30</b>', '16th<br><b>£40</b>', '17th<br><b>£60</b>', '18th<br><b>£40</b>', '19th<br><b>£30</b>', '20th<br><b>£40</b>', '21st<br><b>£40</b>'],
        ['22nd<br><b>£30</b>', '23rd<br><b>£20</b>', '24th<br><b>£50</b>', '25th<br><b>£40</b>', '26th<br><b>£30</b>', '27th<br><b>£60</b>', '28th<br><b>£30</b>'],
        ['29th<br><b>£40</b>', '30th<br><b>£50</b>', '31st<br><b>£50</b>', '', '', '', '']],
       head=['<i>Monday</i>', '<i>Tuesday</i>', '<i>Wednesday</i>', '<i>Thursday</i>', '<i>Friday</i>', '<i>Saturday</i>', '<i>Sunday</i>'])}
<p style="text-align:center"><b>May Special Offers</b><br>{hl('Book Saturday and Sunday and stay Friday for free.', 'y', 3)}<br>
{hl('Book Sunday and Monday and stay Tuesday for free.', 'y')}<br>{hl('<b>Only one special offer can be used per booking.</b>', 'p', 4)}</p>
<p class="stem">What is the {hl('<b>least</b>', 'b', 5)} amount Imani needs to pay for her four-night stay?</p>""",
    options={'A': '£100', 'B': '£110', 'C': '£120', 'D': '£130', 'E': '£140'},
    notes=[(1, 'g', 'Four nights in a row, all in May.'),
           (2, 'y', 'One of the four nights must be a Sunday.'),
           (3, 'y', 'Friday is free only if she also books that Saturday and Sunday. Tuesday is free only if she books the Sunday and Monday before it.'),
           (4, 'p', 'Never two free nights in one booking.'),
           (5, 'b', 'Cheapest possible.')],
    steps=[
        f"""<p>Four nights with a Sunday in them can only be one of four shapes. Each shape gets exactly one free night:</p>
{calc(f'Thu–Fri–Sat–Sun {ar()} Fri free, pay Thu + Sat + Sun',
      f'Fri–Sat–Sun–Mon {ar()} Fri free, pay Sat + Sun + Mon',
      f'Sat–Sun–Mon–Tue {ar()} Tue free, pay Sat + Sun + Mon',
      f'Sun–Mon–Tue–Wed {ar()} Tue free, pay Sun + Mon + Wed')}""",
        f"""<p>Price the paid nights for each of the four weekends:</p>
{table([['Sun 7th', '50 + 50 + 40 = 140', '50 + 40 + 30 = 120', '40 + 30 + 50 = 120'],
        ['Sun 14th', '50 + 50 + 40 = 140', '50 + 40 + 30 = 120', '40 + 30 + 60 = 130'],
        [hl('Sun 21st', 'g'), '40 + 40 + 40 = 120', hl('40 + 40 + 30 = <b>110</b>', 'g'), '40 + 30 + 50 = 120'],
        ['Sun 28th', '40 + 60 + 30 = 130', '60 + 30 + 40 = 130', '30 + 40 + 50 = 120']],
       head=['weekend', 'Thu + Sat + Sun', 'Sat + Sun + Mon', 'Sun + Mon + Wed'])}""",
        f"""<p>The cheapest is the weekend of the 21st:</p>
{_hotel()}
{calc(f'least = {boxed("£110")}')}""",
    ],
    answer_text='£110: for example Friday 19th to Monday 22nd with the Friday free (£40 + £40 + £30).',
    why={'A': '£100 would need the three paid nights to cost £100, but the cheapest Saturday + Sunday + Monday is £40 + £40 + £30 = £110.',
         'C': '£120 is the best deal on the other weekends (e.g. Fri 5th to Mon 8th). It misses the cheaper weekend of the 21st.',
         'D': '£130 is the best you can do on the last weekend (Sun 28th) when you try Thu–Sun, Fri–Mon or Sat–Tue there.',
         'E': '£140 is Friday 19th to Monday 22nd at full price (30 + 40 + 40 + 30): it forgets the free Friday.'},
    fast='Every Sunday-stay gets one free night, so compare 3-night sums. Sat 20 + Sun 21 + Mon 22 = 40 + 40 + 30 = £110 is the lowest.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _code():
    cols = {'A': 'y', 'N': 'b', 'D': 'g', 'M': 'v', 'E': 'o', 'R': 'p', 'U': 'paper', 'Y': 'paper'}
    rows = [('AND', [('A', 'o+'), ('N', '–++'), ('D', '–o')]),
            ('MAN', [('M', '–+–'), ('A', 'o+'), ('N', '–++')]),
            ('MEND', [('M', '–+–'), ('E', '++'), ('N', '–++'), ('D', '–o')]),
            ('RUNNY', [('R', 'oo'), ('U', '+o'), ('N', '–++'), ('N', '–++'), ('Y', 'ooo')]),
            ('EAR', [('E', '++'), ('A', 'o+'), ('R', 'oo')])]
    parts, lab = [], []
    sw = 20
    for i, (word, chunks) in enumerate(rows):
        y = 40 + 62 * i
        lab.append(text(100, y + 30, word, k='red' if word == 'EAR' else 'ink', size=19, anchor='end', font='print'))
        x = 118
        for letter, code in chunks:
            w = sw * len(code) + 12
            parts.append(rect(x, y + 8, w, 32, k='ink', fill=cols[letter], sw=1.5, rx=5))
            lab.append(text(x + w / 2, y + 2, letter, k='pen', size=16))
            lab.append(text(x + w / 2, y + 31, ' '.join(code), k='ink', size=19, font='print'))
            x += w + 8
    lab += [text(500, 74, 'A = o+ (given)', k='ink', size=16, anchor='start'),
            text(500, 136, 'so M = –+–, N = –++', k='ink', size=16, anchor='start'),
            text(500, 198, 'so E = ++', k='ink', size=16, anchor='start'),
            text(500, 260, 'R, U: 2 each', k='ink', size=16, anchor='start'),
            text(500, 322, '= ++ o+ oo', k='red', size=20, anchor='start', font='scrawl')]
    return svg(640, 360, rough(*parts) + ''.join(lab),
               'Each code word split into coloured chunks: A = o+, N = –++, D = –o, M = –+–, E = ++, R = oo, U = +o, Y = ooo; EAR = ++ o+ oo')


def _cd(s):
    return f'<span style="font-family:var(--print);letter-spacing:.14em;white-space:nowrap">{s}</span>'


Q.append(dict(
    n=16, orig=32, answer='A', topic='Codes',
    question=f"""<p>In a particular coding system, letters of the alphabet are represented by {hl('two-character or three-character combinations', 'y', 1)} of the symbols o, + and –.</p>
<p>For example, {hl('the letter A is represented as ' + _cd('o+'), 'g', 2)}, and the letter Z is represented as {_cd('–o+')}.</p>
<p>The table shows how certain words are represented in this coding system.</p>
{table([['AND', _cd('o+–++–o')], ['MAN', _cd('–+–o+–++')], ['MEND', _cd('–+–++–++–o')], ['RUNNY', _cd('oo+o–++–++ooo')]], head=['word', 'code'])}
<p class="stem">How is the word {hl('EAR', 'b', 3)} represented by the code?</p>""",
    options={'A': _cd('++o+oo'), 'B': _cd('–++o+oo'), 'C': _cd('++o+–oo'), 'D': _cd('++o+oo+'), 'E': _cd('–++o+–oo+')},
    notes=[(1, 'y', 'Each letter is 2 or 3 symbols, with no gaps between letters. You have to work out where each letter ends.'),
           (2, 'g', 'The way in: A = o+. Find it inside the words.'),
           (3, 'b', 'A is known, so we only need E and R.')],
    steps=[
        f"""<p>MAN has A in the middle. Find {_cd('o+')} in {_cd('–+–o+–++')}:</p>
{calc(f'{_cd("–+–")} | {_cd("o+")} | {_cd("–++")} {ar()} M = {_cd("–+–")}, N = {_cd("–++")}',
      f'AND = {_cd("o+")} | {_cd("–++")} | {_cd("–o")} {ar()} D = {_cd("–o")}')}""",
        f"""<p>MEND: take off M at the front and N, D at the end. What is left is E:</p>
{calc(f'{_cd("–+–")} | {_cd("++")} | {_cd("–++")} | {_cd("–o")} {ar()} E = {_cd("++")}')}""",
        f"""<p>RUNNY ends in N, N, Y: {_cd("–++")} {_cd("–++")} {_cd("ooo")}. That leaves {_cd("oo+o")} for R and U.
Each letter needs at least 2 symbols, so it must split 2 + 2:</p>
{calc(f'R = {_cd("oo")}, U = {_cd("+o")}')}
{_code()}""",
        f"""{calc(f'E | A | R = {_cd("++")} | {_cd("o+")} | {_cd("oo")} {ar()} {boxed(_cd("++o+oo"))}')}""",
    ],
    answer_text='A: ++ o+ oo (E = ++, A = o+, R = oo).',
    why={'B': 'B starts with N ( –++ ) instead of E ( ++ ): it spells NAR.',
         'C': 'C slips a stray – in before R. R is just oo.',
         'D': 'D adds an extra + at the end. That would make R = oo+ and leave U as a single o, but every letter needs 2 or 3 symbols.',
         'E': 'E starts with N ( –++ ) and has extra symbols on R: it isn’t E, A, R at all.'},
    fast='MAN with A = o+ gives N = –++, then MEND leaves E = ++. RUNNY leaves oo+o for R and U, so R = oo. EAR = ++o+oo.',
))
