from wslib import *

Y = 2009
Q = []
R3 = 3 ** 0.5


# ---------------------------------------------------------------- 17 (Q36)
def _rowing():
    bw, x0 = 52, 120
    rows = [('first', [(4, 10, 'b')], '= 40'), ('second', [(6, 11, 'o')], '= 66'),
            ('third', [(5, 12, 'v'), (3, 8, 'g')], '= 60 + 24 = 84')]
    parts, lab = [], []
    lab.append(text(x0, 24, 'each block = 100 m; the number = calories for that 100 m', k='muted', size=15, anchor='start'))
    for i, (name, segs, tot) in enumerate(rows):
        y = 44 + i * 70
        x = x0
        for n, cal, f in segs:
            for _ in range(n):
                parts.append(rect(x + 2, y, bw - 4, 36, k='ink', fill=f, sw=1.4))
                lab.append(text(x + bw / 2, y + 24, cal, k='ink', size=16))
                x += bw
        lab.append(text(x0 - 12, y + 24, name, k='ink', size=17, anchor='end'))
        lab.append(text(x + 8, y + 25, tot, k='red', size=18, font='scrawl', anchor='start'))
    y3 = 44 + 2 * 70 + 40
    parts += [brace(x0 + 2, x0 + 5 * bw - 2, y3, '', k='violet'), brace(x0 + 5 * bw + 2, x0 + 8 * bw - 2, y3, '', k='green')]
    lab += [text(x0 + 2.5 * bw, y3 + 34, 'first 500 m: 60 ÷ 5 = 12 each', k='violet', size=15),
            text(x0 + 6.5 * bw, y3 + 34, '300 m: 40 ÷ 5 = 8 each', k='green', size=15)]
    return svg(640, 268, rough(*parts) + ''.join(lab),
               'Rowing sessions split into 100 m blocks: 4 blocks of 10, 6 blocks of 11, then 5 blocks of 12 and 3 blocks of 8, totalling 190')


Q.append(dict(
    n=17, orig=36, answer='B', topic='Reading displays & rates',
    question=f"""<p>The rowing machine in our gym has a display that tells the user how much work they
have done. The display shows the following information:</p>
{table([['1', 'distance rowed since starting', ''],
        ['2', f"number of calories used {hl('per 500 m', 'y', 1)} rowing", '(an average update every 15 seconds)'],
        ['3', 'time since starting', ''],
        ['4', 'number of rowing strokes per minute', '(an average update every 30 seconds)']])}
<p>Today I have used the machine {hl('three times', 'g', 2)}, each time as part of a circuit of training using
several machines in the gym. During my third session, {hl('I re-set the counter after rowing 500 m', 'p', 3)}.</p>
{table([['first', '400 m', '50'], ['second', '600 m', '55'], ['third', hl('800 m', 'p'), '60 for the first 500 m'],
        ['', '', '40 for remainder']], head=['', '<i>distance rowed</i>', '<i>number of calories used per 500 m</i>'])}
<p class="stem">How many calories did I use up on the rowing machine?</p>""",
    options={'A': '155', 'B': '190', 'C': '205', 'D': '206', 'E': '260'},
    notes=[(1, 'y', 'It’s a <b>rate</b>: calories for every 500 m, not the total. Scale it to the distance actually rowed.'),
           (2, 'g', 'Add up all three sessions.'),
           (3, 'p', 'The third session (800 m) is split: the first 500 m at one rate, the other 800 − 500 = 300 m at another.')],
    steps=[
        f"""<p>Calories = rate per 500 m × (distance ÷ 500):</p>
{calc('first: 400 m is 0.8 of 500 → 0.8 × 50 = 40', 'second: 600 m is 1.2 of 500 → 1.2 × 55 = 66',
      'third, first part: 500 m → 60', 'third, rest: 300 m is 0.6 of 500 → 0.6 × 40 = 24')}""",
        f"""<p>Or chop everything into 100 m blocks (a fifth of 500 m):</p>{_rowing()}""",
        f"""{calc(f'40 + 66 + 60 + 24 = {boxed("190")}')}
{note('Per 100 m is easy: 50 per 500 m is 10 per 100 m, so 400 m = 4 × 10 = 40.', 'tip')}""",
    ],
    answer_text='190 calories: 40 + 66 + (60 + 24).',
    why={'A': '155 = 50 + 55 + 50: treats every session as exactly 500 m (averaging 60 and 40 for the third).',
         'C': '205 = 50 + 55 + 60 + 40: adds the display numbers as if they were totals. They are per 500 m.',
         'D': '206 = 40 + 66 + 60 + 40: right for the first two, but counts the last 300 m as a full 500 m.',
         'E': '260 = 50 + 110 + 60 + 40: rounds every part of 500 m up to a whole 500 m.'},
    fast='Per 100 m: 10, 11, 12 and 8 calories. 4 × 10 + 6 × 11 + 5 × 12 + 3 × 8 = 40 + 66 + 60 + 24 = 190.',
))


# ---------------------------------------------------------------- 18 (Q37)
def _sightlines():
    g = 250
    parts = [line(20, g, 630, g, k='ink', w=2),
             rect(520, 50, 56, 200, k='ink', fill='b', sw=2),
             rect(520, 180, 92, 70, k='ink', fill='o', sw=2),
             line(26, g, 26, 170, k='ink', w=2), rect(16, 200, 10, 30, k='ink', fill='paper', sw=1.6),
             line(40, g - 2, 520, 180, k='orange', w=2.2, dash=True),
             line(40, g - 2, 520, 50, k='pen', w=2.2, dash=True),
             circle(150, 242, 8, k='green', fill='g', sw=2),
             line(150, g, 150, 222, k='green', w=3),
             circle(150, 214, 10, k='green', fill='g', sw=2),
             brace(152, 518, 262, '', k='muted')]
    lab = [eye(40, 238, facing='right'),
           text(150, 298, 'shrub 1.6 m', k='green', size=15),
           text(140, 178, 'tree ≈ 4.6 m', k='green', size=16),
           text(44, 274, 'her eye', k='muted', size=14),
           text(566, 222, 'bungalow', k='ink', size=14),
           text(566, 240, '7 m', k='ink', size=15),
           text(548, 100, 'flats', k='ink', size=15),
           text(548, 120, '20 m', k='ink', size=15),
           text(335, 300, '30 m', k='muted', size=16),
           text(300, 40, 'same place, so same scale:', k='red', size=18, font='scrawl'),
           text(300, 64, '20 ÷ 7 × 1.6 ≈ 4.6 m', k='red', size=18, font='scrawl')]
    return svg(640, 316, rough(*parts) + ''.join(lab),
               'Side view: sight lines from her eye skim the shrub to the bungalow top and a taller tree to the top of the flats')


Q.append(dict(
    n=18, orig=37, answer='D', topic='Similar triangles',
    question=f"""<p>When Mrs Brown looks out of her back room window, a {hl('bungalow 7m high', 'g', 1)} and 30m
beyond her garden fence is {hl('just obscured', 'y', 2)} by a shrub in her hedge which is {hl('1.6m high', 'g', 3)}.
She wants to choose a tree to plant {hl('beside the shrub', 'y', 4)} which, when fully grown, will have
the same effect on a small block of {hl('flats 20m high', 'g', 5)} beside the bungalow. However, she
{hl('does not want it to be much bigger than necessary', 'p', 6)} or it will block out her light.</p>
<p>The characteristics of some trees are shown below:</p>
{table([['<i>Copper Beech</i>', 'Copper red leaves', 'average', '20.0', '13.0'],
        ['<i>Flowering cherry</i>', 'Beautiful blossom', 'vigorous', '10.0', '8.0'],
        ['<i>Hawthorn</i>', 'Rugged and sturdy', 'average', '8.0', '5.2'],
        ['<i>Holly</i>', 'Shiny green leaves', 'slow', '7.0', '3.2'],
        ['<i>Hornbeam</i>', 'Silvery leaves', 'average', '4.8', '3.8'],
        ['<i>Japanese Maple</i>', 'Red autumn leaves', 'slow', '4.0', '4.2'],
        ['<i>Mountain Ash</i>', 'Bright red berries', 'average', '4.5', '2.5'],
        ['<i>Sycamore</i>', 'Dense foliage', 'vigorous', '13.5', '9.5']],
       head=['<i>Tree</i>', '<i>Features</i>', '<i>Growth</i>', hl('<i>Height (m)</i>', 'g', 7), '<i>Width (m)</i>'])}
<p class="stem">Which of the trees above would be her best choice?</p>""",
    options={'A': 'Copper Beech', 'B': 'Hawthorn', 'C': 'Holly', 'D': 'Hornbeam', 'E': 'Mountain Ash'},
    notes=[(1, 'g', 'The bungalow is 7 m tall.'),
           (2, 'y', '“Just obscured”: her line of sight skims the top of the shrub and lands exactly on the top of the bungalow.'),
           (3, 'g', 'The shrub is 1.6 m tall.'),
           (4, 'y', 'The tree stands where the shrub is, and the flats stand where the bungalow is. Same distances, so it’s a scale-up.'),
           (5, 'g', 'The flats are 20 m tall.'),
           (6, 'p', 'Choose the <b>smallest</b> tree that is tall enough, not just any tall tree.'),
           (7, 'g', 'Only height matters for hiding the flats.')],
    steps=[
        f"""<p>Draw it from the side. Her sight lines fan out from her eye like the sides of a triangle:</p>{_sightlines()}""",
        f"""<p>The tree is at the shrub’s spot and the flats are at the bungalow’s spot, so heights scale by the same factor:</p>
{calc('flats ÷ bungalow = 20 ÷ 7', 'tree = 1.6 × 20 ÷ 7 = 32 ÷ 7 ≈ 4.6 m')}
{note('32 ÷ 7: 7 × 4.5 = 31.5, so 32 ÷ 7 is a little over 4.5 (about 4.57).', 'tip')}""",
        f"""<p>Now the shortest tree that reaches about 4.6 m:</p>
{calc(f'Mountain Ash 4.5 m {cross()} just too short', f'Hornbeam 4.8 m {tick()} just enough',
      f'Holly 7.0, Hawthorn 8.0, Copper Beech 20.0 {ar()} far bigger than needed')}
{calc(f'best choice {ar()} {boxed("Hornbeam")}')}
{note('No window height or hedge distance is given, so the simple model is the one to use: sight lines from one low point, and heights at the hedge scale like heights at the buildings.', 'check')}""",
    ],
    answer_text='Hornbeam: the tree must be about 1.6 × 20/7 ≈ 4.6 m, and Hornbeam (4.8 m) is the smallest that is tall enough.',
    why={'A': 'Copper Beech (20 m) matches the flats’ height, but the tree is much closer to her, so it needs to be far shorter. Much bigger than necessary.',
         'B': 'Hawthorn (8 m) would work but is much bigger than needed, blocking her light.',
         'C': 'Holly (7 m) copies the bungalow’s height. Tall enough, but much bigger than necessary.',
         'E': 'Mountain Ash (4.5 m) is just short of the 4.57 m needed, so the top of the flats would peep over.'},
    fast='Scale the shrub: 1.6 × 20/7 ≈ 4.6 m. Smallest tree at least that tall: Hornbeam (4.8 m).',
))


# ---------------------------------------------------------------- 19 (Q38)
def _ratio():
    parts, lab = [], []
    panels = [('NI price stays the same', [(1980, 100, 100), (1981, 130, 100)]),
              ('NI price goes UP', [(1980, 100, 100), (1981, 160, 123)])]
    base = 236
    for i, (title, groups) in enumerate(panels):
        x0 = 40 + i * 310
        lab.append(text(x0 + 130, 30, title, k='red', size=19, font='scrawl'))
        for j, (yr, uk, ni) in enumerate(groups):
            gx = x0 + 40 + j * 130
            parts.append(rect(gx, base - uk, 34, uk, k='ink', fill='b', sw=1.6))
            parts.append(rect(gx + 40, base - ni, 34, ni, k='ink', fill='o', sw=1.6))
            lab.append(text(gx + 17, base - uk - 6, uk, k='pen', size=15))
            lab.append(text(gx + 57, base - ni - 6, ni, k='orange', size=15))
            lab.append(text(gx + 37, base + 22, yr, k='ink', size=16))
            lab.append(text(gx + 37, base + 46, f'{round(100 * ni / uk)}%', k='red', size=19, font='scrawl'))
        parts.append(line(x0, base, x0 + 270, base, k='ink', w=2))
    lab += [text(320, 304, 'blue = UK price, orange = NI price, red = what the graph shows (NI ÷ UK)', k='ink', size=15),
            text(320, 326, 'Both give the same drop from 100% to 77%!', k='red', size=16)]
    return svg(640, 338, rough(*parts) + ''.join(lab),
               'Two made-up examples: NI prices flat or NI prices rising, but UK prices rising faster, both give a ratio falling from 100 to 77 per cent')


Q.append(dict(
    n=19, orig=38, answer='D', topic='Graphs & ratios',
    question=f"""<p>The graph below shows Northern Ireland house prices {hl('as a percentage of the UK average', 'y', 1)} (1980=100%) for the period 1980 to 1986.</p>
{fig(Y, 'ps_q19_graph', 'Line graph of NI house price as a percentage of UK house price: 100 in 1980, about 77 in 1981, 82 in 1982, 75 in 1984, 76 in 1985, 72 in 1986', 330)}
<p class="stem">Which one of the following pieces of information {hl('can be inferred', 'b', 2)} from the graph above?</p>""",
    options={'A': 'House prices in Northern Ireland fell by almost 30% in the period shown.',
             'B': 'House prices in Northern Ireland rose in some years and fell in others.',
             'C': 'Average house prices in the UK (outside Northern Ireland) have risen over the period shown.',
             'D': 'In some years average prices in Northern Ireland rose compared to those in the UK as a whole.',
             'E': 'House prices in Northern Ireland had peaked in 1980'},
    notes=[(1, 'y', 'The line is NI price ÷ UK price. It shows how NI <b>compares</b> with the UK, not what either price actually did.'),
           (2, 'b', 'It must follow for certain from the graph alone.')],
    steps=[
        f"""<p>The graph is a <b>ratio</b>. If it falls, NI prices might have fallen, stayed the same, or even risen, as long as UK prices rose faster.
Two made-up examples give exactly the same graph:</p>{_ratio()}""",
        f"""<p>So any option about actual NI prices or actual UK prices can’t be inferred. Only comparisons can:</p>
{calc(f'A: the <b>ratio</b> fell about 28%, not NI prices {cross()}', f'B: actual NI prices: unknown {cross()}',
      f'C: actual UK prices: unknown {cross()}',
      f'D: 1981 → 1982 (77% → 82%) and 1984 → 1985 (75% → 76%) the ratio rose {tick()}',
      f'E: 1980 is the top of the ratio, not necessarily of NI prices {cross()}')}
{calc(f'only D compares NI with the UK {ar()} {boxed("D")}')}""",
    ],
    answer_text='D: the line rises in 1981–82 and 1984–85, so in those years NI prices rose compared with the UK.',
    why={'A': 'The ratio fell from 100% to about 72%, but NI prices themselves might have stayed the same or risen while UK prices rose faster.',
         'B': 'The graph never shows NI prices on their own, so you can’t tell when they rose or fell.',
         'C': 'Probably true in real life, but this graph only shows a ratio. It can’t show UK prices on their own.',
         'E': '1980 is the peak of the ratio only. NI prices could have kept rising after 1980.'},
    fast='It’s a ratio graph: only a statement comparing NI with the UK can be inferred. That’s D (the line goes up twice).',
))


# ---------------------------------------------------------------- 20 (Q42)
def _lotto():
    parts, lab = [], []
    cw, ch, x0, y0 = 48, 40, 20, 30
    for t in range(5):
        for u in range(10):
            n = 10 * t + u
            if n == 0:
                continue
            mult = n % 3 == 0
            dig = any(d in '369' for d in str(n))
            f = 'b' if mult else ('o' if dig else 'paper')
            x, y = x0 + u * cw, y0 + t * ch
            parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='ink' if (mult or dig) else 'muted', fill=f, sw=1.3))
            lab.append(text(x + cw / 2, y + 27, n, k='ink', size=16, font='print'))
    lx = x0 + 10 * cw + 16
    parts += [rect(lx, 40, 22, 22, k='ink', fill='b', sw=1.3), rect(lx, 100, 22, 22, k='ink', fill='o', sw=1.3)]
    lab += [text(lx + 30, 50, 'multiple', k='ink', size=15, anchor='start'), text(lx + 30, 68, 'of 3 = 16', k='ink', size=15, anchor='start'),
            text(lx + 30, 110, 'has 3, 6 or 9', k='ink', size=15, anchor='start'), text(lx + 30, 128, '= 15 more', k='ink', size=15, anchor='start'),
            text(lx + 6, 180, 'total 31', k='red', size=22, font='scrawl', anchor='start')]
    return svg(650, 236, rough(*parts) + ''.join(lab),
               'Grid of 1 to 49 in rows of ten: 16 multiples of 3 in blue and 15 more numbers containing a 3, 6 or 9 in orange')


Q.append(dict(
    n=20, orig=42, answer='E', topic='Counting',
    question=f"""<p>To take part in the National Lottery, entrants must select six different numbers {hl('between 1 and 49 inclusive', 'g', 1)}.</p>
<p>My mother asked me to buy a National Lottery ticket for her. "Choose any six numbers
you like," she said, "but make sure that each one is {hl('a multiple of 3', 'y', 2)}, {hl('or contains a 3, or 6 or 9', 'y', 3)}."</p>
<p class="stem">How many numbers can I choose from?</p>""",
    options={'A': '15', 'B': '16', 'C': '22', 'D': '25', 'E': '31'},
    notes=[(1, 'g', '1 to 49, both included.'),
           (2, 'y', '3, 6, 9, … 48: that’s 48 ÷ 3 = 16 numbers.'),
           (3, 'y', 'Also any number with a digit 3, 6 or 9, like 13, 16, 19 or 31. “Or” means either rule will do, but don’t count a number twice.')],
    steps=[
        f"""{calc('multiples of 3: 3, 6, … 48 → 48 ÷ 3 = 16 numbers')}""",
        f"""<p>Now add the numbers with a 3, 6 or 9 digit that are <b>not</b> already multiples of 3:</p>
{calc('ending in 3, 6 or 9: 13, 16, 19, 23, 26, 29, 43, 46, 49 = 9 (33, 36, 39 already counted)',
      'in the thirties: 31, 32, 34, 35, 37, 38 = 6 (30, 33, 36, 39 already counted)')}
{_lotto()}""",
        f"""{calc(f'16 + 9 + 6 = {boxed("31")}')}
{note('Write 1 to 49 in rows of ten: the 3, 6 and 9 columns and the whole thirties row light up at once.', 'tip')}""",
    ],
    answer_text='31 numbers: 16 multiples of 3, plus 15 more that contain a 3, 6 or 9.',
    why={'A': '15 counts only the extra numbers with a 3, 6 or 9 digit and forgets the multiples of 3 themselves.',
         'B': '16 is just the multiples of 3. It misses 13, 16, 19, 31 and the rest.',
         'C': '22 counts only numbers containing a 3, 6 or 9, missing multiples like 12, 15, 18, 21, 24, 27, 42, 45 and 48.',
         'D': '25 reads the rule as “contains a 3” only, missing 16, 19, 26, 29, 46 and 49.'},
    fast='16 multiples of 3, + 9 more ending in 3/6/9 (13, 16, 19, 23, 26, 29, 43, 46, 49), + 6 more thirties (31, 32, 34, 35, 37, 38) = 31.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _years():
    data = [(20, 10), (25, 12), (25, 15), (25, 12), (25, 20), (30, 18), (30, 25), (30, 23), (30, 20), (30, 5)]
    x0, bw, gap = 74, 52, 5
    parts, lab = [], []
    for i, (owed, took) in enumerate(data):
        x = x0 + i * (bw + gap)
        last = i == 9
        parts.append(rect(x, 50, bw, 104, k='ink', fill='g' if last else 'paper', sw=1.6))
        parts.append(line(x, 84, x + bw, 84, k='muted', w=1.2))
        parts.append(line(x, 118, x + bw, 118, k='muted', w=1.2))
        lab.append(text(x + bw / 2, 74, owed, k='ink', size=17))
        lab.append(text(x + bw / 2, 108, took, k='ink', size=17))
        lab.append(text(x + bw / 2, 142, '25' if last else owed - took, k='red' if last else 'orange', size=17))
        lab.append(text(x + bw / 2, 176, f'yr {i + 1}', k='muted', size=15))
        if i < 9:
            parts.append(arrow(x + bw - 8, 44, x + bw + gap + 12, 44, k='red', bend=-0.5, w=1.8))
            lab.append(text(x + bw + gap / 2 + 2, 24, '+5', k='red', size=14))
    lab += [text(x0 - 8, 74, 'owed', k='ink', size=15, anchor='end'), text(x0 - 8, 108, 'took', k='ink', size=15, anchor='end'),
            text(x0 - 8, 142, 'spare', k='orange', size=15, anchor='end'),
            text(x0 + 9 * (bw + gap) + bw / 2, 194, 'left!', k='red', size=18, font='scrawl'),
            text(330, 212, 'only 5 spare days carry over each year; the rest are lost', k='ink', size=15)]
    return svg(650, 222, rough(*parts) + ''.join(lab),
               'Ten years of holiday: each year he leaves at least 5 days spare, so 5 carry over; year 10 is 25 + 5 = 30 owed, 5 taken, 25 left')


Q.append(dict(
    n=21, orig=43, answer='B', topic='Rules & carry-over',
    question=f"""<p>Oliver's first job is with Bubble Engineering Ltd. The company grants paid holidays each
year on the following basis:</p>
{table([['First 5 years', '20 days'], [hl('Sixth to tenth year', 'g'), hl('25 days', 'g')], ['Eleventh year onwards', '30 days']],
       head=['<i>Length of Employment</i>', '<i>Holiday entitlement</i>'])}
<p><i>All holidays are granted only at the company's discretion.<br>
{hl('Employees who are unable to take their entitlement may carry forward up to 5 days to the following year.', 'y', 2)}</i></p>
<p>Oliver has decided to leave Bubble Engineering on the {hl('tenth anniversary', 'g', 1)} of his starting
there. Part of his reason for leaving is that he has never been able to take his full holiday
entitlement:</p>
<p>Holiday Record</p>
{table([['<i>Holiday Granted (days)</i>', '10', '12', '15', '12', '20', '18', '25', '23', hl('20', 'g'), hl('5 so far', 'p')]],
       head=['<i>Year</i>', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])}
<p>Oliver knows the company always avoids adverse publicity by {hl('giving the full entitlement once employees give notice', 'p', 3)}.</p>
<p class="stem">How many {hl('more', 'b', 4)} days holiday will he get before he leaves?</p>""",
    options={'A': '20', 'B': '25', 'C': '30', 'D': '35', 'E': '65'},
    notes=[(1, 'g', 'He leaves at the end of year 10. Year 10 is a “sixth to tenth year”: 25 days.'),
           (2, 'y', 'Unused days roll over, but at most 5, and only into the next year.'),
           (3, 'p', 'So he gets everything he’s owed for year 10: 25 days plus whatever carried over from year 9.'),
           (4, 'b', 'He has already had 5 days of year 10. How many <b>more</b>?')],
    steps=[
        f"""<p>Year 10 entitlement: <b>25 days</b> (sixth to tenth year).</p>""",
        f"""<p>Carry-over from year 9: did he leave at least 5 days unused?</p>
{calc('year 9: owed 25 (+ 5 carried in from year 8) = 30', f'took 20 {ar()} 10 spare, but only 5 can carry over')}
{note('Even ignoring year 8, 25 − 20 = 5 spare, so 5 days carry into year 10 either way.', 'check')}
{_years()}""",
        f"""{calc('year 10: 25 + 5 = 30 days owed', 'already taken: 5', f'still to come: 30 − 5 = {boxed("25")}')}
{note('The carry-over is capped at 5 days. All the extra days he missed in years 1 to 8 are simply lost: they don’t pile up.', 'trap')}""",
    ],
    answer_text='25 days: year 10’s 25 plus 5 carried over from year 9, minus the 5 already taken.',
    why={'A': '20 forgets the 5 days carried over from year 9 (25 − 5).',
         'C': '30 is year 10’s full entitlement, forgetting he has already taken 5 days.',
         'D': '35 adds the 5 days already taken instead of subtracting them (30 + 5).',
         'E': '65 adds up every day he has ever missed (225 owed − 160 taken). Only 5 days can roll over, and only for one year.'},
    fast='Year 10: 25 + 5 carried from year 9 (he left at least 5 spare) = 30. Minus the 5 already taken = 25.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _tiling():
    s = 46
    w = s * R3 / 2
    ox, oy = 20, 22
    nl, H = 8, 8 * s
    off = lambda i: s / 2 if i % 2 == 0 else 0
    P = lambda li, y: (round(ox + li * w, 1), round(oy + y, 1))
    hexes = []
    for a in range(-1, 4):
        for b in range(-2, 4):
            xc, yc = 1 + 3 * a, s * (1 + 3 * b + 1.5 * a)
            vs = [(xc, yc - s), (xc + 1, yc - s / 2), (xc + 1, yc + s / 2), (xc, yc + s), (xc - 1, yc + s / 2), (xc - 1, yc - s / 2)]
            if all(0 <= v[0] <= nl and 0 <= v[1] <= H for v in vs):
                hexes.append(((xc, yc), vs))
    tile_c = (4, s * 5.5)
    tris = []
    for i in range(nl):
        for side in (0, 1):
            e = off(i + side)
            for k in range(-2, 12):
                y1, y2 = e + k * s, e + (k + 1) * s
                ap = (i + 1 - side, y1 + s / 2)
                pts = [(i + side, y1), (i + side, y2), ap]
                if all(0 <= p[1] <= H for p in pts):
                    tris.append(pts)
    parts, lab, num = [], [], 0
    for pts in tris:
        cx = sum(p[0] for p in pts) / 3
        cy = sum(p[1] for p in pts) / 3
        in_hex = any(((cx - h[0][0]) * w) ** 2 + (cy - h[0][1]) ** 2 < (0.8 * s) ** 2 for h in hexes)
        in_tile = (tile_c[0] - 1 <= min(p[0] for p in pts) <= tile_c[0] + 1
                   and tile_c[1] - 0.5 * s - 1 <= cy <= tile_c[1] + 2 * s + 1)
        if in_hex:
            continue
        parts.append(poly([P(*p) for p in pts], k='muted', fill='y' if in_tile else 'paper', sw=1.2))
        if in_tile:
            num += 1
            X, Yc = P(cx, cy)
            lab.append(text(X, Yc + 5, num, k='ink', size=15, font='print'))
    for (c, vs) in hexes:
        hi = c == tile_c
        parts.append(poly([P(*v) for v in vs], k='red' if hi else 'ink', fill='o', sw=3 if hi else 1.8))
    X, Yc = P(*tile_c)
    lab.append(text(X, Yc + 6, 'hex', k='red', size=16, font='scrawl'))
    tx = ox + nl * w + 26
    lab += [text(tx, 70, 'one repeating block:', k='red', size=20, font='scrawl', anchor='start'),
            text(tx, 104, '1 hexagon (red outline)', k='ink', size=16, anchor='start'),
            text(tx, 128, '+ the 12 yellow triangles', k='ink', size=16, anchor='start'),
            text(tx, 170, 'copies of this block', k='ink', size=16, anchor='start'),
            text(tx, 192, 'cover the whole floor', k='ink', size=16, anchor='start'),
            text(tx, 236, '1 hexagon : 12 triangles', k='green', size=20, font='scrawl', anchor='start')]
    return svg(640, H + 2 * oy, rough(*parts) + ''.join(lab),
               f'The tiling redrawn: one hexagon and the {num} triangles that belong to it are highlighted as one repeating block')


Q.append(dict(
    n=22, orig=44, answer='C', topic='Tiling & ratio',
    question=f"""<p>The pattern below shows part of the tiling of a large floor in a community centre. It is
made up of two types of tile: a hexagon and a triangle.</p>
{fig(Y, 'ps_q22_tiles', 'A patch of triangular tiles with six dark hexagons arranged in two staggered columns', 200)}
<p class="stem">For a {hl('sufficiently large expanse of flooring', 'p', 1)}, approximately what {hl('proportion of the two types of tile', 'b', 2)} will be required?</p>""",
    options={'A': '1 hexagon to 6 triangles', 'B': '1 hexagon to 9 triangles', 'C': '1 hexagon to 12 triangles',
             'D': '1 hexagon to 15 triangles', 'E': '1 hexagon to 18 triangles'},
    notes=[(1, 'p', 'Ignore the ragged edge of the picture. Find the pattern that <b>repeats</b> across a big floor.'),
           (2, 'b', 'How many triangle tiles for every hexagon tile?')],
    steps=[
        f"""<p>A hexagon fills exactly the space of <b>6 triangles</b>. Look at the vertical strips of triangles in the picture:
they come in a repeating set of three: a strip through the left half of the hexagons, a strip through the right half, then a plain strip.</p>""",
        f"""<p>Go down one strip from one hexagon to the next (6 triangle spaces) and count:</p>
{calc('left-half strip: 3 spaces of hexagon + 3 triangles', 'right-half strip: 3 spaces of hexagon + 3 triangles',
      'plain strip: 6 triangles', f'block total: 1 hexagon + 3 + 3 + 6 = <b>12 triangles</b>')}
{_tiling()}""",
        f"""{calc(f'ratio {ar()} {boxed("1 hexagon to 12 triangles")}')}
{note('Area check: 1 hexagon + 12 triangles = 6 + 12 = 18 triangle spaces, so hexagons cover a third of the floor. That looks right in the picture.', 'check')}
{note('Counting the picture directly gives about 16 triangles per hexagon, because its border is full of extra triangles. On a big floor the border hardly matters.', 'trap')}""",
    ],
    answer_text='1 hexagon to 12 triangles: each repeating block is one hexagon plus 12 triangles.',
    why={'A': '6 counts only the triangles touching the hexagon’s sides and misses the ones in between.',
         'B': '9 shares the plain strip between two hexagon columns (6 + 3). But the strips go hexagon, hexagon, plain, so each hexagon column has a whole plain strip of its own.',
         'D': '15 is roughly what you get by counting the picture, which has extra triangles round its border (about 16 per hexagon). A large floor has no such border.',
         'E': '18 counts the whole ring of triangles round one hexagon, but neighbouring hexagons share those rings. (18 is also the block size if you count the hexagon’s own 6 spaces as triangles.)'},
    fast='Strips repeat hexagon, hexagon, plain. Per hexagon: 3 + 3 + 6 = 12 triangles.',
))


# ---------------------------------------------------------------- 23 (Q48)
def _route_row(y, order, route, x0=60, sp=110, mark=None):
    X = {t: x0 + i * sp for i, t in enumerate(order)}
    parts = [line(X[order[0]] - 24, y, X[order[-1]] + 24, y, k='ink', w=2)]
    lab = []
    for t in order:
        parts.append(circle(X[t], y, 6, k='ink', fill='paper' if t != 'X' else 'ink', sw=2))
        lab.append(text(X[t], y + 26, t, k='ink', size=18, font='print', weight='bold'))
    L = len(route) - 1
    lev = lambda i: y - 14 - 10 * (L - 1 - i)
    for i in range(L):
        a, b = route[i], route[i + 1]
        parts.append(line(X[a], lev(i), X[b], lev(i), k='red', w=2, head=True))
        if i < L - 1:
            parts.append(line(X[b], lev(i), X[b], lev(i + 1), k='red', w=1.4))
    if mark:
        t, i = mark
        parts.append(circle(X[t], lev(i), 9, k='orange', sw=2.6))
    return parts, lab


def _routes():
    parts, lab = [], []
    rows = [('A', 'AXBC', 'XAXBCBX', 'A – X – B – C'), ('D', 'CXBA', 'XBABXCX', 'C – X – B – A'),
            ('E', 'XABC', 'XABCBAX', 'X – A – B – C')]
    for j, (opt, order, route, lay) in enumerate(rows):
        y = 100 + j * 112
        p, l = _route_row(y, order, route)
        parts += p
        lab += l
        lab += [text(450, y - 30, f'{opt}: {route} ✓', k='green', size=19, font='scrawl', anchor='start'),
                text(450, y - 6, f'towns in a line:', k='ink', size=15, anchor='start'),
                text(450, y + 14, lay, k='ink', size=15, anchor='start')]
    lab.append(text(320, 22, 'red = the lorry’s journey, one step at a time', k='red', size=15))
    return svg(640, 360, rough(*parts) + ''.join(lab),
               'Routes A, D and E drawn on towns in a straight line: each just goes out to the far towns and comes back')


def _route_c():
    Xx, Ax, Cx, Bx = (70, 210), (70, 80), (230, 80), (230, 210)
    parts = [arrow(*Xx, *Ax, k='red'), arrow(*Ax, *Cx, k='red'), arrow(*Cx, *Bx, k='red'), arrow(*Bx, *Xx, k='red')]
    lab = []
    for t, (x, y) in (('X', Xx), ('A', Ax), ('C', Cx), ('B', Bx)):
        parts.append(circle(x, y, 6, k='ink', fill='ink' if t == 'X' else 'paper', sw=2))
        lab.append(text(x + (-18 if x < 150 else 18), y + 6, t, k='ink', size=18, font='print', weight='bold'))
    lab += [text(150, 30, 'B: XACBX ✓', k='green', size=19, font='scrawl'),
            text(150, 250, 'an ordinary loop', k='ink', size=15)]
    p, l = _route_row(170, 'AXBC', 'XAXBCX', x0=330, sp=90, mark=('B', 4))
    parts += p
    lab += l
    lab += [text(465, 30, 'C: XAXBCX ✗', k='red', size=19, font='scrawl'),
            text(465, 230, 'coming home from C you pass B,', k='orange', size=15),
            text(465, 250, 'so the journey is really XAXBCBX', k='orange', size=15)]
    return svg(640, 264, rough(*parts) + ''.join(lab),
               'Route B as a loop round four towns; route C on towns A, X, B, C in a line, where the trip home from C passes B again')


Q.append(dict(
    n=23, orig=48, answer='C', topic='Routes & logic',
    question=f"""<p>Starting from its depot in town X, a delivery lorry is to make deliveries to three towns A, B
and C, {hl('in any order which the driver chooses', 'y', 1)} and finally to return to X.</p>
<p>{hl('Straight roads connect each town to every other town.', 'y', 2)}</p>
<p class="stem">{hl('Depending on the layout of the towns', 'p', 3)}, which of the following {hl('could <b>NOT</b> be the shortest journey', 'b', 4)} for him to take?</p>""",
    options={'A': 'XAXBCBX', 'B': 'XACBX', 'C': 'XAXBCX', 'D': 'XBABXCX', 'E': 'XABCBAX'},
    notes=[(1, 'y', 'He must visit A, B and C, starting and finishing at X.'),
           (2, 'y', 'Straight roads: going direct is never longer than going via another town.'),
           (3, 'p', 'The towns might even lie in a straight line. Then driving from one town to another passes through the towns in between.'),
           (4, 'b', 'Four routes are the shortest for <b>some</b> layout. Find the one that never is.')],
    steps=[
        f"""<p>Going via an extra town is never shorter than going direct. So a shortest journey only passes a town twice
(like X in the middle) when that town lies <b>on the straight road</b> it has to use anyway, i.e. the towns are in a line.
Each route lists every town it passes through.</p>""",
        f"""<p>Find a layout for each route:</p>{_routes()}""",
        f"""{_route_c()}
<p>For C to go back through X between A and B, X must lie on the road from A to B (A – X – B). And C must be on that same line,
or XACBX would be shorter. So:</p>
{calc(f'C beyond B (A – X – B – C): the drive home from C passes B {ar()} really XAXBCBX',
      f'C between X and B (A – X – C – B): the drive to B passes C {ar()} really XAXCBCX',
      f'C off the line: XACBX is shorter {ar()} not the shortest')}
<p>So XAXBCX is never the shortest journey {ar()} {boxed('C')}</p>""",
    ],
    answer_text='XAXBCX: whenever its back-and-forth through X makes sense, the trip between B, C and X must pass another town it doesn’t list.',
    why={'A': 'Shortest when A – X – B – C lie in a line: out to A and back, then out to C and back, passing B both ways.',
         'B': 'Shortest for lots of ordinary layouts, e.g. four towns round a neat loop.',
         'D': 'Shortest when C – X – B – A lie in a line: out past B to A and back, then out to C and back.',
         'E': 'Shortest when X – A – B – C lie in a line: drive to the far end and back, passing A and B twice.'},
    fast='Repeated towns only happen with towns in a line. A, D and E each fit a line, B is a normal loop. C needs X between A and B, but then going to or from C passes B (or C) again unlisted.',
))


# ---------------------------------------------------------------- 24 (Q49)
def _butt():
    X = lambda v: 60 + v * 0.2
    parts = [rect(X(0), 50, X(2500) - X(0), 40, k='ink', fill='p', sw=1.8),
             rect(X(0), 140, X(200) - X(0), 40, k='ink', fill='o', sw=1.8),
             rect(X(200), 140, X(2200) - X(200), 40, k='ink', fill='b', sw=1.8),
             rect(X(2200), 140, X(2500) - X(2200), 40, k='red', fill='y', sw=2.4),
             brace(X(2200), X(2500), 186, '', k='red')]
    lab = [text(X(0), 40, 'needed: 25 weeks × 100 L', k='ink', size=16, anchor='start'),
           text(X(1250), 76, '2500 L', k='ink', size=18),
           text(X(0), 130, 'from the butt', k='ink', size=16, anchor='start'),
           text(X(100), 166, '200', k='ink', size=15),
           text(X(1200), 166, 'rain kept: ½ × 25 × 160 = 2000 L', k='ink', size=16),
           text(X(2350), 166, '300', k='red', size=16),
           text(X(2350), 226, 'mains water', k='red', size=17, font='scrawl')]
    return svg(640, 240, rough(*parts) + ''.join(lab),
               'Bars: 2500 litres needed; the butt supplies 200 plus 2000 litres of rain, leaving 300 litres from the mains')


Q.append(dict(
    n=24, orig=49, answer='B', topic='Volume & rates',
    question=f"""<p>A rainwater butt in Joan's garden fills from a flat roof of an equivalent area to {hl('25 square metres', 'g', 1)}. The butt {hl('holds 200 litres and is full', 'g', 2)} when Joan starts using it in the
summer. During the gardening season, {hl('160 litres falls on each square metre', 'g', 3)} of
roof. {hl('Only half of this is collected', 'p', 4)} as the rest evaporates. Joan uses {hl('100 litres from the butt to top up her garden pond each week for 25 weeks', 'g', 5)}. If there is not enough water in
the butt, she completes the job with mains water which is rather expensive. During the
summer months {hl('there is never enough rain to overfill the butt', 'y', 6)}.</p>
<p class="stem">How much mains water would she expect to use in an average summer?</p>""",
    options={'A': '0 litres', 'B': '300 litres', 'C': '500 litres', 'D': '2000 litres', 'E': '2300 litres'},
    notes=[(1, 'g', 'Roof area: multiply by the rain per m².'),
           (2, 'g', 'She starts with 200 litres already in the butt.'),
           (3, 'g', '160 litres per m² over the whole season.'),
           (4, 'p', 'Halve the rain!'),
           (5, 'g', 'Total needed: 25 × 100 = 2500 litres.'),
           (6, 'y', 'No overflow, so every litre collected gets used.')],
    steps=[
        f"""<p>Water available from the butt:</p>
{calc('rain on the roof: 25 × 160 = 4000 L', 'collected: ½ × 4000 = 2000 L', 'plus the 200 L in the butt at the start → 2200 L')}""",
        f"""<p>Water needed, and the shortfall:</p>
{calc('needed: 25 × 100 = 2500 L', f'mains = 2500 − 2200 = {boxed("300 litres")}')}
{_butt()}""",
        f"""{note('Week by week: 2000 ÷ 25 = 80 L of rain a week, but she uses 100. The butt drops 20 L a week, so the 200 L lasts 10 weeks; then 20 L of mains a week for 15 weeks = 300 L. Same answer.', 'check')}""",
    ],
    answer_text='300 litres: she needs 2500 L but the butt only provides 200 + 2000 = 2200 L.',
    why={'A': '0 litres forgets that half the rain evaporates (4000 L would be plenty).',
         'C': '500 litres forgets the 200 L already in the butt at the start (2500 − 2000).',
         'D': '2000 litres is the rainwater collected, not the mains water.',
         'E': '2300 litres = 2500 − 200 ignores the rain altogether.'},
    fast='½ × 25 × 160 = 2000, + 200 in the butt = 2200. Need 25 × 100 = 2500. Short by 300 L.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _net():
    T, L, Rr = (150, 30), (30, 238), (270, 238)
    mL, mR, mB = (90, 134), (210, 134), (150, 238)
    parts = [poly([T, mL, mR], k='ink', fill='g', sw=2), poly([mL, mR, mB], k='ink', fill='p', sw=2),
             poly([mL, L, mB], k='ink', fill='b', sw=2), poly([mR, mB, Rr], k='ink', fill='y', sw=2),
             arrow(mB[0] - 34, mB[1] - 10, mB[0] + 34, mB[1] - 10, k='red', bend=-0.55, w=2.6),
             arrow(mL[0] + 16, mL[1] - 26, mL[0] + 4, mL[1] + 32, k='red', bend=-0.5, w=2.6),
             arrow(mR[0] - 4, mR[1] + 32, mR[0] - 16, mR[1] - 26, k='red', bend=-0.5, w=2.6)]
    lab = [text(150, 92, 'G', k='ink', size=22, font='print', weight='bold'),
           text(150, 176, 'R', k='ink', size=22, font='print', weight='bold'),
           text(72, 222, 'B', k='ink', size=22, font='print', weight='bold'),
           text(228, 222, 'Y', k='ink', size=22, font='print', weight='bold')]
    for p in (mL, mR, mB):
        lab.append(circle(p[0], p[1], 5, k='red', fill='paper', sw=2.4))
    tx = 300
    lab += [text(tx, 50, 'Clockwise round each corner', k='red', size=19, font='scrawl', anchor='start'),
            text(tx, 82, 'left middle: G → R → B', k='ink', size=17, anchor='start'),
            text(tx, 110, 'right middle: Y → R → G', k='ink', size=17, anchor='start'),
            text(tx, 138, 'bottom middle: B → R → Y', k='ink', size=17, anchor='start'),
            text(tx, 166, 'the 3 tips: G → B → Y', k='ink', size=17, anchor='start'),
            text(tx, 200, '(start anywhere: B → R → Y', k='muted', size=15, anchor='start'),
            text(tx, 220, ' is the same as R → Y → B)', k='muted', size=15, anchor='start')]
    return svg(620, 256, rough(*parts) + ''.join(lab),
               'The net with clockwise arrows round the three middle corners: G R B on the left, Y R G on the right, B R Y at the bottom')


def _views():
    fills = {'G': 'g', 'R': 'p', 'B': 'b', 'Y': 'y'}
    parts, lab = [], []
    for cx, (left, right, bottom), title, sub, ok in (
            (170, ('B', 'R', 'Y'), 'view B: R → Y → B', 'same order as the net ✓', True),
            (470, ('Y', 'R', 'B'), 'view E: R → B → Y', 'backwards: a mirror image ✗', False)):
        apex, bl, br, c = (cx, 30), (cx - 100, 196), (cx + 100, 196), (cx, 140)
        parts += [poly([apex, c, bl], k='ink', fill=fills[left], sw=2), poly([apex, c, br], k='ink', fill=fills[right], sw=2),
                  poly([bl, c, br], k='ink', fill=fills[bottom], sw=2),
                  arrow(cx + 21, 128, cx + 3, 164, k='red', bend=-0.45, w=2.4),
                  arrow(cx - 3, 164, cx - 21, 128, k='red', bend=-0.45, w=2.4)]
        lab += [text(cx - 40, 126, left, k='ink', size=22, font='print', weight='bold'),
                text(cx + 40, 126, right, k='ink', size=22, font='print', weight='bold'),
                text(cx, 188, bottom, k='ink', size=22, font='print', weight='bold'),
                text(cx, 226, title, k='green' if ok else 'red', size=19, font='scrawl'),
                text(cx, 250, sub, k='green' if ok else 'red', size=15)]
    return svg(640, 262, rough(*parts) + ''.join(lab),
               'Views B and E side by side: B reads R, Y, B clockwise like the net; E reads R, B, Y, the mirror image')


Q.append(dict(
    n=25, orig=50, answer='E', topic='Nets & 3D views',
    question=f"""<p>Four triangles of card {hl('coloured on one side', 'y', 1)} are joined as shown.</p>
{fig(Y, 'ps_q25_net', 'Net: a large triangle split into four; G at the top, R in the middle, B bottom left, Y bottom right. G = Green, R = Red, B = Blue, Y = Yellow', 380)}
<p>The joined triangles are then {hl('folded and joined to make a pyramid', 'y', 2)}.</p>
<p class="stem">Which of the following {hl('could <b>not</b> be a view from above', 'b', 3)}?</p>
{fig(Y, 'ps_q25_opts', 'Five views A to E, each a triangle split into three faces meeting at a centre point', 470)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'The coloured side ends up outside, so you see the colours the right way round, never a mirror image.'),
           (2, 'y', 'Four triangles make a triangular pyramid: every corner has three faces meeting at it.'),
           (3, 'b', 'From above you see one corner and the three faces around it. Four options are real corners; one is impossible.')],
    steps=[
        f"""<p>The pyramid has 4 corners. Three are the points in the middle of each side of the net, where three triangles already meet.
The fourth is where the three outer tips come together.</p>""",
        f"""<p>Folding doesn’t flip anything, so going <b>clockwise</b> round a corner you meet the faces in the same order as on the net:</p>{_net()}""",
        f"""<p>Read each option clockwise (start anywhere):</p>
{calc(f'A: G → Y → R = Y → R → G {tick()} right middle', f'B: R → Y → B {tick()} bottom middle',
      f'C: B → G → R = G → R → B {tick()} left middle', f'D: G → B → Y {tick()} the tips',
      f'E: R → B → Y {cross()} bottom middle backwards')}
{_views()}
{calc(f'E is a mirror image, so it can’t be seen {ar()} {boxed("E")}')}
{note('Why are the tips G → B → Y? Stand the pyramid on R and look down. You are now looking at the net from behind, so left and right swap: G at the top, B on the right, Y on the left. Going clockwise: G, B, Y = view D.', 'check')}
{note('Faster: B and E use the same three colours in opposite orders, so one of them must be wrong. Check that corner on the net.', 'tip')}""",
    ],
    answer_text='View E: it shows R, B, Y clockwise, the mirror image of the real corner (R, Y, B).',
    why={'A': 'Possible: the corner at the right-hand middle point of the net (G, Y, R clockwise).',
         'B': 'Possible: the corner at the bottom middle point of the net (R, Y, B clockwise).',
         'C': 'Possible: the corner at the left-hand middle point of the net (G, R, B clockwise).',
         'D': 'Possible: the corner where the three tips meet (G, B, Y clockwise), the top when it stands on R.'},
    fast='B and E are mirror images of each other. Round the net’s bottom middle point: R, then Y, then B clockwise. That’s B, so E is impossible.',
))
