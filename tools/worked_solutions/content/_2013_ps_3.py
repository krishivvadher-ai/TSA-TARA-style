from wslib import *

Y = 2013
Q = []

# ---------------------------------------------------------------- 18 (Q37)
def _tunes():
    s = 6
    parts, lab = [], []
    piles = [(40, 1, 10, 'g', '10 s × 1'), (170, 6, 15, 'b', '15 s × 6'), (360, 3, 20, 'o', '20 s × 3')]
    for x, n, secs, f, name in piles:
        for i in range(n - 1, -1, -1):
            parts.append(rect(x + i * 5, 34 - i * 4, secs * s, 34, k='ink', fill=f, sw=1.5))
        lab.append(text(x + secs * s / 2, 92, name, k='ink', size=17))
    lab.append(text(600, 58, 'the repertoire', k='muted', size=15, anchor='end'))
    x = 40
    for secs, f in ((10, 'g'), (15, 'b'), (15, 'b')):
        parts.append(rect(x, 140, secs * s, 38, k='ink', fill=f, sw=1.8))
        lab.append(text(x + secs * s / 2, 165, f'{secs} s', k='ink', size=16))
        x += secs * s
    for i in range(2):
        parts.append(rect(x + i * 120, 140, 120, 38, k='muted', fill='none', sw=1.4))
        lab.append(text(x + i * 120 + 60, 165, f'go {i + 2}', k='muted', size=15))
    lab += [text(40, 128, 'shortest go: 3 different tunes', k='pen', size=17, anchor='start'),
            text(x + 250, 165, '…', k='muted', size=20, anchor='start'),
            brace(40, 280, 184, '40 s', k='red', size=18),
            text(320, 252, '3600 s ÷ 40 s = 90 goes in an hour', k='green', size=22, font='scrawl')]
    return svg(640, 266, rough(*parts) + ''.join(lab),
               'Tune lengths: one 10 s, six 15 s, three 20 s; the shortest go is 10 + 15 + 15 = 40 seconds, so 90 goes fit in 3600 seconds')

Q.append(dict(
    n=18, orig=37, answer='C', topic='Maximum & minimum',
    question=f"""<p>I have a bird automaton that, when activated, flaps its wings and whistles {hl('three different tunes', 'y', 1)}
successively, selected at random from its repertoire of ten. It performs {hl('one of its ten tunes for 10 seconds, six of them for 15 seconds each and three of them for 20 seconds each', 'g', 2)}.</p>
<p>When my granddaughter visits she is fascinated, {hl('activating it again and again as soon as it stops', 'y', 3)}
each time. On her last visit she kept it going for {hl('a whole hour', 'g', 4)}, and I lost count of how many times
she activated it.</p>
<p class="stem">What is the {hl('<b>maximum</b>', 'b', 5)} number of times that my automaton could possibly have been activated
during one hour?</p>""",
    options={'A': '75', 'B': '80', 'C': '90', 'D': '120', 'E': '225'},
    notes=[(1, 'y', 'Each go plays 3 tunes, and they must be <b>different</b> tunes.'),
           (2, 'g', 'Only <b>one</b> tune is 10 seconds long. The next shortest are 15 seconds.'),
           (3, 'y', 'No gaps between goes.'),
           (4, 'g', '1 hour = 60 × 60 = 3600 seconds.'),
           (5, 'b', 'Most goes = each go as short as possible.')],
    steps=[
        f"""<p>Make one go as short as possible: pick the three shortest <b>different</b> tunes.</p>
{calc(f'one 10 s tune + two 15 s tunes = 10 + 15 + 15 = <b>40 s</b>')}{_tunes()}""",
        f"""{calc('1 hour = 3600 s', f'3600 ÷ 40 = {boxed("90")}')}
{note('Every go could be 10 + 15 + 15: the 10 s tune can be picked every time, since “different” only applies within one go.', 'check')}""",
    ],
    answer_text='90: the shortest possible go is 10 + 15 + 15 = 40 seconds, and 3600 ÷ 40 = 90.',
    why={'A': '75 uses the average tune (160 ÷ 10 = 16 s, so 48 s a go). The maximum needs the shortest tunes.',
         'B': '80 uses three 15-second tunes (45 s a go), forgetting the 10-second tune can be one of the three.',
         'D': '120 uses three 10-second tunes (30 s), but there is only one 10-second tune and the tunes must be different.',
         'E': '225 is 3600 ÷ 16: one average tune per go. Each go plays three tunes.'},
    fast='Shortest go = 10 + 15 + 15 = 40 s. 3600 ÷ 40 = 90.',
))

# ---------------------------------------------------------------- 19 (Q38)
def _shop():
    data = [('Mon', 4, '10 h'), ('Tue', 3, '?'), ('Wed', 4.8, '12 h'), ('Thu', 4, '10 h'), ('Fri', 4, '?'), ('Sat', 4, '10 h'), ('Sun', 2.4, '6 h')]
    base, u = 270, 40
    parts, lab = [], []
    for k in range(1, 6):
        parts.append(line(40, base - k * u, 620, base - k * u, k='muted', w=1, dash=True))
        lab.append(text(34, base - k * u + 5, f'{k * 2.5:g} h', k='muted', size=13, anchor='end'))
    for i, (d, v, h) in enumerate(data):
        x = 60 + i * 82
        f = 'o' if h == '?' else 'b'
        parts.append(rect(x, base - v * u, 46, v * u, k='ink', fill=f, sw=1.6))
        lab += [text(x + 23, base + 20, d, k='ink', size=16),
                text(x + 23, base + 42, h, k='red' if h == '?' else 'pen', size=18 if h == '?' else 16, font='scrawl')]
    parts.append(line(40, base, 620, base, k='ink', w=2))
    lab += [text(330, 26, 'Mon: 4 lines in 10 hours, so 1 line = 2.5 hours of customers', k='pen', size=17),
            text(40, base + 72, 'Tue: 3 lines = 7½ h at the normal rate → open a bit LESS than 7½ h', k='orange', size=16, anchor='start'),
            text(40, base + 94, 'Fri: 4 lines = 10 h at the normal rate → open a bit LESS than 10 h', k='orange', size=16, anchor='start')]
    return svg(640, base + 108, rough(*parts) + ''.join(lab),
               'Redrawn bar chart with gridlines labelled in hours: Monday 4 lines for 10 hours, Wednesday 4.8 for 12, Sunday 2.4 for 6; Tuesday 3 lines and Friday 4 lines need slightly fewer hours')

Q.append(dict(
    n=19, orig=38, answer='E', topic='Charts & rates',
    question=f"""<p>Graham recorded the number of visitors to his shop each day last week and presented the results
in the bar chart below:</p>
{fig(Y, 'ps_q19_chart', 'Bar chart of total customers per day with gridlines but no numbers: Monday, Thursday, Friday and Saturday reach the 4th gridline, Tuesday the 3rd, Wednesday about 4.8, Sunday about 2.4', 520)}
<p>When he calculated the {hl('number of customers per hour', 'y', 1)} he found that he had {hl('the same number for five of the days', 'g', 2)}, but {hl('the values for Tuesday and Friday were slightly higher', 'p', 3)}. The opening hours of
the shop are as follows:</p>
{table([['Monday', '8 am', '6 pm'], ['Tuesday', '?', '?'], ['Wednesday', '8 am', '8 pm'], ['Thursday', '8 am', '6 pm'],
        ['Friday', '?', '?'], ['Saturday', '8 am', '6 pm'], ['Sunday', '10 am', '4 pm']], head=['Day', 'Open', 'Close'])}
<p class="stem">Which one of the following {hl('could be', 'b', 4)} the opening hours of the shop for Tuesday and Friday?</p>""",
    options={'A': 'Tuesday 9.30 am–5.30 pm, Friday 8.00 am–6.30 pm', 'B': 'Tuesday 9.00 am–4.30 pm, Friday 8.30 am–6.00 pm',
             'C': 'Tuesday 9.00 am–4.30 pm, Friday 8.00 am–6.00 pm', 'D': 'Tuesday 9.00 am–5.00 pm, Friday 8.00 am–6.30 pm',
             'E': 'Tuesday 10.00 am–5.00 pm, Friday 8.30 am–6.00 pm'},
    notes=[(1, 'y', 'Customers per hour = bar height ÷ hours open.'),
           (2, 'g', 'Mon, Wed, Thu, Sat, Sun share one rate. Use them to turn bar heights into hours.'),
           (3, 'p', 'Higher rate = the same customers in <b>fewer</b> hours. Slightly fewer, and it must be true for <b>both</b> days.'),
           (4, 'b', 'Test each option against both days.')],
    steps=[
        f"""<p>No numbers on the axis? No problem: count gridlines. Monday reaches 4 lines and is open 8 am–6 pm = 10 hours.</p>
{calc(f'4 lines in 10 h {ar()} 1 line = 2.5 h', f'check Wed: 12 h ÷ 2.5 = 4.8 lines {tick()}   Sun: 6 h ÷ 2.5 = 2.4 lines {tick()}')}{_shop()}""",
        f"""<p>Now test each option (each day must be <b>under</b> its normal hours):</p>
{calc(f'A: Tue 9.30–5.30 = 8 h {cross()}   Fri 8.00–6.30 = 10½ h {cross()}',
      f'B: Tue 9.00–4.30 = 7½ h {cross()} (exactly normal)   Fri 8.30–6.00 = 9½ h {tick()}',
      f'C: Tue 7½ h {cross()}   Fri 8.00–6.00 = 10 h {cross()}',
      f'D: Tue 9.00–5.00 = 8 h {cross()}   Fri 10½ h {cross()}',
      f'E: Tue 10.00–5.00 = 7 h {tick()}   Fri 8.30–6.00 = 9½ h {tick()} {ar()} {boxed("E")}')}""",
    ],
    answer_text='E: Tuesday 7 hours (under 7½) and Friday 9½ hours (under 10), so both rates are slightly higher.',
    why={'A': 'Tuesday 8 h and Friday 10½ h are both too long: those rates would come out lower, not higher.',
         'B': 'Friday’s 9½ h works, but Tuesday’s 7½ h gives exactly the normal rate, not a higher one.',
         'C': '7½ h and 10 h give exactly the normal rate on both days.',
         'D': 'Tuesday 8 h and Friday 10½ h: both rates come out lower.'},
    fast='Mon: 4 lines = 10 h, so 1 line = 2.5 h. Tue (3 lines) must be under 7½ h and Fri (4 lines) under 10 h. Only E: 7 h and 9½ h.',
))

# ---------------------------------------------------------------- 20 (Q42)
def _profit():
    vals = [0, -500, 500, 1000, 500, 0, -800]
    nets = [-500, 1000, 500, -500, -500, -800]
    X = lambda n: 60 + n * 82
    Z, s = 170, 0.1
    parts, lab = [], []
    for n, v in enumerate(vals):
        if v:
            top = Z - v * s if v > 0 else Z
            parts.append(rect(X(n), top, 50, abs(v) * s, k='green' if n == 3 else 'ink', fill='g' if v > 0 else 'p', sw=2.6 if n == 3 else 1.6))
        ly = Z - v * s - 8 if v >= 0 else Z - v * s + 20
        lab.append(text(X(n) + 25, ly, f'£{v:,}'.replace('£-', '−£'), k='green' if v > 0 else 'red' if v < 0 else 'ink', size=16))
        lab.append(text(X(n) + 25, 290, n, k='ink', size=16))
    for n, d in enumerate(nets, 1):
        lab.append(text(X(n) + 25, 26, f'{d:+,}'.replace('-', '−'), k='green' if d > 0 else 'red', size=15))
    parts.append(line(40, Z, 630, Z, k='ink', w=2))
    lab += [text(X(3) + 25, Z - 40, 'best', k='green', size=19, font='scrawl'),
            text(330, 312, 'number of applications', k='muted', size=15),
            text(X(0) + 25, 26, 'change:', k='muted', size=14),
            text(X(0) + 25, 46, '(bar − 1000)', k='muted', size=12)]
    return svg(640, 322, rough(*parts) + ''.join(lab),
               'Running profit after 0 to 6 applications: 0, minus 500, 500, 1000, 500, 0, minus 800; the peak is at 3 applications')

Q.append(dict(
    n=20, orig=42, answer='C', topic='Graphs & profit',
    question=f"""<p>The graph below shows the {hl('additional financial value', 'y', 1)} of repeated applications of fertiliser applied to
crops in a field for a year. For example, {hl('two applications gives £2,000 more value to the crop than one application', 'y')}.</p>
{fig(Y, 'ps_q20_graph', 'Bar chart of additional value per application: 1st 500, 2nd 2000, 3rd 1500, 4th 500, 5th 500, 6th about 200', 300)}
<p class="stem">If {hl('each application of fertiliser costs £1,000', 'g', 2)}, how many applications should be made to {hl("maximise the farmer's profit", 'b', 3)}?</p>""",
    options={'A': '0', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'y', 'Each bar is the <b>extra</b> value from that one application, not a running total.'),
           (2, 'g', 'So each application is worth it only if its bar is above £1,000.'),
           (3, 'b', 'Profit = total extra value − total cost. Find the number that makes it biggest.')],
    steps=[
        f"""<p>For each application, extra value − £1,000 cost:</p>
{calc('1st: 500 − 1000 = −500', '2nd: 2000 − 1000 = +1000', '3rd: 1500 − 1000 = +500', '4th: 500 − 1000 = −500', '5th: −500, 6th: about −800')}""",
        f"""<p>Keep a running total of the profit:</p>{_profit()}
{calc(f'0 → −500 → +500 → <b>+1000</b> → +500 → 0 → −800', f'peak after {boxed("3")} applications')}
{note('Don’t stop at 0 just because the first application loses money: the second one more than pays it back.', 'trap')}""",
    ],
    answer_text='3 applications: profit £1,000 (value 500 + 2000 + 1500 = £4,000, cost £3,000).',
    why={'A': '0 applications gives £0 profit, but 3 applications make £1,000.',
         'B': '2 gives £500 profit, but the 3rd adds £1,500 for £1,000, another £500.',
         'D': 'The 4th adds only £500 but costs £1,000: profit drops back to £500.',
         'E': 'After 5 the profit is back down to £0.'},
    fast='Keep adding while the bar beats £1,000: bars 2 and 3 do, bar 4 doesn’t. Running profit −500, +500, +1000, then down. So 3.',
))

# ---------------------------------------------------------------- 21 (Q43)
def _rail():
    X = lambda t: 110 + t * 8
    Yd = lambda d: 270 - d * 6.2
    stations = [('Teovil', 0), ('Gidion', 7), ('Uble', 12), ('Ergen', 19), ('Lowley', 25), ('Aregon', 30), ('Erd', 36)]
    normal = [(0, 0), (7, 7), (10, 7), (15, 12), (18, 12), (25, 19), (28, 19), (34, 25), (37, 25), (42, 30), (45, 30), (51, 36)]
    late = [(15, 12), (37, 12), (42.25, 19), (44.25, 19), (48.75, 25), (50.75, 25), (54.5, 30), (56.5, 30), (61, 36)]
    parts, lab = [], []
    for name, d in stations:
        parts.append(line(X(0), Yd(d), X(64), Yd(d), k='muted', w=1, dash=True))
        lab.append(text(X(0) - 8, Yd(d) + 5, f'{name} ({d})', k='ink', size=15, anchor='end'))
    parts += [poly([(X(t), Yd(d)) for t, d in normal], k='pen', sw=3, closed=False),
              poly([(X(t), Yd(d)) for t, d in late], k='red', sw=3, closed=False),
              line(X(0), 284, X(64), 284, k='ink', w=2, head=True)]
    for t, lbl in ((0, '10.20'), (15, '10.35'), (37, '10.57'), (51, '11.11'), (61, '11.21')):
        parts.append(line(X(t), 278, X(t), 290, k='ink', w=1.6))
        lab.append(text(X(t), 308, lbl, k='ink', size=15))
    lab += [text(X(26), Yd(12) + 22, 'stuck at Uble: 22 min', k='red', size=17, font='scrawl'),
            text(X(31), Yd(26), 'timetable', k='pen', size=17, anchor='end'),
            text(X(50) + 6, Yd(16), 'yesterday:', k='red', size=15, anchor='start'),
            text(X(50) + 6, Yd(16) + 18, '80 km/h, 2-min stops', k='red', size=15, anchor='start'),
            brace(X(51), X(61), Yd(36) - 6, '10 min late', k='red', size=16, down=False),
            text(X(32), 330, 'km from Teovil on the left; flat bits = waiting at a station', k='muted', size=14)]
    return svg(640, 340, rough(*parts) + ''.join(lab),
               'Distance-time graph from Teovil to Erd: the timetable train arrives at 11.11; yesterday’s train waits 22 minutes at Uble, then runs faster with shorter stops and arrives at 11.21')

Q.append(dict(
    n=21, orig=43, answer='C', topic='Timetables & speed',
    question=f"""<p>There is a half-hourly train service that operates along the Rowbina Valley, between Erd and Teovil.
Leaving Erd at 10 and 40 minutes past each hour, trains stop at Aregon, Lowley, Ergen, Uble and
Gidion before arriving at Teovil {hl('51 minutes after departure', 'g', 1)} from Erd. In the opposite direction, trains
leave Teovil at 20 and 50 minutes past each hour, arriving at Erd 51 minutes later.</p>
{fig(Y, 'ps_q21_chart', 'Distances chart in km: Erd to Aregon 6, Aregon to Lowley 5, Lowley to Ergen 6, Ergen to Uble 7, Uble to Gidion 5, Gidion to Teovil 7; Erd to Teovil 36, Erd to Uble 24', 300)}
<p>The trains {hl('normally average a speed of 60 km/h, but this rises to 80 km/h if they are running late', 'y', 2)}.
They {hl('stop for three minutes at each station en route, but this is reduced to two minutes when running late', 'y', 3)}.</p>
<p>Yesterday the 10.20 am train from Teovil {hl('arrived at Uble on time', 'p', 4)}, but because of a technical fault,
{hl('remained at Uble for 22 minutes', 'p', 5)}. There were no further delays.</p>
<p class="stem">How many minutes late was yesterday's 10.20 am train from Teovil {hl('when it arrived at Erd', 'b', 6)}?</p>""",
    options={'A': '5 mins', 'B': '8 mins', 'C': '10 mins', 'D': '13 mins', 'E': '15 mins'},
    notes=[(1, 'g', 'Check: 36 km at 60 km/h = 36 min (1 km a minute!), plus 5 stops × 3 = 15 min. 36 + 15 = 51 ✓'),
           (2, 'y', '80 km/h once late: 3 km takes 2¼ min instead of 3.'),
           (3, 'y', 'And each later stop is 1 minute shorter.'),
           (4, 'p', 'No delay at all before Uble.'),
           (5, 'p', 'A 22-minute stop instead of the usual 3: it leaves <b>19</b> minutes late.'),
           (6, 'b', 'Late leaving Uble, minus the time it claws back on the way to Erd.')],
    steps=[
        f"""<p>Normal times (60 km/h = 1 km per minute). Teovil → Uble is 7 + 5 = 12 km:</p>
{calc(f'10.20 + 12 min running + 3 min at Gidion = arrives Uble <b>10.35</b>', f'normally leaves Uble 10.38 and reaches Erd 10.20 + 51 = <b>11.11</b>')}""",
        f"""<p>Yesterday: it sat at Uble for 22 minutes.</p>
{calc(f'leaves Uble 10.35 + 22 = <b>10.57</b> {ar()} 19 min late', 'Uble → Erd = 24 km at 80 km/h = 24 ÷ 80 × 60 = 18 min',
      'stops at Ergen, Lowley, Aregon: 3 × 2 = 6 min', f'arrives 10.57 + 18 + 6 = <b>11.21</b>')}""",
        f"""{_rail()}
{calc(f'11.21 − 11.11 = {boxed("10 minutes late")}')}
{note('Catch-up = 6 min on speed (24 → 18) + 3 min on stops (9 → 6) = 9 min. 19 − 9 = 10.', 'check')}""",
    ],
    answer_text='10 minutes late: it left Uble 19 minutes late and clawed back 9 minutes.',
    why={'A': '5 uses the faster speed and shorter stops for the whole route from Teovil (saving 14). But it ran normally until Uble.',
         'B': '8 would need 11 minutes of catch-up. The last 24 km can only give 9 (6 from speed, 3 from stops).',
         'D': '13 treats all 22 minutes as delay (forgetting the normal 3-minute stop), or forgets the shorter stops (19 − 6).',
         'E': '15 would mean only 4 minutes clawed back, but the faster running alone saves 6.'},
    fast='Leaves Uble 19 late. Last 24 km: normally 24 + 9 = 33 min, late 18 + 6 = 24 min, saving 9. 19 − 9 = 10.',
))

# ---------------------------------------------------------------- 22 (Q44)
def _church():
    cx, cy, s = 320, 150, 56
    parts = [rect(cx - s / 2, cy - s / 2, s, s, k='ink', fill='paper', sw=2),
             line(cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2, k='ink', w=1.4), line(cx + s / 2, cy - s / 2, cx - s / 2, cy + s / 2, k='ink', w=1.4),
             rect(cx - s / 2, cy - s / 2 - 52, s, 52, k='ink', fill='y', sw=2),
             rect(cx - s / 2, cy + s / 2, s, 140, k='ink', fill='b', sw=2),
             rect(cx - s / 2 - 62, cy - s / 2, 62, s, k='ink', fill='g', sw=2),
             rect(cx + s / 2, cy - s / 2, 62, s, k='ink', fill='o', sw=2),
             line(80, 70, 30, 70, k='ink', head=True, w=2), line(80, 70, 130, 70, k='ink', w=2),
             line(80, 40, 80, 100, k='ink', w=2),
             line(186, 150, 222, 150, k='green', head=True, w=2.2), line(454, 150, 418, 150, k='orange', head=True, w=2.2)]
    lab = [text(20, 75, 'N', k='ink', size=16, anchor='end', font='print'), text(140, 75, 'S', k='ink', size=16, anchor='start', font='print'),
           text(80, 34, 'E', k='ink', size=16, font='print'), text(80, 118, 'W', k='ink', size=16, font='print'),
           text(cx, cy - s / 2 - 62, 'EAST end: stained glass', k='ink', size=16),
           text(cx, cy + s / 2 + 160, 'WEST end: door', k='ink', size=16),
           text(cx, cy + s / 2 + 70, 'long', k='pen', size=15), text(cx, cy + s / 2 + 88, 'nave', k='pen', size=15),
           text(cx - s / 2 - 31, cy - s / 2 - 8, 'north', k='green', size=14), text(cx + s / 2 + 31, cy - s / 2 - 8, 'south', k='orange', size=14),
           eye(166, 150, k='green', facing='right'), eye(474, 150, k='orange', facing='left'),
           text(130, 196, 'from the NORTH:', k='green', size=16), text(130, 216, 'east end on your left,', k='green', size=15),
           text(130, 234, 'long nave on your right', k='green', size=15),
           text(520, 196, 'from the SOUTH:', k='orange', size=16), text(520, 216, 'long nave on your left,', k='orange', size=15),
           text(520, 234, 'east end on your right', k='orange', size=15)]
    return svg(640, 348, rough(*parts) + ''.join(lab),
               'The church plan labelled: east end at the top, long nave to the west at the bottom, north transept left, south transept right; a viewer from the north sees the nave on the right, from the south on the left')

Q.append(dict(
    n=22, orig=44, answer='E', topic='Plans & views',
    question=f"""<p>The diagram below shows a view of a church from above:</p>
{fig(Y, 'ps_q22_plan', 'Compass with North pointing left, East up, South right, West down; the church is a cross with a short arm at the top, a long arm at the bottom and two side arms', 300)}
<p>There are {hl('three windows facing south', 'y', 1)}, {hl('two windows facing north', 'y', 2)} and a {hl('stained glass window facing east', 'y', 3)}. {hl('The only doors are one in the westernmost end and one in a north-facing wall', 'p', 4)}.</p>
<p class="stem">Which one of the following gives a {hl('possible view', 'b', 5)} of the church?</p>
{fig(Y, 'ps_q22_views', 'Five elevation drawings: A view from East with a door in the left wing and a window in the middle; B view from West with no door or window; C view from South with two windows on the long left part; D view from South with one window on the short left part and two on the long right part; E view from North with a window on the short left part and a door and a window on the long right part', 430)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'The south side must show 3 windows.'),
           (2, 'y', 'The north side must show 2 windows (plus a door, see 4).'),
           (3, 'y', 'The east end shows the stained glass.'),
           (4, 'p', 'Doors only on the west end and on a north-facing wall. Nowhere else!'),
           (5, 'b', 'Watch the compass: north points to the <b>left</b> of the plan, east to the top.')],
    steps=[
        f"""<p>Read the plan with its own compass: east is the <b>top</b> (short arm), west is the <b>bottom</b> (long nave),
north is on the left, south on the right. Now stand on each side and look in:</p>{_church()}""",
        f"""<p>Check each view against the rules:</p>
{calc(f'A, from east: a door in an east-facing wall {cross()}', f'B, from west: the west door is missing {cross()}',
      f'C, from south: nave on the left {tick()} but only 2 windows, needs 3 {cross()}',
      f'D, from south: 3 windows, but the long nave is on the right, back to front {cross()}',
      f'E, from north: nave on the right {tick()}, 2 windows {tick()}, door in the north wall {tick()} {ar()} {boxed("E")}')}""",
    ],
    answer_text='View E: from the north, the long nave is on the right, with two windows and the north door.',
    why={'A': 'A shows a door on an east-facing wall. Doors are only at the west end and in a north wall.',
         'B': 'B has no door, but the view from the west must show the west door.',
         'C': 'C has the nave on the correct side but only 2 south windows. There should be 3.',
         'D': 'D has 3 windows, but from the south the long nave (west) must be on your left. D has it on the right: a mirror image.'},
    fast='From the south the long nave is on your left; from the north it is on your right. C has 2 windows, D is flipped, A and B break the door rule. E.',
))

# ---------------------------------------------------------------- 23 (Q48)
def _coins():
    def coin(x, y, k, f, label, r=20):
        return [circle(x, y, r, k=k, fill=f, sw=2)], [text(x, y + 5, label, k='ink', size=14 if r < 22 else 15)]
    parts, lab = [], []
    parts.append(rect(30, 34, 110, 52, k='red', fill='p', sw=2.2, rx=6))
    lab += [text(85, 66, 'red 160K', k='ink', size=17), text(170, 66, '=', k='ink', size=26),
            text(240, 66, 'item 135K', k='ink', size=18), text(304, 66, '+', k='ink', size=24)]
    for i in range(3):
        p, l = coin(340 + i * 46, 60, 'green', 'g', '8K')
        parts += p
        lab += l
    p, l = coin(482, 60, 'pen', 'b', '1K')
    parts += p
    lab += l
    lab.append(text(520, 66, '= 25K change', k='muted', size=15, anchor='start'))
    for i in range(4):
        p, l = coin(50 + i * 46, 150, 'green', 'g', '8K')
        parts += p
        lab += l
    p, l = coin(234, 150, 'pen', 'b', '1K')
    parts += p
    lab += l
    lab += [text(270, 156, '= 32 + 1 = 33K newspaper ✓', k='green', size=18, anchor='start'),
            text(320, 220, 'red note 160K ÷ green 8K = 20 green coins', k='red', size=22, font='scrawl')]
    return svg(640, 240, rough(*parts) + ''.join(lab),
               'Coins: a red 160K note equals a 135K item plus three 8K green coins and one 1K blue coin; four green and one blue make 33K; 160 divided by 8 is 20')

Q.append(dict(
    n=23, orig=48, answer='B', topic='Equations & logic',
    question=f"""<p>When travelling in Kromistan and not understanding the currency, I offered a red note for an item
marked {hl("'135K'. I was given, in change, three green coins and one blue coin", 'g', 1)}. Later, for a newspaper
marked {hl("'33K', I offered a handful of coins and the vendor took four green and one blue", 'g', 2)}. There are
{hl('only these three denominations', 'y', 3)} of money available; {hl("the smallest is marked '1K'", 'y')} and {hl('each higher denomination is a whole number multiple of the lower denominations', 'y', 4)}.</p>
<p class="stem">How many {hl('green coins are worth one red note', 'b', 5)}?</p>""",
    options={'A': '8', 'B': '20', 'C': '29', 'D': '160', 'E': '167'},
    notes=[(1, 'g', 'Red = 135 + 3 green + 1 blue.'),
           (2, 'g', '4 green + 1 blue = 33.'),
           (3, 'y', 'Red, green and blue are the only money, and one of them is worth 1K.'),
           (4, 'y', 'Bigger ones are exact multiples of smaller ones. Use this to test your answer.'),
           (5, 'b', 'Red ÷ green, not the value of either.')],
    steps=[
        f"""<p>The red note pays for a 135K item, so it is the big one. So green or blue is the 1K.</p>
{calc(f'blue = 1: 4 green = 33 − 1 = 32 {ar()} green = <b>8</b>', f'green = 1: blue = 33 − 4 = 29')}""",
        f"""<p>Work out the red note in each case, then test the “whole number multiple” rule:</p>
{calc(f'blue 1, green 8: red = 135 + 3 × 8 + 1 = 160 {ar()} 160 ÷ 8 = 20 {tick()} 160 ÷ 1 {tick()}',
      f'green 1, blue 29: red = 135 + 3 + 29 = 167 {ar()} 167 ÷ 29 = 5.76… {cross()}')}{_coins()}
{calc(f'one red note = {boxed("20")} green coins')}""",
    ],
    answer_text='20: blue is 1K, green 8K and red 160K.',
    why={'A': '8K is the value of one green coin, not how many make a red note.',
         'C': '29 is what blue would be if green were 1K, but then red = 167, which isn’t a multiple of 29.',
         'D': '160 is the red note’s value in K, not a number of green coins.',
         'E': '167 is the red note in the case that fails (green = 1K).'},
    fast='4g + b = 33 with one coin worth 1: b = 1, g = 8. Red = 135 + 24 + 1 = 160 = 20 greens.',
))

# ---------------------------------------------------------------- 24 (Q49)
def _votes():
    parts, lab = [], []
    rows = [(70, 5, 8, 'before: 5 – 8, defeated', 'red'), (184, 7, 6, '2 switch: 7 – 6, carried ✓', 'green')]
    for y, nf, na, cap, kc in rows:
        for i in range(nf):
            moved = y == 184 and i >= 5
            parts.append(circle(40 + i * 26, y, 11, k='orange' if moved else 'green', fill='g', sw=2.6 if moved else 1.8))
        for i in range(na):
            parts.append(circle(240 + i * 26, y, 11, k='red', fill='p', sw=1.8))
        for i in range(10):
            parts.append(circle(452 + i * 19, y, 8, k='muted', fill='paper', sw=1.4))
        lab += [text(40, y + 36, cap, k=kc, size=17, anchor='start', font='scrawl')]
    lab += [text(92, 44, 'for', k='green', size=16), text(332, 44, 'against', k='red', size=16),
            text(538, 44, 'abstain (ignored)', k='muted', size=15)]
    parts += [arrow(240, 84, 170, 168, k='orange', bend=-0.15), arrow(266, 84, 196, 168, k='orange', bend=-0.15)]
    return svg(640, 236, rough(*parts) + ''.join(lab),
               'Counters: 5 for, 8 against and 10 abstaining; two against voters switch to for, giving 7 for and 6 against')

Q.append(dict(
    n=24, orig=49, answer='A', topic='Voting & logic',
    question=f"""<p>At committee meetings of the Massing Social Club motions are carried or defeated by a {hl('simple majority, abstentions being ignored', 'y', 1)}.</p>
<p>At the last meeting a proposal to install a satellite dish was {hl('defeated by 8 votes to 5', 'g', 2)} with {hl('10 committee members abstaining', 'g')}. However, because of the large number of abstentions it was
decided that the matter should be discussed further at the next meeting and a vote taken again.</p>
<p class="stem">What is the {hl('minimum number of committee members who must change the way they voted', 'b', 3)} if the
{hl('result is to be reversed', 'p', 4)} at the next meeting?</p>""",
    options={'A': '2', 'B': '4', 'C': '7', 'D': '8', 'E': '12'},
    notes=[(1, 'y', 'More votes for than against wins. Abstainers don’t count either way.'),
           (2, 'g', '5 for, 8 against: “for” is 3 behind.'),
           (3, 'b', 'Find the cheapest way to make “for” win.'),
           (4, 'p', 'Reversed = carried. “For” must be <b>more</b> than “against”: a tie isn’t enough.')],
    steps=[
        f"""<p>One person switching from against to for moves the gap by <b>2</b> (one less against, one more for).</p>
{calc(f'now: 5 for, 8 against (gap 3)', f'1 switch: 6 for, 7 against {ar()} still defeated {cross()}',
      f'2 switches: 7 for, 6 against {ar()} carried {tick()}')}{_votes()}""",
        f"""<p>Could abstainers do it with fewer? Each abstainer who votes for only closes the gap by 1:
5 + 4 = 9 against 8 needs <b>4</b> people. Switching is quicker {ar()} {boxed("2")}</p>""",
    ],
    answer_text='2: two members switch from against to for, making it 7 to 6.',
    why={'B': '4 abstainers voting for (9 to 8) works too, but switching voters closes the gap twice as fast.',
         'C': '7 would be needed only if “for” had to reach 12, a majority of all 23 members. Abstentions are ignored.',
         'D': '8 is everyone who voted against: far more than needed.',
         'E': '12 is a majority of all 23 members, not the number who have to change.'},
    fast='Gap is 3. Each switch from against to for closes it by 2. Two switches: 7–6.',
))

# ---------------------------------------------------------------- 25 (Q50)
def _street():
    n, w, x0 = 15, 36, 50
    parts, lab = [], []
    def house(x, y, num, f):
        parts.append(rect(x + 2, y, w - 4, 30, k='ink', fill=f, sw=1.4))
        lab.append(text(x + w / 2, y + 21, num, k='ink', size=14, font='print'))
    # street 1: up one side, back down the other
    for i in range(n):
        top, bot = 1 + i, 2 * n - i
        house(x0 + i * w, 36, top, 'g' if top == 6 else 'paper')
        house(x0 + i * w, 98, bot, 'y' if bot == 25 else 'b' if bot in (24, 26) else 'paper')
    parts += [line(x0, 72, x0 + n * w, 72, k='muted', w=1.2), line(x0, 92, x0 + n * w, 92, k='muted', w=1.2),
              line(x0 + 40, 82, x0 + n * w - 40, 82, k='pen', head=True, w=1.8, dash=True)]
    lab += [text(x0, 26, 'Up-and-back street (15 a side): 1 → 15, then 16 → 30 coming back', k='pen', size=16, anchor='start'),
            text(x0, 152, 'opposite 25 is 31 − 25 = 6 (changes with the length); next door: 24 and 26', k='ink', size=15, anchor='start')]
    # street 2: odds and evens
    for i in range(n):
        odd, even = 2 * i + 1, 2 * i + 2
        house(x0 + i * w, 200, odd, 'y' if odd == 25 else 'b' if odd in (23, 27) else 'paper')
        house(x0 + i * w, 262, even, 'g' if even == 26 else 'paper')
    parts += [line(x0, 236, x0 + n * w, 236, k='muted', w=1.2), line(x0, 256, x0 + n * w, 256, k='muted', w=1.2)]
    lab += [text(x0, 190, 'Odds-and-evens street: odds on one side, evens opposite', k='pen', size=16, anchor='start'),
            text(x0, 316, 'opposite 25 is always 26 (any length); next door: 23 and 27', k='ink', size=15, anchor='start')]
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'Two streets: numbered up and back, where 25 faces 6 and has neighbours 24 and 26; numbered odds and evens, where 25 faces 26 and has neighbours 23 and 27')

Q.append(dict(
    n=25, orig=50, answer='E', topic='Logic & numbering',
    question=f"""<p>The housing estate on which Andrew lives has streets of variable length. In each street the houses
are {hl('directly opposite each other, with the same number of houses on each side', 'y', 1)}. However, the
numbering of the houses is inconsistent.</p>
<p>Some streets are {hl('numbered consecutively on each side, starting at one end of the street, going up to the end and then back down the other side', 'y', 2)}.</p>
<p>Other streets have {hl('the odd numbers on one side, starting from 1, and the evens on the other side, starting with 2 at the same end', 'y', 3)}.</p>
<p>Andrew's friend Amy lives on the same estate at 25 Acacia Avenue, {hl('which is not the end house in the street', 'p', 4)}.</p>
<p class="stem">If Andrew {hl("knows the number of the house opposite Amy's", 'g', 5)}, which one of the following statements is
{hl('definitely true', 'b', 6)}?</p>""",
    options={'A': 'He knows the exact number of houses in the street.',
             'B': 'He knows that the number of houses in the street is one of two numbers.',
             'C': "If the house opposite Amy's is 26, he knows the number of houses in the street.",
             'D': 'If he knows the number of the house next door to Amy, he can work out the number of houses in the street.',
             'E': "He knows the numbers of the houses immediately adjoining Amy's."},
    notes=[(1, 'y', 'Same number of houses each side, so a street has an even number of houses.'),
           (2, 'y', 'System 1 (up and back). With n a side, house k faces house 2n + 1 − k.'),
           (3, 'y', 'System 2 (odds and evens). House 25 always faces 26.'),
           (4, 'p', 'This rules out one sneaky case (see step 2).'),
           (5, 'g', 'He knows the opposite number, but not which system the street uses.'),
           (6, 'b', 'Must be true whatever the opposite number turns out to be.')],
    steps=[
        f"""<p>Sketch both kinds of street with Amy at 25:</p>{_street()}""",
        f"""<p>What does the opposite number tell Andrew?</p>
{calc(f'opposite is <b>not 26</b> {ar()} must be up-and-back {ar()} next door are <b>24 and 26</b>',
      f'opposite <b>is 26</b> {ar()} up-and-back would need 2n + 1 − 25 = 26, so n = 25 and Amy is the last house on her side: an end house!',
      f'Amy isn’t at the end {ar()} so it is odds-and-evens {ar()} next door are <b>23 and 27</b>')}
<p>Either way he knows her neighbours {ar()} {boxed('E')}</p>""",
        f"""{note('A and B fail when the opposite house is 26: an odds-and-evens street can be any length (28, 30, 32… houses). C says the opposite of the truth, and D fails for the same street because 23 and 27 are next door whatever its length.', 'check')}""",
    ],
    answer_text='E: opposite not 26 means neighbours 24 and 26; opposite 26 means odds-and-evens, so neighbours 23 and 27.',
    why={'A': 'Not if the opposite house is 26: then it is an odds-and-evens street, which could be any length.',
         'B': 'Same problem: with 26 opposite, the street could have 28, 30, 32… houses, far more than two choices.',
         'C': 'Backwards: 26 opposite means odds-and-evens numbering, which tells you nothing about the length.',
         'D': 'In an odds-and-evens street, next door is 23 and 27 whatever the length, so it doesn’t help.'},
    fast='Opposite not 26 → up-and-back → neighbours 24, 26. Opposite 26 → (up-and-back would make Amy an end house) → odds-and-evens → 23, 27. Either way he knows.',
))
