import math
from wslib import *

Y = 2016
Q = []


def _glyph(cx, cy, ch, rot=0, size=40, k='ink', font='print'):
    """A letter centred on (cx, cy), turned rot degrees clockwise."""
    t = text(cx, cy + size * 0.36, ch, k=k, size=size, font=font)
    return f'<g transform="rotate({rot} {cx} {cy})">{t}</g>' if rot else t


# ---------------------------------------------------------------- 1 (Q2)
def _boards():
    order = [(24, 30, 90), (8, 90, 150), (30, 150, 210), (18, 210, 270), (21, 270, 330), (11, 330, 390)]

    def board(cx, cy, r, hits, title):
        parts, lab = [], []
        for num, a0, a1 in order:
            p0 = (cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0)))
            p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
            f = ('g' if num == 18 else 'b') if num in hits else 'paper'
            parts.append(path(f'M{cx} {cy} L{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 0 0 {p1[0]:.1f} {p1[1]:.1f} Z',
                              k='ink', fill=f, sw=1.8))
            am = math.radians((a0 + a1) / 2)
            lab.append(text(cx + r * 0.62 * math.cos(am), cy - r * 0.62 * math.sin(am) + 8, num,
                            k='red' if num == 18 else 'ink', size=24, weight='bold' if num in hits else None))
        lab.append(text(cx, cy + r + 40, title, k='pen', size=24, font='scrawl'))
        return parts, lab

    p1, l1 = board(160, 140, 110, (8, 18, 24), '8 + 18 + 24 = 50')
    p2, l2 = board(480, 140, 110, (11, 18, 21), '11 + 18 + 21 = 50')
    return svg(640, 310, rough(*p1, *p2) + ''.join(l1 + l2),
               'Two copies of the dartboard: one shades 8, 18 and 24, the other shades 11, 18 and 21; 18 is shaded in both')


Q.append(dict(
    n=1, orig=2, answer='C', topic='Number puzzles',
    question=f"""<p>An unusual dartboard is used in a playground game:</p>
{fig(Y, 'ps_q01_board', 'A round dartboard split into six sectors: 8, 24, 11, 21, 18 and 30', 230)}
<p>In order to win the big prize, contestants must score {hl('exactly 50 with three darts', 'g', 1)}, {hl('all of which must be in different sectors', 'y', 2)}.</p>
<p class="stem">Which number {hl('<b>must</b>', 'b', 3)} they hit with one of the three darts in order to score 50?</p>""",
    options={'A': '8', 'B': '11', 'C': '18', 'D': '21', 'E': '24'},
    notes=[(1, 'g', 'Three darts, total exactly 50. No more, no less.'),
           (2, 'y', 'No repeats: three <b>different</b> numbers.'),
           (3, 'b', 'Find <b>every</b> way to make 50. The answer is the number that is in all of them.')],
    steps=[
        f"""<p>Odd and even trick. 50 is even. The only odd numbers on the board are <b>11</b> and <b>21</b>.</p>
{calc('odd: 11, 21', 'even: 8, 18, 24, 30',
      f'even total {ar()} use <b>no</b> odd numbers or <b>both</b> odd numbers')}
{note('One odd number + two even numbers always makes an odd total, so it can never be 50.', 'tip')}""",
        f"""<p>Case 1: both odd numbers.</p>
{calc(f'11 + 21 = 32 {ar()} need 50 − 32 = 18 {tick()} (18 is on the board)')}
<p>Case 2: three even numbers from 8, 18, 24, 30.</p>
{calc(f'any trio with 30: smallest is 30 + 8 + 18 = 56 {cross()} too big',
      f'without 30: 8 + 18 + 24 = 50 {tick()}')}""",
        f"""<p>So there are exactly two winning throws:</p>{_boards()}
{calc(f'18 is in both {ar()} {boxed("18")}')}""",
    ],
    answer_text='18: the only two ways to make 50 are 8 + 18 + 24 and 11 + 18 + 21.',
    why={'A': '8 is only in one way (8 + 18 + 24). You can also win with 11 + 18 + 21, which has no 8.',
         'B': '11 is only in 11 + 18 + 21. The throw 8 + 18 + 24 wins without it.',
         'D': '21 is only in 11 + 18 + 21. The throw 8 + 18 + 24 wins without it.',
         'E': '24 is only in 8 + 18 + 24. The throw 11 + 18 + 21 wins without it.'},
    fast='Even total, so 0 or 2 odd numbers: 11 + 21 + 18, or 8 + 18 + 24. 18 is in both.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _flight():
    X = lambda h: 40 + h * 23            # hours after 17:30 on 19 August (GMT)
    y = 92
    legs = [(0, 9, 'fly', 'b'), (9, 10, 'LA', 'o'), (10, 18, 'fly', 'b'), (18, 19.5, 'Hawaii', 'o'), (19.5, 24.75, 'fly', 'b')]
    parts, lab = [], []
    for a, b, name, f in legs:
        parts.append(rect(X(a), y, X(b) - X(a), 40, k='ink', fill=f, sw=1.6))
        lab.append(text((X(a) + X(b)) / 2, y + 26, name, k='ink', size=16 if f == 'b' else 13))
    lab += [text(X(0), y - 34, '17:30, 19 Aug', k='ink', size=17, anchor='start'),
            text(X(0), y - 14, 'London', k='muted', size=15, anchor='start'),
            text(X(24.75), y - 34, '18:15, 20 Aug (GMT)', k='ink', size=17, anchor='end'),
            text(X(24.75), y - 14, '= 06:15, 21 Aug in Auckland', k='muted', size=15, anchor='end')]
    parts.append(brace(X(0), X(24.75), y + 46, 'whole trip: 24 h 45 min', k='red'))
    lab += [text(X(12.4), y + 110, 'orange = on the ground (1 h + 1½ h)', k='orange', size=17),
            text(X(12.4), y + 136, 'blue = in the air: 24¾ − 2½ = 22¼ h', k='pen', size=19, font='scrawl')]
    return svg(660, 250, rough(*parts) + ''.join(lab),
               'Timeline in GMT from 17:30 on 19 August to 18:15 on 20 August, 24 hours 45 minutes, with a 1-hour stop and a 1.5-hour stop')


Q.append(dict(
    n=2, orig=6, answer='B', topic='Time zones',
    question=f"""<p>I have booked a flight from London to Auckland, which is in a time zone {hl('12 hours ahead of GMT', 'y', 1)}. I am due to leave London at {hl('17:30 GMT on 19 August', 'g', 2)} and will arrive in Auckland at
{hl('06:15 on 21 August (local time)', 'p', 3)}. My journey includes {hl('a 1-hour stop in Los Angeles and a 1.5-hour stop in Hawaii', 'g', 4)}.</p>
<p class="stem">How many hours am I due to spend {hl('in the air', 'b', 5)}?</p>""",
    options={'A': '12¾', 'B': '22¼', 'C': '23¼', 'D': '24¾', 'E': '34¼'},
    notes=[(1, 'y', 'Auckland clocks are 12 hours <b>ahead</b>. To turn Auckland time into GMT, take 12 hours off.'),
           (2, 'g', 'Start time, already in GMT.'),
           (3, 'p', 'This is Auckland time! Put it into GMT before you subtract.'),
           (4, 'g', 'Time on the ground: 1 + 1.5 = 2.5 hours.'),
           (5, 'b', 'Flying time only, so the stops come off.')],
    steps=[
        f"""<p>Put both times on the <b>same clock</b> (GMT):</p>
{calc(f'arrive 06:15 on 21 Aug (Auckland) − 12 h {ar()} <b>18:15 on 20 Aug GMT</b>')}""",
        f"""<p>Whole trip, from 17:30 on the 19th to 18:15 on the 20th:</p>
{calc(f'17:30 → 17:30 next day = 24 h', f'17:30 → 18:15 = 45 min', f'total = 24 h 45 min = <b>24¾ h</b>')}
{_flight()}""",
        f"""<p>Take off the two stops:</p>
{calc(f'24¾ − 1 − 1½ = {boxed("22¼ hours")}')}""",
    ],
    answer_text='22¼ hours: a 24¾-hour trip minus 2½ hours of stops.',
    why={'A': '12¾ is just 17:30 to 06:15 on the clock. It ignores the dates and the time zone. Far too short for a flight to the other side of the world.',
         'C': '23¼ takes off only the 1½-hour Hawaii stop. The 1-hour stop in Los Angeles is on the ground too.',
         'D': '24¾ is the whole trip. It forgets to take off the 2½ hours of stops.',
         'E': '34¼ ignores the time zone: 17:30 on the 19th to 06:15 on the 21st is 36¾ hours on the clocks, minus 2½. But Auckland is 12 hours ahead.'},
    fast='06:15 Auckland = 18:15 GMT the day before. 17:30 → 18:15 next day = 24¾ h. Minus 2½ h of stops = 22¼.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _coasters():
    rows = [('Ring Racer', '140', '135', '688', '13'), ('Dodonpa', '121', '107', '400', '25'),
            ('Goliath', '155', '85', '267', '50'), ('Superman', '122', '100', '267', '33'),
            ('Intimidator 305', '145', '90', '188', '24'), ('Top Thrill Dragster', '150', '120', '99', '27'),
            ('Voyage', '138', '67', '102', '10'), ('Kingda Ka', '122', '128', '56', '39')]
    tests = [lambda v: int(v) <= 143, lambda v: int(v) >= 90, lambda v: int(v) <= 200, lambda v: int(v) <= 40]
    cols = [292, 386, 480, 574]
    heads = [('height', 'at most 143'), ('speed', 'at least 90'), ('one flight', 'at most $200'), ('queue', 'at most 40')]
    parts, lab = [], []
    for x, (h1, h2) in zip(cols, heads):
        lab.append(text(x, 26, h1, k='ink', size=16))
        lab.append(text(x, 46, h2, k='muted', size=14))
    for i, (name, *vals) in enumerate(rows):
        y = 62 + i * 32
        win = name == 'Kingda Ka'
        if win:
            parts.append(rect(18, y, 604, 30, k='green', fill='g', sw=2))
        lab.append(text(222, y + 21, name, k='green' if win else 'ink', size=16, anchor='end',
                        weight='bold' if win else None))
        for x, v, t in zip(cols, vals, tests):
            ok = t(v)
            lab.append(text(x - 4, y + 21, v, k='ink', size=16, anchor='end'))
            lab.append(text(x + 4, y + 22, '✓' if ok else '✗', k='green' if ok else 'red', size=19, anchor='start'))
    lab.append(text(320, 340, 'only Kingda Ka passes all four tests', k='green', size=22, font='scrawl'))
    return svg(640, 352, rough(*parts) + ''.join(lab),
               'Checklist of the eight roller coasters against the four rules; only Kingda Ka gets four ticks')


Q.append(dict(
    n=3, orig=7, answer='C', topic='Tables & rules',
    question=f"""<p>Anton wants to ride one of the top 8 roller coasters in the world to celebrate his 13th birthday.
The top 8 roller coasters are spread around the world. Anton has to decide which roller coaster
to visit, taking into consideration:</p>
<p>- {hl("Anton's height: 143 cm", 'g', 1)}<br>- {hl('$400 maximum for two one-way flights', 'p', 2)}<br>- The roller coaster must reach {hl('at least 90mph', 'y', 3)}<br>- Queue time is {hl('no longer than 40 minutes', 'y', 4)}</p>
{table([['Ring Racer,<br>Rheinland-Pfalz', '140', '135', '123', '688', '13'],
        ['Dodonpa,<br>Yamanashi', '121', '107', '170', hl('400', 'p'), '25'],
        ['Goliath,<br>California', '155', '85', '235', '267', '50'],
        ['Superman,<br>California', '122', '100', '415', '267', '33'],
        ['Intimidator 305,<br>Virginia', hl('145', 'p'), '90', '305', '188', '24'],
        ['Top Thrill Dragster,<br>Ohio', '150', '120', '420', '99', '27'],
        ['Voyage,<br>Indiana', '138', '67', '154', '102', '10'],
        ['Kingda Ka,<br>New Jersey', '122', '128', '456', '56', '39']],
       head=['Roller coaster location', 'Min height requirement (cm)', 'Speed (mph)', hl('Highest drop (ft)', 'p', 5),
             'Flight cost (one way) ($)', 'Average queue time (mins)'])}
<p class="stem">Which roller coaster will Anton choose to ride?</p>""",
    options={'A': 'Intimidator 305', 'B': 'Dodonpa', 'C': 'Kingda Ka', 'D': 'Superman', 'E': 'Voyage'},
    notes=[(1, 'g', 'The minimum height must be <b>143 or less</b>. A 145 cm limit keeps him off!'),
           (2, 'p', 'Two flights (there and back) for $400, so one flight must be <b>$200 or less</b>. The table gives one-way prices.'),
           (3, 'y', '“At least” means 90 itself is fine.'),
           (4, 'y', '40 minutes or less.'),
           (5, 'p', 'Drop height is not one of his rules. Ignore this column.')],
    steps=[
        f"""<p>Turn the four rules into four quick tests for each row:</p>
{calc('min height ≤ 143', 'speed ≥ 90', f'one-way flight ≤ $400 ÷ 2 = <b>$200</b>', 'queue ≤ 40')}""",
        f"""<p>Tick or cross every box:</p>{_coasters()}""",
        f"""<p>Only one coaster gets four ticks {ar()} {boxed('Kingda Ka')}</p>
{note('Dodonpa’s flight cost is exactly $400, which looks like the limit. But that is one way: two flights cost $800.', 'trap')}""",
    ],
    answer_text='Kingda Ka: tall enough, fast enough, flights 2 × $56 = $112, queue 39 minutes.',
    why={'A': 'Intimidator 305 needs riders of at least 145 cm. Anton is only 143 cm. (Its 90 mph would have been fine.)',
         'B': 'Dodonpa’s $400 is for <b>one</b> flight. Two flights cost $800, double his limit.',
         'D': 'Superman’s flights cost 2 × $267 = $534, over $400.',
         'E': 'Voyage only reaches 67 mph, below 90.'},
    fast='Halve $400: each flight ≤ $200. That leaves Intimidator, Top Thrill, Voyage and Kingda Ka. Height knocks out the first two, speed knocks out Voyage.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _cube_map():
    s = 66
    parts, lab = [], []

    def cell(col, row, ox, oy, ch, rot, f='paper', k='ink'):
        x, y = ox + col * s, oy + row * s
        parts.append(rect(x, y, s, s, k='ink', fill=f, sw=2))
        lab.append(_glyph(x + s / 2, y + s / 2, ch, rot, size=42, k=k))

    # left: the map built from the two views
    ox, oy = 40, 46
    cell(1, 0, ox, oy, 'B', 0, 'b')
    cell(0, 1, ox, oy, 'E', 0, 'o')
    cell(1, 1, ox, oy, 'A', 0, 'y')
    cell(2, 1, ox, oy, 'F', 0, 'g')
    cell(1, 2, ox, oy, 'D', 180, 'v')
    lab += [text(ox + 1.5 * s, 30, 'map from the two views', k='ink', size=19, font='scrawl'),
            text(20, 278, '① A’s head touches B', k='pen', size=17, anchor='start'),
            text(20, 302, '② E on A’s left, F on A’s right, both upright', k='orange', size=17, anchor='start'),
            text(20, 326, '③ D under A’s feet, upside down', k='violet', size=17, anchor='start'),
            text(20, 350, '(C is round the back)', k='muted', size=15, anchor='start')]

    # right: net D
    ox2, oy2 = 440, 46
    cell(1, 0, ox2, oy2, 'C', 180)
    cell(0, 1, ox2, oy2, 'E', 90, 'o')
    cell(1, 1, ox2, oy2, 'B', 0, 'b')
    cell(2, 1, ox2, oy2, 'F', -90, 'g')
    cell(1, 2, ox2, oy2, 'A', 0, 'y')
    cell(1, 3, ox2, oy2, 'D', 180, 'v')
    parts += [arrow(ox2 + 0.5 * s, oy2 + s - 10, ox2 + s + 8, oy2 + s + 16, k='red', bend=-0.35, w=2),
              arrow(ox2 + 2.5 * s, oy2 + s - 10, ox2 + 2 * s - 8, oy2 + s + 16, k='red', bend=0.35, w=2)]
    lab += [text(ox2 + 1.5 * s, 30, 'net D', k='ink', size=19, font='scrawl'),
            text(ox2 + 1.5 * s, oy2 + 4 * s + 26, 'tops of E and F point at B ✓', k='red', size=16)]
    return svg(660, 362, rough(*parts) + ''.join(lab),
               'Left: B above A, E to the left, F to the right and D upside down below A. Right: net D, where E and F are turned so their tops point at B')


Q.append(dict(
    n=4, orig=8, answer='D', topic='Nets & cubes',
    question=f"""<p>A cube is labelled with six letters and, when {hl('viewed in two positions', 'y', 1)}, looks like this:</p>
{fig(Y, 'ps_q04_cubes', 'Two views of the cube. Left: B on top, A on the front left, F on the front right. Right: D on top, A upside down on the front left, E upside down on the front right', 300)}
<p class="stem">Which one of the following nets {hl('could be folded', 'b', 2)} to make the above cube?</p>
{fig(Y, 'ps_q04_nets', 'Five cross-shaped nets A to E with the letters A to F in different places and turned different ways', 440)}""",
    options={'A': 'net A', 'B': 'net B', 'C': 'net C', 'D': 'net D', 'E': 'net E'},
    notes=[(1, 'y', 'The same cube twice. A is in both views, so build everything around A.'),
           (2, 'b', 'Right faces <b>and</b> letters pointing the right way.')],
    steps=[
        f"""<p>View 1: B sits on top of A, and F is on A’s right. Everything is the right way up.</p>
<p>View 2: A is upside down. Spin this view half a turn so that A stands up again:</p>
<ul><li>D, on top, drops <b>below</b> A and turns upside down.</li>
<li>E, on the right, swings to A’s <b>left</b> and becomes the right way up, with its arms pointing at A.</li></ul>""",
        f"""<p>Now draw A with its four neighbours:</p>{_cube_map()}
<p>So opposite pairs are A–C, B–D, E–F. Every net gets these pairs right, so it all comes down to <b>which way the letters point</b>. Four checks:</p>
<ul><li>① A’s head touches B.</li><li>② F is on A’s right; E is on A’s left with its arms pointing at A.</li>
<li>③ D is under A’s feet, upside down.</li><li>④ E and F stand up on the sides, so their <b>tops touch B</b>.</li></ul>""",
        f"""<p>Test the nets:</p>
{calc(f'A: E and F stand upright beside B, so their tops point up the page, not at B {cross()} (④)',
      f'B: turn it so A is upright: E is now on A’s right, F on its left. Swapped {cross()} (②)',
      f'C: E’s arms point at C, away from A {cross()} (②)',
      f'E: A is above B with its feet on B {cross()} (①)',
      f'D: B on A’s head, D upside down under A, tops of E and F point at B {tick()} {ar()} {boxed("D")}')}
{note('Moving a square round a corner of a net turns it a quarter turn. That is why E and F lie on their sides in net D but stand upright in the map.', 'tip')}""",
    ],
    answer_text='Net D: every letter touches the right neighbours and points the right way.',
    why={'A': 'E and F sit beside B standing upright, so their tops point up the page, not at B. On the cube their tops touch B, so here they would end up lying on their sides.',
         'B': 'With A turned upright, E is on A’s right and F on A’s left. View 1 shows F on A’s right, so this is the mirror image.',
         'C': 'E’s arms point at C, away from A. View 2 shows E’s arms pointing at A.',
         'E': 'A is above B with A’s feet touching B. On the cube B sits on A’s head.'},
    fast='Spin view 2 so A is upright: B on A’s head, D upside down under A’s feet, E left and F right with their tops touching B. Only net D does all of that.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _rota():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    who = [('Robert', 'b', 'pen', {1, 2, 4}), ('Sheila', 'g', 'green', {0, 2, 3}), ('Tom', 'o', 'orange', {0, 1, 3, 4})]
    x0, y0, cw, ch = 120, 40, 90, 46
    parts, lab = [], []
    for j, d in enumerate(days):
        lab.append(text(x0 + j * cw + cw / 2, y0 - 12, d, k='ink', size=18))
    for i, (name, f, k, on) in enumerate(who):
        y = y0 + i * ch
        lab.append(text(x0 - 12, y + 30, name, k=k, size=19, anchor='end'))
        for j in range(5):
            parts.append(rect(x0 + j * cw + 3, y + 3, cw - 6, ch - 6, k='ink' if j in on else 'muted', fill=f if j in on else 'none', sw=1.6))
            if j in on:
                lab.append(text(x0 + j * cw + cw / 2, y + 31, 'on', k='ink', size=18))
            elif name == 'Tom':
                lab.append(text(x0 + j * cw + cw / 2, y + 31, 'off', k='red', size=20, font='scrawl'))
    parts += [arrow(x0 + 2.5 * cw, y0 + 3 * ch + 30, x0 + 2.5 * cw, y0 + 3 * ch - 2, k='red', w=2)]
    lab += [text(x0 + 2.5 * cw, y0 + 3 * ch + 50, 'Tom off Wednesday, so Robert and Sheila both work', k='red', size=17),
            text(x0 + 2.5 * cw, y0 + 3 * ch + 76, 'nobody works 3 nights in a row ✓', k='green', size=18, font='scrawl')]
    return svg(600, 270, rough(*parts) + ''.join(lab),
               'Rota: Robert Tuesday, Wednesday, Friday; Sheila Monday, Wednesday, Thursday; Tom every night except Wednesday')


Q.append(dict(
    n=5, orig=12, answer='C', topic='Logic & rotas',
    question=f"""<p>Three night security guards, Robert, Sheila and Tom, are assigned to guard a factory for five
consecutive nights, Monday night to Friday night inclusive.</p>
<p>{hl('Two of the guards are to be on duty each night', 'y', 1)}. {hl('Tom must be on duty for four nights', 'g', 2)} and
Robert and Sheila are on duty for three nights each. Regulations do not allow any guard to
work for {hl('more than two consecutive nights', 'p', 3)}.</p>
<p class="stem">If {hl('Robert is on duty on Friday night', 'g', 4)}, then the nights when Sheila is on duty are</p>""",
    options={'A': 'Monday, Tuesday, Thursday.', 'B': 'Monday, Tuesday, Friday.', 'C': 'Monday, Wednesday, Thursday.',
             'D': 'Monday, Wednesday, Friday.', 'E': 'Tuesday, Wednesday, Friday.'},
    notes=[(1, 'y', '3 guards, 2 on duty, so exactly <b>one guard is off</b> each night.'),
           (2, 'g', 'Tom has just one night off out of five.'),
           (3, 'p', 'Two in a row is fine. <b>Three in a row is banned.</b>'),
           (4, 'g', 'The extra clue that pins everything down.')],
    steps=[
        f"""<p>Start with Tom: 4 nights out of 5 but never 3 in a row. His night off must split the week in the middle:</p>
{calc(f'Mon Tue | <b>off</b> | Thu Fri {tick()}', f'off any other night {ar()} 3 or 4 nights in a row {cross()}')}""",
        f"""<p>Wednesday: Tom is off, so <b>Robert and Sheila both work</b>.<br>Friday: Tom works, and we are told Robert does. Friday is full.</p>""",
        f"""<p>Robert has Wed and Fri, and needs one more night. Thursday would give Wed-Thu-Fri, three in a row {cross()}.
So <b>Sheila takes Thursday</b>, and Robert’s extra night is Monday or Tuesday.</p>""",
        f"""<p>Sheila now has Wed and Thu, and needs one more: Monday or Tuesday. Tuesday would give Tue-Wed-Thu {cross()}.
So Sheila takes <b>Monday</b> and Robert takes Tuesday.</p>{_rota()}
{calc(f'Sheila: {boxed("Monday, Wednesday, Thursday")}')}""",
    ],
    answer_text='Monday, Wednesday, Thursday.',
    why={'A': 'Sheila is off on Wednesday. But Wednesday is Tom’s night off, so Robert would be on his own.',
         'B': 'Friday is already full with Tom and Robert. Sheila can’t work Friday (and she must work Wednesday).',
         'D': 'Friday is already full with Tom and Robert, so Sheila can’t be there.',
         'E': 'Friday is already full with Tom and Robert, so Sheila can’t be there.'},
    fast='Tom off Wednesday (no 3 in a row), so R and S both work Wednesday. Friday is Tom + Robert. Robert can’t do Thursday (W-T-F), so Sheila does; Sheila can’t do Tuesday (T-W-T), so Monday.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _family():
    ppl = [(70, 'Dad', 'unemployed', 'pen'), (160, 'Grandpa', 'nearly 72', 'pen'), (250, 'Me', '6', 'pen'),
           (340, 'Brother', '8', 'pen'), (440, 'Mum', 'nurse', 'orange'), (530, 'Grandma', 'watching', 'violet'),
           (615, 'Sister', '3', 'green')]
    parts, lab = [], []
    parts.append(rect(28, 46, 352, 192, k='pen', sw=2.2, rx=14))
    lab.append(text(204, 36, 'concession family ticket £4.80', k='pen', size=19, font='scrawl'))
    for x, name, info, k in ppl:
        s = 1.5 if name in ('Dad', 'Grandpa', 'Mum', 'Grandma') else 1.1
        lab.append(stick_person(x, 168, k=k, s=s))
        lab.append(text(x, 194, name, k='ink', size=16))
        lab.append(text(x, 214, info, k='muted', size=14))
    lab += [text(440, 252, 'adult £3.80', k='orange', size=17), text(530, 252, 'spectator £0.70', k='violet', size=15),
            text(615, 252, 'under 4: free', k='green', size=15),
            text(330, 296, '4.80 + 3.80 + 0.70 = £9.30', k='red', size=26, font='scrawl')]
    return svg(660, 310, rough(*parts) + ''.join(lab),
               'Seven family members: Dad, Grandpa, me and my brother share a concession family ticket; Mum pays as an adult, Grandma as a spectator, my sister is free')


Q.append(dict(
    n=6, orig=13, answer='C', topic='Tables & best deal',
    question=f"""<p>As a treat for my {hl('sixth birthday', 'g', 1)} I am going swimming with my family {hl('next Saturday afternoon', 'p', 2)}.
{hl('My mum is a nurse', 'p', 3)} and {hl('my dad is unemployed', 'g', 4)}. {hl('My sister is three years younger than me', 'g', 5)} and
{hl('my brother is two years older', 'g', 6)} but they will both enjoy the treat too. {hl('Grandma is coming but she will watch rather than swim', 'y', 7)}. Grandpa loves swimming even though he is {hl('nearly 72 years old', 'g', 8)},
so he will be in the pool enjoying the swim.</p>
<p>The charges at the local swimming centre are shown below:</p>
{table([['Adult', '£3.80', '£2.90'], ['Unemployed Adult', '£2.10', '£1.50'],
        ['Child/Senior Citizen (over 65 years)', '£1.90', '£1.50'], ['Family ticket (2 adults and 2 children)', '£9.50', '£7.10'],
        [hl('*Concession family ticket (2 adults and 2 children)', 'g'), hl('£4.80', 'g'), '£3.60'],
        ['Family ticket (1 adult and 2 children)', '£5.70', '£4.30'],
        ['*Concession family ticket (1 adult and 2 children)', '£3.60', '£2.85'],
        ['Spectators', '£0.70', '£0.50'], ['Under 4s', 'free', 'free']],
       head=['Admission for:', 'Peak Times', 'Off-Peak Times'])}
<p>{hl('*Adults must be Unemployed or Senior Citizens', 'y', 9)}<br>Off-peak – Monday to Friday 9 am to 5 pm<br>Peak – all other times and school holidays</p>
<p class="stem">What is the lowest price that we could pay for our tickets?</p>""",
    options={'A': '£7.00', 'B': '£9.10', 'C': '£9.30', 'D': '£12.10', 'E': '£12.30'},
    notes=[(1, 'g', 'Me: 6, a child.'),
           (2, 'p', 'Saturday is <b>peak</b> (off-peak is only Monday to Friday). Use the Peak column only.'),
           (3, 'p', 'Mum works, so she is a full-price adult. She can’t go on a concession ticket.'),
           (4, 'g', 'Dad is unemployed: he counts for a concession ticket.'),
           (5, 'g', 'Sister: 3, under 4, so <b>free</b>.'),
           (6, 'g', 'Brother: 8, a child.'),
           (7, 'y', 'Grandma just needs a spectator ticket.'),
           (8, 'g', 'Grandpa is over 65: a senior citizen, so he counts for a concession ticket too.'),
           (9, 'y', 'Dad + Grandpa are the two concession adults!')],
    steps=[
        f"""<p>Who is who? 4 swimmers who can share the cheap ticket, plus Mum, Grandma and a free sister:</p>{_family()}""",
        f"""<p>The concession family ticket (2 adults + 2 children) for Dad, Grandpa, me and my brother:</p>
{calc('concession ticket £4.80', 'Mum, adult £3.80', 'Grandma, spectator £0.70', 'sister, free',
      f'total = {boxed("£9.30")}')}""",
        f"""<p>Check the other ways quickly (all peak prices):</p>
{calc('everyone separately: 3.80 + 2.10 + 1.90 + 1.90 + 1.90 + 0.70 = £12.30',
      'normal family ticket (Mum, Dad, 2 boys) 9.50 + Grandpa 1.90 + 0.70 = £12.10',
      'concession for Dad + 2 boys 3.60 + Mum 3.80 + Grandpa 1.90 + 0.70 = £10.00',
      f'£9.30 is the lowest {tick()}')}""",
    ],
    answer_text='£9.30: concession family ticket £4.80 + Mum £3.80 + Grandma £0.70, sister free.',
    why={'A': '£7.00 uses <b>off-peak</b> prices (3.60 + 2.90 + 0.50). Saturday afternoon is peak.',
         'B': '£9.10 is also off-peak: normal family ticket 7.10 + Grandpa 1.50 + Grandma 0.50.',
         'D': '£12.10 uses the normal family ticket (9.50) for Mum, Dad and the boys. It misses the concession ticket with Grandpa.',
         'E': '£12.30 is everyone paying separately, with no family ticket at all.'},
    fast='Saturday = peak. Dad (unemployed) + Grandpa (senior) + the 2 boys = concession £4.80. Mum £3.80, Grandma £0.70, sister free: £9.30.',
))


# ---------------------------------------------------------------- 7 (Q14)
PT = {'C': (.5, .5), 'N': (.5, 0), 'E': (1, .5), 'S': (.5, 1), 'W': (0, .5),
      'NW': (0, 0), 'NE': (1, 0), 'SE': (1, 1), 'SW': (0, 1)}


def _tile(x, y, s, segs, k='ink', w=2.6, box='muted', fill='none'):
    out = [rect(x, y, s, s, k=box, fill=fill, sw=1.4)]
    for a, b in segs:
        (ax, ay), (bx, by) = PT[a], PT[b]
        out.append(line(x + ax * s, y + ay * s, x + bx * s, y + by * s, k=k, w=w))
    return out


S_TILES = {(0, 0): [('E', 'S')], (1, 0): [('W', 'E')], (2, 0): [('W', 'C')],
           (0, 1): [('N', 'C'), ('C', 'SE')], (1, 2): [('NW', 'SE')], (2, 3): [('NW', 'C'), ('C', 'S')],
           (0, 4): [('C', 'E')], (1, 4): [('W', 'E')], (2, 4): [('N', 'W')]}
W_TILES = {(0, 0): [('N', 'S')], (2, 0): [('N', 'S')], (0, 1): [('N', 'S')], (1, 1): [('SW', 'C'), ('C', 'SE')],
           (2, 1): [('N', 'S')], (0, 2): [('N', 'C'), ('C', 'NE')], (2, 2): [('N', 'C'), ('C', 'NW')]}


def _floor_bits():
    s = 46
    parts, lab = [], []
    marks_s = {(1, 2): ('C', 'g', 'tr'), (0, 1): ('D', 'b', 'tr'), (2, 3): ('D', 'b', 'tr')}
    marks_w = {(0, 2): ('E', 'o', 'bl'), (2, 2): ('A', 'v', 'br')}
    for (ox, oy, tiles, rows, marks, title) in ((40, 50, S_TILES, 5, marks_s, 'the S'),
                                                 (260, 96, W_TILES, 3, marks_w, 'bottom of the W')):
        lab.append(text(ox + 1.5 * s, oy - 14, title, k='ink', size=19, font='scrawl'))
        for c in range(3):
            for r in range(rows):
                f = marks[(c, r)][1] if (c, r) in marks else 'none'
                parts += _tile(ox + c * s, oy + r * s, s, tiles.get((c, r), []), fill=f)
        for (c, r), (letter, f, where) in marks.items():
            lx = ox + c * s + (10 if where == 'bl' else s - 10)
            ly = oy + r * s + (16 if where == 'tr' else s - 6)
            lab.append(text(lx, ly, letter, k='red', size=17, font='print', weight='bold'))
    lab += [text(450, 120, 'C = the long slant', k='ink', size=17, anchor='start'),
            text(450, 146, 'D = the S’s bend,', k='ink', size=17, anchor='start'),
            text(450, 168, 'turned a quarter turn', k='muted', size=15, anchor='start'),
            text(450, 200, 'A and E = the two', k='ink', size=17, anchor='start'),
            text(450, 222, 'W corners, turned', k='muted', size=15, anchor='start'),
            text(450, 262, 'B = nowhere!', k='red', size=22, anchor='start', font='scrawl')]
    return svg(660, 310, rough(*parts) + ''.join(lab),
               'The S and the bottom of the W drawn tile by tile, with the tiles matching options A, C, D and E marked')


def _mirror():
    s = 62
    parts, lab = [], []
    b_turns = [[('N', 'C'), ('C', 'SW')], [('E', 'C'), ('C', 'NW')], [('S', 'C'), ('C', 'NE')], [('W', 'C'), ('C', 'SE')]]
    s_turns = [[('N', 'C'), ('C', 'SE')], [('E', 'C'), ('C', 'SW')], [('S', 'C'), ('C', 'NW')], [('W', 'C'), ('C', 'NE')]]
    lab.append(text(20, 52, 'B turned 4 ways', k='red', size=17, anchor='start'))
    lab.append(text(20, 152, 'S-bend tile', k='pen', size=17, anchor='start'))
    lab.append(text(20, 172, 'turned 4 ways', k='pen', size=17, anchor='start'))
    for i, segs in enumerate(b_turns):
        parts += _tile(170 + i * 90, 18, s, segs, k='red', box='ink')
    for i, segs in enumerate(s_turns):
        parts += _tile(170 + i * 90, 122, s, segs, k='pen', box='ink', fill='b' if i == 1 else 'none')
    lab += [text(170 + 90 + s / 2, 204, '= D', k='pen', size=16),
            text(330, 240, 'no match in any position: they are mirror images', k='red', size=19, font='scrawl'),
            text(330, 264, '(a tile can be turned round, but not flipped over)', k='muted', size=15)]
    return svg(560, 276, rough(*parts) + ''.join(lab),
               'Option B in all four turns compared with the S-bend tile in all four turns: none of them match')


Q.append(dict(
    n=7, orig=14, answer='B', topic='Shapes & patterns',
    question=f"""<p>The floor of the reception area of the head office of Stott and Walsh is tiled as shown below:</p>
{fig(Y, 'ps_q07_floor', 'A 15 by 15 grid of square tiles with lines on them spelling STOTT, a plus sign, and WALSH', 440)}
<p class="stem">Which one of these tiles could {hl('<b>not</b>', 'b', 1)} be used to {hl('replace a damaged tile on this floor', 'y', 2)}?</p>
{fig(Y, 'ps_q07_opts', 'Five tiles A to E, each with a short line pattern', 470)}""",
    options={'A': 'tile A', 'B': 'tile B', 'C': 'tile C', 'D': 'tile D', 'E': 'tile E'},
    notes=[(1, 'b', 'Four of these tiles are somewhere on the floor. Find the one that isn’t.'),
           (2, 'y', 'A replacement must match a tile that is already there. You may <b>turn</b> a tile round, but you can’t flip it over (the pattern is only on top).')],
    steps=[
        f"""<p>Every option has a slant that runs into a <b>corner</b> of the tile. T, L, H and + have no slants at all, and the
O and A only have little cut-off slants between the middles of two edges. So only look at the <b>S</b> and the bottom of the <b>W</b>.
Draw them tile by tile:</p>{_floor_bits()}""",
        f"""<p>Match the options:</p>
{calc(f'C: the long slant through the middle of the S {tick()}',
      f'D: the S’s bend (straight line in, slant out), turned a quarter turn {tick()}',
      f'A and E: the two bottom corners of the W, turned {tick()}',
      'B: straight line in, slant out… but it bends the <b>other</b> way')}""",
        f"""<p>Check B properly: turn it all four ways and compare with the S-bend tile.</p>{_mirror()}
{calc(f'B is the S tile’s mirror image, and it appears nowhere else {ar()} {boxed("B")}')}""",
    ],
    answer_text='Tile B: it is a mirror image of the tile used in the S, so no turn of it fits the floor.',
    why={'A': 'A is the bottom right corner of the W (straight line down, slant up), turned a quarter turn.',
         'C': 'C is the long corner-to-corner slant in the middle of the S.',
         'D': 'D is the S’s bend: a straight line into the middle and a slant to a corner, turned a quarter turn.',
         'E': 'E is the bottom left corner of the W, turned upside down.'},
    fast='Only S and W have slants. C, D come from the S; A, E from the W. B bends the opposite way to the S’s tiles, so it’s the mirror image.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _route_map():
    T = {'A': (100, 70), 'E': (560, 110), 'Y': (330, 190), 'T': (240, 330)}
    roads = [('A', 'E', 31, (330, 76), 'middle'), ('A', 'Y', 18, (226, 118), 'middle'),
             ('A', 'T', 25, (156, 210), 'end'), ('Y', 'E', 20, (440, 138), 'middle'),
             ('Y', 'T', 17, (272, 262), 'end'), ('T', 'E', 23, (418, 250), 'start')]
    best = {('E', 'Y'), ('Y', 'A'), ('A', 'T'), ('T', 'E')}
    parts, lab = [], []
    for a, b, km, (lx, ly), anc in roads:
        on = (a, b) in best or (b, a) in best
        (x1, y1), (x2, y2) = T[a], T[b]
        parts.append(line(x1, y1, x2, y2, k='green' if on else 'muted', w=5 if on else 2, dash=not on))
        lab.append(text(lx, ly, f'{km} km', k='green' if on else 'muted', size=19, anchor=anc,
                        weight='bold' if on else None))
    for name, (x, y) in T.items():
        parts.append(circle(x, y, 9, k='ink', fill='ink'))
    lab += [text(100, 48, 'Arford', k='ink', size=19), text(560, 88, 'Essover (home)', k='ink', size=19),
            text(330, 166, 'Yewton', k='ink', size=19), text(240, 362, 'Teechester', k='ink', size=19)]
    lab += [text(640, 300, 'E → Y → A → T → E', k='green', size=22, anchor='end', font='scrawl'),
            text(640, 330, '20 + 18 + 25 + 23 = 86', k='green', size=22, anchor='end', font='scrawl'),
            text(640, 20, 'dashed = not used', k='muted', size=15, anchor='end')]
    return svg(660, 376, rough(*parts) + ''.join(lab),
               'Sketch map of the four towns with the shortest loop Essover, Yewton, Arford, Teechester, Essover drawn thick: 86 km')


Q.append(dict(
    n=8, orig=18, answer='C', topic='Routes & networks',
    question=f"""<p>This diagram shows the roads that connect four towns and the distances involved.</p>
{fig(Y, 'ps_q08_map', 'Four towns: Arford to Essover 31 km, Arford to Yewton 18 km, Arford to Teechester 25 km, Yewton to Essover 20 km, Yewton to Teechester 17 km, Teechester to Essover 23 km. Not to scale', 420)}
<p>I live in Essover. This afternoon I have to {hl('visit clients in Arford, Teechester and Yewton before returning to Essover', 'y', 1)}. {hl('It does not matter in which order', 'g', 2)} I visit the clients.</p>
<p class="stem">What is the {hl('minimum distance', 'b', 3)} I could travel this afternoon?</p>""",
    options={'A': '78 km', 'B': '83 km', 'C': '86 km', 'D': '89 km', 'E': '93 km'},
    notes=[(1, 'y', 'A round trip: start and finish at Essover, calling at all three towns.'),
           (2, 'g', 'Try every order. With three towns there are only a few.'),
           (3, 'b', 'Shortest round trip.')],
    steps=[
        f"""<p>A loop from Essover through the other three towns. Going round a loop backwards gives the same distance, so there are only <b>3</b> different loops:</p>
{calc('E → A → Y → T → E = 31 + 18 + 17 + 23 = 89',
      'E → A → T → Y → E = 31 + 25 + 17 + 20 = 93',
      'E → Y → A → T → E = 20 + 18 + 25 + 23 = <b>86</b>')}""",
        f"""{_route_map()}
{note('Both slow loops use the 31 km road. Avoiding it is the key.', 'tip')}""",
        f"""<p>Could doubling back help? No: any repeated road just adds distance (e.g. E → Y → A → Y → T → E = 96).</p>
{calc(f'minimum = {boxed("86 km")}')}""",
    ],
    answer_text='86 km: Essover, Yewton, Arford, Teechester, Essover (or the reverse).',
    why={'A': '78 = 17 + 18 + 20 + 23, the four shortest roads. They don’t make a loop: you’d be stuck at Arford and have to come back along the 18 km road.',
         'B': '83 is E → T → A → Y (66 km) plus the 17 km road from Yewton to Teechester. That ends at Teechester, not at home.',
         'D': '89 is the loop E → A → Y → T → E, which uses the long 31 km road.',
         'E': '93 is the loop E → A → T → Y → E: the 31 km and 25 km roads, the worst loop.'},
    fast='Only three loops. Avoid the 31 km road: E–Y–A–T–E = 20 + 18 + 25 + 23 = 86.',
))
