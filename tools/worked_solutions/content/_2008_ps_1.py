import math
from wslib import *

Y = 2008
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _fares():
    k, x0 = 4, 40
    parts = [rect(x0, 40, 50 * k, 44, k='ink', fill='b', sw=1.8),
             rect(x0 + 50 * k, 40, 35 * k, 44, k='ink', fill='o', sw=1.8),
             rect(x0 + 85 * k, 40, 35 * k, 44, k='ink', fill='o', sw=1.8)]
    lab = [text(x0 + 25 * k, 68, 'adult 50p', k='ink', size=17),
           text(x0 + 67.5 * k, 68, 'child 35p', k='ink', size=17),
           text(x0 + 102.5 * k, 68, 'child 35p', k='ink', size=17)]
    extra = brace(x0, x0 + 120 * k, 88, '1 adult + 2 children = 120p', k='red')
    X = lambda p: 40 + p * 9
    parts.append(rect(X(25), 186, X(50) - X(25), 28, k='green', fill='g', sw=1.6))
    parts.append(line(X(0), 200, X(60), 200, k='ink', w=2))
    for p in range(0, 61, 10):
        parts.append(line(X(p), 194, X(p), 206, k='ink', w=1.5))
        lab.append(text(X(p), 226, p, k='muted', size=14))
    parts += [line(X(25), 182, X(25), 218, k='red', w=2.6), line(X(50), 182, X(50), 218, k='red', w=2.6),
              circle(X(35), 200, 7, k='orange', fill='o', sw=2.4)]
    lab += [text(X(25), 176, 'half adult = 25', k='red', size=15),
            text(X(50), 176, 'adult = 50', k='red', size=15),
            text(X(37.5), 154, 'the child fare must land in the green zone', k='green', size=16),
            text(X(35), 250, 'child 35 ✓', k='orange', size=18, font='scrawl'),
            text(X(62), 205, 'pence', k='muted', size=14, anchor='start')]
    return svg(620, 262, rough(*parts) + ''.join(lab) + extra,
               'Bar of 50p plus two 35p bars making 120p; number line with the child fare 35 between 25 and 50')

Q.append(dict(
    n=1, orig=2, answer='C', topic='Testing the options',
    question=f"""<p>A child's bus fare is {hl('cheaper than the adult fare', 'y', 1)} but is {hl('more than half the adult fare', 'y', 2)}. The
total cost of a single journey for {hl('an adult and two children is £1.20', 'g', 3)}. {hl('Adult fares are all multiples of 10 p', 'p', 4)}.</p>
<p class="stem">What is the {hl('adult fare', 'b', 5)}?</p>""",
    options={'A': '30 p', 'B': '40 p', 'C': '50 p', 'D': '60 p', 'E': '70 p'},
    notes=[(1, 'y', 'Child &lt; adult.'),
           (2, 'y', 'Child &gt; half the adult. <b>Strictly</b> more, so exactly half is not allowed.'),
           (3, 'g', 'adult + child + child = 120p.'),
           (4, 'p', 'Only the <b>adult</b> fare has to be a round 10p. The child fare can be any amount.'),
           (5, 'b', 'Five adult fares to test: perfect for trying each one.')],
    steps=[
        f"""<p>Write the total as one line, then the child fare drops out of any adult fare:</p>
{calc('adult + 2 × child = 120p', f'child = (120 − adult) ÷ 2')}""",
        f"""<p>Test each option against both rules (cheaper than adult, more than half of adult):</p>
{calc(f'A: adult 30 {ar()} child (120 − 30) ÷ 2 = 45: dearer than the adult ' + cross(),
      f'B: adult 40 {ar()} child 40: the same, not cheaper ' + cross(),
      f'C: adult 50 {ar()} child 35: between 25 and 50 ' + tick(),
      f'D: adult 60 {ar()} child 30: exactly half, not more than half ' + cross(),
      f'E: adult 70 {ar()} child 25: less than half (35) ' + cross())}""",
        f"""{_fares()}
{calc(f'adult fare = {boxed("50 p")}')}""",
    ],
    answer_text='50p: the child fare is then 35p, which is cheaper than 50p and more than 25p.',
    why={'A': '30p makes the child fare 45p, which is <b>more</b> than the adult fare.',
         'B': '40p makes the child fare 40p too: the same as the adult, not cheaper.',
         'D': '60p makes the child fare 30p, which is exactly half. The rule says <b>more</b> than half.',
         'E': '70p makes the child fare 25p, which is less than half of 70p (35p).'},
    fast='Child = (120 − adult) ÷ 2. Only 50 gives a child fare (35) strictly between half the adult (25) and the adult (50).',
))


# ---------------------------------------------------------------- 2 (Q6)
def _wheels():
    parts = [circle(90, 80, 45, k='orange', sw=2.6), circle(250, 88, 37, k='pen', sw=2.6),
             line(90, 80, 170, 58, k='ink', w=2.4), line(170, 58, 250, 88, k='ink', w=2.4),
             line(150, 40, 190, 40, k='ink', w=3), line(170, 40, 170, 58, k='ink', w=2.4),
             circle(90, 125, 5, k='red', fill='p'), circle(250, 125, 5, k='red', fill='p')]
    lab = [text(310, 62, 'rear wheel: 2.5 m per turn', k='orange', size=18, anchor='start'),
           text(310, 92, 'front wheel: 2 m per turn', k='pen', size=18, anchor='start'),
           text(310, 124, 'red dots = valves, both at the bottom', k='red', size=15, anchor='start')]
    X = lambda d: 40 + d * 46
    parts.append(line(X(0), 200, X(12.3), 200, k='ink', w=2, head=True))
    for d in (2, 4, 6, 8, 10, 12):
        parts.append(circle(X(d), 200, 6, k='pen', fill='b', sw=2))
        lab.append(text(X(d), 182, d, k='pen', size=16))
    for d in (2.5, 5, 7.5, 10):
        parts.append(rect(X(d) - 6, 206, 12, 12, k='orange', fill='o', sw=2))
        lab.append(text(X(d), 238, d, k='orange', size=16))
    parts.append(circle(X(10), 205, 20, k='green', sw=3))
    lab += [text(X(0), 182, 'front', k='pen', size=15, anchor='start'),
            text(X(0), 238, 'rear', k='orange', size=15, anchor='start'),
            text(X(10), 268, 'both valves at the bottom: 10 m', k='green', size=18, font='scrawl'),
            text(X(12.3) + 4, 205, 'm', k='muted', size=15, anchor='start')]
    return svg(640, 280, rough(*parts) + ''.join(lab),
               'A motorbike with valves at the bottom; a number line marking every 2 m for the front wheel and every 2.5 m for the rear, meeting first at 10 m')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Multiples (LCM)',
    question=f"""<p>Steven has a customised motorcycle that he is very proud of and shows regularly in
competitions. It is very important to him that his presentation is perfect and he likes to
stop in front of the judges with {hl('both his tyre valves in the same position', 'y', 1)}. The front tyre is
smaller than the rear to aid its handling. The {hl('circumference of the front wheel is 2m and the circumference of the rear wheel is 2.5m', 'g', 2)}.</p>
<p>Steven starts with both valves in the same position at the bottom of each wheel.</p>
<p class="stem">How far must he drive before the valves {hl('line up again at the bottom of each wheel', 'b', 3)}?</p>""",
    options={'A': '2.0 m', 'B': '2.5 m', 'C': '4.5 m', 'D': '10.0 m', 'E': '12.5 m'},
    notes=[(1, 'y', 'A valve is back at the bottom after every <b>whole turn</b> of its wheel.'),
           (2, 'g', 'One turn moves the bike one circumference: 2 m for the front, 2.5 m for the rear.'),
           (3, 'b', 'Both at once: the first distance that is a whole number of turns for <b>both</b> wheels (the lowest common multiple).')],
    steps=[
        f"""<p>List where each valve is back at the bottom:</p>
{calc(f'front: 2, 4, 6, 8, <b>10</b>, 12 … m', f'rear: 2.5, 5, 7.5, <b>10</b>, 12.5 … m')}""",
        f"""{_wheels()}""",
        f"""{calc(f'first match = 10 m {ar()} front 10 ÷ 2 = 5 turns, rear 10 ÷ 2.5 = 4 turns', f'answer = {boxed("10.0 m")}')}
{note('Hate decimals? Count in half-metres: 2 m = 4 halves and 2.5 m = 5 halves. LCM of 4 and 5 is 20 halves = 10 m.', 'tip')}""",
    ],
    answer_text='10 m: the front wheel turns 5 times and the rear wheel 4 times.',
    why={'A': '2 m is one turn of the front wheel only. The rear valve has gone 0.8 of a turn, so it isn’t at the bottom.',
         'B': '2.5 m is one turn of the rear wheel only. The front has done 1.25 turns.',
         'C': '4.5 m just adds the two circumferences (2 + 2.5). That isn’t a whole number of turns for either wheel.',
         'E': '12.5 m is 5 rear turns, but the front would be on 6.25 turns. (And 10 m comes first anyway.)'},
    fast='Multiples of 2.5: 2.5, 5, 7.5, 10. The first one that is also a multiple of 2 is 10 m.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _pin():
    parts, lab = [], []
    for i, ch in enumerate('ABCDEFGHIJ'):
        x = 40 + i * 36
        lab.append(text(x, 28, ch, k='ink', size=16, font='print'))
        lab.append(text(x, 50, (i + 1) % 10, k='pen', size=16))
    lab.append(text(40 + 10 * 36, 40, 'the key', k='muted', size=15, anchor='start'))
    xs = [40 + i * 70 for i in range(5)]
    for i, (x, ch) in enumerate(zip(xs, 'DFGCB')):
        parts.append(rect(x, 76, 56, 44, k='ink', fill='g' if i == 4 else 'b', sw=1.8))
        lab.append(text(x + 28, 106, ch, k='ink', size=22, font='print'))
    lab.append(text(xs[4] + 66, 104, '← last letter B = bicycle lock', k='green', size=17, anchor='start'))
    digits = [4, 6, 7, 3]
    for i, d in enumerate(digits):
        lab.append(text(xs[i] + 28, 150, d, k='pen', size=24, font='scrawl'))
        parts.append(rect(xs[3 - i], 212, 56, 40, k='ink', fill='y', sw=1.8))
        parts.append(arrow(xs[i] + 28, 158, xs[3 - i] + 28, 208, k='muted', w=1.6))
    for i, d in enumerate(reversed(digits)):
        lab.append(text(xs[i] + 28, 240, d, k='ink', size=22, font='print'))
    lab += [text(xs[4] + 10, 150, 'decode D F G C', k='pen', size=16, anchor='start'),
            text(xs[4] + 10, 196, 'then turn it back', k='red', size=16, anchor='start'),
            text(xs[4] + 10, 216, 'the right way round', k='red', size=16, anchor='start'),
            text(xs[4] + 10, 250, '= 3764', k='red', size=26, font='scrawl', anchor='start')]
    return svg(640, 268, rough(*parts) + ''.join(lab),
               'Key A to J equals 1 to 0; the line D F G C B ends in B, decodes to 4 6 7 3 and reverses to 3 7 6 4')

Q.append(dict(
    n=3, orig=7, answer='E', topic='Codes',
    question=f"""<p>I have so many four digit code numbers to remember that I cannot keep them all in my
head. The banks say you should not write down your Personal Identification Numbers
(PINs) for cash and credit cards and keep them in a wallet with the cards. So I can find
out what the numbers are, I have devised a code which should be complicated enough to
confuse any thief who steals my wallet. I code all the numbers using {hl('1=A, 2=B up to 9=I, 0=J', 'y', 1)}. Then I {hl('write the coded numbers down backwards', 'p', 2)} so 1234 is written DCBA. Finally
{hl('at the end of each coded number I add an extra letter', 'y', 3)} between A and J to say what that
particular code is of: C is for credit card; F is for phone card; {hl('B is for bicycle lock combination', 'g', 4)}; E is for my Eastern Bank card and D is for my Denton Building Society card.</p>
<p>My list looks as follows:</p>
{table([['A', 'D', 'G', 'E', 'F'], ['C', 'J', 'D', 'B', 'E'], ['B', 'G', 'F', 'A', 'C'], ['G', 'J', 'A', 'C', 'D'], ['D', 'F', 'G', 'C', 'B']])}
<p class="stem">What is my {hl('bicycle lock combination', 'b', 5)}?</p>""",
    options={'A': '4673', 'B': '5741', 'C': '7613', 'D': '4356', 'E': '3764'},
    notes=[(1, 'y', 'Letter = position in the alphabet, with J standing for 0.'),
           (2, 'p', 'Backwards! After decoding, turn the digits round.'),
           (3, 'y', 'The type letter is the <b>5th</b> (last) letter, not the first.'),
           (4, 'g', 'So we want the line that <b>ends</b> in B.'),
           (5, 'b', 'One line only: the bike lock.')],
    steps=[
        f"""<p>Find the bike lock by its <b>last</b> letter:</p>
{calc('A D G E | <b>F</b> = phone card', 'C J D B | <b>E</b> = Eastern Bank', 'B G F A | <b>C</b> = credit card',
      'G J A C | <b>D</b> = Denton', f'D F G C | <b>B</b> = bicycle lock {tick()}')}""",
        f"""<p>Decode D F G C, then undo the backwards writing:</p>{_pin()}
{calc(f'D F G C {ar()} 4 6 7 3 {ar()} reversed {ar()} {boxed("3764")}')}""",
        f"""{note('Check with their own example: 1234 is written DCBA. Decoding DCBA gives 4321, and reversing gives 1234 back. Same method.', 'check')}""",
    ],
    answer_text='3764: the line ending in B is DFGC, which decodes to 4673, and reversed that is 3764.',
    why={'A': '4673 decodes D F G C but forgets to turn it back round.',
         'B': '5741 is the <b>phone card</b> line (A D G E, ending in F), decoded and reversed.',
         'C': '7613 takes the line that <b>starts</b> with B (B G F A C) and reads G F A C forwards. The type letter goes at the end, not the start.',
         'D': '4356 would need the letters D C E F (or F E C D) in the list, and no line has them.'},
    fast='Line ending in B: DFGC. Decode 4673, reverse: 3764.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _slot():
    front = [(40, 210), (40, 90), (100, 90), (100, 130), (140, 130), (140, 90), (200, 90), (200, 210)]
    parts = [poly([(200, 90), (250, 55), (250, 175), (200, 210)], k='ink', fill='paper', sw=2),
             poly([(100, 130), (140, 130), (190, 95), (150, 95)], k='ink', fill='o', sw=2),
             poly([(100, 90), (150, 55), (150, 95), (100, 130)], k='ink', fill='paper', sw=2),
             poly([(40, 90), (100, 90), (150, 55), (90, 55)], k='ink', fill='y', sw=2),
             poly([(140, 90), (200, 90), (250, 55), (190, 55)], k='ink', fill='y', sw=2),
             poly(front, k='ink', fill='b', sw=2.2)]
    lab = [text(145, 240, 'side view A needs a slot', k='ink', size=16),
           text(145, 260, 'right through, front to back', k='ink', size=16)]
    # plan of the slotted block
    parts += [rect(330, 60, 120, 120, k='red', sw=2.4),
              line(375, 60, 375, 180, k='red', w=2.2), line(405, 60, 405, 180, k='red', w=2.2),
              rect(500, 60, 120, 120, k='green', sw=2.4), rect(545, 105, 30, 30, k='green', sw=2.2)]
    lab += [text(390, 44, 'its view from above', k='red', size=16),
            text(390, 205, 'a strip right across', k='red', size=16),
            text(560, 44, 'the real view', k='green', size=16),
            text(560, 205, 'a small closed square', k='green', size=16),
            text(475, 132, '≠', k='red', size=40),
            text(475, 250, 'so A can’t be a side view', k='red', size=20, font='scrawl')]
    return svg(660, 272, rough(*parts) + ''.join(lab),
               'A block with a slot cut right through it; from above that shows a strip across the top, not the small square in the real top view')

Q.append(dict(
    n=4, orig=8, answer='A', topic='3D views',
    question=f"""<p>The drawing shows a sculpture as {hl('seen from above', 'y', 1)}.</p>
{fig(Y, 'ps_q04_plan', 'Top view: a large square with a small square in the middle', 110)}
<p class="stem">Which of these could {hl('<b>not</b>', 'b', 2)} be a view from one of the sides?</p>
{fig(Y, 'ps_q04_opts', 'Five side views: A a block with a notch cut in the top middle; B a block with a small block on top; C a square with a small square inside; D a block with a small block on top and a small square inside; E a plain square', 380)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'From above you only see a small square inside a big one. It could be a block sticking up, a hole going down, or a shallow dip. We don’t know which!'),
           (2, 'b', 'Four views can be explained by <b>some</b> sculpture. Find the one that can’t.')],
    steps=[
        f"""<p>For each option, invent a sculpture that would give it <b>and</b> still look like the top view:</p>
<ul><li><b>B</b>: a small cube sitting in the middle of the top. From above you see its square. {tick()}</li>
<li><b>D</b>: the same, plus a square tunnel through the side. {tick()}</li>
<li><b>C</b>: a square shaft down from the top and a square tunnel through the sides. {tick()}</li>
<li><b>E</b>: the small square is a shallow dip in the top, hidden from the side. {tick()}</li></ul>""",
        f"""<p><b>A</b> has a notch in its outline. You can only see sky through the top of a side view if the gap goes
<b>all the way through</b>, front to back. That is a slot across the top:</p>{_slot()}""",
        f"""<p>From above, a slot would show as two lines right across the top, not a small closed square. So the one that is
not a side view is {boxed('A')}.</p>
{note('A side view shows the outline of the whole sculpture. A hole in the middle of the top is hidden behind the front wall, so it can’t make a dent in the outline.', 'check')}""",
    ],
    answer_text='View A: its notch would need a slot right across the top, which the top view does not show.',
    why={'B': 'B works: a small block standing on top of the middle shows as the inner square from above.',
         'C': 'C works: a square tunnel through the sides (with a shaft down from the top) shows as a square inside the side view.',
         'D': 'D works: a block on top and a tunnel through the side.',
         'E': 'E works: if the inner square is a shallow dip in the top, the side just looks like a plain block.'},
    fast='A notch in a side outline means a slot right through, which would show from above as a strip across the top. The top view has a small square instead, so A.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _waiters():
    s, x0 = 0.55, 130
    ot, n30, n40 = 250 * s, 450 * s, 600 * s
    parts = [rect(x0, 40, ot, 44, k='ink', fill='o', sw=1.8), rect(x0 + ot, 40, n30, 44, k='ink', fill='b', sw=1.8),
             rect(x0, 120, ot, 44, k='ink', fill='o', sw=1.8), rect(x0 + ot, 120, n40, 44, k='ink', fill='b', sw=1.8),
             line(x0 + ot + n30, 28, x0 + ot + n30, 176, k='red', w=2.2, dash=True)]
    lab = [text(x0 + ot / 2, 68, '10 overtime', k='ink', size=16), text(x0 + ot + n30 / 2, 68, '30 normal', k='ink', size=16),
           text(x0 + ot / 2, 148, '10 overtime', k='ink', size=16), text(x0 + ot + n40 / 2, 148, '40 normal', k='ink', size=16),
           text(x0 - 12, 58, 'Pierre', k='ink', size=17, anchor='end'), text(x0 - 12, 80, '€700', k='pen', size=17, anchor='end'),
           text(x0 - 12, 138, '2 × Marc', k='ink', size=17, anchor='end'), text(x0 - 12, 160, '€850', k='pen', size=17, anchor='end')]
    extra = brace(x0 + ot + n30, x0 + ot + n40, 170, '10 normal = €150', k='red')
    return svg(640, 224, rough(*parts) + ''.join(lab) + extra,
               'Bar model: Pierre is 10 overtime plus 30 normal making 700; double Marc is 10 overtime plus 40 normal making 850; the extra 10 normal sessions are worth 150')

Q.append(dict(
    n=5, orig=12, answer='C', topic='Two unknowns',
    question=f"""<p>Pierre and Marc are waiters. In one particular month, {hl('Pierre worked 30 sessions at the normal rate and 10 sessions at the overtime rate', 'g', 1)}. {hl('Marc worked 20 sessions at the normal rate and 5 sessions at the overtime rate', 'g', 2)}. At the end of this month, {hl('Pierre earned 700 euros. Marc earned 425 euros', 'g', 3)}.</p>
<p class="stem">What is the {hl('overtime rate', 'b', 4)} per session?</p>""",
    options={'A': '35 euros', 'B': '30 euros', 'C': '25 euros', 'D': '20 euros', 'E': '15 euros'},
    notes=[(1, 'g', 'Pierre: 30 normal + 10 overtime.'),
           (2, 'g', 'Marc: 20 normal + 5 overtime. Exactly half of Pierre’s overtime: handy!'),
           (3, 'g', 'Their pay: €700 and €425.'),
           (4, 'b', 'We want the <b>overtime</b> rate, not the normal one.')],
    steps=[
        f"""<p>Write both months as a line each (N = normal rate, V = overtime rate):</p>
{calc('Pierre: 30N + 10V = 700', 'Marc: 20N + 5V = 425')}""",
        f"""<p>Double Marc, so both have 10 overtime sessions. Then the only difference is 10 normal sessions:</p>
{calc('2 × Marc: 40N + 10V = 850')}{_waiters()}
{calc(f'850 − 700 = 150 {ar()} 10N = 150 {ar()} N = €15')}""",
        f"""<p>Put N = 15 back into Pierre:</p>
{calc(f'30 × 15 = 450', f'700 − 450 = 250 for 10 overtime sessions {ar()} V = {boxed("€25")}')}
{note('Marc: 20 × 15 + 5 × 25 = 300 + 125 = 425. It fits.', 'check')}""",
    ],
    answer_text='€25 per overtime session (the normal rate is €15).',
    why={'A': 'With €35 overtime, Marc’s normal rate would be (425 − 175) ÷ 20 = €12.50, and then Pierre would earn €725, not €700.',
         'B': 'With €30 overtime, Marc’s normal rate would be €13.75 and Pierre would earn €712.50.',
         'D': 'With €20 overtime, Marc’s normal rate would be €16.25 and Pierre would earn €687.50.',
         'E': '€15 is the <b>normal</b> rate, not the overtime rate.'},
    fast='Double Marc: 40N + 10V = 850. Take away Pierre: 10N = 150, so N = 15. Then 10V = 700 − 450 = 250, so V = 25.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _sector(cx, cy, r, a0, a1, fill):
    P = lambda a: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
    x0, y0 = P(a0)
    x1, y1 = P(a1)
    big = 1 if a1 - a0 > 180 else 0
    return path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 0 {x1:.1f} {y1:.1f} Z', k='ink', fill=fill, sw=1.8)


def _pie():
    cx, cy, r = 170, 150, 120
    parts = [_sector(cx, cy, r, -20, 180, 'b'), _sector(cx, cy, r, 180, 250, 'b'),
             _sector(cx, cy, r, 250, 280, 'o'), _sector(cx, cy, r, 280, 340, 'o')]
    u = lambda a: (math.cos(math.radians(a)), -math.sin(math.radians(a)))
    (ax, ay), (bx, by) = u(250), u(340)
    d = 22
    parts.append(path(f'M{cx + d * ax:.1f} {cy + d * ay:.1f} L{cx + d * (ax + bx):.1f} {cy + d * (ay + by):.1f} '
                      f'L{cx + d * bx:.1f} {cy + d * by:.1f}', k='red', sw=2.6))
    parts.append(arrow(258, 292, 196, 258, k='orange', bend=0.2))
    lab = [text(180, 82, 'home wins', k='ink', size=17), text(108, 196, 'away', k='ink', size=16),
           text(108, 214, 'wins', k='ink', size=16),
           text(262, 304, 'both draw slices', k='orange', size=16, anchor='start'),
           text(340, 60, 'each match = 360° ÷ 24 = 15°', k='ink', size=17, anchor='start'),
           text(340, 110, 'draws together make a', k='orange', size=18, anchor='start'),
           text(340, 134, 'right angle = 90° = ¼', k='orange', size=18, anchor='start'),
           text(340, 160, '¼ of 24 = 6 draws', k='orange', size=18, anchor='start'),
           text(340, 214, 'wins = 24 − 6 = 18', k='green', size=26, font='scrawl', anchor='start')]
    return svg(640, 318, rough(*parts) + ''.join(lab),
               'Pie chart redrawn: the two draw slices together form a right angle, a quarter of the pie, so 6 draws and 18 wins')

Q.append(dict(
    n=6, orig=13, answer='E', topic='Pie charts',
    question=f"""<p>The chart below shows the distribution of results this season for the Arlsea Strikers
hockey team. They have {hl('played 24 matches', 'g', 1)} to date and {hl('lost none', 'y', 2)}.</p>
{fig(Y, 'ps_q06_pie', 'Pie chart: home wins just over half; away wins; home draws a thin slice; away draws a bigger slice', 300)}
<p class="stem">How many matches have they {hl('won', 'b', 3)}?</p>""",
    options={'A': '4', 'B': '6', 'C': '14', 'D': '16', 'E': '18'},
    notes=[(1, 'g', 'The whole pie = 24 matches.'),
           (2, 'y', 'No losses, so every match is a win or a draw. Wins = 24 − draws.'),
           (3, 'b', 'All wins: home <b>and</b> away.')],
    steps=[
        f"""<p>No numbers on the chart, so look for an easy angle. The two <b>draw</b> slices sit side by side,
and their outside edges make a perfect right angle:</p>{_pie()}""",
        f"""{calc(f'draws = 90° = ¼ of the pie {ar()} ¼ × 24 = 6', f'wins = 24 − 6 = {boxed("18")}')}
{note('Same thing from the other side: the wins cover the other three-quarters, ¾ × 24 = 18.', 'check')}""",
    ],
    answer_text='18 wins: the draws are a quarter of the pie (6 matches), so the other three-quarters are wins.',
    why={'A': '4 is about the size of one draw slice (the away draws), not the wins.',
         'B': '6 is the number of <b>draws</b>.',
         'C': '14 is roughly the home wins on their own. It leaves out the away wins.',
         'D': '16 would mean 8 draws, a third of the pie. The draws make a right angle, which is a quarter.'},
    fast='The two draw slices form a right angle: ¼ of 24 = 6 draws, so 24 − 6 = 18 wins.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _net():
    c, ox, oy = 70, 30, 24
    cell = {'T': (1, 0), 'L': (0, 1), 'X': (1, 1), 'R': (2, 1), 'F': (3, 1), 'S': (1, 2)}
    fills = {'T': 'b', 'S': 'b', 'L': 'o', 'R': 'o', 'X': 'g', 'F': 'g'}
    parts, marks, lab = [], [], []
    for f, (i, j) in cell.items():
        parts.append(rect(ox + i * c, oy + j * c, c, c, k='ink', fill=fills[f], sw=1.8))
    X0 = lambda f: ox + cell[f][0] * c
    Y0 = lambda f: oy + cell[f][1] * c
    g = dict(k='muted', w=12)
    marks += [line(X0('T') + 3, Y0('T') + 35, X0('T') + 67, Y0('T') + 35, **g),
              line(X0('S') + 35, Y0('S') + 3, X0('S') + 35, Y0('S') + 67, **g),
              line(X0('X') + 35, Y0('X') + 3, X0('X') + 35, Y0('X') + 67, **g),
              line(X0('X') + 3, Y0('X') + 35, X0('X') + 67, Y0('X') + 35, **g),
              line(X0('L') + 7, Y0('L') + 63, X0('L') + 63, Y0('L') + 7, **g),
              line(X0('R') + 7, Y0('R') + 7, X0('R') + 63, Y0('R') + 63, **g),
              line(X0('F'), Y0('F') + 70, X0('F') + 70, Y0('F'), k='ink', w=2)]
    dots = [(X0('X'), Y0('X')), (X0('R'), Y0('R')), (X0('L'), Y0('L') + 70), (X0('F'), Y0('F') + 70)]
    for x, y in dots:
        marks.append(circle(x, y, 8, k='red', sw=2.6))
    lab += [text(X0('T') + 35, Y0('T') + 22, 'stripe', k='ink', size=14),
            text(X0('S') + 35, Y0('S') + 62, 'stripe', k='ink', size=14),
            text(ox + 4 * c - 35, oy + 2 * c - 6, 'line', k='ink', size=14),
            text(66, 56, 'cross +', k='red', size=15), text(66, 74, 'top stripe', k='red', size=15),
            text(260, 56, 'cross + top stripe', k='red', size=15),
            text(96, 196, 'line +', k='red', size=15, anchor='end'), text(96, 214, 'bottom stripe', k='red', size=15, anchor='end'),
            text(258, 196, 'line + bottom', k='red', size=15), text(258, 214, 'stripe', k='red', size=15)]
    lab += [text(340, 40, 'Same colour = opposite faces,', k='ink', size=17, anchor='start'),
            text(340, 62, 'never seen at the same time:', k='ink', size=17, anchor='start'),
            text(352, 92, 'stripe ↔ stripe', k='pen', size=17, anchor='start'),
            text(352, 116, 'band ↔ band', k='orange', size=17, anchor='start'),
            text(352, 140, 'cross ↔ line', k='green', size=17, anchor='start'),
            text(340, 180, 'Red rings: each band runs from the', k='red', size=16, anchor='start'),
            text(340, 200, 'corner by the cross and top stripe', k='red', size=16, anchor='start'),
            text(340, 220, 'to the corner by the line and', k='red', size=16, anchor='start'),
            text(340, 240, 'the bottom stripe.', k='red', size=16, anchor='start')]
    return svg(640, 256, rough(*parts) + ''.join(marks) + ''.join(lab),
               'The net with opposite faces in matching colours: the two stripes, the two bands, and the cross with the thin line; the band ends are ringed')


def _iso_cube(cx, cy, s):
    C = (cx, cy)
    Lv, B, Rv = (cx - 0.866 * s, cy - 0.5 * s), (cx, cy - s), (cx + 0.866 * s, cy - 0.5 * s)
    Lb, Cb, Rb = (Lv[0], Lv[1] + s), (cx, cy + s), (Rv[0], Rv[1] + s)
    left = lambda a, b: (Lb[0] + a * (Cb[0] - Lb[0]), Lb[1] + a * (Cb[1] - Lb[1]) - b * s)
    right = lambda a, b: (Cb[0] + a * (Rb[0] - Cb[0]), Cb[1] + a * (Rb[1] - Cb[1]) - b * s)
    top = lambda p, q: (Lv[0] + p * (C[0] - Lv[0]) + q * (B[0] - Lv[0]), Lv[1] + p * (C[1] - Lv[1]) + q * (B[1] - Lv[1]))
    faces = [poly([Lv, C, Rv, B], k='ink', fill='paper', sw=2), poly([Lv, C, Cb, Lb], k='ink', fill='paper', sw=2),
             poly([C, Rv, Rb, Cb], k='ink', fill='paper', sw=2)]
    return faces, left, right, top


def _seg(f, a, b, **kw):
    (x1, y1), (x2, y2) = f(*a), f(*b)
    return line(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), **kw)


def _de_cubes():
    g = dict(k='muted', w=12)
    fD, lD, rD, tD = _iso_cube(140, 120, 80)
    fE, lE, rE, tE = _iso_cube(460, 120, 80)
    parts = fD + [_seg(tD, (0.5, 0.08), (0.5, 0.92), **g), _seg(lD, (0, 0), (1, 1), k='ink', w=2),
                  _seg(rD, (0.92, 0.92), (0.08, 0.08), **g),
                  _seg(rD, (0.06, 0.94), (0.94, 0.06), k='green', w=3, dash=True)]
    parts += fE + [_seg(tE, (0.5, 0.08), (0.5, 0.92), **g), _seg(lE, (0.5, 0.06), (0.5, 0.94), **g),
                   _seg(lE, (0.06, 0.5), (0.94, 0.5), **g), _seg(rE, (0.92, 0.92), (0.08, 0.08), **g)]
    parts += [circle(140, 120, 11, k='red', sw=3), circle(460, 120, 11, k='red', sw=3)]
    lab = [text(30, 30, 'D', k='ink', size=24, font='print', weight='700'),
           text(350, 30, 'E', k='ink', size=24, font='print', weight='700'),
           text(140, 232, 'middle corner: line, bottom', k='ink', size=16),
           text(140, 252, 'stripe and a band meet', k='ink', size=16),
           text(140, 278, 'band must run into it ✗', k='red', size=19, font='scrawl'),
           text(250, 150, 'should be', k='green', size=15, anchor='start'),
           text(250, 168, 'this way', k='green', size=15, anchor='start'),
           text(460, 232, 'middle corner: cross, bottom', k='ink', size=16),
           text(460, 252, 'stripe and a band meet', k='ink', size=16),
           text(460, 278, 'band keeps away from it ✓', k='green', size=19, font='scrawl')]
    return svg(620, 292, rough(*parts) + ''.join(lab),
               'Cubes D and E with the middle corner ringed: in D the band misses the corner it should run into; in E the band correctly avoids it')

Q.append(dict(
    n=7, orig=14, answer='E', topic='Nets & cubes',
    question=f"""<p>The cut out below was {hl('folded together to make a cube', 'y', 1)}.</p>
{fig(Y, 'ps_q07_net', 'Cross-shaped net: a cross in the middle; a stripe above and a stripe below; diagonal bands left and right; a square with a thin diagonal line on the far right', 260)}
<p class="stem">Which of the following cubes {hl('was formed from this cut-out', 'b', 2)}?</p>
{fig(Y, 'ps_q07_cubes', 'Five cubes A to E, each showing three faces', 460)}""",
    options={'A': 'cube A', 'B': 'cube B', 'C': 'cube C', 'D': 'cube D', 'E': 'cube E'},
    notes=[(1, 'y', 'In a row of faces, two faces with one face between them end up <b>opposite</b>. You can never see opposite faces together.'),
           (2, 'b', 'Only one picture is possible. Knock the others out one rule at a time.')],
    steps=[
        f"""<p>Name the faces and pair up the opposites (one face between them in a straight line):</p>{_net()}""",
        f"""<p><b>Test 1: opposite faces can’t both be seen.</b></p>
{calc('A: stripe on top <b>and</b> a stripe on the front ' + cross(),
      'B: stripe on top <b>and</b> a stripe on the right ' + cross(),
      'C: the thin line on top <b>and</b> the cross ' + cross(),
      f'D: stripe, line, band {ar()} allowed', f'E: stripe, cross, band {ar()} allowed')}""",
        f"""<p><b>Test 2: D or E? Use a corner.</b> In both, the top stripe runs straight <b>into</b> the front-left face.
The stripe below the cross does that (it carries on the cross’s bar, and the line face is opposite the cross),
so the top face is the <b>bottom</b> stripe. Now look at the corner in the middle of each picture:</p>{_de_cubes()}
<ul><li>D: the middle corner joins the line, the bottom stripe and a band. Every band runs <b>into</b> that corner (red rings above), but D’s band goes the other way {cross()}</li>
<li>E: the middle corner joins the cross, the bottom stripe and a band. A band never touches that corner, and E’s doesn’t. The cross’s bar also runs neatly into the stripe {tick()}</li></ul>
{calc(f'answer = {boxed("E")}')}""",
    ],
    answer_text='Cube E: cross at the front, the bottom stripe on top and a band on the right, all joined the way the net folds.',
    why={'A': 'A shows two plain stripes side by side, but the two stripe faces are opposite each other.',
         'B': 'B also shows both stripe faces at once (top and right), and they are opposite.',
         'C': 'C shows the thin line and the cross together, but they are opposite faces.',
         'D': 'D’s faces are allowed, but the band is on the wrong diagonal: it should run into the middle corner where it meets the line and the bottom stripe.'},
    fast='Opposites: stripe/stripe, band/band, cross/line. That kills A, B, C. In D the band misses the corner it shares with the line, so E.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _car():
    s, x0 = 0.8, 170
    parts = [rect(x0, 40, 550 * s, 44, k='ink', fill='b', sw=1.8),
             rect(x0, 120, 440 * s, 44, k='ink', fill='g', sw=1.8),
             rect(x0 + 440 * s, 120, 110 * s, 44, k='red', fill='p', sw=2)]
    lab = [text(x0 + 275 * s, 68, '500 + 10% = 550 Bols', k='ink', size=17),
           text(x0 + 220 * s, 148, '80% of 550 = 440', k='ink', size=17),
           text(x0 + 495 * s, 148, '110', k='red', size=18),
           text(x0 - 12, 58, 'new car', k='ink', size=17, anchor='end'), text(x0 - 12, 78, 'costs', k='ink', size=17, anchor='end'),
           text(x0 - 12, 138, 'old car', k='ink', size=17, anchor='end'), text(x0 - 12, 158, 'fetches', k='ink', size=17, anchor='end')]
    extra = brace(x0 + 440 * s, x0 + 550 * s, 172, 'he pays 110', k='red')
    return svg(640, 222, rough(*parts) + ''.join(lab) + extra,
               'Bars: new car costs 550; the old car fetches 440; the gap of 110 is what he pays')

Q.append(dict(
    n=8, orig=18, answer='E', topic='Percentages',
    question=f"""<p>{hl('Inflation in Bolandia has been a steady 10% per year', 'y', 1)} for many years. Evitan, a Bolandian
citizen, bought his car {hl('one year ago for 500 Bols', 'g', 2)}. He now wants to trade in his car for an
identical model. He can expect to receive {hl('80% of the current new value of his existing car', 'p', 3)}. {hl('The price of new models has increased in line with inflation', 'y', 4)}.</p>
<p class="stem">How many {hl('extra', 'b', 5)} Bols will he have to pay for his new car?</p>""",
    options={'A': '50', 'B': '55', 'C': '60', 'D': '100', 'E': '110'},
    notes=[(1, 'y', 'Prices go up 10% a year.'),
           (2, 'g', 'Paid 500 Bols, one year ago.'),
           (3, 'p', 'Trap! 80% of what the car costs new <b>today</b>, not 80% of the 500 he paid.'),
           (4, 'y', 'So a new car now costs 500 + 10%.'),
           (5, 'b', 'Extra = new price − what he gets for the old car.')],
    steps=[
        f"""{calc(f'new price now = 500 + 10% = 500 + 50 = <b>550</b>')}""",
        f"""{calc(f'trade-in = 80% of 550 {ar()} 10% = 55, so 80% = 8 × 55 = <b>440</b>')}""",
        f"""{_car()}
{calc(f'extra = 550 − 440 = {boxed("110")}')}
{note('Shortcut: he gets 80% back, so he pays the other 20% of today’s price. 20% of 550 = 110.', 'tip')}""",
    ],
    answer_text='110 Bols: a new car costs 550 and he gets 440 for the old one.',
    why={'A': '50 is only the price rise (550 − 500). It forgets he gets just 80% back for his car.',
         'B': '55 is 10% of 550, as if he lost only 10% of the value.',
         'C': '60 is 500 − 440: it compares the trade-in with the <b>old</b> price, forgetting the new car now costs 550.',
         'D': '100 is 20% of 500: it uses the old price and ignores the 10% inflation.'},
    fast='He pays the 20% he doesn’t get back, of today’s price: 20% of 550 = 110.',
))
