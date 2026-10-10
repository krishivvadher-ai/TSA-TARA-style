from wslib import *

Y = 2011
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _pools():
    X = lambda v: 50 + (v - 6) * 85
    parts = [line(X(5.8), 96, X(12.3), 96, k='ink', head=True)]
    lab = []
    for i in range(13):
        v = 6 + i / 2
        parts.append(line(X(v), 90, X(v), 102, k='ink', w=1.4))
        lab.append(text(X(v), 122, f'{v:g}', k='muted', size=14))
    groups = [((6, 6.5, 7, 7.5), 'muted', '1 draw'), ((8, 8.5, 9), 'pen', '2 draws'),
              ((10, 10.5), 'green', '3 draws'), ((12,), 'orange', '4 draws')]
    for vals, col, name in groups:
        for v in vals:
            parts.append(circle(X(v), 96, 8, k=col, fill='paper' if col == 'muted' else {'pen': 'b', 'green': 'g', 'orange': 'o'}[col], sw=2.4))
        lab.append(text((X(vals[0]) + X(vals[-1])) / 2, 150, name, k=col, size=17, font='scrawl'))
    for v in (9.5, 11, 11.5):
        parts.append(line(X(v) - 7, 89, X(v) + 7, 103, k='red', w=2.6))
        parts.append(line(X(v) - 7, 103, X(v) + 7, 89, k='red', w=2.6))
    for v, letter in ((8.5, 'A'), (9, 'B'), (9.5, 'C'), (10, 'D'), (10.5, 'E')):
        lab.append(text(X(v), 74, letter, k='ink', size=15, font='print', weight='700'))
    lab.append(text(X(9.5), 44, '9.5 can’t be made!', k='red', size=20, font='scrawl'))
    parts.append(arrow(X(9.5), 50, X(9.5), 62, k='red'))
    return svg(620, 165, rough(*parts) + ''.join(lab),
               'Number line of the totals that can be made: 8, 8.5, 9 with two draws, 10 and 10.5 with three draws; 9.5 is a gap')


Q.append(dict(
    n=1, orig=2, answer='C', topic='Making totals',
    question=f"""<p>To play a football pools game, participants must select {hl('four matches', 'g', 1)} from the fifty on the
coupon. Points are scored depending on the result of each match as follows:</p>
<p>{hl('If the home team wins, the participant scores 1.0 point<br>If the away team wins, the participant scores 1.5 points<br>If the match is a draw, the participant scores 3.0 points', 'y', 2)}</p>
<p class="stem">Which of the following total scores for the four matches is {hl('<b>not</b>', 'b', 3)} possible?</p>""",
    options={'A': '8.5 points', 'B': '9.0 points', 'C': '9.5 points', 'D': '10.0 points', 'E': '10.5 points'},
    notes=[(1, 'g', 'Exactly 4 results get added up. No more, no fewer.'),
           (2, 'y', 'Only three scores exist: <b>1</b>, <b>1.5</b> and <b>3</b>.'),
           (3, 'b', 'Four of the totals can be made. Hunt for the one that can’t.')],
    steps=[
        f"""<p>The options are all big (8.5 to 10.5), and the most you can get is 4 × 3 = 12. Big totals need lots of draws,
so sort by <b>how many draws</b>. Each group gives a short, complete list:</p>
{calc(f'4 draws {ar()} 12',
      f'3 draws {ar()} 9 + one more match (1 or 1.5) {ar()} <b>10</b> or <b>10.5</b>',
      f'2 draws {ar()} 6 + two more (1 + 1, 1 + 1.5 or 1.5 + 1.5) {ar()} <b>8</b>, <b>8.5</b> or <b>9</b>',
      f'1 draw {ar()} 3 + three more (3 to 4.5) {ar()} at most 7.5',
      f'0 draws {ar()} at most 4 × 1.5 = 6')}""",
        f"""<p>Put every possible total on a number line:</p>{_pools()}
{calc(f'9.5 is missing from every list {ar()} {boxed("C")}')}
{note('Why not 9.5? With 3 draws you are already at 9 and the last match adds at least 1. With 2 draws you are at 6 and the other two matches add at most 3. So you jump from 9 straight to 10.', 'check')}""",
    ],
    answer_text='9.5 points: two draws reach at most 9, three draws give at least 10.',
    why={'A': '8.5 = 3 + 3 + 1 + 1.5 (two draws, a home win and an away win).',
         'B': '9.0 = 3 + 3 + 1.5 + 1.5 (two draws and two away wins).',
         'D': '10.0 = 3 + 3 + 3 + 1 (three draws and a home win).',
         'E': '10.5 = 3 + 3 + 3 + 1.5 (three draws and an away win).'},
    fast='Three draws give 10 or 10.5; two draws give 8, 8.5 or 9. Nothing lands on 9.5.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _weights():
    X = lambda kg: 130 + kg * 42
    rows = [('Alma', 7), ('Brigit', 5), ('Cara', 6), ('Danni', 6.5), ('Evelyn', 8)]
    parts, lab = [], []
    for i, (name, kg) in enumerate(rows):
        y = 34 + i * 42
        if name == 'Alma':
            parts.append(rect(X(0), y, X(10) - X(0), 26, k='muted', sw=1.8))
            parts.append(line(X(10), y - 6, X(10), y + 32, k='red', w=2, dash=True))
            lab.append(text(X(10) + 8, y + 12, '10 kg off by week 3…', k='red', size=15, anchor='start'))
            lab.append(text(X(10) + 8, y + 30, '…then 3 kg back on', k='red', size=15, anchor='start'))
        f = 'g' if name == 'Evelyn' else 'b'
        parts.append(rect(X(0), y, X(kg) - X(0), 26, k='ink', fill=f, sw=1.8))
        lab.append(text(120, y + 19, name, k='ink', size=17, anchor='end'))
        lab.append(text(X(kg) - 8, y + 19, f'{kg:g} kg'.replace('6.5', '6½'), k='ink', size=16, anchor='end'))
    parts.append(line(X(0), 24, X(0), 248, k='ink', w=2))
    lab.append(text(X(8) + 10, 34 + 4 * 42 + 19, '← most lost', k='green', size=20, font='scrawl', anchor='start'))
    lab.append(text(X(5), 270, 'weight lost: start → after week 4', k='muted', size=16))
    return svg(660, 282, rough(*parts) + ''.join(lab),
               'Bars of weight lost after 4 weeks: Alma 7, Brigit 5, Cara 6, Danni 6 and a half, Evelyn 8; Alma had lost 10 by week 3')


Q.append(dict(
    n=2, orig=6, answer='E', topic='Reading tables',
    question=f"""<p>To encourage themselves to lose weight, Alma, Brigit, Cara, Danni and Evelyn each put
£10 into a pot. They weighed themselves when they began and again at the end of each
week. {hl('The one who had lost most weight after 4 weeks', 'b', 1)} won the £50. The following chart
shows their progress:</p>
{table([[hl('<i>Starting weight</i>', 'g', 2), '71kg', '67kg', '63½kg', '66½kg', '69kg'],
        ['<i>Weight after week 1</i>', '67kg', '68kg', '62kg', '67kg', '66kg'],
        ['<i>Weight after week 2</i>', '63½kg', '66½kg', '59kg', '62kg', '63½kg'],
        ['<i>Weight after week 3</i>', hl('61kg', 'p', 3), '66kg', '58kg', '61½kg', '62kg'],
        [hl('<i>Weight after week 4</i>', 'g'), '64kg', '62kg', '57½kg', '60kg', '61kg']],
       head=['', '<i>Alma</i>', '<i>Brigit</i>', '<i>Cara</i>', '<i>Danni</i>', '<i>Evelyn</i>'])}
<p class="stem">Who won the £50?</p>""",
    options={'A': 'Alma', 'B': 'Brigit', 'C': 'Cara', 'D': 'Danni', 'E': 'Evelyn'},
    notes=[(1, 'b', 'Compare the <b>start</b> with <b>week 4</b> only. The weeks in between don’t count.'),
           (2, 'g', 'Just two rows matter: the first and the last.'),
           (3, 'p', 'Alma was 10 kg down after week 3, but then put weight back on. Tempting trap!')],
    steps=[
        f"""<p>Weight lost = starting weight − weight after week 4:</p>
{calc('Alma: 71 − 64 = <b>7 kg</b>', 'Brigit: 67 − 62 = <b>5 kg</b>', 'Cara: 63½ − 57½ = <b>6 kg</b>',
      'Danni: 66½ − 60 = <b>6½ kg</b>', 'Evelyn: 69 − 61 = <b>8 kg</b>')}""",
        f"""{_weights()}
{calc(f'most weight lost after 4 weeks = 8 kg {ar()} {boxed("Evelyn")}')}
{note('Alma had lost the most by week 3 (10 kg), which is why A looks good. But the prize is for weight lost <b>after 4 weeks</b>, and she put 3 kg back on.', 'trap')}""",
    ],
    answer_text='Evelyn: 69 kg down to 61 kg, a loss of 8 kg.',
    why={'A': 'Alma lost 10 kg by week 3 but put 3 kg back on, so only 7 kg after 4 weeks.',
         'B': 'Brigit lost 5 kg, the least of all five.',
         'C': 'Cara is the lightest at the end, but the prize is for weight <b>lost</b>: she lost 6 kg.',
         'D': 'Danni lost 6½ kg, less than Evelyn’s 8 kg.'},
    fast='First row minus last row: 7, 5, 6, 6½, 8. Evelyn wins.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _reigns():
    bins = [('0–15', [('Richard I', 10)]),
            ('16–30', [('John', 17), ('Edward II', 20), ('Richard II', 22)]),
            ('31–45', [('Henry II', 35), ('Edward I', 35)]),
            ('46–60', [('Henry III', 56), ('Edward III', 50)])]
    fills = ['y', 'b', 'g', 'o']
    parts, lab = [], []
    base, ch, cw = 200, 38, 138
    for i, (name, kings) in enumerate(bins):
        x = 24 + i * 150
        for j, (k, yrs) in enumerate(kings):
            y = base - (j + 1) * ch
            parts.append(rect(x, y, cw, ch - 4, k='ink', fill=fills[i], sw=1.6, rx=4))
            lab.append(text(x + cw / 2, y + 23, f'{k} · {yrs}', k='ink', size=15))
        lab.append(text(x + cw / 2, base + 24, f'{name} yrs', k='ink', size=16))
        lab.append(text(x + cw / 2, base - len(kings) * ch - 12, len(kings), k='red', size=26, font='scrawl'))
    parts.append(line(14, base, 610, base, k='ink', w=2))
    lab.append(text(310, 258, 'bars 1, 3, 2, 2 (total 8 kings) = chart E', k='green', size=21, font='scrawl'))
    return svg(620, 272, rough(*parts) + ''.join(lab),
               'The eight kings sorted into four groups by length of reign: 1 in 0 to 15, 3 in 16 to 30, 2 in 31 to 45, 2 in 46 to 60')


Q.append(dict(
    n=3, orig=7, answer='E', topic='Charts & grouping',
    question=f"""<p>Below is a list of the Angevin and Plantagenet kings of England and the dates of their
reigns.</p>
{table([['Henry II', '1154 - 1189'], ['Richard I', '1189 - 1199'], ['John', '1199 - 1216'], ['Henry III', '1216 - 1272'],
        ['Edward I', '1272 - 1307'], ['Edward II', '1307 - 1327'], ['Edward III', '1327 - 1377'], ['Richard II', '1377 - 1399']],
       head=['Monarch', 'Reign'])}
<p class="stem">Which of the following bar charts represents a distribution of the {hl('lengths of the reigns', 'b', 1)} of
{hl('these kings', 'g', 2)}?</p>
{fig(Y, 'ps_q03_bars', 'Five bar charts A to E of number of kings against length of reign in groups 0-15, 16-30, 31-45 and 46-60 years', 470)}""",
    options={'A': 'chart A', 'B': 'chart B', 'C': 'chart C', 'D': 'chart D', 'E': 'chart E'},
    notes=[(1, 'b', 'Length = end year − start year. Then drop each king into his group.'),
           (2, 'g', '8 kings, so the bars must add up to <b>8</b>.')],
    steps=[
        f"""<p>Work out each reign (end − start):</p>
{calc('Henry II 1189 − 1154 = 35', 'Richard I 1199 − 1189 = 10', 'John 1216 − 1199 = 17', 'Henry III 1272 − 1216 = 56',
      'Edward I 1307 − 1272 = 35', 'Edward II 1327 − 1307 = 20', 'Edward III 1377 − 1327 = 50', 'Richard II 1399 − 1377 = 22')}""",
        f"""<p>Stack each king in his group, like building the bar chart with blocks:</p>{_reigns()}
{calc(f'0–15: 1, 16–30: 3, 31–45: 2, 46–60: 2 {ar()} {boxed("E")}')}
{note('Quick check before reading any chart: the bars must add up to 8. C adds to 7 and D adds to 9, so they are out at once.', 'tip')}""",
    ],
    answer_text='Chart E: 1, 3, 2, 2.',
    why={'A': 'A shows 1, 3, 3, 1: it has moved one of the long reigns (Henry III 56 or Edward III 50) down into 31–45.',
         'B': 'B has 2 in every group, but only Richard I reigned 15 years or less.',
         'C': 'C shows 1, 3, 1, 2, which is only 7 kings: one of the two 35-year reigns is missing.',
         'D': 'D shows 1, 3, 3, 2, which is 9 kings. There are only 8.'},
    fast='Lengths 35, 10, 17, 56, 35, 20, 50, 22. Groups: 1, 3, 2, 2. That is E.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _journey():
    O = (60, 232)
    P = [(60, 232), (150, 207), (255, 97), (350, 72), (430, 72), (500, 232)]
    parts = [line(O[0], O[1], 600, O[1], k='ink', head=True), line(O[0], O[1], O[0], 24, k='ink', head=True),
             poly(P, k='pen', sw=3.2, closed=False)]
    for (x, y) in P[1:-1]:
        parts.append(circle(x, y, 4, k='pen', fill='paper', sw=2))
    lab = [text(105, 210, '1', k='red', size=20, font='scrawl'),
           text(190, 150, '2', k='red', size=20, font='scrawl'),
           text(300, 75, '3', k='red', size=20, font='scrawl'),
           text(390, 62, '4', k='red', size=20, font='scrawl'),
           text(476, 140, '5', k='red', size=20, font='scrawl'),
           text(36, 128, 'distance from home', k='muted', size=15, rotate=-90),
           text(590, 254, 'time', k='muted', size=15, anchor='end'),
           text(60, 254, 'home = 0', k='muted', size=14, anchor='start')]
    key = ['1  village: steady, gentle slope', '2  open road: faster, so steeper', '3  hill: slower, so gentler',
           '4  stops to admire the view: flat', '5  rushes home: steep, down to 0']
    for i, s in enumerate(key):
        lab.append(text(318, 116 + i * 22, s, k='ink', size=15, anchor='start'))
    return svg(620, 266, rough(*parts) + ''.join(lab),
               'Sketch of the correct graph: gentle rise, steeper rise, gentler rise, flat, then a steep fall back to zero')


Q.append(dict(
    n=4, orig=8, answer='D', topic='Distance–time graphs',
    question=f"""<p>A man drives off from his house and travels through the village {hl('at a constant speed', 'g', 1)}. As
he leaves the village behind, {hl('his speed increases to a new constant value', 'y', 2)} which he
maintains until he reaches a steep hill which {hl('slows him down', 'y', 3)}. At the top of the hill the
driver {hl('stops for a few minutes', 'y', 4)} to admire the view. He realises that he has left his picnic
basket at home and so {hl('drives rapidly back along his route', 'y', 5)} to collect it.</p>
<p class="stem">Which one of the following graphs best represents the driver's {hl('distance from home', 'b', 6)}
throughout his journey?</p>
{fig(Y, 'ps_q04_graphs', 'Five distance-from-home against time graphs A to E', 480)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'g', 'Steady speed = straight sloping line.'),
           (2, 'y', 'Faster = <b>steeper</b>.'),
           (3, 'y', 'Slower = less steep.'),
           (4, 'y', 'Not moving = <b>flat</b> line.'),
           (5, 'y', 'Heading home: the distance falls, quickly, all the way back to 0.'),
           (6, 'b', 'He starts at home, so the graph starts at 0, and it ends at 0 when he gets back.')],
    steps=[
        f"""<p>Sketch what the graph has to look like, one stage at a time:</p>{_journey()}""",
        f"""<p>Now knock out the graphs that break a rule:</p>
<ul><li>A keeps going <b>up</b> at the end: he never comes home. {cross()}</li>
<li>C starts <b>above 0</b> with a flat bit: he would be standing still away from home. {cross()}</li>
<li>E has <b>no flat part</b>: no stop at the top of the hill. {cross()}</li>
<li>B goes gentle, then <b>even gentler</b>, then steep: he slows down after the village and speeds up on the hill. Backwards! {cross()}</li>
<li>D: gentle, steep, gentle, flat, then down to 0. {tick()}</li></ul>
{calc(f'answer = {boxed("D")}')}""",
    ],
    answer_text='Graph D: gentle, steeper, gentler, flat, then a quick return to 0.',
    why={'A': 'A never comes back down: he would still be driving away from home at the end.',
         'B': 'B gets less steep after the village and steeper on the hill: the wrong way round.',
         'C': 'C starts above 0, but he sets off from his house.',
         'E': 'E has no flat section, so there is no stop to admire the view.'},
    fast='Starts at 0, has a flat bit, ends at 0: only B and D. Speed goes up after the village, so the 2nd slope is steeper: D.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _coffee():
    def jar(x, y, h, f):
        return [rect(x, y + 10, 70, h, k='ink', fill=f, sw=2, rx=8), rect(x + 8, y, 54, 12, k='ink', fill='paper', sw=2, rx=3)]
    parts, lab = [], []
    parts += jar(40, 30, 64, 'o')
    lab += [text(75, 70, '200 g', k='ink', size=17), text(75, 128, 'Kostless', k='ink', size=16),
            text(75, 22, '£1.70', k='red', size=18, font='scrawl')]
    parts.append(arrow(130, 66, 260, 66, k='pen', bend=-0.12))
    lab += [text(195, 48, '× 5', k='pen', size=22, font='scrawl'),
            text(280, 72, '1 kg = 5 × £1.70 = £8.50', k='ink', size=19, anchor='start')]
    parts += jar(40, 160, 80, 'b')
    lab += [text(75, 210, '250 g', k='ink', size=17), text(75, 274, 'Savemore', k='ink', size=16),
            text(75, 152, '£2.50', k='red', size=18, font='scrawl')]
    parts.append(arrow(130, 206, 260, 206, k='pen', bend=-0.12))
    lab += [text(195, 188, '× 4', k='pen', size=22, font='scrawl'),
            text(280, 212, '1 kg = 4 × £2.50 = £10.00', k='ink', size=19, anchor='start')]
    parts.append(line(520, 70, 520, 206, k='red', w=2.2, tail=True, head=True))
    lab += [text(530, 132, '£1.50', k='red', size=22, font='scrawl', anchor='start'),
            text(530, 156, 'per kg', k='red', size=17, anchor='start')]
    return svg(620, 290, rough(*parts) + ''.join(lab),
               'Kostless: 200 g for 1.70, times 5 gives 8.50 per kilogram. Savemore: 250 g for 2.50, times 4 gives 10.00 per kilogram. Difference 1.50')


Q.append(dict(
    n=5, orig=12, answer='A', topic='Best buy',
    question=f"""<p>Jars of Bestcaff coffee {hl('weighing 200g are normally £2.50', 'g', 1)} at Kostless and Savemore, but
both supermarkets have a special offer this week:</p>
{table([['KOSTLESS<br>BESTCAFF<br>' + hl('80p OFF', 'y', 2), 'SAVEMORE<br>BESTCAFF<br>' + hl('25% EXTRA FREE', 'y', 3)]])}
<p class="stem">By how much {hl('per kilogram', 'b', 4)} is Kostless's offer better value for money than Savemore's?</p>""",
    options={'A': '£1.50 per kg', 'B': '£4.00 per kg', 'C': '£7.00 per kg', 'D': '£8.50 per kg', 'E': '£16.00 per kg'},
    notes=[(1, 'g', 'Normal jar: 200 g for £2.50.'),
           (2, 'y', 'Same 200 g, but 80p cheaper: £1.70.'),
           (3, 'y', 'Same £2.50, but 25% more coffee in the jar.'),
           (4, 'b', 'Compare the price of 1 kg (1000 g) at each shop.')],
    steps=[
        f"""<p>What do you actually get at each shop?</p>
{calc('Kostless: 200 g for £2.50 − £0.80 = <b>£1.70</b>',
      f'Savemore: 25% of 200 g = 50 g extra {ar()} <b>250 g</b> for £2.50')}""",
        f"""<p>Scale each jar up to 1 kg:</p>{_coffee()}
{note('Choose the multiplier that turns each jar into 1000 g: 200 × 5 and 250 × 4. Much easier than finding a price per gram.', 'tip')}""",
        f"""{calc(f'£10.00 − £8.50 = {boxed("£1.50 per kg")}')}""",
    ],
    answer_text='£1.50 per kg: £8.50 a kilo at Kostless against £10.00 a kilo at Savemore.',
    why={'B': '£4.00 is just the 80p discount scaled up to a kilogram (0.80 × 5). It ignores Savemore’s offer.',
         'C': '£7.00 isn’t the gap between the two kilo prices (£10.00 and £8.50). It would need Savemore to charge £15.50 a kilo.',
         'D': '£8.50 is Kostless’s price for a kilogram, not the difference between the shops.',
         'E': '£16.00 is far too big: it is more than either shop charges for a whole kilogram.'},
    fast='Kostless £1.70 × 5 = £8.50 per kg. Savemore 250 g for £2.50, × 4 = £10 per kg. Difference £1.50.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _eu_bar():
    X = lambda p: 40 + p * 5.4
    segs = [('France', 14.6, 'b', 30), ('Spain', 11.4, 'g', 50), ('Sweden', 10.2, 'o', 30), ('Germany', 8.1, 'v', 50), ('Finland', 7.6, 'y', 30)]
    parts, lab, run = [], [], 0
    totals = []
    for name, p, f, ty in segs:
        parts.append(rect(X(run), 62, X(run + p) - X(run), 36, k='ink', fill=f, sw=1.6))
        lab.append(text((X(run) + X(run + p)) / 2, 86, p, k='ink', size=15))
        lab.append(text((X(run) + X(run + p)) / 2, ty, name, k='ink', size=15))
        run += p
        totals.append(round(run, 1))
    parts.append(rect(X(run), 62, X(100) - X(run), 36, k='muted', fill='paper', sw=1.6))
    lab.append(text((X(run) + X(100)) / 2, 86, 'the other 22 countries: 48.1', k='muted', size=15))
    for t in totals[1:]:
        lab.append(text(X(t), 122, f'{t:g}', k='green' if t > 50 else 'pen', size=15))
        parts.append(line(X(t), 100, X(t), 108, k='pen', w=1.5))
    parts.append(line(X(50), 52, X(50), 140, k='red', w=2.4, dash=True))
    lab.append(text(X(50) + 6, 150, '50%', k='red', size=18, font='scrawl', anchor='start'))
    lab.append(text(X(26) - 30, 150, 'running totals ↑', k='pen', size=15))
    return svg(600, 162, rough(*parts) + ''.join(lab),
               'A 100 percent bar filled with France, Spain, Sweden, Germany and Finland; the running total passes 50 at 51.9')


Q.append(dict(
    n=6, orig=13, answer='A', topic='Reading tables',
    question=f"""<p>The table shows the areas of the countries of the European Union.</p>
{table([['Austria', '83858', '1.90', '99'], ['Belgium', '30510', '0.70', '344'], ['Bulgaria', '110912', '2.50', '70'],
        ['Cyprus', '9250', '0.20', '84'], ['Czech Republic', '78866', '1.80', '131'], ['Denmark', '43094', '1.00', '126'],
        ['Estonia', '45226', '1.00', '29'], [hl('Finland', 'g'), '337030', hl('7.60', 'g'), '16'],
        [hl('France', 'g'), '643548', hl('14.60', 'g'), '99'], [hl('Germany', 'g'), '357021', hl('8.10', 'g'), '231'],
        ['Greece', '131940', '3.00', '84'], ['Hungary', '93030', '2.10', '108'], ['Ireland', '70280', '1.60', '60'],
        ['Italy', '301320', '6.80', '196'], ['Latvia', '64589', '1.50', '35'], ['Lithuania', '65200', '1.50', '52'],
        ['Luxembourg', '2586', '0.10', '181'], ['Malta', '316', '0.00', '1261'], ['Netherlands', '41526', '0.90', '394'],
        ['Poland', '312685', '7.10', '122'], ['Portugal', '92931', '2.10', '114'], ['Romania', '238391', '5.40', '91'],
        [hl('Spain', 'g'), '504782', hl('11.40', 'g'), '87'], ['Slovakia', '48845', '1.10', '111'], ['Slovenia', '20253', '0.50', '99'],
        [hl('Sweden', 'g'), '449964', hl('10.20', 'g'), '20'], ['United Kingdom', '244820', '5.50', '246'],
        ['<b>European Union</b>', '<b>4422773</b>', '<b>100.00</b>', '']],
       head=['<i>Country</i>', '<i>area (sq km)</i>', hl('<i>% of EU area</i>', 'y', 1), '<i>population density (people/sq km)</i>'])}
<p class="stem">What is the {hl('minimum number of countries', 'b', 2)} needed to make up {hl('at least 50%', 'g', 3)} of the total
land area?</p>""",
    options={'A': '5', 'B': '6', 'C': '7', 'D': '11', 'E': '22'},
    notes=[(1, 'y', 'The percentages are done for you. No need to touch the huge area numbers.'),
           (2, 'b', 'Fewest countries: grab the <b>biggest</b> ones first.'),
           (3, 'g', 'Stop as soon as the running total reaches 50.')],
    steps=[
        f"""<p>Scan the % column for the biggest values and add them, largest first:</p>
{calc('France 14.6', 'Spain + 11.4 = 26.0', 'Sweden + 10.2 = 36.2', 'Germany + 8.1 = 44.3 (still under 50)',
      f'Finland + 7.6 = <b>51.9</b> {tick()} over 50')}
{note('14.6 + 11.4 = 26 exactly: a neat pair to start with.', 'tip')}""",
        f"""{_eu_bar()}
<p>The four biggest only make 44.3%, so four countries can never be enough. Five can.</p>
{calc(f'minimum = {boxed("5")}')}""",
    ],
    answer_text='5 countries: France, Spain, Sweden, Germany and Finland make 51.9%.',
    why={'B': '6 countries would work, but 5 already passes 50%, so 6 isn’t the minimum.',
         'C': '7 is even more than needed.',
         'D': '11 is far too many: the five biggest countries alone already cover 51.9%.',
         'E': '22 is how many countries are <b>left over</b> (27 − 5), not how many are needed.'},
    fast='Biggest five: 14.6 + 11.4 + 10.2 + 8.1 + 7.6 = 51.9. The biggest four make only 44.3. So 5.',
))


# ---------------------------------------------------------------- 7 (Q14)
BOOK_W = [13.2, 15.7, 8.4, 24.9, 15.7, 12.6, 7.7]
BOOK_H = [57.0, 77.2, 93.5, 64.5, 93.7, 114.0, 77.3]
BOOK_U = ['3', '4', '5', '3½', '5', '6', '4']


def _shelf():
    s, x0, base = 1.25, 240, 200
    parts, lab = [], []
    x = x0
    for i, (w, h) in enumerate(zip(BOOK_W, BOOK_H)):
        f = 'y' if i == 0 else 'b' if i == 1 else 'paper'
        parts.append(rect(x, base - h * s, w * s, h * s, k='ink', fill=f, sw=1.8))
        lab.append(text(x + w * s / 2, base - 8, i + 1, k='muted', size=14))
        lab.append(text(x + w * s / 2, base - h * s - 8, BOOK_U[i], k='pen', size=17, font='scrawl'))
        x += w * s
    parts.append(line(x0 - 10, base, x + 10, base, k='ink', w=2.4))
    parts.append(arrow(150, 150, 222, 150, k='red'))
    lab += [eye(130, 150, facing='right'),
            text(130, 124, 'look from', k='red', size=16), text(130, 106, 'this end', k='red', size=16),
            text(x + 30, 70, 'book numbers at the bottom,', k='ink', size=15, anchor='start'),
            text(x + 30, 92, 'heights (in squares) on top', k='pen', size=15, anchor='start'),
            text(x + 30, 130, 'book 1 is nearest the eye', k='ink', size=15, anchor='start'),
            text(x + 30, 152, 'book 2 has only book 1', k='ink', size=15, anchor='start'),
            text(x + 30, 174, 'in front of it', k='ink', size=15, anchor='start')]
    return svg(660, 222, rough(*parts) + ''.join(lab),
               'The seven books redrawn with heights 3, 4, 5, 3 and a half, 5, 6 and 4 squares, looked at from the left end')


def _left_views():
    s = 1.55

    def panel(ox, base, pieces, lines, title, col):
        p, l = [], []
        for (x, w, h) in pieces:
            p.append(rect(ox + x * s, base - h * s, w * s, h * s, k='ink', sw=1.8))
        for (x1, x2, h) in lines:
            p.append(line(ox + x1 * s, base - h * s, ox + x2 * s, base - h * s, k='ink', w=1.8))
        l.append(text(ox + 66, base + 30, title, k=col, size=20, font='scrawl'))
        return p, l

    pD, lD = panel(70, 222, [(0, 85.8, 115.3), (0, 49, 89.9), (0, 36.1, 57.7), (49, 20.5, 69.3)], [(0, 49, 78.2)], 'D: possible ✓', 'green')
    pC, lC = panel(380, 222, [(0, 85.7, 114.5), (0, 41.2, 88.7), (41.2, 16.5, 77.8)], [(0, 41.2, 57.4)], 'C: impossible ✗', 'red')
    extra = [line(70, 222 - 78.2 * s, 70 + 49 * s, 222 - 78.2 * s, k='green', w=3.2),
             line(380, 222 - 77 * s, 380 + 41.2 * s, 222 - 77 * s, k='red', w=3, dash=True)]
    lab = [text(62, 222 - 78.2 * s + 5, 'book 2’s top', k='green', size=15, anchor='end'),
           text(372, 222 - 77 * s - 4, 'book 2’s top', k='red', size=15, anchor='end'),
           text(372, 222 - 77 * s + 15, 'should be here!', k='red', size=15, anchor='end'),
           text(62, 222 - 57.7 * s + 5, 'book 1', k='muted', size=14, anchor='end'),
           text(372, 222 - 57.4 * s + 12, 'book 1', k='muted', size=14, anchor='end')]
    return svg(620, 272, rough(*pD, *pC, *extra) + ''.join(lD + lC + lab),
               'Option D redrawn with book 2’s top edge showing from the left side; option C redrawn with that edge missing')


Q.append(dict(
    n=7, orig=14, answer='C', topic='3D views',
    question=f"""<p>There are seven books on my shelf, which are of {hl('various sizes', 'p', 1)}. When I look at them
straight on I see the following picture:</p>
{fig(Y, 'ps_q07_shelf', 'Seven books of different heights standing side by side, with an arrow pointing at the left-hand end', 220)}
<p>I now look at them {hl('from the left-hand end (in the direction of the arrow)', 'y', 2)}.</p>
<p class="stem">Which one of the following diagrams is {hl('<b>not</b>', 'b', 3)} a possible view when seen from the left-hand
end?</p>
{fig(Y, 'ps_q07_opts', 'Five end-on views A to E, each made of overlapping rectangles that share the bottom-left corner', 420)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'p', 'The picture only shows heights and thicknesses. How deep each book is (front to back) is unknown, so lots of views could happen.'),
           (2, 'y', 'From the end, a book hides everything behind it, except bits that stick up higher or out further.'),
           (3, 'b', 'Four views can happen. Find the one that can’t.')],
    steps=[
        f"""<p>Number the books from the end you are looking from, and note their heights:</p>{_shelf()}""",
        f"""<p>The rule for an end view: book 1 is nearest, so its whole end shows. Every other book only shows where it sticks out
above or beyond <b>all the books in front of it</b>.</p>
<p>Book 2 (height 4) has only book 1 (height 3) in front of it. So book 2 always sticks up above book 1, and its top edge
must appear as a line at height 4 <b>starting right at the left edge</b> of the view.</p>""",
        f"""<p>Look for that line in each option. A, B, D and E all have it. C does not:</p>{_left_views()}
<p>In C the left block goes straight from book 1’s top (3) to a top at 5. The only height-4 shape is a thin strip standing
further back, which would mean book 2 is hidden at the front. Impossible.</p>
{calc(f'not possible = {boxed("C")}')}""",
    ],
    answer_text='View C: book 2’s top edge (height 4) must show from the left edge, and C has no such line.',
    why={'A': 'Possible: books 1 and 2 are equally deep, book 3 is deep enough to hide books 4, 5 and 7, and tall book 6 pokes up above.',
         'B': 'Possible: each book is a little deeper than the one before, so you see a staircase of edges, with tall book 6 deepest.',
         'D': 'Possible: like B, but books 2 and 3 are equally deep (so book 2’s top is a line inside book 3) and book 4 peeks out behind book 3.',
         'E': 'Possible: nearly every book is a bit deeper than the one before, so almost all seven show, and book 7 peeks out behind book 6.'},
    fast='Book 2 is taller than book 1 and nothing else is in front of it, so its top must show as a line from the left edge at height 4. Only C misses it.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _digits():
    xs = [30, 92, 176, 238, 322, 384, 446, 508]
    digs = ['1', '7', '0', '6', '2', '3', '4', '5']
    fills = ['b', 'b', 'o', 'o', 'g', 'g', 'g', 'g']
    parts, lab = [], []
    for x, d, f in zip(xs, digs, fills):
        parts.append(rect(x, 64, 54, 58, k='ink', fill=f, sw=2, rx=4))
        lab.append(text(x + 27, 104, d, k='ink', size=28, font='print'))
    lab += [text(160, 102, '-', k='ink', size=28, font='print'), text(306, 102, '-', k='ink', size=28, font='print')]
    lab += [text(88, 40, 'day: 1? or 31', k='pen', size=17), text(88, 58, '(0, 2 are taken)', k='muted', size=14),
            text(234, 40, 'month: 0?', k='orange', size=17), text(234, 58, '(not 01, 02, 10, 11, 12)', k='muted', size=14),
            text(442, 40, 'year: 2 + smallest digits left', k='green', size=17), text(442, 58, '0, 1, 2 used, so 3, 4, 5', k='muted', size=14)]
    parts.append(circle(30 + 27, 93, 19, k='red', sw=2))
    parts.append(circle(176 + 27, 93, 19, k='red', sw=2))
    parts.append(circle(322 + 27, 93, 19, k='red', sw=2))
    lab.append(text(300, 152, 'every date needs 0, 1 and 2, so the year can’t use them again', k='red', size=17))
    return svg(600, 166, rough(*parts) + ''.join(lab),
               'Eight digit boxes showing 17-06-2345: the day uses 1, the month uses 0, the year starts with 2, and the year then uses 3, 4, 5')


Q.append(dict(
    n=8, orig=18, answer='D', topic='Digits & dates',
    question=f"""<p>Dates may be written in an eight digit form. For instance, 19 January 2005 may be written
19-01-2005.</p>
<p class="stem">In what year will the {hl('next date', 'b', 1)} occur for which {hl('all eight digits are different', 'y', 2)}?</p>""",
    options={'A': '2013', 'B': '2134', 'C': '2145', 'D': '2345', 'E': '2456'},
    notes=[(1, 'b', 'This paper is from 2011, so look forward from then. Every year until 2999 starts with a <b>2</b>.'),
           (2, 'y', '8 different digits from 0–9: only two digits are left out altogether.')],
    steps=[
        f"""<p>The year starts with <b>2</b>, so 2 can’t appear in the day or month.</p>""",
        f"""<p><b>Month</b> (01 to 12): 02 and 12 contain a 2, 11 repeats. 01 and 10 use both 0 and 1, and then the day could only
start with 3: 30 or 31, which need a 0 or 1 again. {cross()}</p>
<p>So the month is <b>0?</b> (03 to 09). It uses the 0.</p>""",
        f"""<p><b>Day</b> must start with 0, 1, 2 or 3. The 0 and 2 are taken, so the day is <b>1?</b> (13 to 19) or <b>31</b>.
Either way it uses the <b>1</b>.</p>""",
        f"""<p>So the day, month and the year’s first digit always use 0, 1 and 2. The other three year digits must come from 3–9.
The smallest is 3, 4, 5:</p>{_digits()}
{calc(f'e.g. 17-06-2345 {ar()} 1, 7, 0, 6, 2, 3, 4, 5 all different {tick()}', f'earliest year = {boxed("2345")}')}""",
    ],
    answer_text='2345 (for example 17-06-2345).',
    why={'A': '2013 uses 0 and 1, but the month needs a 0 or a 1. No month fits.',
         'B': '2134 uses 1, 2 and 3. The month must then be 0?, and the day has to start with 0, 1, 2 or 3: all taken.',
         'C': '2145 uses 1. The month takes the 0, and the day can’t start with 0, 1 or 2; starting with 3 means 30 or 31, which repeat 0 or 1.',
         'E': '2456 does work (e.g. 17-08-2456), but 2345 comes first.'},
    fast='Day and month together always need a 0 and a 1, and the year starts with 2. So the rest of the year uses 3 upwards: 2345.',
))
