import math
from wslib import *

Y = 2014
Q = []


def _pie(cx, cy, r, shares, fills, labels, k='ink'):
    parts, lab, a0 = [], [], -90.0
    total = sum(shares)
    for s, f, l in zip(shares, fills, labels):
        a1 = a0 + 360 * s / total
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        big = 1 if a1 - a0 > 180 else 0
        parts.append(path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z', k=k, fill=f, sw=1.8))
        am = math.radians((a0 + a1) / 2)
        lr = r * 0.62 if s / total > 0.12 else r + 22
        lab.append(text(cx + lr * math.cos(am), cy + lr * math.sin(am) + 5, l, k='ink', size=15))
        a0 = a1
    return parts, lab


# ---------------------------------------------------------------- 9 (Q19)
def _leap():
    X = lambda d: 30 + d * 1.55
    parts = [line(X(0), 70, X(366), 70, k='ink', w=2)]
    lab = []
    months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    starts = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    for m, s0 in zip(months, starts):
        parts.append(line(X(s0), 64, X(s0), 76, k='muted', w=1.4))
        lab.append(text(X(s0 + 14), 92, m, k='muted', size=14))
    parts.append(line(X(59.5), 40, X(59.5), 100, k='red', w=2.6))
    lab.append(text(X(59.5), 32, '29 Feb (leap year)', k='red', size=16, font='scrawl'))
    for name, d, col in (('Ryan 50', 50, 'pen'), ('Rebecca 124', 124, 'violet'), ('Richard 151', 151, 'pen'),
                         ('Ralph 251', 251, 'pen'), ('Ruth 322', 322, 'violet'), ('Robert 351', 351, 'green')):
        parts.append(circle(X(d), 70, 5, k=col, fill='paper'))
        lab.append(text(X(d), 122 if d != 50 else 112, name, k=col, size=14, rotate=0))
    lab.append(text(X(200), 146, 'everyone after 29 Feb moves 1 day later in the year', k='red', size=16))
    return svg(620, 158, rough(*parts) + ''.join(lab), 'Year timeline: Ryan on day 50 before 29 February; all the others move one day later in a leap year')

Q.append(dict(
    n=9, orig=19, answer='D', topic='Calendars & days of the week', attempt='D',
    question=f"""<p>Elsie has six grandchildren. Their birthdays are as follows:</p>
{table([['Ryan', hl('19th February', 'p', 3)], ['Rebecca', '3rd May'], ['Richard', '30th May'], ['Ralph', '7th September'],
        ['Ruth', '17th November'], ['Robert', '16th December']])}
<p>Remarkably, {hl("in non-leap years the boys' birthdays are on the 50th, 150th, 250th and 350th days of the year, whilst the girls' birthdays are on the 123rd and 321st days", 'g', 1)}, and all six are on
different days of the week.</p>
<p class="stem">Which other grandchild's birthday is on the same day of the week as Ryan's {hl('in a leap year', 'b', 2)}?</p>""",
    options={'A': 'Ralph', 'B': 'Rebecca', 'C': 'Richard', 'D': 'Robert', 'E': 'Ruth'},
    notes=[(1, 'g', 'Day numbers are given: no need to count through the months!'),
           (2, 'b', 'A leap year adds 29 February, so every date <b>after</b> it moves one day later in the year.'),
           (3, 'p', 'Ryan is in February, <b>before</b> the 29th, so he doesn’t move.')],
    steps=[
        f"""<p>Two dates fall on the same weekday when the gap between them is a whole number of weeks (a multiple of 7).</p>""",
        f"""<p>In a leap year, Ryan stays on day 50 and everyone else moves up by 1:</p>{_leap()}""",
        f"""<p>Gaps from Ryan’s day 50, then divide by 7:</p>
{calc('Rebecca 124 − 50 = 74 = 70 + 4 ' + cross(), 'Richard 151 − 50 = 101 = 98 + 3 ' + cross(),
      'Ralph 251 − 50 = 201 = 196 + 5 ' + cross(), 'Ruth 322 − 50 = 272 = 266 + 6 ' + cross(),
      f'Robert 351 − 50 = 301 = 7 × 43 exactly {tick()} {ar()} {boxed("Robert")}')}
{note('Quick 7× facts: 7 × 40 = 280, 7 × 43 = 301. Knock off big chunks of 70 or 140 to find remainders fast.', 'tip')}""",
    ],
    answer_text='Robert: in a leap year his birthday is exactly 43 weeks after Ryan’s.',
    why={'A': 'Ralph is 201 days after Ryan: 201 ÷ 7 leaves 5.',
         'B': 'Rebecca is 74 days after: leaves 4.',
         'C': 'Richard is 101 days after: leaves 3.',
         'E': 'Ruth is 272 days after: leaves 6.'},
    fast='Leap year: everyone except Ryan gains 1. Boys’ gaps become 101, 201, 301: only 301 = 7 × 43.',
))

# ---------------------------------------------------------------- 10 (Q20)
def _pattern():
    bw, x0 = 54, 30
    parts, lab = [], []
    nums = [1, 2, 3, 4, 5, 6, 3, 4]
    for i, n in enumerate(nums):
        f = 'o' if n == 3 else 'b' if n == 4 else 'paper'
        parts.append(rect(x0 + i * bw, 64, bw - 8, 40, k='ink', fill=f, sw=1.8))
        lab.append(text(x0 + i * bw + (bw - 8) / 2, 92, n, k='ink', size=20))
    parts.append(path(f'M{x0 + 2 * bw + 23} 64 Q{x0 + 4.5 * bw} 14 {x0 + 6 * bw + 23} 64', k='orange', sw=2.4))
    parts.append(path(f'M{x0 + 3 * bw + 23} 104 Q{x0 + 5.5 * bw} 154 {x0 + 7 * bw + 23} 104', k='pen', sw=2.4))
    lab += [text(x0 + 4.5 * bw, 26, 'same symbol', k='orange', size=16),
            text(x0 + 5.5 * bw, 152, 'same symbol', k='pen', size=16)]
    word = 'SOMETIME'
    for i, ch in enumerate(word):
        f = 'o' if i in (2, 6) else 'b' if i in (3, 7) else 'paper'
        parts.append(rect(x0 + i * bw, 172, bw - 8, 40, k='green', fill=f, sw=1.8))
        lab.append(text(x0 + i * bw + (bw - 8) / 2, 200, ch, k='ink', size=22, font='print'))
    lab.append(text(x0 + 8 * bw + 10, 198, 'fits!', k='green', size=22, font='scrawl', anchor='start'))
    return svg(540, 226, rough(*parts) + ''.join(lab), 'Pattern 1 2 3 4 5 6 3 4: letters 3 and 7 match and letters 4 and 8 match, which fits SOMETIME')

Q.append(dict(
    n=10, orig=20, answer='E', topic='Codes & patterns', attempt='E',
    question=f"""<p>Whenever my friend Alistair writes to me he does so entirely in code. He always uses symbols
for letters but {hl('changes the code each time', 'p', 1)}, so any particular symbol does not necessarily stand
for the same letter of the alphabet every time.</p>
<p>I always start to crack the code by looking at how he has written his name at the end of his
letter. For instance, last time he was:</p>
{fig(Y, 'q10_name', 'Last time: eight symbols spelling ALISTAIR', 330)}
<p>In my last letter to him I asked him when he intends to visit me next. Today I have received a
reply consisting of {hl('just one word', 'y', 2)} as follows:</p>
{fig(Y, 'q10_reply', 'The reply: eight symbols; the 3rd and 7th match and the 4th and 8th match', 330)}
<p class="stem">When can I assume that he intends to appear?</p>""",
    options={'A': 'TOMORROW', 'B': 'THURSDAY', 'C': 'SATURDAY', 'D': 'NOVEMBER', 'E': 'SOMETIME'},
    notes=[(1, 'p', 'The code changes every time, so last letter’s key is <b>useless</b> now.'),
           (2, 'y', 'No name this time, so the only clue is the <b>pattern</b> of repeated symbols.')],
    steps=[
        f"""<p>Ignore the old key. Number each symbol by when it first appears:</p>
{calc('&gt; ↓ ◊ Σ ∞ ∇ ◊ Σ', f'{ar()} 1 2 3 4 5 6 <b>3 4</b>')}
<p>So: 8 letters, the 3rd = 7th, the 4th = 8th, all the rest different.</p>""",
        f"""{_pattern()}
{calc('TOMORROW: O appears 3 times ' + cross(), 'THURSDAY: no repeats ' + cross(), 'SATURDAY: A at 2nd and 7th ' + cross(),
      'NOVEMBER: E at 4th and 7th ' + cross(), f'SOMETIME: M at 3rd and 7th, E at 4th and 8th {tick()} {ar()} {boxed("E")}')}""",
        f"""{note('The trap: decoding with last time’s key gives S, A, T, ?, R, ?, T, ?, which tempts you towards SATURDAY. But the key has changed, and SATURDAY doesn’t even fit the pattern.', 'trap')}""",
    ],
    answer_text='SOMETIME: it is the only word with the same repeat pattern.',
    why={'A': 'TOMORROW has O three times (2nd, 4th, 7th) and RR together: wrong pattern.',
         'B': 'THURSDAY has no repeated letters, but the reply has two repeats.',
         'C': 'SATURDAY repeats A in the 2nd and 7th places, not 3rd/7th and 4th/8th. (It only looks right if you use last time’s key.)',
         'D': 'NOVEMBER repeats E in the 4th and 7th places: wrong pattern.'},
    fast='Code changes → use the repeat pattern: positions 3 = 7 and 4 = 8. Only SOMETIME (M…M, E…E).',
))

# ---------------------------------------------------------------- 11 (Q24)
def _receipt():
    parts = [path('M40 20 L300 20 L300 210 L287 222 L274 210 L261 222 L248 210 L235 222 L222 210 L209 222 L196 210 '
                  'L183 222 L170 210 L157 222 L144 210 L131 222 L118 210 L105 222 L92 210 L79 222 L66 210 L53 222 L40 210 Z',
                  k='ink', fill='paper', sw=1.8),
             line(60, 160, 280, 160, k='ink', w=1.4, dash=True)]
    lab = [text(170, 48, 'DINNER', k='ink', size=18, font='print'),
           text(60, 82, 'Smoked salmon', k='ink', size=17, anchor='start'), text(280, 82, '6.10', k='ink', size=17, anchor='end'),
           text(60, 110, 'Rainbow trout', k='ink', size=17, anchor='start'), text(280, 110, '16.10', k='ink', size=17, anchor='end'),
           text(60, 138, 'Profiteroles', k='ink', size=17, anchor='start'), text(280, 138, '6.20', k='ink', size=17, anchor='end'),
           text(60, 188, 'TOTAL', k='ink', size=18, anchor='start', font='print'), text(280, 188, '£28.40', k='green', size=22, anchor='end', font='scrawl'),
           text(320, 100, '10p under', k='green', size=20, font='scrawl', anchor='start'),
           text(320, 124, 'the £28.50 limit', k='green', size=20, font='scrawl', anchor='start')]
    return svg(480, 236, rough(*parts) + ''.join(lab), 'Receipt: smoked salmon 6.10, rainbow trout 16.10, profiteroles 6.20, total 28.40')

Q.append(dict(
    n=11, orig=24, answer='D', topic='Best combination', attempt='C',
    question=f"""<p>A hotel offers its guests a dinner allowance of {hl('£28.50', 'g', 1)} per night. A guest wishes to spend up to
her allowance on a {hl('three course meal', 'y', 2)} {hl('without overspending', 'p', 3)}.</p>
<p>Here is the menu:</p>
{table([['<b>STARTER</b>', ''], ['Soup of the day', '5.00'], ['Prawn cocktail', '6.50'], ['Smoked salmon', '6.10'], ['Duck confit salad', '6.95'],
        ['<b>MAIN COURSE</b>', ''], ['Sirloin steak 8 ozs.', '14.90'], ['Gammon steak', '12.50'], ['Rainbow trout', '16.10'],
        ["Duck a l'orange", '15.15'], ['Vegetarian risotto', '12.75'],
        ['<b>DESSERT</b>', ''], ['Cheese and biscuits', '6.10'], ['Cheesecake', '5.60'], ['Apple pie and cream', '5.30'],
        ['Lemon sorbet', '5.20'], ['Profiteroles', '6.20']], head=['', 'PRICE (£)'])}
<p class="stem">What is the {hl('largest', 'b', 4)} sum she can spend without exceeding the limit?</p>""",
    options={'A': '£28.05', 'B': '£28.30', 'C': '£28.35', 'D': '£28.40', 'E': '£28.45'},
    notes=[(1, 'g', 'The ceiling: £28.50.'),
           (2, 'y', 'Exactly one starter, one main and one dessert.'),
           (3, 'p', 'Total must be £28.50 <b>or less</b>.'),
           (4, 'b', 'Test the options from the biggest down: the first one you can make is the answer.')],
    steps=[
        f"""<p>Start with the biggest option, <b>£28.45</b>. Look at the pence: only two dishes end in 5p,
Duck confit salad (6.95) and Duck à l'orange (15.15). A total ending in 5p needs exactly one of them.</p>
<ul><li>Duck salad 6.95: main + dessert must be 21.50. Try each main: 14.90 → 6.60, 12.50 → 9.00, 16.10 → 5.40, 12.75 → 8.75. No dessert costs those. {cross()}</li>
<li>Duck à l'orange 15.15: starter + dessert must be 13.30, but the biggest possible is 6.50 + 6.20 = 12.70. {cross()}</li></ul>
<p>So £28.45 is impossible.</p>""",
        f"""<p>Next, <b>£28.40</b>: 6.10 + 16.10 = 22.20, and 28.40 − 22.20 = 6.20 = profiteroles {tick()}</p>{_receipt()}
{calc(f'largest possible = {boxed("£28.40")}')}""",
    ],
    answer_text='£28.40 (smoked salmon, rainbow trout, profiteroles).',
    why={'A': '£28.05 can be made, but bigger totals are possible.',
         'B': '£28.30 can be made, but £28.40 is bigger.',
         'C': '£28.35 is what you get by grabbing the priciest starter and main first (duck salad + trout + apple pie). Greedy picking misses £28.40.',
         'E': '£28.45 is impossible: the pence can’t be made to work (see step 1).'},
    fast='Work down from the biggest option. 28.45 fails the pence check; 28.40 = 6.10 + 16.10 + 6.20 works.',
))

# ---------------------------------------------------------------- 12 (Q25)
def _threshold():
    rows = [('2.5 mph', 98), ('3.0 mph', 95), ('3.5 mph', 94), ('4.0 mph', 102), ('4.5 mph', 115), ('5.0 mph', 131)]
    X = lambda v: 110 + (v - 80) * 7.5
    parts, lab = [], []
    for i, (name, v) in enumerate(rows):
        y = 30 + i * 34
        ok = v >= 101
        parts.append(rect(X(80), y, X(v) - X(80), 22, k='ink', fill='g' if ok else 'p', sw=1.6))
        lab.append(text(100, y + 17, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) - 8, y + 17, f'{v}' + (' ✓' if ok else ' ✗'), k='ink', size=16, anchor='end'))
    parts.append(line(X(101), 18, X(101), 240, k='red', w=2.4, dash=True))
    lab.append(text(X(101), 256, 'need about 101 per mile', k='red', size=17, font='scrawl'))
    lab.append(text(X(131) + 12, 30 + 3 * 34 + 17, '← slowest that works', k='green', size=17, anchor='start'))
    return svg(640, 268, rough(*parts) + ''.join(lab), 'Calories per mile at 180 lb for each speed, with the 101 line; 4.0 mph is the slowest above it')

Q.append(dict(
    n=12, orig=25, answer='C', topic='Tables & rates', attempt='C',
    question=f"""<p>Chris is an actor and recently feels he has become overweight. He aims to lose {hl('at least 7.5 lbs', 'g', 1)}
over the next 10 weeks. He decides he is able to walk the following number of miles over {hl('each of the next ten weeks', 'y', 2)}:</p>
<p>Mondays – 5 miles<br>Wednesdays – 5 miles<br>Saturdays – 8 miles<br>Sundays – 8 miles</p>
<p>The table below shows calories burned per mile by walking at various speeds.</p>
{table([['2.5mph', '55', '65', '76', '87', hl('98', 'p'), '109', '120', '136', '150'],
        ['3.0mph', '53', '64', '74', '85', hl('95', 'p'), '106', '117', '133', '146'],
        ['3.5mph', '52', '62', '73', '83', hl('94', 'p'), '104', '114', '130', '143'],
        ['4.0mph', '57', '68', '80', '91', hl('102', 'g'), '114', '125', '142', '156'],
        ['4.5mph', '64', '76', '89', '102', hl('115', 'g'), '127', '140', '159', '175'],
        ['5.0mph', '73', '87', '102', '116', hl('131', 'g'), '145', '160', '182', '200']],
       head=['Walking speed ↓<br>Starting weight →', '100lb', '120lb', '140lb', '160lb', hl('180lb', 'b', 4), '200lb', '220lb', '250lb', '275lb'])}
<p>{hl('NB: A lb in fat equals 3500 calories', 'y', 3)}</p>
<p class="stem">What is the {hl('slowest speed', 'b', 5)} he needs to walk at to lose at least 7.5 lbs if he starts at 180 lbs?</p>""",
    options={'A': '2.5 mph', 'B': '3.0 mph', 'C': '4.0 mph', 'D': '4.5 mph', 'E': '5.0 mph'},
    notes=[(1, 'g', '7.5 lb of fat to burn.'),
           (2, 'y', 'The same walking every week, for 10 weeks.'),
           (3, 'y', 'Turns pounds into calories: × 3500.'),
           (4, 'b', 'Only the 180 lb column matters.'),
           (5, 'b', 'The slowest speed that still burns enough. Careful: the table isn’t in order!')],
    steps=[
        f"""<p>Total calories to burn and total miles walked:</p>
{calc('7.5 × 3500 = 24 500 + 1750 = <b>26 250 calories</b>', '5 + 5 + 8 + 8 = 26 miles a week', '26 × 10 = <b>260 miles</b>')}""",
        f"""<p>Calories needed per mile:</p>
{calc(f'26 250 ÷ 260 {ar()} 260 × 100 = 26 000, with 250 left over', f'so just over 100 {ar()} need <b>about 101 per mile</b>')}""",
        f"""<p>Now read down the 180 lb column:</p>{_threshold()}
{calc(f'slowest speed with 101 or more = {boxed("4.0 mph")} (102 per mile)')}
{note('Check: 102 × 260 = 26 520, which is at least 26 250. At 2.5 mph: 98 × 260 = 25 480, which is too few.', 'check')}""",
    ],
    answer_text='4.0 mph (102 calories per mile at 180 lb).',
    why={'A': '2.5 mph burns 98 per mile: 98 × 260 = 25 480, not enough.',
         'B': '3.0 mph burns only 95 per mile: not enough.',
         'D': '4.5 mph works, but it isn’t the slowest that works.',
         'E': '5.0 mph works too, but it’s even faster than needed.'},
    fast='26 250 calories ÷ 260 miles ≈ 101 per mile. In the 180 lb column, the first value of 101 or more is 102 at 4.0 mph.',
))

# ---------------------------------------------------------------- 13 (Q26)
def _bars():
    parts, lab = [], []
    data = [('Arthur', 10, 7), ('Belinda', 6, 3), ('Carol', 4, 1)]
    u = 14
    for i, (name, a, b) in enumerate(data):
        x = 40 + i * 92
        parts.append(rect(x, 180 - a * u, 40, a * u, k='ink', fill='paper', sw=1.8))
        parts.append(rect(x, 180 - b * u, 40, b * u, k='ink', fill='b', sw=1.8))
        parts.append(line(x + 52, 180 - a * u, x + 52, 180 - b * u, k='red', head=True, w=2))
        lab.append(text(x + 20, 200, name, k='ink', size=15))
        lab.append(text(x + 20, 172 - a * u, a, k='muted', size=15))
        lab.append(text(x + 20, 180 - b * u + 18 if b > 1 else 180 - b * u - 4, b, k='pen', size=17))
        lab.append(text(x + 63, 180 - (a + b) * u / 2, '−3', k='red', size=15, anchor='start'))
    parts.append(line(30, 180, 300, 180, k='ink', w=2))
    p2, l2 = _pie(450, 105, 80, [7, 3, 1], ['b', 'g', 'o'], ['Arthur 7', 'Belinda 3', 'Carol 1'])
    lab += [text(160, 232, 'before (white) and after (blue)', k='ink', size=15),
            text(450, 222, 'now 7 : 3 : 1', k='pen', size=20, font='scrawl')]
    return svg(580, 245, rough(*parts, *p2) + ''.join(lab + l2), 'Bars 10, 6 and 4 each drop by 3 to 7, 3 and 1; a pie chart in the ratio 7 to 3 to 1')

Q.append(dict(
    n=13, orig=26, answer='D', topic='Charts & ratio', attempt='B',
    question=f"""<p>The bar chart shows the amount of money in the savings accounts of three friends at the start
of the year.</p>
{fig(Y, 'q13_bars', 'Bar chart of account balances: Arthur tallest, Belinda middle, Carol smallest', 220)}
<p>Since then, they have {hl('all spent the same amount', 'p', 1)} of money from their accounts and {hl("the amount in Belinda's account has halved", 'y', 2)}.</p>
<p class="stem">Which one of the following pie charts {hl('could represent', 'b', 3)} the amounts of money in the accounts now?</p>
{fig(Y, 'q13_pies', 'Five pie charts A to E split between Arthur, Belinda and Carol', 430)}""",
    options={'A': 'pie A', 'B': 'pie B', 'C': 'pie C', 'D': 'pie D', 'E': 'pie E'},
    notes=[(1, 'p', 'Take the <b>same number</b> off every bar, not the same fraction.'),
           (2, 'y', 'That amount = half of Belinda’s starting balance.'),
           (3, 'b', 'No scale, so work with the bar heights in ratio.')],
    steps=[
        f"""<p>Measure the bars against each other: they are in the ratio about <b>5 : 3 : 2</b>.
Call them 10, 6 and 4 units so halving is easy.</p>""",
        f"""<p>Belinda halves: 6 → 3, so everyone spent 3 units.</p>{_bars()}
{calc('Arthur 10 − 3 = 7', 'Belinda 6 − 3 = 3', 'Carol 4 − 3 = 1', f'total 11 {ar()} Arthur ≈ 64%, Belinda ≈ 27%, Carol ≈ 9%')}""",
        f"""<p>So the pie needs a big Arthur (about two-thirds), Belinda about a quarter, and Carol only a <b>tiny sliver</b>,
a third the size of Belinda’s slice. Only pie {boxed('D')} has that.</p>""",
    ],
    answer_text='Pie D: Arthur about 64%, Belinda about 27%, Carol a thin 9%.',
    why={'A': 'Arthur is exactly half and Carol is bigger than she should be (about 19%).',
         'B': 'Carol’s slice (about 19%) is nearly as big as Belinda’s, but it should be a third of Belinda’s.',
         'C': 'Carol’s slice is <b>bigger</b> than Belinda’s.',
         'E': 'Arthur is under half and Carol has a whole quarter.'},
    fast='Same amount off each: 10, 6, 4 → 7, 3, 1. Carol must be a tiny slice, a third of Belinda’s: only D.',
))

# ---------------------------------------------------------------- 14 (Q30)
def _journeys():
    s = 13
    parts = [rect(40, 50, 15 * s, 40, k='ink', fill='b', sw=1.8), rect(40 + 15 * s, 50, 9 * s, 40, k='ink', fill='o', sw=1.8),
             rect(40, 130, 30 * 6.5, 40, k='ink', fill='b', sw=1.8), rect(40 + 30 * 6.5, 130, 15 * 6.5, 40, k='ink', fill='o', sw=1.8)]
    lab = [text(20, 76, 'km', k='muted', size=15, anchor='end'), text(20, 156, 'min', k='muted', size=15, anchor='end'),
           text(40 + 7.5 * s, 76, 'trip 1: 15 km', k='ink', size=16), text(40 + 15 * s + 4.5 * s, 76, '9 km', k='ink', size=16),
           text(40 + 15 * 6.5, 156, 'trip 1: 30 min', k='ink', size=16), text(40 + 30 * 6.5 + 7.5 * 6.5, 156, '15 min', k='ink', size=16),
           text(40 + 12 * s, 38, 'total 24 km', k='pen', size=17), text(40 + 22.5 * 6.5, 196, 'total 45 min (24 ÷ 32 = ¾ h)', k='pen', size=17),
           text(420, 112, 'trip 2: 9 km in 15 min', k='orange', size=20, font='scrawl'),
           text(420, 140, '= 36 km/h', k='orange', size=24, font='scrawl')]
    return svg(560, 212, rough(*parts) + ''.join(lab), 'Bars: trip 1 is 15 km and 30 minutes; trip 2 is 9 km and 15 minutes; together 24 km in 45 minutes')

Q.append(dict(
    n=14, orig=30, answer='D', topic='Average speed', attempt='C',
    question=f"""<p>David has a new cycle computer but has not learned all the functions yet, so can only read the
{hl('cumulative mileage and average speed of all of the journeys', 'y', 1)} since he fitted it. On his first
journey using it he covered {hl('15 km at an average speed of 30 km/h', 'g', 2)}. He can work out from this
that the journey took him 15/30 hours or exactly 30 minutes. After the second journey, his
{hl('cumulative mileage was 24 km and overall average speed 32 km/h', 'g', 3)}.</p>
<p class="stem">What was his average speed on the {hl('second journey', 'b', 4)}?</p>""",
    options={'A': '18 km/h', 'B': '31 km/h', 'C': '34 km/h', 'D': '36 km/h', 'E': '45 km/h'},
    notes=[(1, 'y', 'The display shows totals for <b>both</b> trips together.'),
           (2, 'g', 'Trip 1: 15 km in 30 minutes.'),
           (3, 'g', 'Both trips together: 24 km at 32 km/h.'),
           (4, 'b', 'Find trip 2’s distance and time separately.')],
    steps=[
        f"""<p>Average speed always means total distance ÷ total time, so work with totals:</p>
{calc(f'total time = 24 ÷ 32 = {frac(3, 4)} hour = <b>45 minutes</b>', 'trip 2 time = 45 − 30 = <b>15 minutes</b>', 'trip 2 distance = 24 − 15 = <b>9 km</b>')}""",
        f"""{_journeys()}{calc(f'9 km in 15 min {ar()} × 4 {ar()} 36 km in 60 min = {boxed("36 km/h")}')}""",
        f"""{note('Never average two speeds: (30 + 34) ÷ 2 = 32 looks neat, but the trips take different times, so it is wrong.', 'trap')}""",
    ],
    answer_text='36 km/h: 9 km in 15 minutes.',
    why={'A': '18 km/h would be 9 km taking 30 minutes, but trip 2 only took 15.',
         'B': '31 km/h doesn’t come from any correct working.',
         'C': '34 km/h is the trap: averaging the speeds, (30 + 34) ÷ 2 = 32. You can only do that if both trips take the same time.',
         'E': '45 is the total time in <b>minutes</b>, not a speed.'},
    fast='24 ÷ 32 = ¾ h = 45 min, so trip 2 is 15 min for 9 km = 36 km/h.',
))

# ---------------------------------------------------------------- 15 (Q31)
def _dials():
    parts, lab = [], []
    for i, (n, sub) in enumerate(((10, 'any digit'), (9, 'not the 1st'), (8, 'not the 1st or 2nd'))):
        x = 70 + i * 150
        parts.append(rect(x - 45, 30, 90, 90, k='ink', fill='paper', sw=2, rx=14))
        lab.append(text(x, 92, n, k='pen', size=44, font='scrawl'))
        lab.append(text(x, 146, sub, k='muted', size=15))
        if i < 2:
            lab.append(text(x + 75, 85, '×', k='red', size=30))
    lab.append(text(510, 92, '= 720', k='green', size=36, font='scrawl', anchor='start'))
    return svg(640, 160, rough(*parts) + ''.join(lab), 'Three dials: 10 choices, then 9, then 8, multiplying to 720')

Q.append(dict(
    n=15, orig=31, answer='B', topic='Counting', attempt='B',
    question=f"""<p>I have bought a combination lock for my bicycle. The combination is a three-digit number in the
{hl('range 000-999', 'y', 1)} and it is currently set to the manufacturer's default combination of 999. Before I
use the lock I need to set the combination. I want to use a combination where {hl('all three digits are different', 'p', 2)}.</p>
<p class="stem">How many combinations are there in the range 000-999 where all three digits are different?</p>""",
    options={'A': '504', 'B': '720', 'C': '810', 'D': '900', 'E': '990'},
    notes=[(1, 'y', 'Starting with 0 is allowed (012 is a combination), so every dial has 10 digits.'),
           (2, 'p', 'No digit may be used twice.')],
    steps=[
        f"""<p>Fill the three dials one at a time:</p>{_dials()}
{calc(f'10 × 9 × 8 = 90 × 8 = {boxed("720")}')}""",
    ],
    answer_text='720 = 10 × 9 × 8.',
    why={'A': '504 = 9 × 8 × 7: one choice too few on every dial.',
         'C': '810 = 9 × 9 × 10: doesn’t apply the “all different” rule properly.',
         'D': '900 counts 100–999, the ordinary three-digit numbers, with repeats allowed.',
         'E': '990 = 1000 − 10 only removes 000, 111, …, 999. Things like 112 repeat a digit too.'},
    fast='10 choices, then 9, then 8: 720.',
))

# ---------------------------------------------------------------- 16 (Q32)
L16 = 30
def _P(a, b, ox, oy, L=L16):
    return (ox + a * L * 0.866, oy + a * L * 0.5 + b * L)


NETS = {
    'A': [[(0, 0), (1, -1), (1, 0)], [(1, -1), (1, 0), (2, -1)], [(1, 0), (2, -1), (2, 0)], [(2, -1), (2, 0), (3, -1)],
          [(2, 0), (3, -1), (3, 0)], [(3, -1), (3, 0), (4, -1)], [(3, 0), (4, -1), (4, 0)]],
    'B': [[(0, -1), (1, -1), (0, 0)], [(0, 0), (1, -1), (1, 0)], [(-1, 1), (0, 0), (0, 1)], [(0, 0), (1, 0), (0, 1)],
          [(0, 1), (1, 0), (1, 1)], [(1, 0), (2, 0), (1, 1)], [(1, 1), (2, 0), (2, 1)], [(1, 1), (2, 1), (1, 2)]],
    'C': [[(-1, 0), (0, -1), (0, 0)], [(0, -1), (1, -2), (1, -1)], [(0, -1), (1, -1), (0, 0)], [(0, 0), (1, -1), (1, 0)],
          [(1, -1), (2, -1), (1, 0)], [(1, 0), (2, -1), (2, 0)], [(0, 0), (1, 0), (0, 1)], [(1, 0), (2, 0), (1, 1)]],
    'D': [[(0, -1), (1, -1), (0, 0)], [(1, -1), (2, -1), (1, 0)], [(0, 0), (1, -1), (1, 0)], [(-1, 1), (0, 0), (0, 1)],
          [(0, 0), (1, 0), (0, 1)], [(0, 1), (1, 0), (1, 1)], [(1, 0), (2, 0), (1, 1)], [(1, 1), (2, 0), (2, 1)]],
    'E': [[(0, 0), (1, -1), (1, 0)], [(1, -1), (2, -1), (1, 0)], [(1, 0), (2, -1), (2, 0)], [(1, 0), (2, 0), (1, 1)],
          [(0, 1), (1, 0), (1, 1)], [(0, 0), (1, 0), (0, 1)], [(0, -1), (1, -1), (0, 0)], [(-1, 1), (0, 0), (0, 1)]],
}


def _nets_row():
    parts, lab = [], []
    spots = {'A': (14, 78), 'B': (160, 58), 'C': (290, 88), 'D': (420, 58), 'E': (560, 58)}
    verdict = {'A': ('only 7!', 'red'), 'B': ('OK', 'green'), 'C': ('5 meet', 'red'), 'D': ('5 meet', 'red'), 'E': ('6 meet', 'red')}
    bad = {'C': (1, 0), 'D': (1, 0), 'E': (1, 0)}
    for k, tris in NETS.items():
        ox, oy = spots[k]
        for i, t in enumerate(tris):
            f = 'none'
            if k == 'B':
                f = 'b' if i < 4 else 'o'
            parts.append(poly([_P(a, b, ox, oy) for a, b in t], k='ink', fill=f, sw=1.6))
        if k in bad:
            x, y = _P(*bad[k], ox, oy)
            parts.append(circle(x, y, 9, k='red', sw=2.6))
        lab.append(text(ox + 30, 20, k, k='ink', size=20, font='print', weight='700'))
        lab.append(text(ox + 30, 196, verdict[k][0], k=verdict[k][1], size=20, font='scrawl'))
    return svg(680, 210, rough(*parts) + ''.join(lab),
               'The five nets: A has only 7 triangles; C and D have 5 triangles meeting at one point; E has 6; B works')


def _octa():
    cx, cy = 150, 120
    T, Bm = (cx, cy - 95), (cx, cy + 95)
    Lp, Rp, F, Bk = (cx - 95, cy), (cx + 95, cy), (cx + 25, cy + 26), (cx - 25, cy - 26)
    parts = [poly([T, Lp, F], k='ink', fill='b'), poly([T, F, Rp], k='ink', fill='b'),
             poly([Bm, Lp, F], k='ink', fill='o'), poly([Bm, F, Rp], k='ink', fill='o'),
             line(*T, *Bk, k='muted', dash=True, w=1.5), line(*Lp, *Bk, k='muted', dash=True, w=1.5),
             line(*Rp, *Bk, k='muted', dash=True, w=1.5), line(*Bm, *Bk, k='muted', dash=True, w=1.5)]
    lab = [text(cx + 120, cy - 50, 'top 4 faces', k='pen', size=18, anchor='start'),
           text(cx + 120, cy - 28, '(blue fan)', k='pen', size=16, anchor='start'),
           text(cx + 120, cy + 50, 'bottom 4 faces', k='orange', size=18, anchor='start'),
           text(cx + 120, cy + 72, '(orange fan)', k='orange', size=16, anchor='start')]
    # net B big, with fold arrows
    ox, oy, L = 455, 92, 52
    for i, t in enumerate(NETS['B']):
        parts.append(poly([_P(a, b, ox, oy, L) for a, b in t], k='ink', fill='b' if i < 4 else 'o', sw=1.8))
        cxx = sum(_P(a, b, ox, oy, L)[0] for a, b in t) / 3
        cyy = sum(_P(a, b, ox, oy, L)[1] for a, b in t) / 3
        lab.append(text(cxx, cyy + 6, i + 1, k='ink', size=15))
    x0, y0 = _P(0, 0, ox, oy, L)
    x1, y1 = _P(1, 1, ox, oy, L)
    parts += [circle(x0, y0, 6, k='pen', fill='paper'), circle(x1, y1, 6, k='orange', fill='paper')]
    lab += [text(x0 - 16, y0 - 34, '4 round here', k='pen', size=16, anchor='end'),
            text(x1 + 34, y1 + 50, '4 round here', k='orange', size=16, anchor='start'),
            text(ox + 40, 300, 'each fan folds into a pyramid;', k='ink', size=16),
            text(ox + 40, 320, 'the two pyramids meet base to base', k='ink', size=16)]
    parts.append(arrow(x0 - 70, y0 - 10, x0 - 20, y0 + 6, k='pen', bend=-0.3))
    parts.append(arrow(x1 + 70, y1 + 30, x1 + 14, y1 + 8, k='orange', bend=0.3))
    return svg(680, 332, rough(*parts) + ''.join(lab),
               'Octahedron coloured as a blue top pyramid and an orange bottom pyramid, next to net B with faces 1 to 4 blue and 5 to 8 orange')

Q.append(dict(
    n=16, orig=32, answer='B', topic='Nets & folding', attempt='C',
    question=f"""<p>A regular octahedron is a solid composed of {hl('eight equilateral triangles', 'g', 1)}, as shown in the image
below:</p>
{fig(Y, 'q16_octa', 'An octahedron: two square-based pyramids joined base to base', 190)}
<p class="stem">Which one of the following paper shapes will {hl('fold into an octahedron', 'b', 2)}?</p>
{fig(Y, 'q16_nets', 'Five nets of triangles A to E', 430)}""",
    options={'A': 'net A', 'B': 'net B', 'C': 'net C', 'D': 'net D', 'E': 'net E'},
    notes=[(1, 'g', 'Count first: a net must have exactly <b>8</b> triangles.'),
           (2, 'b', 'In an octahedron exactly <b>4</b> faces meet at every corner.')],
    steps=[
        f"""<p>Two quick tests knock out the wrong nets:</p>
<ul><li><b>Count</b> the triangles: there must be 8.</li>
<li><b>Look round each point</b>: an octahedron has 4 faces at every corner, so no point of the net may have 5 or more triangles round it (they would overlap when folded).</li></ul>
{_nets_row()}""",
        f"""<p>Only B survives. Check it really folds: B is two “fans” of 4 triangles. Each fan wraps round its middle point into a pyramid with no base,
and the two pyramids join along their square edges. That is exactly an octahedron.</p>{_octa()}
{calc(f'answer = {boxed("B")}')}""",
    ],
    answer_text='Net B: two fans of four triangles that fold into the top and bottom pyramids.',
    why={'A': 'A has only <b>7</b> triangles. One face would be missing.',
         'C': 'Five triangles meet at one point, but an octahedron only has 4 at a corner, so two faces would overlap.',
         'D': 'Same problem as C: five triangles round one point.',
         'E': 'Six triangles round one point make a flat hexagon, which can’t fold up at that point at all.'},
    fast='Count to 8 (A out). Circle any point with 5+ triangles round it (C, D, E out). B.',
))

# ---------------------------------------------------------------- 17 (Q36)
def _clock(cx, cy, r, h, m, k):
    parts = [circle(cx, cy, r, k=k, fill='paper', sw=2.4)]
    for i in range(12):
        a = math.radians(i * 30 - 90)
        parts.append(line(cx + (r - 7) * math.cos(a), cy + (r - 7) * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a), k='ink', w=1.4))
    am = math.radians(m * 6 - 90)
    ah = math.radians((h % 12) * 30 + m * 0.5 - 90)
    parts.append(line(cx, cy, cx + (r - 12) * math.cos(am), cy + (r - 12) * math.sin(am), k='ink', w=2.4))
    parts.append(line(cx, cy, cx + (r - 26) * math.cos(ah), cy + (r - 26) * math.sin(ah), k='ink', w=3.4))
    return parts


def _clocks():
    parts, lab = [], []
    specs = [(100, 'Lucy’s watch', 2, 30, 'pen', 'shows 2:30', '(30 min late by it)'),
             (300, 'real time', 2, 20, 'muted', '2:20', '(watch is 10 fast)'),
             (500, 'interview room', 2, 0, 'green', 'shows 2:00', 'ON TIME!')]
    for cx, title, h, m, k, sub, sub2 in specs:
        parts += _clock(cx, 100, 56, h, m, k)
        lab += [text(cx, 28, title, k=k, size=18, font='scrawl'), text(cx, 182, sub, k='ink', size=17),
                text(cx, 204, sub2, k=k, size=16)]
    parts.append(arrow(110, 222, 490, 222, k='red', bend=0.08))
    lab.append(text(300, 258, 'room clock = watch − 30 min', k='red', size=17))
    return svg(620, 268, rough(*parts) + ''.join(lab), 'Three clocks: Lucy’s watch shows 2:30, real time is 2:20, the interview-room clock shows 2:00')

Q.append(dict(
    n=17, orig=36, answer='E', topic='Clocks & time', attempt='',
    question=f"""<p>Lucy allowed an hour to travel to a job interview, {hl('intending to arrive exactly on time', 'y', 1)}. The train
which she took arrived {hl('ten minutes late', 'g', 2)} by her watch. The taxi which she then took got caught in
a traffic jam for {hl('an unexpected 15 minutes', 'g', 2)} and walking to the appropriate room took {hl('five minutes longer', 'g', 2)} than anticipated. {hl("The clock in the interview room was running 30 minutes slower than Lucy's watch", 'b', 3)} {hl('which was running ten minutes fast', 'p', 4)}.</p>
<p class="stem">According to the clock in the interview room, when did Lucy arrive?</p>""",
    options={'A': 'She was ten minutes early.', 'B': 'She was ten minutes late.', 'C': 'She was thirty minutes late.',
             'D': 'She was sixty minutes late.', 'E': 'She was on time.'},
    notes=[(1, 'y', 'She plans by her own watch.'),
           (2, 'g', 'Delays: add them up.'),
           (3, 'b', 'The room clock is compared with her <b>watch</b>, not with real time.'),
           (4, 'p', 'Red herring! The question never needs real time.')],
    steps=[
        f"""<p>Pick an example: say the interview is at 2:00. Lucy plans to arrive when her watch says 2:00.</p>
{calc('delays = 10 + 15 + 5 = <b>30 minutes</b>', f'so her watch says <b>2:30</b> when she arrives')}""",
        f"""<p>The room clock is 30 minutes behind her watch:</p>
{calc(f'2:30 − 30 min = 2:00 {ar()} exactly the interview time = {boxed("on time")}')}{_clocks()}""",
        f"""{note('The “ten minutes fast” is a distraction. Both her delays and the room clock are measured against her watch, so real time never matters.', 'trap')}""",
    ],
    answer_text='On time: the room clock is 30 minutes behind her watch, which cancels the 30 minutes of delays.',
    why={'A': '10 early comes from wrongly taking off the watch’s 10 minutes as well.',
         'B': '10 late comes from adding the watch’s 10 minutes in the wrong direction.',
         'C': '30 late is true by her <b>watch</b>, not by the room clock.',
         'D': '60 late adds the room clock’s 30 minutes instead of taking them away.'},
    fast='30 minutes of delays by her watch; the room clock is 30 behind her watch: on time.',
))
