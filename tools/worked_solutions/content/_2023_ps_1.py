from wslib import *

Y = 2023
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _drinks():
    parts, lab = [], []
    x0, ph = 40, 22.5
    parts.append(rect(x0, 40, 15 * ph, 36, k='ink', fill='y', sw=1.8))
    parts.append(rect(x0 + 15 * ph, 40, 9 * ph, 36, k='ink', fill='v', sw=1.8))
    lab += [text(x0 + 7.5 * ph, 64, 'day: 15 hours', k='ink', size=17),
            text(x0 + 19.5 * ph, 64, 'night: 9 hours', k='ink', size=17),
            text(x0, 28, 'one day = 24 hours', k='muted', size=15, anchor='start'),
            text(x0 + 7.5 * ph, 100, '15 × 18 = 270 cold', k='pen', size=17),
            text(x0 + 19.5 * ph, 100, '9 × 12 = 108 cold', k='pen', size=17)]
    lab.append(text(x0, 134, 'cold = 270 + 108 = 378 = 3 equal parts of 126', k='ink', size=17, anchor='start'))
    for i in range(3):
        parts.append(rect(x0 + 120 * i, 146, 120, 36, k='ink', fill='b', sw=1.8))
        lab.append(text(x0 + 120 * i + 60, 170, '126', k='ink', size=17))
    for i in range(2):
        parts.append(rect(x0 + 120 * i, 206, 120, 36, k='ink', fill='o', sw=1.8))
        lab.append(text(x0 + 120 * i + 60, 230, '126', k='ink', size=17))
    parts.append(rect(x0 + 240, 206, 120, 36, k='muted', sw=1.6))
    lab += [text(x0 + 300, 230, '⅓ fewer', k='red', size=16),
            text(x0 + 380, 170, 'cold 378', k='pen', size=21, anchor='start', font='scrawl'),
            text(x0 + 380, 230, 'hot 252', k='orange', size=21, anchor='start', font='scrawl'),
            text(x0, 280, '3 parts + 2 parts = 5 parts = 5 × 126 = 630 drinks', k='red', size=21, anchor='start', font='scrawl')]
    return svg(600, 296, rough(*parts) + ''.join(lab),
               'A 24-hour strip split into 15 day hours and 9 night hours, then a bar model: cold drinks are 3 parts of 126, hot drinks 2 parts, total 5 parts = 630')


Q.append(dict(
    n=1, orig=2, answer='D', topic='Rates & fractions',
    question=f"""<p>The table shows the number of cold drinks sold, {hl('per hour', 'y', 1)}, yesterday at a 24-hour service
station.</p>
{table([[hl('day time (15 hours)', 'g', 2), '18'], [hl('night time (9 hours)', 'g'), '12']], head=['', 'cold drinks'])}
<p>The service station also sells hot drinks. {hl('One-third fewer hot drinks were sold per hour than cold drinks', 'p', 3)}, regardless of the time of day.</p>
<p class="stem">How many drinks {hl('<b>in total</b>', 'b', 4)} were sold yesterday?</p>""",
    options={'A': '252', 'B': '378', 'C': '450', 'D': '630', 'E': '720'},
    notes=[(1, 'y', 'These are drinks <b>per hour</b>, not per day. Multiply by the hours.'),
           (2, 'g', 'Two different rates: 15 hours at one rate, 9 hours at the other. Do them separately.'),
           (3, 'p', '“One-third fewer” means take a third <b>away</b>. Hot = ⅔ of cold, not ⅓ of cold.'),
           (4, 'b', 'Total = cold + hot, for the whole 24 hours.')],
    steps=[
        f"""<p>Cold drinks over the whole day: rate × hours, for each part of the day.</p>
{calc('day: 15 × 18 = 270', 'night: 9 × 12 = 108', f'cold total = 270 + 108 = <b>378</b>')}""",
        f"""<p>Hot drinks: one-third fewer every hour, so the whole day is one-third fewer too. Split the cold total into thirds:</p>
{calc(f'378 ÷ 3 = 126 {ar()} one third', f'hot = 378 − 126 = <b>252</b> (two thirds)')}
{note('Same answer the long way: hot per hour is 12 by day and 8 by night, so 15 × 12 + 9 × 8 = 180 + 72 = 252.', 'check')}""",
        f"""<p>Picture it as parts: cold is 3 parts, hot is 2 parts.</p>
{_drinks()}
{calc(f'378 + 252 = {boxed("630")}')}""",
    ],
    answer_text='630 drinks: 378 cold + 252 hot.',
    why={'A': '252 is only the <b>hot</b> drinks. The question wants cold + hot.',
         'B': '378 is only the <b>cold</b> drinks.',
         'C': '450 is the <b>daytime</b> total only (270 cold + 180 hot). It leaves out the 9 night hours.',
         'E': '720 uses 24 hours for both rates (18 × 24 + 12 × 24) instead of 15 hours and 9 hours.'},
    fast='Cold: 15 × 18 + 9 × 12 = 378 = 3 thirds. Hot is 2 thirds. Total = 5 thirds = 5 × 126 = 630.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _pin():
    X = lambda d: 50 + 56 * d
    parts, lab = [], []
    parts.append(line(X(0) - 20, 110, X(9) + 24, 110, k='ink', w=2))
    chosen = {2: 'b', 9: 'b', 4: 'o', 7: 'o'}
    for d in range(10):
        f = chosen.get(d, 'paper')
        parts.append(circle(X(d), 110, 17, k='ink' if d in chosen else 'muted', fill=f, sw=2 if d in chosen else 1.5))
        lab.append(text(X(d), 117, d, k='ink' if d in chosen else 'muted', size=20, font='print'))
    parts.append(path(f'M{X(2)} 90 Q{(X(2) + X(9)) / 2} 0 {X(9)} 90', k='pen', sw=2.4))
    parts.append(path(f'M{X(4)} 130 Q{(X(4) + X(7)) / 2} 190 {X(7)} 130', k='orange', sw=2.4))
    lab += [text((X(2) + X(9)) / 2, 34, '2 + 9 = 11', k='pen', size=19),
            text((X(4) + X(7)) / 2, 182, '4 + 7 = 11', k='orange', size=19),
            text(X(0) - 6, 158, 'chosen: 2, 4, 7, 9', k='green', size=17, anchor='start', font='scrawl'),
            text(X(0) - 6, 178, 'no two are neighbours', k='green', size=17, anchor='start', font='scrawl')]
    # the PIN
    bx = 110
    for i, (dgt, f) in enumerate(((7, 'o'), (4, 'o'), (9, 'b'), (2, 'b'))):
        parts.append(rect(bx + 62 * i, 214, 52, 52, k='ink', fill=f, sw=2, rx=6))
        lab.append(text(bx + 62 * i + 26, 249, dgt, k='ink', size=28, font='print'))
    lab += [text(bx - 12, 248, 'PIN', k='ink', size=20, anchor='end', font='scrawl'),
            text(bx + 26, 290, 'odd', k='orange', size=16),
            text(bx + 62 * 3 + 26, 290, 'smallest', k='pen', size=16),
            text(bx + 270, 236, 'first pair 7 + 4 = 11', k='orange', size=17, anchor='start'),
            text(bx + 270, 260, 'last pair 9 + 2 = 11', k='pen', size=17, anchor='start')]
    return svg(620, 300, rough(*parts) + ''.join(lab),
               'Digits 0 to 9 on a line: 2 and 9 joined (sum 11), 4 and 7 joined (sum 11), none next to each other; the PIN 7 4 9 2')


Q.append(dict(
    n=2, orig=6, answer='D', topic='Logic & digits',
    question=f"""<p>The 4-digit PIN of my bank card has been set so that {hl('the first two digits and the last two digits both separately add up to 11', 'y', 1)}.</p>
<p>{hl('The first digit is odd', 'g', 2)} and {hl('the last digit in the PIN is the smallest of the four', 'g', 3)}. {hl('All four digits are different', 'y', 4)}, and {hl('no two digits in the PIN are numerically consecutive with each other', 'p', 5)}. So, for
example, if the PIN contains the digit ‘6’ then it cannot contain either the digits ‘5’ or ‘7’.</p>
<p class="stem">What is the {hl('<b>first</b> digit', 'b', 6)} of my PIN?</p>""",
    options={'A': '1', 'B': '3', 'C': '5', 'D': '7', 'E': '9'},
    notes=[(1, 'y', 'Two pairs, each adding to 11.'),
           (2, 'g', 'First digit: 1, 3, 5, 7 or 9.'),
           (3, 'g', 'The last digit is the smallest of all four.'),
           (4, 'y', 'No repeats.'),
           (5, 'p', 'The big filter! No two digits next to each other on the number line, <b>anywhere</b> in the PIN, not just side by side.'),
           (6, 'b', 'Only the first digit is asked for.')],
    steps=[
        f"""<p>List the digit pairs that add to 11:</p>
{calc('2 + 9, 3 + 8, 4 + 7, 5 + 6', f'5 + 6 {cross()} they are consecutive {ar()} only <b>29, 38, 47</b> left')}""",
        f"""<p>The PIN uses two of these pairs. Check each mix for neighbours:</p>
{calc(f'29 with 38: 2 and 3 are neighbours {cross()}', f'38 with 47: 3 and 4 are neighbours {cross()}', f'29 with 47: digits 2, 4, 7, 9, no neighbours {tick()}')}
{_pin()}""",
        f"""<p>Now place them. The smallest digit (2) is last, so the last pair is <b>9, 2</b>.
The first pair is 4 and 7, and the first digit is odd, so it starts with 7.</p>
{calc(f'PIN = 7 4 9 2 {ar()} first digit = {boxed("7")}')}""",
    ],
    answer_text='7 (the PIN is 7492).',
    why={'A': '1 would need a 10 to make 11. Impossible.',
         'B': '3 pairs with 8, but the other pair (29 or 47) always brings a neighbour: 2 or 4 next to 3, 7 or 9 next to 8.',
         'C': '5 pairs with 6, and 5 and 6 are consecutive.',
         'E': '9 pairs with 2, but 2 is the smallest digit so it must go last. That makes 9, 2 the <b>last</b> pair, not the first.'},
    fast='Pairs to 11 without neighbours: 29 and 47 only. Smallest (2) last gives __92, then the odd one of 4 and 7 goes first: 7.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _exercise():
    parts, lab = [], []
    x0, bw = 40, 104
    blocks = [('40', 'y'), ('60', 'b'), ('60', 'b'), ('70', 'g'), ('70', 'g')]
    for i, (v, f) in enumerate(blocks):
        parts.append(rect(x0 + bw * i, 70, bw, 46, k='ink', fill=f, sw=1.8))
        lab.append(text(x0 + bw * i + bw / 2, 100, v, k='ink', size=22))
        lab.append(text(x0 + bw * i + bw / 2, 140, '10 min', k='muted', size=14))
    parts.append(brace(x0 + 4, x0 + bw - 4, 62, '', k='orange', down=False))
    parts.append(brace(x0 + bw + 4, x0 + 3 * bw - 4, 62, '', k='pen', down=False))
    parts.append(brace(x0 + 3 * bw + 4, x0 + 5 * bw - 4, 62, '', k='green', down=False))
    lab += [text(x0 + bw / 2, 30, 'fast walk', k='orange', size=17),
            text(x0 + 2 * bw, 30, 'slow cycle: 180 ÷ 3 = 60', k='pen', size=17),
            text(x0 + 4 * bw, 30, 'slow swim: 210 ÷ 3 = 70', k='green', size=17),
            text(x0 + bw / 2, 166, '120 ÷ 3', k='orange', size=16),
            text(x0, 196, 'each table value is for 30 min, so one 10-minute block = value ÷ 3', k='ink', size=16, anchor='start'),
            text(x0, 230, '40 + 60 + 60 + 70 + 70 = 300 calories', k='red', size=22, anchor='start', font='scrawl')]
    return svg(600, 244, rough(*parts) + ''.join(lab),
               'Fifty minutes split into five 10-minute blocks: walking 40, cycling 60 and 60, swimming 70 and 70, total 300')


Q.append(dict(
    n=3, orig=7, answer='C', topic='Tables & rates',
    question=f"""<p>Jarold {hl('weighs 60 kg', 'g', 1)}. He decides to start a daily exercise regime of {hl('fast walking for 10 minutes, slow cycling for 20 minutes and slow swimming for 20 minutes', 'g', 2)}.</p>
<p>The table below shows the rate at which calories are used up, {hl('per 30 minutes', 'y', 3)} of exercise, by
people of different weights.</p>
{table([['slow cycling', '160', '170', hl('180', 'g'), '190'],
        ['fast cycling', '190', '210', '230', '240'],
        ['slow swimming', '190', '200', hl('210', 'g'), '220'],
        ['fast swimming', '220', '250', '280', '295'],
        ['slow walking', '50', '55', '60', '75'],
        [hl('fast walking', 'p', 4), '100', '110', hl('120', 'g'), '150']],
       head=['', '50 kg', '55 kg', '60 kg', '65 kg'])}
<p class="stem">How many calories will Jarold use during exercise on the first day of this regime?</p>""",
    options={'A': '170 calories', 'B': '190 calories', 'C': '300 calories', 'D': '340 calories', 'E': '510 calories'},
    notes=[(1, 'g', 'Use the 60 kg column only.'),
           (2, 'g', 'Three activities, and none of them lasts 30 minutes!'),
           (3, 'y', 'Every number in the table is for <b>30 minutes</b>. 10 min = ⅓ of it, 20 min = ⅔ of it.'),
           (4, 'p', 'Pick the right rows: fast walking, but <b>slow</b> cycling and <b>slow</b> swimming.')],
    steps=[
        f"""<p>Read the 60 kg column (all per 30 minutes):</p>
{calc('fast walking 120', 'slow cycling 180', 'slow swimming 210')}""",
        f"""<p>Work in 10-minute blocks: divide each value by 3. Walking is 1 block, the others are 2 blocks each.</p>
{_exercise()}
{calc('walking: 120 ÷ 3 = 40', 'cycling: 180 ÷ 3 × 2 = 120', 'swimming: 210 ÷ 3 × 2 = 140', f'total = 40 + 120 + 140 = {boxed("300 calories")}')}""",
    ],
    answer_text='300 calories: 40 walking + 120 cycling + 140 swimming.',
    why={'A': '170 gives every activity only 10 minutes: (120 + 180 + 210) ÷ 3.',
         'B': '190 is just one number from the table (for example slow cycling at 65 kg), not the total of the three activities.',
         'D': '340 gives every activity 20 minutes: (120 + 180 + 210) × ⅔. The walking is only 10 minutes.',
         'E': '510 adds the table values straight (120 + 180 + 210), as if each activity lasted 30 minutes.'},
    fast='Per 10 minutes at 60 kg: walk 40, cycle 60, swim 70. Total = 40 + 2 × 60 + 2 × 70 = 300.',
))


# ---------------------------------------------------------------- 4 (Q8)
_SEG = {
    'a': lambda x, y, w, h: (x + 7, y, x + w - 7, y),
    'b': lambda x, y, w, h: (x + w, y + 7, x + w, y + h / 2 - 7),
    'c': lambda x, y, w, h: (x + w, y + h / 2 + 7, x + w, y + h - 7),
    'd': lambda x, y, w, h: (x + 7, y + h, x + w - 7, y + h),
    'e': lambda x, y, w, h: (x, y + h / 2 + 7, x, y + h - 7),
    'f': lambda x, y, w, h: (x, y + 7, x, y + h / 2 - 7),
    'g': lambda x, y, w, h: (x + 7, y + h / 2, x + w - 7, y + h / 2),
}


def _digit(x, y, real, shown, w=58, h=108):
    out = []
    for s, f in _SEG.items():
        x1, y1, x2, y2 = f(x, y, w, h)
        if s in shown and s in real:
            out.append(line(x1, y1, x2, y2, k='ink', w=8))
        elif s in shown:
            out.append(line(x1, y1, x2, y2, k='green', w=8))
        elif s in real:
            out.append(line(x1, y1, x2, y2, k='red', w=3, dash=True))
        else:
            out.append(line(x1, y1, x2, y2, k='muted', w=1, dash=True))
    return out


def _clock():
    parts, lab = [], []
    cases = [('15:29', '9', 'abcdfg', '5'), ('15:30', '0', 'abcdef', '6'), ('15:31', '1', 'bc', '“4”'), ('15:32', '2', 'abdeg', '“E”')]
    for i, (t, d, real, look) in enumerate(cases):
        x = 70 + 150 * i
        shown = (set(real) - {'b'}) | {'f', 'g'}
        parts += _digit(x, 66, set(real), shown)
        lab += [text(x + 29, 26, f'real {t}', k='ink', size=17),
                text(x + 29, 48, f'should be {d}', k='pen', size=17),
                text(x + 29, 206, f'shows {look}', k='ink', size=17)]
    # legend
    parts += [line(60, 238, 96, 238, k='red', w=3, dash=True), line(60, 268, 96, 268, k='green', w=8)]
    lab += [text(106, 244, 'top-right should light but is dark in all four: 1 element OFF', k='red', size=17, anchor='start'),
            text(106, 274, 'middle and top-left are lit in all four: 2 elements ON', k='green', size=17, anchor='start')]
    return svg(640, 290, rough(*parts) + ''.join(lab),
               'Four seven-segment digits 9, 0, 1, 2 as the clock shows them: the top-right segment is always dark and the middle and top-left segments are always lit')


Q.append(dict(
    n=4, orig=8, answer='C', topic='Digital displays',
    question=f"""<p>As I waited for a train yesterday I was puzzled when I noticed the digital clock on the platform
{hl('change from', 'g', 1)}</p>
{fig(Y, 'ps_q04_clock1', 'A display showing 15:25 (the last digit looks like a 5)', 150)}
<p>to</p>
{fig(Y, 'ps_q04_clock2', 'A display showing 15:36 (the last digit looks like a 6)', 150)}
<p>but then {hl('a minute later', 'g')} it changed to</p>
{fig(Y, 'ps_q04_clock3', 'A display showing 15:3 followed by a broken digit like a 4 with no top-right bar', 150)}
<p>And then, {hl('after another minute', 'g')}, it changed to</p>
{fig(Y, 'ps_q04_clock4', 'A display showing 15:3 followed by a digit shaped like a capital E', 150)}
<p>I realised that {hl('the last digit was not displaying properly', 'y', 2)}.</p>
<p class="stem">What was wrong with the last digit?</p>""",
    options={'A': 'One element was permanently on and one element was permanently off.',
             'B': 'One element was permanently on and two elements were permanently off.',
             'C': 'Two elements were permanently on and one element was permanently off.',
             'D': 'Two elements were permanently on and two elements were permanently off.',
             'E': 'Three elements were permanently on and one element was permanently off.'},
    notes=[(1, 'g', 'Each change is one minute. The tens digit goes 2 → 3, so the first change must be 15:29 → 15:30.'),
           (2, 'y', 'Only the last digit is broken. The real last digits are 9, 0, 1, 2.')],
    steps=[
        f"""<p>Find the real times first. The minutes go from 2_ to 3_ in one minute, so it must be:</p>
{calc(f'15:29 {ar()} 15:30 {ar()} 15:31 {ar()} 15:32', f'real last digits: <b>9, 0, 1, 2</b>')}""",
        f"""<p>Draw each real digit and compare it with what the clock showed. Red dashes = should be lit but dark. Green = lit but shouldn’t be.</p>
{_clock()}""",
        f"""<p>Spot what never changes:</p>
{calc(f'top-right: dark every time, even for 9, 0, 1, 2 which all need it {ar()} 1 off',
      f'middle: lit on 0 and 1, which don’t use it {ar()} on', f'top-left: lit on 1 and 2, which don’t use it {ar()} on',
      f'2 on, 1 off {ar()} {boxed("C")}')}
{note('Quick test: which bars are lit in all four pictures? Only top-left and middle. Which bar is never lit? Only top-right.', 'tip')}""",
    ],
    answer_text='Two elements stuck on (top-left and middle) and one stuck off (top-right).',
    why={'A': 'A spots the dead top-right bar but only one of the stuck bars (for example just the middle, from 0 showing as 6). The top-left is stuck on too: look at the 1.',
         'B': 'Only one bar is never lit (top-right). The bottom-left lights up in the 6 and the E, so it works.',
         'D': 'Same problem as B: you need two bars that never light, but only the top-right never lights.',
         'E': 'Only two bars are lit in all four displays. The top and bottom bars are dark in the third one, so they aren’t stuck on.'},
    fast='Real digits 9, 0, 1, 2. Lit in all four displays: top-left and middle (2 on). Never lit: top-right (1 off).',
))


# ---------------------------------------------------------------- 5 (Q12)
def _walk():
    X = lambda km: 110 + 46 * km
    parts, lab = [], []
    rows = [(90, '10:00', 3, 10), (210, '11:00', 6, 6), (330, '12:00', 9, 2)]
    for y, t, d, a in rows:
        parts.append(line(X(0), y, X(10), y, k='ink', w=2))
        for km in range(11):
            parts.append(line(X(km), y - 5, X(km), y + 5, k='ink', w=1.4))
        lab.append(text(14, y - 34, t, k='ink', size=20, anchor='start', font='scrawl'))
        lab.append(text(X(0) - 10, y + 5, 'bottom', k='muted', size=14, anchor='end'))
        lab.append(text(X(10) + 10, y + 5, 'top', k='muted', size=14, anchor='start'))
        off = 10 if d == a else 0
        lab.append(stick_person(X(d) - off, y - 8, k='pen', s=0.9))
        lab.append(stick_person(X(a) + off, y - 8, k='orange', s=0.9))
        lab.append(text(X(d) - off - 12, y - 30, 'D', k='pen', size=17, anchor='end'))
        lab.append(text(X(a) + off + 12, y - 30, 'A', k='orange', size=17, anchor='start'))
    lab.append(text(X(10), 22, 'each tick = 1 km', k='muted', size=14, anchor='end'))
    parts.append(brace(X(3), X(10), 100, '', k='red'))
    lab.append(text(X(6.5), 138, '7 km apart, closing at 3 + 4 = 7 km/h', k='red', size=17))
    lab.append(text(X(6) + 44, 186, 'they pass at 6 km', k='green', size=19, anchor='start', font='scrawl'))
    parts.append(brace(X(2), X(9), 340, '', k='red'))
    lab.append(text(X(5.5), 378, 'moving apart at 3 + 4 = 7 km/h: 7 km apart', k='red', size=17))
    parts += [arrow(X(9) + 14, 304, X(9) + 44, 304, k='pen'), arrow(X(2) - 14, 304, X(2) - 44, 304, k='orange')]
    return svg(640, 392, rough(*parts) + ''.join(lab),
               'Three snapshots of the 10 km path at 10:00, 11:00 and 12:00: they meet at 6 km at 11:00 and are 7 km apart at 12:00')


Q.append(dict(
    n=5, orig=12, answer='E', topic='Speed & meeting',
    question=f"""<p>David set out at 09:00 on a {hl('10 km path', 'g', 1)} up a hill, walking at {hl('3 km/hour', 'g')}. Andrew set out from the
top of the hill {hl('one hour later', 'p', 2)}, walking the same path in the opposite direction, at {hl('4 km/hour', 'g')}.</p>
<p class="stem">How far apart will David and Andrew be {hl('1 hour after they pass each other', 'b', 3)}?</p>""",
    options={'A': '1 km', 'B': '3 km', 'C': '4 km', 'D': '6 km', 'E': '7 km'},
    notes=[(1, 'g', 'The path ends after 10 km. Check nobody reaches the end too soon.'),
           (2, 'p', 'A distraction for this question! The head start only changes <b>when</b> they meet, not how fast they separate.'),
           (3, 'b', 'After passing they walk <b>away</b> from each other.')],
    steps=[
        f"""<p>Once they have passed, they walk in opposite directions, so the gap grows by both speeds added together:</p>
{calc(f'3 + 4 = 7 km every hour {ar()} 1 hour later: 7 km')}""",
        f"""<p>Check neither walker runs out of path in that hour:</p>
{calc('10:00: David is 3 km up, Andrew at the top (10 km), 7 km apart',
      f'gap closes at 7 km/h {ar()} they meet at 11:00, 6 km up',
      '12:00: David at 6 + 3 = 9 km, Andrew at 6 − 4 = 2 km',
      f'9 − 2 = {boxed("7 km")}')}
{_walk()}""",
    ],
    answer_text='7 km: after passing they separate at 3 + 4 = 7 km/h.',
    why={'A': '1 km uses 4 − 3, as if they walked the same way. They walk in opposite directions.',
         'B': '3 km is only how far David walks in the hour.',
         'C': '4 km is only how far Andrew walks in the hour.',
         'D': '6 km is where they meet (6 km up the path), not the gap an hour later.'},
    fast='Moving apart in opposite directions: 3 + 4 = 7 km in an hour. Quick check: David at 9 km, Andrew at 2 km, both still on the path.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _ruler():
    s, x0 = 11, 220
    X = lambda cm: x0 + s * cm
    rows = [('plastic 450 cm³, $12', 30), ('plastic 450 cm³, $13', 20), ('wood 500 cm³, $15', 20),
            ('wood 550 cm³, $18', 30), ('wood 600 cm³, $22', 20)]
    parts, lab = [], []
    for i, (name, ln) in enumerate(rows):
        y = 40 + 38 * i
        bad = ln > 25
        parts.append(rect(X(0), y, s * ln, 24, k='ink', fill='p' if bad else 'b', sw=1.6))
        lab.append(text(x0 - 10, y + 18, name, k='muted' if bad else 'ink', size=16, anchor='end'))
        lab.append(text(X(ln) + 10, y + 19, f'{ln} cm', k='red' if bad else 'ink', size=16, anchor='start'))
        if bad:
            parts.append(line(x0 - 150, y + 12, x0 - 6, y + 12, k='red', w=2))
    parts.append(line(X(25), 26, X(25), 236, k='red', w=2.4, dash=True))
    lab.append(text(X(25), 18, '25 cm limit', k='red', size=17, font='scrawl'))
    lab.append(text(x0, 258, 'longest side of each box', k='muted', size=14, anchor='start'))
    return svg(620, 268, rough(*parts) + ''.join(lab),
               'Bars for the five boxes by length: the two 30 cm boxes cross the 25 cm limit and are crossed out')


Q.append(dict(
    n=6, orig=13, answer='E', topic='Tables & constraints',
    question=f"""<p>Juan needs to buy some boxes to store his collection of badges. The types of box that are
available from his local shop are shown in the table below.</p>
{table([['plastic', hl('30', 'p'), '8', '2', '450', '12'],
        ['plastic', '20', '6', '4', '450', '13'],
        ['wood', '20', '10', '3', '500', '15'],
        ['wood', hl('30', 'p'), '5', '4', '550', '18'],
        ['wood', '20', '10', '4', '600', '22']],
       head=['box material', 'length (cm)', 'width (cm)', 'depth (cm)', hl('capacity (cm³)', 'y', 1), 'price ($)'])}
<p>Juan wants {hl('two different boxes', 'p', 2)} with a {hl('combined capacity of at least 1000 cm³', 'y', 3)}. He also wants to
make sure that {hl('neither box has any side longer than 25 cm', 'y', 4)}.</p>
<p class="stem">What is the {hl('<b>least</b>', 'b', 5)} that Juan can pay for the boxes?</p>""",
    options={'A': '$28', 'B': '$30', 'C': '$31', 'D': '$34', 'E': '$35'},
    notes=[(1, 'y', 'Use this column for “capacity”. Don’t multiply the sides: the walls take up room, so capacity is less than length × width × depth.'),
           (2, 'p', 'Two <b>different</b> boxes: no buying two of the same.'),
           (3, 'y', 'Add the two capacities: 1000 or more.'),
           (4, 'y', 'Any box with a 30 cm side is out.'),
           (5, 'b', 'Cheapest pair that passes every test.')],
    steps=[
        f"""<p>First knock out boxes with a side over 25 cm:</p>
{_ruler()}
{calc('left: plastic 450 ($13), wood 500 ($15), wood 600 ($22)')}""",
        f"""<p>Now try the pairs (different boxes, at least 1000 cm³):</p>
{calc(f'450 + 500 = 950 {cross()} too small', f'450 + 600 = 1050 {tick()} $13 + $22 = <b>$35</b>', f'500 + 600 = 1100 {tick()} $15 + $22 = $37')}
{calc(f'least = {boxed("$35")}')}
{note('Two of the $15 wood boxes would make exactly 1000 cm³ for $30, but he wants two <b>different</b> boxes.', 'trap')}""",
    ],
    answer_text='$35: the plastic 20 cm box ($13) and the 600 cm³ wood box ($22).',
    why={'A': '$28 pairs the $13 and $15 boxes because 20 × 6 × 4 = 480 and 20 × 10 × 3 = 600 make 1080. But the real capacities are 450 + 500 = 950: too small.',
         'B': '$30 is two of the $15 wood box. They have to be two <b>different</b> boxes.',
         'C': '$31 ($13 + $18) uses the 550 cm³ wood box, which is 30 cm long.',
         'D': '$34 ($12 + $22) uses the $12 plastic box, which is 30 cm long.'},
    fast='Cross out the two 30 cm boxes. Of 450, 500 and 600, only pairs with the 600 reach 1000. Cheapest: the 450 and 600 boxes, $13 + $22 = $35.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _salt():
    parts, lab = [], []
    x0 = 110
    rows = [('Store 1', ['o'] * 12, 30, '£8.40'),
            ('Store 2', ['b', 'y'] * 6, 30, '£9.00'),
            ('Store 3', ['b', 'b', 'g'] * 4, 30, '£8.00'),
            ('Store 4', ['b'] * 9, 40, '£9.00')]
    for i, (name, fills, pitch, total) in enumerate(rows):
        y = 30 + 50 * i
        lab.append(text(x0 - 14, y + 24, name, k='ink', size=18, anchor='end'))
        for j, f in enumerate(fills):
            parts.append(rect(x0 + pitch * j + 2, y + 2, pitch - 4, 30, k='ink', fill=f, sw=1.4, rx=4))
        same = total == '£9.00'
        lab.append(text(x0 + 372, y + 24, total, k='red' if same else 'ink', size=21, anchor='start', font='scrawl' if same else 'hand'))
    parts += [arrow(x0 + 478, 134, x0 + 440, 100, k='red', bend=0.15), arrow(x0 + 478, 166, x0 + 440, 196, k='red', bend=-0.15)]
    lab.append(text(x0 + 462, 157, 'same!', k='red', size=22, anchor='start', font='scrawl'))
    ly = 246
    for j, (f, t) in enumerate((('b', '£1 (full price)'), ('y', '50p (half price)'), ('g', 'free'), ('o', '70p (30% off)'))):
        parts.append(rect(20 + 150 * j, ly - 14, 18, 18, k='ink', fill=f, sw=1.2, rx=3))
        lab.append(text(44 + 150 * j, ly, t, k='ink', size=14, anchor='start'))
    lab.append(text(x0, 276, 'Store 4: 9 bags of 1⅓ kg cover the same 12 kg, so pay for 9 bags', k='muted', size=15, anchor='start'))
    return svg(640, 290, rough(*parts) + ''.join(lab),
               'Twelve kilograms of salt as bags for each store: 12 bags at 70p, six full plus six half price, eight paid plus four free, or nine bigger bags; totals 8.40, 9, 8 and 9 pounds')


Q.append(dict(
    n=7, orig=14, answer='D', topic='Percentages & offers',
    question=f"""<p>Dan wants to buy {hl('12 kg', 'g', 1)} of rock salt to help keep his driveway clear of ice during the winter. He
has looked online and found four different offers on the {hl('recommended retail price of a 1 kg bag', 'y', 2)}.</p>
<p><b>1</b>&nbsp; Store 1 has {hl('30% off', 'g', 3)} the price of a 1 kg bag.</p>
<p><b>2</b>&nbsp; Store 2 has {hl('buy one and get one at half price', 'g', 4)}.</p>
<p><b>3</b>&nbsp; Store 3 has {hl('buy two and get one free', 'g', 5)}.</p>
<p><b>4</b>&nbsp; Store 4 has {hl('one third extra for same price', 'p', 6)} as a 1 kg bag.</p>
<p class="stem">Which pair of offers works out to be the {hl('same price per kg', 'b', 7)}?</p>""",
    options={'A': '1 and 2', 'B': '1 and 4', 'C': '2 and 3', 'D': '2 and 4', 'E': '3 and 4'},
    notes=[(1, 'g', 'Handy: 12 divides by 2, 3 and 4, so price exactly 12 kg at each store.'),
           (2, 'y', 'No price is given. Make one up: say a 1 kg bag costs £1.'),
           (3, 'g', 'Each bag 70p.'),
           (4, 'g', 'Every 2 bags cost £1 + 50p = £1.50.'),
           (5, 'g', 'Every 3 bags cost £2.'),
           (6, 'p', 'Not 30% off! You get 1⅓ kg for £1, so a third <b>more salt</b>, not a third off the price.'),
           (7, 'b', 'Compare like with like: the cost of the same 12 kg at each store.')],
    steps=[
        f"""<p>Say a 1 kg bag is £1 and price Dan’s 12 kg at every store:</p>
{calc('Store 1: 12 bags × 70p = £8.40',
      'Store 2: 6 pairs × £1.50 = £9.00',
      'Store 3: 4 lots of 3 bags × £2 = £8.00',
      'Store 4: 12 ÷ 1⅓ = 9 big bags × £1 = £9.00')}
{note('12 ÷ 1⅓: each big bag holds 4 thirds of a kg, and 12 kg = 36 thirds, so 36 ÷ 4 = 9 bags.', 'tip')}""",
        f"""<p>See it as bags:</p>
{_salt()}
{calc(f'Stores 2 and 4 both cost £9.00 {ar()} {boxed("2 and 4")}')}""",
    ],
    answer_text='Stores 2 and 4: both work out at 75p per kg (when a bag is £1).',
    why={'A': 'Store 1 is 70p per kg but Store 2 is 75p per kg.',
         'B': 'Treats “one third extra” like “30% off”. A third extra salt for the same money only saves a quarter (75p per kg), not 30%.',
         'C': 'Store 3 is cheaper: you pay for 2 bags out of every 3, so about 67p per kg.',
         'E': 'Mixes up “one free with every two” (pay ⅔) with “one third extra” (pay ¾). Store 3 costs £8 for 12 kg; Store 4 costs £9.'},
    fast='Bag = £1. Per kg: 1 → 70p, 2 → 75p, 3 → 67p, 4 → £1 ÷ 1⅓ = 75p. Same: 2 and 4.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _scores():
    X = lambda s: 150 + 48 * (s - 12)
    parts, lab = [], []
    players = [('Sonny', 13, 'orange'), ('Bobby', 14, 'ink'), ('Vandy', 15, 'ink'), ('Georgina', 16, 'ink'), ('Riaz', 17, 'green')]
    for i, (name, s, k) in enumerate(players):
        y = 54 + 40 * i
        f = {'orange': 'o', 'green': 'g'}.get(k, 'none')
        parts.append(line(X(s + 1), y, X(s + 3), y, k=k if k != 'ink' else 'muted', w=10))
        parts.append(circle(X(s), y, 7, k='ink', fill='paper', sw=2))
        lab.append(text(130, y + 6, f'{name} {s}', k=k, size=17, anchor='end'))
    parts.append(line(X(12), 262, X(21), 262, k='ink', w=2))
    for s in range(12, 22):
        parts.append(line(X(s), 256, X(s), 268, k='ink', w=1.4))
        lab.append(text(X(s), 290, s, k='muted', size=15))
    parts.append(line(X(16), 30, X(16), 250, k='orange', w=2, dash=True))
    parts.append(line(X(18), 30, X(18), 250, k='green', w=2, dash=True))
    lab += [text(X(12), 22, 'o = score after 4 rounds;  bar = after adding 1, 2 or 3', k='muted', size=14, anchor='start'),
            text(X(16) - 6, 246, 'Sonny ≤ 16', k='orange', size=16, anchor='end'),
            text(X(18) + 6, 246, 'Riaz ≥ 18', k='green', size=16, anchor='start'),
            text(X(17), 316, 'top − bottom is always at least 18 − 16 = 2', k='red', size=19, font='scrawl')]
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'Score line from 12 to 21: Riaz can only finish on 18 to 20 and Sonny only on 14 to 16, so the gap is at least 2')


Q.append(dict(
    n=8, orig=18, answer='A', topic='Logic & scores',
    question=f"""<p>Five friends play a word game called Wordsmith. The objective is to score as many as points
as possible, using the letters of a randomly chosen starting word to create new words. {hl('Each letter used in a word scores one point', 'y', 1)}, and the player with the most points after five rounds is
the winner.</p>
<p>The word chosen for this particular game was ‘RAINBOW’. In the first four rounds, the words
selected by the five players were as follows:</p>
{table([['BRAIN', 'BROWN', 'ROBIN', 'BRAWN', 'WORN'], ['WARN', 'BARON', 'BORN', 'IRON', 'BOAR'],
        ['BRAN', 'RAIN', 'WAR', 'BROW', 'BAN'], ['NOW', 'WON', 'AN', 'NO', 'OR']],
       head=['Georgina', 'Riaz', 'Bobby', 'Vandy', 'Sonny'])}
<p>The words given in the final round by the five players were: {hl("‘ROW’, ‘BAR’, ‘AIR’, ‘ON’ and ‘I’", 'g', 2)}
{hl('(not in order)', 'p', 3)}.</p>
<p class="stem">Which one of the following is {hl('<b>not</b> a possible difference', 'b', 4)} between the final scores of the players
with the most and least points?</p>""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'y', 'Score = number of letters. BRAIN = 5 points.'),
           (2, 'g', 'Final round adds 3, 3, 3, 2 and 1 points: one each.'),
           (3, 'p', 'We don’t know who said which word, so try different matches.'),
           (4, 'b', 'Find the gap (top score − bottom score) that can never happen.')],
    steps=[
        f"""<p>Totals after four rounds (count the letters):</p>
{calc('Georgina 5 + 4 + 4 + 3 = 16', 'Riaz 5 + 5 + 4 + 3 = 17', 'Bobby 5 + 4 + 3 + 2 = 14',
      'Vandy 5 + 4 + 4 + 2 = 15', 'Sonny 4 + 4 + 3 + 2 = 13')}""",
        f"""<p>Riaz gets at least 1 more, so he ends on <b>at least 18</b>. Sonny gets at most 3 more, so he ends on <b>at most 16</b>.</p>
{_scores()}
{calc(f'top ≥ 18 and bottom ≤ 16 {ar()} the gap is at least 2', f'a gap of 1 is impossible {ar()} {boxed("1")}')}""",
        f"""<p>Check the others really can happen (final-round points in brackets):</p>
{calc('gap 2: Sonny 13 (+3) = 16, Bobby (+3) 17, Vandy (+3) 18, Georgina (+2) 18, Riaz (+1) 18',
      'gap 3: Sonny (+3) 16, Bobby (+3) 17, Vandy (+3) 18, Georgina (+1) 17, Riaz (+2) 19',
      'gap 4: Sonny (+3) 16, Bobby (+2) 16, Vandy (+1) 16, Georgina (+3) 19, Riaz (+3) 20',
      'gap 5: Sonny (+2) 15, Bobby (+3) 17, Vandy (+1) 16, Georgina (+3) 19, Riaz (+3) 20')}""",
    ],
    answer_text='1: Riaz always ends on 18 or more and Sonny on 16 or less, so the gap is at least 2.',
    why={'B': '2 can happen: give Sonny, Bobby and Vandy the 3-letter words, Georgina ON and Riaz I. Scores 16, 17, 18, 18, 18.',
         'C': '3 can happen: Sonny, Bobby, Vandy +3, Georgina +1, Riaz +2. Scores 16 to 19.',
         'D': '4 can happen: Georgina and Riaz +3, Sonny +3, Bobby +2, Vandy +1. Scores 16 to 20.',
         'E': '5 can happen: Riaz 20 at the top and Sonny +2 = 15 at the bottom.'},
    fast='Riaz starts on 17, Sonny on 13. Riaz ends ≥ 18, Sonny ends ≤ 16, so the gap can never be 1.',
))
