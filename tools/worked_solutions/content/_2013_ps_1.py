from wslib import *

Y = 2013
Q = []

# ---------------------------------------------------------------- 1 (Q2)
def _thermo():
    X = lambda t: 150 + (t - 4) * 50
    parts, lab = [], []
    parts.append(rect(X(8), 22, X(9) - X(8), 150, k='green', fill='g', sw=2))
    for r, y, k in ((7, 50, 'pen'), (9, 92, 'orange'), (10, 134, 'violet')):
        parts.append(line(X(r - 2), y, X(r + 2), y, k=k, w=7))
        parts.append(circle(X(r), y, 7, k=k, fill='paper', sw=2.4))
        lab.append(text(X(r - 2) - 14, y + 6, f'reads {r}°: {r - 2}° to {r + 2}°', k=k, size=17, anchor='end'))
    parts.append(line(X(4), 190, X(13), 190, k='ink', head=True))
    for t in range(4, 13):
        parts.append(line(X(t), 184, X(t), 196, k='ink', w=1.5))
        lab.append(text(X(t), 216, f'{t}°', k='muted', size=15))
    lab.append(text(X(8.5), 250, 'only 8° to 9° is inside all three windows', k='green', size=22, font='scrawl'))
    return svg(640, 262, rough(*parts) + ''.join(lab),
               'Three windows on a number line: 5 to 9, 7 to 11 and 8 to 12; they all overlap only from 8 to 9')

Q.append(dict(
    n=1, orig=2, answer='D', topic='Ranges & overlap',
    question=f"""<p>Three thermometers are {hl('each accurate to within 2 degrees above or below', 'y', 1)} the temperature they
actually read. One reads 7°, one reads 9° and one reads 10°.</p>
<p class="stem">What is the {hl('minimum range', 'b', 2)} in which the true temperature lies?</p>""",
    options={'A': '5°–12°', 'B': '7°–9°', 'C': '8°–10°', 'D': '8°–9°', 'E': '7°–10°'},
    notes=[(1, 'y', 'Every thermometer could be up to 2° out either way, so each reading gives a <b>window</b>: reading − 2 to reading + 2.'),
           (2, 'b', 'All three are accurate, so the true temperature must sit inside <b>all three</b> windows at once. Find the overlap.')],
    steps=[
        f"""<p>Turn each reading into a window:</p>
{calc(f'reads 7° {ar()} 5° to 9°', f'reads 9° {ar()} 7° to 11°', f'reads 10° {ar()} 8° to 12°')}""",
        f"""<p>Line the windows up. The true temperature has to be in the bit they <b>share</b>:</p>{_thermo()}""",
        f"""{calc(f'bottom: the highest lower limit = 8° (from the 10° thermometer)', f'top: the lowest upper limit = 9° (from the 7° thermometer)',
      f'true temperature between {boxed("8° and 9°")}')}
{note('Overlap trick: biggest bottom to smallest top. Here 10 − 2 = 8 and 7 + 2 = 9.', 'tip')}""",
    ],
    answer_text='8°–9°: the only temperatures that are within 2° of all three readings.',
    why={'A': '5°–12° joins all three windows together. That is where it could be if only <b>one</b> thermometer had to be right.',
         'B': '7°–9° starts at the lowest reading, but the 10° thermometer says it can’t be below 8°.',
         'C': '8°–10° forgets the 7° thermometer: the temperature can’t be above 7 + 2 = 9°.',
         'E': '7°–10° just runs from the lowest reading to the highest. It never uses the ±2.'},
    fast='Lowest it can be: 10 − 2 = 8°. Highest it can be: 7 + 2 = 9°. So 8°–9°.',
))

# ---------------------------------------------------------------- 2 (Q6)
def _dates():
    parts, lab = [], []
    xs = [120, 162, 222, 264, 324, 366, 408, 450]
    left = [520, 562]
    rows = [(46, 'any date', ['2', 'd', '0', 'm', '1', '9', 'Y', 'Y'], ['?', '?'], 'his age'),
            (146, '1974', ['2', '5', '0', '6', '1', '9', '7', '4'], ['3', '8'], 'age 38'),
            (246, '1983', ['2', '5', '0', '6', '1', '9', '8', '3'], ['4', '7'], 'age 47')]
    fills = ['paper', 'y', 'paper', 'y', 'paper', 'paper', 'b', 'b']
    lab += [text(162, 34, 'DD', k='muted', size=15), text(264, 34, 'MM', k='muted', size=15),
            text(408, 34, 'YYYY', k='muted', size=15), text(562, 34, 'left over', k='green', size=15)]
    for y, title, digs, lo, age in rows:
        for x, d, f in zip(xs, digs, fills):
            parts.append(rect(x, y, 38, 44, k='ink', fill=f, sw=1.8))
            lab.append(text(x + 19, y + 31, d, k='ink', size=24, font='print'))
        for x, d in zip(left, lo):
            parts.append(rect(x, y, 38, 44, k='green', fill='g', sw=2))
            lab.append(text(x + 19, y + 31, d, k='ink', size=24, font='print'))
        lab += [text(211, y + 32, '/', k='muted', size=26), text(313, y + 32, '/', k='muted', size=26),
                text(104, y + 30, title, k='ink', size=18, anchor='end'),
                text(562, y + 66, age, k='green', size=18, font='scrawl')]
    lab += [text(242, 116, 'd and m must be the same', k='orange', size=16),
            text(242, 134, 'in both years (same birthday)', k='orange', size=16),
            text(320, 342, '38 + 9 = 47 ✓  so born 1974 − 38 = 1936', k='red', size=22, font='scrawl')]
    return svg(640, 356, rough(*parts) + ''.join(lab),
               'Digit boxes: every such date is 2d/0m/19YY; in 1974 and 1983 the birthday 25/06 leaves 3, 8 and then 4, 7 over, ages 38 and 47')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Dates & digits',
    question=f"""<p>On only 360 occasions during the twentieth century was it possible to write the date in the form
DD/MM/YYYY using {hl('eight different digits', 'y', 1)}. One example was 28th July 1956 (28/07/1956).</p>
<p>{hl("Eleven of Arthur's birthdays", 'p', 2)} have been such dates (though not his date of birth), and in 1974 and
1983 {hl('the two digits that did not form part of the date made up his age at the time', 'g', 3)}.</p>
<p class="stem">In which year was Arthur born?</p>""",
    options={'A': '1909', 'B': '1916', 'C': '1918', 'D': '1936', 'E': '1938'},
    notes=[(1, 'y', 'DD/MM/YYYY has 8 digits. All different means 8 of the ten digits 0–9 are used once, and <b>2 are left over</b>.'),
           (2, 'p', 'A birthday is the <b>same day and month</b> every year. That links 1974 and 1983 together.'),
           (3, 'g', 'The 2 spare digits make his age, e.g. 3 and 8 make 38.')],
    steps=[
        f"""<p>First, what must every such date look like? The year is 19__, so <b>1</b> and <b>9</b> are used.</p>
<ul><li>Month: 10, 11, 12 and 01 reuse the 1, and 09 reuses the 9. So the month is 0m, and <b>0</b> is used too.</li>
<li>Day: it can’t start with 0 or 1 (used), and 30 or 31 reuse 0 or 1. So the day is <b>2</b>d.</li></ul>
{calc(f'every date = 2d / 0m / 19YY {ar()} 1, 9, 0, 2 always used')}""",
        f"""<p>Now list the spare digits for each year (d, m and the age share them):</p>
{calc(f'1974: used 1, 9, 7, 4, 0, 2 {ar()} free <b>3, 5, 6, 8</b>', f'1983: used 1, 9, 8, 3, 0, 2 {ar()} free <b>4, 5, 6, 7</b>',
      f'same birthday, so d and m are in <b>both</b> lists {ar()} 5 and 6')}
<p>So his birthday is 25/06 (or 26/05), and the leftover digits make his age:</p>{_dates()}""",
        f"""{calc(f'1974: 3 and 8 {ar()} 38 (83 is silly: then 1983 would make him 92)', f'1983: 4 and 7 {ar()} 47 {tick()} exactly 9 years older',
      f'born 1974 − 38 = {boxed("1936")}')}
{note('Check: years using two of 3, 4, 7, 8 after 1936 are 1937, 38, 43, 47, 48, 73, 74, 78, 83, 84, 87. That is eleven birthdays ✓. And 25/06/1936 repeats the 6, so his date of birth doesn’t count ✓.', 'check')}""",
    ],
    answer_text='1936: his birthday is 25/06 (or 26/05), and he was 38 in 1974 and 47 in 1983.',
    why={'A': '1909 makes him 65 then 74. In 1974 the date would need 3 and 8, in 1983 it would need 5 and 6: two different birthdays.',
         'B': '1916 makes him 58 then 67. The date would need 3 and 6 in 1974 but 4 and 5 in 1983: not the same birthday.',
         'C': '1918 makes him 56 then 65. The date would need 3 and 8 in 1974 but 4 and 7 in 1983.',
         'E': '1938 makes him 36 then 45. The date would need 5 and 8 in 1974 but 6 and 7 in 1983.'},
    fast='Dates are always 2d/0m/19YY. Spare digits: 1974 → 3, 5, 6, 8; 1983 → 4, 5, 6, 7. Same birthday, so d and m are 5 and 6; ages 38 and 47; born 1936.',
))

# ---------------------------------------------------------------- 3 (Q7)
def _bonus():
    cols = [(30, 120, ''), (150, 100, 'absent %'), (250, 110, 'over target'), (360, 100, 'rejects %'), (460, 160, 'bonus?')]
    rows = [('Smith', '5', '+5', '2', '£500', 'g'),
            ('Jones', '10', '+6', '4', 'none', 'p'),
            ('Patel', '0', '+12', '5', '£500', 'g'),
            ('Owololu', '4', '0', '7', '£500', 'g'),
            ('McKay', '3', '−4', '4', 'none', 'p')]
    bad = {('Jones', 1), ('McKay', 2)}
    parts, lab = [], []
    y0, rh = 74, 40
    for x, w, h in cols[1:]:
        lab.append(text(x + w / 2, 30, h, k='ink', size=17))
    lab += [text(200, 56, '£500: &lt; 10', k='green', size=14), text(305, 56, '£500: 0 or more', k='green', size=14),
            text(410, 56, '£500: &lt; 8', k='green', size=14)]
    for i, (name, a, o, r, verdict, vf) in enumerate(rows):
        y = y0 + i * rh
        lab.append(text(40, y + 26, name, k='ink', size=18, anchor='start'))
        for j, v in enumerate((a, o, r), 1):
            x, w, _ = cols[j]
            f = 'p' if (name, j) in bad else 'paper'
            parts.append(rect(x + 4, y + 4, w - 8, rh - 8, k='ink', fill=f, sw=1.4))
            lab.append(text(x + w / 2, y + 27, v, k='red' if (name, j) in bad else 'ink', size=18, font='print'))
        x, w, _ = cols[4]
        parts.append(rect(x + 4, y + 4, w - 8, rh - 8, k='green' if vf == 'g' else 'red', fill=vf, sw=1.8))
        lab.append(text(x + w / 2, y + 27, verdict, k='ink', size=19, font='scrawl'))
    lab.append(text(320, y0 + 5 * rh + 30, 'red = breaks a £500 rule', k='red', size=17))
    return svg(640, y0 + 5 * rh + 44, rough(*parts) + ''.join(lab),
               'Grid of each worker’s absence, production and rejects: Jones fails on 10% absence, McKay on −4%; the other three get £500')

Q.append(dict(
    n=3, orig=7, answer='D', topic='Tables & rules',
    question=f"""<p>In order to qualify for a bonus, employees must fulfil certain criteria:</p>
{table([['£1,000 bonus', f"{hl('Absences', 'y', 1)} {hl('less than', 'p', 2)} 5%<br>Production target exceeded by at least 10%<br>{hl('Rejects', 'y', 3)} are less than 5% of output"],
        ['£500 bonus', f"Absences less than 10%<br>Production targets {hl('met', 'g', 4)}<br>Rejects are less than 8% of output"]])}
<p>Workers performed as follows:</p>
{table([['Attendance (%)', '95', '90', '100', '96', '97'],
        ['Over production target (%)', '+5', '+6', '+12', '0', '-4'],
        ['Product accepted (%)', '98', '96', '95', '93', '96']],
       head=['', 'Smith', 'Jones', 'Patel', 'Owololu', 'McKay'])}
<p class="stem">Who qualifies for {hl('a bonus', 'b', 5)}?</p>""",
    options={'A': 'Nobody', 'B': 'Smith', 'C': 'Patel and Smith', 'D': 'Owololu, Patel and Smith',
             'E': 'Jones, Owololu, Patel and Smith'},
    notes=[(1, 'y', 'The table gives <b>attendance</b>, the rules talk about <b>absences</b>: absence = 100 − attendance.'),
           (2, 'p', '“Less than” is strict. Exactly 5% is <b>not</b> less than 5%.'),
           (3, 'y', 'Same switch: rejects = 100 − product accepted.'),
           (4, 'g', 'Met = 0 or more over target. Exactly on target (0) counts!'),
           (5, 'b', 'Either bonus counts, the £500 one too.')],
    steps=[
        f"""<p>Flip the table into the rules’ language first:</p>
{calc('absent % = 100 − attendance: 5, 10, 0, 4, 3', 'rejects % = 100 − accepted: 2, 4, 5, 7, 4')}""",
        f"""<p>Test the easier <b>£500</b> rules (absent under 10, target met, rejects under 8):</p>{_bonus()}""",
        f"""<p>Does anyone get the bigger £1,000 instead? It doesn’t change the answer, but it shows the traps:</p>
{calc(f'Smith: absent exactly 5 (not less than 5), and only +5 {ar()} no', f'Patel: absent 0, +12, but rejects exactly 5 (not less than 5) {ar()} no',
      f'so nobody gets £1,000, but three get £500 {ar()} {boxed("Owololu, Patel and Smith")}')}
{note('Owololu’s 0 means he hit the target exactly. “Targets met” is satisfied.', 'trap')}""",
    ],
    answer_text='Owololu, Patel and Smith: all three meet every £500 rule.',
    why={'A': 'Nobody gets £1,000, but three people get the £500. Don’t forget the smaller bonus.',
         'B': 'Misses Patel (only his rejects stop the £1,000, he still gets £500) and Owololu.',
         'C': 'Misses Owololu: 0% over target means the target was met exactly, which counts.',
         'E': 'Adds Jones, but 90% attendance is 10% absence, and 10 is not less than 10.'},
    fast='Absent = 100 − attendance, rejects = 100 − accepted. £500 needs absent under 10, target 0 or more, rejects under 8: Smith, Patel, Owololu.',
))

# ---------------------------------------------------------------- 4 (Q8)
def _map():
    A, D, C = (470, 120), (470, 250), (150, 250)
    EN, EW, ES = (150, 50), (150, 120), (150, 190)
    parts = [circle(*A, 9, k='ink', fill='y', sw=2.2), circle(*D, 7, k='ink', fill='paper'), circle(*C, 7, k='ink', fill='paper'),
             line(A[0], A[1] + 10, D[0], D[1] - 10, k='pen', head=True, w=2.6),
             line(D[0] - 10, D[1], C[0] + 10, C[1], k='pen', head=True, w=2.6),
             line(C[0], C[1] - 10, EN[0], EN[1] + 6, k='orange', head=True, w=2.6, dash=True),
             circle(*EN, 8, k='orange', fill='o'), circle(*EW, 8, k='orange', fill='o'), circle(*ES, 8, k='orange', fill='o'),
             line(A[0] - 12, A[1] - 4, EN[0] + 12, EN[1] + 3, k='green', head=True, w=1.8, dash=True),
             line(A[0] - 12, A[1], EW[0] + 12, EW[1], k='green', head=True, w=1.8, dash=True),
             line(A[0] - 12, A[1] + 4, ES[0] + 12, ES[1] - 3, k='green', head=True, w=1.8, dash=True),
             circle(330, 120, 6, k='muted', fill='paper'),
             line(590, 92, 590, 32, k='ink', head=True, w=2)]
    lab = [text(A[0] + 16, A[1] + 6, 'Akeland (you)', k='ink', size=18, anchor='start'),
           text(D[0] + 14, D[1] + 6, 'Ducton', k='ink', size=17, anchor='start'),
           text(C[0] - 14, C[1] + 6, 'Cranton', k='ink', size=17, anchor='end'),
           text(A[0] + 10, 190, 'south', k='pen', size=16, anchor='start'),
           text(310, 274, 'west', k='pen', size=16),
           text(EN[0] - 14, EN[1] + 6, 'Eksberg?', k='orange', size=17, anchor='end'),
           text(EW[0] - 14, EW[1] + 6, 'Eksberg?', k='orange', size=17, anchor='end'),
           text(ES[0] - 14, ES[1] + 6, 'Eksberg?', k='orange', size=17, anchor='end'),
           text(250, 62, 'NW', k='green', size=18, font='scrawl'), text(260, 112, 'W', k='green', size=18, font='scrawl'),
           text(250, 178, 'SW', k='green', size=18, font='scrawl'),
           text(330, 146, 'Benford', k='muted', size=14), text(330, 162, '(red herring)', k='muted', size=13),
           text(590, 26, 'N', k='ink', size=18, font='print'),
           text(150, 300, 'north of Cranton by an unknown amount', k='orange', size=16)]
    return svg(640, 312, rough(*parts) + ''.join(lab),
               'Map: from Akeland go south to Ducton, west to Cranton, then north an unknown distance to Eksberg, which could be north-west, west or south-west of Akeland')

Q.append(dict(
    n=4, orig=8, answer='B', topic='Directions & maps',
    question=f"""<p>I stopped in a town called Akeland to ask the way to Eksberg. The only sense I could get from a
local was as follows:</p>
<p>{hl('Akeland is east of Benford.', 'p', 1)}</p>
<p>{hl('Eksberg is north of Cranton.', 'g')}</p>
<p>{hl('Ducton is south of Akeland.', 'g', 2)}</p>
<p>{hl('Cranton is west of Ducton.', 'g')}</p>
<p>Assuming that 'east' means, as near as it matters, 'due east', which one of the following can be
{hl('said with certainty', 'b', 3)}?</p>""",
    options={'A': 'I need to go due west.', 'B': 'I need to go to the west, but it may be north-west or south-west.',
             'C': 'I need to go north-west.', 'D': 'I need to go to the north, but it may also be a bit west.',
             'E': 'I need to go south-west.'},
    notes=[(1, 'p', 'Benford never connects to the other towns. A red herring.'),
           (2, 'g', 'The useful chain: Akeland → south to Ducton → west to Cranton → north to Eksberg.'),
           (3, 'b', 'It must be true whatever the (unknown) distances are.')],
    steps=[
        f"""<p>Start where you are, Akeland, and follow the chain, drawing as you go:</p>{_map()}""",
        f"""<p>No distances are given, so compare the two up-and-down legs:</p>
{calc(f'north leg shorter than south leg {ar()} Eksberg is south-west', f'north leg equal to south leg {ar()} due west',
      f'north leg longer {ar()} north-west')}
<p>The only sure thing: Cranton is west of Ducton, so Eksberg is <b>to the west</b>. North or south of that, we can’t tell
{ar()} {boxed('B')}</p>""",
    ],
    answer_text='West, but it could be north-west or south-west: the north and south legs have unknown lengths.',
    why={'A': 'Due west only if the north leg exactly equals the south leg. We aren’t told the distances.',
         'C': 'North-west only if the north leg is the longer one. Not certain.',
         'D': 'Eksberg is definitely west, and it could just as well be to the south. “To the north” isn’t certain.',
         'E': 'South-west only if the north leg is the shorter one. Not certain.'},
    fast='Akeland → south → west → north. The west part is certain; the north part might be more or less than the south part. So west, maybe NW or SW.',
))

# ---------------------------------------------------------------- 5 (Q12)
def _savings():
    Yp = lambda p: 270 - p * 0.17
    parts, lab = [], []
    parts.append(line(40, Yp(0), 610, Yp(0), k='ink', w=2))
    panels = [(70, 270, 0, 600, 300, 15, 615, 'Year 1'), (340, 540, 615, 1215, 915, 45.75, 1260.75, 'Year 2')]
    for x0, x1, s, f, avg, inte, end, title in panels:
        parts.append(poly([(x0, Yp(0)), (x0, Yp(s)), (x1, Yp(f)), (x1, Yp(0))], k='pen', fill='b', sw=2))
        parts.append(line(x0, Yp(avg), x1, Yp(avg), k='red', w=2.2, dash=True))
        parts.append(line(x1 + 8, Yp(f), x1 + 8, Yp(end), k='green', w=6))
        lab += [text((x0 + x1) / 2, 292, title, k='ink', size=18, font='scrawl'),
                text(x0 - 4, Yp(s) - 8, f'start £{s}', k='pen', size=15, anchor='start'),
                text(x1, Yp(f) - 26, f'finish £{f}', k='pen', size=15, anchor='end'),
                text((x0 + x1) / 2, Yp(avg) - 8, f'average £{avg}', k='red', size=16),
                text(x1 + 18, Yp(end) + 4, f'+£{inte:g}', k='green', size=17, anchor='start', font='scrawl')]
    lab.append(text(340, 30, '5% of 915 = 45.75 → £1,260.75', k='green', size=19, anchor='start', font='scrawl'))
    return svg(640, 304, rough(*parts) + ''.join(lab),
               'Two ramps: year 1 from 0 to 600 with average 300 and 15 interest; year 2 from 615 to 1215 with average 915 and 45.75 interest')

Q.append(dict(
    n=5, orig=12, answer='B', topic='Percentages & interest',
    question=f"""<p>I have just joined a savings scheme. I will pay in {hl('£50 each month', 'g', 1)} and at the end of each complete
year I will be paid {hl('5% interest on my average balance', 'y', 2)} ({hl('i.e. the average of my starting and finishing amount', 'y', 3)}) for the previous 12 months.</p>
<p class="stem">How much will I have in total when my interest has been paid at the {hl('end of the second year', 'b', 4)}?
(Answer to the nearest £10.)</p>""",
    options={'A': '£1230', 'B': '£1260', 'C': '£1290', 'D': '£1380', 'E': '£1990'},
    notes=[(1, 'g', '12 × £50 = <b>£600</b> paid in each year.'),
           (2, 'y', 'Interest once a year, and only 5% of the <b>average</b>, not of the final amount.'),
           (3, 'y', 'Average = (start + finish) ÷ 2. Nice and easy.'),
           (4, 'b', 'Two rounds of interest. Year 1’s interest is already in the pot when year 2 starts.')],
    steps=[
        f"""<p><b>Year 1</b>: start with nothing.</p>
{calc('start £0, finish 12 × 50 = £600', f'average = (0 + 600) ÷ 2 = £300', f'interest = 5% of 300 = £15 {ar()} pot = <b>£615</b>')}""",
        f"""<p><b>Year 2</b>: start with the £615.</p>
{calc('start £615, finish 615 + 600 = £1,215', 'average = (615 + 1215) ÷ 2 = 1830 ÷ 2 = £915',
      f'interest = 5% of 915 = £45.75', f'pot = 1215 + 45.75 = 1260.75 {ar()} {boxed("£1260")}')}
{note('5% = half of 10%. 10% of 915 = 91.50, half of that = 45.75.', 'tip')}""",
        f"""<p>Picture it: each year the money ramps up steadily, and interest is paid on the middle height of the ramp.</p>{_savings()}""",
    ],
    answer_text='£1260: £15 interest in year 1, £45.75 in year 2, on top of £1,200 paid in.',
    why={'A': '£1230 gives year 2 only £15 interest again, as if it started from £0. Year 2 starts with £615 already saved.',
         'C': '£1290 pays 5% on the <b>finishing</b> balance each year (£30, then £61.50) instead of the average.',
         'D': '£1380 needs £180 of interest, which is 15% of £1,200. Far too much.',
         'E': '£1990 needs about £790 of interest on £1,200 saved. Nothing like 5% a year.'},
    fast='Year 1: average 300 → +15 → 615. Year 2: average (615 + 1215) ÷ 2 = 915 → +45.75 → 1260.75, so £1260.',
))

# ---------------------------------------------------------------- 6 (Q13)
def _cake():
    s, base = 40, 262
    H = lambda v: v * s
    parts = [rect(60, base - H(1.6), 100, H(1.6), k='ink', fill='y', sw=1.8),
             rect(60, base - H(2.6), 100, H(1.0), k='ink', fill='b', sw=1.8),
             rect(260, base - H(2.6), 100, H(2.6), k='ink', fill='paper', sw=1.8),
             rect(260, base - H(4.55), 100, H(1.95), k='ink', fill='g', sw=1.8),
             rect(460, base - H(4.095), 100, H(4.095), k='ink', fill='o', sw=1.8),
             rect(460, base - H(4.55), 100, H(0.455), k='muted', fill='none', sw=1.6),
             line(30, base, 600, base, k='ink', w=2),
             arrow(172, base - H(2.6), 250, base - H(3.7), k='red', bend=-0.2),
             arrow(372, base - H(4.7), 452, base - H(4.7), k='red', bend=-0.25)]
    lab = [text(110, base - H(0.8) + 6, '1.60', k='ink', size=17), text(110, base - H(2.1) + 6, 'time 1.00', k='ink', size=16),
           text(110, base - H(2.6) - 10, 'cost £2.60', k='pen', size=19, font='scrawl'),
           text(310, base - H(1.3) + 6, '2.60', k='ink', size=17), text(310, base - H(3.6) + 6, '+1.95', k='ink', size=17),
           text(310, base - H(4.55) - 10, '£4.55', k='pen', size=19, font='scrawl'),
           text(510, base - H(2) + 6, '4.55 − 0.455', k='ink', size=16),
           text(510, base - H(4.55) - 10, '£4.10', k='green', size=22, font='scrawl'),
           text(200, base - H(3.6) - 4, '+75%', k='red', size=19), text(412, base - H(5.15), '−10%', k='red', size=19),
           text(110, base + 24, 'cost to make', k='muted', size=15), text(310, base + 24, 'normal price', k='muted', size=15),
           text(510, base + 24, 'friends’ price', k='muted', size=15)]
    return svg(640, 296, rough(*parts) + ''.join(lab),
               'Three bars: cost 2.60 (1.60 ingredients plus 1.00 time), normal price 4.55 after adding 75%, friends pay 4.10 after 10% off')

Q.append(dict(
    n=6, orig=13, answer='B', topic='Percentages & costs',
    question=f"""<p>Every Thursday, Marilyn spends {hl('10 hours making 60 cakes', 'g', 1)} to sell at her local market. The cost of
the ingredients to make each cake is £1.60 and Marilyn {hl('charges £6 an hour for her time', 'y', 2)}. She
usually sets the sale price for a cake at {hl('75% more than the total costs of making it', 'y', 3)}. However, when
she sells to her friends she gives them a {hl('10% discount on the normal sale price', 'p', 4)}.</p>
<p class="stem">What do her friends have to pay for {hl('one', 'b', 5)} of Marilyn's cakes?</p>""",
    options={'A': '£3.42', 'B': '£4.10', 'C': '£4.29', 'D': '£4.55', 'E': '£4.88'},
    notes=[(1, 'g', '60 cakes in 10 hours = 6 cakes an hour.'),
           (2, 'y', 'Her time is a cost too: £6 an hour shared by 6 cakes = <b>£1 per cake</b>.'),
           (3, 'y', 'Total cost = ingredients + time. Then add 75% of that.'),
           (4, 'p', 'The 10% comes off the <b>sale price</b>, as a separate second step.'),
           (5, 'b', 'Price of one cake, not the whole batch.')],
    steps=[
        f"""<p>Cost of one cake:</p>
{calc(f'time: 10 h × £6 = £60 for 60 cakes {ar()} £1 a cake', f'ingredients £1.60 {ar()} total cost = <b>£2.60</b>')}""",
        f"""<p>Normal price, 75% more:</p>
{calc('75% of 2.60 = half (1.30) + quarter (0.65) = 1.95', '2.60 + 1.95 = <b>£4.55</b>')}""",
        f"""<p>Friends get 10% off that:</p>
{calc('10% of 4.55 = 0.455', f'4.55 − 0.455 = 4.095 {ar()} {boxed("£4.10")}')}{_cake()}""",
    ],
    answer_text='£4.10: cost £2.60, plus 75% makes £4.55, minus 10% makes £4.095.',
    why={'A': '£3.42 adds the 75% to the ingredients only (2.80), then adds the £1 for time and takes 10% off.',
         'C': '£4.29 merges the two changes into +65% (2.60 × 1.65). Take 10% off the new price instead.',
         'D': '£4.55 is the normal price: it forgets the friends’ 10% discount.',
         'E': '£4.88 is more than the full price of £4.55, so it can’t be a discounted price.'},
    fast='Cost = 1.60 + 60 ÷ 60 = 2.60. × 1.75 = 4.55. × 0.9 = 4.095 ≈ £4.10.',
))

# ---------------------------------------------------------------- 7 (Q14)
def _wages():
    base, s = 250, 1.3
    parts, lab = [], []
    panels = [(40, 'up first', [(100, 'paper'), (150, 'g'), (75, 'p')], ['+50%', '−50% of 150']),
              (350, 'down first', [(100, 'paper'), (50, 'p'), (75, 'p')], ['−50%', '+50% of 50'])]
    for x0, title, bars, ops in panels:
        parts.append(line(x0 - 10, base - 100 * s, x0 + 250, base - 100 * s, k='muted', w=1.6, dash=True))
        for i, (v, f) in enumerate(bars):
            x = x0 + i * 95
            parts.append(rect(x, base - v * s, 60, v * s, k='ink', fill=f, sw=1.8))
            lab.append(text(x + 30, base - v * s - 8, f'£{v}', k='ink', size=18))
        for i, op in enumerate(ops):
            lab.append(text(x0 + 77 + i * 95, base + 22, op, k='red', size=15))
        lab.append(text(x0 + 125, 22, title, k='pen', size=20, font='scrawl'))
        parts.append(line(x0, base, x0 + 250, base, k='ink', w=2))
    lab += [text(320, 282, 'Both orders end at £75: below the start', k='red', size=19, font='scrawl'),
            text(625, base - 100 * s + 5, 'start', k='muted', size=14, anchor='end')]
    return svg(640, 294, rough(*parts) + ''.join(lab),
               'Exaggerated example with 50 percent: 100 up to 150 then down to 75, or 100 down to 50 then up to 75; both end below 100')

Q.append(dict(
    n=7, orig=14, answer='C', topic='Percentage change',
    question=f"""<p>A business, facing turbulent times, changed the wages of its workers by the {hl('same percentage', 'y', 1)} in
two successive years, but the changes were in {hl('opposite directions', 'p', 2)}.</p>
<p class="stem">Which of the following best describes the wages of the workers {hl('after the second change', 'b', 3)}?</p>""",
    options={'A': 'The same as the original wage.', 'B': 'Necessarily higher than the original wage.',
             'C': 'Necessarily lower than the original wage.', 'D': 'Higher than originally if the first change was an increase, otherwise lower.',
             'E': 'Higher than originally if the first change was a decrease, otherwise lower.'},
    notes=[(1, 'y', 'Same percentage both years, e.g. 10% and 10%.'),
           (2, 'p', 'One up, one down. It feels like they cancel out. They don’t!'),
           (3, 'b', 'Compare the final wage with the original one.')],
    steps=[
        f"""<p>Try it with numbers: a £100 wage and 10% changes, both orders.</p>
{calc(f'up first: 100 → 110 {ar()} 10% of 110 is 11 {ar()} 110 − 11 = <b>99</b>', f'down first: 100 → 90 {ar()} 10% of 90 is 9 {ar()} 90 + 9 = <b>99</b>')}
<p>The second change is a percentage of a <b>different</b> amount, so it doesn’t undo the first one.</p>""",
        f"""<p>Exaggerate to see it clearly: use 50%.</p>{_wages()}
{calc(f'× 1.5 × 0.5 = × 0.75, and × 0.5 × 1.5 = × 0.75 {ar()} the order doesn’t matter', f'always lower {ar()} {boxed("C")}')}
{note('Stuck on a percentage question with no numbers? Pick £100 and a big, easy percentage.', 'tip')}""",
    ],
    answer_text='Necessarily lower: × (1 + p) × (1 − p) is always less than 1.',
    why={'A': 'Only true if the change is 0%. Any real change leaves the wage lower.',
         'B': 'It is never higher: the cut comes off the bigger amount, or the rise goes on the smaller amount.',
         'D': 'The order doesn’t matter: × 1.1 × 0.9 and × 0.9 × 1.1 are both × 0.99.',
         'E': 'Same mistake as D the other way round: both orders end lower.'},
    fast='£100 with ±10%: 110 → 99, or 90 → 99. Lower either way.',
))

# ---------------------------------------------------------------- 8 (Q18)
def _race():
    X = lambda t: 60 + t * 14.5
    R = lambda f: 60 + f * 540
    parts = [line(R(0), 70, R(1), 70, k='ink', w=3)]
    lab = [text(R(0), 100, 'Alvros', k='ink', size=17), text(R(1), 100, 'Berget', k='ink', size=17)]
    for f in (1 / 3, 2 / 3):
        parts.append(line(R(f), 60, R(f), 80, k='ink', w=2))
    for i in range(3):
        lab.append(text(R(i / 3 + 1 / 6), 56, 'Sven: 10 min', k='pen', size=15))
    # car and walker
    cx = R(2 / 3) - 40
    parts += [rect(cx - 22, 78, 44, 14, k='orange', fill='o', sw=1.8), circle(cx - 12, 94, 4, k='orange', fill='paper'),
              circle(cx + 12, 94, 4, k='orange', fill='paper')]
    lab += [text(R(2 / 3), 118, 'car breaks down', k='red', size=16, font='scrawl'),
            stick_person(R(5 / 6), 106, k='orange', s=0.8), text(R(5 / 6) + 34, 100, 'walk', k='orange', size=15, anchor='start')]
    # time bars
    parts += [rect(X(0), 150, X(30) - X(0), 30, k='ink', fill='b', sw=1.8),
              rect(X(0), 200, X(20 / 3) - X(0), 30, k='ink', fill='o', sw=1.8),
              rect(X(20 / 3), 200, X(110 / 3) - X(20 / 3), 30, k='ink', fill='p', sw=1.8),
              line(X(0), 256, X(38), 256, k='ink', head=True, w=2),
              line(X(30), 140, X(30), 246, k='red', w=2, dash=True), line(X(110 / 3), 140, X(110 / 3), 246, k='red', w=2, dash=True)]
    lab += [text(X(15), 171, 'Sven cycles: 30 min', k='ink', size=16),
            text(X(10 / 3), 221, '6⅔', k='ink', size=14), text(X(65 / 3), 221, 'Helga walks the last third: 30 min', k='ink', size=16),
            text(X(0) - 8, 171, 'Sven', k='pen', size=15, anchor='end'), text(X(0) - 8, 221, 'Helga', k='orange', size=15, anchor='end')]
    for t in range(0, 40, 10):
        parts.append(line(X(t), 250, X(t), 262, k='ink', w=1.5))
        lab.append(text(X(t), 280, f'{t} min', k='muted', size=14))
    lab.append(text(X(33.3), 136, 'gap 6⅔ min', k='red', size=17, font='scrawl'))
    return svg(640, 292, rough(*parts) + ''.join(lab),
               'Road in thirds, Sven 10 minutes per third; time bars: Sven 30 minutes, Helga 6 and two thirds by car then 30 walking, finishing 6 and two thirds minutes later')

Q.append(dict(
    n=8, orig=18, answer='C', topic='Speed & time',
    question=f"""<p>Sven is a keen cyclist and is riding from Alvros to Berget. At his normal cycling speed this will take
him {hl('30 minutes', 'g', 1)}. His wife, Helga, will go by car to bring him and his bike back. They leave at the
same time, but {hl('two thirds of the way', 'g', 2)} between the two towns the car breaks down and Helga has to
walk the rest of the way. The car goes at {hl('three times the speed', 'y', 3)} Sven cycles. But Helga walks at
{hl('only one third of the speed', 'p', 4)} he cycles.</p>
<p class="stem">{hl('Who arrives at Berget first, and by how much', 'b', 5)} (to the nearest minute if necessary)?</p>""",
    options={'A': 'Helga by 12 minutes.', 'B': 'They arrive at the same time.', 'C': 'Sven by 7 minutes.',
             'D': 'Sven by 33 minutes.', 'E': 'Sven by 37 minutes.'},
    notes=[(1, 'g', 'Sven’s whole ride is 30 minutes, so each third of the road takes him 10 minutes.'),
           (2, 'g', 'Two thirds by car, the last third on foot.'),
           (3, 'y', '3 times faster means a third of the time.'),
           (4, 'p', '3 times slower means 3 times the time. This is what sinks Helga.'),
           (5, 'b', 'Two things to find: who wins, and the gap.')],
    steps=[
        f"""<p>Work in thirds of the road. Sven takes 10 minutes per third.</p>
{calc(f'Helga by car: 2 thirds = 20 min at Sven’s speed {ar()} ÷ 3 = 6⅔ min', f'Helga on foot: 1 third = 10 min at Sven’s speed {ar()} × 3 = 30 min',
      f'Helga total = 6⅔ + 30 = <b>36⅔ min</b>')}""",
        f"""{_race()}
{calc(f'36⅔ − 30 = 6⅔ min ≈ 7 min {ar()} {boxed("Sven by 7 minutes")}')}
{note('“Three times faster” and “three times slower” don’t cancel out. Slow stretches cost far more time than fast ones save.', 'trap')}""",
    ],
    answer_text='Sven by 7 minutes: Helga takes 6⅔ + 30 = 36⅔ minutes against his 30.',
    why={'A': 'Helga can’t win: the last third alone takes her 30 minutes, as long as Sven’s whole ride.',
         'B': 'Assumes 3 times faster and 3 times slower cancel out. They don’t.',
         'D': 'Swaps the fractions: driving one third (3⅓ min) and walking two thirds (60 min) gives 63⅓, which is Sven by 33.',
         'E': '37 minutes is roughly Helga’s whole journey time (36⅔), not the gap between them.'},
    fast='Each third = 10 min for Sven. Helga: 20 ÷ 3 + 10 × 3 = 6⅔ + 30 = 36⅔. Sven wins by 6⅔ ≈ 7.',
))
