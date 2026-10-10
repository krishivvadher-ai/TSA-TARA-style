import math
from wslib import *

Y = 2015
Q = []

MARQUEE = [('6 x 3', '20 x 10', '£150', '£45', '£25', '£80', '£300'),
           ('6 x 6', '20 x 20', '£200', '£60', '£35', '£95', '£390'),
           ('6 x 9', '20 x 30', '£235', '£85', '£55', '£115', '£490'),
           ('6 x 12', '20 x 40', '£280', '£95', '£45', '£120', '£540'),
           ('6 x 15', '20 x 50', '£380', '£125', '£80', '£155', '£740'),
           ('6 x 18', '20 x 60', '£440', '£145', '£90', '£185', '£860'),
           ('9 x 3', '30 x 10', '£175', '£65', '£45', '£95', '£380'),
           ('9 x 6', '30 x 20', '£235', '£85', '£55', '£115', '£490'),
           ('9 x 9', '30 x 30', '£320', '£105', '£65', '£135', '£625'),
           ('9 x 12', '30 x 40', '£380', '£125', '£75', '£155', '£735'),
           ('9 x 15', '30 x 50', '£440', '£145', '£80', '£185', '£850'),
           ('9 x 18', '30 x 60', '£520', '£165', '£90', '£230', '£1,005'),
           ('9 x 21', '30 x 70', '£590', '£185', '£100', '£260', '£1,135'),
           ('9 x 24', '30 x 80', '£680', '£205', '£110', '£280', '£1,275'),
           ('9 x 27', '30 x 90', '£730', '£225', '£120', '£310', '£1,385'),
           ('9 x 30', '30 x 100', '£810', '£245', '£130', '£380', '£1,565')]


def _marquee_rows():
    rows = []
    for r in MARQUEE:
        r = list(r)
        if r[0] == '9 x 27':
            r[0] = hl(r[0], 'g')
            r[6] = hl(r[6], 'g')
        rows.append(r)
    return rows


# ---------------------------------------------------------------- 9 (Q19)
def _floor():
    ox, oy, m = 50, 50, 20
    parts = [rect(ox, oy, 27 * m, 9 * m, k='ink', fill='paper', sw=2.4)]
    lab = []
    for row in (0, 1):
        for i in range(5):
            cx, cy = ox + 54 + i * 108, oy + 46 + row * 88
            parts.append(circle(cx, cy, 20, k='orange', fill='o', sw=2))
            for j in range(8):
                a = math.radians(j * 45)
                lab.append(circle(cx + 31 * math.cos(a), cy + 31 * math.sin(a), 4.5, k='pen', fill='b', sw=1.4))
    parts += [line(ox, oy - 18, ox + 27 * m, oy - 18, k='red', tail=True, head=True, w=2),
              line(ox - 18, oy, ox - 18, oy + 9 * m, k='red', tail=True, head=True, w=2)]
    lab += [text(ox + 13.5 * m, oy - 26, '27 m', k='red', size=20, font='scrawl'),
            text(ox - 26, oy + 4.5 * m + 6, '9 m', k='red', size=20, font='scrawl', anchor='end'),
            text(ox + 13.5 * m, oy + 9 * m + 32, '9 × 27 = 243 m², just over the 240 m² needed', k='green', size=19),
            text(ox + 13.5 * m, oy + 9 * m + 58, '10 round tables × 8 gilt chairs = 80 seats', k='ink', size=17)]
    return svg(620, 300, rough(*parts) + ''.join(lab),
               'Floor plan of a 9 by 27 metre marquee holding ten round tables of eight chairs')

Q.append(dict(
    n=9, orig=19, answer='D', topic='Best price from a table',
    question=f"""<p>Steve and Jen are getting married and would like to have their reception in a marquee. There will
be {hl('80 people', 'g', 1)} attending in total and they would like to have the {hl('most expensive tables and chairs', 'p', 2)}
– {hl('eight people will sit at each table', 'y', 3)}. The capacity for a marquee can be worked out using the
industry standard of allowing {hl('3 m<sup>2</sup> per person', 'y', 4)}. Price lists from the hire company they will use
are given below:</p>
{table(_marquee_rows(), head=['Size (m)', 'Size (ft)', 'Marquee', 'Carpet', 'Lighting', 'Lining', 'Complete Package'])}
{table([['Bistro chair', '£1.30'], ['Gilt chair', hl('£2.40', 'g')], ['Trestle table (seats 6)', '£4.00'],
        ['Round table (seats 8)', hl('£6.00', 'g')], ['Patio table (seats 4)', '£4.00']], head=['Item', 'Cost'])}
<p class="stem">What is the {hl('lowest total cost of a complete marquee package plus tables and chairs', 'b', 5)} for Steve
and Jen's reception?</p>""",
    options={'A': '£982', 'B': '£1,385', 'C': '£1,529', 'D': '£1,637', 'E': '£1,817'},
    notes=[(1, 'g', '80 people: 80 chairs, and 80 × 3 m² of floor.'),
           (2, 'p', 'Not the cheapest furniture! Gilt chairs (£2.40) and round tables (£6.00).'),
           (3, 'y', 'Round tables seat exactly 8, so 80 ÷ 8 = 10 tables.'),
           (4, 'y', 'Area needed = 80 × 3 = 240 m². Size (m) is width × length, so multiply.'),
           (5, 'b', '“Lowest” refers to the marquee: the smallest one that is big enough. Use the <b>Complete Package</b> column.')],
    steps=[
        f"""<p>Marquee area needed:</p>
{calc('80 × 3 = <b>240 m²</b>',
      f'6 m wide: biggest is 6 × 18 = 108 {cross()}',
      f'9 × 24 = 216 {cross()} too small',
      f'9 × 27 = 243 {tick()} smallest that fits {ar()} package <b>£1,385</b>')}""",
        f"""<p>The most expensive furniture:</p>
{calc('80 gilt chairs: 80 × £2.40 = <b>£192</b>', '80 ÷ 8 = 10 round tables: 10 × £6 = <b>£60</b>')}
{note('80 × 2.40: do 8 × 24 = 192.', 'tip')}
{_floor()}""",
        f"""{calc(f'£1,385 + £192 + £60 = {boxed("£1,637")}')}""",
    ],
    answer_text='£1,637: the 9 × 27 m package (£1,385) + 80 gilt chairs (£192) + 10 round tables (£60).',
    why={'A': '£982 uses the marquee alone (£730) instead of the complete package: 730 + 192 + 60.',
         'B': '£1,385 is just the marquee package. It forgets the tables and chairs.',
         'C': '£1,529 uses the cheap bistro chairs (£104) and £4 tables (£40), but they want the <b>most expensive</b>.',
         'E': '£1,817 uses the 9 × 30 package (£1,565): one size bigger than needed.'},
    fast='240 m² → 9 × 27 (243 m²) → £1,385. Add 80 × 2.40 = 192 and 10 × 6 = 60: £1,637.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _sorted_bars():
    X = lambda v: 70 + v * 3.4
    data = [('7MO', 20), ('7EV', 36), ('7SP', 49), ('7BR', 57), ('7RA', 71), ('7LE', 82)]
    parts, lab = [], []
    for g in range(0, 101, 20):
        parts.append(line(X(g), 30, X(g), 250, k='muted' if g else 'ink', w=1.5 if g else 2))
        lab.append(text(X(g), 272, g, k='muted', size=15))
    for i, (name, v) in enumerate(data):
        y = 38 + i * 35
        parts.append(rect(X(0), y, X(v) - X(0), 24, k='ink', fill='b', sw=1.6))
        lab.append(text(X(0) - 8, y + 18, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 6, y + 18, v, k='pen', size=17, anchor='start'))
    notes_ = [(20, 0, 'ends ON the first line'), (49, 2, 'just short of halfway, 40 to 60'), (82, 5, 'pokes just past 80')]
    for v, i, t in notes_:
        y = 38 + i * 35 + 12
        lab.append(text(X(100) + 10, y + 5, t, k='red', size=16, anchor='start'))
        parts.append(line(X(v) + 32, y, X(100) + 4, y, k='red', w=1.4, dash=True))
    return svg(660, 284, rough(*parts) + ''.join(lab),
               'Correct bar chart: bars 20, 36, 49, 57, 71 and 82 against gridlines every 20; the shortest ends on the first line and the longest just past 80')

Q.append(dict(
    n=10, orig=20, answer='E', topic='Reading charts',
    question=f"""<p>The maths sets at Newtown Comprehensive are identified by their teacher's name. Every year
the Head of Maths gives the same test to all the maths sets at the end of year 7, calculates the
average mark for each set and then produces the results on a bar chart in {hl('ascending order', 'y', 1)}. He
is asked to present the graphs for the last five years to the Board of Governors. Unfortunately,
when they were cut and pasted onto one sheet by the Clerk to the Governors, the {hl('years were missed off', 'p', 2)}.</p>
<p>The results for last year were as follows:</p>
{table([['<b><i>Av. mark</i></b>', '57', '36', '82', '20', '71', '49']], head=['<i>Set</i>', '7BR', '7EV', '7LE', '7MO', '7RA', '7SP'])}
<p class="stem">Which one of these five graphs shows {hl("last year's results", 'b', 3)}?</p>
{fig(Y, 'ps_q10_bars', 'Five horizontal bar charts A to E, each with six bars in ascending order and gridlines dividing the width into five', 420)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'y', 'Sort the marks from smallest to biggest: that is the order of the bars.'),
           (2, 'p', 'All five charts look alike (six bars getting longer). Only the exact lengths tell them apart.'),
           (3, 'b', 'Match each bar length to 20, 36, 49, 57, 71, 82.')],
    steps=[
        f"""<p>Put the marks in ascending order:</p>
{calc('7MO 20, 7EV 36, 7SP 49, 7BR 57, 7RA 71, 7LE 82')}""",
        f"""<p>Scale: each chart is 5 squares wide and marks go up to 100, so <b>one square = 20 marks</b>. Use landmarks:</p>{_sorted_bars()}""",
        f"""<p>Check the landmarks on each chart:</p>
{calc('shortest bar ends exactly on the first line (20)? B and C go past it ' + cross(),
      'longest bar just past the 80 line (82)? A stops exactly on it ' + cross(),
      '3rd bar nearly halfway between 40 and 60 (49)? D stops just after 40 ' + cross(),
      f'E passes every check {tick()} {ar()} {boxed("E")}')}""",
    ],
    answer_text='Graph E: bars at 20, 36, 49, 57, 71 and 82.',
    why={'A': 'A’s longest bar stops exactly on the 80 line (should be 82) and its 4th bar passes the 60 line (should be 57).',
         'B': 'B’s shortest bar is about 26, not 20, and its longest only reaches about 78.',
         'C': 'C’s first three bars are too long: about 24, 42 and 51 instead of 20, 36 and 49.',
         'D': 'D’s 3rd bar only reaches about 42 (should be 49) and its 4th passes the 60 line (should be 57).'},
    fast='One square = 20. Shortest on the first line rules out B and C; longest just past 80 rules out A; 49 nearly halfway between 40 and 60 rules out D.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _income():
    X = lambda v: 30 + v * 0.093
    parts = [rect(X(0), 70, X(4385) - X(0), 46, k='ink', fill='g', sw=1.8),
             rect(X(4385), 70, X(5585) - X(4385), 46, k='ink', fill='o', sw=1.8),
             line(X(5905), 40, X(5905), 140, k='red', w=2, dash=True)]
    lab = [text((X(0) + X(4385)) / 2, 99, 'tax-free allowance £4,385', k='ink', size=17),
           text((X(4385) + X(5585)) / 2, 99, '£1,200', k='ink', size=16),
           text(X(0), 56, 'Mary earns £5,585', k='ink', size=17, anchor='start'),
           text(X(5905) + 6, 34, '10% band', k='red', size=15, anchor='end'),
           text(X(5905) + 6, 160, 'ends at 4,385 + 1,520', k='red', size=15, anchor='end'),
           text(300, 196, 'all £1,200 is in the 10% band: 10% of 1,200 = £120', k='green', size=20, font='scrawl')]
    parts.append(brace(X(4385), X(5585), 122, '', k='orange'))
    return svg(620, 210, rough(*parts) + ''.join(lab),
               'Income bar: 4,385 pounds tax-free, then 1,200 pounds taxed at 10 percent, all inside the 10 percent band')

Q.append(dict(
    n=11, orig=24, answer='B', topic='Tax & allowances',
    question=f"""<p>Nowadays many people in the UK work out their own income tax bills. Everyone has a personal
allowance which is the amount of money they can earn each tax year before they start paying
tax. Income above the personal allowance is taxed in bands. The UK tax bands and personal
allowances for four tax years are shown below. {hl('The tax year runs from 6 April to 5 April the following year', 'y', 1)}.</p>
{table([['Starting Rate at 10% on the first', '1500', hl('1520', 'g'), '1880', '1920'],
        ['Basic Rate at 22% on the next', '----', '26880', '27520', '27980'],
        ['Basic Rate at 23% on the next', '26500', '----', '----', '----'],
        ['Higher Rate at 40%', 'over 28000', 'over 28400', 'over 29400', 'over 29900'],
        ['<b><i>Personal Allowance</i></b>', '', '', '', ''],
        ['Aged under 65', '4335', hl('4385', 'g'), '4535', '4615'],
        ['Aged 65 and over but under 75', '5720', '5790', '5990', '6100'],
        ['Aged 75 and over', '5980', '6050', '6260', '6370'],
        ["<b><i>Married Couple's Allowance</i></b>", '', '', '', ''],
        ['Elder spouse aged', '', '', '', ''],
        ['Under 65', '1970', hl('----', 'p', 4), '----', '----'],
        ['65 and over but under 75', '5125', '5185', '5365', '5465'],
        ['75 and over', '5195', '5255', '5435', '5535']],
       head=['<i>TAX RATES</i>', '1999-2000', hl('2000-01', 'g', 2), '2001-02', '2002-03'])}
<p>{hl('Mary is 52 and her husband is 58', 'p', 4)}. Her only earnings each year are from a summer job.
{hl('Between 6 April 2000 and 5 April 2001', 'g', 2)} she earned {hl('£5,585', 'g', 3)}.</p>
<p class="stem">How much tax did she pay?</p>""",
    options={'A': 'None', 'B': '£120', 'C': '£125', 'D': '£152', 'E': '£1,200'},
    notes=[(1, 'y', 'So 6 April 2000 to 5 April 2001 is the <b>2000-01</b> tax year.'),
           (2, 'g', 'Use only the 2000-01 column.'),
           (3, 'g', 'Her whole income for that year.'),
           (4, 'p', 'Elder spouse is 58, so “under 65”, and in 2000-01 there is no married couple’s allowance (----).')],
    steps=[
        f"""<p>Pick the right column and rows:</p>
{calc(f'6 Apr 2000 to 5 Apr 2001 {ar()} <b>2000-01</b>',
      f'Mary is 52 {ar()} personal allowance (under 65) = <b>£4,385</b>',
      f'husband 58 {ar()} married couple’s allowance under 65 = ---- = nothing')}""",
        f"""<p>Tax only the part above her allowance:</p>
{calc('£5,585 − £4,385 = <b>£1,200</b> taxable',
      f'starting rate: 10% on the first £1,520 {ar()} all £1,200 fits in this band',
      f'10% of £1,200 = {boxed("£120")}')}{_income()}""",
    ],
    answer_text='£120: £1,200 above her £4,385 allowance, all taxed at 10%.',
    why={'A': '“None” needs a bigger allowance, such as adding a married couple’s allowance. Her husband is under 65, and in 2000-01 that row is empty.',
         'C': '£125 uses the 1999-2000 allowance (£4,335): 1,250 × 10%. Her tax year is 2000-01.',
         'D': '£152 is 10% of the whole £1,520 band. She only has £1,200 to tax.',
         'E': '£1,200 is her <b>taxable income</b>, not the tax. It forgets the 10%.'},
    fast='2000-01, under 65: 5,585 − 4,385 = 1,200, inside the 10% band, so £120.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _rain():
    cum = [0, 50, 92, 110, 140, 170, 232, 262, 357, 400, 445, 510, 530]
    X = lambda m: 70 + m * 44
    Yr = lambda r: 300 - r * 0.46
    parts = [line(X(0), Yr(0), X(12.4), Yr(0), k='ink', head=True), line(X(0), Yr(0), X(0), Yr(600), k='ink', head=True)]
    lab = []
    for r in range(0, 601, 100):
        lab.append(text(X(0) - 8, Yr(r) + 5, r, k='muted', size=14, anchor='end'))
    for i, m in enumerate('JFMAMJJASOND'):
        lab.append(text(X(i + 0.5), Yr(0) + 20, m, k='muted', size=15))
    parts.append(rect(X(5), Yr(600), X(9) - X(5), Yr(0) - Yr(600), k='muted', fill='y', sw=1))
    parts.append(poly([(X(i), Yr(v)) for i, v in enumerate(cum)], k='pen', sw=2.8, closed=False))
    for m, v in ((5, 170), (9, 400)):
        parts.append(line(X(0), Yr(v), X(m), Yr(v), k='red', w=1.8, dash=True))
        parts.append(circle(X(m), Yr(v), 6, k='red', fill='paper', sw=2.4))
    parts.append(line(X(9) + 70, Yr(170), X(9) + 70, Yr(400), k='green', tail=True, head=True, w=2.2))
    lab += [text(X(5) + 12, Yr(170) + 30, 'start of June ≈ 170', k='red', size=16, anchor='start'),
            text(X(9) - 6, Yr(400) - 12, 'end of Sept ≈ 400', k='red', size=16, anchor='end'),
            text(X(9) + 80, Yr(285) + 6, '230 mm', k='green', size=20, font='scrawl', anchor='start'),
            text(X(7), Yr(0) + 44, 'Jun to Sep = 4 months', k='orange', size=17),
            text(X(0) + 16, Yr(600) + 20, 'mm so far', k='muted', size=14, anchor='start')]
    return svg(660, 360, rough(*parts) + ''.join(lab),
               'Cumulative rainfall graph: about 170 mm at the start of June and 400 mm at the end of September, a rise of 230 mm over 4 months')

Q.append(dict(
    n=12, orig=25, answer='D', topic='Cumulative graphs',
    question=f"""<p>The graph below shows the {hl('cumulative', 'y', 1)} rainfall for Malvern Wells in the UK for 2010.</p>
{fig(Y, 'ps_q12_rain', 'Cumulative rainfall graph for 2010, rising from 0 at the start of January to about 530 mm at the end of December, with month gridlines', 440)}
<p class="stem">What, approximately, was the {hl('average monthly rainfall', 'b', 4)} from the {hl('<b>beginning</b>', 'p', 2)} of June to the {hl('<b>end</b>', 'p', 3)}
of September?</p>""",
    options={'A': '30 mm/month', 'B': '40 mm/month', 'C': '48 mm/month', 'D': '57 mm/month', 'E': '100 mm/month'},
    notes=[(1, 'y', 'Cumulative = running total since 1 January. Rain in a period = later reading − earlier reading.'),
           (2, 'p', 'Beginning of June = end of May = the gridline <b>before</b> the June column.'),
           (3, 'p', 'End of September = the gridline <b>after</b> the Sep column.'),
           (4, 'b', 'June, July, August, September = 4 months. Divide by 4.')],
    steps=[
        f"""<p>Read the running total at the two gridlines:</p>
{calc('beginning of June (end of May) ≈ <b>170 mm</b>', 'end of September ≈ <b>400 mm</b>')}{_rain()}""",
        f"""{calc('rain in Jun–Sep = 400 − 170 = <b>230 mm</b>', f'230 ÷ 4 = 57.5 {ar()} about {boxed("57 mm/month")}')}
{note('Never divide a cumulative reading on its own. 400 ÷ 4 = 100 counts all the rain since January.', 'trap')}""",
    ],
    answer_text='About 57 mm/month: 230 mm fell over the 4 months.',
    why={'A': '30 mm is roughly July on its own (232 to 262), one month, not the average.',
         'B': '40 starts from the <b>end</b> of June (≈ 230) instead of the beginning: 170 ÷ 4 ≈ 43.',
         'C': '48 stops at the end of <b>August</b> (≈ 357): 187 ÷ 4 ≈ 47.',
         'E': '100 forgets the graph is cumulative: 400 ÷ 4 = 100.'},
    fast='Take the end-of-May reading (170) from the end-of-September reading (400): 230 ÷ 4 ≈ 57.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _bath_graph():
    s, ox, oy = 50, 90, 290
    P = lambda a, b: (ox + a * s, oy - b * s)
    parts, lab = [], []
    for i in range(9):
        parts.append(line(ox + i * s, oy, ox + i * s, oy - 5 * s, k='muted', w=1))
        lab.append(text(ox + i * s, oy + 22, f'{i * 1.5:g}', k='muted', size=14))
    for j in range(6):
        parts.append(line(ox, oy - j * s, ox + 8 * s, oy - j * s, k='muted', w=1))
    for j, t in ((1, '¼'), (2, '½'), (3, '¾'), (4, 'full')):
        lab.append(text(ox - 8, oy - j * s + 6, t, k='ink', size=16, anchor='end'))
    parts.append(line(*P(0, 4), *P(8, 4), k='red', w=1.8, dash=True))
    parts.append(poly([P(0, 0), P(1, 1), P(6, 3), P(8, 3)], k='pen', sw=3.4, closed=False))
    parts.append(circle(*P(1, 1), 5, k='pen', fill='paper'))
    parts.append(circle(*P(6, 3), 5, k='pen', fill='paper'))
    lab += [text(P(1, 1)[0] + 10, P(1, 1)[1] + 30, 'both taps: 90 L in 1.5 min', k='green', size=16, anchor='start'),
            text(P(3.2, 2.2)[0], P(3.2, 2.2)[1] - 14, 'hot only: 180 L in 7.5 min', k='orange', size=16, rotate=-21),
            text(P(7, 3)[0], P(7, 3)[1] - 12, 'cooling', k='pen', size=16),
            text(P(4, 4)[0], P(4, 4)[1] - 10, 'full = 360 L (never reached)', k='red', size=15),
            text(ox + 4 * s, oy + 46, 'time (minutes): 1 square = 1.5 min', k='ink', size=15),
            text(ox - 52, oy - 5 * s - 14, 'depth', k='ink', size=15, anchor='start')]
    return svg(560, 346, rough(*parts) + ''.join(lab),
               'Depth-time graph on a grid: up 1 square in the first square, then up 2 squares over the next 5 squares to three quarters full, then flat')

Q.append(dict(
    n=13, orig=26, answer='B', topic='Rates & graphs',
    question=f"""<p>Duncan's bath has a {hl('flat base and vertical sides', 'y', 1)}. It can be filled completely from the {hl('hot tap in 15 minutes', 'g', 2)} or from the {hl('cold tap in 10 minutes', 'g', 2)}. Its capacity is {hl('360 litres', 'g', 3)}. When preparing a bath,
Duncan's habit is to {hl('run both taps together for 1½ minutes', 'g', 4)}, before turning off the cold tap. He
{hl('turns the hot tap off when the bath is ¾ full', 'p', 5)}, then {hl('leaves the water for a while', 'y', 6)} to cool down to a
suitable temperature before he climbs in.</p>
<p class="stem">Which graph would show how the depth of water increases as Duncan prepares his bath?</p>
{fig(Y, 'ps_q13_graphs', 'Five depth-time graphs A to E on 8 by 5 grids, each rising 1 square in the first square, then more slowly, then flat', 520)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'y', 'Straight sides: depth goes up in step with the volume. Steady flow = straight line.'),
           (2, 'g', 'Turn these into litres per minute.'),
           (3, 'g', 'Full = 360 L, so ¼ = 90 L and ¾ = 270 L.'),
           (4, 'g', 'Stage 1: both taps, 1.5 minutes.'),
           (5, 'p', 'It stops at ¾, not full.'),
           (6, 'y', 'Then flat: the depth stays the same while it cools.')],
    steps=[
        f"""<p>Flow rates:</p>
{calc('hot: 360 ÷ 15 = <b>24 L/min</b>', 'cold: 360 ÷ 10 = <b>36 L/min</b>', 'both: 24 + 36 = <b>60 L/min</b>')}""",
        f"""<p>Stage 1, both taps for 1.5 minutes:</p>
{calc(f'1.5 × 60 = 90 L = ¼ of the bath')}
<p>Every graph starts by going 1 square across and 1 square up. So <b>1 square across = 1.5 min</b> and <b>1 square up = ¼ bath</b>.</p>""",
        f"""<p>Stage 2, hot tap only, from ¼ to ¾ full:</p>
{calc(f'270 − 90 = 180 L more', f'180 ÷ 24 = 7.5 min {ar()} 7.5 ÷ 1.5 = <b>5 squares across</b>', f'¼ to ¾ = <b>2 squares up</b>')}
{_bath_graph()}""",
        f"""<p>So after the first corner the line climbs 2 squares while going 5 across, and then goes flat at 3 squares up.</p>
{calc('C, E: flatten at 4 squares (full) ' + cross(), 'A: reaches ¾ after only 4 squares across (too fast) ' + cross(),
      'D: takes 6 squares across (too slow) ' + cross(), f'B: 2 up in 5 across, flat at ¾ {tick()} {ar()} {boxed("B")}')}""",
    ],
    answer_text='Graph B: up 1 square in 1.5 min, then 2 more squares over 7.5 min, then flat at ¾.',
    why={'A': 'A climbs from ¼ to ¾ in 4 squares (6 min): the hot tap would have to fill the bath in 12 minutes, not 15.',
         'C': 'C keeps filling to the top (4 squares). He turns the tap off at ¾.',
         'D': 'D takes 6 squares (9 min) for the hot stage: that hot tap would need 18 minutes to fill the bath.',
         'E': 'E also fills to the very top (4 squares) instead of stopping at ¾.'},
    fast='Both taps: 90 L = ¼ in 1.5 min (1 square each way). Hot: 180 L ÷ 24 = 7.5 min = 5 squares for 2 squares up, flat at ¾: B.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _league():
    teams = [('East Rovers', 31, 12, '43 ✓', 'green'),
             ('West Athletic', 24, 18, '42 ✓', 'green'),
             ('North Rangers', 22, 9, '31, but 9 wins ✓', 'green'),
             ('South United', 22, 9, '31, only 7 wins ✗', 'red'),
             ('Top Town', 17, 21, '38 ✓', 'green'),
             ('Bottom Albion', 15, 15, '30 ✗', 'red')]
    X = lambda p: 140 + p * 7.6
    parts, lab = [], []
    for i, (name, now, extra, note_, col) in enumerate(teams):
        y = 40 + i * 40
        parts.append(rect(X(0), y, X(now) - X(0), 26, k='ink', fill='b', sw=1.5))
        parts.append(f'<rect x="{X(now)}" y="{y}" width="{X(now + extra) - X(now):.1f}" height="26" class="k-ink f-y" stroke-width="1.5" stroke-dasharray="5 4"/>')
        lab.append(text(X(0) - 8, y + 19, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(now + extra) + 8, y + 19, note_, k=col, size=17, anchor='start'))
    parts.append(line(X(31), 26, X(31), 290, k='red', w=2.4, dash=True))
    lab += [text(X(31), 310, 'East has 31 points and 8 wins already, even if it loses the rest', k='red', size=16),
            text(X(0), 22, 'blue = points now, yellow = most it can add (3 per game left)', k='muted', size=14, anchor='start')]
    return svg(660, 322, rough(*parts) + ''.join(lab),
               'Bars of points now plus the most each team can add; the line at 31 is East Rovers lowest possible total')

Q.append(dict(
    n=14, orig=30, answer='D', topic='League tables',
    question=f"""<p>Towards the end of a sports season in which {hl('all teams in the league play each other four times', 'y', 1)},
the league positions are as follows:</p>
{table([['East Rovers', '16', '8', '7', '1', '31'],
        ['West Athletic', '14', '7', '3', '4', '24'],
        ['North Rangers', '17', '6', '4', '7', '22'],
        ['South United', '17', '4', '10', '3', '22'],
        ['Top Town', '13', '3', '8', '2', '17'],
        ['Bottom Albion', '15', '3', '6', '6', '15']],
       head=['', 'Played', 'Won', 'Drawn', 'Lost', 'Pts'])}
<p>{hl('Three points are awarded for a win, 1 point per draw and 0 for a loss', 'y', 2)}. At the end of the season,
{hl('if two teams have the same number of points, the league will be decided by the highest number of games won', 'p', 3)}.</p>
<p class="stem">How many of the competing teams {hl('could win', 'b', 4)} the league when all the games have been
completed?</p>""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'y', '6 teams: each plays 5 others × 4 = <b>20 games</b>. Games left = 20 − played.'),
           (2, 'y', 'Best case: win every game left, +3 each.'),
           (3, 'p', 'Tie-break on <b>wins</b>. Count wins, not just points.'),
           (4, 'b', '“Could” = is there any possible set of results where they finish top?')],
    steps=[
        f"""<p>Best possible finish for each team (win every game left):</p>
{table([['East Rovers', '4', '31 + 12 = 43', '12'],
        ['West Athletic', '6', '24 + 18 = 42', '13'],
        ['North Rangers', '3', '22 + 9 = <b>31</b>', '<b>9</b>'],
        ['South United', '3', '22 + 9 = <b>31</b>', '<b>7</b>'],
        ['Top Town', '7', '17 + 21 = 38', '10'],
        ['Bottom Albion', '5', '15 + 15 = 30', '8']],
       head=['Team', 'Games left', 'Most points', 'Wins then'])}""",
        f"""<p>Now the hurdle: East already has <b>31 points and 8 wins</b>, and can’t drop below that. To win, a team must beat 31,
or tie on 31 with <b>more than 8 wins</b>.</p>{_league()}""",
        f"""{calc(f'East {tick()} · West 42 {tick()} · Top Town 38 {tick()}',
      f'North 31 with 9 wins: ties East on points, wins the tie-break {tick()}',
      f'South 31 with 7 wins: loses the tie-break {cross()} · Bottom 30 {cross()}',
      f'East, West, North, Top Town = {boxed("4 teams")}')}
{note('Best case for North: North wins its last 3, East loses all 4, and the others don’t pass 31. Nothing in the table stops that.', 'check')}""",
    ],
    answer_text='4 teams: East, West, North and Top Town.',
    why={'A': '1 assumes the leaders have already won it. They can still be caught.',
         'B': '2 only counts the top two by points now and ignores Top Town’s 7 games in hand.',
         'C': '3 misses North: it can only tie East on 31 points, but it would have more wins (9 against 8).',
         'E': '5 includes South, which can also reach 31, but with only 7 wins it loses the tie-break to East.'},
    fast='East is stuck on at least 31 points and 8 wins. Max points: W 42, T 38, N 31 (9 wins), S 31 (7 wins), B 30. Count E, W, T, N = 4.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _hobby():
    X = lambda h: 120 + (h - 9) * 54
    rows = [('Painting', 20, 10, 12, 30, '$15/h'), ('Painting', 20, 10.5, 13, 40, '$16/h'), ('Painting', 50, 10, 12, 24, 'leave 9:10'),
            ('Dancing', 30, 9.5, 13, 45, 'leave 9:00'), ('Dancing', 10, 13, 17, 45, 'back 17:10'),
            ('Pottery', 60, 10, 11.5, 35, 'leave 9:00'), ('Pottery', 60, 11, 13, 40, '$20/h'),
            ('Writing', 10, 10, 12.5, 35, '$14/h'), ('Writing', 30, 14, 15.5, 24, '$16/h')]
    parts = [rect(X(9.25), 30, X(16.25) - X(9.25), 9 * 32 + 8, k='green', fill='g', sw=1.5)]
    lab = [text(X(9.25), 24, '9:15', k='green', size=15), text(X(16.25), 24, '16:15', k='green', size=15)]
    for h in range(9, 18):
        lab.append(text(X(h), 9 * 32 + 62, f'{h}:00', k='muted', size=13))
        parts.append(line(X(h), 9 * 32 + 40, X(h), 9 * 32 + 46, k='ink', w=1.4))
    for i, (name, tr, s, f, price, tag) in enumerate(rows):
        y = 36 + i * 32
        a, b = s - tr / 60, f + tr / 60
        bad = a < 9.25 or b > 16.25
        best = tag == '$14/h'
        parts.append(line(X(a), y + 12, X(b), y + 12, k='muted', w=2))
        parts.append(rect(X(s), y + 2, X(f) - X(s), 20, k='red' if bad else 'ink', fill='p' if bad else ('y' if best else 'b'), sw=2.4 if best else 1.4))
        lab.append(text(X(9) - 8, y + 17, f'{name} ${price}', k='ink', size=14, anchor='end'))
        lab.append(text(X(f) + X(b) - X(f) + 6, y + 17, tag, k='red' if bad else ('green' if best else 'pen'), size=14, anchor='start'))
    lab.append(text(X(13), 9 * 32 + 84, 'grey line = travelling, box = the class', k='muted', size=14))
    return svg(660, 9 * 32 + 96, rough(*parts) + ''.join(lab),
               'Timeline of the nine classes with travel time; four fall outside the 9:15 to 16:15 window; writing 10:00 to 12:30 is cheapest per hour at 14 dollars')

Q.append(dict(
    n=15, orig=31, answer='C', topic='Timetables & best value',
    question=f"""<p>I am planning to take up a new hobby. There are a number of classes available locally,
summarised in the table below:</p>
<p>[I {hl('do not want to have to leave home before 09:15', 'y', 1)} and I {hl('must be back by 16:15', 'y', 2)}. I will choose the
activity that is the {hl('cheapest per hour', 'b', 3)}.]</p>
{table([['Painting', '20 mins', '10:00', '12:00', '30'], ['', '20 mins', '10:30', '13:00', '40'], ['', '50 mins', '10:00', '12:00', '24'],
        ['Dancing', '30 mins', '9:30', '13:00', '45'], ['', '10 mins', '13:00', '17:00', '45'],
        ['Pottery', '60 mins', '10:00', '11:30', '35'], ['', '60 mins', '11:00', '13:00', '40'],
        ['Writing', '10 mins', '10:00', '12:30', '35'], ['', '30 mins', '14:00', '15:30', '24']],
       head=['Activity', hl('Travel time (one way)', 'p', 4), 'Start time', 'Finish time', 'Class price ($)'])}
<p class="stem">What will be the price of the class I will take?</p>""",
    options={'A': '$24', 'B': '$30', 'C': '$35', 'D': '$40', 'E': '$45'},
    notes=[(1, 'y', 'Leave time = start − travel. Must be 9:15 or later.'),
           (2, 'y', 'Home time = finish + travel. Must be 16:15 or earlier.'),
           (3, 'b', 'Price ÷ length of the class in hours. Not the cheapest price!'),
           (4, 'p', 'Travel is each way: count it before the class and after it.')],
    steps=[
        f"""<p>Cross out classes that break the time rules:</p>
{calc(f'Painting 10:00 with 50 min travel {ar()} leave 9:10 ' + cross(),
      f'Dancing 9:30 with 30 min {ar()} leave 9:00 ' + cross(),
      f'Dancing till 17:00 {ar()} home 17:10 ' + cross(),
      f'Pottery 10:00 with 60 min {ar()} leave 9:00 ' + cross())}""",
        f"""<p>Price per hour for the five that are left:</p>
{calc('Painting 10:00–12:00: $30 ÷ 2 = $15/h', 'Painting 10:30–13:00: $40 ÷ 2.5 = $16/h', 'Pottery 11:00–13:00: $40 ÷ 2 = $20/h',
      '<b>Writing 10:00–12:30: $35 ÷ 2.5 = $14/h</b>', 'Writing 14:00–15:30: $24 ÷ 1.5 = $16/h')}
{_hobby()}
{calc(f'cheapest per hour = Writing at $14/h {ar()} price {boxed("$35")}')}""",
    ],
    answer_text='$35: the 10:00–12:30 writing class, $14 an hour.',
    why={'A': '$24 is the cheapest <b>price</b>, not per hour. The $24 painting needs leaving at 9:10, and the $24 writing class is $16/h.',
         'B': '$30 painting is allowed and good value ($15/h), but writing is $1 an hour cheaper.',
         'D': '$40 classes cost $16/h (painting) or $20/h (pottery).',
         'E': '$45 dancing is cheap per hour, but one class means leaving at 9:00 and the other gets you home at 17:10.'},
    fast='Strike the four that break 9:15/16:15 (each has 50–60 min travel, a 9:30 start or a 17:00 finish). Of the rest, $35 ÷ 2.5 = $14/h is cheapest.',
))


# ---------------------------------------------------------------- 16 (Q32)
SMALL_X = [(410, 438), (490, 518), (622, 650), (702, 730), (780, 808), (860, 888), (940, 968), (1020, 1048)]
ROWS_Y = [(177, 232), (258, 313), (340, 395), (421, 476), (501, 557)]
BIG = [((597, 650), (368, 453)), ((676, 730), (368, 453)), ((597, 650), (470, 557)), ((676, 730), (470, 557))]


def _remote_plan():
    k, ox, oy = 0.27, 40, 30
    R = lambda xr, yr: ((610 - yr[1]) * k + ox, (xr[0] - 138) * k + oy, (yr[1] - yr[0]) * k, (xr[1] - xr[0]) * k)
    parts = [rect(ox, oy, 483 * k, 1045 * k, k='ink', fill='paper', sw=2.2)]
    for ci, xr in enumerate(SMALL_X):
        for ri, yr in enumerate(ROWS_Y):
            if ci in (2, 3) and ri >= 2:
                continue
            x, y, w, h = R(xr, yr)
            parts.append(rect(x, y, w, h, k='ink', fill='b', sw=1.2))
    for yr in (ROWS_Y[0], ROWS_Y[4]):
        x, y, w, h = R((1075, 1105), yr)
        parts.append(rect(x, y, w, h, k='ink', fill='black', sw=1.2))
    for xr, yr in BIG:
        x, y, w, h = R(xr, yr)
        parts.append(rect(x, y, w, h, k='ink', fill='o', sw=1.4))
    lab = []
    for ri, yr in enumerate(ROWS_Y):
        cx = (610 - (yr[0] + yr[1]) / 2) * k + ox
        lab.append(text(cx, oy - 8, f'r{ri + 1}', k='red', size=14))
    ex = ox + 483 * k / 2
    lab += [eye(ex, oy + 1045 * k + 34, k='ink', facing='up'),
            text(ex, oy + 1045 * k + 70, 'you look up', k='ink', size=15),
            text(ex, oy + 1045 * k + 88, 'from here', k='ink', size=15)]
    # the view (all buttons the same height), wider scale
    kv, vx, base = 0.78, 250, 230
    V = lambda yr: ((610 - yr[1]) * kv + vx, (yr[1] - yr[0]) * kv)
    parts.append(rect(vx, base, 483 * kv, 64, k='ink', fill='paper', sw=2.2))
    for yr in ((368, 453), (470, 557)):
        x, w = V(yr)
        parts.append(rect(x, base - 16, w, 16, k='orange', fill='o', sw=1.6))
    for ri, yr in enumerate(ROWS_Y):
        x, w = V(yr)
        parts.append(rect(x, base - 16, w, 16, k='ink', fill='b', sw=1.6))
        lab.append(text(x + w / 2, base - 26, f'r{ri + 1}', k='red', size=15))
    lab += [text(vx + 483 * kv / 2, base + 40, 'what you see (all buttons the same height)', k='ink', size=15),
            text(vx, 70, 'Turn the page so the arrow points up.', k='ink', size=16, anchor='start'),
            text(vx, 94, 'Each row r1 to r5 becomes one small block.', k='ink', size=16, anchor='start'),
            text(vx, 118, 'r5 (bottom of the picture) is on your LEFT.', k='red', size=16, anchor='start'),
            text(vx, 150, 'The big orange buttons sit by r3 to r5,', k='orange', size=16, anchor='start'),
            text(vx, 174, 'so they show on the left, filling the gaps.', k='orange', size=16, anchor='start')]
    return svg(640, 420, rough(*parts) + ''.join(lab),
               'The remote turned so you look at its end from below: the five rows become five blocks, row 5 on the left, with the big buttons filling the gaps on the left')


def _views_bd():
    boxes = [(9, 56), (68, 115), (127, 174), (186, 233), (245, 292)]
    parts, lab = [], []
    for ox, title, ok in ((20, 'B: big buttons taller ✓', True), (350, 'D: impossible ✗', False)):
        base = 150
        parts.append(rect(ox, base, 300, 54, k='ink', fill='paper', sw=2))
        for a, b in ((9, 68), (92, 150)):
            parts.append(rect(ox + a, base - 30, b - a, 30, k='orange', fill='o', sw=1.8))
        for i, (a, b) in enumerate(boxes):
            if not ok and i == 0:
                parts.append(f'<rect x="{ox + a}" y="{base - 14}" width="{b - a}" height="14" class="k-red f-none" stroke-width="2.2" stroke-dasharray="4 3"/>')
                continue
            parts.append(rect(ox + a, base - 14, b - a, 14, k='ink', fill='b', sw=1.6))
        lab.append(text(ox + 150, base + 84, title, k='green' if ok else 'red', size=20))
    parts += [arrow(20 + 60, 76, 20 + 34, 130, k='green', bend=0.2), arrow(350 + 60, 76, 350 + 34, 130, k='red', bend=0.2)]
    lab += [text(20 + 64, 70, 'r5 block in front of the big button', k='green', size=16, anchor='start'),
            text(350 + 64, 70, 'r5 block missing!', k='red', size=20, font='scrawl', anchor='start'),
            text(20 + 150, 258, 'orange = big buttons (behind)', k='orange', size=15),
            text(350 + 150, 258, 'but the black button is nearest you', k='red', size=15)]
    return svg(670, 270, rough(*parts) + ''.join(lab),
               'Views B and D side by side: in B the row-5 block sits in front of the tall big button; in D that block is missing')

Q.append(dict(
    n=16, orig=32, answer='D', topic='3D views',
    question=f"""<p>My TV remote control is shown below. {hl('All the buttons stick out', 'y', 1)} from the body of the remote
control.</p>
{fig(Y, 'ps_q16_remote', 'Remote control seen from above: rows of small buttons, four larger square buttons near the bottom left of centre, two black buttons at the right end, and an arrow pointing at the right-hand end', 380)}
<p class="stem">When {hl('viewed from the direction of the arrow', 'y', 2)}, which one of the diagrams below is {hl('<b>not</b>', 'b', 3)} a possible
view of the remote control?</p>
{fig(Y, 'ps_q16_views', 'Five end views A to E: a long body with five small blocks on top, some with taller blocks behind', 520)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'Every button shows up in the view, but we are <b>not told how far</b> each one sticks out. Big buttons could be taller.'),
           (2, 'y', 'You look at the right-hand end, along the rows. Each row of buttons lines up into one block.'),
           (3, 'b', 'Four views can be made with some choice of button heights. Find the one that can’t.')],
    steps=[
        f"""<p>Picture yourself at the arrow, looking along the remote:</p>{_remote_plan()}""",
        f"""<p>Button heights are unknown, so each view just picks different heights:</p>
<ul><li><b>A</b>: everything the same height. The big buttons fill the gaps between r5, r4 and r3. {tick()}</li>
<li><b>B</b>: both pairs of big buttons stick up higher, so they rise behind the small blocks. {tick()}</li>
<li><b>C</b>: like B, but the big buttons are stepped (a low edge at normal button height). {tick()}</li>
<li><b>E</b>: only the lower pair of big buttons is taller. {tick()}</li></ul>""",
        f"""<p>Now D: the left-hand small block (row 5) has vanished. Row 5 includes the black button, the one <b>nearest</b> your eye.
It sticks out, so it must always appear, in front of the big button.</p>{_views_bd()}
{calc(f'not possible = {boxed("D")}')}""",
    ],
    answer_text='View D: the row of buttons nearest you (with the black button) is missing.',
    why={'A': 'A is the view if every button sticks out the same amount.',
         'B': 'B is the view if the big buttons stick out further than the small ones.',
         'C': 'C fits big buttons that are taller with a lower step, so you see their edge at normal height too.',
         'E': 'E fits only the lower pair of big buttons being taller.'},
    fast='The views only differ in how high the big buttons are, which you’re not told. But D drops the front block of row 5 (the black button), which must always show.',
))


# ---------------------------------------------------------------- 17 (Q36)
def _signing():
    X = lambda m: 40 + m * 1.06
    parts, lab = [], []
    t = 0
    for i in range(7):
        parts.append(rect(X(t), 50, X(t + 60) - X(t), 40, k='ink', fill='g', sw=1.5))
        lab.append(text((X(t) + X(t + 60)) / 2, 76, '60', k='ink', size=15))
        parts.append(rect(X(t + 60), 50, X(t + 70) - X(t + 60), 40, k='ink', fill='p', sw=1.5))
        t += 70
    parts.append(rect(X(t), 50, X(540) - X(t), 40, k='ink', fill='g', sw=2.2))
    lab.append(text((X(t) + X(540)) / 2, 76, '50', k='red', size=16))
    for h in range(10):
        parts.append(line(X(h * 60), 96, X(h * 60), 106, k='ink', w=1.4))
        lab.append(text(X(h * 60), 124, f'{9 + h}', k='muted', size=14))
    lab += [text(X(0), 36, 'green = signing (minutes), pink = 10-minute break', k='muted', size=15, anchor='start'),
            text(X(270), 156, '7 × 60 + 50 = 470 minutes of signing', k='pen', size=19),
            text(X(510), 36, 'no full hour, no break', k='red', size=15, anchor='end')]
    return svg(640, 170, rough(*parts) + ''.join(lab),
               'Timeline 9 am to 6 pm: seven blocks of 60 minutes signing each followed by a 10 minute break, then a final 50 minutes of signing')

Q.append(dict(
    n=17, orig=36, answer='C', topic='Time & rates',
    question=f"""<p>A film star has agreed to sign autographs for £1 each at a charity function, all day {hl('from 9 am to 6 pm', 'g', 1)}.</p>
<p>He claims to sign his name consistently {hl('ten times every minute', 'g', 2)}, but insists on having a {hl('ten-minute break after each full hour of signing', 'p', 3)}.</p>
<p class="stem">How much do the organisers hope that the autographs will raise?</p>""",
    options={'A': '£4,500', 'B': '£4,600', 'C': '£4,700', 'D': '£4,800', 'E': '£5,400'},
    notes=[(1, 'g', '9 hours = 540 minutes.'),
           (2, 'g', '10 autographs a minute = £10 a minute.'),
           (3, 'p', 'Breaks come after 60 minutes of <b>signing</b>, not on the hour by the clock. So each cycle is 70 minutes.')],
    steps=[
        f"""<p>One cycle = 60 min signing + 10 min break = <b>70 min</b>.</p>
{calc(f'540 ÷ 70 = 7 cycles (490 min) with 50 min left', f'the last 50 min is all signing (not a full hour {ar()} no break needed)')}""",
        f"""{_signing()}
{calc('signing time = 7 × 60 + 50 = 470 min', f'470 × 10 = 4,700 autographs × £1 = {boxed("£4,700")}')}""",
    ],
    answer_text='£4,700: 470 minutes of signing at 10 a minute.',
    why={'A': '£4,500 takes a break in every one of the 9 clock hours (90 minutes off).',
         'B': '£4,600 takes 8 breaks (80 minutes off). Only 7 full hours of signing fit in the day.',
         'D': '£4,800 needs 8 full hours of signing, plus 7 breaks: 9 hours 10 minutes, longer than the day.',
         'E': '£5,400 forgets the breaks completely: 540 × 10.'},
    fast='70-minute cycles: 540 = 7 × 70 + 50. Signing = 420 + 50 = 470 min → £4,700.',
))
