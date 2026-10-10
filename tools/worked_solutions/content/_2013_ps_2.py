from wslib import *

Y = 2013
Q = []

# ---------------------------------------------------------------- 9 (Q19)
def _cuts():
    parts, lab = [], []
    house = [(0, 0), (45, 40), (45, 110), (-45, 110), (-45, 40)]
    r = 17.8
    specs = [('A', 70, [[(0, 0), (45, 40), (-45, 40)], [(45, 40), (45, 110), (-45, 110), (-45, 40)]], ((-45, 40), (45, 40)), '3 + 4'),
             ('B', 195, [[(0, 0), (45, 40), (45, 75)], [(0, 0), (45, 75), (45, 110), (-45, 110), (-45, 40)]], ((0, 0), (45, 75)), '3 + 5'),
             ('C', 320, [[(0, 0), (20, r), (-20, r)], [(20, r), (45, 40), (45, 110), (-45, 110), (-45, 40), (-20, r)]], ((-20, r), (20, r)), '3 + 6'),
             ('D', 445, [[(0, 0), (45, 40), (45, 75), (-45, 75), (-45, 40)], [(45, 75), (45, 110), (-45, 110), (-45, 75)]], ((-45, 75), (45, 75)), '5 + 4')]
    oy = 44
    for letter, cx, pieces, (p1, p2), res in specs:
        for piece, f in zip(pieces, ('y', 'b')):
            parts.append(poly([(cx + x, oy + y) for x, y in piece], k='ink', fill=f, sw=1.8))
        parts.append(line(cx + p1[0], oy + p1[1], cx + p2[0], oy + p2[1], k='red', w=3))
        lab += [text(cx, 30, letter, k='ink', size=20, font='print', weight='700'),
                text(cx, oy + 140, res, k='green', size=20, font='scrawl'), text(cx, oy + 162, 'possible', k='green', size=15)]
    cx = 570
    parts.append(poly([(cx + x, oy + y) for x, y in house], k='ink', fill='paper', sw=1.8))
    lab += [text(cx, 30, 'E', k='ink', size=20, font='print', weight='700'), text(cx, oy + 78, '?', k='red', size=40, font='scrawl'),
            text(cx, oy + 140, '4 + 6 ✗', k='red', size=20, font='scrawl'), text(cx, oy + 162, 'needs 10 sides', k='red', size=15),
            text(320, 236, 'one cut gives at most 5 + 4 = 9 sides in total', k='pen', size=19)]
    return svg(640, 250, rough(*parts) + ''.join(lab),
               'Four pentagons cut by one red line into a triangle and quadrilateral, triangle and pentagon, triangle and hexagon, pentagon and quadrilateral; quadrilateral plus hexagon is impossible')

Q.append(dict(
    n=9, orig=19, answer='E', topic='Shapes & cutting',
    question=f"""<p>I am making a patchwork quilt from leftover pieces of cloth of various shapes and sizes. This
pentagonal piece of cloth is rather large, so I want to cut it into two pieces.</p>
{fig(Y, 'ps_q09_pentagon', 'A pentagon shaped like a house: a square with a triangular roof', 120)}
<p class="stem">Which one of the following combinations is it {hl('<b>not</b>', 'b', 1)} possible to produce by making {hl('one straight cut', 'y', 2)}
across a pentagonal piece of cloth?</p>""",
    options={'A': 'A triangle and a quadrilateral.', 'B': 'A triangle and a pentagon.', 'C': 'A triangle and a hexagon.',
             'D': 'A quadrilateral and a pentagon.', 'E': 'A quadrilateral and a hexagon.'},
    notes=[(1, 'b', 'Four of these can happen. Find the one that can’t.'),
           (2, 'y', 'One straight line, starting and ending on the edge (at a corner or partway along a side).')],
    steps=[
        f"""<p>Count the <b>total</b> number of sides of the two pieces. The cut becomes a side of both pieces (+2),
and every side it crosses partway along gets split into two (+1 each).</p>
{calc(f'corner to corner: 5 + 2 = <b>7</b> {ar()} 3 + 4', f'corner to the middle of a side: 5 + 2 + 1 = <b>8</b> {ar()} 3 + 5 or 4 + 4',
      f'middle of a side to middle of a side: 5 + 2 + 2 = <b>9</b> {ar()} 3 + 6 or 4 + 5')}""",
        f"""<p>Sketch each one on the house shape:</p>{_cuts()}""",
        f"""{calc(f'quadrilateral + hexagon = 4 + 6 = 10 sides', f'more than the 9 maximum {ar()} {boxed("E")}')}
{note('Can’t remember the rule? Just doodle cuts on the pentagon: the four possible pairs turn up quickly, and 4 + 6 never does.', 'tip')}""",
    ],
    answer_text='A quadrilateral and a hexagon: that needs 10 sides in total, but one cut makes at most 9.',
    why={'A': 'Possible: cut corner to corner across the bottom of the roof.',
         'B': 'Possible: cut from the top corner to partway down one wall.',
         'C': 'Possible: snip the top corner off with a short cut across the two roof edges.',
         'D': 'Possible: cut straight across both walls.'},
    fast='Total sides after one cut is 7, 8 or 9. 4 + 6 = 10, so E is impossible.',
))

# ---------------------------------------------------------------- 10 (Q20)
def _booked():
    data = [('Mon', 25), ('Tue', 52), ('Wed', 43), ('Thu', 61), ('Fri', 37)]
    base, s = 250, 2.8
    parts, lab = [], []
    for i, (d, v) in enumerate(data):
        x = 70 + i * 110
        f = 'p' if d == 'Mon' else 'g' if d == 'Fri' else 'paper'
        parts.append(rect(x, base - v * s, 64, v * s, k='ink', fill=f, sw=1.8))
        ly = base - v * s + 28 if d == 'Mon' else base - v * s - 10
        lab += [text(x + 32, ly, v, k='ink', size=19), text(x + 32, base + 22, d, k='ink', size=17)]
    parts += [line(40, base - 30 * s, 625, base - 30 * s, k='red', w=2.2, dash=True), line(40, base, 625, base, k='ink', w=2)]
    lab += [text(320, 24, 'already booked each morning = 100 − spaces', k='pen', size=18),
            text(44, base - 30 * s - 8, '30 or fewer: small room', k='red', size=15, anchor='start'),
            text(102, base + 46, '26 with him ✗', k='red', size=17, font='scrawl'),
            text(542, base + 46, '38 with him ✓', k='green', size=17, font='scrawl'),
            text(542, base + 66, 'fewest others', k='green', size=15)]
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'Bars of candidates already booked each morning: Monday 25 is under the 30 line; Friday 37 is the smallest above it')

Q.append(dict(
    n=10, orig=20, answer='E', topic='Tables & conditions',
    question=f"""<p>Thomas needs to book a place to sit a test next week, but is {hl('free only in the mornings', 'p', 1)}. The test
centre runs the test every day from Monday to Friday and holds a morning and an afternoon sitting.
Each sitting has {hl('a total of 100 places', 'g', 2)} available and will take place in the main hall {hl('unless there are 30 or fewer candidates, in which case a smaller room is used', 'y', 3)}. He does not like to take tests in
crowded places, so he wants to {hl('make sure that he is in the main hall', 'b', 4)} and will try to be with the
{hl('smallest number of other candidates', 'b', 5)} possible. The number of places that are {hl('still available', 'g', 6)} are
shown in the table below.</p>
{table([['Monday', hl('75', 'g'), '67'], ['Tuesday', hl('48', 'g'), '47'], ['Wednesday', hl('57', 'g'), '2'],
        ['Thursday', hl('39', 'g'), '10'], ['Friday', hl('63', 'g'), '46']],
       head=['Day', 'Spaces available a.m.', 'Spaces available p.m.'])}
<p class="stem">On which day should he choose to sit the test?</p>""",
    options={'A': 'Monday', 'B': 'Tuesday', 'C': 'Wednesday', 'D': 'Thursday', 'E': 'Friday'},
    notes=[(1, 'p', 'Mornings only: ignore the whole p.m. column.'),
           (2, 'g', '100 places in each sitting.'),
           (3, 'y', 'Main hall needs <b>31 or more</b> candidates, counting Thomas himself.'),
           (4, 'b', 'Rule 1: it must be the main hall for certain.'),
           (5, 'b', 'Rule 2: then as few other people as possible.'),
           (6, 'g', 'These are <b>empty</b> places. People already booked = 100 − spaces.')],
    steps=[
        f"""<p>Turn morning spaces into people already booked:</p>
{calc('Mon 100 − 75 = 25', 'Tue 100 − 48 = 52', 'Wed 100 − 57 = 43', 'Thu 100 − 39 = 61', 'Fri 100 − 63 = 37')}""",
        f"""<p>Add Thomas and check the main hall rule (more than 30):</p>{_booked()}""",
        f"""{calc(f'Monday: 25 + 1 = 26 {ar()} small room {cross()}', f'the rest are main hall; fewest others = Friday, 37 {ar()} {boxed("Friday")}')}
{note('Monday looks perfect (fewest people), but that is exactly why it fails: with so few, the test moves to the small room.', 'trap')}""",
    ],
    answer_text='Friday: 37 others already booked, the fewest of any morning that is sure to be in the main hall.',
    why={'A': 'Monday has only 25 booked, so 26 with Thomas: 30 or fewer means the small room.',
         'B': 'Tuesday has 52 others booked, more than Friday’s 37.',
         'C': 'Wednesday has 43 others. (Its 2 afternoon spaces don’t matter: he can’t do afternoons.)',
         'D': 'Thursday has the fewest spaces, so it is the most crowded morning: 61 others.'},
    fast='Booked = 100 − spaces: 25, 52, 43, 61, 37. Monday (26 with him) is the small room. Smallest of the rest: Friday.',
))

# ---------------------------------------------------------------- 11 (Q24)
def _carpet():
    s, ox, oy = 20, 80, 46
    parts, lab = [], []
    for i in range(3):
        for j in range(3):
            parts.append(rect(ox + i * 8 * s, oy + j * 4 * s, 8 * s, 4 * s, k='muted', fill='b' if (i + j) % 2 == 0 else 'v', sw=1))
            lab.append(text(ox + i * 8 * s + 4 * s, oy + j * 4 * s + 2 * s + 6, '8 × 4', k='muted', size=15))
    for x in (8, 16):
        parts.append(line(ox + x * s, oy, ox + x * s, oy + 12 * s, k='red', w=4))
    for y in (4, 8):
        parts.append(line(ox, oy + y * s, ox + 24 * s, oy + y * s, k='red', w=4))
    parts.append(rect(ox, oy, 24 * s, 12 * s, k='pen', sw=5))
    lab += [text(ox + 12 * s, oy - 12, '24 m', k='ink', size=18), text(ox - 16, oy + 6 * s, '12 m', k='ink', size=18, rotate=-90),
            text(ox, oy + 12 * s + 34, 'blue edge: 24 + 12 + 24 + 12 = 72 m', k='pen', size=18, anchor='start'),
            text(ox, oy + 12 * s + 60, 'red seams: 2 × 24 + 2 × 12 = 72 m', k='red', size=18, anchor='start'),
            text(ox + 24 * s, oy + 12 * s + 60, 'total 144 m', k='green', size=22, anchor='end', font='scrawl')]
    return svg(640, 360, rough(*parts) + ''.join(lab),
               'The 24 by 12 m showroom tiled with nine 8 by 4 m pieces in a 3 by 3 grid; outside edge 72 m in blue, seams 72 m in red')

Q.append(dict(
    n=11, orig=24, answer='C', topic='Area & perimeter',
    question=f"""<p>Mr Daley has bought some used carpeting for his new {hl('24 m x 12 m', 'g', 1)} car showroom. The carpet is in
{hl('8 m x 4 m rectangles', 'g', 2)} which will be joined using a strip of double-sided tape {hl('along all seams', 'y', 3)}.
Additionally, double-sided tape will be needed to stick the carpet {hl('around the edges of the showroom', 'y', 4)}.</p>
<p class="stem">What is the {hl('minimum', 'b', 5)} amount of tape he requires?</p>""",
    options={'A': '72 m', 'B': '108 m', 'C': '144 m', 'D': '216 m', 'E': '288 m'},
    notes=[(1, 'g', 'Floor: 24 × 12 = 288 m².'),
           (2, 'g', 'Each piece is 32 m², so 288 ÷ 32 = <b>9 pieces</b>.'),
           (3, 'y', 'A seam is where two pieces meet. One strip covers it.'),
           (4, 'y', 'Plus the outside edge of the room: its perimeter.'),
           (5, 'b', 'Lay the pieces to keep the seams short. (Spoiler: the layout makes no difference!)')],
    steps=[
        f"""<p>Edges first: the perimeter of the showroom.</p>{calc('24 + 12 + 24 + 12 = <b>72 m</b>')}""",
        f"""<p>Lay the pieces neatly: 3 along (3 × 8 = 24) and 3 down (3 × 4 = 12).</p>{_carpet()}
{calc('seams running along: 2 lines × 24 m = 48 m', 'seams running down: 2 lines × 12 m = 24 m', 'seams = 72 m')}""",
        f"""{calc(f'tape = 72 + 72 = {boxed("144 m")}')}
{note('Would a cleverer layout use less? No. Each piece has a 24 m perimeter, so 9 pieces have 216 m of edge. The outside takes 72 m; the other 144 m is seams, each counted twice (a piece on each side), so seams are always 72 m.', 'check')}""",
    ],
    answer_text='144 m: 72 m round the edge plus 72 m of seams.',
    why={'A': '72 m is only the edge (or only the seams). He needs both.',
         'B': '108 m halves all 216 m of piece edges. But the outside edges have a piece on one side only, so they aren’t shared.',
         'D': '216 m tapes all the way round every piece (9 × 24), which tapes each seam twice.',
         'E': '288 is the floor <b>area</b> in m², not a length of tape.'},
    fast='Perimeter 72 m + seams (2 × 24 + 2 × 12 = 72 m) = 144 m.',
))

# ---------------------------------------------------------------- 12 (Q25)
def _theatre():
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    cw, ch, x0, y0 = 70, 54, 30, 40
    weeks = [[None] * 6 + [7], list(range(8, 15)), list(range(15, 22)), list(range(22, 29))]
    parts, lab = [], []
    for i, d in enumerate(days):
        lab.append(text(x0 + cw * i + cw / 2, 30, d, k='muted', size=16))
    for r, wk in enumerate(weeks):
        tot = 0
        for c, d in enumerate(wk):
            x, y = x0 + c * cw, y0 + r * ch
            if d is None:
                parts.append(rect(x + 3, y + 3, cw - 6, ch - 6, k='muted', sw=1, fill='none'))
                continue
            n = 0 if d == 25 else 3 if c == 6 else 2 if c in (3, 4) else 1
            tot += n
            f = 'p' if d == 25 else 'o' if c == 6 else 'y' if c in (3, 4) else 'paper'
            parts.append(rect(x + 3, y + 3, cw - 6, ch - 6, k='ink', fill=f, sw=1.6))
            lab.append(text(x + 8, y + 18, d, k='ink', size=13, anchor='start', font='print'))
            lab.append(text(x + cw / 2 + 8, y + ch - 12, 'shut' if d == 25 else n, k='red' if d == 25 else 'pen',
                            size=17 if d == 25 else 24, font='scrawl'))
        lab.append(text(x0 + 7 * cw + 14, y0 + r * ch + 34, f'= {tot}', k='green', size=22, anchor='start', font='scrawl'))
    yb = y0 + 4 * ch
    lab += [text(x0, yb + 28, 'Sun–Fri: 1 show (7 pm)   ·   Wed, Thu: +1 matinee (2 pm)', k='ink', size=16, anchor='start'),
            text(x0, yb + 50, 'Sat: 3 shows (2 pm, 5.30 pm, 8.30 pm)   ·   25th (a Wednesday): 0', k='ink', size=16, anchor='start'),
            text(320, yb + 86, '3 + 11 + 11 + 9 = 34 performances', k='green', size=24, font='scrawl')]
    return svg(640, yb + 100, rough(*parts) + ''.join(lab),
               'December calendar from Saturday 7th to Saturday 28th with the number of shows each day; week totals 3, 11, 11 and 9 make 34')

Q.append(dict(
    n=12, orig=25, answer='B', topic='Calendars & counting',
    question=f"""{table([[f"WINTER SPECTACULAR<br>AT<br>THE PLAYTIME THEATRE<br><br>{hl('From: Saturday 7th December', 'g', 1)}<br>{hl('To: Saturday 28th December', 'g')}<br>{hl('Performances nightly at 7 pm (Sun–Fri)', 'y', 2)}<br>{hl('(Saturdays at 5.30 pm and 8.30 pm)', 'y', 3)}<br>{hl('Matinees Weds, Thurs and Sat at 2 pm', 'y', 4)}<br>Tickets from £8<br>{hl('(Theatre closed 25th December)', 'p', 5)}"]])}
<p class="stem">{hl('How many times', 'b', 6)} will the Winter Spectacular be performed at the Playtime Theatre during its run?</p>""",
    options={'A': '31', 'B': '34', 'C': '35', 'D': '36', 'E': '38'},
    notes=[(1, 'g', 'The run starts <b>and</b> ends on a Saturday: 7th, 14th, 21st, 28th are all in.'),
           (2, 'y', 'One evening show each Sunday to Friday.'),
           (3, 'y', 'Saturdays have 2 evening shows instead of the 7 pm one.'),
           (4, 'y', 'Plus an afternoon show on Wednesdays, Thursdays and Saturdays.'),
           (5, 'p', 'The 25th is a Wednesday (7 → 14 → 21 → 28 are Saturdays). You lose its evening show <b>and</b> its matinee.'),
           (6, 'b', 'Count every performance, matinees included. The ticket price is a distraction.')],
    steps=[
        f"""<p>Sketch the calendar. 7th is a Saturday, so the Saturdays are 7, 14, 21, 28 and Christmas Day is a Wednesday.</p>{_theatre()}""",
        f"""<p>Or count by type:</p>
{calc('Saturdays: 4 × 3 = 12', 'Sun–Fri evenings: 18 days (three weeks of 6), minus the 25th = 17',
      'Wed and Thu matinees: 6 (three of each), minus the 25th = 5', f'12 + 17 + 5 = {boxed("34")}')}""",
    ],
    answer_text='34 performances: 12 on Saturdays, 17 weekday evenings and 5 midweek matinees.',
    why={'A': '31 counts only three Saturdays (missing the first or last day of the run), so it is 3 shows short.',
         'C': '35 takes off Christmas Day’s evening show but forgets its matinee (the 25th is a Wednesday).',
         'D': '36 forgets that the theatre is closed on the 25th.',
         'E': '38 adds a 7 pm show on Saturdays as well. Saturdays have 5.30 and 8.30 instead.'},
    fast='Week by week: Sat 7th = 3, then 11 and 11 for the two full weeks, then 11 − 2 = 9 for Christmas week. 34.',
))

# ---------------------------------------------------------------- 13 (Q26)
def _pairs():
    import math
    cx, cy, R = 150, 140, 88
    pts = [(cx + R * math.cos(math.radians(90 + 60 * i)), cy - R * math.sin(math.radians(90 + 60 * i))) for i in range(6)]
    parts, lab = [], []
    for i in range(6):
        for j in range(i + 1, 6):
            parts.append(line(*pts[i], *pts[j], k='pen', w=1.6))
    for p in pts:
        parts.append(circle(*p, 9, k='ink', fill='y', sw=1.8))
    lab += [text(cx, 262, '6 people: 15 lines', k='pen', size=18, font='scrawl'),
            text(cx, 284, 'one handshake per pair', k='ink', size=15)]
    parts += [arrow(418, 104, 538, 104, k='green', bend=-0.22), arrow(538, 130, 418, 130, k='orange', bend=-0.22)]
    lab += [stick_person(400, 170, k='ink', s=1.3), stick_person(556, 170, k='ink', s=1.3),
            text(400, 196, 'A', k='ink', size=18), text(556, 196, 'B', k='ink', size=18),
            text(478, 66, 'card A → B', k='green', size=16), text(478, 176, 'card B → A', k='orange', size=16),
            text(478, 236, 'cards: 2 per pair', k='red', size=19, font='scrawl'),
            text(478, 262, '6 × 5 = 30, not 15', k='red', size=19, font='scrawl')]
    return svg(640, 296, rough(*parts) + ''.join(lab),
               'Six dots joined by 15 lines, one per pair; and two people swapping two cards, so cards count each pair twice')

Q.append(dict(
    n=13, orig=26, answer='E', topic='Counting pairs',
    question=f"""<p>A popular option at the Pizza Parlour is the 'Plus Two' pizza, which is a basic cheese and tomato
pizza plus a choice of any {hl('two different', 'y', 1)} additional toppings from the following list:</p>
<p>Tuna &nbsp;&nbsp; Ham &nbsp;&nbsp; Chicken &nbsp;&nbsp; Onion &nbsp;&nbsp; Mushroom &nbsp;&nbsp; Sweetcorn</p>
<p>This gives 15 variations, which can be calculated as follows:</p>
<p>Each of the six additional toppings can be combined with one of the other five to create 30 pairs,
but {hl('this counts each pair twice', 'y', 2)}, e.g. tuna and ham; ham and tuna.</p>
<p class="stem">Which of the following {hl('does not', 'b', 3)} give a result of 15?</p>""",
    options={'A': 'The total number of matches when six teams play each other once.',
             'B': 'The total number of handshakes when six people shake hands with each other.',
             'C': 'The total number of crackers needed for six children to pull a cracker with each of the others.',
             'D': 'The total number of partnerships possible when two people are chosen from a shortlist of six to represent their society in a debate.',
             'E': 'The total number of cards sent when six friends send each other Christmas cards.'},
    notes=[(1, 'y', 'Choosing 2 out of 6, where the order doesn’t matter.'),
           (2, 'y', 'Tuna + ham is the same pizza as ham + tuna, so 6 × 5 = 30 is halved to 15.'),
           (3, 'b', 'Look for the situation where A → B and B → A are <b>different</b> things.')],
    steps=[
        f"""<p>The 15 comes from: 6 × 5 = 30, then ÷ 2 because each pair is one thing. So ask of each option:
does one <b>pair</b> of the six give exactly <b>one</b> thing?</p>{_pairs()}""",
        f"""{calc(f'A: one match per pair of teams {ar()} 15 {tick()}', f'B: one handshake per pair {ar()} 15 {tick()}',
      f'C: one cracker per pair of children {ar()} 15 {tick()}', f'D: one partnership per pair {ar()} 15 {tick()}',
      f'E: each pair sends <b>two</b> cards (one each way) {ar()} 30 {cross()}')}
{calc(f'answer {boxed("E")}')}""",
    ],
    answer_text='Christmas cards: A’s card to B and B’s card to A are different cards, so it is 6 × 5 = 30.',
    why={'A': 'One match for each pair of teams: 15.',
         'B': 'One handshake for each pair of people: 15.',
         'C': 'Each pair of children shares one cracker: 15.',
         'D': 'A partnership is just a pair of the six: 15.'},
    fast='Which one counts each pair twice? Cards: A sends to B and B sends to A. 6 × 5 = 30.',
))

# ---------------------------------------------------------------- 14 (Q30)
def _fuel():
    s, x0 = 0.9, 70
    parts = [rect(x0, 56, 375 * s, 44, k='ink', fill='g', sw=1.8), rect(x0 + 375 * s, 56, 125 * s, 44, k='ink', fill='paper', sw=1.8),
             rect(x0, 172, 550 * s, 50, k='ink', fill='none', sw=2.2), rect(x0, 172, 375 * s, 50, k='ink', fill='y', sw=1.8),
             arrow(x0 + 170, 104, x0 + 170, 166, k='red', bend=0)]
    lab = [text(320, 34, '20,000 miles ÷ 40 mpg = 500 gallons of E75', k='pen', size=19, font='scrawl'),
           text(x0 + 375 * s / 2, 84, 'ethanol 75% = 375', k='ink', size=17),
           text(x0 + 375 * s + 125 * s / 2, 84, 'petrol 125', k='muted', size=15),
           text(x0 + 186, 142, 'only this part comes from beet', k='red', size=15, anchor='start'),
           text(x0 + 375 * s / 2, 203, '375 gallons', k='ink', size=17),
           text(x0 + 375 * s + 175 * s / 2, 203, 'rest of acre', k='muted', size=14),
           text(x0, 246, 'one acre = 550 gallons', k='muted', size=15, anchor='start'),
           text(x0 + 550 * s, 246, '375 ÷ 550 ≈ 0.68 acre', k='green', size=20, anchor='end', font='scrawl')]
    return svg(640, 260, rough(*parts) + ''.join(lab),
               'Bar of 500 gallons of fuel split into 375 ethanol and 125 petrol; the 375 gallons fill about 0.68 of an acre bar of 550 gallons')

Q.append(dict(
    n=14, orig=30, answer='B', topic='Rates & units',
    question=f"""<p>An acre of land planted with sugar beet produces {hl('550 gallons of ethanol', 'g', 1)} from the sugar by
fermentation. A car converted to run on {hl('E75 (a 75% ethanol, 25% petrol mixture)', 'y', 2)} can do {hl('40 miles per gallon', 'g', 3)}.</p>
<p class="stem">If you drive {hl('20,000 miles per year', 'g')}, how many acres of sugar beet will be needed to produce the
{hl('ethanol you need', 'b', 4)}?</p>""",
    options={'A': '(20000/40 x 25/100)/550 = 0.23', 'B': '(20000/40 x 75/100)/550 = 0.68', 'C': '(20000/40 x 100/75)/550 = 1.21',
             'D': '(40/20000 x 100/75) x 550 = 1.47', 'E': '(20000/40 x 100/25)/550 = 3.63'},
    notes=[(1, 'g', 'One acre gives 550 gallons of <b>ethanol</b>.'),
           (2, 'y', 'Each gallon of fuel is only 75% ethanol. The other 25% is petrol, which beet doesn’t make.'),
           (3, 'g', '40 miles per gallon of the <b>mixture</b>.'),
           (4, 'b', 'Only the ethanol part has to come from the beet.')],
    steps=[
        f"""<p>Follow the units: miles {ar()} gallons of fuel {ar()} gallons of ethanol {ar()} acres.</p>
{calc('20,000 ÷ 40 = 500 gallons of E75', '75% of 500 = 375 gallons of ethanol', f'375 ÷ 550 ≈ 0.68 acres')}{_fuel()}""",
        f"""<p>Now find the option doing exactly those steps: × 75/100, then ÷ 550 {ar()} {boxed("B")}</p>
{note('Quick sense check: 375 is about two-thirds of 550, so the answer is a bit under 0.7.', 'tip')}""",
    ],
    answer_text='(20000/40 × 75/100)/550 = 0.68 acres.',
    why={'A': 'Uses 25%, the petrol share. The beet makes the ethanol, which is 75%.',
         'C': 'Divides by 75% instead of multiplying, giving more ethanol (667 gallons) than fuel used (500). Impossible.',
         'D': 'Upside down: 40 ÷ 20,000 is gallons per mile, and then it multiplies by 550. The units don’t work.',
         'E': 'Divides by 25%: that makes 2,000 gallons from 500 gallons of fuel. Nonsense.'},
    fast='500 gallons of fuel, 75% ethanol = 375, ÷ 550 ≈ 0.68. That is formula B.',
))

# ---------------------------------------------------------------- 15 (Q31)
def _range():
    rows = [('Clipper', 60, 12), ('Ghia', 70, 11), ('Sedan', 75, 10), ('Estate', 80, 8), ('Saloon', 82, 5)]
    X = lambda v: 110 + v * 0.56
    parts, lab = [], []
    for i, (name, t, e) in enumerate(rows):
        y = 34 + i * 38
        v = t * e
        parts.append(rect(X(0), y, X(v) - X(0), 28, k='ink', fill='g' if name == 'Ghia' else 'b', sw=1.6))
        lab += [text(100, y + 20, name, k='ink', size=17, anchor='end'),
                text(X(v) - 8, y + 20, f'{t} × {e} = {v}', k='ink', size=16, anchor='end')]
    lab += [text(X(770) + 6, 34 + 38 + 22, '← furthest', k='green', size=17, font='scrawl', anchor='start'),
            text(110, 22, 'miles on one full tank = litres × miles per litre', k='muted', size=15, anchor='start')]
    return svg(640, 236, rough(*parts) + ''.join(lab),
               'Range on a full tank: Clipper 720, Ghia 770, Sedan 750, Estate 640, Saloon 410 miles; Ghia goes furthest')

Q.append(dict(
    n=15, orig=31, answer='B', topic='Tables & rates',
    question=f"""<p>The following table gives information about five different car models.</p>
{table([['Clipper', '1.5', '60', '12'], ['Ghia', '2.0', '70', '11'], ['Sedan', '2.5', '75', '10'], ['Estate', '3.0', '80', '8'], ['Saloon', '4.0', '82', '5']],
       head=['Model', hl('Engine capacity (litres)', 'p', 1), hl('Fuel tank capacity (litres)', 'g', 2), hl('Maximum fuel economy (miles per litre)', 'g', 3)])}
<p class="stem">Which of these models will travel {hl('furthest on one full tank', 'b', 4)} of petrol {hl('under optimum conditions', 'y', 5)}?</p>""",
    options={'A': 'Clipper', 'B': 'Ghia', 'C': 'Sedan', 'D': 'Estate', 'E': 'Saloon'},
    notes=[(1, 'p', 'Engine size is a distraction. You don’t need it.'),
           (2, 'g', 'How many litres one tank holds.'),
           (3, 'g', 'How far each litre goes.'),
           (4, 'b', 'Distance on a tank = litres × miles per litre.'),
           (5, 'y', 'Best conditions, so use the maximum economy figure as it is.')],
    steps=[
        f"""<p>Multiply tank size by miles per litre for each car:</p>
{calc('Clipper 60 × 12 = 720', 'Ghia 70 × 11 = 770', 'Sedan 75 × 10 = 750', 'Estate 80 × 8 = 640', 'Saloon 82 × 5 = 410')}
{note('× 11 trick: 70 × 11 = 700 + 70 = 770.', 'tip')}""",
        f"""{_range()}{calc(f'furthest = {boxed("Ghia")} (770 miles)')}""",
    ],
    answer_text='Ghia: 70 litres × 11 miles per litre = 770 miles.',
    why={'A': 'The Clipper has the best economy, but its small tank only gives 720 miles.',
         'C': 'The Sedan is close, 750 miles, but 20 short of the Ghia.',
         'D': 'The Estate manages only 640 miles.',
         'E': 'The Saloon has the biggest tank but the worst economy: just 410 miles.'},
    fast='Tank × mpl: 720, 770, 750, 640, 410. Ghia.',
))

# ---------------------------------------------------------------- 16 (Q32)
def _teeth():
    groups = ['25–34', '35–44', '45–54', '55–64', '65–74', '75+']
    X = lambda i: 90 + i * 96
    Yp = lambda p: 250 - p * 2.1
    prof = [1, 3, 10, 22, 48, 71]
    semi = [3, 14, 34, 58, 71, 87]
    others = [[1, 4, 14, 34, 53, 71], [2, 7, 23, 48, 66, 82]]
    parts, lab = [], []
    gap = [(X(i), Yp(v)) for i, v in enumerate(semi)] + [(X(i), Yp(v)) for i, v in reversed(list(enumerate(prof)))]
    parts.append(poly(gap, k='none', fill='y', sw=0))
    for row in others:
        parts.append(poly([(X(i), Yp(v)) for i, v in enumerate(row)], k='muted', sw=1.4, closed=False))
    parts.append(poly([(X(i), Yp(v)) for i, v in enumerate(semi)], k='orange', sw=3, closed=False))
    parts.append(poly([(X(i), Yp(v)) for i, v in enumerate(prof)], k='pen', sw=3, closed=False))
    for i, (a, b) in enumerate(zip(prof, semi)):
        parts += [circle(X(i), Yp(a), 5, k='pen', fill='paper'), circle(X(i), Yp(b), 5, k='orange', fill='paper')]
        lab.append(text(X(i), 274, groups[i], k='ink', size=15))
    parts += [line(60, Yp(0), 600, Yp(0), k='ink', w=2), line(60, Yp(50), 600, Yp(50), k='muted', w=1.4, dash=True)]
    lab += [text(600, Yp(50) - 6, 'half', k='muted', size=14, anchor='end'), text(50, Yp(0) + 5, '0%', k='muted', size=14, anchor='end'),
            text(50, Yp(50) + 5, '50%', k='muted', size=14, anchor='end'), text(50, Yp(100) + 5, '100%', k='muted', size=14, anchor='end'),
            text(X(1) - 30, Yp(40), 'semi/unskilled manual', k='orange', size=17, anchor='start'),
            text(X(4) + 4, Yp(30), 'professionals:', k='pen', size=17, anchor='start'),
            text(X(4) + 4, Yp(30) + 20, 'lower at every age', k='pen', size=15, anchor='start'),
            text(320, 296, 'age group (grey lines: the two middle groups)', k='muted', size=14)]
    return svg(640, 306, rough(*parts) + ''.join(lab),
               'Line chart of percentage with no natural teeth by age: the professionals line is below the semi-skilled and unskilled line at every age')

Q.append(dict(
    n=16, orig=32, answer='B', topic='Reading tables',
    question=f"""<p>The table below shows the {hl('percentage', 'p', 1)} of adults, grouped by age and socio-economic group, with
no natural teeth.</p>
{table([[hl('Professionals, employers and managers', 'g', 2), '1', '3', '10', '22', '48', '71'],
        ['Intermediate', '1', '4', '14', '34', '53', '71'],
        ['Skilled manual', '2', '7', '23', '48', '66', '82'],
        [hl('Semi-skilled and unskilled manual', 'g'), '3', '14', '34', '58', '71', '87']],
       head=['Age group →', '<i>25–34</i>', '<i>35–44</i>', '<i>45–54</i>', '<i>55–64</i>', '<i>65–74</i>', '<i>75+</i>'])}
<p class="stem">Which one of the following conclusions {hl('can be drawn from the table', 'b', 3)} above?</p>""",
    options={'A': 'Most people have lost their natural teeth by the age of 55.',
             'B': 'Professional people tend to keep their natural teeth longer than semi-skilled and unskilled manual workers.',
             'C': 'Manual work is bad for your teeth.', 'D': 'People without natural teeth tend not to be employed as managers.',
             'E': 'There are over three times as many 45–54 year-old manual workers with no teeth as professionals.'},
    notes=[(1, 'p', 'Percentages of each group, not numbers of people. We don’t know how big each group is.'),
           (2, 'g', 'Compare the top row with the bottom row, age by age.'),
           (3, 'b', 'It must follow from the numbers alone: no guessing about causes.')],
    steps=[
        f"""<p>Compare professionals with semi-skilled/unskilled in each age group:</p>
{calc('1 vs 3, 3 vs 14, 10 vs 34, 22 vs 58, 48 vs 71, 71 vs 87', f'professionals are lower <b>every time</b> {ar()} they keep their teeth longer')}{_teeth()}""",
        f"""<p>Quick check of the others: A needs over 50% before 55, but the 45–54 column is only 10–34%. C and D claim a cause, which a table
of percentages can’t show. E talks about numbers of people, but we only have percentages. {ar()} {boxed('B')}</p>""",
    ],
    answer_text='B: in every age group a smaller percentage of professionals have lost all their teeth.',
    why={'A': 'Before 55 (the 45–54 column) the figures are only 10% to 34%, nowhere near “most”.',
         'C': 'The table shows a link, not a cause. Diet, money or dental care could explain it.',
         'D': 'Turns the link round: the table says nothing about who gets employed as a manager.',
         'E': 'The table gives percentages, not numbers. Without the size of each group you can’t compare how many people.'},
    fast='Read across: professionals have the lowest % in every column, semi/unskilled the highest. That is B. The rest claim causes or numbers.',
))

# ---------------------------------------------------------------- 17 (Q36)
def _catchup():
    X = lambda d: 60 + (d - 15) * 38
    Ya = lambda a: 150 - a * 5.5
    parts, lab = [], []
    pts2 = [(16, 16)] + [(16 + i, 16 - 3 * i) for i in range(1, 10)]
    pts3 = [(25, -11)] + [(25 + i, -11 + 3 * i) for i in range(1, 5)]
    parts += [line(40, Ya(0), 625, Ya(0), k='ink', w=2),
              poly([(X(d), Ya(a)) for d, a in pts2], k='red', sw=3, closed=False),
              poly([(X(d), Ya(a)) for d, a in pts3], k='green', sw=3, closed=False)]
    for d, a in pts2 + pts3[1:]:
        parts.append(circle(X(d), Ya(a), 4, k='ink', fill='paper', sw=1.5))
    parts.append(circle(X(25), Ya(-11), 7, k='red', fill='p', sw=2))
    parts.append(circle(X(29), Ya(1), 7, k='green', fill='g', sw=2))
    lab += [text(44, Ya(0) - 8, 'on target (average 5)', k='ink', size=15, anchor='start'),
            text(X(16) + 10, Ya(16) - 6, 'day 16: just over 16 miles ahead', k='pen', size=16, anchor='start'),
            text(X(20.5) + 10, Ya(2.5) - 4, '2 miles a day: −3 each day', k='red', size=16, anchor='start'),
            text(X(25), Ya(-11) + 30, 'today (day 25): about 11 behind', k='red', size=16),
            text(625, Ya(-6) + 8, '8 miles a day:', k='green', size=15, anchor='end'),
            text(625, Ya(-6) + 26, '+3 each day', k='green', size=15, anchor='end'),
            text(625, Ya(1) - 16, '4 days ✓', k='green', size=20, anchor='end', font='scrawl')]
    for d in (16, 25, 29):
        lab.append(text(X(d), 266, f'day {d}', k='muted', size=14))
    return svg(640, 276, rough(*parts) + ''.join(lab),
               'Graph of miles ahead of the 5-a-day target: about 16 ahead on day 16, falling 3 a day to about 11 behind on day 25, then climbing 3 a day to above zero on day 29')

Q.append(dict(
    n=17, orig=36, answer='B', topic='Averages',
    question=f"""<p>Last month, in an attempt to improve my fitness, I began to run daily. The {hl('maximum distance', 'g', 1)} I have
time to fit in on any particular day is {hl('8 miles', 'g')}, but my aim is to maintain {hl('an average of at least 5 miles per day', 'y', 2)}.</p>
<p>{hl('After 15 days my average was just under 6 miles per day', 'g', 3)}, then {hl('the following day I increased my average to just over 6', 'p', 4)}. Since then ({hl('for the last 9 days, up to and including today', 'g', 5)}) I have been able to
run only 2 miles each day.</p>
<p class="stem">What is the {hl('<b>minimum</b> number of days from now', 'b', 6)} until I can bring my average back up to 5 miles per
day?</p>""",
    options={'A': '2 days', 'B': '4 days', 'C': '9 days', 'D': '18 days', 'E': '26 days'},
    notes=[(1, 'g', 'The best catch-up day is 8 miles.'),
           (2, 'y', 'Average 5 means the total must be at least 5 × (number of days).'),
           (3, 'g', 'Total after 15 days: just under 15 × 6 = 90.'),
           (4, 'p', 'This is the one that matters: after 16 days the total is just over 16 × 6 = <b>96</b>.'),
           (5, 'g', '9 more days at 2 miles: + 18 miles. Today is day 16 + 9 = <b>25</b>.'),
           (6, 'b', 'So run the maximum 8 miles every day from now on.')],
    steps=[
        f"""<p>Where am I today?</p>
{calc('days so far: 16 + 9 = 25', 'miles so far: just over 96 + 9 × 2 = just over 114', 'needed for an average of 5: 25 × 5 = 125',
      f'behind by just under <b>11 miles</b>')}""",
        f"""<p>Each new day the target goes up by 5. Running 8 gains 8 − 5 = <b>3 miles</b> a day on it.</p>{_catchup()}
{calc(f'3 days: 3 × 3 = 9 {ar()} still about 2 short {cross()}', f'4 days: 4 × 3 = 12 {ar()} back above target {tick()}', f'answer = {boxed("4 days")}')}""",
        f"""{note('With totals: after 4 more days, just over 114 + 32 = just over 146, and 29 × 5 = 145 ✓. After 3: just over 138, but 28 × 5 = 140 ✗.', 'check')}""",
    ],
    answer_text='4 days of 8 miles: each gains 3 miles on the target, and he is about 11 behind.',
    why={'A': 'Two 8-mile days win back only 6 miles; he is about 11 behind.',
         'C': '9 undoes the nine 2-mile days one for one ((5 − 2) × 9 = 27 behind, ÷ 3). That ignores the 16 miles he was ahead on day 16.',
         'D': '18 aims for an average of 6 again, not 5: 150 − 114 = 36 behind, gaining only 2 a day.',
         'E': '26 is about how many days have passed. He only needs to win back about 11 miles, at 3 a day.'},
    fast='Day 25, just over 114 miles, need 125: about 11 short. Each 8-mile day gains 3: 4 days.',
))
