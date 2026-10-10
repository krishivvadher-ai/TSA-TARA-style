from wslib import *

Y = 2014
Q = []

# ---------------------------------------------------------------- 1 (Q2)
def _calendar():
    days = 'MTWTFSS'
    cw, ch, x0, y0 = 62, 44, 14, 34
    parts, labels = [], []
    for i, d in enumerate(days):
        labels.append(text(x0 + cw * i + cw / 2, 24, d, k='muted', size=17))
    who, turn = {}, 0
    for day in range(1, 32):
        wd = (day - 1) % 7
        works = wd < 5 or (wd == 5 and day in (6, 20))
        if works:
            who[day] = 'AB'[turn % 2]
            turn += 1
    for day in range(1, 32):
        wd, wk = (day - 1) % 7, (day - 1) // 7
        x, y = x0 + cw * wd, y0 + ch * wk
        fill = {'A': 'b', 'B': 'o'}.get(who.get(day), 'none')
        parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='ink' if day in who else 'muted', fill=fill, sw=1.6))
        labels.append(text(x + 10, y + 19, day, k='ink', size=14, anchor='start', font='print'))
        if day in who:
            labels.append(text(x + cw - 14, y + ch - 10, who[day], k='pen' if who[day] == 'A' else 'orange', size=20, font='scrawl'))
        elif wd == 5:
            labels.append(text(x + cw / 2 + 6, y + ch - 9, 'off', k='muted', size=16, font='scrawl'))
    a = sum(1 for v in who.values() if v == 'A')
    b = sum(1 for v in who.values() if v == 'B')
    labels.append(text(x0 + 7 * cw + 20, y0 + 60, f'A drives {a}', k='pen', size=24, anchor='start', font='scrawl'))
    labels.append(text(x0 + 7 * cw + 20, y0 + 92, f'B drives {b}', k='orange', size=24, anchor='start', font='scrawl'))
    labels.append(text(x0 + 7 * cw + 20, y0 + 130, f'25 days in total', k='ink', size=20, anchor='start'))
    labels.append(text(x0 + 7 * cw + 20, y0 + 156, 'Saturdays 6 and 20', k='ink', size=17, anchor='start'))
    labels.append(text(x0 + 7 * cw + 20, y0 + 178, 'are in the rotation too', k='ink', size=17, anchor='start'))
    return svg(720, y0 + ch * 5 + 14, rough(*parts) + ''.join(labels),
               'Calendar of a 31-day month starting on Monday with working days alternating A and B; A drives 13, B drives 12')

Q.append(dict(
    n=1, orig=2, answer='C', topic='Calendars & rotations', attempt='D',
    question=f"""<p>Two neighbours work for the same company and share the journey to work, driving alternately in
{hl('strict rotation', 'y', 1)}. They work Monday to Friday each week and {hl('every other Saturday', 'p', 2)}. (They always
work the same Saturdays as each other.)</p>
<p class="stem">What is the {hl('<b>maximum</b>', 'b', 3)} number of days either of them has to drive in a {hl('calendar month', 'g', 4)}?</p>""",
    options={'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15'},
    notes=[(1, 'y', 'Every working day is in the rotation, A, B, A, B… <b>Saturdays included.</b>'),
           (2, 'p', 'Only alternate Saturdays: 1st, 3rd, 5th… never two in a row.'),
           (3, 'b', 'Pick the month with the most working days, then give the odd day to whoever starts.'),
           (4, 'g', 'The longest month has 31 days.')],
    steps=[
        f"""<p>Most working days fit in a <b>31-day month</b> = 4 full weeks + 3 extra days.</p>
{calc(f'4 weeks {ar()} 20 weekdays + 4 Saturdays', f'best 3 extra days = 3 weekdays (Mon, Tue, Wed) {ar()} 23 weekdays')}""",
        f"""<p>Saturdays: that month has 4 Saturdays and they work every other one.</p>
{calc(f'4 Saturdays {ar()} work 2 of them', f'23 + 2 = <b>25 working days</b>')}
{note('Starting the month on a Thursday gives 22 weekdays and 5 Saturdays: they work 3 of them, so 22 + 3 = 25 again. You can never beat 25.', 'check')}""",
        f"""<p>Now share the 25 days in strict rotation, A, B, A, B…</p>
{_calendar()}
{calc(f'25 days {ar()} A gets 13, B gets 12', f'maximum = {boxed("13")}')}""",
    ],
    answer_text='13 days: 25 working days shared alternately.',
    why={'A': '11 is too few: 25 days can only split 13 and 12.',
         'B': '12 is the <b>other</b> neighbour’s share. It is also what you get if you forget the Saturdays (23 weekdays split 12 and 11).',
         'D': '14 comes from giving <b>both</b> Saturdays to one driver (12 weekdays + 2 Saturdays). Saturdays are part of the strict rotation, so they alternate too.',
         'E': '15 would need at least 29 working days. A month never has that many.'},
    fast='Most working days in a month = 23 weekdays + 2 Saturdays = 25. Half of 25 rounded up = 13.',
))

# ---------------------------------------------------------------- 2 (Q6)
def _cycle_graph():
    X = lambda t: 70 + 52 * t
    Yd = lambda d: 286 - d * 0.125
    parts, lab = [], []
    parts.append(line(X(0), Yd(0), X(10.4), Yd(0), k='ink', head=True))
    parts.append(line(X(0), Yd(0), X(0), Yd(1950), k='ink', head=True))
    for t in range(0, 11):
        lab.append(text(X(t), Yd(0) + 22, t, k='muted', size=15))
    lab.append(text(X(5), Yd(0) + 44, 'time (minutes)', k='ink', size=17))
    for d, name in ((0, 'home'), (400, 'lights 1'), (1300, 'lights 2'), (1800, 'office')):
        lab.append(text(X(0) - 8, Yd(d) + 5, name, k='ink', size=15, anchor='end'))
    for d in (400, 1300):
        for t0 in range(0, 10, 2):
            colour = 'green' if (t0 // 2) % 2 == 0 else 'red'
            parts.append(line(X(t0) + 2, Yd(d), X(t0 + 2) - 2, Yd(d), k=colour, w=7))
    for t in (2, 4, 6, 8):
        parts.append(line(X(t), Yd(400), X(t), Yd(1300), k='muted', w=1.2, dash=True))
    pts = [(2 / 3, 0), (2, 400), (4, 400), (7, 1300), (8, 1300), (29 / 3, 1800)]
    parts.append(poly([(X(t), Yd(d)) for t, d in pts], k='pen', sw=3, closed=False))
    lab += [text(X(3), Yd(400) - 14, 'wait 2 min', k='red', size=20, font='scrawl'),
            text(X(7.5), Yd(1300) - 14, 'wait 1 min', k='red', size=20, font='scrawl'),
            text(X(6.1), Yd(850) + 4, 'ride 3 min', k='pen', size=18, anchor='start'),
            text(X(1.25), Yd(200) - 4, '80 s', k='pen', size=16, anchor='end'),
            text(X(8.7), Yd(1600), '100 s', k='pen', size=16, anchor='end'),
            text(X(5), Yd(1300) - 40, 'dashed lines: both lights change together', k='muted', size=15)]
    parts.append(line(X(2 / 3), Yd(0) + 62, X(29 / 3), Yd(0) + 62, k='orange', tail=True, head=True, w=2))
    lab.append(text(X(5.2), Yd(0) + 86, 'whole journey = 9 minutes', k='orange', size=20, font='scrawl'))
    lab.append(text(X(10.2), Yd(400) - 10, 'green / red', k='muted', size=14, anchor='end'))
    return svg(640, 390, rough(*parts) + ''.join(lab),
               'Distance-time graph of the worst case: wait 2 minutes at the first lights, ride 3 minutes, wait 1 minute at the second lights')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Speed, time & timetables', attempt='E',
    question=f"""<p>Central Avenue is a long straight road, several kilometres long. Both my home and my office are
on Central Avenue, and the diagram below shows their positions, together with two sets of
traffic lights that lie in between.</p>
{fig(Y, 'q02_road', 'Home, then 400 m to the first lights, 900 m to the second lights, then 500 m to the office', 520)}
<p>Both sets of lights turn to green for Central Avenue traffic {hl('simultaneously', 'p', 1)}, {hl('showing green for exactly two minutes, turning green again exactly two minutes later', 'y', 2)}.</p>
<p>I cycle to work every morning at a steady speed of {hl('5 metres per second', 'g', 3)} (except, of course,
whilst waiting at traffic lights).</p>
<p class="stem">What is the {hl('<b>longest</b>', 'b', 4)} journey time I can expect the journey to work to take?</p>""",
    options={'A': '6 minutes', 'B': '7 minutes', 'C': '8 minutes', 'D': '9 minutes', 'E': '10 minutes'},
    notes=[(1, 'p', 'The two sets of lights are <b>linked</b>: they change at the same moment. That limits the waiting.'),
           (2, 'y', 'One cycle = 2 min green, 2 min red, then repeat (4 minutes).'),
           (3, 'g', '5 m every second, so divide each distance by 5 to get seconds.'),
           (4, 'b', 'Worst case, but it must be a case that can really happen.')],
    steps=[
        f"""<p>Riding time first (no waiting):</p>
{calc(f'400 ÷ 5 = 80 s', f'900 ÷ 5 = 180 s = 3 min', f'500 ÷ 5 = 100 s', f'total = 360 s = <b>6 min</b> of riding')}""",
        f"""<p>Worst luck at the first lights: arrive just as they turn red. Wait the full <b>2 minutes</b>.
You set off again at the exact moment both lights go green.</p>""",
        f"""<p>The next 900 m takes exactly 3 minutes, so you reach lights 2 three minutes into their cycle:</p>
{calc(f'green 0 → 2 min, red 2 → 4 min', f'you arrive at 3 min {ar()} red, so wait <b>1 minute</b>')}
{note('If you sail through lights 1 on green instead, you still reach lights 2 at most 1 minute before they go green. So the most waiting possible is 2 + 1 = 3 minutes.', 'check')}""",
        f"""<p>Picture the worst case on a distance–time graph (flat bits = waiting):</p>
{_cycle_graph()}
{calc(f'6 min riding + 2 min + 1 min waiting = {boxed("9 minutes")}')}""",
    ],
    answer_text='9 minutes: 6 riding + 2 waiting at the first lights + 1 waiting at the second.',
    why={'A': '6 minutes is the riding time with no waiting at all, which is the <b>shortest</b> journey.',
         'B': '7 minutes only adds one short wait.',
         'C': '8 minutes waits at the first lights but forgets the second set.',
         'E': '10 minutes waits the full 2 minutes at <b>both</b> lights. That can’t happen, because they change together and you arrive at lights 2 halfway through red.'},
    fast='Ride 1800 m at 5 m/s = 6 min. Max wait 2 min at lights 1; you then reach lights 2 three minutes into the cycle, so 1 more. 6 + 2 + 1 = 9.',
))

# ---------------------------------------------------------------- 3 (Q7)
def _size_check():
    s = 6
    parts = [rect(30, 40, 30 * s, 16 * s, k='green', sw=2.5),
             rect(36, 52, 20 * s, 12 * s, k='pen', fill='b', sw=2),
             rect(250, 26, 50 * s * 0.62, 25 * s * 0.62, k='red', fill='p', sw=2.2)]
    lab = [text(30 + 15 * s, 30, 'letter limit 30 × 16 cm', k='green', size=17),
           text(36 + 10 * s, 52 + 6 * s + 6, '20 × 12 cm, 110 g', k='ink', size=16),
           text(36 + 10 * s, 52 + 6 * s + 26, 'fits, so LETTER', k='pen', size=18, font='scrawl'),
           text(250 + 93, 26 + 47, '50 × 25 × 10 cm', k='ink', size=16),
           text(250 + 93, 26 + 72, 'too big, so PARCEL', k='red', size=18, font='scrawl')]
    return svg(460, 160, rough(*parts) + ''.join(lab), 'The 20 by 12 cm item fits inside the letter limit; the 50 by 25 cm item does not')


def _chunks():
    X = lambda g: 30 + g * 3.2
    parts = [line(X(0), 60, X(125), 60, k='ink', head=True)]
    lab = []
    parts.append(rect(X(0), 44, X(30) - X(0), 16, k='ink', fill='g', sw=1.6))
    for i, c in enumerate(('b', 'b', 'b')):
        parts.append(rect(X(30 + 30 * i), 44, X(30) - X(0), 16, k='ink', fill=c, sw=1.6))
    for g in (0, 30, 60, 90, 120):
        parts.append(line(X(g), 56, X(g), 66, k='ink', w=1.6))
        lab.append(text(X(g), 84, g, k='muted', size=14))
    parts.append(line(X(110), 30, X(110), 70, k='red', w=2.6))
    lab += [text(X(110), 24, '110 g', k='red', size=18, font='scrawl'),
            text(X(15), 38, 'first 30 g', k='green', size=14),
            text(X(75), 38, '3 extra chunks', k='pen', size=15),
            text(X(62), 106, '80 g extra = 2.67 chunks, part of a chunk counts, so 3', k='ink', size=15)]
    return svg(470, 118, rough(*parts) + ''.join(lab), 'Number line showing 110 g needs the first 30 g plus 3 extra 30 g chunks')

Q.append(dict(
    n=3, orig=7, answer='C', topic='Tables & rules', attempt='E',
    question=f"""<p>The United States Postal Service has an online guide to help people using their postal service.
This is an extract:</p>
<p><b>First Class Mail</b></p>
<p>First class mail must be used for handwritten or personal correspondence.</p>
<p><b>First Class Mail Rates</b> – single piece rates</p>
{table([['First 30 grams Letter size mail', '$0.44'],
        [f'Each additional 30 grams {hl("or part thereof", "p", 1)}', '$0.17 up to 360 grams'],
        ['First 30 grams Parcel', '$1.22'],
        ['Each additional 30 grams or part thereof', '$0.17'],
        ['Standard Postcard', '$0.28']])}
<p>{hl('<b>Letters</b>: 30 cm long, 16 cm wide, 1 cm thick, maximum weight 360 grams', 'y', 2)}. ({hl('Any item larger than this must be sent as a parcel', 'y', 3)}).</p>
<p><b>Parcels</b>: Dimensions cannot exceed 1250 cm.</p>
<p>I want to send two items through the post using first class mail. One is {hl('50 cm long, 25 cm wide, 10 cm thick and weighs 300 grams', 'g', 4)}. The other is {hl('20 cm long, 12 cm wide, 0.20 cm thick and weighs 110 grams', 'g', 5)}.</p>
<p class="stem">How much will it cost me to send the items?</p>""",
    options={'A': '$2.92', 'B': '$3.53', 'C': '$3.70', 'D': '$4.04', 'E': '$4.48'},
    notes=[(1, 'p', '“Or part thereof” = any bit of a chunk counts as a whole chunk. <b>Round up.</b>'),
           (2, 'y', 'Check each item against the letter limits <b>before</b> choosing a price.'),
           (3, 'y', 'Only items too big for a letter are parcels.'),
           (4, 'g', 'Item 1: way bigger than 30 × 16 × 1, so it’s a parcel.'),
           (5, 'g', 'Item 2: 20 × 12 × 0.2 fits inside 30 × 16 × 1, so it’s a letter!')],
    steps=[
        f"""<p>Sort each item: letter or parcel?</p>{_size_check()}""",
        f"""<p>Parcel, 300 g: the first 30 g is one price, the rest goes in 30 g chunks.</p>
{calc('300 − 30 = 270 g left', f'270 ÷ 30 = 9 chunks {ar()} 9 × $0.17 = $1.53',
      f'$1.22 + $1.53 = <b>$2.75</b>')}
{note('9 × 0.17: do 10 × 0.17 = 1.70, then take one 0.17 off, giving 1.53.', 'tip')}""",
        f"""<p>Letter, 110 g: same idea, but watch the rounding.</p>{_chunks()}
{calc('110 − 30 = 80 g left', f'80 ÷ 30 = 2.67 {ar()} part of a chunk counts {ar()} 3 chunks',
      f'$0.44 + 3 × $0.17 = $0.44 + $0.51 = <b>$0.95</b>')}""",
        f"""{calc(f'$2.75 + $0.95 = {boxed("$3.70")}')}""",
    ],
    answer_text='$3.70: parcel $2.75 + letter $0.95.',
    why={'A': '$2.92 is too low. You would have to leave out most of the letter’s cost.',
         'B': '$3.53 rounds the letter’s 80 g <b>down</b> to 2 chunks ($0.78). “Or part thereof” means round up.',
         'D': '$4.04 overcharges the parcel (11 chunks instead of 9).',
         'E': '$4.48 charges the small item as a <b>parcel</b> ($1.22 + 3 × 0.17 = $1.73). It fits the letter size, so it is a letter.'},
    fast='Letter or parcel first! Parcel 1.22 + 9 × 0.17 = 2.75. Letter 0.44 + 3 × 0.17 = 0.95. Total 3.70.',
))

# ---------------------------------------------------------------- 4 (Q8)
def _tlf():
    c, ox, oy = 21, 215, 112
    R = lambda x, y, w, h, f: rect(ox + x * c, oy + y * c, w * c, h * c, k='ink', fill=f, sw=1.6)
    parts = [R(0, 0, 6, 2, 'b'), R(1, 2, 2, 8, 'b'),
             R(4, 2, 2, 8, 'g'), R(6, 8, 1, 2, 'g'),
             R(7, 0, 2, 10, 'o'), R(9, 0, 1, 2, 'o'), R(9, 4, 1, 2, 'o')]
    lab = [text(ox + 2 * c, oy + 6.2 * c, 'T', k='pen', size=26, font='scrawl'),
           text(ox + 5 * c, oy + 6.2 * c, 'L', k='green', size=26, font='scrawl'),
           text(ox + 8 * c, oy + 6.2 * c, 'F', k='orange', size=26, font='scrawl'),
           text(ox + 3.5 * c, oy + 9.6 * c, 'gap', k='muted', size=13, rotate=-90),
           text(ox + 6.5 * c, oy + 4.5 * c, 'slot', k='muted', size=13, rotate=-90)]
    # grid ticks along the bottom and left
    for i in range(11):
        lab.append(text(ox + i * c, oy + 10 * c + 16, i, k='muted', size=11))
        lab.append(text(ox - 8, oy + i * c + 4, i, k='muted', size=11, anchor='end'))
    # side-view strips
    sh = 14

    def hstrip(y, cuts, label, ly):
        p = [rect(ox, y, 10 * c, sh, k='red', sw=2)] + [line(ox + x * c, y, ox + x * c, y + sh, k='red', w=2) for x in cuts]
        return p, text(ox + 5 * c, ly, label, k='red', size=17)

    def vstrip(x, cuts, label, lx, anchor):
        p = [rect(x, oy, sh, 10 * c, k='red', sw=2)] + [line(x, oy + y * c, x + sh, oy + y * c, k='red', w=2) for y in cuts]
        return p, text(lx, oy + 5 * c, label, k='red', size=17, anchor=anchor)

    p1, t1 = hstrip(oy + 10 * c + 34, [1, 3, 4, 9], 'from below: 1 | 2 | 1 | 5 | 1', oy + 10 * c + 70)
    p2, t2 = hstrip(oy - 40, [6, 7], 'from above: 6 | 1 | 3', oy - 50)
    p3, t3 = vstrip(ox - 50, [2], 'from left:', ox - 60, 'end')
    p4, t4 = vstrip(ox + 10 * c + 36, [2, 4, 6], 'from right:', ox + 10 * c + 60, 'start')
    t3 += text(ox - 60, oy + 5 * c + 22, '2 | 8', k='red', size=17, anchor='end')
    t5 = text(ox + 10 * c + 60, oy + 5 * c + 22, '2 | 2 | 2 | 4', k='red', size=17, anchor='start')
    cx, cy = ox + 5 * c, oy + 5 * c
    eyes = (eye(cx, oy + 10 * c + 96, facing='up') + eye(cx, oy - 78, facing='down')
            + eye(ox - 110, cy + 52, facing='right') + eye(ox + 10 * c + 100, cy + 52, facing='left'))
    looks = [arrow(cx + 24, oy + 10 * c + 92, cx + 30, oy + 10 * c + 52, k='muted', bend=0.2, w=1.6),
             arrow(cx + 24, oy - 82, cx + 30, oy - 44, k='muted', bend=-0.2, w=1.6),
             arrow(ox - 92, cy + 50, ox - 56, cy + 30, k='muted', bend=0.2, w=1.6),
             arrow(ox + 10 * c + 82, cy + 50, ox + 10 * c + 54, cy + 30, k='muted', bend=-0.2, w=1.6)]
    body = rough(*parts, *p1, *p2, *p3, *p4, *looks) + ''.join(lab) + t1 + t2 + t3 + t4 + t5 + eyes
    return svg(660, 500, body, 'The paperweight drawn flat on a 10 by 10 grid with the four side views next to it')

Q.append(dict(
    n=4, orig=8, answer='B', topic='3D views', attempt='B',
    question=f"""<p>Below is Thomas Leslie Fuller's brass paperweight, which shows his initials.</p>
{fig(Y, 'q04_weight', 'The paperweight: the letters T, L and F joined together as one solid block', 260)}
<p class="stem">Which one of the following is {hl('<b>not</b>', 'b', 1)} a side view of Thomas' paperweight when it is
{hl('placed flat on a table (either side up)', 'y', 2)}?</p>
{fig(Y, 'q04_opts', 'Five long thin strips A to E, each divided by vertical lines in different places', 300)}""",
    options={'A': 'strip A', 'B': 'strip B', 'C': 'strip C', 'D': 'strip D', 'E': 'strip E'},
    notes=[(1, 'b', 'Find the odd one out: four strips are real views, one is impossible.'),
           (2, 'y', 'Lying flat, you can look at it from 4 sides. Turning it over flips each view back to front.')],
    steps=[
        f"""<p>Lay the paperweight flat and draw the front face on a 10 × 10 grid. Then look at it from each of the four sides.
Wherever the nearest edge changes, you see a line in the side view.</p>{_tlf()}""",
        f"""<p>Measure the five strips (each is 10 units long):</p>
{calc('A = 1 | 2 | 1 | 5 | 1 ' + tick() + ' from below',
      'C = 3 | 1 | 6 ' + tick() + ' from above, flipped over',
      'D = 2 | 2 | 2 | 4 ' + tick() + ' from the right',
      'E = 1 | 5 | 1 | 2 | 1 ' + tick() + ' from below, flipped over',
      'B = 2 | 4 | 1 | 3 ' + cross() + ' matches nothing!')}""",
        f"""<p>So the one that is <b>not</b> a side view is {boxed('B')}.</p>
{note('“Either side up” means the mirror image of each view counts too, which is why C and E are allowed.', 'check')}""",
    ],
    answer_text='Strip B (2-4-1-3) does not match any side.',
    why={'A': 'A is the view from below: crossbar, T stem, crossbar, the L + F base, the F’s middle arm.',
         'C': 'C is the view from above (flipped): the top bar, the slot, then the F’s top.',
         'D': 'D is the view from the right: F’s top arm, stem, middle arm, stem.',
         'E': 'E is A flipped over (the view from below with the paperweight upside down).'},
    fast='Count sections: below 5, above 3, left 2, right 4. Only one view has 4 sections (2-2-2-4), so a 2-4-1-3 strip is impossible.',
))

# ---------------------------------------------------------------- 5 (Q12)
def _leftover_line():
    X = lambda m: 40 + (m - 250) * 1.35
    parts = [line(X(250), 70, X(660), 70, k='ink', head=True)]
    lab = []
    for m in range(250, 651, 50):
        parts.append(line(X(m), 64, X(m), 76, k='ink', w=1.5))
        lab.append(text(X(m), 96, f'£{m}', k='muted', size=13))
    pts = [('A', 300, 'red'), ('D', 340, 'red'), ('C', 560, 'orange'), ('E', 580, 'orange'), ('B', 590, 'green')]
    for i, (k, m, col) in enumerate(pts):
        parts.append(circle(X(m), 70, 6, k=col, fill='paper', sw=2.4))
        lab.append(text(X(m), 50 - (i % 2) * 18, f'{k} £{m}', k=col, size=16, font='hand'))
    parts.append(line(X(600), 30, X(600), 110, k='green', w=2.2, dash=True))
    lab.append(text(X(600) + 6, 128, 'target £600', k='green', size=18, font='scrawl', anchor='start'))
    return svg(620, 140, rough(*parts) + ''.join(lab), 'Number line of money left over: A 300, D 340, C 560, E 580, B 590; the target is 600')

Q.append(dict(
    n=5, orig=12, answer='B', topic='Tables & rules', attempt='C',
    question=f"""<p>David is planning a holiday for {hl('himself and his wife', 'p', 1)}. He has a budget of £2,000 but wishes to
{hl('retain about £600', 'b', 2)} for spending money. Below is a table showing different holiday possibilities.</p>
{table([['Moscow', f'£300 {hl("per person", "p")}', f'£250 {hl("per person", "p")}', 'N/A', f'£120 per night {hl("for 2 only", "y")}'],
        ['Cyprus', f'£195 {hl("per person", "p")}', 'N/A', 'N/A', f'£42.50 {hl("per person per night", "p", 3)}'],
        ['Barcelona', '£215 per person', '£210 per person', 'N/A', '£370 per week per person'],
        ['Paris', f'£80 {hl("per person", "p")}', '£78 per person', 'N/A', f'£180 per night {hl("per room for 2", "y", 4)}'],
        ['Scotland', 'N/A', 'N/A', '£40 per day', f'£80 per night {hl("for 2 only", "y")}'],
        ['Rome', f'£110 {hl("per person", "p")}', '£220 per person', 'N/A', f'£120 per night {hl("for 2 only", "y")}']],
       head=['', 'Return flight', 'Ferry and train', 'Car hire and fuel', 'Hotel accommodation'])}
<p class="stem">Which one of the following holiday possibilities leaves him with as near to £600 as possible?</p>""",
    options={'A': 'Ten nights in Moscow, travelling by ferry and train.', 'B': 'Twelve nights in Cyprus.',
             'C': 'Twelve days and nights in Scotland.', 'D': 'Twelve nights in Rome travelling by plane.',
             'E': 'Seven nights in Paris travelling by plane.'},
    notes=[(1, 'p', '<b>2 people!</b> Anything “per person” must be doubled.'),
           (2, 'b', '£2000 − £600 = aim to <b>spend about £1400</b>.'),
           (3, 'p', 'Per person <b>and</b> per night: × 2 people × number of nights.'),
           (4, 'y', '“For 2” / “per room” prices are already for both of them, so don’t double them.')],
    steps=[
        f"""<p>Target: spend about <b>£1,400</b> (so £600 is left). Price each holiday, doubling every “per person” cost:</p>
{calc(f'A Moscow: 2 × 250 + 10 × 120 = 500 + 1200 = 1700 {ar()} left <b>£300</b>',
      f'B Cyprus: 2 × 195 + 12 × (2 × 42.50) = 390 + 12 × 85 = 390 + 1020 = 1410 {ar()} left <b>£590</b>',
      f'C Scotland: 12 × 40 + 12 × 80 = 480 + 960 = 1440 {ar()} left <b>£560</b>',
      f'D Rome: 2 × 110 + 12 × 120 = 220 + 1440 = 1660 {ar()} left <b>£340</b>',
      f'E Paris: 2 × 80 + 7 × 180 = 160 + 1260 = 1420 {ar()} left <b>£580</b>')}
{note('12 × 85: 10 × 85 = 850, 2 × 85 = 170, total 1020.', 'tip')}""",
        f"""<p>Which is closest to £600?</p>{_leftover_line()}
{calc(f'B is £10 away, E £20 away, C £40 away {ar()} {boxed("B")}')}""",
    ],
    answer_text='Twelve nights in Cyprus leaves £590, the closest to £600.',
    why={'A': 'Moscow costs £1,700, leaving only £300.',
         'C': 'Scotland leaves £560: close, but £40 off. (If you forget to double the Cyprus hotel, Cyprus looks like it leaves £1,100 and you end up here.)',
         'D': 'Rome costs £1,660, leaving £340.',
         'E': 'Paris leaves £580, £20 off. Careful: the Paris hotel is £180 a night, not £120.'},
    fast='Rough first: Moscow (1,700) and Rome (1,660) are way over, so they’re out. Exact for B, C, E only: 590, 560, 580. B wins.',
))

# ---------------------------------------------------------------- 6 (Q13)
def _calorie_bar():
    X = lambda c: 30 + c * 0.11
    segs = [(225, 'mealworms', 'g'), (525, 'apple', 'y'), (750, 'raisins', 'o'), (1000, 'suet', 'v'), (2500, 'sunflower seeds', 'b')]
    parts, lab, x = [], [], 0
    for amt, name, f in segs:
        parts.append(rect(X(x), 40, X(x + amt) - X(x), 34, k='ink', fill=f, sw=1.6))
        lab.append(text((X(x) + X(x + amt)) / 2, 62, amt, k='ink', size=15))
        if amt >= 500:
            lab.append(text((X(x) + X(x + amt)) / 2, 30, name, k='ink', size=14))
        x += amt
    parts.append(line(X(2500), 20, X(2500), 96, k='red', w=2.2, dash=True))
    lab += [text(X(2500), 112, '2500 so far', k='red', size=17, font='scrawl'),
            text(X(5000), 112, '5000', k='green', size=17, font='scrawl', anchor='end'),
            text(X(3750), 92, 'needs 2500 more', k='pen', size=17)]
    return svg(600, 124, rough(*parts) + ''.join(lab), 'Bar to 5000 calories: the first four foods make 2500 and sunflower seeds must make the other 2500')

Q.append(dict(
    n=6, orig=13, answer='A', topic='Proportion', attempt='A',
    question=f"""<p>The table below shows the energy values for the main foods used by volunteer wardens at a
wild bird reserve to prepare a variety of feed mixes.</p>
{table([['mealworms', '150'], ['peanuts', '560'], ['apples', '350'], ['oats', '370'], ['niger seed', '480'], ['cheese', '400'],
        [hl('sunflower seeds', 'p', 4), hl('500', 'p')], ['raisins', '300'], ['sunflower hearts', '600'], ['suet', '800']],
       head=['Food', f'Energy {hl("per 100 g", "y", 1)} (calories)'])}
<p>A trainee volunteer has been asked to prepare a sample of a special mix to provide {hl('exactly 5,000 calories', 'b', 2)}. He has weighed out the first four ingredients but cannot read the required mass
of the final ingredient because of an ink blot. This is what has been weighed out so far:</p>
<p>{hl('mealworms 150 g, apple 150 g, raisins 250 g, suet 125 g', 'g', 3)}</p>
<p class="stem">What mass of sunflower seeds must be used to successfully complete the task?</p>""",
    options={'A': '500 g', 'B': '520 g', 'C': '540 g', 'D': '560 g', 'E': '680 g'},
    notes=[(1, 'y', 'All values are per 100 g, so turn grams into “hundreds of grams” (150 g = 1.5).'),
           (2, 'b', 'Target total: 5000 calories exactly.'),
           (3, 'g', 'The four amounts already weighed.'),
           (4, 'p', 'Seeds (500), not hearts (600): don’t grab the wrong row.')],
    steps=[
        f"""<p>Calories so far: (grams ÷ 100) × calories per 100 g.</p>
{calc('mealworms: 1.5 × 150 = 225', 'apple: 1.5 × 350 = 525', 'raisins: 2.5 × 300 = 750',
      f'suet: 1.25 × 800 = 800 + 200 = 1000', '<b>total so far = 2500</b>')}""",
        f"""{_calorie_bar()}
{calc(f'5000 − 2500 = 2500 still needed', f'sunflower seeds: 500 per 100 g {ar()} 2500 ÷ 500 = 5 lots of 100 g',
      f'= {boxed("500 g")}')}""",
    ],
    answer_text='500 g of sunflower seeds.',
    why={'B': '520 g would give 2600 calories, making 5100 in total.',
         'C': '540 g would give 2700, making 5200.',
         'D': '560 g would give 2800, making 5300.',
         'E': '680 g would give 3400, making 5900.'},
    fast='225 + 525 + 750 + 1000 = 2500, so seeds give the other 2500. At 500 per 100 g that’s 500 g.',
))

# ---------------------------------------------------------------- 7 (Q14)
def _dog():
    def dog(x, y):
        return (f'<g class="k-orange" fill="none" stroke-width="2.2">'
                f'<ellipse cx="{x}" cy="{y - 14}" rx="16" ry="8"/><circle cx="{x + 18}" cy="{y - 24}" r="6"/>'
                f'<line x1="{x - 10}" y1="{y - 8}" x2="{x - 12}" y2="{y}"/><line x1="{x + 10}" y1="{y - 8}" x2="{x + 12}" y2="{y}"/>'
                f'<line x1="{x - 16}" y1="{y - 16}" x2="{x - 24}" y2="{y - 24}"/></g>')
    parts, lab = [], []
    # panel 1: going out
    parts.append(line(20, 110, 300, 110, k='muted', w=1.5))
    lab.append(stick_person(50, 108, k='pen'))
    parts.append(line(64, 70, 100, 70, k='pen', head=True, w=2.5))
    lab.append(dog(170, 108))
    parts.append(line(194, 70, 284, 70, k='orange', head=True, w=3))
    lab += [text(160, 30, '1. Freya runs out', k='ink', size=18, font='scrawl'),
            text(82, 60, 'slow', k='pen', size=14), text(240, 60, 'fast', k='orange', size=14),
            text(160, 140, 'gap grows by fast − slow', k='red', size=17), text(160, 160, '= grows SLOWLY', k='red', size=17, font='scrawl')]
    # panel 2: coming back
    parts.append(line(340, 110, 620, 110, k='muted', w=1.5))
    lab.append(stick_person(380, 108, k='pen'))
    parts.append(line(394, 70, 430, 70, k='pen', head=True, w=2.5))
    lab.append(dog(540, 108))
    parts.append(line(520, 70, 450, 70, k='orange', head=True, w=3))
    lab += [text(480, 30, '2. Freya runs back', k='ink', size=18, font='scrawl'),
            text(480, 140, 'gap shrinks by fast + slow', k='red', size=17), text(480, 160, '= shrinks QUICKLY', k='red', size=17, font='scrawl')]
    # mini graph
    gx, gy = 220, 200
    parts += [line(gx, gy + 110, gx + 220, gy + 110, k='ink', head=True), line(gx, gy + 110, gx, gy, k='ink', head=True),
              poly([(gx, gy + 110), (gx + 150, gy + 20), (gx + 200, gy + 110)], k='green', sw=3, closed=False)]
    lab += [text(gx + 60, gy + 52, 'gentle', k='green', size=16, rotate=-31),
            text(gx + 190, gy + 58, 'steep', k='green', size=16, rotate=61),
            text(gx - 6, gy + 10, 'gap', k='muted', size=14, anchor='end'), text(gx + 210, gy + 128, 'time', k='muted', size=14),
            text(gx + 260, gy + 64, 'starts at 0 and', k='ink', size=16, anchor='start'),
            text(gx + 260, gy + 84, 'ends at 0 = graph B', k='ink', size=16, anchor='start')]
    return svg(640, 330, rough(*parts) + ''.join(lab), 'Two cartoon panels of Sue and Freya with arrows, and a graph rising gently then falling steeply')

Q.append(dict(
    n=7, orig=14, answer='B', topic='Graphs & motion', attempt='B',
    question=f"""<p>Sue takes her dog Freya to the park. She throws a stick for Freya to fetch. Freya {hl('runs to collect the stick and bring it back to Sue', 'y', 1)}. {hl('While Freya is collecting the stick, Sue walks slowly towards Freya', 'p', 2)}.</p>
<p class="stem">Which one of the following graphs could correctly show the {hl('distance between Sue and Freya', 'b', 3)}?</p>
{fig(Y, 'q07_graphs', 'Five distance-time graphs A to E', 520)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'y', 'Two parts: out (gap grows), then back (gap shrinks to 0).'),
           (2, 'p', 'Sue walks towards Freya the whole time: she slows the growing and speeds up the shrinking.'),
           (3, 'b', 'The graph shows the GAP between them, starting at 0 (they start together).')],
    steps=[
        f"""<p>They start together, so the gap starts at <b>0</b>. Freya brings the stick back to Sue, so it ends at <b>0</b>.
That rules out A, C (start at 20 m) and E (never comes back down).</p>""",
        f"""<p>Now compare the two halves:</p>{_dog()}""",
        f"""<p>Up slowly, down quickly: gentle rise, steep fall {ar()} {boxed('B')}</p>""",
    ],
    answer_text='Graph B: the gap grows slowly and then shrinks quickly back to 0.',
    why={'A': 'A starts 20 m apart and ends 20 m apart, but they start and finish together.',
         'C': 'C also starts at 20 m, but they start together.',
         'D': 'D is the wrong way round: fast rise, slow fall. On the way back both are closing the gap, so it must fall faster.',
         'E': 'E never returns to 0, but Freya brings the stick back to Sue.'},
    fast='Starts and ends at 0 → B or D. Going out the gap grows at (fast − slow), coming back it shrinks at (fast + slow), so the fall is steeper: B.',
))

# ---------------------------------------------------------------- 8 (Q18)
def _lights():
    s = 7.2
    def bar(y, segs, title):
        parts, lab, x = [], [text(20, y - 12, title, k='ink', size=18, font='scrawl', anchor='start')], 20
        for secs, name, f in segs:
            w = secs * s
            parts.append(rect(x, y, w, 34, k='ink', fill=f, sw=1.6))
            lab.append(text(x + w / 2, y + 23, secs if w < 60 else f'{name} {secs}', k='ink', size=14 if w < 60 else 15))
            x += w
        return parts, lab, x
    p1, l1, e1 = bar(50, [(2, 'all red', 'p'), (25, 'main road green', 'g'), (2, 'all red', 'p')], 'Normal: side road waits 2 + 25 + 2 = 29 s')
    p2, l2, e2 = bar(150, [(2, 'all red', 'p'), (10, 'people', 'y'), (2, 'all red', 'p'), (35, 'main road green', 'g'), (2, 'all red', 'p')],
                     'Button pressed: 2 + 10 + 2 + 35 + 2 = 51 s')
    extra = [brace(20, e2, 186, 'side road waits 51 s', k='red'),
             text(20, 104, 'side road just turned red', k='muted', size=14, anchor='start')]
    return svg(440, 250, rough(*p1, *p2) + ''.join(l1 + l2) + ''.join(extra), 'Two timelines: normal wait 29 seconds; with the pedestrian phase the wait is 51 seconds')

Q.append(dict(
    n=8, orig=18, answer='D', topic='Sequences & timings', attempt='B',
    question=f"""<p>A main road crosses a side road and the junction is controlled by a set of traffic lights. The
normal sequence is for the lights to be green for {hl('25 seconds on the main road', 'g', 1)} followed by 15
seconds of green for the side road. There is also a pedestrian phase in the lights when all the
road lights are red. If a pedestrian presses a button to cross any of the roads then, {hl('after the side road lights have been green, the pedestrian lights turn green for 10 seconds', 'y', 2)}. {hl('Following a pedestrian phase, the main road green period is increased to 35 seconds', 'p', 3)} to clear the build-up.
{hl('Whenever any of the lights change there is a two-second period when all lights are red', 'p', 4)}. The
time on amber is included in the green times given above.</p>
<p class="stem">What is the {hl('longest', 'b', 5)} time traffic on the side road will have to wait for their lights to go green?</p>""",
    options={'A': '19 seconds', 'B': '29 seconds', 'C': '45 seconds', 'D': '51 seconds', 'E': '66 seconds'},
    notes=[(1, 'g', 'Normal main road green = 25 s.'),
           (2, 'y', 'The pedestrian phase slots in straight after the side road’s green.'),
           (3, 'p', 'After pedestrians, the main road gets <b>35</b> s, not 25.'),
           (4, 'p', '+2 s of all-red at <b>every</b> change. Count every change.'),
           (5, 'b', 'Longest wait means assume the pedestrian button was pressed.')],
    steps=[
        f"""<p>The side road starts waiting the moment its own light turns red. Count everything until it is green again.</p>{_lights()}""",
        f"""{calc('normal: 2 + 25 + 2 = 29 s', f'with pedestrians: 2 + 10 + 2 + 35 + 2 = {boxed("51 s")}')}
{note('Every light change adds 2 s. With pedestrians there are three changes before the side road is green again: side → people, people → main, main → side.', 'check')}""",
    ],
    answer_text='51 seconds, when the pedestrian phase is used.',
    why={'A': '19 s (2 + 15 + 2) uses the side road’s own 15 s green, but the side road is waiting for the <b>main road</b>.',
         'B': '29 s is the normal wait without pedestrians. It isn’t the longest.',
         'C': '45 s (10 + 35) forgets the three 2-second all-red gaps.',
         'E': '66 s adds on the side road’s own 15 s of green, which isn’t waiting.'},
    fast='Worst case = pedestrian phase. Write the sequence: 2, 10, 2, 35, 2 → 51.',
))
