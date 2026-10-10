from wslib import *

Y = 2018
Q = []

# shared seven-segment helper (used again in part 2)
DIG7 = {'0': 'abcdef', '1': 'bc', '2': 'abged', '3': 'abgcd', '4': 'fbgc', '5': 'afgcd',
        '6': 'afgedc', '7': 'abc', '8': 'abcdefg', '9': 'abcfg'}


def seg7(x, y, w, h, segs, k='ink', sw=5, gap=4):
    """Seven-segment digit with its top-left corner at (x, y)."""
    m = y + h / 2
    ends = {'a': (x, y, x + w, y), 'b': (x + w, y, x + w, m), 'c': (x + w, m, x + w, y + h),
            'd': (x, y + h, x + w, y + h), 'e': (x, m, x, y + h), 'f': (x, y, x, m), 'g': (x, m, x + w, m)}
    out = []
    for s in segs:
        x1, y1, x2, y2 = ends[s]
        if x1 == x2:
            out.append(line(x1, y1 + gap, x2, y2 - gap, k=k, w=sw))
        else:
            out.append(line(x1 + gap, y1, x2 - gap, y2, k=k, w=sw))
    return out


# ---------------------------------------------------------------- 1 (Q2)
def _class():
    parts, lab = [], []
    # girls
    for i in range(6):
        x = 40 + i * 30
        lab.append(stick_person(x, 112, k='orange', s=1.0))
        for j in range(3):
            parts.append(circle(x - 8 + j * 8, 128, 4, k='red', fill='p', sw=1.5))
    lab += [text(115, 30, '6 girls', k='orange', size=20, font='scrawl'),
            text(115, 160, '3 roses each', k='ink', size=16),
            text(115, 182, '6 × 3 = 18 roses', k='red', size=17)]
    # boys in groups of 3 with a tree each
    for g in range(6):
        gx = 262 + (g % 3) * 130
        gy = 92 if g < 3 else 196
        for b in range(3):
            lab.append(stick_person(gx + b * 18, gy, k='pen', s=0.8))
        tx = gx + 66
        parts.append(poly([(tx, gy - 42), (tx - 14, gy - 12), (tx + 14, gy - 12)], k='green', fill='g', sw=1.8))
        parts.append(line(tx, gy - 12, tx, gy, k='green', w=2.4))
        parts.append(rect(gx - 12, gy - 50, 100, 58, k='muted', sw=1.4, rx=10))
    lab += [text(450, 30, '18 boys = 6 groups of 3', k='pen', size=20, font='scrawl'),
            text(450, 228, '1 birch tree per group: 6 trees', k='green', size=17),
            text(330, 262, 'plants: 18 roses + 6 trees = 24 ✓   pupils: 6 + 18 = 24 ✓', k='ink', size=18)]
    return svg(660, 276, rough(*parts) + ''.join(lab),
               'Six girls with three roses each make 18 roses; eighteen boys in six groups of three plant six trees; 24 plants in all')

Q.append(dict(
    n=1, orig=2, answer='D', topic='Equations & word problems',
    question=f"""<p>There are {hl('24 pupils', 'g', 1)} in a class. They decided to help the local park by planting {hl('a total of 24 plants', 'g', 2)}, a mixture of birch trees and roses. {hl('Each girl planted three roses', 'y', 3)}, and {hl('every three boys planted one birch tree between them', 'p', 4)}.</p>
<p class="stem">How many {hl('<b>more boys than girls</b>', 'b', 5)} are there in the class?</p>""",
    options={'A': '3', 'B': '6', 'C': '8', 'D': '12', 'E': '18'},
    notes=[(1, 'g', 'Girls + boys = 24.'),
           (2, 'g', 'Roses + trees = 24 as well. Two totals, two unknowns.'),
           (3, 'y', '1 girl → 3 plants. Girls make lots of plants!'),
           (4, 'p', 'Trap: it’s 1 tree per <b>three</b> boys, so boys make very few plants. Boys ÷ 3 = trees.'),
           (5, 'b', 'They want boys − girls, not the number of boys.')],
    steps=[
        f"""<p>Write the two facts as sums:</p>
{calc('girls + boys = 24', f'roses + trees = 3 × girls + {frac("boys", "3")} = 24')}""",
        f"""<p>Times the second line by 3 to clear the fraction, then take away the first line:</p>
{calc('9 × girls + boys = 72', '1 × girls + boys = 24', f'subtract {ar()} 8 × girls = 48 {ar()} <b>girls = 6</b>', 'boys = 24 − 6 = <b>18</b>')}
{note('No algebra? Try the options. The number of boys must divide by 3 (they work in threes), and boys + girls = 24.', 'tip')}""",
        f"""<p>Check it with a picture:</p>{_class()}
{calc(f'18 − 6 = {boxed("12")} more boys')}""",
    ],
    answer_text='12: 18 boys and 6 girls.',
    why={'A': '3 is impossible: boys + girls = 24 is even, so boys − girls must be even too.',
         'B': '6 is the number of <b>girls</b> (or of trees), not the difference.',
         'C': '8 would mean 8 girls and 16 boys. The 8 girls alone plant 24 roses, so the boys’ trees push the total past 24 (and 16 boys don’t split into threes).',
         'E': '18 is the number of <b>boys</b>. The question asks how many more boys than girls.'},
    fast='Boys must be a multiple of 3. Girls g, boys 24 − g: 3g + (24 − g) ÷ 3 = 24 gives g = 6. 18 − 6 = 12.',
))

# ---------------------------------------------------------------- 2 (Q6)
def _bottles():
    s = 0.36  # px per ml
    base, parts, lab = 230, [], []

    def bottle(x, layers, title, sub):
        y = base
        for ml, f, name in layers:
            hgt = ml * s
            parts.append(rect(x, y - hgt, 90, hgt, k='ink', fill=f, sw=1.4))
            if name:
                lab.append(text(x + 45, y - hgt / 2 + 6, name, k='ink', size=15))
            y -= hgt
        parts.append(rect(x, base - 500 * s, 90, 500 * s, k='ink', sw=2.4, rx=6))
        lab.append(text(x + 45, 36, title, k='pen', size=18, font='scrawl'))
        lab.append(text(x + 45, base + 24, sub, k='ink', size=16))

    bottle(30, [(100, 'o', '100 conc'), (400, 'b', '400 water')], '1. made up', '500 ml, 1 : 4')
    bottle(250, [(80, 'o', '80 conc'), (320, 'b', '320 water'), (100, 'paper', 'spilt')], '2. after the spill', '400 ml left')
    bottle(470, [(80, 'o', '80'), (320, 'b', '320 water'), (100, 'o', '+100 conc')], '3. topped up', '180 conc in 500')
    parts.append(arrow(130, 140, 240, 140, k='red', bend=-0.15))
    parts.append(arrow(350, 140, 460, 140, k='red', bend=-0.15))
    lab += [text(185, 118, 'lose ⅕', k='red', size=16), text(405, 118, 'add 100', k='red', size=16)]
    return svg(600, 268, rough(*parts) + ''.join(lab),
               'Three bottles: 100 ml concentrate and 400 water; after the spill 80 and 320; after topping up 180 concentrate and 320 water')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Ratio & percentages',
    question=f"""<p>Jake has a {hl('500 ml', 'g', 1)} bottle of orange squash that he has made according to the instructions on
the bottle of concentrate. The instructions dictate that he should add {hl('4 parts water to 1 part concentrate', 'y', 2)}. He accidentally spills his squash, and now there is only {hl('400 ml', 'g', 3)} in the bottle. He
then {hl('tops up the remainder with concentrate', 'p', 4)}.</p>
<p class="stem">What {hl('percentage', 'b', 5)} of the squash in his 500 ml bottle is now concentrate?</p>""",
    options={'A': '18%', 'B': '20%', 'C': '28%', 'D': '36%', 'E': '40%'},
    notes=[(1, 'g', 'Start: a full 500 ml of ready-made squash.'),
           (2, 'y', '4 + 1 = 5 parts, so concentrate is 1 part in <b>5</b> = 20%. (Not 1 in 4!)'),
           (3, 'g', 'The spilt squash takes concentrate with it: 400 ml is still 20% concentrate.'),
           (4, 'p', 'He refills the missing 100 ml with <b>pure</b> concentrate.'),
           (5, 'b', 'Concentrate ÷ 500 × 100.')],
    steps=[
        f"""<p>Follow the concentrate through the three stages:</p>{_bottles()}""",
        f"""{calc('start: 500 ÷ 5 = 100 ml concentrate', f'after the spill: 400 ÷ 5 = <b>80 ml</b> concentrate', f'top-up: 80 + 100 = <b>180 ml</b> concentrate')}""",
        f"""{calc(f'{frac(180, 500)} = {frac(36, 100)} = {boxed("36%")}')}
{note('Out of 500, double it and move the point: 180 × 2 = 360, so 36%.', 'tip')}""",
    ],
    answer_text='36%: 180 ml of the 500 ml is concentrate.',
    why={'A': '18% is 180 ml divided by 1000 instead of 500.',
         'B': '20% is the strength before the accident: it forgets the 100 ml of pure concentrate added.',
         'C': '28% would need 140 ml of concentrate, so only 40 ml would have survived the spill. But 400 ml of squash at 1 part in 5 still holds 80 ml.',
         'E': '40% reads “4 parts water to 1 part concentrate” as 1 part in 4 (125 ml at the start, 100 after the spill, 200 after the top-up). It is 1 part in 5.'},
    fast='Concentrate is ⅕. After the spill 400 ÷ 5 = 80 ml, plus 100 ml = 180 ml. 180 ÷ 500 = 36%.',
))

# ---------------------------------------------------------------- 3 (Q7)
def _pro_net():
    data = [(2013, 59, 51), (2014, 55, 50), (2015, 44, 68), (2016, 45, 67), (2017, 44, 65)]
    zero, sc = 196, 5
    parts = [line(80, zero, 620, zero, k='ink', w=2)]
    lab = [text(72, zero + 5, '0', k='muted', size=15, anchor='end'),
           text(330, 24, 'professionals out − in (a bar above the line = a loss)', k='ink', size=17)]
    for i, (yr, a, b) in enumerate(data):
        x = 110 + i * 102
        v = b - a
        top = zero - v * sc if v > 0 else zero
        f = 'g' if yr == 2015 else ('p' if v > 0 else 'b')
        parts.append(rect(x, top, 64, abs(v) * sc, k='ink', fill=f, sw=1.6))
        if v > 0:
            lab.append(text(x + 32, zero + 22, yr, k='ink', size=16))
            lab.append(text(x + 32, top - 10, f'{b} − {a} = {v}', k='green' if yr == 2015 else 'ink', size=15,
                            weight='700' if yr == 2015 else None))
        else:
            lab.append(text(x + 32, zero - 10, yr, k='ink', size=16))
            lab.append(text(x + 32, zero + abs(v) * sc + 22, f'{b} − {a} = {v}', k='ink', size=15))
            lab.append(text(x + 32, zero + abs(v) * sc + 42, '(a gain)', k='muted', size=14))
    lab.append(text(110 + 2 * 102 + 32, 52, 'biggest loss', k='green', size=19, font='scrawl'))
    return svg(640, 296, rough(*parts) + ''.join(lab),
               'Bar chart of professionals leaving minus arriving: 2013 minus 8, 2014 minus 5, 2015 plus 24, 2016 plus 22, 2017 plus 21')


def _baytree_table():
    groups = ['total', 'professionals', 'other employed', 'economically inactive']
    ins = [('2017', [174, 92, 82, 44, 32, 12, 33, 19, 14, 97, 41, 56]),
           ('2016', [154, 83, 71, 45, 32, 13, 24, 14, 10, 85, 37, 48]),
           ('2015', [202, 101, 101, 44, 35, 9, 38, 18, 20, 120, 48, 72]),
           ('2014', [201, 107, 94, 55, 40, 15, 36, 21, 15, 110, 46, 64]),
           ('2013', [201, 102, 99, 59, 41, 18, 32, 15, 17, 110, 46, 64])]
    outs = [('2017', [159, 94, 65, 65, 49, 16, 32, 22, 10, 62, 23, 39]),
            ('2016', [232, 132, 100, 67, 50, 17, 60, 38, 22, 105, 44, 61]),
            ('2015', [260, 136, 124, 68, 49, 19, 66, 37, 29, 126, 50, 76]),
            ('2014', [183, 89, 94, 50, 32, 18, 35, 19, 16, 98, 38, 60]),
            ('2013', [165, 80, 85, 51, 32, 19, 35, 16, 19, 79, 32, 47])]

    def sub(label):
        return f'<tr><th><i>{label}</i></th>' + ''.join(f'<th>{c}</th>' for c in 'PMF' * 4) + '</tr>'

    def rows(data):
        out = ''
        for yr, vals in data:
            cells = ''.join(f'<td>{hl(v, "g") if i == 3 else v}</td>' for i, v in enumerate(vals))
            out += f'<tr><td><i>{yr}</i></td>{cells}</tr>'
        return out
    head = '<tr><th></th>' + ''.join(
        f'<th colspan="3"><i>{hl(g, "y", 1) if g == "professionals" else g}</i></th>' for g in groups) + '</tr>'
    return (f'<div class="tbl-wrap"><table class="ptable"><thead>{head}</thead><tbody>'
            f'{sub(hl("in", "p", 2))}{rows(ins)}{sub(hl("out", "p"))}{rows(outs)}</tbody></table></div>')

Q.append(dict(
    n=3, orig=7, answer='C', topic='Reading tables',
    question=f"""<p>Baytree Island’s Council is concerned to retain a balance of skilled professional workers
amongst the population, and monitors migrants in and migrants out on an annual basis. There
is currently some concern about the trend, and the Chief Administration Officer was asked to
prepare a statistical table for the next Council meeting, as shown below:</p>
{_baytree_table()}
<p>Key: {hl('P = persons', 'g', 3)}, M = males, F = females</p>
<p class="stem">In which year did the island have the {hl('greatest overall loss', 'b', 4)} of professionals?</p>""",
    options={'A': '2013', 'B': '2014', 'C': '2015', 'D': '2016', 'E': '2017'},
    notes=[(1, 'y', 'Only the <b>professionals</b> block matters. Ignore the other twelve columns!'),
           (2, 'p', 'Two halves: “in” (arrived) at the top, “out” (left) at the bottom. Careful: the years run 2017 → 2013, downwards.'),
           (3, 'g', 'P is everyone (M + F), so one column does the job.'),
           (4, 'b', '“Overall loss” = left − arrived. Not just the biggest “out” number.')],
    steps=[
        f"""<p>For each year take the professionals P figure: <b>out − in</b>.</p>
{calc('2013: 51 − 59 = −8 (a gain)', '2014: 50 − 55 = −5 (a gain)', '2015: 68 − 44 = <b>24</b>', '2016: 67 − 45 = 22', '2017: 65 − 44 = 21')}""",
        f"""{_pro_net()}
{calc(f'biggest net loss = 24 in {boxed("2015")}')}
{note('2015 also has the biggest “out” (68), but always subtract the “in” too: 2016 and 2017 are only just behind.', 'check')}""",
    ],
    answer_text='2015: 68 professionals left and only 44 arrived, a net loss of 24.',
    why={'A': '2013 is a <b>gain</b>: 59 professionals arrived and only 51 left.',
         'B': '2014 is also a gain (55 in, 50 out).',
         'D': '2016 loses 22: close, but less than 24. It is the year with the biggest loss of <b>all</b> people (232 − 154), which is the trap if you use the total column.',
         'E': '2017 loses 21. Its 65 leavers look large, but 44 arrived.'},
    fast='Professionals P only: out − in = −8, −5, 24, 22, 21 for 2013–2017. Biggest is 2015.',
))

# ---------------------------------------------------------------- 4 (Q8)
def _clock_tops():
    parts, lab = [], []
    lab.append(text(20, 26, 'The top half of each digit (the middle bar is hidden too):', k='ink', size=17, anchor='start'))
    for i, dgt in enumerate('0123456789'):
        x = 34 + i * 60
        top = [s for s in DIG7[dgt] if s in 'abf']
        parts += seg7(x, 46, 26, 56, top, k='ink', sw=4, gap=3)
        parts += seg7(x, 46, 26, 56, [s for s in DIG7[dgt] if s not in 'abf'], k='muted', sw=1.4, gap=3)
        lab.append(text(x + 13, 128, dgt, k='ink', size=18))
    parts.append(rect(20, 75, 600, 34, k='orange', fill='o', sw=1.4))
    lab.append(text(600, 98, 'hoarding', k='orange', size=15, anchor='end'))
    # the clock as seen
    seen = [('b', '1 only'), ('bf', '4 only'), ('af', '5 or 6'), ('ab', '2, 3 or 7')]
    for i, (segs, cand) in enumerate(seen):
        x = 90 + i * 130 + (30 if i >= 2 else 0)
        parts += seg7(x, 168, 40, 84, list(segs), k='pen', sw=6, gap=4)
        lab.append(text(x + 20, 284, cand, k='pen', size=17))
    parts.append(rect(60, 210, 560, 46, k='orange', fill='o', sw=1.4))
    lab += [text(110, 240, 'hoarding', k='orange', size=15),
            text(20, 160, 'What I could see at Carlisle:', k='ink', size=17, anchor='start'),
            text(350, 316, 'hour 14, minutes 52, 53 or 57 → about 15:00', k='red', size=19, font='scrawl')]
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'Top halves of the digits 0 to 9, then the four visible tops at Carlisle: 1, 4, 5, and 2, 3 or 7')

Q.append(dict(
    n=4, orig=8, answer='C', topic='Digital displays',
    question=f"""<p>Most railway stations have digital clocks that display the time in {hl('24-hour format', 'y', 1)}. I recently
undertook a train journey from Exeter to Aberdeen. As the train left Exeter, the clock on the
platform showed:</p>
{fig(Y, 'ps_q04_clock1', 'Digital clock showing 08:34', 220)}
<p>I lost track of time as I read a book and then dozed. I eventually became aware of the train
coming to rest and the guard announcing ‘Carlisle’.</p>
<p>I opened my eyes, and found that I could {hl('only see the top of the platform clock', 'p', 2)} (because of the
hoarding in the way) as follows:</p>
{fig(Y, 'ps_q04_clock2', 'Only the top half of the clock: one stroke, two strokes, a top bar with a left stroke, a top bar with a right stroke', 270)}
<p class="stem">Approximately what time was it, {hl('to the nearest hour', 'b', 3)}, when the train stopped at Carlisle?</p>""",
    options={'A': '1 o’clock', 'B': '2 o’clock', 'C': '3 o’clock', 'D': '4 o’clock', 'E': '5 o’clock'},
    notes=[(1, 'y', 'So the afternoon shows as 13, 14, 15…'),
           (2, 'p', 'Each digit only shows its top bar and two upper side strokes. Use the 08:34 clock to see how each digit is built (look at its 3 and 4).'),
           (3, 'b', 'Round the time you decode to the nearest hour. Don’t forget the minutes!')],
    steps=[
        f"""<p>Work out what the top half of every digit looks like, then match the four tops on the Carlisle clock:</p>{_clock_tops()}""",
        f"""{calc('1st digit: just a right-hand stroke → 1', '2nd digit: two side strokes, no top bar → 4 (just like the 4 in 08:34)',
                  '3rd digit: top bar + left stroke → 5 or 6, but minutes only go to 5 → 5',
                  '4th digit: top bar + right stroke → 2, 3 or 7')}
{calc(f'time = 14:52, 14:53 or 14:57 {ar()} nearest hour 15:00 = {boxed("3 o’clock")}')}
{note('Sense check: left Exeter at 08:34, reached Carlisle about 6½ hours later. Mid-afternoon is believable.', 'check')}""",
    ],
    answer_text='3 o’clock: the clock reads 14:5_, which rounds to 15:00.',
    why={'A': '1 o’clock would need 12:30 to 13:29. The tops of 2 and 3 have a top bar, which isn’t there.',
         'B': '2 o’clock reads the hour as 14 = 2 pm but forgets the minutes are in the 50s, which round up to 3.',
         'D': '4 o’clock reads the second digit, 4, as the hour and ignores the 1 in front (24-hour clock).',
         'E': '5 o’clock takes the minutes digit 5 as the hour.'},
    fast='Tops: 1, 4, 5, then 2/3/7. So 14:5x, which is nearly 15:00: 3 o’clock.',
))

# ---------------------------------------------------------------- 5 (Q12)
def _shares():
    vals = [('2011', 3.00), ('2012', 4.20), ('2013', 6.30), ('2014', 9.45), ('2015', 15.12), ('2016', 22.68)]
    pct = ['+40%', '+50%', '+50%', '+60%', '+50%']
    mult = ['×1.4', '×1.5', '×1.5', '×1.6', '×1.5']
    parts, lab = [], []
    base = 200
    for i, (yr, v) in enumerate(vals):
        x = 40 + i * 104
        h = v * 7
        f = 'g' if yr in ('2014', '2015') else 'b'
        parts.append(rect(x, base - h, 56, h, k='ink', fill=f, sw=1.5))
        lab.append(text(x + 28, base + 22, yr, k='ink', size=16))
        lab.append(text(x + 28, base - h - 8, f'£{v:.2f}', k='ink', size=15))
        if i:
            mx = x - 24
            hot = i == 4
            parts.append(arrow(mx - 34, base + 40, mx + 34, base + 40, k='green' if hot else 'red', bend=-0.2))
            lab.append(text(mx, base + 70, pct[i - 1], k='green' if hot else 'red', size=18, weight='700' if hot else None))
            lab.append(text(mx, base + 90, mult[i - 1], k='muted', size=14))
    lab.append(text(40 + 4 * 104 - 24, 24, 'biggest jump: 2014 → 2015', k='green', size=18, font='scrawl'))
    return svg(660, 300, rough(*parts) + ''.join(lab),
               'Share values each year with the growth between: plus 40, 50, 50, 60 and 50 percent; the 60 percent jump is 2014 to 2015')

Q.append(dict(
    n=5, orig=12, answer='D', topic='Percentage change',
    question=f"""<p>Below is a table showing the value of Lucy’s shares. They started at £3.00 in 2011 and in 2016
they were worth £22.68.</p>
{table([['2011', '£3.00'], ['2012', '£4.20'], ['2013', '£6.30'], ['2014', hl('£9.45', 'g')], ['2015', hl('£15.12', 'g')], ['2016', hl('£22.68', 'p', 2)]],
       head=['<i>year</i>', '<i>share value</i>'])}
<p class="stem">When did Lucy’s shares have the {hl('biggest percentage increase', 'b', 1)}?</p>""",
    options={'A': '2011–2012', 'B': '2012–2013', 'C': '2013–2014', 'D': '2014–2015', 'E': '2015–2016'},
    notes=[(1, 'b', '<b>Percentage</b> increase = rise ÷ starting value. Compare the multipliers, not the pounds.'),
           (2, 'p', 'Trap: the last jump is the biggest in pounds (£7.56), but it is from a big starting value.')],
    steps=[
        f"""<p>Find each year’s multiplier (new ÷ old). Quick trick: find the rise as a fraction of the old value.</p>
{calc('3.00 → 4.20: rise 1.20 = 0.4 × 3.00 → <b>+40%</b>', '4.20 → 6.30: rise 2.10 = half of 4.20 → <b>+50%</b>',
      '6.30 → 9.45: rise 3.15 = half of 6.30 → <b>+50%</b>', '9.45 → 15.12: rise 5.67 = 0.6 × 9.45 → <b>+60%</b>',
      '15.12 → 22.68: rise 7.56 = half of 15.12 → <b>+50%</b>')}
{note('0.6 × 9.45: 9.45 × 6 = 56.70, then ÷ 10 = 5.67. Exactly the rise!', 'tip')}""",
        f"""{_shares()}
{calc(f'biggest percentage rise: 60% in {boxed("2014–2015")}')}""",
    ],
    answer_text='2014–2015: the value went up by 60% (from £9.45 to £15.12).',
    why={'A': '2011–2012 is +40%, the smallest.',
         'B': '2012–2013 is +50%.',
         'C': '2013–2014 is +50%.',
         'E': '2015–2016 is the biggest rise <b>in pounds</b> (£7.56), but only +50% because it started from £15.12.'},
    fast='Halve the old value and add it on: that gives 6.30, 9.45 and 22.68 exactly, so those are +50%. 9.45 → 15.12 is more than half again (+60%). D.',
))

# ---------------------------------------------------------------- 6 (Q13)
def _wallpaper():
    rows = [('woodchip', 550), ('vymura', 567), ('anaglypta', 576), ('embossed', 525), ('fabric effect', 600)]
    X = lambda v: 160 + (v - 450) * 2.6
    parts, lab = [line(X(450), 22, X(450), 214, k='ink', w=2)], []
    for i, (name, v) in enumerate(rows):
        y = 30 + i * 36
        f = 'g' if name == 'embossed' else 'b'
        parts.append(rect(X(450), y, X(v) - X(450), 24, k='ink', fill=f, sw=1.5))
        lab.append(text(150, y + 18, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 8, y + 18, f'£{v}', k='green' if name == 'embossed' else 'ink', size=16, anchor='start'))
    lab.append(text(X(525) + 60, 30 + 3 * 36 + 18, '← cheapest', k='green', size=18, font='scrawl', anchor='start'))
    lab.append(text(X(450), 234, 'bars start at £450', k='muted', size=14, anchor='start'))
    return svg(640, 244, rough(*parts) + ''.join(lab),
               'Total cost for 54 m: woodchip 550, vymura 567, anaglypta 576, embossed 525, fabric effect 600 pounds')

Q.append(dict(
    n=6, orig=13, answer='D', topic='Best deal',
    question=f"""<p>I am redecorating my house and need to buy wallpaper for one of the rooms. I need to buy
{hl('54 m', 'g', 1)} of wallpaper in total and want to pay the lowest price. The table below shows the details
of the five types of wallpaper I want to choose between.</p>
{table([['woodchip', '2 m', '£25', hl('every fifth roll is free', 'p', 2)],
        ['vymura', '3 m', '£35', hl('10% discount for orders over £500', 'y', 3)],
        ['anaglypta', '3 m', '£40', '20% discount for orders over £500'],
        ['embossed', '4 m', '£50', '25% discount on all orders'],
        ['fabric effect', '5 m', '£100', hl('buy one, get one free', 'p', 4)]],
       head=['<i>wallpaper type</i>', '<i>roll length</i>', '<i>cost per roll</i>', '<i>special offers</i>'])}
<p class="stem">Which type of wallpaper should I choose?</p>""",
    options={'A': 'woodchip', 'B': 'vymura', 'C': 'anaglypta', 'D': 'embossed', 'E': 'fabric effect'},
    notes=[(1, 'g', 'Rolls needed = 54 ÷ roll length, <b>rounded up</b> (you can’t buy part of a roll).'),
           (2, 'p', 'In every 5 rolls you pay for 4.'),
           (3, 'y', 'Check the order really is over £500 before taking the discount.'),
           (4, 'p', 'Pay for half the rolls (rounding up if the number is odd).')],
    steps=[
        f"""<p>Rolls needed for 54 m, then the price after the offer:</p>
{calc('woodchip: 54 ÷ 2 = 27 rolls; 5 are free → pay for 22 × £25 = <b>£550</b>',
      'vymura: 54 ÷ 3 = 18 rolls × £35 = £630 → less 10% = <b>£567</b>',
      'anaglypta: 18 rolls × £40 = £720 → less 20% = <b>£576</b>',
      'embossed: 54 ÷ 4 = 13.5 → <b>14</b> rolls × £50 = £700 → less 25% = <b>£525</b>',
      'fabric: 54 ÷ 5 = 10.8 → <b>11</b> rolls → pay for 6 × £100 = <b>£600</b>')}
{note('25% off is the same as × ¾: 700 ÷ 4 = 175, × 3 = 525.', 'tip')}""",
        f"""{_wallpaper()}
{calc(f'cheapest = {boxed("embossed")}, £525')}""",
    ],
    answer_text='Embossed: 14 rolls for £700, less 25%, is £525.',
    why={'A': 'Woodchip costs £550 (27 rolls, 5 free). Close, but £25 more.',
         'B': 'Vymura costs £567 after its 10% discount.',
         'C': 'Anaglypta costs £576 after its 20% discount.',
         'E': 'Fabric effect costs £600 (pay for 6 of the 11 rolls). If you forget to round 10.8 up to 11 you might think it’s cheaper.'},
    fast='Rolls: 27, 18, 18, 14, 11. Prices: 550, 567, 576, 525, 600. Embossed wins.',
))

# ---------------------------------------------------------------- 7 (Q14)
def _book():
    parts, lab = [], []
    # one block of 8 folded sheets seen from the top
    cx, top = 150, 40
    for i in range(8):
        w = 22 + i * 13
        parts.append(path(f'M{cx - w} 230 C{cx - w} {120 - i * 4}, {cx - 4} {top + 30}, {cx} {top + 22} '
                          f'C{cx + 4} {top + 30}, {cx + w} {120 - i * 4}, {cx + w} 230', k='ink', sw=1.6))
    parts.append(line(cx, top, cx, top + 30, k='red', w=5))
    lab += [text(cx, top - 10, 'stitching', k='red', size=16),
            text(cx - 4, 214, '16', k='red', size=17, anchor='end', weight='700'), text(cx + 4, 214, '17', k='red', size=17, anchor='start', weight='700'),
            text(cx, 258, '1 block: 8 sheets', k='ink', size=16), text(cx, 278, '= 16 leaves = 32 pages', k='ink', size=16),
            text(cx, 300, 'innermost sheet = pages 16 | 17', k='red', size=16)]
    # number line of the three blocks
    X = lambda p: 320 + p * 3.3
    for b, f in ((0, 'b'), (1, 'o'), (2, 'b')):
        parts.append(rect(X(b * 32), 120, 32 * 3.3, 34, k='ink', fill=f, sw=1.6))
        mid = b * 32 + 16
        parts.append(line(X(mid), 108, X(mid), 166, k='red', w=2.6))
        lab.append(text(X(mid), 188, f'{mid}|{mid + 1}', k='red', size=17, weight='700' if b == 1 else None))
        lab.append(text(X(b * 32) + 6, 142, f'{b * 32 + 1}', k='ink', size=13, anchor='start'))
        lab.append(text(X(b * 32 + 32) - 6, 142, f'{b * 32 + 32}', k='ink', size=13, anchor='end'))
    lab += [text(X(48), 96, 'centres every 32 pages', k='ink', size=16),
            text(X(48), 216, 'only these pairs show the stitching', k='red', size=16, font='scrawl')]
    return svg(640, 312, rough(*parts) + ''.join(lab),
               'One block of eight folded sheets with the stitching between pages 16 and 17; blocks run 1 to 32, 33 to 64, 65 to 96 with centres 16|17, 48|49, 80|81')

Q.append(dict(
    n=7, orig=14, answer='C', topic='Folding & page order',
    question=f"""<p>The diagram below shows the method of construction of a book with four {hl('folded sheets', 'y', 1)} in each
block, and three blocks in total. Page one is the first page of the first block of four sheets. At the
centre of each block, you can see the stitching that binds the book together.</p>
{fig(Y, 'ps_q07_book', 'Three blocks of folded sheets side by side, each stitched at its centre fold', 300)}
<p>A book is to be made using the same technique but with {hl('eight sheets of paper in each of the three blocks', 'g', 2)}.</p>
<p class="stem">Which of the following pairs of pages could be {hl('in the centre of a block', 'b', 3)} (that is, if opened there,
the stitching would be visible)?</p>""",
    options={'A': '46 and 47', 'B': '47 and 48', 'C': '48 and 49', 'D': '63 and 64', 'E': '64 and 65'},
    notes=[(1, 'y', 'One sheet folded in half = 2 leaves = <b>4 pages</b> (front and back of each leaf).'),
           (2, 'g', '8 sheets × 4 pages = 32 pages per block; 96 pages in the book.'),
           (3, 'b', 'The centre is the middle of a block’s pages, not the gap between two blocks.')],
    steps=[
        f"""<p>Pages per block: 8 sheets × 4 = <b>32</b>. So the blocks are pages 1–32, 33–64 and 65–96.</p>""",
        f"""<p>The middle of 32 pages is between the 16th and 17th page of the block:</p>{_book()}
{calc('block 1: 16 | 17', 'block 2: 32 + 16 = 48 | 49', 'block 3: 64 + 16 = 80 | 81', f'in the list: {boxed("48 and 49")}')}
{note('A spread always has an even page on the left and the next odd page on the right. 47|48 and 63|64 are the two sides of one leaf, so you can never see them together.', 'check')}""",
    ],
    answer_text='48 and 49: the middle of the second block (pages 33 to 64).',
    why={'A': '46 and 47 do face each other in block 2, but one leaf before the centre. The stitching is between 48 and 49.',
         'B': '47 and 48 are the front and back of the same leaf, so they can’t be seen as an open pair.',
         'D': '63 and 64 are the two sides of one leaf too, near the end of block 2.',
         'E': '64 and 65 is where block 2 ends and block 3 starts: the join between blocks, not the stitched centre.'},
    fast='8 sheets = 32 pages a block. Centres at 16|17, 48|49, 80|81. Only 48 and 49 is listed.',
))

# ---------------------------------------------------------------- 8 (Q18)
def _buckets():
    parts, lab = [], []

    def bucket(x, before, change, after, col, name):
        parts.append(path(f'M{x} 96 L{x + 12} 200 L{x + 68} 200 L{x + 80} 96', k='ink', sw=2))
        parts.append(path(f'M{x} 96 Q{x + 40} 70 {x + 80} 96', k='muted', sw=1.4))
        lab.append(text(x + 40, 128, before, k=col, size=22, font='scrawl'))
        lab.append(text(x + 40, 154, change, k='red', size=18))
        lab.append(text(x + 40, 186, after, k='green', size=22, font='scrawl'))
        lab.append(text(x + 40, 224, name, k='ink', size=15))

    for i in range(4):
        bucket(20 + i * 110, '22', '− 3', '= 19', 'pen', f'girl {i + 1}')
        parts.append(arrow(60 + i * 110, 80, 515, 78, k='red', bend=-0.32 + i * 0.07))
    bucket(480, '?', '+ 12', '= 19', 'red', 'youngest')
    lab += [text(320, 256, 'each of the 4 gives her 3 shells: 4 × 3 = 12', k='red', size=17),
            text(320, 284, 'everyone ends equal on 19, so ? = 19 − 12 = 7', k='green', size=19, font='scrawl')]
    return svg(640, 298, rough(*parts) + ''.join(lab),
               'Four buckets of 22 shells each give 3 to the youngest and end on 19; the youngest gets 12 and also ends on 19, so she had 7')

Q.append(dict(
    n=8, orig=18, answer='B', topic='Working backwards',
    question=f"""<p>Five girls are collecting shells on a beach. They are putting them in {hl('buckets that each hold 24 shells', 'g', 1)}. At the end of the collecting time, they are going to ensure that they {hl('all have the same number of shells', 'y', 2)}. {hl('Four of them are only two short of filling their bucket', 'g', 3)}, but the youngest one is
lagging behind with her total. {hl('Each of the others give her three shells', 'p', 4)} from their buckets in
order to equalise the numbers collected.</p>
<p class="stem">How many shells did the youngest girl {hl('collect for herself', 'b', 5)}?</p>""",
    options={'A': '4', 'B': '7', 'C': '10', 'D': '12', 'E': '19'},
    notes=[(1, 'g', 'Full bucket = 24.'),
           (2, 'y', 'After the sharing, all five have the same number.'),
           (3, 'g', '24 − 2 = 22 each for the four older girls.'),
           (4, 'p', '<b>Each</b> of the four gives 3, so the youngest receives 4 × 3 = 12.'),
           (5, 'b', 'Her own number <b>before</b> the gifts.')],
    steps=[
        f"""{_buckets()}""",
        f"""{calc('older girls: 22 − 3 = 19 each', 'so the youngest also ends with 19',
                  'she received 4 × 3 = 12', f'her own shells = 19 − 12 = {boxed("7")}')}
{note('Check: 4 × 22 + 7 = 95 shells, and 95 ÷ 5 = 19 each. ✓', 'check')}""",
    ],
    answer_text='7 shells: she ends with 19 after receiving 12.',
    why={'A': '4 = 19 − 15: it counts five girls giving 3 shells, but only four girls give.',
         'C': '10 = 22 − 12: it uses the others’ total <b>before</b> they gave shells away.',
         'D': '12 is how many shells she was <b>given</b>, not how many she collected.',
         'E': '19 is what everyone ends up with after the sharing.'},
    fast='Others end on 22 − 3 = 19. She got 12, so she had 19 − 12 = 7.',
))
