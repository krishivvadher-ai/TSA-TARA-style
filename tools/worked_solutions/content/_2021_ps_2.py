import math
from wslib import *

Y = 2021
Q = []


def _pie(cx, cy, r, slices, k='ink', label_r=0.6, size=15):
    """slices: list of (degrees, fill, [label lines]) going clockwise from 12 o'clock."""
    parts, lab, a0 = [], [], -90.0
    for deg, f, lines in slices:
        a1 = a0 + deg
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        big = 1 if deg > 180 else 0
        parts.append(path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z', k=k, fill=f, sw=1.8))
        am = math.radians((a0 + a1) / 2)
        lx, ly = cx + r * label_r * math.cos(am), cy + r * label_r * math.sin(am)
        for i, t in enumerate(lines):
            lab.append(text(lx, ly + 5 + (i - (len(lines) - 1) / 2) * (size + 3), t, k='ink', size=size))
        a0 = a1
    return parts, lab


# ---------------------------------------------------------------- 9 (Q19)
def _zoo():
    parts, lab = [], []
    xs = [60, 122, 184, 246, 308, 400, 492]
    for row, (y, martha_age, martha_type, martha_cost, total, title) in enumerate(
            ((134, '15', 'C', '$11', '$81', 'the day before: Martha is still 15'),
             (300, '16', 'A', '$15', '$85', 'on her birthday: Martha is 16'))):
        who = [('Mum', 'A'), ('Dad', 'A'), ('14', 'C'), ('12', 'C'), ('9', 'C'), (f'Martha {martha_age}', martha_type), ('Gran 62', 'S')]
        for x, (name, t) in zip(xs, who):
            col = {'A': 'pen', 'C': 'green', 'S': 'violet'}[t]
            lab.append(stick_person(x, y, k=col, s=1.1))
            lab.append(text(x, y + 20, name, k='ink', size=14))
            lab.append(text(x, y - 48, {'A': 'adult', 'C': 'child', 'S': 'senior'}[t], k=col, size=14))
        parts.append(rect(30, y - 68, 308, 98, k='green', sw=2.2, rx=12))
        lab.append(text(184, y - 76, 'Family of 5 (2 adults + 3 children) = $57', k='green', size=15))
        lab.append(text(400, y - 76, martha_cost, k='red', size=18, font='scrawl'))
        lab.append(text(492, y - 76, '$13', k='red', size=18, font='scrawl'))
        lab.append(text(596, y - 18, '= ' + total, k='green' if row == 0 else 'red', size=28, font='scrawl'))
        lab.append(text(18, y - 104, title, k='ink', size=18, anchor='start', font='scrawl'))
    parts.append(circle(596, 106, 42, k='green', sw=2.4))
    return svg(660, 330, rough(*parts) + ''.join(lab),
               'Two rows of the seven family members: the day before, Martha is a child and the tickets cost 81 dollars; on her birthday she is an adult and they cost 85 dollars')

Q.append(dict(
    n=9, orig=19, answer='B', topic='Tables & best deal',
    question=f"""<p>Martha is hoping that her parents will agree to a family visit to Rockworld Zoo as a treat for her
{hl('16<sup>th</sup> birthday', 'p', 1)}. This would include Martha, her mum and dad, her {hl('brothers aged 14, 12 and 9', 'g', 2)}
years old and her {hl('grandmother, who is 62', 'g', 2)}.</p>
<p>They have looked at the price tariff for tickets and have decided that they would want to {hl('book online the day before', 'y', 3)} the proposed visit and that they could go {hl("either on Martha's birthday or on the day before it", 'p', 4)}.</p>
<p>The table shows the possible ticket prices.</p>
{table([['Adult (16–59 years)', '$17.00', '$15.00', '$14.00'],
        ['Senior Citizen (60+)', '$15.00', '$13.00', '$12.00'],
        ['Child (3–15 years)', '$13.00', '$11.00', '$10.00'],
        ['Family of 4*', '$54.00', '$49.00', '$46.00'],
        ['Family of 5**', '$63.00', hl('$57.00', 'g'), '$54.00']],
       head=['<i>Type of ticket</i>', '<i>At the gate on the day</i>', hl('<i>Booked online 1 day in advance</i>', 'y'), '<i>Booked online 7 days in advance</i>'])}
<p>* Family of 4 can be 2 adults and 2 children or 1 adult and 3 children<br>
** {hl('Family of 5 can be 2 adults and 3 children or 1 adult and 4 children', 'y', 5)}</p>
<p class="stem">What would be the {hl('smallest amount', 'b', 6)} that the family could pay for their tickets?</p>""",
    options={'A': '$76', 'B': '$81', 'C': '$84', 'D': '$87', 'E': '$91'},
    notes=[(1, 'p', 'Turning 16 makes Martha an <b>adult</b> (16–59). The day before, she is 15: still a <b>child</b>.'),
           (2, 'g', 'Brothers are children (3–15). Gran is 62: a senior, not an adult.'),
           (3, 'y', 'Only the “1 day in advance” column counts. Cover the other two columns.'),
           (4, 'p', 'Two possible days, and Martha’s age is different on each. Price both.'),
           (5, 'y', 'Family tickets only cover adults and children, never seniors.'),
           (6, 'b', 'Find the cheapest mix of tickets on the cheaper day.')],
    steps=[
        f"""<p>Sort the 7 people for each day:</p>
<ul><li>day before: Mum, Dad = adults; Martha (15), 14, 12, 9 = <b>4 children</b>; Gran = senior</li>
<li>birthday: Mum, Dad, Martha (16) = <b>3 adults</b>; 14, 12, 9 = 3 children; Gran = senior</li></ul>""",
        f"""<p>Price each day using the “1 day in advance” column:</p>
{calc('day before: Family of 5 $57 + 1 child $11 + Gran $13 = <b>$81</b>',
      'birthday: Family of 5 $57 + 1 adult $15 + Gran $13 = <b>$85</b>')}
{_zoo()}""",
        f"""<p>Check the other mixes for the day before, just in case:</p>
{calc('Family of 4 (2 adults + 2 children) $49 + 2 children $22 + Gran $13 = $84',
      'all single tickets: 2 × $15 + 4 × $11 + $13 = $87',
      f'cheapest = {boxed("$81")} (go the day before)')}
{note('Being a child for one more day saves $4: a child ticket is $11, an adult ticket $15.', 'tip')}""",
    ],
    answer_text='$81: go the day before the birthday, Family of 5 + one child + Gran.',
    why={'A': '$76 uses the “7 days in advance” prices (54 + 10 + 12). They are only booking 1 day ahead.',
         'C': '$84 uses a Family of 4 ticket and pays for two more children separately (49 + 22 + 13).',
         'D': '$87 buys every ticket separately on the day before (30 + 44 + 13), with no family ticket.',
         'E': '$91 pays gate prices (63 + 13 + 15), or buys single tickets on the birthday (45 + 33 + 13).'},
    fast='Day before, Martha is still a child: Family of 5 ($57) + child ($11) + senior ($13) = $81.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _spend():
    rows = [('furniture', 48, 18, '48 ÷ 18 ≈ 2.7'), ('clothes', 120, 90, '120 ÷ 90 ≈ 1.3'),
            ('stationery', 72, 72, '72 ÷ 72 = 1'), ('food', 120, 180, '120 ÷ 180 ≈ 0.7')]
    s, x0 = 1.6, 120
    parts, lab = [], []
    for i, (name, sale, cust, ratio) in enumerate(rows):
        y = 50 + i * 66
        parts.append(rect(x0, y, sale * s, 20, k='ink', fill='b', sw=1.5))
        parts.append(rect(x0, y + 24, cust * s, 20, k='ink', fill='o', sw=1.5))
        lab.append(text(x0 + sale * s + 6, y + 16, f'{sale}°', k='pen', size=14, anchor='start'))
        lab.append(text(x0 + cust * s + 6, y + 40, f'{cust}°', k='orange', size=14, anchor='start'))
        lab.append(text(x0 - 10, y + 29, name, k='ink', size=17, anchor='end'))
        lab.append(text(650, y + 29, ratio, k='red', size=18, anchor='end', font='scrawl'))
    parts += [rect(x0, 16, 16, 12, k='ink', fill='b', sw=1.2), rect(x0 + 170, 16, 16, 12, k='ink', fill='o', sw=1.2)]
    lab += [text(x0 + 22, 27, 'sales slice', k='pen', size=15, anchor='start'),
            text(x0 + 192, 27, 'customers slice', k='orange', size=15, anchor='start'),
            text(650, 27, 'spend per customer', k='red', size=15, anchor='end'),
            text(380, 322, 'biggest ratio first: furniture, clothes, stationery, food', k='green', size=18, font='scrawl')]
    return svg(660, 336, rough(*parts) + ''.join(lab),
               'Paired bars of each department’s sales and customer slices; ratios furniture 2.7, clothes 1.3, stationery 1, food 0.7')

Q.append(dict(
    n=10, orig=20, answer='E', topic='Pie charts & ratios',
    question=f"""<p>The sales for the four departments of a store are shown in the two pie charts below.</p>
{fig(Y, 'ps_q10_pies', 'Two pie charts. Total sales: food a third, clothes a third, stationery and furniture share the rest. Number of customers: food half, clothes a quarter, stationery most of the rest, furniture a thin slice.', 460)}
<p class="stem">Which one of the following lists the departments in order, {hl('from highest', 'y', 1)} {hl('average amount spent per customer', 'b', 2)} to lowest?</p>""",
    options={'A': 'clothes, furniture, stationery, food', 'B': 'food, clothes, stationery, furniture',
             'C': 'food, stationery, clothes, furniture', 'D': 'food, stationery, furniture, clothes',
             'E': 'furniture, clothes, stationery, food'},
    notes=[(1, 'y', 'Biggest spenders first.'),
           (2, 'b', 'Average spend = total sales ÷ number of customers. Compare each department’s two slices.')],
    steps=[
        f"""<p>Both pies are shares of the same store, so for each department:</p>
{calc(f'spend per customer ∝ {frac("sales slice", "customers slice")}')}
<p>Big sales slice + small customer slice = big spenders.</p>""",
        f"""<p>Read the angles off the pies (use the clock: each hour = 30°):</p>
{calc('sales: food 120°, clothes 120°, stationery 72°, furniture 48°',
      'customers: food 180°, clothes 90°, stationery 72°, furniture 18°')}
{note('Clothes in the sales pie runs from 12 to 4 o’clock = 120°. In the customers pie it runs 12 to 3 = 90°. Food is exactly half the customers pie.', 'tip')}""",
        f"""<p>Divide sales by customers:</p>{_spend()}
{calc(f'furniture 2.7 &gt; clothes 1.3 &gt; stationery 1 &gt; food 0.7 {ar()} {boxed("E")}')}""",
    ],
    answer_text='Furniture, clothes, stationery, food.',
    why={'A': 'A puts clothes above furniture. But furniture has only a thin sliver of customers for a much bigger sales slice, so each furniture customer spends the most.',
         'B': 'B is just the order of total sales (and of customer numbers). It never divides one by the other.',
         'C': 'C divides the wrong way (customers ÷ sales), which turns the order upside down.',
         'D': 'D puts food first, but food has half the customers and only a third of the sales: the lowest spend each.'},
    fast='Sales slice ÷ customer slice: furniture 48/18, clothes 120/90, stationery 72/72, food 120/180. E.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _letters():
    counts = [('A', 4), ('S', 3), ('R', 3), ('E', 3), ('T', 2), ('W', 2), ('H', 1), ('F', 1), ('O', 1), ('C', 1), ('K', 1), ('N', 1)]
    u, base, x0, bw = 36, 196, 70, 44
    parts, lab = [], []
    for i, (ch, n) in enumerate(counts):
        x = x0 + i * bw
        for j in range(n):
            f = 'p' if j == 3 else 'b'
            parts.append(rect(x + 4, base - (j + 1) * u, bw - 8, u - 4, k='ink', fill=f, sw=1.5, rx=3))
            lab.append(text(x + bw / 2, base - j * u - 12, ch, k='ink', size=18, font='print'))
        lab.append(text(x + bw / 2, base + 22, n, k='muted', size=15))
    parts.append(line(x0 - 10, base - 3 * u - 2, x0 + 12 * bw + 6, base - 3 * u - 2, k='red', w=2.4, dash=True))
    lab += [text(x0 + 12 * bw + 4, base - 3 * u - 10, '3 sets owned', k='red', size=17, anchor='end', font='scrawl'),
            text(x0 + bw + 30, base - 4 * u + 16, '← the 4th A needs 1 more set', k='red', size=18, anchor='start', font='scrawl'),
            text(x0 + 6 * bw, base + 44, 'capital letters needed for STAR WARS THE FORCE AWAKENS', k='ink', size=15)]
    return svg(660, 256, rough(*parts) + ''.join(lab),
               'Stacks of capital letters needed: A needs 4, S, R and E need 3; the line at 3 sets shows only A goes over')

Q.append(dict(
    n=11, orig=24, answer='B', topic='Counting',
    question=f"""<p>A cinema uses magnetic letters to write the title of the most popular film that it is screening on
its advertisement board. A set of magnetic letters includes the letters of the English alphabet in
{hl('both upper and lower cases', 'y', 1)}, i.e. 26 capital letters and 26 small letters. The cinema has {hl('just enough sets', 'g', 2)} to be able to write the following title:</p>
<p><b>STAR WARS The Force Awakens</b></p>
<p>It is now considering putting this title up {hl('all in capital letters', 'p', 3)}:</p>
<p><b>STAR WARS THE FORCE AWAKENS</b></p>
<p class="stem">What is the {hl('minimum number of extra sets', 'b', 4)} of magnetic letters that the cinema needs to buy?</p>""",
    options={'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4'},
    notes=[(1, 'y', 'One set = one of each capital and one of each small letter. So a set gives only <b>one</b> capital A.'),
           (2, 'g', 'They own exactly the number of sets the first title needs. Work that out first.'),
           (3, 'p', 'Now every letter is a capital, so the small letters they own are no use.'),
           (4, 'b', 'Sets needed now − sets owned.')],
    steps=[
        f"""<p>How many sets do they own? Count the most-used letter in the first title (capitals and small letters separately):</p>
{calc('capitals: <b>A</b> in STAR, WARS, Awakens = 3', 'small letters: <b>e</b> in The, Force, Awakens = 3',
      f'every other letter is used 2 times or fewer {ar()} they own <b>3 sets</b>')}""",
        f"""<p>Now count capitals in STAR WARS THE FORCE AWAKENS:</p>{_letters()}
{calc('A: STAR, WARS, AWAKENS (twice) = <b>4</b>', 'S, R and E: 3 each', f'need 4 sets, own 3 {ar()} buy {boxed("1")}')}
{note('A small e can’t stand in for a capital E, and a set holds only one capital A. So only the count of capitals matters now.', 'trap')}""",
    ],
    answer_text='1 extra set: the all-capitals title needs 4 capital As, and they own 3 sets.',
    why={'A': '0 assumes the 3 sets cover the new title, but AWAKENS in capitals adds a 4th capital A.',
         'C': '2 would only be right if they owned 2 sets. The first title needs 3 capital As (and 3 small es), so they own 3.',
         'D': '3 assumes they own just 1 set, so 4 − 1 = 3.',
         'E': '4 is the number of sets needed in total. They already have 3.'},
    fast='First title: 3 capital As → 3 sets owned. All capitals: 4 As → 4 sets. Buy 1.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _dough():
    parts, lab = [], []
    # dough to loaf
    for i, (d, l) in enumerate(((300, 240), (500, 400))):
        y = 58 + i * 70
        parts.append(path(f'M40 {y + 20} q20 -34 60 -26 q34 6 30 30 q-6 16 -44 16 q-40 0 -46 -20', k='orange', fill='o', sw=2))
        lab.append(text(86, y + 22, f'{d} g', k='ink', size=16))
        parts.append(arrow(150, y + 12, 230, y + 12, k='red', bend=-0.15))
        lab.append(text(190, y - 8, '−20%', k='red', size=16))
        parts.append(rect(250, y - 6, 76, 34, k='ink', fill='y', sw=2, rx=14))
        lab.append(text(288, y + 17, f'{l} g', k='ink', size=16))
    lab += [text(85, 30, 'dough', k='orange', size=17, font='scrawl'), text(288, 30, 'loaf (80%)', k='ink', size=17, font='scrawl')]
    lab += [text(350, 75, '× 40 small = 12 kg', k='pen', size=17, anchor='start'),
            text(350, 145, '× 50 large = 25 kg', k='pen', size=17, anchor='start')]
    # boxes
    s, x0, y = 14.5, 40, 214
    xx = x0
    for kg in (15, 15, 5, 5):
        parts.append(rect(xx, y, kg * s, 44, k='ink', fill='paper', sw=2))
        lab.append(text(xx + kg * s / 2, y + 66, f'{kg} kg box', k='muted', size=14))
        xx += kg * s
    parts.append(rect(x0 + 2, y + 6, 37 * s - 4, 32, k='green', fill='g', sw=1.4))
    parts.append(rect(x0 + 37 * s, y + 6, 3 * s - 2, 32, k='red', fill='p', sw=1.4))
    lab += [text(x0 + 18.5 * s, y + 27, 'used 37 kg', k='ink', size=17),
            text(x0 + 38.5 * s, y - 8, 'waste 3 kg', k='red', size=17, font='scrawl'),
            text(x0, y - 14, 'smallest buy that covers 37 kg: 15 + 15 + 5 + 5 = 40 kg', k='ink', size=16, anchor='start')]
    return svg(660, 300, rough(*parts) + ''.join(lab),
               'Dough to loaf: 300 g makes a 240 g loaf, 500 g makes a 400 g loaf; then 40 kg of boxes with 37 kg used and 3 kg wasted')

Q.append(dict(
    n=12, orig=25, answer='C', topic='Percentages & proportion',
    question=f"""<p>I run a bakery and sell two sizes of loaf. {hl('Small loaves (weighing 240 g)', 'g', 1)} sell for 80p, and {hl('large loaves (weighing 400 g)', 'g', 1)} sell for £1.20.</p>
<p>I buy dough, ready-made, at the start of each day. {hl('Small boxes (5 kg of dough)', 'g', 2)} cost me £10.00
each, and {hl('large boxes (15 kg of dough)', 'g', 2)} cost me £20.00 each.</p>
<p>{hl('The baking process causes each loaf to lose 20% of the weight of the unbaked dough', 'p', 3)}.</p>
<p>I expect to sell {hl('40 small loaves and 50 large loaves', 'g', 4)} each day. I buy enough dough to be able to
make these, and any unused dough at the end of the day has to be thrown away.</p>
<p class="stem">Assuming that I {hl('do not buy any more dough than necessary', 'y', 5)}, what {hl('proportion of the dough that I buy', 'b', 6)} each day do I have to throw away?</p>""",
    options={'A': '5.2%', 'B': '6.3%', 'C': '7.5%', 'D': '17.8%', 'E': '34.8%'},
    notes=[(1, 'g', 'These are <b>baked</b> weights. The dough must weigh more.'),
           (2, 'g', 'Dough only comes in 5 kg and 15 kg lumps. The prices don’t matter here.'),
           (3, 'p', '20% <b>of the dough</b> is lost, so the loaf is 80% of the dough. Divide by 0.8; don’t add 20%.'),
           (4, 'g', '40 small and 50 large every day.'),
           (5, 'y', 'Buy the smallest amount of boxes that covers what you need.'),
           (6, 'b', 'Waste ÷ dough <b>bought</b> (not ÷ dough used).')],
    steps=[
        f"""<p>Work back from loaf to dough. The loaf is 80% of the dough:</p>
{calc('small: 240 ÷ 0.8 = <b>300 g</b> of dough', 'large: 400 ÷ 0.8 = <b>500 g</b> of dough')}
{note('Adding 20% to the loaf (240 + 48 = 288 g) is wrong: the 20% is of the dough, not of the loaf. Check: 20% of 300 = 60, and 300 − 60 = 240.', 'trap')}""",
        f"""<p>Dough needed each day, and the smallest buy that covers it:</p>{_dough()}
{calc('12 kg + 25 kg = <b>37 kg</b> needed', '35 kg is too little; 40 kg is the least you can buy (15 + 15 + 5 + 5)', '40 − 37 = <b>3 kg</b> thrown away')}""",
        f"""{calc(f'{frac(3, 40)} = {frac(7.5, 100)} = {boxed("7.5%")}')}
{note('Buying “no more than necessary” means the waste is always less than one 5 kg box, so under 5 ÷ 40 = 12.5%. That rules out D and E at once.', 'tip')}""",
    ],
    answer_text='7.5%: 37 kg of dough needed, 40 kg bought, 3 kg thrown away.',
    why={'A': '5.2% would mean only about 2 kg thrown away from 40 kg. The waste is exactly 40 − 37 = 3 kg.',
         'B': '6.3% would mean about 2.5 kg thrown away from 40 kg. Again, the real waste is 3 kg.',
         'D': '17.8% buys 45 kg (three 15 kg boxes, which happen to cost the same £60): 8 ÷ 45. But 40 kg is enough.',
         'E': '34.8% would mean about 14 kg thrown away, more than a whole small box. That can’t happen if you buy no more than necessary.'},
    fast='Dough = loaf ÷ 0.8: 300 g and 500 g. 40 × 0.3 + 50 × 0.5 = 37 kg. Buy 40 kg. 3 ÷ 40 = 7.5%.',
))


# ---------------------------------------------------------------- 13 (Q26)
DIFFS = [('Angola', 6), ('Botswana', 10), ('Malawi', 51), ('Mozambique', 40), ('Namibia', 33), ('Tanzania', 33),
         ('Zambia', 40), ('Zimbabwe', 27)]


def _diff_bars():
    u, base, x0, gap = 3.0, 236, 70, 72
    parts, lab = [], []
    parts.append(line(x0 - 20, base, x0 + 8 * gap, base, k='ink', w=1.8))
    for i, (name, d) in enumerate(DIFFS):
        x = x0 + i * gap
        parts.append(rect(x, base - d * u, 30, d * u, k='ink', fill='b', sw=1.6))
        if d > 12:
            lab.append(text(x + 15, base - 10, d, k='ink', size=16))
        else:
            lab.append(text(x + 15, base - d * u - 6, d, k='ink', size=16))
        lab.append(text(x + 15, base + 20 + (i % 2) * 18, name, k='muted', size=14))
    for i in (4, 5):
        x = x0 + i * gap
        parts.append(line(x - 6, base - 28 * u, x + 36, base - 28 * u, k='orange', w=2.6))
    for i in (3, 6):
        x = x0 + i * gap
        parts.append(line(x - 6, base - 46 * u, x + 36, base - 46 * u, k='violet', w=2.6))
    parts += [arrow(392, 110, x0 + 4 * gap + 15, base - 28 * u - 4, k='orange', bend=0.1),
              arrow(428, 110, x0 + 5 * gap + 15, base - 28 * u - 4, k='orange', bend=-0.1)]
    lab += [text(x0 + 4.5 * gap + 15, base - 33 * u - 34, 'A shows 28 here', k='orange', size=16, font='scrawl'),
            text(x0 + 3 * gap + 15, base - 46 * u - 10, 'B: 46', k='violet', size=16, font='scrawl'),
            text(x0 + 6 * gap + 15, base - 46 * u - 10, 'B: 46', k='violet', size=16, font='scrawl'),
            text(x0 + 8 * gap - 10, 40, 'E matches every bar', k='green', size=19, font='scrawl', anchor='end')]
    return svg(660, 284, rough(*parts) + ''.join(lab),
               'Correct difference bars 6, 10, 51, 40, 33, 33, 40, 27; graph A has 28 for Namibia and Tanzania and graph B has 46 for Mozambique and Zambia')

Q.append(dict(
    n=13, orig=26, answer='E', topic='Reading graphs',
    question=f"""<p>The Zambezi River Basin plays a key role in water management for the following eight
countries.</p>
<p>The table below shows the percentage of people with access to clean drinking water in each
country in 2004.</p>
<div class="tbl-wrap"><table class="ptable"><thead><tr><th></th><th colspan="2"><i>percentage with access to clean drinking water (%)</i></th></tr>
<tr><th></th><th>{hl('urban', 'y')}</th><th>{hl('rural', 'y')}</th></tr></thead><tbody>
<tr><td>Angola</td><td>40</td><td>34</td></tr><tr><td>Botswana</td><td>100</td><td>90</td></tr>
<tr><td>Malawi</td><td>95</td><td>44</td></tr><tr><td>Mozambique</td><td>81</td><td>41</td></tr>
<tr><td>Namibia</td><td>100</td><td>67</td></tr><tr><td>Tanzania</td><td>90</td><td>57</td></tr>
<tr><td>Zambia</td><td>88</td><td>48</td></tr><tr><td>Zimbabwe</td><td>100</td><td>73</td></tr></tbody></table></div>
<p class="stem">Which one of the following graphs, suitably labelled, shows the {hl('difference in the percentages', 'b', 1)} of
people with access to clean water in {hl('urban versus rural', 'y', 2)} areas in these countries?</p>
{fig(Y, 'ps_q13_graphs', 'Five bar charts A to E with eight bars each. A, B and E have scales to 60; C has a scale to 120 and D to 100.', 560)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'b', 'One bar per country: urban − rural.'),
           (2, 'y', 'Bars in the table’s order: Angola first, Zimbabwe last.')],
    steps=[
        f"""<p>Work out urban − rural for each country:</p>
{table([['6', '10', '51', '40', hl('33', 'y'), hl('33', 'y'), '40', '27']],
       head=['Angola', 'Botswana', 'Malawi', 'Mozambique', 'Namibia', 'Tanzania', 'Zambia', 'Zimbabwe'])}""",
        f"""<p>C and D go up to 100: C is just the urban numbers and D the rural numbers. Neither is a difference. Out.</p>""",
        f"""<p>A, B and E look alike, so check where they differ. Draw the true bars and compare:</p>{_diff_bars()}
{calc(f'A: Namibia and Tanzania at 28 {cross()} (should be 33)', f'B: Mozambique and Zambia at 46 {cross()} (should be 40)',
      f'E: 6, 10, 51, 40, 33, 33, 40, 27 {tick()} {ar()} {boxed("E")}')}
{note('Pick the countries where the options disagree and calculate just those. Namibia: 100 − 67 = 33 knocks out A straight away.', 'tip')}""",
    ],
    answer_text='Graph E: 6, 10, 51, 40, 33, 33, 40, 27.',
    why={'A': 'A has Namibia and Tanzania at about 28, but both differences are 33 (100 − 67 and 90 − 57).',
         'B': 'B has Mozambique and Zambia at about 46, but both are 40 (81 − 41 and 88 − 48).',
         'C': 'C plots the urban percentages themselves (up to 100), not the differences.',
         'D': 'D plots the rural percentages, not the differences.'},
    fast='Differences: 6, 10, 51, 40, 33, 33, 40, 27. Namibia and Tanzania equal at 33: only E.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _party():
    s, x0 = 5.6, 50
    parts = [rect(x0, 60, 60 * s, 46, k='ink', fill='g', sw=1.8), rect(x0 + 60 * s, 60, 20 * s, 46, k='ink', fill='y', sw=1.8),
             rect(x0 + 80 * s, 60, 20 * s, 46, k='muted', fill='none', sw=1.6)]
    lab = [text(x0 + 30 * s, 82, 'first shop: 60 people', k='ink', size=16), text(x0 + 30 * s, 100, '$120 full price', k='ink', size=15),
           text(x0 + 70 * s, 82, '20 more', k='ink', size=16), text(x0 + 70 * s, 100, '$40', k='ink', size=16),
           text(x0 + 90 * s, 84, 'not', k='muted', size=15), text(x0 + 90 * s, 100, 'coming', k='muted', size=15)]
    for p in (0, 60, 80, 100):
        lab.append(text(x0 + p * s, 128, p, k='muted', size=14))
    lab.append(text(x0 + 50 * s, 150, 'people', k='muted', size=14))
    lab += [text(x0 + 30 * s, 46, 'paid $108 = 90% of $120', k='green', size=17, font='scrawl'),
            text(x0 + 74 * s, 46, '$2 a head', k='orange', size=17, font='scrawl'),
            text(x0 + 70 * s, 186, '$40 is not more than $75', k='red', size=17, font='scrawl'),
            text(x0 + 70 * s, 208, 'so no discount today', k='red', size=17, font='scrawl')]
    parts.append(arrow(x0 + 70 * s, 168, x0 + 70 * s, 112, k='red', bend=0.1))
    return svg(640, 220, rough(*parts) + ''.join(lab),
               'Bar of 100 people: 60 already covered by 120 dollars of food, 20 more cost 40 dollars, the last 20 invited are not coming')

Q.append(dict(
    n=14, orig=30, answer='C', topic='Percentages',
    question=f"""<p>I am planning a party next weekend. I have {hl('invited 100 people', 'p', 1)}. Last week I took advantage of
an offer at my local supermarket where I was able to get {hl('10% off the total price of party food if I spent more than $75', 'y', 2)}. I {hl('paid $108', 'g', 3)} and I estimate that the food that I bought will be {hl('enough for 60 people', 'g', 3)}. I’ve now had replies to the invitations and I know that {hl('there will be 80 people', 'g', 4)} at the
party. This afternoon I will buy the remaining food that I need.</p>
<p class="stem">What is the {hl('total price of the extra food', 'b', 5)} that I need?</p>""",
    options={'A': '$32.40', 'B': '$36.00', 'C': '$40.00', 'D': '$72.00', 'E': '$80.00'},
    notes=[(1, 'p', 'Red herring: only 80 are coming.'),
           (2, 'y', 'The discount only applies to a shop of more than $75. Check this afternoon’s shop too!'),
           (3, 'g', '$108 was <b>after</b> 10% off. Undo it to get the real price of food for 60.'),
           (4, 'g', '80 − 60 = 20 more people to feed.'),
           (5, 'b', 'What this afternoon’s shop will cost.')],
    steps=[
        f"""<p>$108 is what was left after 10% off, so $108 is <b>90%</b> of the full price:</p>
{calc('90% = $108', '10% = $108 ÷ 9 = $12', '100% = $120 for 60 people')}
{note('Don’t add 10% of $108 back on (108 + 10.80 = $118.80). The 10% was taken off the full price, not off $108.', 'trap')}""",
        f"""<p>Full price per person, then the extra people:</p>
{calc('$120 ÷ 60 = <b>$2 a person</b>', '80 − 60 = 20 more people', '20 × $2 = <b>$40</b>')}""",
        f"""<p>Does this afternoon’s shop get 10% off?</p>{_party()}
{calc(f'$40 is under $75 {ar()} no discount {ar()} {boxed("$40.00")}')}""",
    ],
    answer_text='$40: 20 more people at the full price of $2 each, with no discount because $40 is under $75.',
    why={'A': '$32.40 takes 10% off a $36 shop. But $40 is under $75, so there’s no discount this afternoon.',
         'B': '$36 uses the discounted price per person (108 ÷ 60 = $1.80) for the 20 extra people. Today’s shop is too small for the discount.',
         'D': '$72 buys for 40 more people (all 100 invited) at the discounted $1.80. Only 80 are coming.',
         'E': '$80 buys for 40 more people (100 − 60). Only 80 are coming.'},
    fast='$108 ÷ 0.9 = $120 for 60, so $2 a head. 20 more people = $40, under $75 so no discount.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _holiday():
    w, x0 = 20, 50
    parts, lab = [], []
    days = [('May', d) for d in range(14, 32)] + [('June', d) for d in range(1, 11)]
    for i, (m, d) in enumerate(days):
        stay = 7 <= i < 21
        parts.append(rect(x0 + i * w, 60, w, 34, k='ink', fill='y' if stay else 'paper', sw=1.2))
        lab.append(text(x0 + i * w + w / 2, 82, d, k='ink' if stay else 'muted', size=11, font='print'))
    parts.append(rect(x0 - 3, 54, 28 * w + 6, 46, k='green', sw=2.4, rx=6))
    lab += [text(x0 + 14 * w, 40, 'price band May 14 – June 10: £1050 each for 14 nights', k='green', size=16),
            text(x0 + 7 * w, 124, 'arrive May 21', k='red', size=16, font='scrawl'),
            text(x0 + 21 * w, 124, 'leave June 4', k='red', size=16, font='scrawl'),
            text(x0 + 14 * w, 148, '14 nights, all inside the band', k='ink', size=16)]
    parts.append(line(x0 + 7 * w, 100, x0 + 7 * w, 110, k='red', w=2.2))
    parts.append(line(x0 + 21 * w, 100, x0 + 21 * w, 110, k='red', w=2.2))
    # cost bar
    s, y = 0.15, 186
    xx = x0
    for amt, f, name in ((3150, 'b', '3 × £1050 = £3150'), (154, 'o', ''), (84, 'v', '')):
        parts.append(rect(xx, y, amt * s, 40, k='ink', fill=f, sw=1.6))
        if name:
            lab.append(text(xx + amt * s / 2, y + 26, name, k='ink', size=16))
        xx += amt * s
    lab += [text(x0 + 3150 * s + 12, y + 62, '+ £154 single', k='orange', size=15),
            text(xx + 4, y + 26, '+ £84', k='violet', size=15, anchor='start'),
            text(x0, y + 62, '= £3388, then 10% off = £3049.20', k='red', size=18, font='scrawl', anchor='start')]
    return svg(660, 262, rough(*parts) + ''.join(lab),
               'Calendar strip May 14 to June 10 with the stay May 21 to June 4 inside it, and a cost bar of 3150 plus 154 plus 84')

Q.append(dict(
    n=15, orig=31, answer='D', topic='Tables & percentages',
    question=f"""<p>Aliyah is planning a {hl('2 week holiday', 'g', 1)} in Spain with her friend Kyra and her husband. They have
chosen their hotel and are calculating what the total cost will be {hl('for the 3 of them', 'g', 1)}. They have
decided on a {hl('departure date of May 21st', 'y', 2)} and will be ready to make the booking {hl('in early January', 'y', 3)}.</p>
<p>The following table shows dates and prices.</p>
<p>All prices shown are {hl('£s per person', 'g', 1)}.</p>
{table([['7 nights', '£580', '£600', '£650', '£670', '£700', '£700', '£700'],
        [hl('14 nights', 'y'), '£900', '£900', '£970', '£1000', hl('£1050', 'y'), '£1050', '–'],
        ['21 nights', '£1200', '£1230', '£1300', '£1350', '£1400', '–', '–']],
       head=['<i>duration</i>', '<i>Mar 29− Apr 22</i>', '<i>Apr 23−29</i>', '<i>Apr 30− May 6</i>', '<i>May 7−13</i>',
             hl('<i>May 14− June 10</i>', 'y'), '<i>June 11−17</i>', '<i>June 18−24</i>'])}
<p>Single room supplement: £11 on all dates.</p>
<p>Upgrade to a sea view room supplement: £3.</p>
<p>{hl('Supplement prices are per person, per night', 'p', 4)}.</p>
<p>Early booking discount: if booked by 31st January is {hl('5% up to a total of £2500, and 10% on any total above £2500', 'p', 5)}.</p>
<p>{hl('Aliyah needs a single room', 'g', 6)}. {hl('Kyra wants to upgrade the room for her and her husband', 'g', 6)} so that it
has a sea view.</p>
<p class="stem">What will be the {hl('total cost of the hotel booking for the 3 friends', 'b', 7)}?</p>""",
    options={'A': '£2181.20', 'B': '£2910.60', 'C': '£2973.60', 'D': '£3049.20', 'E': '£3218.60'},
    notes=[(1, 'g', '14 nights, 3 people, prices per person.'),
           (2, 'y', 'May 21st falls in the “May 14 − June 10” column.'),
           (3, 'y', 'Booked before 31st January, so the early booking discount applies.'),
           (4, 'p', 'Supplements are per person <b>and</b> per night: × people × 14.'),
           (5, 'p', 'Their total is above £2500, so it gets the 10% rate.'),
           (6, 'g', 'Single room: 1 person. Sea view: 2 people (Kyra and her husband).'),
           (7, 'b', 'Basic price + supplements, then the discount.')],
    steps=[
        f"""<p>Find the right price. They leave May 21st for 14 nights, all inside the May 14 – June 10 band:</p>
{_holiday()}
{calc('3 people × £1050 = <b>£3150</b>')}""",
        f"""<p>Add the supplements (per person, per night, for 14 nights):</p>
{calc('Aliyah single room: 14 × £11 = £154', 'Kyra and husband sea view: 2 × 14 × £3 = £84',
      '3150 + 154 + 84 = <b>£3388</b>')}""",
        f"""<p>Booked in January and the total is above £2500, so take off 10%:</p>
{calc('10% of 3388 = 338.80', f'3388 − 338.80 = {boxed("£3049.20")}')}
{note('If you read the discount as “5% on the first £2500, 10% on the rest” you get £3174.20, which isn’t an option. So the rule means a total above £2500 gets 10% off all of it.', 'check')}""",
    ],
    answer_text='£3049.20: £3150 + £154 + £84 = £3388, less 10%.',
    why={'A': '£2181.20 prices only 2 people (2 × 1050 + 154 + 42 = 2296, then 5% off). There are 3 friends.',
         'B': '£2910.60 forgets Aliyah’s single room supplement (3234 less 10%).',
         'C': '£2973.60 forgets the sea view supplement (3304 less 10%).',
         'E': '£3218.60 takes only 5% off. The total is above £2500, so it gets 10%.'},
    fast='3 × 1050 + 14 × 11 + 2 × 14 × 3 = 3388. Above £2500, so 10% off: 3049.20.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _choc_pies():
    p1, l1 = _pie(165, 150, 108, [(138, 'paper', ['square', '138° = 23']), (138, 'b', ['circle', '138° = 23']),
                                   (84, 'y', ['triangle', '84° = 14'])])
    p2, l2 = _pie(495, 150, 108, [(120, 'o', ['dark', '120° = 20']), (180, 'b', ['milk', '180° = 30']),
                                   (60, 'paper', ['white', '60° = 10'])])
    lab = [text(165, 284, 'shapes', k='ink', size=18, font='scrawl'), text(495, 284, 'types', k='ink', size=18, font='scrawl'),
           text(330, 26, 'each 6° of pie = 1 chocolate', k='red', size=18, font='scrawl')]
    return svg(660, 296, rough(*p1, *p2) + ''.join(l1 + l2 + lab),
               'The two pies redrawn: square 138 degrees is 23, circle 138 is 23, triangle 84 is 14; dark 120 is 20, milk 180 is 30, white 60 is 10')


def _choc_table(letter, rows):
    body = [[name] + [str(v) for v in r] for name, r in zip(('circle', 'square', 'triangle'), rows)]
    return table(body, head=[f'<b>{letter}</b>', 'dark', 'milk', 'white'])


CHOC = {'A': [(8, 10, 2), (8, 14, 4), (4, 6, 4)], 'B': [(5, 10, 5), (8, 10, 2), (8, 6, 6)],
        'C': [(5, 11, 6), (5, 11, 6), (5, 8, 3)], 'D': [(8, 8, 4), (6, 12, 2), (5, 10, 5)],
        'E': [(9, 10, 4), (9, 10, 4), (2, 10, 2)]}


def _choc_check():
    rows = []
    for k, r in CHOC.items():
        cols = [sum(x[i] for x in r) for i in range(3)]
        shapes = [sum(x) for x in r]
        ok_t = cols == [20, 30, 10]
        ok_s = shapes == [23, 23, 14]
        tcell = ' / '.join(map(str, cols)) + ' ' + (tick() if ok_t else cross())
        scell = (' / '.join(map(str, shapes)) + ' ' + (tick() if ok_s else cross())) if ok_t else '<span style="color:var(--muted)">no need</span>'
        rows.append([f'<b>{k}</b>', tcell, scell])
    return table(rows, head=['', 'dark / milk / white (need 20 / 30 / 10)', 'circle / square / triangle (need 23 / 23 / 14)'])

Q.append(dict(
    n=16, orig=32, answer='E', topic='Pie charts & tables',
    question=f"""<p>{hl('A tin of 60 chocolates', 'g', 1)} contains dark chocolates, milk chocolates and white chocolates. Each of
these types of chocolate is present in three different shapes – square, circle and triangle.</p>
<p>The distributions of the chocolates in the tin, {hl('by type and shape', 'y', 2)}, are shown in the pie charts:</p>
{fig(Y, 'ps_q16_pies', 'Two pie charts. Shapes: square and circle large and about equal, triangle smaller. Types: dark a third, milk a half, white the rest.', 460)}
<p class="stem">Which one of the following tables, detailing the contents of the tin, is {hl('consistent with the pie charts', 'b', 3)}?</p>
<div style="display:flex;flex-wrap:wrap;gap:0 26px">{''.join(_choc_table(k, v) for k, v in CHOC.items())}</div>""",
    options={'A': 'table A', 'B': 'table B', 'C': 'table C', 'D': 'table D', 'E': 'table E'},
    notes=[(1, 'g', '60 chocolates: 360° ÷ 60 = 6° per chocolate.'),
           (2, 'y', 'Type totals are the <b>column</b> totals; shape totals are the <b>row</b> totals.'),
           (3, 'b', 'Both pies must match: check columns first, then rows.')],
    steps=[
        f"""<p>Turn each pie into numbers out of 60:</p>{_choc_pies()}
{calc('types: dark ⅓ = 20, milk ½ = 30, white = 10', 'shapes: square = circle (same size slices), triangle smaller')}
{note('Easy fractions first: the dark slice runs 12 to 4 o’clock (a third) and the milk/white line makes milk exactly half.', 'tip')}""",
        f"""<p>Column totals for every table, then row totals for any that survive:</p>{_choc_check()}""",
        f"""<p>Only E has 20 / 30 / 10 <b>and</b> circle = square:</p>
{calc(f'E: circles 9 + 10 + 4 = 23, squares 23, triangles 2 + 10 + 2 = 14 {tick()} {ar()} {boxed("E")}')}""",
    ],
    answer_text='Table E: dark 20, milk 30, white 10 and circles 23, squares 23, triangles 14.',
    why={'A': 'A has the right types (20, 30, 10) but 26 squares and only 20 circles. In the pie, circle and square are the same size.',
         'B': 'B has milk 26 and white 13. Milk should be exactly half the tin (30).',
         'C': 'C has dark 15 and white 15. Dark should be twice white (20 and 10).',
         'D': 'D has dark 19 and white 11 instead of 20 and 10.'},
    fast='Columns must be 20 / 30 / 10: only A and E. Rows: circle must equal square: only E.',
))
