from wslib import *

Y = 2012
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _meet():
    k = 62  # px per km
    x0, x8, yr = 50, 50 + 8 * k, 120
    xm = x0 + 5 * k
    road = line(x0, yr, x8, yr, k='ink', w=2.6)
    parts = [line(x0, yr - 8, x0, yr + 8, k='ink'), line(x8, yr - 8, x8, yr + 8, k='ink'),
             circle(x0 - 10, yr - 12, 9, k='pen'), circle(x0 + 14, yr - 12, 9, k='pen'),
             line(x0 - 10, yr - 12, x0 + 2, yr - 30, k='pen', w=2), line(x0 + 2, yr - 30, x0 + 14, yr - 12, k='pen', w=2),
             arrow(x0 + 30, yr - 60, x0 + 140, yr - 60, k='pen', bend=0),
             arrow(x8 - 30, yr - 60, x8 - 110, yr - 60, k='orange', bend=0),
             line(xm, yr - 40, xm, yr + 14, k='red', w=2.4, dash=True),
             circle(xm, yr, 7, k='red', fill='p')]
    lab = [stick_person(x0 + 2, yr - 30, k='pen', s=0.8), stick_person(x8, yr - 2, k='orange'),
           text(x0 + 85, yr - 72, 'Michael 20 km/h', k='pen', size=17),
           text(x8 - 70, yr - 72, 'Stewart 12 km/h', k='orange', size=17),
           text(xm, yr - 48, 'they meet here', k='red', size=17, font='scrawl'),
           text(x0, yr + 32, 'Michael', k='muted', size=14), text(x8, yr + 32, 'Stewart', k='muted', size=14)]
    braces = [brace(x0, xm, yr + 42, '5 km = 20 × 0.25', k='pen'), brace(xm, x8, yr + 42, '3 km = 12 × 0.25', k='orange')]
    lab.append(text((x0 + x8) / 2, yr + 112, 'gap of 8 km shrinks by 20 + 12 = 32 km every hour', k='red', size=17))
    return svg(620, 250, road + rough(*parts) + ''.join(lab) + ''.join(braces),
               'Michael cycles from the left at 20 km/h and Stewart runs from the right at 12 km/h; they meet 5 km from Michael and 3 km from Stewart')


Q.append(dict(
    n=1, orig=2, answer='A', topic='Speed & meeting',
    question=f"""<p>Stewart and Michael have arranged to meet. Michael is about to set off on his bicycle, and {hl('at the same time Stewart is going to run to meet him', 'y', 1)}.</p>
<p>Michael can cycle at a steady {hl('20 kilometres per hour', 'g', 2)} and Stewart can run at a steady {hl('12 kilometres per hour', 'g', 2)}. They live {hl('8 kilometres', 'g', 3)} from each other.</p>
<p class="stem">How long will it be before they meet?</p>""",
    options={'A': '15 minutes', 'B': '16 minutes', 'C': '20 minutes', 'D': '30 minutes', 'E': '32 minutes'},
    notes=[(1, 'y', 'Both start together and head <b>towards each other</b>, so both of them are closing the gap.'),
           (2, 'g', 'Moving towards each other? <b>Add</b> the speeds: 20 + 12 = 32 km every hour.'),
           (3, 'g', 'The gap they have to close between them.')],
    steps=[
        f"""<p>Picture the road. Every hour, Michael eats 20 km of the gap and Stewart eats 12 km of it.</p>{_meet()}""",
        f"""{calc('closing speed = 20 + 12 = <b>32 km/h</b>',
                  f'time = distance ÷ speed = 8 ÷ 32 = {frac(1, 4)} hour',
                  f'{frac(1, 4)} of 60 minutes = {boxed("15 minutes")}')}""",
        f"""{note('In 15 minutes Michael rides 5 km and Stewart runs 3 km. 5 + 3 = 8 km, the whole gap.', 'check')}""",
    ],
    answer_text='15 minutes: the gap closes at 32 km/h, and 8 km is a quarter of 32.',
    why={'B': '16 minutes is too long: in 16 minutes they would cover 32 × 16 ÷ 60 ≈ 8.5 km, more than the 8 km gap. (16 is the average of the two speeds, not a time.)',
         'C': '20 minutes is Michael’s speed number turned into minutes. In 20 minutes they would close 32 ÷ 3 ≈ 10.7 km, too far.',
         'D': '30 minutes uses the <b>average</b> speed, 16 km/h, for one person: 8 ÷ 16 = ½ hour. But both are moving, so the speeds add.',
         'E': '32 is the closing speed in km/h, not a number of minutes.'},
    fast='Towards each other, so add: 32 km/h. 8 km is ¼ of 32, so ¼ hour = 15 minutes.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _spend():
    s = 3.0  # px per pound
    x0 = 100

    def bar(y, segs):
        parts, lab, x = [], [], x0
        for v, name, f in segs:
            w = v * s
            parts.append(rect(x, y, w, 40, k='ink', fill=f, sw=1.6))
            lab.append(text(x + w / 2, y + 26, name, k='ink', size=15))
            x += w
        return parts, lab, x

    p1, l1, e1 = bar(40, [(84, 'food £84', 'g'), (24, '£24', 'b'), (12, '£12', 'y')])
    p2, l2, e2 = bar(130, [(100.8, 'food £100.80', 'g'), (25.2, '£25.20', 'b'), (12, '£12', 'y')])
    lab = [text(x0 - 10, 66, 'before', k='ink', size=17, anchor='end'), text(x0 - 10, 156, 'after', k='ink', size=17, anchor='end'),
           text(e1 + 10, 66, '= £120', k='ink', size=18, anchor='start'),
           text(e2 + 10, 156, '= £138', k='green', size=22, anchor='start', font='scrawl'),
           text(x0 + 84 * s + 12 * s, 30, 'household', k='pen', size=14), text(x0 + 84 * s + 24 * s + 6 * s + 30, 30, 'store-cupboard', k='orange', size=14),
           text(x0 + 42 * s, 112, '+20% (+£16.80)', k='green', size=15), text(x0 + 100.8 * s + 12.6 * s, 112, '+5%', k='pen', size=15),
           text(x0 + 100.8 * s + 25.2 * s + 6 * s, 200, 'same', k='orange', size=15)]
    return svg(600, 214, rough(*p1, *p2) + ''.join(l1 + l2 + lab),
               'Bars: before, food 84, household 24, store-cupboard 12, total 120; after, food 100.80, household 25.20, store-cupboard 12, total 138')


Q.append(dict(
    n=2, orig=6, answer='B', topic='Percentages',
    question=f"""<p>Over the course of a year, Mr and Mrs Jones and their two sons spend an average of {hl('£120 a week', 'g', 1)}
at the local supermarket. {hl('70% of this spending is the weekly family food bill, 20% goes on household goods and the final 10% on store-cupboard ingredients', 'y', 2)}. When their daughter returns
from her gap year to live at home, {hl('the weekly food bill increases by 20%', 'p', 3)} and {hl('their spending on household goods goes up 5%', 'p', 3)}, whilst {hl('they continue to spend the same on store-cupboard ingredients', 'y', 4)}.</p>
<p class="stem">How much is their new average weekly supermarket spend when their daughter returns home?</p>""",
    options={'A': '£136.80', 'B': '£138.00', 'C': '£144.00', 'D': '£145.00', 'E': '£150.00'},
    notes=[(1, 'g', 'The starting total, split three ways.'),
           (2, 'y', 'Turn the percentages into pounds first: 70% → £84, 20% → £24, 10% → £12.'),
           (3, 'p', 'Each rise is a percentage of <b>its own part</b>, not of the whole £120.'),
           (4, 'y', 'The £12 does not change.')],
    steps=[
        f"""<p>Split the £120 into its three parts:</p>
{calc('food: 70% of 120 = <b>£84</b>', 'household: 20% of 120 = <b>£24</b>', 'store-cupboard: 10% of 120 = <b>£12</b>')}""",
        f"""<p>Now apply each rise to its own part only:</p>
{calc(f'food: 20% of 84 = 16.80 {ar()} 84 + 16.80 = £100.80',
      f'household: 5% of 24 = 1.20 {ar()} 24 + 1.20 = £25.20', 'store-cupboard: still £12')}
{_spend()}""",
        f"""{calc(f'100.80 + 25.20 + 12 = {boxed("£138.00")}')}
{note('Faster: just add the rises. 16.80 + 1.20 = £18, and 120 + 18 = £138.', 'tip')}""",
    ],
    answer_text='£138.00: the food bill rises by £16.80 and household goods by £1.20, so £18 more than £120.',
    why={'A': '£136.80 adds the food rise (£16.80) but forgets the 5% on household goods.',
         'C': '£144 adds 20% to the <b>whole</b> £120. Only the food bill goes up by 20%.',
         'D': '£145 needs a rise of £25, but the real rise is only £18. It comes from taking 20% of the whole £120 (£24) plus the £1.20 household rise: £145.20.',
         'E': '£150 adds 20% and 5% of the whole £120 (24 + 6 = 30). The percentages belong to the separate parts.'},
    fast='Rises only: 20% of £84 = £16.80, 5% of £24 = £1.20. Total rise £18, so £138.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _invig():
    parts, lab = [], []
    # morning box
    parts += [rect(20, 40, 290, 190, k='pen', fill='paper', sw=2, rx=10), rect(340, 40, 290, 190, k='orange', fill='paper', sw=2, rx=10)]
    lab += [text(165, 30, 'Wednesday 9am', k='pen', size=20, font='scrawl'), text(485, 30, 'Wednesday 2pm', k='orange', size=20, font='scrawl'),
            text(40, 80, 'Maths:', k='ink', size=18, anchor='start'), text(130, 80, 'only Marjorie', k='pen', size=18, anchor='start'),
            text(40, 120, 'Latin:', k='ink', size=18, anchor='start'), text(130, 120, 'only Susan', k='pen', size=18, anchor='start'),
            text(40, 170, 'both used up for', k='red', size=16, anchor='start'), text(40, 192, 'the rest of the day!', k='red', size=16, anchor='start'),
            text(40, 218, '(+ Ian or Mike as the man)', k='muted', size=14, anchor='start'),
            text(360, 80, 'English Lang:', k='ink', size=18, anchor='start'),
            text(360, 106, 'Marjorie', k='muted', size=17, anchor='start'), text(470, 106, 'or Jenny', k='green', size=17, anchor='start'),
            text(360, 148, 'Spanish:', k='ink', size=18, anchor='start'),
            text(360, 174, 'Susan', k='muted', size=17, anchor='start'), text(470, 174, 'or Keith', k='green', size=17, anchor='start'),
            text(485, 214, 'Jenny (f) + Keith (m) ✓', k='green', size=18, font='hand')]
    parts += [line(356, 101, 438, 101, k='red', w=2.4), line(356, 169, 412, 169, k='red', w=2.4),
              arrow(250, 86, 350, 100, k='red', bend=-0.15), arrow(230, 126, 350, 166, k='red', bend=0.12)]
    return svg(650, 244, rough(*parts) + ''.join(lab),
               'Wednesday morning needs Marjorie for Maths and Susan for Latin, so in the afternoon English Lang goes to Jenny and Spanish to Keith')


Q.append(dict(
    n=3, orig=7, answer='C', topic='Logic & timetables',
    question=f"""<p><b><u>Kingsbury School Examination Schedule for the first week of June</u></b></p>
{table([['History<br>3hrs', 'English Lit<br>3hrs', hl('Maths<br>2hrs', 'g'), 'Economics<br>2hrs', 'Maths<br>2hrs'],
        ['English Lit<br>2 hrs', 'Physics<br>3hrs', hl('Latin<br>2hrs', 'g'), 'History<br>2hrs', 'Latin<br>2hrs'],
        ['<i>lunch</i>', '<i>lunch</i>', '<i>lunch</i>', '<i>lunch</i>', '<i>lunch</i>'],
        ['Geography<br>2hrs 30mins', 'Chemistry<br>3hrs', hl('English Lang<br>2hrs 30mins', 'g'), 'Economics<br>2hrs 30mins', '-'],
        ['Biology<br>1hr 30mins', 'French<br>2hrs', hl('Spanish<br>2hrs', 'g'), 'German<br>2hrs', '-']],
       head=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])}
<p>All exams take place in the school hall. All morning exams start at 9am, all afternoon exams start at
2pm. {hl('Each session (morning or afternoon) must have at least one male and one female invigilator', 'y', 1)}.
{hl('Each examination must be invigilated by one teacher of that subject', 'y', 2)}. {hl('Each person can only invigilate once a day', 'p', 3)}.</p>
<p>Of the male teachers, Ian teaches Economics and German, Mike teaches French and German,
and Keith teaches French and Spanish. Of the female teachers, Marjorie teaches Maths and
English, Susan teaches Spanish and Latin, and Jenny teaches English and History,</p>
<p class="stem">Who will invigilate on {hl('Wednesday afternoon', 'b', 4)}?</p>""",
    options={'A': 'Ian and Marjorie', 'B': 'Jenny and Mike', 'C': 'Keith and Jenny', 'D': 'Marjorie and Keith', 'E': 'Mike and Susan'},
    notes=[(1, 'y', 'Every session needs a man <b>and</b> a woman.'),
           (2, 'y', 'Each exam needs its own subject teacher in the room.'),
           (3, 'p', 'The key rule: anyone used in the <b>morning</b> is out for the afternoon.'),
           (4, 'b', 'Afternoon = English Lang and Spanish. But sort out the morning first!')],
    steps=[
        f"""<p>Wednesday’s exams: morning <b>Maths</b> and <b>Latin</b>; afternoon <b>English Lang</b> and <b>Spanish</b>.</p>
<p>Start with the morning, because it uses people up:</p>
<ul><li>Maths: only <b>Marjorie</b> teaches it.</li><li>Latin: only <b>Susan</b> teaches it.</li></ul>
<p>So Marjorie and Susan are both busy in the morning and can’t do the afternoon.</p>""",
        f"""<p>Now the afternoon:</p>{_invig()}
{calc(f'English Lang: Marjorie or Jenny {ar()} Marjorie is used {ar()} <b>Jenny</b>',
      f'Spanish: Keith or Susan {ar()} Susan is used {ar()} <b>Keith</b>',
      f'one man + one woman ✓ {ar()} {boxed("Keith and Jenny")}')}""",
    ],
    answer_text='Keith and Jenny: Marjorie and Susan are needed for Maths and Latin in the morning.',
    why={'A': 'Marjorie has to do the morning Maths, and Ian teaches neither English nor Spanish.',
         'B': 'Mike teaches neither English nor Spanish, so he can’t cover Spanish. Jenny is right, but Keith must be the other one.',
         'D': 'Marjorie can teach English, but she is the only Maths teacher, so she is used in the morning. Once a day only.',
         'E': 'Susan is the only Latin teacher, so she is used in the morning. Mike teaches neither afternoon subject.'},
    fast='Morning first: Maths needs Marjorie, Latin needs Susan. Afternoon: English → Jenny, Spanish → Keith.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _cuts():
    parts, lab = [], []
    titles = ['cut across', 'cut lengthways', 'slanting cut']
    for i in range(3):
        x = 20 + i * 215
        rx, ry, rw, rh = x + 8, 60, 66, 130
        parts.append(rect(rx, ry, rw, rh, k='ink', fill='paper', sw=2))
        lab.append(text(x + 95, 32, titles[i], k='ink', size=19, font='scrawl'))
        cx, cy = rx + rw / 2, ry + rh / 2
        if i == 0:
            parts += [rect(rx, cy, rw, rh / 2, k='ink', fill='b', sw=2), line(rx - 6, cy, rx + rw + 6, cy, k='red', w=2.6, dash=True)]
            parts += [rect(x + 120, 70, 66, 50, k='pen', fill='b', sw=2), circle(x + 153, 165, 30, k='pen', fill='b', sw=2)]
            lab += [text(x + 153, 62, 'side: A', k='pen', size=16), text(x + 153, 212, 'top: B', k='pen', size=16)]
        elif i == 1:
            parts += [rect(rx, ry, rw / 2, rh, k='ink', fill='b', sw=2), line(cx, ry - 6, cx, ry + rh + 6, k='red', w=2.6, dash=True)]
            parts += [rect(x + 130, 70, 33, 60, k='pen', fill='b', sw=2),
                      path(f'M{x + 120} 190 A 33 33 0 0 1 {x + 186} 190 Z', k='pen', fill='b', sw=2)]
            lab += [text(x + 146, 62, 'side: A', k='pen', size=16), text(x + 153, 212, 'end: D', k='pen', size=16)]
        else:
            parts += [poly([(rx, ry), (rx, ry + rh), (rx + rw, ry + rh)], k='ink', fill='b', sw=2),
                      line(rx - 4, ry - 8, rx + rw + 4, ry + rh + 8, k='red', w=2.6, dash=True)]
            parts += [poly([(x + 130, 80), (x + 130, 190), (x + 186, 190)], k='pen', fill='b', sw=2)]
            lab += [text(x + 160, 212, 'side: E', k='pen', size=16)]
        parts.append(circle(cx, cy, 4, k='red', fill='p', sw=2))
        parts.append(arrow(x + 82, 120, x + 112, 120, k='muted', bend=0.2, w=1.8))
    lab.append(text(330, 248, 'every cut goes through the centre (red dot), so each side view keeps a right angle', k='red', size=16))
    return svg(660, 262, rough(*parts) + ''.join(lab),
               'Three ways to halve a cylinder seen from the side: across gives a rectangle and a circle, lengthways gives a rectangle and a semicircle, slanting gives a right-angled triangle')


Q.append(dict(
    n=4, orig=8, answer='C', topic='3D views',
    question=f"""<p>Below are pictures of three cylinders.</p>
{fig(Y, 'ps_q04_cylinders', 'A tall cylinder, a medium cylinder about as wide as it is tall, and a short flat cylinder', 300)}
<p class="stem">If a cylinder is cut into two {hl('equal halves', 'y', 1)} with {hl('one straight cut', 'y', 2)}, which one of the following could {hl('<b>not</b>', 'b', 3)}
be a view of one of the halves {hl('from any direction', 'p', 4)}?</p>
{fig(Y, 'ps_q04_opts', 'Option shapes: A rectangle, B circle, C triangle with a point at the top in the middle, D semicircle, E right-angled triangle', 476)}""",
    options={'A': 'rectangle', 'B': 'circle', 'C': 'triangle', 'D': 'semicircle', 'E': 'right-angled triangle'},
    notes=[(1, 'y', 'Two equal halves: the cut has to pass through the <b>centre</b> of the cylinder.'),
           (2, 'y', 'One flat cut: across, lengthways or slanting.'),
           (3, 'b', 'Find the one shape you can never see.'),
           (4, 'p', 'Any direction: from the top, the end or the side. The cylinder can be tall or flat (that is why three are shown).')],
    steps=[
        f"""<p>Try the three kinds of cut and look at one half from the side and from the end:</p>{_cuts()}""",
        f"""{calc(f'cut across {ar()} a shorter cylinder: rectangle (A) from the side, circle (B) from the top',
                  f'cut lengthways {ar()} half a cylinder: semicircle (D) from the end',
                  f'slanting cut, corner to corner {ar()} right-angled triangle (E) from the side')}""",
        f"""<p>Seen from the side with the cut edge-on, the cylinder is a rectangle and the cut is a straight line through its centre. The half you see is the part of
the rectangle on one side of that line, so it always keeps some of the rectangle’s <b>right-angled corners</b> (A or E). Seen from the top or the end you get curves (B or D).</p>
<p>A triangle with no right angle and its point in the middle of the top (C) never appears {ar()} {boxed('C')}</p>""",
    ],
    answer_text='C: every possible half shows right-angled corners or curves, never a pointed triangle like C.',
    why={'A': 'A is possible: cut across, then look at either half from the side (a squat cylinder looks like a rectangle).',
         'B': 'B is possible: cut across, then look down on the half from above. You still see a full circle.',
         'D': 'D is possible: cut lengthways down the middle, then look at the half end-on.',
         'E': 'E is possible: cut slanting from one top edge to the opposite bottom edge, then look from the side.'},
    fast='Halves need a cut through the centre. From the side that keeps right angles (A, E); from above or the end you get curves (B, D). C is the odd one.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _venn():
    cy = 168
    lens = f'M320 {cy - 78.3:.1f} A105 105 0 0 1 320 {cy + 78.3:.1f} A105 105 0 0 1 320 {cy - 78.3:.1f} Z'
    parts = [rect(20, 14, 600, 290, k='ink', fill='paper', sw=2, rx=8),
             circle(250, cy, 105, k='pen', fill='b', sw=2.4), circle(390, cy, 105, k='orange', fill='o', sw=2.4),
             path(lens, k='red', fill='p', sw=2)]
    lab = [text(170, 46, 'maths 127', k='pen', size=21, font='scrawl'), text(470, 46, 'economics 89', k='orange', size=21, font='scrawl'),
           text(205, cy + 8, '96', k='ink', size=26), text(320, cy + 6, '31', k='red', size=30, font='scrawl'),
           text(435, cy + 8, '58', k='ink', size=26), text(320, cy + 32, 'both', k='red', size=16),
           text(560, 290, 'neither 45', k='ink', size=18), text(80, 290, '230 in total', k='ink', size=18)]
    return svg(640, 320, rough(*parts) + ''.join(lab),
               'Venn diagram: maths only 96, both 31, economics only 58, neither 45, total 230')


Q.append(dict(
    n=5, orig=12, answer='B', topic='Venn diagrams',
    question=f"""<p>A merchant bank recently advertised for new graduates to fill positions as trainee analysts; {hl('230', 'g', 1)}
people applied. Of these, {hl('127 had maths', 'g', 2)} as a component of their degree and {hl('89 had economics', 'g', 2)}
as a component of their degree. {hl('Only 45 had neither maths nor economics', 'p', 3)} as a component of
their degree.</p>
<p class="stem">How many must have had {hl('both', 'b', 4)} maths and economics as a component of their degree?</p>""",
    options={'A': '14', 'B': '31', 'C': '59', 'D': '83', 'E': '171'},
    notes=[(1, 'g', 'Everyone: the whole box of the Venn diagram.'),
           (2, 'g', 'These two groups overlap. Anyone with both is counted in <b>both</b> numbers.'),
           (3, 'p', 'Take these out first: they sit outside both circles.'),
           (4, 'b', 'The overlap in the middle.')],
    steps=[
        f"""{calc('people with maths or economics (or both) = 230 − 45 = <b>185</b>')}""",
        f"""{calc('127 + 89 = 216', f'216 is more than 185 {ar()} the overlap has been counted twice',
                  f'both = 216 − 185 = {boxed("31")}')}""",
        f"""<p>Fill in the Venn diagram to check:</p>{_venn()}
{calc('maths only = 127 − 31 = 96', 'economics only = 89 − 31 = 58', '96 + 31 + 58 + 45 = 230 ✓')}""",
    ],
    answer_text='31: 127 + 89 = 216 counts the overlap twice, but only 230 − 45 = 185 people did either subject.',
    why={'A': '14 is 230 − 216: it forgets the 45 people who had neither subject.',
         'C': '59 is 230 − 171, built on option E’s mistake.',
         'D': '83 is 127 − 89 + 45: subtracting the two groups doesn’t find the overlap.',
         'E': '171 is 127 + 89 − 45: it takes the “neither” group away from the wrong number.'},
    fast='Either subject = 230 − 45 = 185. Overlap = 127 + 89 − 185 = 31.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _games():
    rows = [('playing boards', '98 ÷ 1', 98), ('question cards', '5000 ÷ 50', 100), ('playing pieces', '1000 ÷ 6', 166),
            ('money tokens', '5000 ÷ 40', 125), ('bonus tokens', '1000 ÷ 12', 83), ('dice', '300 ÷ 2', 150)]
    X = lambda v: 170 + v * 2.0
    parts, lab = [], []
    for i, (name, sum_, v) in enumerate(rows):
        y = 30 + i * 36
        f = 'p' if v == 83 else 'b'
        parts.append(rect(X(0), y, X(v) - X(0), 24, k='ink', fill=f, sw=1.6))
        lab.append(text(160, y + 18, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 8, y + 18, f'{sum_} → {v}', k='red' if v == 83 else 'ink', size=15, anchor='start'))
    parts.append(line(X(83), 20, X(83), 246, k='red', w=2.4, dash=True))
    lab.append(text(X(83), 266, 'only 83 complete games', k='red', size=18, font='scrawl'))
    return svg(640, 278, rough(*parts) + ''.join(lab),
               'Complete games each part allows: boards 98, cards 100, pieces 166, money 125, bonus tokens 83, dice 150; bonus tokens run out first at 83')


Q.append(dict(
    n=6, orig=13, answer='A', topic='Division & limits',
    question=f"""<p>A boxed up board game consists of the following components:</p>
<ul><li>1 playing board</li><li>50 question cards</li><li>6 playing pieces</li><li>40 money tokens</li><li>{hl('12 bonus tokens', 'g')}</li><li>2 dice</li></ul>
<p>The producers of the board game have all the component parts manufactured separately and sent
to their warehouse, where they box them up and send them to retailers in {hl('cartons of 8 complete games', 'p', 1)}. In their warehouse they have: {hl('98 playing boards; 5,000 question cards; 1,000 playing pieces; 5,000 money tokens; 1,000 bonus tokens and 300 dice', 'g', 2)}.</p>
<p class="stem">What is the {hl('maximum number of cartons', 'b', 3)} of eight games they can dispatch from their warehouse?</p>""",
    options={'A': '10', 'B': '11', 'C': '12', 'D': '20', 'E': '83'},
    notes=[(1, 'p', 'Two steps: first count complete <b>games</b>, then pack them 8 to a carton.'),
           (2, 'g', 'Divide each stock by how many one game needs.'),
           (3, 'b', 'Cartons, not games! Only full cartons of 8 count.')],
    steps=[
        f"""<p>How many complete games could each part make on its own?</p>{_games()}""",
        f"""<p>The part that runs out first decides: the <b>bonus tokens</b>.</p>
{calc('1000 ÷ 12 = 83 remainder 4 → <b>83 games</b>', f'83 ÷ 8 = 10 remainder 3 {ar()} {boxed("10 cartons")}')}
{note('1000 ÷ 12: 12 × 80 = 960, 12 × 3 = 36, so 12 × 83 = 996 with 4 left over.', 'tip')}""",
    ],
    answer_text='10 cartons: the bonus tokens only stretch to 83 games, which fill 10 cartons of 8 (with 3 games spare).',
    why={'B': '11 cartons need 88 games, but there are only enough bonus tokens for 83.',
         'C': '12 is 98 ÷ 8 rounded down: it only checks the playing boards.',
         'D': '20 is 166 ÷ 8 rounded down: it only checks the playing pieces.',
         'E': '83 is the number of complete <b>games</b>, not cartons.'},
    fast='Smallest of 98, 100, 166, 125, 83, 150 is 83 games. 83 ÷ 8 = 10 full cartons.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _sym(kind, cx, cy, up=False):
    if kind == 'bar':
        return rect(cx - 11, cy - 4, 22, 8, k='ink', fill='ink', sw=1)
    if kind == 'vbar':
        return rect(cx - 4, cy - 11, 8, 22, k='ink', fill='ink', sw=1)
    if kind == 'hex':
        return poly([(cx - 12, cy), (cx - 6, cy - 7), (cx + 6, cy - 7), (cx + 12, cy), (cx + 6, cy + 7), (cx - 6, cy + 7)], k='ink', fill='ink', sw=1)
    if kind == 'tri':
        if up:
            return poly([(cx, cy - 9), (cx - 9, cy + 8), (cx + 9, cy + 8)], k='ink', fill='ink', sw=1)
        return poly([(cx, cy + 9), (cx - 9, cy - 8), (cx + 9, cy - 8)], k='ink', fill='ink', sw=1)
    return ''


def _board():
    c = 52
    covered = {(1, 1), (1, 2), (2, 3), (3, 2), (3, 4), (4, 1)}
    blank = {(1, 3), (1, 4), (2, 2), (2, 4), (3, 1), (3, 3), (4, 2), (4, 3)}
    parts, lab = [], []

    def grid(ox, oy):
        p = []
        for r in range(1, 5):
            for col in range(1, 5):
                x, y = ox + (col - 1) * c, oy + (r - 1) * c
                f = 'g' if (r, col) in blank else 'paper'
                p.append(rect(x, y, c, c, k='ink', fill=f, sw=1.6))
                if (r, col) in covered:
                    p.append(circle(x + c / 2, y + c / 2, 20, k='muted', sw=1.6))
        return p

    ox1, ox2, oy = 30, 370, 50
    parts += grid(ox1, oy) + grid(ox2, oy)
    for (r, col) in covered:
        lab.append(text(ox1 + (col - 0.5) * c, oy + (r - 0.5) * c + 7, '?', k='muted', size=20))
    lab += [_sym('bar', ox1 + 0.5 * c, oy + 1.5 * c), _sym('hex', ox1 + 3.5 * c, oy + 3.5 * c)]
    # B turned through a half turn
    b_turned = [('hex', 4, 4), ('tri', 4, 1), ('bar', 3, 4), ('tri', 3, 2), ('bar', 2, 1)]
    for kind, r, col in b_turned:
        lab.append(_sym(kind, ox2 + (col - 0.5) * c, oy + (r - 0.5) * c, up=True))
    lab += [text(ox1 + 2 * c, 32, 'what the board tells us', k='ink', size=18, font='scrawl'),
            text(ox2 + 2 * c, 32, 'B turned upside down', k='green', size=18, font='scrawl'),
            text(ox1 + 2 * c, oy + 4 * c + 26, 'green = must be blank', k='green', size=15),
            text(ox1 + 2 * c, oy + 4 * c + 46, '? = hidden, anything goes', k='muted', size=15),
            text(ox2 + 2 * c, oy + 4 * c + 26, 'symbols land only on ? squares', k='green', size=15),
            text(ox2 + 2 * c, oy + 4 * c + 46, 'plus the bar and hexagon ✓', k='green', size=15)]
    parts.append(arrow(ox1 + 4 * c + 20, oy + 2 * c, ox2 - 20, oy + 2 * c, k='red', bend=-0.15))
    lab.append(text((ox1 + 4 * c + ox2) / 2, oy + 2 * c + 36, 'match?', k='red', size=16))
    return svg(620, 316, rough(*parts) + ''.join(lab),
               'Left: the board with hidden squares marked ? and visible empty squares green. Right: option B turned upside down; its symbols fall only on hidden squares and on the visible bar and hexagon')


Q.append(dict(
    n=7, orig=14, answer='B', topic='Rotations & grids',
    question=f"""<p>In a game, circular counters are moved around a board which is a 4 x 4 grid. There are symbols on
some of the squares on the board. At one point in the game, the board looks like this ({hl('all the circles represent counters which completely cover any symbol on the square that they occupy', 'y', 1)}):</p>
{fig(Y, 'ps_q07_board', 'The board: six counters; a small bar in row 2 column 1 and a flat hexagon in the bottom-right square are visible', 128)}
<p class="stem">Which one of the following diagrams {hl('could', 'b', 2)} show the layout of the board ({hl('not necessarily viewed in the same direction as above', 'p', 3)})?</p>
{fig(Y, 'ps_q07_opts', 'Five 4 by 4 grids A to E showing hexagons, bars and triangles in different squares', 474)}""",
    options={'A': 'grid A', 'B': 'grid B', 'C': 'grid C', 'D': 'grid D', 'E': 'grid E'},
    notes=[(1, 'y', 'A counter can hide anything. But a square you <b>can</b> see that is empty must be empty, and the two symbols you can see must be there.'),
           (2, 'b', 'Find the only option that agrees with every visible square.'),
           (3, 'p', 'You may turn the board round. Watch which way the bar and hexagon then face!')],
    steps=[
        f"""<p>Write down what the board really tells us: 8 squares are visibly <b>blank</b>, 6 are hidden (?), the bar lies flat in row 2 on the left,
and the flat hexagon is in the bottom-right corner.</p>""",
        f"""<p>Which turns are allowed? In every option the hexagon lies flat, like on the board. A quarter turn would stand it on its point,
so the option must be either the right way up or turned upside down (half turn).</p>
{calc(f'right way up: hexagon must be bottom-right {ar()} C or E',
      f'upside down: hexagon must be top-left {ar()} A or B')}""",
        f"""<p>Test those four:</p>
<ul><li><b>C</b>: its triangle in the top row, 3rd column sits on a visibly blank square {cross()}</li>
<li><b>E</b>: its bar in the top row, 3rd column sits on a visibly blank square {cross()}</li>
<li><b>A</b> upside down: its triangle (row 2, column 2) lands on row 3, column 3, which is blank {cross()}</li>
<li><b>B</b> upside down: everything lands on a hidden square, the bar or the hexagon {tick()}</li></ul>
{_board()}
{calc(f'only {boxed("B")} fits')}""",
        f"""{note('D is the sneaky one: give it a quarter turn and every symbol lands in a hidden square, and its upright bar even becomes the flat bar. But the hexagon would then stand on its point, and the board’s hexagon is flat.', 'trap')}""",
    ],
    answer_text='Grid B, turned upside down: every symbol is under a counter except the bar and the hexagon, which match.',
    why={'A': 'Upside down, A’s triangle in row 2, column 2 lands on a square we can see is blank.',
         'C': 'C’s triangle (top row, 3rd column) is on a square that is visibly blank on the board.',
         'D': 'A quarter turn puts the symbols in the right squares, but the flat hexagon would end up standing on its point.',
         'E': 'E’s upright bar (top row, 3rd column) is on a visibly blank square.'},
    fast='Hexagon is flat, so only half turns. Hexagon top-left (A, B) or bottom-right (C, E). Check the blank squares: only B survives.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _map():
    u = 82  # px per km
    X = lambda e: 70 + (e - 20.5) * u
    Yn = lambda n: 362 - (n - 4.6) * u
    parts, lab = [], []
    ix, iy = X(23), Yn(8)
    r1, r2 = 1.8 * u, 1.1 * u
    parts.append(f'<path d="M{ix - r1} {iy} a{r1} {r1} 0 1 0 {2 * r1} 0 a{r1} {r1} 0 1 0 {-2 * r1} 0 Z '
                 f'M{ix - r2} {iy} a{r2} {r2} 0 1 0 {2 * r2} 0 a{r2} {r2} 0 1 0 {-2 * r2} 0 Z" '
                 f'class="k-orange f-y" fill-rule="evenodd" stroke-width="1.6"/>')
    for e in (21, 22, 23, 24):
        parts.append(line(X(e), Yn(4.75), X(e), Yn(8.35), k='muted', w=1.2))
        lab.append(text(X(e), Yn(4.6) + 16, f'{e}', k='muted', size=15))
    for n in (5, 6, 7, 8):
        parts.append(line(X(20.7), Yn(n), X(24.45), Yn(n), k='muted', w=1.2))
        lab.append(text(X(20.62), Yn(n) + 5, f'0{n}', k='muted', size=15, anchor='end'))
    for name, e, n in (('G', 22, 6), ('H', 23, 6), ('I', 23, 8)):
        parts.append(circle(X(e), Yn(n), 7, k='ink', fill='ink'))
        lab.append(text(X(e) + 12, Yn(n) + 22, name, k='ink', size=20, font='print', weight='700', anchor='start'))
    opts = [('A', 22, 7, 'green'), ('B', 21, 6, 'red'), ('C', 22, 5, 'red'), ('D', 24, 7, 'red'), ('E', 23, 7, 'red')]
    for name, e, n, col in opts:
        parts.append(circle(X(e), Yn(n), 13, k=col, fill='paper', sw=2.4))
        lab.append(text(X(e), Yn(n) + 6, name, k=col, size=17, font='print', weight='700'))
    lab += [text(X(24.6), Yn(6.3), "yellow ring: Ingrid's", k='orange', size=16, anchor='start'),
            text(X(24.6), Yn(6.3) + 20, 'band, 1100 m to 1800 m', k='orange', size=16, anchor='start'),
            text(X(24.6), Yn(5.0), '1 square = 1 km', k='ink', size=16, anchor='start'),
            text(X(24.6), Yn(5.0) + 20, 'diagonal ≈ 1.41 km', k='ink', size=16, anchor='start')]
    return svg(600, 392, rough(*parts) + ''.join(lab),
               'Map grid with Gordon at 22,06, Helen at 23,06 and Ingrid at 23,08, the five option points, and the ring of distances 1100 to 1800 m around Ingrid')


Q.append(dict(
    n=8, orig=18, answer='A', topic='Maps & distance',
    question=f"""<p>This diagram shows the positions of three ornithologists on a map. {hl('The squares on the map are 1000m along each side', 'g', 1)}.</p>
{fig(Y, 'ps_q08_map', 'Grid map with eastings 20 to 25 and northings 05 to 08; G at 22,06, H at 23,06 and I at 23,08', 440)}
<p>The ornithologists are trying to find an injured falcon which is carrying a radio transmitter. Each
ornithologist has a radio tracking device. The direction-finding part of the trackers is not working but
the signal strength gives an indication of the distance to the bird.</p>
<p>The ornithologists have the following information about the distance from themselves to the bird.</p>
<p>Gordon is at position 22,06; signal strength indicates {hl('more than 500m and less than 2000m', 'g', 2)}.<br>
Helen is at position 23,06; signal strength indicates {hl('more than 100m and less than 2000m', 'g', 2)}.<br>
Ingrid is at position 23,08; signal strength indicates {hl('more than 1100m and less than 1800m', 'p', 3)}.</p>
<p class="stem">At which one of the following grid points {hl('could', 'b', 4)} the bird be located?</p>""",
    options={'A': '22,07', 'B': '21,06', 'C': '22,05', 'D': '24,07', 'E': '23,07'},
    notes=[(1, 'g', 'One square = 1 km. A diagonal across one square = √2 ≈ 1.41 km (Pythagoras).'),
           (2, 'g', 'Bands for Gordon and Helen. “Less than 2000 m” means exactly 2000 m is <b>not</b> allowed.'),
           (3, 'p', 'Ingrid’s band is the narrowest: start with her.'),
           (4, 'b', 'The point must fit all three bands at once.')],
    steps=[
        f"""<p>Grid points can only be certain distances apart:</p>
{calc('1 square straight = 1000 m', f'1 square diagonally = √(1² + 1²) = √2 ≈ <b>1414 m</b>', '2 squares straight = 2000 m')}""",
        f"""<p>Ingrid needs more than 1100 m and less than 1800 m. 1000 m is too close and 2000 m too far, so the bird is exactly
<b>one diagonal step</b> from Ingrid (23,08): that means 22,07 or 24,07.</p>{_map()}""",
        f"""<p>Check those two against Gordon (22,06):</p>
{calc(f'22,07: 1 square away = 1000 m {ar()} between 500 and 2000 ✓',
      f'24,07: 2 across and 1 up = √(4 + 1) = √5 ≈ 2236 m {ar()} too far ✗')}
<p>And Helen to 22,07: one diagonal, 1414 m, between 100 and 2000 ✓. So {boxed('22,07')}</p>""",
    ],
    answer_text='22,07: 1000 m from Gordon, 1414 m from Helen and 1414 m from Ingrid, inside all three bands.',
    why={'B': '21,06 is exactly 2000 m from Helen (needs less than 2000) and about 2830 m from Ingrid.',
         'C': '22,05 is √10 ≈ 3160 m from Ingrid, far outside her 1800 m limit.',
         'D': '24,07 is √5 ≈ 2240 m from Gordon, more than his 2000 m limit.',
         'E': '23,07 is only 1000 m from Ingrid, but she needs more than 1100 m.'},
    fast='Ingrid’s band (1100–1800) only allows a diagonal step: 22,07 or 24,07. Gordon rules out 24,07 (≈ 2.24 km). Answer 22,07.',
))
