import math
from wslib import *

Y = 2008
Q = []


# ---------------------------------------------------------------- 9 (Q19)
Q9_DATA = [('Belgium', '−2.6', '−2.5', '8.9', '10.6'), ('Canada', '6.9', '5.4', '9.6', '11.2'),
           ('France', '4.7', '−4.3', '12.7', '12.1'), ('Germany', '5.5', '−4.0', '9.1', '9.0'),
           ('Italy', '7.3', '−1.3', '12.5', '10.7'), ('Japan', '5.9', '−3.2', '2.9', '2.8'),
           ('Netherlands', '1.2', '2.4', '9.6', '8.4'), ('Spain', '4.9', '−6.8', '24.1', '22.1'),
           ('Sweden', '8.2', '−1.8', '8.1', '8.7'), ('UK', '4.2', '3.3', '8.8', '10.0'),
           ('USA', '5.7', '3.4', '5.4', '6.4')]


def _q9_table():
    body = ''
    for name, a, b, c, d in Q9_DATA:
        if name == 'UK':
            cells = [hl('UK', 'g'), hl(a, 'g'), b, hl(c, 'g'), hl(d, 'g')]
        else:
            cells = [name, a, b, c, d]
        body += '<tr>' + ''.join(f'<td>{x}</td>' for x in cells) + '</tr>'
    head = ('<thead><tr><th rowspan="2"></th><th colspan="2"><i>INDUSTRIAL PRODUCTION</i><br>Annual Change %</th>'
            '<th colspan="2"><i>UNEMPLOYMENT</i><br>Rate %</th></tr>'
            '<tr><th>Latest</th><th>Year ago</th><th>Latest</th><th>Year ago</th></tr></thead>')
    return f'<div class="tbl-wrap"><table class="ptable">{head}<tbody>{body}</tbody></table></div>'


def _quadrant():
    X = lambda v: 70 + (v + 4) * 40
    Yf = lambda f: 190 - f * 60
    parts = [rect(X(4.2), Yf(2.2), X(9.3) - X(4.2), Yf(1.2) - Yf(2.2), k='green', fill='g', sw=1.6),
             line(X(-4), Yf(0), X(9.3), Yf(0), k='ink', w=1.8, head=True),
             line(X(0), Yf(-2.5), X(0), Yf(2.3), k='ink', w=1.8, head=True),
             line(X(4.2), Yf(-2.5), X(4.2), Yf(2.2), k='red', w=1.8, dash=True),
             line(X(-4), Yf(1.2), X(9.3), Yf(1.2), k='red', w=1.8, dash=True)]
    lab = []
    for v in (-4, 4, 8):
        lab.append(text(X(v), Yf(0) + 20, v, k='muted', size=14))
    for f in (-2, -1, 1, 2):
        parts.append(line(X(0) - 5, Yf(f), X(0) + 5, Yf(f), k='ink', w=1.4))
        lab.append(text(X(0) - 9, Yf(f) + 5, f, k='muted', size=14, anchor='end'))
    pts = [('Belgium', -2.6, 1.7, 0, -12, 'middle'), ('France', 4.7, -0.6, 12, 5, 'start'),
           ('Italy', 7.3, -1.8, 12, 5, 'start'), ('USA', 5.7, 1.0, 12, 18, 'start')]
    for name, v, f, dx, dy, anc in pts:
        parts.append(circle(X(v), Yf(f), 6, k='ink', fill='paper', sw=2))
        lab.append(text(X(v) + dx, Yf(f) + dy, name, k='ink', size=16, anchor=anc))
    parts.append(circle(X(6.9), Yf(1.6), 7, k='green', fill='g', sw=2.6))
    parts.append(circle(X(4.2), Yf(1.2), 7, k='red', fill='p', sw=2.4))
    lab += [text(X(6.9) + 12, Yf(1.6) + 6, 'Canada ✓', k='green', size=18, font='scrawl', anchor='start'),
            text(X(4.2) - 12, Yf(1.2) - 10, 'UK', k='red', size=18, anchor='end'),
            text(X(6.75), Yf(2.2) - 8, 'beats the UK on both', k='green', size=16),
            text(135, Yf(-1.6), 'below 0 =', k='muted', size=15), text(135, Yf(-1.6) + 18, 'unemployment rose', k='muted', size=15),
            text(330, 372, 'industrial production change, latest (%) →', k='ink', size=16),
            text(26, 200, 'fall in unemployment →', k='ink', size=16, rotate=-90)]
    return svg(640, 384, rough(*parts) + ''.join(lab),
               'Scatter of the five options against the UK: only Canada has both a bigger production rise and a bigger fall in unemployment')

Q.append(dict(
    n=9, orig=19, answer='B', topic='Tables',
    question=f"""<p>The table below shows the unemployment rate and percent change in industrial
production over the last year for several countries.</p>
{_q9_table()}
<p class="stem">Which country has had a {hl('larger percentage increase in industrial production', 'y', 1)} and {hl('greater fall in the percentage unemployed', 'y', 2)} {hl('than the UK', 'b', 3)} {hl('over the last year', 'p', 4)}?</p>""",
    options={'A': 'Belgium', 'B': 'Canada', 'C': 'France', 'D': 'Italy', 'E': 'USA'},
    notes=[(1, 'y', 'Test 1: the “Latest” annual change must beat the UK’s 4.2.'),
           (2, 'y', 'Test 2: unemployment must have <b>fallen</b> (year ago → latest) by more than the UK’s fall.'),
           (3, 'b', 'Both tests, compared with the UK row.'),
           (4, 'p', 'Production: use the Latest column only (that already is the change over the last year). Unemployment: compare the two columns.')],
    steps=[
        f"""<p>Get the UK’s two numbers first:</p>
{calc('production: up <b>4.2%</b>', f'unemployment: 10.0 → 8.8 {ar()} fell by <b>1.2</b>')}""",
        f"""<p>Test the five options. Both must pass:</p>
{calc(f'Belgium: −2.6 {cross()} (production went down)',
      f'Canada: 6.9 {tick()} and 11.2 → 9.6, a fall of 1.6 {tick()}',
      f'France: 4.7 {tick()} but 12.1 → 12.7, it <b>rose</b> {cross()}',
      f'Italy: 7.3 {tick()} but 10.7 → 12.5, it <b>rose</b> {cross()}',
      f'USA: 5.7 {tick()} but 6.4 → 5.4, a fall of only 1.0 {cross()}')}""",
        f"""<p>Plot it: across = production, up = fall in unemployment. Only one country lands in the top-right box:</p>
{_quadrant()}{calc(f'answer = {boxed("Canada")}')}""",
    ],
    answer_text='Canada: production up 6.9% (UK 4.2%) and unemployment down 1.6 points (UK 1.2).',
    why={'A': 'Belgium’s unemployment fell a lot (1.7), but its industrial production <b>fell</b> by 2.6%.',
         'C': 'France’s production rose 4.7%, but its unemployment went <b>up</b> (12.1 → 12.7).',
         'D': 'Italy has a big production rise (7.3%), but unemployment went up (10.7 → 12.5). Read the columns the right way round.',
         'E': 'The USA passes on production, but its unemployment fell by 1.0, less than the UK’s 1.2.'},
    fast='UK: 4.2 and a fall of 1.2. Only Canada beats both (6.9 and a fall of 1.6).',
))


# ---------------------------------------------------------------- 10 (Q20)
def _map():
    X = lambda e: 160 + e * 10
    Yn = lambda n: 220 - n * 10
    parts, lab = [], []
    for e in range(-5, 16, 5):
        parts.append(line(X(e), Yn(-10), X(e), Yn(20), k='muted', w=1, dash=True))
    for n in range(-10, 21, 5):
        parts.append(line(X(-5), Yn(n), X(15), Yn(n), k='muted', w=1, dash=True))
    ahmed = [(5, 15), (0, 15), (0, 0), (5, 0)]
    wayne = [(0, 0), (0, -5), (10, -5), (10, 10)]
    best = [(5, 0), (5, 10), (10, 10)]
    for route, k, w, d in ((ahmed, 'pen', 3, False), (wayne, 'orange', 3, False), (best, 'green', 4, True)):
        for (e1, n1), (e2, n2) in zip(route, route[1:]):
            parts.append(line(X(e1), Yn(n1), X(e2), Yn(n2), k=k, w=w, dash=d))
    for name, (e, n), dx, dy, anc in (('A', (5, 15), 12, -6, 'start'), ('B', (0, 0), -12, -6, 'end'),
                                      ('C', (5, 0), 10, 20, 'start'), ('D', (0, -5), -12, 18, 'end'),
                                      ('E', (10, 10), 12, -6, 'start')):
        parts.append(circle(X(e), Yn(n), 7, k='ink', fill='paper', sw=2.2))
        lab.append(text(X(e) + dx, Yn(n) + dy, name, k='ink', size=19, font='print', weight='700', anchor=anc))
    lab += [text(X(5) - 8, Yn(5) + 5, '10', k='green', size=17, anchor='end'),
            text(X(7.5), Yn(10) - 8, '5', k='green', size=17),
            text(X(-5), 14, 'N ↑   one square = 5 km', k='muted', size=15, anchor='start')]
    tx = 350
    lab += [text(tx, 50, 'A Abbeytown, B Barneyville', k='ink', size=16, anchor='start'),
            text(tx, 72, 'C Carloston, D Denburgh, E Easterby', k='ink', size=16, anchor='start'),
            text(tx, 112, 'Ahmed: A → B → C, ends at C', k='pen', size=17, anchor='start'),
            text(tx, 140, 'Wayne: B → D → E, ends at E', k='orange', size=17, anchor='start'),
            text(tx, 186, 'C to E on the roads:', k='green', size=18, anchor='start'),
            text(tx, 210, '10 km north + 5 km east', k='green', size=18, anchor='start'),
            text(tx, 250, '= 15 km', k='green', size=30, font='scrawl', anchor='start')]
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'Grid map: Ahmed drives A to B to C, Wayne drives B to D to E; the shortest road route from C to E is 10 km north and 5 km east')

Q.append(dict(
    n=10, orig=20, answer='B', topic='Maps & routes',
    question=f"""<p>The roads on Bolandia all run {hl('either north - south or east - west', 'y', 1)} and are laid out on a 5km
grid. Ahmed and Wayne are delivery drivers. One morning, {hl('Ahmed starts at Abbeytown and drives 5km west then 15km south to reach Barneyville. He then drives 5km east to Carloston', 'g', 2)}. {hl('Wayne started at Barneyville, drove 5km south to Denburgh then 10km east and 15km north to Easterby', 'g', 3)}. Ahmed then rings Wayne to arrange to meet for lunch.</p>
<p class="stem">If {hl('one of them stays where he is', 'p', 4)}, what is the {hl('minimum distance', 'b', 5)} the other must drive to
meet him?</p>""",
    options={'A': '10 km', 'B': '15 km', 'C': '25 km', 'D': '30 km', 'E': '35 km'},
    notes=[(1, 'y', 'No diagonal shortcuts: road distance = east–west part + north–south part.'),
           (2, 'g', 'Ahmed finishes at Carloston.'),
           (3, 'g', 'Wayne finishes at Easterby. Both trips pass through Barneyville, so measure from there.'),
           (4, 'p', 'Only where they are <b>now</b> matters, not how far they have already driven.'),
           (5, 'b', 'Shortest road route from Carloston to Easterby.')],
    steps=[
        f"""<p>Put Barneyville at the centre and track each driver (E = east, N = north):</p>
{calc(f'Carloston: Barneyville + 5 E {ar()} <b>5 E, 0 N</b>',
      f'Easterby: 5 S, then 10 E, then 15 N {ar()} <b>10 E, 10 N</b>')}""",
        f"""{_map()}""",
        f"""{calc(f'east: 10 − 5 = 5 km', f'north: 10 − 0 = 10 km', f'shortest = 5 + 10 = {boxed("15 km")}')}""",
    ],
    answer_text='15 km: Easterby is 5 km east and 10 km north of Carloston.',
    why={'A': '10 km is only the north–south part. It forgets the 5 km east.',
         'C': '25 km is Ahmed’s whole morning drive (5 + 15 + 5), not the gap between them.',
         'D': '30 km is Wayne’s whole morning drive (5 + 10 + 15).',
         'E': '35 km retraces Wayne’s route back to Barneyville and on to Carloston (30 + 5). Far from the shortest.'},
    fast='From Barneyville: Carloston is (5 E, 0) and Easterby is (10 E, 10 N). Gap = 5 + 10 = 15 km.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _shows():
    days = 'MTWTFSS'
    per = [1, 1, 2, 2, 1, 2, 0]
    cw, ch, x0, y0 = 56, 44, 14, 34
    parts, lab = [], []
    for i, d in enumerate(days):
        lab.append(text(x0 + cw * i + cw / 2, 24, d, k='muted', size=17))
    for day in range(1, 32):
        idx = day - 1 + 2
        wd, wk = idx % 7, idx // 7
        x, y = x0 + cw * wd, y0 + ch * wk
        n = per[wd]
        fill = {2: 'g', 1: 'b', 0: 'none'}[n]
        extra = day >= 29
        parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='red' if extra else 'ink', fill=fill, sw=2.8 if extra else 1.4))
        lab.append(text(x + 7, y + 18, day, k='ink', size=14, anchor='start', font='print'))
        lab.append(text(x + cw - 12, y + ch - 9, n if n else '–', k='pen' if n else 'muted', size=20, font='scrawl'))
    tx = x0 + 7 * cw + 22
    lab += [text(tx, 50, 'a full week = 9 shows', k='ink', size=18, anchor='start'),
            text(tx, 72, '(6 evenings + 3 matinees)', k='muted', size=15, anchor='start'),
            text(tx, 110, 'days 1–28: 4 × 9 = 36', k='pen', size=18, anchor='start'),
            text(tx, 150, 'days 29–31 (red):', k='red', size=18, anchor='start'),
            text(tx, 172, 'Wed + Thu + Fri', k='red', size=18, anchor='start'),
            text(tx, 194, '= 2 + 2 + 1 = 5', k='red', size=18, anchor='start'),
            text(tx, 240, 'total 41', k='green', size=28, font='scrawl', anchor='start')]
    return svg(680, y0 + ch * 5 + 14, rough(*parts) + ''.join(lab),
               'A 31-day month starting on Wednesday, each day showing its number of performances; the extra days 29 to 31 are Wednesday to Friday')

Q.append(dict(
    n=11, orig=24, answer='D', topic='Calendars',
    question=f"""<p>A long-running play in London's West End is performed {hl('every evening except Sunday', 'y', 1)}. In
addition, there are {hl('matinee performances every Wednesday, Thursday and Saturday', 'y', 2)}.</p>
<p class="stem">What is the {hl('maximum', 'b', 3)} number of performances that can be given during a {hl('calendar month of 31 days', 'g', 4)}?</p>""",
    options={'A': '36', 'B': '38', 'C': '39', 'D': '41', 'E': '42'},
    notes=[(1, 'y', '6 evening shows a week (Monday to Saturday).'),
           (2, 'y', 'Wednesday, Thursday and Saturday have <b>2</b> shows; Sunday has none.'),
           (3, 'b', 'We get to choose which day the month starts on.'),
           (4, 'g', '31 days = 4 full weeks + 3 extra days, and the 3 extra days come <b>in a row</b>.')],
    steps=[
        f"""{calc('one week: 6 evenings + 3 matinees = 9 shows', '4 full weeks (28 days): 4 × 9 = <b>36</b>')}""",
        f"""<p>Shows per day: Mon 1, Tue 1, Wed 2, Thu 2, Fri 1, Sat 2, Sun 0. Find the best 3 days <b>in a row</b>:</p>
{calc('Tue + Wed + Thu = 1 + 2 + 2 = 5', 'Wed + Thu + Fri = 2 + 2 + 1 = 5', 'Thu + Fri + Sat = 2 + 1 + 2 = 5',
      f'Fri + Sat + Sun = 3, Sat + Sun + Mon = 3 … {ar()} best is <b>5</b>')}
{note('Three 2-show days (Wed, Thu, Sat) would give 6, but they are not next to each other: Friday is in the way.', 'trap')}""",
        f"""<p>Start the month on a Wednesday, for example:</p>{_shows()}
{calc(f'36 + 5 = {boxed("41")}')}""",
    ],
    answer_text='41: four full weeks give 36, and the best 3 extra days in a row add 5.',
    why={'A': '36 is just the 4 full weeks. It forgets the 3 extra days.',
         'B': '38 is what you get with the worst extra days (Sun, Mon, Tue: 0 + 1 + 1). We want the maximum.',
         'C': '39 counts only an evening show on each extra day (36 + 3), missing the matinees.',
         'E': '42 gives each of the 3 extra days two shows (Wed, Thu, Sat), but those days aren’t in a row.'},
    fast='4 × 9 = 36. The best 3 days in a row (e.g. Wed–Fri) add 2 + 2 + 1 = 5. Total 41.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _workers():
    tasks = [('foundations', 1, 6, 1, 'y'), ('brickwork', 5, 13, 2, 'o'), ('roof', 10, 25, 1, 'b'),
             ('glass', 12, 21, 1, 'g'), ('decorate', 20, 27, 1, 'v')]
    X = lambda d: 44 + (d - 1) * 20
    u, base = 34, 214
    parts, lab = [], []
    for d in range(1, 29):
        h = 0
        for name, a, b, men, f in tasks:
            if a <= d <= b:
                for _ in range(men):
                    parts.append(rect(X(d), base - (h + 1) * u, 18, u, k='ink', fill=f, sw=1.2))
                    h += 1
    parts.append(line(36, base, X(28) + 24, base, k='ink', w=2))
    for d in (1, 5, 10, 12, 13, 15, 20, 25, 28):
        lab.append(text(X(d) + 9, base + 18, d, k='red' if d in (12, 13) else 'muted', size=14))
    for m in range(1, 5):
        lab.append(text(30, base - m * u + 6, m, k='muted', size=14, anchor='end'))
    for i, (name, a, b, men, f) in enumerate(tasks):
        x = 44 + i * 118
        parts.append(rect(x, 14, 16, 16, k='ink', fill=f, sw=1.2))
        lab.append(text(x + 22, 28, name, k='ink', size=15, anchor='start'))
    lab += [text(X(12.5) + 9, base - 4 * u - 26, '4 men on days 12 and 13', k='red', size=17, font='scrawl'),
            text(330, base + 44, 'days of April', k='muted', size=14),
            text(330, base + 72, 'squares: 6 + 18 + 16 + 10 + 8 = 58', k='green', size=19)]
    return svg(640, base + 86, rough(*parts) + ''.join(lab),
               'Stacked chart of workers on site each day of April; the tallest stack is 4 men on days 12 and 13; there are 58 squares in total')

Q.append(dict(
    n=12, orig=25, answer='D', topic='Charts & schedules',
    question=f"""<p>Peter is having a large conservatory built at the back of his house. Below is a plan of the
project, showing when each part of the conservatory is to be built.</p>
{fig(Y, 'ps_q12_plan', 'Bar chart on a grid of April days: prepare foundations, brickwork (two squares tall), roof, glass and decorate', 520)}
<p>{hl('Each blocked square on the plan represents one man for one day', 'y', 1)}.</p>
<p class="stem">How many {hl('days labour', 'b', 2)} will Peter have to pay for, and what is the {hl('maximum number of workers on site at the same time', 'b', 3)}?</p>""",
    options={'A': '48 and 3', 'B': '48 and 4', 'C': '58 and 3', 'D': '58 and 4', 'E': '58 and 6'},
    notes=[(1, 'y', 'Count squares, not bars. The brickwork bar is <b>2 squares tall</b>: 2 men every day.'),
           (2, 'b', 'Total squares = total man-days.'),
           (3, 'b', 'The tallest pile of squares on any one day.')],
    steps=[
        f"""<p>Count each bar: days long × men tall.</p>
{calc('foundations: 6 days × 1 = 6 (days 1–6)', 'brickwork: 9 days × <b>2</b> = 18 (days 5–13)',
      'roof: 16 days × 1 = 16 (days 10–25)', 'glass: 10 days × 1 = 10 (days 12–21)',
      'decorate: 8 days × 1 = 8 (days 20–27)', f'total = 6 + 18 + 16 + 10 + 8 = <b>58</b>')}
{note('Count along the grid lines, or read the start and end days and do end − start + 1. For the roof, 25 − 10 + 1 = 16.', 'tip')}""",
        f"""<p>Now stack the jobs day by day to find the busiest day:</p>{_workers()}
{calc(f'days 12–13: brickwork 2 + roof 1 + glass 1 = <b>4</b>')}""",
        f"""{calc(f'answer = {boxed("58 and 4")}')}""",
    ],
    answer_text='58 man-days, with at most 4 workers on site (days 12 and 13).',
    why={'A': '48 is 10 short (as if a whole job like the glass was missed), and 3 forgets the brickwork has 2 men.',
         'B': 'The 4 is right, but 48 is 10 squares short of the true total of 58.',
         'C': 'The 58 is right, but 3 counts the brickwork as one man. On days 12–13 there are 2 + 1 + 1 = 4.',
         'E': '6 adds up every row of the chart (1 + 2 + 1 + 1 + 1), as if every job ran on the same day. They don’t all overlap.'},
    fast='Squares: 6 + 18 + 16 + 10 + 8 = 58. Busiest: brickwork (2) + roof + glass overlap on days 12–13 = 4.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _bend(kind, corner, x, y, t, k='ink', w=9):
    kx = x + (t if 'R' in corner else 0)
    ky = y + (t if 'B' in corner else 0)
    m1 = (kx, y + t / 2)
    m2 = (x + t / 2, ky)
    if kind == 'square':
        return path(f'M{m1[0]} {m1[1]} L{x + t / 2} {y + t / 2} L{m2[0]} {m2[1]}', k=k, sw=w)
    a1 = math.degrees(math.atan2(m1[1] - ky, m1[0] - kx))
    a2 = math.degrees(math.atan2(m2[1] - ky, m2[0] - kx))
    sweep = 1 if round((a2 - a1) % 360) == 90 else 0
    r = t / 2
    return path(f'M{m1[0]} {m1[1]} A{r} {r} 0 0 {sweep} {m2[0]} {m2[1]}', k=k, sw=w)


B_TILES = {(0, 0): [('round', 'TL'), ('square', 'BR')], (0, 1): [('square', 'BL'), ('round', 'TR')],
           (0, 2): [('square', 'TL'), ('round', 'BR')], (1, 0): [('round', 'TR'), ('round', 'BL')],
           (1, 1): [('round', 'TL'), ('round', 'BR')], (1, 2): [('square', 'BL'), ('round', 'TR')],
           (2, 0): [('round', 'TL'), ('round', 'BR')], (2, 1): [('round', 'BL'), ('round', 'TR')],
           (2, 2): [('square', 'TL'), ('round', 'BR')]}


def _tiles():
    parts = [rect(30, 60, 140, 140, k='ink', fill='paper', sw=2),
             _bend('square', 'TL', 30, 60, 140, w=16), _bend('round', 'BR', 30, 60, 140, w=16)]
    lab = [text(100, 40, 'one tile', k='ink', size=18, font='scrawl'),
           text(100, 226, 'square bend in one corner,', k='pen', size=15),
           text(100, 246, 'round bend in the opposite one', k='pen', size=15)]
    t, x0, y0 = 70, 270, 50
    for (r, c), bends in B_TILES.items():
        bad = all(b[0] == 'round' for b in bends)
        x, y = x0 + c * t, y0 + r * t
        parts.append(rect(x, y, t, t, k='red' if bad else 'green', fill='p' if bad else 'g', sw=1.6))
    for (r, c), bends in B_TILES.items():
        for kind, corner in bends:
            parts.append(_bend(kind, corner, x0 + c * t, y0 + r * t, t))
    lab += [text(x0 + 105, 36, 'pattern B, cut into 9 tiles', k='ink', size=17),
            text(500, 90, 'pink tiles have', k='red', size=17, anchor='start'),
            text(500, 112, 'TWO round bends', k='red', size=17, anchor='start'),
            text(500, 134, 'and no square one ✗', k='red', size=17, anchor='start'),
            text(500, 186, 'count: 5 square,', k='ink', size=17, anchor='start'),
            text(500, 208, '13 round bends', k='ink', size=17, anchor='start'),
            text(500, 236, '9 tiles need 9 of each', k='green', size=17, anchor='start')]
    return svg(680, 270, rough(*parts) + ''.join(lab),
               'One tile with a square bend and a round bend in opposite corners; pattern B redrawn as nine tiles, four of which would need two round bends')

Q.append(dict(
    n=13, orig=26, answer='B', topic='Patterns & tiles',
    question=f"""<p>The design of a tile for a bathroom wall is shown below:</p>
{fig(Y, 'ps_q13_tile', 'Square tile: a thick square-cornered bend around the top-left corner and a thick curved bend around the bottom-right corner', 80)}
<p class="stem">Which of the following patterns may {hl('<b>NOT</b>', 'b', 1)} be made using {hl('only a number of identical tiles', 'y', 2)}
as shown?</p>
{fig(Y, 'ps_q13_opts', 'Five patterns A to E, each made of thick black square and curved bends', 400)}""",
    options={'A': 'pattern A', 'B': 'pattern B', 'C': 'pattern C', 'D': 'pattern D', 'E': 'pattern E'},
    notes=[(1, 'b', 'Four patterns can be made; find the impossible one.'),
           (2, 'y', 'Every tile is the same, so you can only turn it round. However you turn it, it has <b>one square bend and one round bend</b>, in opposite corners.')],
    steps=[
        f"""<p>Each pattern is a 3 × 3 block of tiles. The key fact about one tile:</p>{_tiles()}""",
        f"""<p>Check each tile in each pattern: does it have one square and one round bend in opposite corners?</p>
{calc(f'A: every tile the same way round {tick()}', f'C, D, E: each tile has one of each {tick()}',
      f'B: the middle-left tile has a round bend (bottom of the “D”) <b>and</b> a round bend (top of the bracket) {cross()}')}""",
        f"""{note('Quick check without splitting: 9 tiles always give 9 square bends and 9 round bends. Pattern B only has 5 square bends (2 in each “D” and 1 at the top right).', 'tip')}
{calc(f'answer = {boxed("B")}')}""",
    ],
    answer_text='Pattern B: several of its tiles would need two round bends, but every tile has one square and one round bend.',
    why={'A': 'A is every tile turned the same way.',
         'C': 'C works: each tile is turned so it still has one square and one round bend.',
         'D': 'D works: the circle uses four round bends and the square uses four square bends, from eight different tiles.',
         'E': 'E works: every tile has one square and one round bend.'},
    fast='Every tile = 1 square + 1 round bend. In B the “D” shapes and brackets leave tiles with two round bends (only 5 square bends for 9 tiles).',
))


# ---------------------------------------------------------------- 14 (Q30)
def _bricks():
    parts = []
    for i in range(4):
        parts.append(rect(70, 40 + i * 60, 30, 60, k='ink', fill='b', sw=1.6))
    parts += [rect(100, 40, 30, 30, k='ink', fill='o', sw=1.6)]
    for i in range(3):
        parts.append(rect(100, 70 + i * 60, 30, 60, k='ink', fill='b', sw=1.6))
    parts += [rect(100, 250, 30, 30, k='ink', fill='o', sw=1.6),
              rect(290, 110, 30, 30, k='ink', fill='o', sw=1.6), rect(290, 140, 30, 30, k='ink', fill='o', sw=1.6),
              line(280, 140, 330, 140, k='red', w=2.4, dash=True),
              arrow(136, 55, 284, 120, k='orange', bend=-0.1), arrow(136, 265, 284, 160, k='orange', bend=0.1)]
    lab = [text(100, 26, 'an 80 cm strip, 2 columns', k='ink', size=15),
           text(62, 166, '4 bricks', k='pen', size=16, anchor='end'),
           text(100, 304, '½ + 3 + ½ = 4', k='orange', size=16),
           text(305, 198, 'one brick cut', k='orange', size=15),
           text(305, 216, 'in two: no waste', k='orange', size=15),
           text(400, 70, 'Every 10 cm-wide column', k='ink', size=17, anchor='start'),
           text(400, 92, 'of the 400 cm drive:', k='ink', size=17, anchor='start'),
           text(400, 124, '400 ÷ 20 = 20 bricks', k='pen', size=18, anchor='start'),
           text(400, 164, '550 ÷ 10 = 55 columns', k='pen', size=18, anchor='start'),
           text(400, 214, '55 × 20 = 1100', k='green', size=28, font='scrawl', anchor='start')]
    return svg(640, 316, rough(*parts) + ''.join(lab),
               'Two columns of bricks: a straight column of 4 and a staggered column of half, 3 and half; the two halves come from one brick, so every column uses the same number')

Q.append(dict(
    n=14, orig=30, answer='B', topic='Area',
    question=f"""<p>I am resurfacing my driveway using bricks in the pattern shown below. The visible part of
the brick measures {hl('10cm by 20cm', 'g', 1)}. To achieve a rectangular shape, part of some of the
bricks must be cut off. {hl('The part which is cut off can be used elsewhere on the drive', 'y', 2)}. The
diagram shows that {hl('eight bricks would be required to cover an area 40cm by 40cm', 'g', 3)}:</p>
{fig(Y, 'ps_q14_bricks', 'A 40 cm by 40 cm square covered by staggered 10 by 20 cm bricks, some cut in half at the edges', 260)}
<p class="stem">What is the {hl('minimum', 'b', 4)} number of bricks needed to resurface a rectangular drive measuring
{hl('550cm by 400cm', 'g', 5)}?</p>""",
    options={'A': '1080 bricks', 'B': '1100 bricks', 'C': '1120 bricks', 'D': '1127 bricks', 'E': '1128 bricks'},
    notes=[(1, 'g', 'One brick covers 10 × 20 = 200 cm².'),
           (2, 'y', 'No waste! Every cut-off half gets used somewhere else. So you can just divide the areas.'),
           (3, 'g', 'Check the idea: 40 × 40 = 1600 cm², and 1600 ÷ 200 = 8. It works.'),
           (4, 'b', 'With nothing wasted, the minimum is drive area ÷ brick area.'),
           (5, 'g', 'Drive area = 550 × 400.')],
    steps=[
        f"""{calc('one brick = 10 × 20 = 200 cm²', f'check: 40 × 40 = 1600 {ar()} 1600 ÷ 200 = 8 bricks {tick()} (matches the diagram)')}""",
        f"""{calc(f'drive = 550 × 400 = 220 000 cm²', f'220 000 ÷ 200 = {boxed("1100")}')}
{note('Cancel first: 550 × 400 ÷ 200 = 550 × 2 = 1100. No big numbers needed.', 'tip')}""",
        f"""<p>Why the cut bricks don’t cost extra: a staggered column needs a half brick at each end, and one brick cut in two gives both halves.</p>{_bricks()}""",
    ],
    answer_text='1100 bricks: 220 000 cm² ÷ 200 cm² per brick, with every cut piece reused.',
    why={'A': '1080 = 40 columns × 27 whole bricks: it leaves out the cut pieces, so part of the drive is bare.',
         'C': '1120 = 40 columns × 28: it lays the columns along the 550 cm side and uses a new brick for every half piece.',
         'D': '1127 = 28 × 20 + 27 × 21: it counts every half brick at the column ends as a whole new brick.',
         'E': '1128 = 28 × 21 + 27 × 20: the same mistake, starting with a staggered column. The cut-offs can be reused.'},
    fast='Nothing is wasted, so divide areas: 550 × 400 ÷ 200 = 550 × 2 = 1100.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _compost():
    u, x0 = 46, 150
    parts, lab = [], []
    row1 = ['y'] * 2 + ['g'] * 4
    row2 = ['y'] * 2 + ['o'] * 4 + ['g'] * 4
    for i, f in enumerate(row1):
        parts.append(rect(x0 + i * u, 50, u, 40, k='ink', fill=f, sw=1.6))
    for i, f in enumerate(row2):
        parts.append(rect(x0 + i * u, 150, u, 40, k='ink', fill=f, sw=1.6))
    lab += [text(x0 + u, 42, 'sand 5 kg', k='ink', size=16), text(x0 + 4 * u, 42, 'coir 10 kg', k='ink', size=16),
            text(x0 + u, 142, 'sand 5', k='ink', size=16), text(x0 + 4 * u, 142, 'add 10 kg of sand', k='orange', size=16),
            text(x0 + 8 * u, 142, 'coir 10', k='ink', size=16),
            text(x0 - 12, 66, 'now', k='ink', size=17, anchor='end'), text(x0 - 12, 86, '15 kg', k='pen', size=17, anchor='end'),
            text(x0 - 12, 166, 'conifers', k='ink', size=17, anchor='end'), text(x0 - 12, 186, '25 kg', k='pen', size=17, anchor='end'),
            text(x0 + 6 * u + 14, 76, 'each block = 2.5 kg', k='muted', size=15, anchor='start')]
    extra = brace(x0, x0 + 6 * u, 196, 'sand 15 kg = 60%', k='orange') + brace(x0 + 6 * u, x0 + 10 * u, 196, 'coir 10 kg = 40%', k='green')
    return svg(640, 250, rough(*parts) + ''.join(lab) + extra,
               'Blocks of 2.5 kg: now 2 sand and 4 coir; for conifers 6 sand and the same 4 coir, so 4 blocks (10 kg) of sand are added')

Q.append(dict(
    n=15, orig=31, answer='B', topic='Ratio & mixtures',
    question=f"""<p>John has {hl('15kg of general potting compost which is made up of 1/3 sand and 2/3 coir', 'g', 1)}. He
wants compost to repot some conifers which require a better draining mixture of {hl('60% sand to 40% coir', 'y', 2)}.</p>
<p class="stem">How much sand does he have to {hl('add', 'b', 3)} to his general purpose compost to make it suitable
for conifers?</p>""",
    options={'A': '5 kg', 'B': '10 kg', 'C': '15 kg', 'D': '20 kg', 'E': '25 kg'},
    notes=[(1, 'g', '⅓ of 15 = 5 kg sand, ⅔ = 10 kg coir.'),
           (2, 'y', 'He only adds sand, so the <b>coir stays at 10 kg</b>. That 10 kg must become 40%.'),
           (3, 'b', 'The sand he adds, not the total sand.')],
    steps=[
        f"""{calc('sand = ⅓ × 15 = 5 kg', 'coir = ⅔ × 15 = 10 kg')}""",
        f"""<p>The coir doesn’t change, so build the new mix around it:</p>
{calc(f'40% = 10 kg {ar()} 10% = 2.5 kg {ar()} 100% = 25 kg', f'sand needed = 60% = 6 × 2.5 = <b>15 kg</b>')}""",
        f"""{_compost()}
{calc(f'add 15 − 5 = {boxed("10 kg")}')}
{note('15 kg of sand out of 25 kg = 15/25 = 60%. It works.', 'check')}""",
    ],
    answer_text='10 kg: the 10 kg of coir must be 40%, so the mix is 25 kg with 15 kg of sand; he already has 5 kg.',
    why={'A': '5 kg is the sand he <b>already</b> has.',
         'C': '15 kg is the total sand in the new mix. He already has 5 of it.',
         'D': '20 kg mixes up the new total (25 kg) with the sand: 25 − 5 = 20.',
         'E': '25 kg is the weight of the whole new mixture.'},
    fast='Coir stays 10 kg = 40%, so the mix is 25 kg and sand is 15 kg. Add 15 − 5 = 10 kg.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _bracket8():
    parts, lab = [], []
    yc = lambda i: 24 + i * 34 + 13
    for i in range(8):
        parts.append(rect(20, 24 + i * 34, 160, 26, k='ink', fill='b', sw=1.6))
        lab.append(text(100, yc(i) + 6, f'group {i + 1}: 9 teams', k='ink', size=15))
    qc = [(yc(2 * k) + yc(2 * k + 1)) / 2 for k in range(4)]
    for k in range(4):
        parts.append(line(180, yc(2 * k), 230, qc[k], k='muted', w=1.8))
        parts.append(line(180, yc(2 * k + 1), 230, qc[k], k='muted', w=1.8))
        parts.append(rect(230, qc[k] - 15, 70, 30, k='ink', fill='o', sw=1.6))
        lab.append(text(265, qc[k] + 6, f'QF {k + 1}', k='ink', size=16))
    sc = [(qc[0] + qc[1]) / 2, (qc[2] + qc[3]) / 2]
    for k in range(2):
        parts.append(line(300, qc[2 * k], 350, sc[k], k='muted', w=1.8))
        parts.append(line(300, qc[2 * k + 1], 350, sc[k], k='muted', w=1.8))
        parts.append(rect(350, sc[k] - 15, 70, 30, k='ink', fill='y', sw=1.6))
        lab.append(text(385, sc[k] + 6, f'SF {k + 1}', k='ink', size=16))
    fc = (sc[0] + sc[1]) / 2
    parts += [line(420, sc[0], 460, fc, k='muted', w=1.8), line(420, sc[1], 460, fc, k='muted', w=1.8),
              rect(460, fc - 17, 80, 34, k='ink', fill='g', sw=1.8)]
    lab += [text(500, fc + 6, 'final', k='ink', size=17),
            text(600, 60, '4 QFs', k='orange', size=18, anchor='end'),
            text(600, 84, '= 8 teams', k='orange', size=18, anchor='end'),
            text(600, 108, '= 8 groups', k='orange', size=18, anchor='end'),
            text(330, 318, 'equal groups of at least 2: 16, 24, 32 … 72 = 8 × 9 ✓', k='green', size=17)]
    return svg(640, 332, rough(*parts) + ''.join(lab),
               'Knockout tree: 8 group winners feed 4 quarter finals, 2 semi-finals and the final; 72 teams make 8 groups of 9')

Q.append(dict(
    n=16, orig=32, answer='E', topic='Tournaments',
    question=f"""<p>A netball tournament is divided into two stages. In the first stage, the teams are divided
into {hl('equal groups', 'y', 1)} within which {hl('each team plays every other team once', 'p', 2)}. In the second
stage, the {hl('winners of each group', 'y', 3)} take part in a knockout competition which {hl('starts with four quarter finals', 'g', 4)}.</p>
<p class="stem">Which of the following {hl('could', 'b', 5)} be the number of teams starting the tournament?</p>""",
    options={'A': '8', 'B': '20', 'C': '44', 'D': '50', 'E': '72'},
    notes=[(1, 'y', 'Every group is the same size.'),
           (2, 'p', 'So a group needs at least 2 teams, or nobody plays anyone.'),
           (3, 'y', 'Exactly one team per group goes through.'),
           (4, 'g', '4 quarter finals × 2 teams = 8 teams in the knockout.'),
           (5, 'b', 'It only has to be possible.')],
    steps=[
        f"""{calc(f'4 quarter finals × 2 = 8 group winners {ar()} <b>8 groups</b>')}""",
        f"""{_bracket8()}""",
        f"""<p>Equal groups, so the number of teams must divide exactly by 8 (with at least 2 per group):</p>
{calc('8 ÷ 8 = 1 team per group: no one to play ' + cross(), '20 ÷ 8 = 2.5 ' + cross(), '44 ÷ 8 = 5.5 ' + cross(),
      '50 ÷ 8 = 6.25 ' + cross(), f'72 ÷ 8 = 9 teams per group {tick()} {ar()} {boxed("72")}')}""",
    ],
    answer_text='72: eight equal groups of 9 teams, whose 8 winners fill the four quarter finals.',
    why={'A': '8 teams would mean 8 groups of 1. Nobody could play anyone in the first stage.',
         'B': '20 ÷ 8 = 2.5. (20 makes 4 groups of 5, but 4 winners only fill two semi-finals, not four quarter finals.)',
         'C': '44 ÷ 8 = 5.5, so the groups can’t be equal.',
         'D': '50 ÷ 8 = 6.25, so the groups can’t be equal.'},
    fast='4 QFs = 8 group winners = 8 equal groups. Only 72 is a multiple of 8 (bigger than 8).',
))


# ---------------------------------------------------------------- 17 (Q36)
def _flights():
    X = lambda h: 40 + h * 24
    parts = [rect(X(2.5), 90, X(9.25) - X(2.5), 44, k='ink', fill='b', sw=1.8),
             rect(X(9.25), 90, X(14.5) - X(9.25), 44, k='ink', fill='y', sw=1.8),
             rect(X(14.5), 90, X(21.75) - X(14.5), 44, k='ink', fill='b', sw=1.8),
             line(X(0), 170, X(24), 170, k='ink', w=2)]
    lab = [text(40, 30, 'Saturday, everything in Dubai time', k='ink', size=17, anchor='start'),
           text((X(2.5) + X(9.25)) / 2, 109, 'flight 1', k='ink', size=15),
           text((X(2.5) + X(9.25)) / 2, 127, '6 h 45', k='pen', size=17),
           text((X(9.25) + X(14.5)) / 2, 109, 'wait', k='ink', size=15),
           text((X(9.25) + X(14.5)) / 2, 127, '5 h 15', k='orange', size=17),
           text((X(14.5) + X(21.75)) / 2, 109, 'flight 2', k='ink', size=15),
           text((X(14.5) + X(21.75)) / 2, 127, '7 h 15', k='pen', size=17)]
    for h, s in ((2.5, '02:30'), (9.25, '09:15'), (14.5, '14:30'), (21.75, '21:45')):
        parts.append(line(X(h), 80, X(h), 170, k='muted', w=1.2, dash=True))
        lab.append(text(X(h), 72, s, k='red', size=16))
    for h in range(0, 25, 6):
        parts.append(line(X(h), 164, X(h), 176, k='ink', w=1.5))
        lab.append(text(X(h), 194, f'{h:02d}:00', k='muted', size=14))
    lab += [text(X(0), 226, '= 22:30 Fri in London', k='red', size=15, anchor='start'),
            text(X(24), 226, '= 20:45 in Kampala', k='red', size=15, anchor='end')]
    return svg(640, 240, rough(*parts) + ''.join(lab),
               'Timeline in Dubai time: flight 1 from 02:30 to 09:15, a wait until 14:30, flight 2 from 14:30 to 21:45')

Q.append(dict(
    n=17, orig=36, answer='B', topic='Time zones',
    question=f"""<p>Below is part of an itinerary for flying from London to Kampala. It involves changing flights
at Dubai with a {hl('wait of 5 hours 15 minutes', 'p', 1)}. {hl('All times are local times', 'y', 2)}. {hl('Dubai is 4 hours ahead of London and Kampala is 1 hour behind Dubai', 'g', 3)}.</p>
{table([['DEPART LONDON (HEATHROW)', '22:30 FRI 30.01.04'], ['DEPART DUBAI', '14:30 SAT 31.01.04'], ['ARRIVE KAMPALA (ENTEBE)', '20:45 SAT 31.01.04']])}
<p class="stem">What is the {hl('total time spent in the air', 'b', 4)}?</p>""",
    options={'A': '12 hrs 30 mins', 'B': '14 hrs 00 mins', 'C': '15 hrs 00 mins', 'D': '17 hrs 00 mins', 'E': '19 hrs 15 mins'},
    notes=[(1, 'p', 'The wait is on the ground: it is <b>not</b> time in the air. It also tells us when the first plane landed.'),
           (2, 'y', 'Each time is on a different clock. Convert them all to one clock first.'),
           (3, 'g', 'Dubai = London + 4. Dubai = Kampala + 1.'),
           (4, 'b', 'Flight 1 + flight 2.')],
    steps=[
        f"""<p>Put every time into <b>Dubai</b> time (it is the middle of the trip):</p>
{calc(f'leave London 22:30 Fri + 4 h {ar()} <b>02:30 Sat</b>',
      f'land in Dubai = 14:30 − 5 h 15 {ar()} <b>09:15 Sat</b>',
      'leave Dubai <b>14:30 Sat</b>',
      f'land in Kampala 20:45 + 1 h {ar()} <b>21:45 Sat</b>')}""",
        f"""{_flights()}
{calc('flight 1: 02:30 → 09:15 = 6 h 45', 'flight 2: 14:30 → 21:45 = 7 h 15', f'total = 6 h 45 + 7 h 15 = {boxed("14 h 00")}')}""",
        f"""{note('The whole trip is 02:30 → 21:45 = 19 h 15. Take off the 5 h 15 wait: 14 h. Same answer.', 'check')}""",
    ],
    answer_text='14 hours: flights of 6 h 45 and 7 h 15.',
    why={'A': '12 h 30 is too short. The two flights alone take 6 h 45 and 7 h 15.',
         'C': '15 h comes from using a 3-hour gap for London (the London to Kampala difference) on the first flight, which lands in Dubai.',
         'D': '17 h ignores the time zones: 22:30 Fri to 20:45 Sat is 22 h 15 on the clocks, minus the 5 h 15 wait.',
         'E': '19 h 15 is the whole journey, including the 5 h 15 sitting in Dubai.'},
    fast='All in Dubai time: 02:30 → 21:45 = 19 h 15. Minus the 5 h 15 wait = 14 h.',
))
