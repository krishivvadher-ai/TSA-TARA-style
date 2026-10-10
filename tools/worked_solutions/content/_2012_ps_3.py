import math
from wslib import *

Y = 2012
Q = []


# ---------------------------------------------------------------- 18 (Q37)
def _race_table():
    names = ['Damon', 'Nigel', 'Michael', 'David', 'James']
    rows = [('Rague', [10, 1, 5, 3, 8, 2, 1, '', 1, '']), ('Kolm', [11, '', 6, '', 16, 2, 11, 1, 6, 3]),
            ('Ostrov', [19, 2, 11, 3, 17, '', 12, '', 16, 1]), ('Vostok', [29, 1, 19, 2, 18, '', 13, '', 21, 3]),
            ('Billard', [39, 1, 27, 2, 23, 3, 14, '', 22, '']), ('Menz', [47, 2, 28, '', 24, '', 24, 1, 27, 3]),
            ('Fondra', [48, '', 38, 1, 32, 2, 25, '', 32, 3]), ('Hahn', [49, '', 43, 3, 40, 2, 35, 1, 33, '']),
            ('Limberg', [50, '', 51, 2, 41, '', 45, 1, 38, 3])]
    head1 = '<tr><th colspan="11">Running Points Total and Placings</th></tr>'
    head2 = '<tr><th></th>' + ''.join(f'<th colspan="2">{n}</th>' for n in names) + '</tr>'
    head3 = '<tr><th>Circuit</th>' + '<th>Total</th><th>Pl.</th>' * 5 + '</tr>'
    body = ''
    for circ, v in rows:
        cells = [str(x) for x in v]
        if circ == 'Fondra':
            cells[0] = hl(cells[0], 'g')
            cells[6] = hl(cells[6], 'g')
        body += f'<tr><td style="text-align:left">{circ}</td>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>'
    return (f'<div class="tbl-wrap"><table class="ptable"><thead>{head1}{head2}{head3}</thead>'
            f'<tbody>{body}</tbody></table></div>')


def _catchup():
    panels = [('after Billard (race 5)', 4, 39, 14), ('after Menz (race 6)', 3, 47, 24), ('after Fondra (race 7)', 2, 48, 25)]
    s = 4.0
    parts, lab = [], []
    for i, (title, left, damon, david) in enumerate(panels):
        y = 30 + i * 92
        lab.append(text(20, y + 14, title, k='ink', size=17, anchor='start', font='scrawl'))
        parts.append(rect(200, y, david * s, 30, k='ink', fill='b', sw=1.6))
        parts.append(rect(200 + david * s, y, left * 10 * s, 30, k='pen', fill='paper', sw=1.6))
        parts.append(line(200 + damon * s, y - 10, 200 + damon * s, y + 42, k='red', w=2.6))
        best = david + 10 * left
        ok = best > damon
        lab += [text(200 + david * s / 2, y + 21, f'{david}', k='ink', size=15),
                text(200 + max(david + 10 * left, damon) * s + 10, y + 21, f'+{10 * left} if he wins the rest', k='pen', size=15, anchor='start'),
                text(200 + damon * s, y + 60, f'Damon {damon}', k='red', size=15),
                text(30, y + 44, f'David best {best}', k='green' if ok else 'red', size=16, anchor='start'),
                text(30, y + 64, 'can still win' if ok else 'CANNOT win', k='green' if ok else 'red', size=16, anchor='start', weight='700' if not ok else None)]
    return svg(640, 300, rough(*parts) + ''.join(lab),
               'David’s total plus 10 points for every race left, against Damon’s total: after Billard 54 v 39, after Menz 54 v 47, after Fondra 45 v 48 so David cannot win')


Q.append(dict(
    n=18, orig=37, answer='C', topic='Tables & points',
    question=f"""<p>The Ruritanian Go Kart Drivers' Championship is decided over a series of {hl('9 races', 'g', 1)}. For each event
{hl('the winner is allocated 10 points, second gets 8 points and third gets 5 points. All other finishers are given 1 point', 'y', 2)}. The championship leaders' placings are shown below and the drivers all finished in
each race.</p>
{_race_table()}
<p class="stem">Which was the {hl('earliest race after which one of the leaders knew he could not win', 'b', 3)} the Drivers'
Championship?</p>""",
    options={'A': 'Billard', 'B': 'Menz', 'C': 'Fondra', 'D': 'Hahn', 'E': 'Limberg'},
    notes=[(1, 'g', 'The table lists all 9 races, so you can count how many are left after each one.'),
           (2, 'y', 'Most a driver can gain in a race = 10 points. A blank “Pl.” means he finished outside the top 3 (1 point).'),
           (3, 'b', 'Look for the first time someone’s best possible total falls below the leader’s current total.')],
    steps=[
        f"""<p>A driver is <b>definitely out</b> once his total plus 10 points for every race left is less than the leader’s total now.
Races left: after race 5 (Billard) 4, after Menz 3, after Fondra 2, after Hahn 1.</p>""",
        f"""<p>The driver furthest behind Damon is David. Check him race by race:</p>{_catchup()}
{calc(f'after Billard: 14 + 40 = 54 &gt; 39 {ar()} still possible',
      f'after Menz: 24 + 30 = 54 &gt; 47 {ar()} still possible (Michael is on 24 too)',
      f'after Fondra: 25 + 20 = 45 &lt; 48 {ar()} David can’t win')}
<p>The earliest race is {boxed('Fondra')}.</p>""",
        f"""{note('Damon also scores at least 1 point in every race, which only makes it harder for David. It doesn’t change the answer.', 'check')}""",
    ],
    answer_text='Fondra: after it David has 25 with 2 races left, so at most 45, already below Damon’s 48.',
    why={'A': 'After Billard, David (14) could still win all 4 remaining races: 54, well above Damon’s 39.',
         'B': 'After Menz, David and Michael (24 each) could still reach 54 with 3 wins, above Damon’s 47.',
         'D': 'After Hahn, James is knocked out too (33 + 10 = 43 &lt; 49), but David was already out one race earlier.',
         'E': 'Limberg is the last race: Damon learns he has lost (50 v Nigel’s 51), but that is far from the earliest.'},
    fast='Best possible = total + 10 × races left. After Fondra (2 left): David 25 + 20 = 45 &lt; Damon’s 48. Earlier races still leave him a chance.',
))


# ---------------------------------------------------------------- 19 (Q38)
def _offcuts():
    s = 38
    parts, lab = [], []
    specs = [('A', 4.5, 3.7, 20, 40, '1.1 m strip: too narrow', 'red'),
             ('B', 5.0, 4.0, 240, 40, '1.4 m strip: too narrow', 'red'),
             ('C', 4.2, 4.4, 470, 40, '1.8 m strip: lobby fits ✓', 'green'),
             ('D', 5.8, 2.6, 20, 284, '1.6 m left: too narrow', 'red'),
             ('E', 4.8, 4.0, 300, 284, '1.4 m strip: too narrow', 'red')]
    for name, w, h, x, y, msg, col in specs:
        parts.append(rect(x, y, w * s, h * s, k='ink', fill='paper', sw=2))
        if name == 'D':
            parts.append(rect(x, y, 4.2 * s, 2.6 * s, k='pen', fill='b', sw=1.6))
            lab.append(text(x + 2.1 * s, y + 1.3 * s + 5, 'office 4.2 × 2.6', k='pen', size=14))
            parts.append(rect(x + 4.2 * s, y, (w - 4.2) * s, h * s, k=col, fill='p', sw=1.4))
        else:
            parts.append(rect(x, y, 4.2 * s, 2.6 * s, k='pen', fill='b', sw=1.6))
            lab.append(text(x + 2.1 * s, y + 1.3 * s + 5, 'office 4.2 × 2.6', k='pen', size=14))
            parts.append(rect(x, y + 2.6 * s, w * s, (h - 2.6) * s, k=col, fill='g' if col == 'green' else 'p', sw=1.4))
            if name == 'C':
                parts.append(rect(x + 4, y + 2.6 * s + 3, 2.2 * s, 1.8 * s - 6, k='green', fill='g', sw=2))
                lab.append(text(x + 1.1 * s + 4, y + 3.5 * s + 5, 'lobby 2.2 × 1.8', k='green', size=14))
        lab += [text(x + w * s / 2, y - 10, f'{name}: {w} × {h} m', k='ink', size=17, font='scrawl'),
                text(x + w * s / 2, y + h * s + 22, msg, k=col, size=15)]
    return svg(660, 470, rough(*parts) + ''.join(lab),
               'Each offcut drawn to scale with the 4.2 by 2.6 m office placed in it; only in C is the leftover strip 1.8 m wide, enough for the 2.2 by 1.8 m lobby')


Q.append(dict(
    n=19, orig=38, answer='C', topic='Area & fitting shapes',
    question=f"""<p>The diagram shows the dimensions of an office and entrance lobby. I wish to carpet them. {hl('Each must have a single piece of carpet with no joins', 'y', 1)}, but {hl('I can use two separate pieces for the two rooms', 'y', 2)}. As I intend to do it as inexpensively as possible, I will buy {hl('an offcut', 'p', 3)}.</p>
{fig(Y, 'ps_q19_plan', 'Plan: lobby 2.2 m by 1.8 m next to an office 2.6 m wide and 4.2 m long', 380)}
<p class="stem">Which of the following offcut pieces will be {hl('suitable', 'b', 4)}?</p>""",
    options={'A': '4.5 x 3.7 m', 'B': '5.0 x 4.0 m', 'C': '4.2 x 4.4 m', 'D': '2.6 x 5.8 m', 'E': '4.8 x 4.0 m'},
    notes=[(1, 'y', 'Each room needs a whole rectangle: office 4.2 × 2.6, lobby 2.2 × 1.8.'),
           (2, 'y', 'Both rectangles get cut from the <b>one</b> offcut.'),
           (3, 'p', 'One offcut only. Big enough in area is not the same as the right shape!'),
           (4, 'b', 'Can both rectangles be cut out of it, side by side?')],
    steps=[
        f"""<p>The office needs a side of at least 4.2 m, so lay the office along a long side. Then the lobby (2.2 × 1.8) has to fit in what is left:
a strip at least <b>1.8 m wide</b> and 2.2 m long.</p>{_offcuts()}""",
        f"""{calc('A: 3.7 − 2.6 = 1.1 m ✗ (and 4.5 − 4.2 = 0.3 m)', 'B: 4.0 − 2.6 = 1.4 m ✗', f'C: 4.4 − 2.6 = 1.8 m, strip 4.2 long ✓ {ar()} {boxed("C")}',
                  'D: 5.8 − 4.2 = 1.6 m ✗', 'E: 4.0 − 2.6 = 1.4 m ✗')}
{note('Area alone fools you: B is 20 m², far more than the 14.88 m² needed, but its leftover strip is the wrong shape.', 'trap')}""",
    ],
    answer_text='4.2 × 4.4 m: the office takes 4.2 × 2.6, leaving a 4.2 × 1.8 strip for the 2.2 × 1.8 lobby.',
    why={'A': 'After the office, A leaves strips only 1.1 m and 0.3 m wide. The lobby needs 1.8 m.',
         'B': 'B has plenty of area (20 m²), but the strips left are 1.4 m and 0.8 m wide.',
         'D': 'D is exactly the office’s width, leaving 2.6 × 1.6: 0.2 m too short for the lobby’s 1.8 m.',
         'E': 'E leaves strips 1.4 m and 0.6 m wide: too narrow for the lobby.'},
    fast='Office uses 2.6 of one side, so the other side must be at least 2.6 + 1.8 = 4.4 (with 4.2 the other way). Only 4.2 × 4.4.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _clock():
    cx, cy, r = 235, 150, 105
    parts, lab = [], []
    parts.append(circle(cx, cy, r, k='ink', fill='paper', sw=2.4))
    # right half (12 -> 6), fast
    parts.append(path(f'M{cx} {cy - r - 14} A{r + 14} {r + 14} 0 0 1 {cx} {cy + r + 14}', k='pen', sw=3.2))
    # left half (6 -> 12), slow
    parts.append(path(f'M{cx} {cy + r + 14} A{r + 14} {r + 14} 0 0 1 {cx} {cy - r - 14}', k='orange', sw=3.2))
    for i in range(12):
        a = math.radians(i * 30 - 90)
        parts.append(line(cx + (r - 9) * math.cos(a), cy + (r - 9) * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a), k='ink', w=1.6))
    parts.append(line(cx, cy, cx - r + 18, cy, k='red', w=3.2))
    parts.append(circle(cx, cy, 5, k='ink', fill='ink'))
    lab += [text(cx, cy - r + 26, '12', k='ink', size=17), text(cx, cy + r - 14, '6', k='ink', size=17),
            text(cx + r - 22, cy + 6, '3', k='ink', size=17), text(cx - r + 22, cy - 12, '9', k='ink', size=17),
            text(cx + r + 30, cy - 70, 'down: fast', k='pen', size=17, anchor='start'),
            text(cx + r + 30, cy - 48, '15 min', k='pen', size=20, anchor='start', font='scrawl'),
            text(cx - r - 30, cy + 70, 'up: slow', k='orange', size=17, anchor='end'),
            text(cx - r - 30, cy + 92, '45 min', k='orange', size=20, anchor='end', font='scrawl'),
            text(cx + r + 30, cy + 30, 'shows quarter to (at 9):', k='red', size=16, anchor='start'),
            text(cx + r + 30, cy + 52, '15 + 22.5 = 37.5 min past', k='red', size=16, anchor='start'),
            text(cx + r + 30, cy + 74, '= 22.5 minutes to', k='red', size=20, anchor='start', font='scrawl')]
    return svg(600, 300, rough(*parts) + ''.join(lab),
               'Clock face: the minute hand takes 15 minutes from 12 down to 6 and 45 minutes from 6 back up to 12; at 9 it is 37.5 minutes past')


Q.append(dict(
    n=20, orig=42, answer='D', topic='Clocks & speed',
    question=f"""<p>The Tickton town hall clock is rather a curiosity. It {hl('shows the correct time every hour on the hour', 'y', 1)},
but the minute hand travels {hl('three times as fast down to 6 as it does back up to 12', 'y', 2)}, though {hl('within each half of its revolution its speed is constant', 'y', 3)}.</p>
<p class="stem">What is the correct time when the Tickton town hall clock {hl('shows quarter to the hour', 'b', 4)}?</p>""",
    options={'A': '7.5 minutes to the hour', 'B': '10 minutes to the hour', 'C': '20 minutes to the hour',
             'D': '22.5 minutes to the hour', 'E': '25 minutes to the hour'},
    notes=[(1, 'y', 'One full lap of the hand still takes exactly 60 real minutes.'),
           (2, 'y', '3 times as fast = a third of the time. Down : up = 1 : 3.'),
           (3, 'y', 'Steady within a half, so halfway up takes half of the “up” time.'),
           (4, 'b', 'Quarter to = the hand points at 9, halfway up the slow side.')],
    steps=[
        f"""<p>Split the hour in the ratio 1 : 3 (fast down, slow up):</p>
{calc('1 + 3 = 4 parts = 60 minutes → 1 part = 15 minutes', '12 → 6 takes <b>15 min</b>; 6 → 12 takes <b>45 min</b>')}""",
        f"""{_clock()}
{calc('the hand reaches 6 at 15 minutes past', '6 → 9 is half of the slow climb: 45 ÷ 2 = 22.5 min',
      f'real time = 15 + 22.5 = 37.5 min past {ar()} 60 − 37.5 = {boxed("22.5 minutes to")}')}""",
    ],
    answer_text='22.5 minutes to the hour: the hand reaches 6 after 15 minutes, then needs 22.5 of its 45 slow minutes to climb to 9.',
    why={'A': '7.5 minutes to gets the speeds the wrong way round (slow down for 45 minutes, fast up for 15).',
         'B': '10 to the hour means 6 → 9 took 35 minutes but 9 → 12 only 10. The speed is steady on the way up, so those must be equal.',
         'C': '20 to the hour splits the hour into thirds (20 down, 40 up) instead of quarters. “Three times as fast” makes it 15 and 45.',
         'E': '25 to the hour means 6 → 9 took 20 minutes and 9 → 12 took 25: unequal, so the speed would change on the way up.'},
    fast='Down 15 min, up 45 min. 9 is halfway up: 15 + 22.5 = 37.5 past, i.e. 22.5 to.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _skybars():
    rows = [('Avonmouth', (16, 25), (19, 9)), ('Dun Laoghaire', (16, 45), (19, 22)), ('Greenock', (16, 49), (19, 18)),
            ('Leith', (16, 43), (19, 11)), ('London', (16, 12), (18, 56))]
    X = lambda h, m: 180 + (h + m / 60 - 16) * 120
    parts, lab = [], []
    for h in (16, 17, 18, 19):
        parts.append(line(X(h, 0), 24, X(h, 0), 222, k='muted', w=1, dash=True))
        lab.append(text(X(h, 0), 240, f'{h}:00', k='muted', size=14))
    for i, (town, (h1, m1), (h2, m2)) in enumerate(rows):
        y = 32 + i * 38
        mins = (h2 * 60 + m2) - (h1 * 60 + m1)
        best = town == 'Leith'
        parts.append(rect(X(h1, m1), y, X(h2, m2) - X(h1, m1), 26, k='ink', fill='g' if best else 'y', sw=1.6))
        lab += [text(170, y + 19, town, k='ink', size=16, anchor='end'),
                text((X(h1, m1) + X(h2, m2)) / 2, y + 19, f'{mins // 60} h {mins % 60:02d}', k='green' if best else 'ink', size=16, weight='700' if best else None)]
    lab.append(text(380, 262, 'bar = moonrise to sunset (both in the sky)', k='ink', size=16))
    return svg(640, 274, rough(*parts) + ''.join(lab),
               'Bars from moonrise to sunset: Avonmouth 2 h 44, Dun Laoghaire 2 h 37, Greenock 2 h 29, Leith 2 h 28, London 2 h 44')


Q.append(dict(
    n=21, orig=43, answer='D', topic='Time intervals',
    question=f"""<p>The table below shows the times of sunrise and sunset and moonrise and moonset for certain
towns on the same day (in hours:minutes).</p>
{table([['Avonmouth', '06:57', '19:09', '16:25', '00:56'], ['Dun Laoghaire', '07:10', '19:22', '16:45', '01:02'],
        ['Greenock', '07:05', '19:18', '16:49', '00:46'], ['Hull', '06:47', '18:59', '16:22', '00:36'],
        ['Leith', '06:58', '19:11', '16:43', '00:39'], ['Liverpool', '06:58', '19:10', '16:32', '00:49'],
        ['London', '06:45', '18:56', '16:12', '00:42']],
       head=['', 'Sunrise', hl('Sunset', 'g', 1), hl('Moonrise', 'g', 1), hl('Moonset', 'p', 2)])}
<p class="stem">In which of the towns are the {hl('sun and moon in the sky together', 'b', 3)} for the {hl('shortest', 'b', 3)} time?</p>""",
    options={'A': 'Avonmouth', 'B': 'Dun Laoghaire', 'C': 'Greenock', 'D': 'Leith', 'E': 'London'},
    notes=[(1, 'g', 'The moon rises in the afternoon while the sun is still up. Together from moonrise until sunset.'),
           (2, 'p', 'The moon sets just after midnight, long after sunset (and before the next sunrise), so it adds nothing.'),
           (3, 'b', 'Work out sunset − moonrise for the five options and pick the smallest.')],
    steps=[
        f"""<p>Both are up from <b>moonrise</b> (about 4.30 pm) until <b>sunset</b> (about 7 pm). The moonset and sunrise columns are red herrings.</p>{_skybars()}""",
        f"""{calc('Avonmouth: 16:25 → 19:09 = 2 h 44', 'Dun Laoghaire: 16:45 → 19:22 = 2 h 37', 'Greenock: 16:49 → 19:18 = 2 h 29',
                  f'Leith: 16:43 → 19:11 = 2 h 28 {ar()} shortest', 'London: 16:12 → 18:56 = 2 h 44')}
{note('Count up in chunks: 16:43 → 17:00 is 17 min, → 19:00 is 2 h 17, → 19:11 is 2 h 28.', 'tip')}
{calc(f'answer = {boxed("Leith")}')}""",
    ],
    answer_text='Leith: the sun and moon share the sky for 2 h 28 min, one minute less than Greenock.',
    why={'A': 'Avonmouth: 2 h 44, one of the longest.',
         'B': 'Dun Laoghaire: 2 h 37.',
         'C': 'Greenock is the trap: 2 h 29, just one minute longer than Leith. (It has the latest moonrise, but not the shortest gap.)',
         'E': 'London: 2 h 44. It has the earliest sunset, but also the earliest moonrise.'},
    fast='Together = sunset − moonrise. Leith 2 h 28 beats Greenock 2 h 29.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _skeletons():
    c = 22
    parts, lab = [], []
    flat = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3), (-1, 2), (-2, 2)]

    def panel(ox, oy, cells, outs, title, sub):
        p, l = [], []
        for (x, y) in cells:
            p.append(rect(ox + x * c, oy + y * c, c, c, k='ink', fill='b', sw=1.4))
        for (x, y), toward in outs:
            cx, cy = ox + x * c + c / 2, oy + y * c + c / 2
            p.append(rect(ox + x * c, oy + y * c, c, c, k='ink', fill='o', sw=1.4))
            p.append(circle(cx, cy, 8, k='red' if not toward else 'green', fill='paper', sw=1.8))
            if toward:
                p.append(circle(cx, cy, 2.4, k='green', fill='ink', sw=1))
            else:
                p += [line(cx - 5, cy - 5, cx + 5, cy + 5, k='red', w=1.8), line(cx - 5, cy + 5, cx + 5, cy - 5, k='red', w=1.8)]
        l += [text(ox + c, oy - 34, title, k='ink', size=17, font='scrawl'), text(ox + c, oy - 14, sub, k='muted', size=13)]
        return p, l

    specs = [(80, 'A', 'from above', [((2, 0), True)], flat),
             (240, 'D', 'from its left side', [((2, 0), True)], flat),
             (400, 'C', 'from the front', [((2, 0), False)], flat)]
    for ox, name, sub, outs, cells in specs:
        p, l = panel(ox, 70, cells, outs, name, sub)
        parts += p
        lab += l
    lflat = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3)]
    p, l = panel(560, 70, lflat, [((2, 0), True), ((0, 2), False)], 'B and E', 'both stubs stick out')
    parts += p
    lab += l
    lab += [text(56, 190, 'blue = the flat part (the L, plus a flat 2-cube stub in A, D, C)', k='pen', size=15, anchor='start'),
            text(56, 212, 'orange = where the other 2-cube stub sticks out:', k='orange', size=15, anchor='start'),
            text(56, 234, '⊙ towards you    ⊗ away from you', k='ink', size=15, anchor='start'),
            text(290, 262, 'A = D,  B = E,  C is the mirror image of A and D', k='red', size=18, font='scrawl')]
    return svg(680, 276, rough(*parts) + ''.join(lab),
               'Each solid drawn as its flat part with the sticking-out stub marked: A and D point towards you, C points away, B and E have stubs in opposite directions')


Q.append(dict(
    n=22, orig=44, answer='C', topic='3D shapes & mirror images',
    question=f"""<p>Five pictures of solids made by {hl('sticking cubes together', 'y', 1)} are shown below.</p>
<p class="stem">Which one of the following (A-E) is a different shape from {hl('<b>all</b> the others', 'b', 2)}?</p>
{fig(Y, 'ps_q22_solids', 'Five solids A to E made of cubes, drawn from different angles', 640)}""",
    options={'A': 'solid A', 'B': 'solid B', 'C': 'solid C', 'D': 'solid D', 'E': 'solid E'},
    notes=[(1, 'y', 'Each solid can be turned any way, so describe it by its structure, not by how it is drawn.'),
           (2, 'b', '“All” is the key word: the shapes come in matching <b>pairs</b>, and one is left without a partner.')],
    steps=[
        f"""<p>Count the cubes: every solid has 11, so that doesn’t help. Look for the skeleton instead. Each solid is:</p>
<ul><li>a <b>corner cube</b> with two straight arms at right angles, each <b>4 cubes</b> long (counting the corner);</li>
<li>plus two 2-cube <b>stubs</b>, one on the 3rd cube of each arm (counting from the corner).</li></ul>
<p>So the only difference is <b>which way the two stubs point</b>.</p>""",
        f"""<p>Find the stubs in each picture:</p>
<ul><li><b>A</b>: the arms lie flat on the table. One stub lies flat too (pointing away from the other arm); the other is the tower going <b>up</b>.</li>
<li><b>D</b>: the arms are the tall column and the arm coming forward. One stub hangs down (in the same flat plane, pointing away from the column); the other sticks out <b>sideways</b> to the left.</li>
<li><b>C</b>: the arms are the column and the bottom row. One stub hangs down (flat, pointing away from the column); the other goes <b>backwards</b> from near the top of the column.</li>
<li><b>B</b>: arms = column and bottom row. One stub comes forwards along the floor, the other goes backwards from the column: <b>opposite</b> ways, both out of the flat L.</li>
<li><b>E</b>: arms flat on the table. One stub goes up, the other hangs down: again <b>opposite</b> ways, both out of the L.</li></ul>
{calc(f'B and E have both stubs sticking out in opposite directions {ar()} <b>B = E</b>')}""",
        f"""<p>A, C and D all have one flat stub and one sticking-out stub. Now check which way it sticks out.
Turn each one so its flat part looks the same (corner top-left, arms going right and down, flat stub pointing left):</p>{_skeletons()}
<p>In A and D the sticking-out stub comes <b>towards</b> you; in C it goes <b>away</b>. So <b>A = D</b>, and C is their mirror image.</p>
{calc(f'pairs: A–D and B–E {ar()} the one with no partner is {boxed("C")}')}""",
        f"""{note('In the exam you don’t need to prove the mirror image. Once you spot that A matches D and B matches E, C must be the answer.', 'tip')}""",
    ],
    answer_text='C: A and D are the same solid, B and E are the same solid, and C (a mirror image of A and D) matches none of them.',
    why={'A': 'A is the same solid as D (turn D so its column lies flat on the table).',
         'B': 'B is the same solid as E: both have their two stubs pointing in opposite directions.',
         'D': 'D is the same solid as A: same flat part, and the extra stub sticks out on the same side.',
         'E': 'E is the same solid as B.'},
    fast='Same skeleton every time: two 4-cube arms with a 2-cube stub on each. Pair them by stub directions: A–D, B–E. C is left over.',
))


# ---------------------------------------------------------------- 23 (Q48)
def _votes():
    rows = [('Green', 87, 0), ('Johnson', 63, 0), ('Gonzalez', 45, 0), ('McBride', 36, 0), ('Daniels', 18, 17), ('Mathur', 17, 0)]
    X = lambda v: 130 + v * 3.4
    parts, lab = [], []
    for i, (name, v, extra) in enumerate(rows):
        y = 26 + i * 34
        f = 'p' if name in ('Daniels', 'Mathur') else 'g'
        parts.append(rect(X(0), y, X(v) - X(0), 24, k='ink', fill=f, sw=1.6))
        if extra:
            parts.append(rect(X(v), y, X(v + extra) - X(v), 24, k='red', fill='paper', sw=1.6))
            lab.append(text(X(v + extra) + 8, y + 18, f'18 + 17 = 35 at best', k='red', size=15, anchor='start'))
        else:
            lab.append(text(X(v) + 8, y + 18, f'{v}' + ('  (bottom: out first)' if name == 'Mathur' else ''), k='ink', size=15, anchor='start'))
        lab.append(text(120, y + 18, name, k='ink', size=16, anchor='end'))
    parts.append(line(X(36), 20, X(36), 230, k='orange', w=2.2, dash=True))
    lab.append(text(X(36), 250, 'McBride 36', k='orange', size=15))
    lab.append(text(X(36) + 150, 250, 'Daniels can never pass him', k='red', size=15))
    return svg(640, 262, rough(*parts) + ''.join(lab),
               'First-round votes; even with all 17 of Mathur’s votes Daniels reaches only 35, below McBride’s 36, so Daniels drops out next')


Q.append(dict(
    n=23, orig=48, answer='D', topic='Voting systems',
    question=f"""<p>In the elections for the mayor of Bitton, the single transferable vote system is used. In this, each
voter places a '1' beside the candidate they most want and a '2' beside their second choice. {hl('Voters may only vote for two candidates', 'p', 1)}. In the first round of counting all the '1' votes are counted. {hl("If no candidate has over 50% of the votes, the bottom candidate in the poll drops out and the '2' votes of all those who voted for this candidate are added to the appropriate other candidates", 'y', 2)}. This process
continues until one candidate has {hl('over 50% of the vote', 'g', 3)} - this person is then elected mayor.</p>
<p>The votes after the first round of counting were as follows:</p>
<p>Malcolm Green 87<br>Susan Johnson 63<br>Pedro Gonzalez 45<br>Ian McBride 36<br>{hl('Wayne Daniels 18', 'p')}<br>{hl('Reeta Mathur 17', 'p')}<br>Total votes cast 254</p>
<p class="stem">How many candidates {hl('can still win', 'b', 4)}?</p>""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'p', 'Only a first and second choice. Votes can move on to someone else.'),
           (2, 'y', 'The bottom candidate drops out each round and their voters’ second choices get passed on.'),
           (3, 'g', 'Over 50% of 254 = more than 127, so 128 votes.'),
           (4, 'b', 'Who has <b>any</b> possible way to win, with the luckiest transfers?')],
    steps=[
        f"""<p>Mathur (17) is bottom, so she drops out first. Could Daniels then survive?</p>{_votes()}
<p>Even if every one of Mathur’s 17 voters picked Daniels second, he reaches only 35, still below McBride’s 36. So Daniels is bottom next and drops out: <b>Daniels can’t win</b>.</p>""",
        f"""<p>Everyone else has a route to 128 with lucky transfers. The hardest case is McBride:</p>
{calc(f'36 + 17 (Mathur’s) + 18 (Daniels’) = 71 {ar()} now Gonzalez (45) is bottom and drops out',
      f'71 + 45 = 116 {ar()} now Johnson (63) is bottom and drops out',
      '116 + 63 = 179 → over 127, McBride wins')}
<p>Gonzalez can win the same way, and Green and Johnson obviously can.</p>
{calc(f'Green, Johnson, Gonzalez, McBride {ar()} {boxed("4")}')}""",
    ],
    answer_text='4: Green, Johnson, Gonzalez and McBride. Mathur is out now, and Daniels can never pass McBride.',
    why={'A': '1 assumes the leader must win, but transfers can overturn an 87-vote lead (nobody has 128 yet).',
         'B': '2 forgets that low candidates can collect transfers: Gonzalez and McBride could still reach 128.',
         'C': '3 stops at Gonzalez, but McBride (36) can win too if the transfers keep coming his way.',
         'E': '5 includes Daniels, but even all of Mathur’s votes take him only to 35, behind McBride’s 36.'},
    fast='Need 128. Mathur goes first; Daniels at most 18 + 17 = 35 &lt; 36, so he goes next. Everyone above can be built up to 128. Answer 4.',
))


# ---------------------------------------------------------------- 24 (Q49)
def _bulbs():
    parts, lab = [], []
    s = 20
    parts += [rect(150, 40, 15 * s, 34, k='ink', fill='p', sw=1.6), rect(150, 100, 3 * s, 34, k='ink', fill='g', sw=1.6),
              rect(150 + 3 * s, 100, 12 * s, 34, k='green', fill='paper', sw=1.6)]
    lab += [text(140, 63, '100 W bulb', k='ink', size=16, anchor='end'), text(150 + 7.5 * s, 63, '15p a week', k='ink', size=16),
            text(140, 123, '20 W bulb', k='ink', size=16, anchor='end'), text(150 + 1.5 * s, 123, '3p', k='ink', size=16),
            text(150 + 9 * s, 123, 'saves 12p a week', k='green', size=17, font='scrawl'),
            text(310, 172, 'extra cost to win back: £10 − 40p = 960p', k='pen', size=17),
            text(310, 200, '960 ÷ 12 = 80 weeks', k='red', size=22, font='scrawl')]
    return svg(620, 214, rough(*parts) + ''.join(lab),
               'Weekly running cost: 15p for the 100 W bulb against 3p for the 20 W bulb, saving 12p a week; 960p extra cost takes 80 weeks to win back')


Q.append(dict(
    n=24, orig=49, answer='C', topic='Rates & payback',
    question=f"""<p>Standard 100W light bulbs cost {hl('40p each', 'g', 1)} and are expected to last for 2 years in average use. Low
power equivalent brightness bulbs cost {hl('£10 each', 'g', 1)}, are expected to last for 8 years and use only
20W. {hl('A 100W lightbulb operated for 10 hours will use 7.5p of electricity', 'y', 2)}. {hl('A 20W bulb will operate for 50 hours on the same amount of electricity', 'y', 2)}. I have a light in my living room which is on for about {hl('20 hours per week', 'g', 3)}. Next time the living room bulb breaks, I will buy a low wattage bulb {hl('instead of a standard one', 'p', 4)}.</p>
<p class="stem">How long will it be before I have {hl('recovered the extra purchase cost', 'b', 5)}?</p>""",
    options={'A': '70 weeks', 'B': '77 weeks', 'C': '80 weeks', 'D': '83 weeks', 'E': '96 weeks'},
    notes=[(1, 'g', 'The two prices: the <b>difference</b> is what you have to win back.'),
           (2, 'y', 'Both cost 7.5p: 10 hours for the 100 W bulb, 50 hours for the 20 W bulb.'),
           (3, 'g', '20 hours = 2 lots of 10 hours.'),
           (4, 'p', 'You were going to spend 40p anyway, so the extra is only £10 − 40p.'),
           (5, 'b', 'Weeks until the weekly savings add up to the extra cost.')],
    steps=[
        f"""{calc('extra purchase cost = £10 − 40p = <b>960p</b>')}""",
        f"""<p>Running cost for one week (20 hours):</p>
{calc(f'100 W: 20 h = 2 × 10 h {ar()} 2 × 7.5p = <b>15p</b>', f'20 W: 7.5p per 50 h {ar()} 20 h = {frac(20, 50)} × 7.5p = <b>3p</b>',
      'saving = 15 − 3 = <b>12p a week</b>')}{_bulbs()}""",
        f"""{calc(f'960 ÷ 12 = {boxed("80 weeks")}')}
{note('The lifetimes (2 years, 8 years) are a distraction: you only need the extra price and the weekly saving.', 'trap')}""",
    ],
    answer_text='80 weeks: the extra 960p is won back at 12p a week.',
    why={'A': '70 weeks uses an extra cost of £8.40 (£10 minus four 40p bulbs over 8 years). You only replace one bulb now.',
         'B': '77 weeks uses an extra cost of £9.20 (taking off two standard bulbs instead of one).',
         'D': '83 weeks forgets to take off the 40p: 1000 ÷ 12 ≈ 83.',
         'E': '96 weeks uses a saving of only 10p a week: the 20 W bulb costs 3p a week, not 5p.'},
    fast='Extra 960p. Weekly cost 15p v 3p, saving 12p. 960 ÷ 12 = 80.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _tiles():
    c = 23
    shapes = [('A', 4, 4, [[(0, 0), (0, 1), (1, 1)], [(0, 2), (0, 3), (1, 2)], [(3, 0), (3, 1), (2, 1)], [(3, 2), (3, 3), (2, 2)]], []),
              ('B', 5, 3, [[(0, 0), (1, 0), (0, 1)], [(3, 0), (4, 0), (4, 1)], [(1, 1), (1, 2), (2, 2)], [(2, 1), (3, 1), (3, 2)]], []),
              ('C', 4, 4, [[(0, 0), (1, 0), (0, 1)], [(2, 0), (3, 0), (3, 1)], [(1, 1), (2, 1), (1, 2)], [(2, 2), (1, 3), (2, 3)]], []),
              ('D', 4, 4, [[(1, 0), (2, 0), (2, 1)], [(3, 1), (3, 2), (2, 2)], [(2, 3), (1, 3), (1, 2)], [(0, 2), (0, 1), (1, 1)]], []),
              ('E', 5, 5, [[(0, 1), (1, 1), (1, 2)], [(2, 1), (3, 1), (3, 0)], [(3, 2), (3, 3), (4, 3)], [(1, 3), (1, 4), (2, 3)]], [(2, 2)])]
    fills = ['b', 'g', 'o', 'v']
    parts, lab = [], []
    x = 20
    for name, w, h, ls, extra in shapes:
        oy = 50
        for f, cells in zip(fills, ls):
            for (cx, cy) in cells:
                parts.append(rect(x + cx * c, oy + cy * c, c, c, k='ink', fill=f, sw=1.3))
        for (cx, cy) in extra:
            parts.append(rect(x + cx * c, oy + cy * c, c, c, k='red', fill='p', sw=2.2))
            lab.append(text(x + cx * c + c / 2, oy + cy * c + 17, '?', k='red', size=17, weight='700'))
        n = sum(len(l) for l in ls) + len(extra)
        lab += [text(x + w * c / 2, 36, name, k='ink', size=20, font='print', weight='700'),
                text(x + w * c / 2, oy + 5 * c + 26, f'{n} squares', k='red' if extra else 'green', size=16),
                text(x + w * c / 2, oy + 5 * c + 46, 'impossible ✗' if extra else '4 Ls ✓', k='red' if extra else 'green', size=16, font='scrawl')]
        x += w * c + 26
    return svg(640, 222, rough(*parts) + ''.join(lab),
               'A to D each split into four L-shaped tables of 3 squares; E has 13 squares, so its middle square cannot be covered')


Q.append(dict(
    n=25, orig=50, answer='E', topic='Shapes & tiling',
    question=f"""<p>In the committee room of my cricket club there are {hl('four tables, all identical', 'y', 1)} to the one shown below.</p>
{fig(Y, 'ps_q25_table', 'An L-shaped table made of three equal squares', 93)}
<p class="stem">Which of the following arrangements is it {hl('<b>not</b>', 'b', 2)} possible to make by putting four of these tables
together?</p>
{fig(Y, 'ps_q25_opts', 'Five outlines: A an H shape, B a wide shape with a notch, C a T shape, D a plus sign, E a pinwheel', 446)}""",
    options={'A': 'arrangement A', 'B': 'arrangement B', 'C': 'arrangement C', 'D': 'arrangement D', 'E': 'arrangement E'},
    notes=[(1, 'y', 'Each table is an L of <b>3 squares</b>, so four tables cover exactly <b>12 squares</b>.'),
           (2, 'b', 'Find the outline that can’t be split into four Ls.')],
    steps=[
        f"""<p>Measure each outline in “table squares” (the width of a table arm) and count:</p>
{calc('A 12, B 12, C 12, D 12', f'E: a 5 × 5 pinwheel with <b>13</b> squares {ar()} one too many!')}""",
        f"""<p>Check A to D really split into four Ls, and see what goes wrong with E:</p>{_tiles()}""",
        f"""<p>Four tables in a pinwheel leave a square <b>hole</b> in the middle. Outline E has no hole, so it can’t be made: {boxed('E')}</p>""",
    ],
    answer_text='E: it covers 13 squares (a pinwheel with its middle filled in); four tables only cover 12.',
    why={'A': 'A (the H) splits into four Ls: two down each side.',
         'B': 'B splits into four Ls: one in each top corner and two in the middle.',
         'C': 'C (the T) splits into four Ls: one at each end of the bar, two down the stem.',
         'D': 'D (the plus) splits into four Ls arranged in a ring.'},
    fast='4 tables = 12 squares. Count: A–D have 12, E has 13. E.',
))
