import math
from wslib import *
from _2021_ps_2 import _pie

Y = 2021
Q = []

# ---------------------------------------------------------------- 17 (Q36)
FACES = [('red', 'square'), ('blue', 'square'), ('green', 'square'), ('red', 'circle'), ('blue', 'circle'), ('green', 'circle')]


def _score(a, b):
    s = sum(1 for f in (a, b) if f[1] == 'circle') + sum(1 for f in (a, b) if f[0] == 'red')
    s += 1 if a[1] == b[1] else 0
    s += 2 if a[0] == b[0] else 0
    return s


def _face(x, y, f, r=11):
    k = {'red': 'red', 'blue': 'pen', 'green': 'green'}[f[0]]
    fill = {'red': 'p', 'blue': 'b', 'green': 'g'}[f[0]]
    if f[1] == 'square':
        return rect(x - r, y - r, 2 * r, 2 * r, k=k, fill=fill, sw=2.4)
    return circle(x, y, r, k=k, fill=fill, sw=2.4)


def _dice_grid():
    c, x0, y0 = 50, 110, 64
    parts, lab = [], []
    seen = set()
    for i, a in enumerate(FACES):
        parts.append(_face(x0 - 28, y0 + i * c + c / 2, a))
        parts.append(_face(x0 + i * c + c / 2, y0 - 26, a))
        for j, b in enumerate(FACES):
            s = _score(a, b)
            seen.add(s)
            f = 'y' if s == 7 else 'o' if s == 5 else 'paper'
            parts.append(rect(x0 + j * c, y0 + i * c, c, c, k='ink', fill=f, sw=1.3))
            lab.append(text(x0 + j * c + c / 2, y0 + i * c + c / 2 + 8, s, k='ink', size=21))
    lab += [text(x0 + 3 * c, 18, 'die 2', k='muted', size=15), text(26, y0 + 3 * c, 'die 1', k='muted', size=15, rotate=-90)]
    xr = x0 + 6 * c + 30
    lab += [text(xr, 110, 'scores that happen:', k='ink', size=17, anchor='start'),
            text(xr, 140, ', '.join(str(v) for v in sorted(seen)), k='green', size=22, anchor='start', font='scrawl'),
            text(xr, 196, 'never 6!', k='red', size=30, anchor='start', font='scrawl'),
            text(xr, 240, 'top score 7 (yellow),', k='ink', size=16, anchor='start'),
            text(xr, 262, 'next best 5 (orange):', k='ink', size=16, anchor='start'),
            text(xr, 284, 'nothing in between', k='ink', size=16, anchor='start')]
    return svg(660, y0 + 6 * c + 16, rough(*parts) + ''.join(lab),
               'Six by six grid of every pair of faces with its score; the scores are 0 to 5 and 7, never 6')

Q.append(dict(
    n=17, orig=36, answer='E', topic='Scoring & cases',
    question=f"""<p>A game is played involving two dice. Both dice are 6-sided cubes with the following shapes on
their faces:</p>
<p style="text-align:center">red square<br>blue square<br>green square<br>red circle<br>blue circle<br>green circle</p>
<p>The two dice are thrown and the player scores points according to the following system:</p>
{table([[hl('Each circle displayed', 'y', 1), '1'], [hl('Each red shape displayed', 'y', 1), '1'], [hl('Both same shape', 'y', 2), '1'],
        [hl('Both same colour', 'y', 2), hl('2', 'g')]], head=['<i>outcome</i>', '<i>points scored</i>'])}
<p>{hl('The maximum possible score from a single throw of both dice is 7', 'g', 3)} (both dice displaying red
circles).</p>
<p class="stem">Which one of the following scores is {hl('<b>not</b>', 'b', 4)} possible from a single throw of both dice?</p>""",
    options={'A': '2', 'B': '3', 'C': '4', 'D': '5', 'E': '6'},
    notes=[(1, 'y', '“Each”: these score per die. A red circle on its own is worth 2 (circle + red).'),
           (2, 'y', 'Bonuses for the pair. Same colour is worth 2.'),
           (3, 'g', '7 = 2 circles + 2 reds + same shape 1 + same colour 2.'),
           (4, 'b', 'Find the odd one out: four of these can happen, one can’t.')],
    steps=[
        f"""<p>Score each die on its own, then add the pair bonus:</p>
{calc('red circle 2, red square 1, blue or green circle 1, blue or green square 0',
      'bonus: same shape +1, same colour +2')}""",
        f"""<p>To get 6 you would have to lose exactly 1 point from the top score of 7. Try changing one die:</p>
{calc(f'red circle + red square: 2 + 1 + 2 (colour) = 5 {ar()} lost 2',
      f'red circle + blue circle: 2 + 1 + 1 (shape) = 4 {ar()} lost 3',
      f'no red circle at all: at most 1 + 1 + 1 + 2 = 5')}
<p>So nothing scores 6. Check it with every pair:</p>{_dice_grid()}""",
        f"""<p>The other options all happen:</p>
{calc('2: red square + blue square (1 red + same shape 1)', '3: blue circle + green circle (2 circles + same shape 1)',
      '4: red circle + blue circle (2 circles + 1 red + same shape 1)', '5: red circle + red square (1 circle + 2 reds + same colour 2)',
      f'not possible = {boxed("6")}')}""",
    ],
    answer_text='6: the best non-perfect throw scores 5, and the perfect throw scores 7.',
    why={'A': '2 is possible: red square + blue square (1 for red, 1 for same shape).',
         'B': '3 is possible: blue circle + green circle (2 circles, 1 for same shape).',
         'C': '4 is possible: red circle + blue circle (2 circles, 1 red, 1 same shape).',
         'D': '5 is possible: red circle + red square (1 circle, 2 reds, 2 same colour).'},
    fast='7 needs two red circles. Change either die and you lose at least 2 points (red square gives 5), so 6 is impossible.',
))


# ---------------------------------------------------------------- 18 (Q37)
def _hike():
    s, x0 = 4, 110
    parts = [rect(x0, 60, 90 * s, 44, k='ink', fill='g', sw=1.8), rect(x0 + 90 * s, 60, 30 * s, 44, k='ink', fill='o', sw=1.8),
             rect(x0 + 90 * s, 150, 30 * s, 44, k='ink', fill='o', sw=1.8)]
    lab = [text(x0 - 10, 88, 'all 6 days', k='ink', size=16, anchor='end'),
           text(x0 - 10, 178, 'days 1–5', k='ink', size=16, anchor='end'),
           text(x0 + 45 * s, 88, 'walked 6 × 15 = 90 km', k='ink', size=17),
           text(x0 + 105 * s, 88, 'bus 30', k='ink', size=17),
           text(x0 + 105 * s, 178, 'bus 30', k='ink', size=17),
           text(x0 + 60 * s, 40, 'chart total: 10 + 15 + 20 + 25 + 20 + 30 = 120 km', k='pen', size=17),
           text(x0 + 45 * s, 178, 'bus already used up by day 5', k='red', size=18, font='scrawl'),
           text(x0 + 60 * s, 236, 'bus on day 6 = 30 − 30 = 0 km', k='red', size=22, font='scrawl')]
    parts += [line(x0 + 90 * s, 104, x0 + 90 * s, 150, k='red', w=1.8, dash=True),
              line(x0 + 120 * s, 104, x0 + 120 * s, 150, k='red', w=1.8, dash=True)]
    return svg(620, 250, rough(*parts) + ''.join(lab),
               'Bar of 120 km split into 90 km walked and 30 km by bus; the 30 km of bus was all done by the end of day 5')

Q.append(dict(
    n=18, orig=37, answer='A', topic='Averages & charts',
    question=f"""<p>On a six-day hiking holiday, a group of friends travelled part of the trail by walking and part by
bus. {hl('On average they walked 15 km per day over the six days', 'g', 1)}. {hl('By the end of the 5<sup>th</sup> day, they had travelled 30 km by bus', 'g', 2)}. The chart below shows the {hl('total distance covered each day', 'y', 3)}.</p>
{fig(Y, 'ps_q18_chart', 'Bar chart of distance each day: day 1 10 km, day 2 15, day 3 20, day 4 25, day 5 20, day 6 30', 330)}
<p class="stem">How far did they travel {hl('by bus on the 6<sup>th</sup> day', 'b', 4)}?</p>""",
    options={'A': '0 km', 'B': '5 km', 'C': '10 km', 'D': '15 km', 'E': '30 km'},
    notes=[(1, 'g', 'An average: total walked = 6 × 15 = 90 km. Not 15 km every single day!'),
           (2, 'g', 'Bus total for days 1 to 5.'),
           (3, 'y', 'Each bar = walking + bus for that day.'),
           (4, 'b', 'Bus total for all 6 days − bus total for days 1 to 5.')],
    steps=[
        f"""<p>Total distance from the chart, and total walked from the average:</p>
{calc('10 + 15 + 20 + 25 + 20 + 30 = <b>120 km</b> in total', '6 × 15 = <b>90 km</b> walked')}""",
        f"""<p>The rest was by bus:</p>
{calc('120 − 90 = <b>30 km</b> by bus over all six days', f'30 km by bus already done by the end of day 5 {ar()} day 6 bus = {boxed("0 km")}')}
{_hike()}""",
        f"""{note('Don’t assume they walked 15 km on day 6 (30 − 15 = 15 km by bus). 15 km is only the average over the six days.', 'trap')}""",
    ],
    answer_text='0 km: all 30 km of bus travel had happened by the end of day 5.',
    why={'B': '5 km is the average bus distance per day (30 ÷ 6), not day 6’s share.',
         'C': '10 km would need the six bars to add up to 130 km; they add up to 120 km.',
         'D': '15 km assumes they walked exactly 15 km on day 6 (30 − 15). The 15 km is only an average.',
         'E': '30 km is the bus total for the whole holiday, and it was all used up by the end of day 5.'},
    fast='Chart total 120 − walked 6 × 15 = 30 by bus. All 30 done by day 5, so 0 on day 6.',
))


# ---------------------------------------------------------------- 19 (Q38)
def _shares():
    data = [('2016', 25, 35), ('2017', 65, 75), ('2018', 45, 70)]
    H, base = 200, 250
    parts, lab, tops = [], [], []
    for i, (yr, m, f) in enumerate(data):
        x = 90 + i * 150
        mh = H * m / (m + f)
        parts.append(rect(x, base - H, 80, H - mh, k='ink', fill='p', sw=1.6))
        parts.append(rect(x, base - mh, 80, mh, k='ink', fill='b', sw=1.6))
        lab.append(text(x + 40, base - mh / 2 + 6, f'{100 * m / (m + f):.0f}%', k='pen', size=19))
        lab.append(text(x + 40, base - H + (H - mh) / 2 + 6, f'{100 * f / (m + f):.0f}%', k='red', size=17))
        lab.append(text(x + 40, base + 22, f'{yr}', k='ink', size=16))
        lab.append(text(x + 40, base + 42, f'{m} of {m + f}', k='muted', size=14))
        tops.append((x + 80, base - mh))
    for (x1, y1), (x2, y2) in zip(tops, tops[1:]):
        parts.append(line(x1, y1, x2 - 80, y2, k='pen', w=2.2, dash=True))
    lab += [text(560, 70, 'female share', k='red', size=16, anchor='start'), text(560, 200, 'male share', k='pen', size=16, anchor='start'),
            text(330, 26, '2016 → 2018: male share 42% → 39%, DOWN', k='red', size=19, font='scrawl')]
    return svg(660, 304, rough(*parts) + ''.join(lab),
               'Three 100 per cent bars: males 42 per cent in 2016, 46 per cent in 2017 and 39 per cent in 2018')

Q.append(dict(
    n=19, orig=38, answer='C', topic='Percentages & graphs',
    question=f"""<p>The numbers of males and females enrolled at a college in 2016, 2017 and 2018 are shown in
the graph below.</p>
{fig(Y, 'ps_q19_graph', 'Bar chart: 2016 male 25, female 35; 2017 male 65, female 75; 2018 male 45, female 70', 360)}
<p class="stem">Which one of the following is {hl('<b>not</b>', 'b', 1)} true?</p>""",
    options={'A': 'The percentage of males increased from 2016 to 2017.',
             'B': 'The percentage of females increased from 2017 to 2018.',
             'C': 'The percentage of males increased from 2016 to 2018.',
             'D': 'The percentage increase in the number of males from 2016 to 2017 was greater than the percentage decrease in the number of males from 2017 to 2018.',
             'E': 'The percentage increase in the number of females from 2016 to 2017 was greater than the percentage decrease in the number of females from 2017 to 2018.'},
    notes=[(1, 'b', 'Four statements are true. Find the false one.')],
    steps=[
        f"""<p>Read the bars and add up each year:</p>
{table([['2016', '25', '35', '60'], ['2017', '65', '75', '140'], ['2018', '45', '70', '115']], head=['', 'male', 'female', 'total'])}
{note('Two different ideas! “Percentage of males” = males ÷ everyone that year (A, B, C). “Percentage increase in the number” = change ÷ starting number (D, E).', 'trap')}""",
        f"""<p>Share of males each year:</p>
{calc('2016: 25 ÷ 60 ≈ 42%', '2017: 65 ÷ 140 ≈ 46%', '2018: 45 ÷ 115 ≈ 39%')}
{_shares()}
{calc(f'A: 42% → 46% up {tick()}', f'B: females 54% → 61% up {tick()}', f'C: 42% → 39% <b>down</b> {cross()} {ar()} {boxed("C")} is not true')}""",
        f"""<p>Check D and E too (change ÷ starting number):</p>
{calc(f'D: males 25 → 65 is +40 on 25 = +160%; 65 → 45 is −20 on 65 ≈ −31% {tick()}',
      f'E: females 35 → 75 is +40 on 35 ≈ +114%; 75 → 70 is −5 on 75 ≈ −7% {tick()}')}
{note('Quick check for C without a calculator: in 2016 males are 25 out of 60, a bit over 2 in 5 (40%). In 2018, 2 in 5 of 115 would be 46, and there are only 45. So the share fell.', 'tip')}""",
    ],
    answer_text='C is false: males were 42% in 2016 but only 39% in 2018.',
    why={'A': 'A is true: 25 out of 60 (42%) rises to 65 out of 140 (46%).',
         'B': 'B is true: females go from 75 out of 140 (54%) to 70 out of 115 (61%).',
         'D': 'D is true: males +160% (25 → 65) is bigger than −31% (65 → 45).',
         'E': 'E is true: females +114% (35 → 75) is bigger than −7% (75 → 70).'},
    fast='Males’ share: 25/60 ≈ 42%, 65/140 ≈ 46%, 45/115 ≈ 39%. From 2016 to 2018 it went down, so C is false.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _words():
    words = [('eight', 8), ('five', 5), ('four', 4), ('nine', 9), ('one', 1), ('seven', 7), ('six', 6), ('three', 3), ('two', 2), ('zero', 0)]
    bw, x0 = 62, 20
    parts, lab = [], []
    order = {4: '1st', 9: '2nd', 1: '3rd', 6: '4th'}
    for i, (w, d) in enumerate(words):
        x = x0 + i * bw
        pick = d in order
        parts.append(rect(x + 2, 70, bw - 4, 64, k='green' if pick else 'ink', fill='y' if pick else 'paper', sw=2.2 if pick else 1.4, rx=6))
        lab.append(text(x + bw / 2, 96, w, k='ink', size=16))
        lab.append(text(x + bw / 2, 124, d, k='pen', size=22, font='print'))
        if pick:
            lab.append(text(x + bw / 2, 60, order[d], k='green', size=17, font='scrawl'))
    pts = [x0 + 2 * bw + bw / 2, x0 + 3 * bw + bw / 2, x0 + 4 * bw + bw / 2, x0 + 6 * bw + bw / 2]
    for a, b in zip(pts, pts[1:]):
        parts.append(arrow(a + 8, 140, b - 8, 140, k='red', bend=-0.25))
    lab += [text(x0 + 5 * bw, 26, 'digit words in alphabetical order →', k='muted', size=16),
            text(x0 + 5 * bw, 200, 'PIN 4 9 1 6 = 49 and 16, both squares', k='red', size=21, font='scrawl')]
    return svg(660, 214, rough(*parts) + ''.join(lab),
               'The ten digit words in alphabetical order; four, nine, one and six are picked in that order, giving PIN 4916')

Q.append(dict(
    n=20, orig=42, answer='D', topic='Number puzzles',
    question=f"""<p>The 4-digit PIN for my credit card can be written as {hl('two 2-digit square numbers (between 10 and 100)', 'g', 1)}. When the four digits, which are {hl('all different', 'p', 2)}, are {hl('written individually in words, they are in alphabetical order', 'y', 3)}.</p>
<p class="stem">What is the {hl('last digit', 'b', 4)} of my PIN?</p>""",
    options={'A': '1', 'B': '4', 'C': '5', 'D': '6', 'E': '9'},
    notes=[(1, 'g', 'Only six to choose from: 16, 25, 36, 49, 64, 81.'),
           (2, 'p', 'No repeated digit, so 16 and 81 can’t go together (two 1s).'),
           (3, 'y', 'Spell each digit (four, nine…) and the words must run A to Z.'),
           (4, 'b', 'Just the final digit.')],
    steps=[
        f"""<p>List the 2-digit squares: 16, 25, 36, 49, 64, 81.</p>
<p>Each square sits inside the PIN, so its own two digits must already be in alphabetical order:</p>
{calc(f'16: one, six {tick()}', f'25: two, five {cross()}', f'36: three, six {cross()}', f'49: four, nine {tick()}',
      f'64: six, four {cross()}', f'81: eight, one {tick()}')}""",
        f"""<p>Only 16, 49 and 81 are left. Put the digit words in alphabetical order to see what can follow what:</p>{_words()}""",
        f"""<p>Try the pairs (all digits different):</p>
{calc(f'49 then 16: four, nine, one, six {tick()}', f'16 then 49: six before four {cross()}',
      f'81 then 49: one before four {cross()}', f'49 then 81: nine before eight {cross()}', '16 and 81: digit 1 twice ' + cross(),
      f'PIN = 4916 {ar()} last digit {boxed("6")}')}""",
    ],
    answer_text='6: the PIN is 4916 (four, nine, one, six are in alphabetical order).',
    why={'A': 'Ending in 1 means the second square is 81, but “eight” is first in the alphabet list, so no digit can come before it.',
         'B': 'Ending in 4 means 64, but “six” comes after “four” in the alphabet.',
         'C': 'Ending in 5 means 25, but “two” comes after “five”.',
         'E': 'Ending in 9 means 49 goes last, and 1649 fails because “six” comes after “four”.'},
    fast='Squares whose two words are in order: 16, 49, 81. Only 49 + 16 works: four, nine, one, six. Last digit 6.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _tt(title, rows):
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return (f'<div class="tbl-wrap"><table class="ptable"><thead><tr><th colspan="4"><i>{title}</i></th></tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def _jun_day():
    X = lambda t: 36 + t * 1.6
    parts, lab = [], []
    segs = [(0, 10, 'o', ''), (10, 27, 'paper', ''), (27, 54, 'b', 'train'), (54, 64, 'o', ''), (64, 297, 'g', 'at Aki’s: max 3 h 53 min'),
            (297, 307, 'o', ''), (307, 334, 'b', 'train'), (334, 344, 'o', ''), (344, 360, 'paper', '')]
    for a, b, f, name in segs:
        parts.append(rect(X(a), 70, X(b) - X(a), 36, k='ink', fill=f, sw=1.5))
        if name:
            lab.append(text((X(a) + X(b)) / 2, 93, name, k='ink', size=15 if name == 'train' else 17))
    marks = [(0, '10:00', 0), (27, '10:27', 1), (54, '10:54', 0), (64, '11:04', 1), (297, '14:57', 0), (307, '15:07', 1),
             (334, '15:34', 0), (344, '15:44', 1), (360, '16:00', 0)]
    for t, s, row in marks:
        y = 60 if row == 0 else 40
        parts.append(line(X(t), y + 4, X(t), 70, k='muted', w=1.2))
        lab.append(text(X(t), y, s, k='red' if t == 360 else 'ink', size=14))
    parts.append(line(X(360), 66, X(360), 116, k='red', w=2.6))
    parts.append(rect(X(64), 136, X(124) - X(64), 30, k='ink', fill='g', sw=1.5))
    lab += [text(X(94), 156, '1 hour', k='ink', size=15),
            text(X(124) + 10, 157, 'shortest stay: leave at 12:04 and wait at the station', k='ink', size=16, anchor='start'),
            text(X(0), 128, 'orange = 10 min walk', k='orange', size=14, anchor='start'),
            text(X(180), 200, '3 h 53 min − 1 h = 2 h 53 min', k='red', size=22, font='scrawl')]
    return svg(660, 214, rough(*parts) + ''.join(lab),
               'Timeline of Jun’s day from 10:00 to 16:00: walk, 10:27 train, at Aki’s from 11:04 to 14:57 at most, 15:07 train, home 15:44')

Q.append(dict(
    n=21, orig=43, answer='B', topic='Timetables',
    question=f"""<p>Jun lives in Applecross and Aki lives in Damsonville. {hl('Both live a 10-minute walk from their local train stations', 'p', 1)}, which both lie on the Applecross–Figtown line.</p>
<p>Trains on this line run throughout the day to the following timetable:</p>
<div style="display:flex;flex-wrap:wrap;gap:0 20px">
{_tt('Applecross–Figtown', [['<i>Applecross</i>', 'h:07', hl('h:27', 'g'), 'h:47'], ['<i>Bananagate</i>', 'h:17', 'h:37', 'h:57'],
                            ['<i>Cherrytree</i>', 'h:25', 'h:45', '(h+1):05'], ['<i>Damsonville</i>', 'h:34', hl('h:54', 'g'), '(h+1):14'],
                            ['<i>Elderhampton</i>', 'h:48', '(h+1):08', '(h+1):28'], ['<i>Figtown</i>', 'h:54', '(h+1):14', '(h+1):34']])}
{_tt('Figtown–Applecross', [['<i>Figtown</i>', 'h:07', 'h:27', 'h:47'], ['<i>Elderhampton</i>', 'h:13', 'h:33', 'h:53'],
                            ['<i>Damsonville</i>', 'h:27', 'h:47', hl('(h+1):07', 'g')], ['<i>Cherrytree</i>', 'h:36', 'h:56', '(h+1):16'],
                            ['<i>Bananagate</i>', 'h:44', '(h+1):04', '(h+1):24'], ['<i>Applecross</i>', 'h:54', '(h+1):14', hl('(h+1):34', 'g')]])}
</div>
<p>“h” refers to all hours from 06:00 to 21:00. For instance, the train departing from Applecross at
08:27 arrives in Figtown at 09:14.</p>
<p>{hl('Jun leaves his house at 10:00', 'g', 2)} to go to visit Aki at her house. He {hl('must be back home by 16:00', 'g', 3)}
and will spend {hl("at least 1 hour at Aki's house", 'y', 4)}.</p>
<p class="stem">What is the {hl('difference between the maximum and minimum time', 'b', 5)} that Jun can spend at Aki’s
house?</p>""",
    options={'A': '2 hours 40 minutes', 'B': '2 hours 53 minutes', 'C': '3 hours 26 minutes', 'D': '3 hours 40 minutes',
             'E': '3 hours 53 minutes'},
    notes=[(1, 'p', 'Add 10 minutes of walking at <b>both</b> ends, both ways.'),
           (2, 'g', 'At Applecross station at 10:10, so the 10:07 has gone.'),
           (3, 'g', 'Home by 16:00 means at Applecross station by 15:50.'),
           (4, 'y', 'The minimum stay is exactly 1 hour. He can wait at the station after that.'),
           (5, 'b', 'Longest possible stay − shortest possible stay.')],
    steps=[
        f"""<p><b>Earliest arrival.</b> Jun reaches Applecross station at 10:10. Trains leave at :07, :27, :47:</p>
{calc(f'10:27 from Applecross {ar()} Damsonville 10:54', f'+ 10 min walk {ar()} at Aki’s <b>11:04</b>')}""",
        f"""<p><b>Latest departure.</b> He must be at Applecross station by 15:50. Trains from Damsonville leave at :07, :27, :47
and reach Applecross at :34, :54, :14:</p>
{calc(f'15:27 from Damsonville {ar()} Applecross 15:54 {cross()} too late',
      f'15:07 from Damsonville {ar()} Applecross 15:34 {tick()} home 15:44',
      f'leave Aki’s by 15:07 − 10 min = <b>14:57</b>')}""",
        f"""<p>Put the day on a timeline:</p>{_jun_day()}
{calc('maximum = 11:04 to 14:57 = <b>3 h 53 min</b>', 'minimum = <b>1 hour</b> (the question says at least 1 hour)',
      f'3 h 53 min − 1 h = {boxed("2 h 53 min")}')}
{note('Timetable trick: the (h+1) column is still the same train. The 15:07 from Damsonville is “h = 14, (h+1):07”.', 'tip')}""",
    ],
    answer_text='2 hours 53 minutes: he can stay up to 3 h 53 min (11:04 to 14:57) and must stay at least 1 hour.',
    why={'A': '2 h 40 min uses 1 h 13 min as the minimum (staying until 12:17 to walk straight onto the 12:27 train). He only has to stay 1 hour; he can wait at the station.',
         'C': '3 h 26 min would need a minimum stay of only 27 minutes, but he stays at least an hour.',
         'D': '3 h 40 min times the stay until he gets home (11:04 to 15:44 = 4 h 40 min) and then takes off the hour.',
         'E': '3 h 53 min is the maximum stay on its own. You still have to take off the 1-hour minimum.'},
    fast='Arrive 11:04 (10:27 train). Leave 14:57 (15:07 train, home 15:44). Max 3 h 53, min 1 h. Difference 2 h 53.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _suzy():
    months = [('Mar', 60), ('Apr', 62), ('May', 64), ('Jun', 106), ('Jul', 186), ('Aug', 240)]
    parts, lab = [], []
    base, x0, bw, u = 230, 40, 44, 0.8
    for i, (m, v) in enumerate(months):
        x = x0 + i * bw
        parts.append(rect(x + 4, base - v * u, bw - 8, v * u, k='ink', fill='b', sw=1.5))
        lab.append(text(x + bw / 2, base - v * u - 6, v, k='ink', size=14))
        lab.append(text(x + bw / 2, base + 18, m, k='muted', size=14))
    parts.append(line(x0, base, x0 + 6 * bw, base, k='ink', w=1.6))
    lab.append(text(x0 + 3 * bw, 22, 'km run each month', k='ink', size=16))
    slices = [(30, 'y', ['Mar', '30°']), (31, 'y', ['Apr', '31°']), (32, 'y', ['May', '32°']), (53, 'paper', ['Jun 53°']),
              (93, 'b', ['Jul', '93°']), (121, 'o', ['Aug', '120°'])]
    p2, l2 = _pie(480, 130, 104, slices, label_r=0.66, size=13)
    lab.append(text(480, 262, 'what the pie must look like', k='ink', size=16, font='scrawl'))
    return svg(660, 274, rough(*parts, *p2) + ''.join(lab + l2),
               'Monthly distances 60, 62, 64, 106, 186, 240 as bars, and the matching pie: three equal 30 degree slices, then 53, 93 and 120 degrees')

Q.append(dict(
    n=22, orig=44, answer='D', topic='Pie charts & running totals',
    question=f"""<p>At the beginning of March, Suzy begins training for a marathon running event. At the end of
each month from March until August, she records the {hl('total distance that she has run since the beginning of March', 'p', 1)}. This information is shown in the following table.</p>
{table([['March', '60 km'], ['April', '122 km'], ['May', '186 km'], ['June', '292 km'], ['July', '478 km'], ['August', '718 km']],
       head=['<i>month</i>', '<i>total cumulative distance</i>'])}
<p class="stem">Which one of the following pie charts, suitably labelled, could represent a comparison of the
{hl('monthly distances', 'b', 2)} run by Suzy?</p>
{fig(Y, 'ps_q22_pies', 'Five unlabelled pie charts A to E, each with six slices of different sizes', 560)}""",
    options={'A': 'pie A', 'B': 'pie B', 'C': 'pie C', 'D': 'pie D', 'E': 'pie E'},
    notes=[(1, 'p', 'A running total! Each month’s own distance = this total − last month’s total.'),
           (2, 'b', 'The pie compares the six separate months, not the running totals.')],
    steps=[
        f"""<p>Undo the running total:</p>
{calc('March 60', 'April 122 − 60 = 62', 'May 186 − 122 = 64', 'June 292 − 186 = 106', 'July 478 − 292 = 186', 'August 718 − 478 = 240')}""",
        f"""<p>The whole pie is 718 km, which is almost 720. So each km is about half a degree:</p>
{calc('Mar 30°, Apr 31°, May 32°, Jun 53°, Jul 93°, Aug 120°')}
{_suzy()}
<p>Look for: <b>three almost equal small slices</b>, one a bit bigger (about 53°), one just over a quarter, and one a <b>third</b>.</p>""",
        f"""<p>Only pie {boxed('D')} has three equal thin slices next to a quarter-ish slice and a third.</p>
{note('Fast first check: August is 240 out of 718, a third of the pie. C has one slice of more than half, so it’s out at once.', 'tip')}""",
    ],
    answer_text='Pie D: slices of about 30°, 31°, 32°, 53°, 93° and 120°.',
    why={'A': 'A’s smallest slice (about 15°) is half the size of the next. March, April and May should be three almost equal slices.',
         'B': 'B’s two biggest slices are about the same size, but August (240 km) is much bigger than July (186 km).',
         'C': 'C has one slice of more than half the pie. August is only a third of the total.',
         'E': 'E starts with a tiny sliver (about 5°) and grows steadily. March, April and May should be almost equal.'},
    fast='Monthly: 60, 62, 64, 106, 186, 240. Three equal small slices plus a third for August: D.',
))


# ---------------------------------------------------------------- 23 (Q46)
def _statement():
    parts = [path('M40 20 L380 20 L380 284 L366 296 L352 284 L338 296 L324 284 L310 296 L296 284 L282 296 L268 284 L254 296 '
                  'L240 284 L226 296 L212 284 L198 296 L184 284 L170 296 L156 284 L142 296 L128 284 L114 296 L100 284 L86 296 '
                  'L72 284 L58 296 L40 284 Z', k='ink', fill='paper', sw=1.8),
             line(60, 214, 360, 214, k='ink', w=1.4, dash=True)]
    rows = [('goods (UK)', '2450.00', 'ink'), ('cash withdrawal', '300.00', 'ink'), ('cash charge 2.5%', '7.50', 'orange'),
            ('goods in Spain', '500.00', 'ink'), ('abroad charge 3.5%', '17.50', 'orange')]
    lab = [text(210, 46, 'AUGUST STATEMENT', k='ink', size=17, font='print')]
    for i, (a, b, k) in enumerate(rows):
        y = 78 + i * 27
        lab.append(text(60, y, a, k=k, size=17, anchor='start'))
        lab.append(text(360, y, b, k=k, size=17, anchor='end'))
    lab += [text(60, 240, 'TOTAL', k='ink', size=18, anchor='start', font='print'), text(360, 240, '£3275.00', k='ink', size=19, anchor='end'),
            text(60, 270, 'minimum 2%', k='ink', size=17, anchor='start'), text(360, 270, '£65.50', k='green', size=22, anchor='end', font='scrawl'),
            text(400, 120, '7.50 is more', k='orange', size=17, anchor='start'), text(400, 140, 'than the £3 min', k='orange', size=17, anchor='start'),
            text(400, 182, '17.50 is more', k='orange', size=17, anchor='start'), text(400, 202, 'than the £5 min', k='orange', size=17, anchor='start')]
    return svg(600, 306, rough(*parts) + ''.join(lab),
               'Statement: goods 2450, cash 300, cash charge 7.50, Spain goods 500, abroad charge 17.50, total 3275, 2 per cent is 65.50')

Q.append(dict(
    n=23, orig=46, answer='D', topic='Percentages & money',
    question=f"""<p>In August, Bill used his new, UK-based Bridgford Bank credit card for the first time. The
summary details for this card are shown below.</p>
<div style="border:1px solid #333;padding:6px 16px;margin:.4em 0 .9em;max-width:460px">
<p><b><u>Bridgford Bank Credit Card Summary Details</u></b></p>
<p>{hl('No interest for the first 12 months', 'p', 1)}.</p>
<p>{hl('2.5% charged on cash withdrawals (minimum charge £3)', 'y', 2)}.</p>
<p>{hl('3.5% charged on all transactions made abroad (minimum £5)', 'y', 2)}.</p>
<p>{hl('All charges are added to the account', 'y', 3)} at the time of the
transaction and then the {hl('minimum monthly payment of 2% of the total shown on the statement', 'y', 3)} is calculated at the end of each
month.</p></div>
<p>He {hl('bought goods to the value of £2450', 'g', 4)}. He also {hl('withdrew £300 in cash from a UK cash machine', 'g', 4)}. Then, {hl('on holiday in Spain', 'g', 4)}, he used the card to pay for {hl('£500 worth of goods', 'g', 4)}.</p>
<p class="stem">What would be the {hl('minimum payment', 'b', 5)} for his card use in August?</p>""",
    options={'A': '£65.00', 'B': '£65.16', 'C': '£65.25', 'D': '£65.50', 'E': '£65.56'},
    notes=[(1, 'p', 'No interest to add. Ignore.'),
           (2, 'y', 'Use the percentage, unless it comes to less than the minimum.'),
           (3, 'y', 'Charges go onto the total first, then take 2% of everything.'),
           (4, 'g', 'UK goods: no charge. UK cash: 2.5%. Spain: 3.5%.'),
           (5, 'b', '2% of the statement total.')],
    steps=[
        f"""<p>Work out the charges (check each against its minimum):</p>
{calc(f'cash: 2.5% of £300 = £7.50 {ar()} more than £3, so £7.50',
      f'Spain: 3.5% of £500 = £17.50 {ar()} more than £5, so £17.50',
      'UK goods: no charge')}
{note('2.5% of 300: 1% is 3, so 2.5% is 7.50. 3.5% of 500: 1% is 5, so 3.5% is 17.50.', 'tip')}""",
        f"""<p>Add everything onto the statement, then take 2%:</p>{_statement()}
{calc('2450 + 300 + 7.50 + 500 + 17.50 = £3275', f'1% = 32.75, so 2% = {boxed("£65.50")}')}""",
    ],
    answer_text='£65.50: 2% of £3275 (spending £3250 plus £7.50 and £17.50 of charges).',
    why={'A': '£65.00 is 2% of £3250, leaving out both charges.',
         'B': '£65.16 uses the minimum charges (£3 + £5) instead of the percentages: 2% of £3258. Minimums only apply when the percentage is smaller.',
         'C': '£65.25 adds only £12.50 of charges (£7.50 for cash but just the £5 minimum for Spain): 2% of £3262.50.',
         'E': '£65.56 charges 3.5% on the cash as well (£10.50 + £17.50): 2% of £3278. The cash came from a UK machine.'},
    fast='Charges 7.50 + 17.50 = 25. Total 3250 + 25 = 3275. 2% = 65.50.',
))


# ---------------------------------------------------------------- 24 (Q48)
def _offices():
    rows = [('Calypsio', 3000, 270), ('Jaspoon', 6000, 210), ('Menoko', 4500, 300), ('Sontorius', 3900, 240), ('Zentium', 4800, 210)]
    s, x0 = 0.07, 120
    parts, lab = [], []
    for i, (name, b, l) in enumerate(rows):
        y = 40 + i * 44
        parts.append(rect(x0, y, b * s, 28, k='ink', fill='b', sw=1.5))
        parts.append(rect(x0 + b * s, y, l * s, 28, k='ink', fill='o', sw=1.5))
        lab.append(text(x0 - 10, y + 20, name, k='ink', size=16, anchor='end'))
        lab.append(text(x0 + (b + l) * s + 8, y + 20, f'{b + l:,}'.replace(',', ' ') + ' k', k='ink', size=15, anchor='start'))
    lo, hi = x0 + 3270 * s, x0 + 6210 * s
    parts += [line(lo, 30, lo, 272, k='red', w=2, dash=True), line(hi, 30, hi, 272, k='red', w=2, dash=True),
              line(lo + 4, 262, hi - 4, 262, k='red', head=True, tail=True, w=2.2)]
    lab += [text((lo + hi) / 2, 290, '6210 k − 3270 k = 2940 k = $2 940 000', k='red', size=19, font='scrawl'),
            text(x0, 22, 'building (3000 m²)', k='pen', size=15, anchor='start'), text(x0 + 200, 22, '+ land (600 m²), in $ thousands', k='orange', size=15, anchor='start')]
    return svg(660, 304, rough(*parts) + ''.join(lab),
               'Cost bars in thousands of dollars: Calypsio 3270, Jaspoon 6210, Menoko 4800, Sontorius 4140, Zentium 5010; the gap from cheapest to dearest is 2940')

Q.append(dict(
    n=24, orig=48, answer='E', topic='Area & cost',
    question=f"""<p>A company analyses five possible cities to build a 5 storey office building. The {hl('total floor area of the 5 storeys', 'y', 1)} required by the company is {hl('3000 m²', 'g', 1)} and the {hl('total land area', 'y', 2)} required on which to
build it is {hl('600 m²', 'g', 2)}.</p>
<p>The table below gives the land price and construction price in $ per m² in five cities.</p>
{table([['Calypsio', '1000', '450'], ['Jaspoon', '2000', '350'], ['Menoko', '1500', '500'], ['Sontorius', '1300', '400'], ['Zentium', '1600', '350']],
       head=['<i>city</i>', f'<i>construction costs ($ per m²) {hl("of total floor area", "y")}</i>', '<i>land purchase costs ($ per m²)</i>'])}
<p>The cost of building the office is the cost per square metre for the total floor space of all
5 storeys requirements and the plot land area purchase cost.</p>
<p class="stem">What is the {hl('difference in cost', 'b', 3)} to build the office between the {hl('most expensive and least expensive', 'b', 3)} of the five cities lowest and highest estimates for building the office?</p>""",
    options={'A': '$870 000', 'B': '$1 210 000', 'C': '$1 410 000', 'D': '$2 700 000', 'E': '$2 940 000'},
    notes=[(1, 'y', 'Construction is priced on the floor area: 3000 m² (all 5 storeys).'),
           (2, 'y', 'Land is priced on the plot: only 600 m².'),
           (3, 'b', 'Cost every city, then dearest − cheapest.')],
    steps=[
        f"""<p>Cost = 3000 × construction price + 600 × land price. Work in $ thousands:</p>
{calc('Calypsio: 3000 + 270 = <b>3270</b>', 'Jaspoon: 6000 + 210 = <b>6210</b>', 'Menoko: 4500 + 300 = 4800',
      'Sontorius: 3900 + 240 = 4140', 'Zentium: 4800 + 210 = 5010')}
{note('3000 × 1000 = 3 000 000 = 3000 thousand. 600 × 450 = 270 000 = 270 thousand. Keeping everything in thousands saves writing zeros.', 'tip')}""",
        f"""{_offices()}{calc(f'6 210 000 − 3 270 000 = {boxed("$2 940 000")}')}
{note('Don’t charge the land on 3000 m²: the building has 5 floors, but it only stands on a 600 m² plot.', 'trap')}""",
    ],
    answer_text='$2 940 000: Jaspoon ($6 210 000) minus Calypsio ($3 270 000).',
    why={'A': '$870 000 is the gap between the two cheapest cities (Sontorius − Calypsio), not the cheapest and the dearest.',
         'B': '$1 210 000 isn’t the gap between any two of the correct totals (3270, 4140, 4800, 5010, 6210 thousand).',
         'C': '$1 410 000 is Jaspoon − Menoko. Menoko isn’t the cheapest city.',
         'D': '$2 700 000 charges the land on the 3000 m² floor area too (Jaspoon 7 050 000 − Calypsio 4 350 000).'},
    fast='3000 × build + 600 × land. Cheapest Calypsio 3.27 m, dearest Jaspoon 6.21 m. Difference 2.94 m.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _paydays():
    cards = [('Feb', 24, '24th'), ('Mar', 24, '24th'), ('Apr', 28, '26th'), ('May', 26, '26th'), ('Jun', 23, '23rd'),
             ('Jul', 28, '26th'), ('Aug', 25, '25th'), ('Sep', 22, '22nd')]
    lengths = [28, 31, 30, 31, 30, 31, 31]
    cw, x0 = 80, 12
    parts, lab = [], []
    for i, (m, thu, paid) in enumerate(cards):
        x = x0 + i * cw
        last = i == len(cards) - 1
        parts.append(rect(x + 4, 60, cw - 12, 96, k='red' if last else 'ink', fill='y' if last else 'paper', sw=2.4 if last else 1.6, rx=8))
        lab.append(text(x + cw / 2 - 2, 84, m, k='ink', size=18, font='scrawl'))
        lab.append(text(x + cw / 2 - 2, 110, f'Thu {thu}', k='pen', size=15))
        lab.append(text(x + cw / 2 - 2, 138, 'paid ' + paid, k='red' if last else 'green', size=15))
    for i, L in enumerate(lengths):
        x = x0 + (i + 1) * cw - 4
        shift = {28: '+0', 30: '−2', 31: '−3'}[L]
        lab.append(text(x, 44, shift, k='orange', size=15))
        lab.append(text(x, 180, f'{L} d', k='muted', size=13))
    lab += [text(330, 20, '4th Thursday moves back by (days in month − 28); add 7 if it drops below 22', k='orange', size=15),
            text(330, 212, 'two 24ths in a row → only February (28 days) keeps the date', k='ink', size=16)]
    return svg(660, 224, rough(*parts) + ''.join(lab),
               'Month cards February to September with the fourth Thursday and pay date: 24, 24, 26, 26, 23, 26, 25, then 22 in September')

Q.append(dict(
    n=25, orig=50, answer='A', topic='Calendars',
    question=f"""<p>The company that I currently work for pays its employees monthly. Pay day is {hl('the fourth Thursday of every month or the 26th, whichever is earlier', 'y', 1)}. Since I joined the company the dates
on which I have been paid (in order) have been:</p>
<p>{hl('24<sup>th</sup><br>24<sup>th</sup>', 'g', 2)}<br>26<sup>th</sup><br>26<sup>th</sup><br>23<sup>rd</sup><br>26<sup>th</sup><br>{hl('25<sup>th</sup> (last month)', 'g', 3)}</p>
<p class="stem">On what date will I be paid {hl('this month', 'b', 4)}?</p>""",
    options={'A': '22nd', 'B': '23rd', 'C': '24th', 'D': '25th', 'E': '26th'},
    notes=[(1, 'y', 'The 4th Thursday is always the 22nd to 28th. If it’s the 26th, 27th or 28th, pay day is the 26th instead.'),
           (2, 'g', 'Same date two months running: the clue that unlocks the months.'),
           (3, 'g', 'A real Thursday (25th is before the 26th).'),
           (4, 'b', 'The month after the 25th.')],
    steps=[
        f"""<p>How does the 4th Thursday move from one month to the next? Four weeks is 28 days, so:</p>
{calc('28-day month (February): same date', '30-day month: 2 days earlier', '31-day month: 3 days earlier',
      '(if that drops below the 22nd, add 7: the date jumps a week later)')}""",
        f"""<p>Paid the 24th twice in a row, so the date didn’t move: the first of those months had 28 days. That’s <b>February</b>.
Now follow the months:</p>{_paydays()}
{calc('Mar 24 − 3 = 21, too early, + 7 = 28 (Apr) → paid 26th ' + tick(), 'Apr 28 − 2 = 26 (May) → paid 26th ' + tick(),
      'May 26 − 3 = 23 (Jun) → paid 23rd ' + tick(), 'Jun 23 − 2 = 21, + 7 = 28 (Jul) → paid 26th ' + tick(),
      'Jul 28 − 3 = 25 (Aug) → paid 25th ' + tick(), f'Aug 25 − 3 = {boxed("22nd")} in September')}""",
        f"""{note('Real calendar check: in 2022 the 4th Thursdays were 24 Feb, 24 Mar, 28 Apr, 26 May, 23 Jun, 28 Jul, 25 Aug and 22 Sep.', 'check')}""",
    ],
    answer_text='The 22nd: last month was August (31 days), so the 4th Thursday moves back 3 days from the 25th.',
    why={'B': '23rd moves back only 2 days, as if last month had 30 days. It was August, with 31.',
         'C': '24th moves back only 1 day. No month has 29 days except a leap February, and last month was August.',
         'D': '25th keeps last month’s date, which only happens after a 28-day February.',
         'E': '26th would need the 4th Thursday to be the 26th or later, but it moves back from the 25th.'},
    fast='Two 24ths in a row = February then March. Step on: Apr 28, May 26, Jun 23, Jul 28, Aug 25, so Sep 22.',
))
