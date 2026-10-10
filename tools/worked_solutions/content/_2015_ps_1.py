from wslib import *

Y = 2015
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _coins():
    parts, lab = [], []
    for i in range(15):
        r, c = divmod(i, 5)
        x, y = 50 + c * 46, 62 + r * 46
        parts.append(circle(x, y, 19, k='ink', fill='y', sw=1.8))
        lab.append(text(x, y + 5, '50', k='ink', size=14, font='print'))
    for i in range(10):
        r, c = divmod(i, 5)
        x, y = 340 + c * 38, 62 + r * 92
        back = r == 1
        parts.append(circle(x, y, 14, k='muted' if back else 'ink', fill='none' if back else 'o', sw=1.6))
        lab.append(text(x, y + 5, '10', k='muted' if back else 'ink', size=12, font='print'))
    parts.append(f'<rect x="318" y="134" width="196" height="40" rx="14" class="k-red f-none" stroke-width="2" stroke-dasharray="6 5"/>')
    parts.append(arrow(518, 154, 598, 154, k='red', bend=-0.25))
    lab += [text(142, 24, '15 × 50p = £7.50', k='ink', size=18),
            text(416, 24, '10 × 10p = £1.00', k='ink', size=18),
            text(418, 126, 'these 5 stay in', k='orange', size=16),
            text(604, 200, '5 come back out', k='red', size=18, font='scrawl', anchor='end'),
            text(142, 222, 'all 15 stay in', k='ink', size=16),
            text(300, 262, 'kept: 15 fifties and 5 tens = 3 : 1', k='green', size=22, font='scrawl')]
    return svg(620, 278, rough(*parts) + ''.join(lab),
               'Fifteen 50p coins and ten 10p coins; five of the 10p coins are returned, leaving 15 fifties and 5 tens')

Q.append(dict(
    n=1, orig=2, answer='D', topic='Money & coins',
    question=f"""<p>A public telephone has been vandalised and will take {hl('only 50 pence coins and 10 pence coins', 'y', 1)}. A
woman puts {hl('£8.50', 'g', 2)} into the phone to make a long-distance call with {hl('twenty-five coins', 'g', 2)}. {hl('Five 10 pence coins are returned', 'p', 3)} when she finishes her call.</p>
<p class="stem">What combination of coins is {hl('retained', 'b', 4)} by the machine?</p>""",
    options={'A': 'Twice as many 10s as 50s.', 'B': 'One-and-a-half times as many 50s as 10s.',
             'C': 'The same number of 50s and 10s.', 'D': 'Three times as many 50s as 10s.',
             'E': 'One-and-a-half times as many 10s as 50s.'},
    notes=[(1, 'y', 'Only two kinds of coin, so it is a “how many of each?” puzzle.'),
           (2, 'g', 'Two facts to use together: 25 coins and £8.50 in total.'),
           (3, 'p', 'The five returned coins are all 10p. Take them off <b>after</b> you find the mix.'),
           (4, 'b', '“Retained” = kept by the machine, so after the 5 coins come back.')],
    steps=[
        f"""<p>Pretend all 25 coins were 10p, then swap some for 50p coins:</p>
{calc(f'25 × 10p = £2.50 {ar()} short by £8.50 − £2.50 = <b>£6.00</b>',
      f'each swap (10p {ar()} 50p) adds 40p',
      f'£6.00 ÷ 40p = 600 ÷ 40 = <b>15 swaps</b>')}
<p>So she put in <b>15 × 50p</b> and <b>10 × 10p</b>.</p>
{calc('check: 15 × 50p + 10 × 10p = £7.50 + £1.00 = £8.50 ' + tick())}""",
        f"""<p>Now the machine gives back five 10p coins:</p>{_coins()}
{calc('50s kept: 15', '10s kept: 10 − 5 = 5', f'15 ÷ 5 = 3 {ar()} {boxed("three times as many 50s as 10s")}')}""",
    ],
    answer_text='Three times as many 50s as 10s: 15 fifties and 5 tens are kept.',
    why={'A': 'A has it upside down. There are far more 50s than 10s (15 against 5).',
         'B': '15 fifties to 10 tens is 1.5 times as many: that is what went <b>in</b>. It forgets the five 10s that came back.',
         'C': 'Equal piles would need, say, 5 and 5 (£3.00). The machine kept 15 fifties but only 5 tens.',
         'E': 'E is the “before” ratio (15 : 10) turned upside down, so it mixes up the coins and forgets the returned 10s.'},
    fast='All 10p = £2.50. Extra £6 ÷ 40p = 15 fifties, so 10 tens. 5 tens come back: 15 : 5 = 3 : 1.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _roast():
    X = lambda t: 30 + t * 7.3
    parts, lab = [line(X(0), 160, X(72), 160, k='ink', head=True)], []
    for t in range(0, 71, 10):
        parts.append(line(X(t), 154, X(t), 166, k='ink', w=1.5))
        lab.append(text(X(t), 186, t, k='muted', size=15))
    parts += [rect(X(0), 40, X(60) - X(0), 32, k='ink', fill='o', sw=1.8),
              rect(X(60), 40, X(70) - X(60), 32, k='ink', fill='y', sw=1.8),
              rect(X(40), 100, X(70) - X(40), 32, k='ink', fill='g', sw=1.8),
              line(X(70), 26, X(70), 150, k='red', w=2.4, dash=True),
              line(X(40), 88, X(40), 150, k='green', w=2, dash=True)]
    lab += [text(X(30), 62, 'beef in hot oven: 60 min', k='ink', size=16),
            text(X(65), 34, 'stand', k='ink', size=15),
            text(X(55), 122, 'potatoes 30 min', k='ink', size=16),
            text(X(70) + 8, 22, 'serve!', k='red', size=20, font='scrawl', anchor='start'),
            text(X(40) - 6, 120, 'potatoes in', k='green', size=17, font='scrawl', anchor='end'),
            text(X(40) - 6, 140, 'at 40 min', k='green', size=17, font='scrawl', anchor='end'),
            text(X(36), 212, 'minutes after the beef goes in', k='muted', size=15)]
    return svg(620, 224, rough(*parts) + ''.join(lab),
               'Timeline: beef cooks 0 to 60 minutes, stands 60 to 70; potatoes cook 40 to 70 so both are ready at 70')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Timings & recipes',
    question=f"""<p>William wants to cook roast beef and potatoes for {hl('himself and four friends', 'p', 1)}. From his cookbook
he gets the following information:</p>
{table([['Rare', '---', '10 minutes per 500 g'],
        ['Medium rare', '20 minutes per 500 g plus 20 mins', hl('15 minutes per 500 g plus 15 minutes', 'y', 4)],
        ['Well done', '30 minutes per 500 g plus 30 minutes', '---']],
       head=['BEEF', 'Medium oven', 'Hot oven'])}
<p>{hl('Allow 300 g per person.', 'g', 2)}</p>
<p>After removing from the oven, the meat should be allowed to {hl('stand for 10 minutes', 'p', 3)}.</p>
{table([['', '40 minutes', hl('30 minutes', 'g')]], head=['ROAST POTATOES', 'Medium oven', 'Hot oven'])}
<p>William buys a joint of the correct weight and decides to cook it {hl('medium rare in a hot oven', 'y', 4)}.</p>
<p class="stem">How long after putting the beef in the oven should he put in the potatoes, so that both will be
{hl('ready to serve at the same time', 'b', 5)}?</p>""",
    options={'A': '25 minutes', 'B': '30 minutes', 'C': '31 minutes', 'D': '40 minutes', 'E': '50 minutes'},
    notes=[(1, 'p', 'Himself <b>and</b> four friends = <b>5 people</b>, not 4.'),
           (2, 'g', '5 × 300 g gives the weight of the joint.'),
           (3, 'p', 'The beef is not ready to serve until 10 minutes <b>after</b> it leaves the oven.'),
           (4, 'y', 'Only one cell of the beef table matters: medium rare, hot oven. The potatoes go in the same hot oven.'),
           (5, 'b', 'Work backwards from serving time.')],
    steps=[
        f"""<p>Weight of the joint:</p>
{calc(f'5 people × 300 g = 1500 g = 3 × 500 g')}""",
        f"""<p>Beef, medium rare, hot oven:</p>
{calc('3 × 15 min + 15 min = 45 + 15 = <b>60 min</b> in the oven',
      f'+ 10 min standing {ar()} ready to serve <b>70 min</b> after it goes in')}""",
        f"""<p>Potatoes take 30 minutes in the hot oven, so they must finish at 70 minutes too:</p>
{_roast()}
{calc(f'70 − 30 = {boxed("40 minutes")}')}""",
    ],
    answer_text='40 minutes: the beef is ready to serve at 70 minutes and the potatoes need the last 30.',
    why={'A': '25 minutes forgets the “plus 15 minutes”: 45 + 10 − 30 = 25.',
         'B': '30 minutes forgets the 10 minutes of standing: 60 − 30 = 30.',
         'C': '31 minutes forgets to count William himself: 4 × 300 = 1200 g, 2.4 × 15 + 15 = 51, then 51 + 10 − 30 = 31.',
         'E': '50 minutes uses the <b>medium</b> oven: 3 × 20 + 20 = 80, 80 + 10 − 40 = 50. He chose the hot oven.'},
    fast='1500 g: 3 × 15 + 15 = 60, + 10 standing = 70, − 30 for the potatoes = 40.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _knockout():
    rows = [('Andrew', ('1', 'ok'), ('60 − 56 = 4', 'out'), ('', '')),
            ('Carole', ('2', 'ok'), ('56 − 56 = 0', 'ok'), ('56 − 53 = 3', 'ok')),
            ('Edward', ('2', 'ok'), ('59 − 56 = 3', 'out'), ('', '')),
            ('Grace', ('3', 'out'), ('', ''), ('', '')),
            ('Ian', ('2', 'ok'), ('54 − 53 = 1', 'ok'), ('54 − 52 = 2', 'win'))]
    cols = [(110, 'late', 120), (230, 'missed deadline', 170), (400, 'non-A pieces', 170)]
    parts, lab = [], []
    for x, head, w in cols:
        lab.append(text(x + w / 2, 30, head, k='ink', size=17))
    lab.append(text(14, 30, 'pupil', k='muted', size=16, anchor='start'))
    for i, (name, *cells) in enumerate(rows):
        y = 44 + i * 44
        lab.append(text(14, y + 28, name, k='ink', size=19, anchor='start'))
        for (x, _, w), (val, st) in zip(cols, cells):
            fill = {'ok': 'g', 'out': 'p', 'win': 'y', '': 'none'}[st]
            parts.append(rect(x, y + 4, w - 10, 36, k='ink' if st else 'muted', fill=fill, sw=1.4))
            if val:
                mark = {'ok': ' ✓', 'out': ' ✗', 'win': ' ★'}[st]
                lab.append(text(x + (w - 10) / 2, y + 28, val + mark, k='red' if st == 'out' else 'ink', size=16))
        if name in ('Andrew', 'Edward', 'Grace'):
            parts.append(line(10, y + 22, 96, y + 22, k='red', w=2.6))
    lab.append(text(300, 280, 'out if late 3+ times or 3+ homeworks missed the deadline', k='muted', size=15))
    return svg(580, 292, rough(*parts) + ''.join(lab),
               'Knockout grid: Grace out for lateness, Andrew and Edward out for missed deadlines; Ian beats Carole on non-A pieces, 2 against 3')

Q.append(dict(
    n=3, orig=7, answer='E', topic='Tables & rules',
    question=f"""<p>A teacher is going to award a prize to her most deserving pupil in the current school year. She
has narrowed it down to five students and must make her final judgements. She won't give the
prize to anyone who has been {hl('late to her lessons more than twice', 'y', 1)}. She won't give it to anyone
who has {hl('failed to complete more than two pieces of homework by the deadline set', 'y', 2)}. After these
criteria have been met, the prize will be awarded to the student with the {hl('fewest non-A-grade pieces of work', 'b', 3)}.</p>
{table([['Andrew', '8', '4', '1', '60', '56', '58'],
        ['Carole', '11', '2', '2', '56', '56', '53'],
        ['Edward', '9', '6', '2', '59', '56', '58'],
        ['Grace', '10', '6', hl('3', 'p'), '58', '57', '56'],
        ['Ian', '11', '10', '2', '54', '53', '52']],
       head=['Pupil', 'Year group', hl('No. of lessons missed', 'p', 4), 'No. of times late for lesson', 'No. of homeworks set',
             'Homeworks completed by deadline', 'Homeworks with grade A'])}
<p class="stem">Which student will be awarded the prize?</p>""",
    options={'A': 'Andrew', 'B': 'Carole', 'C': 'Edward', 'D': 'Grace', 'E': 'Ian'},
    notes=[(1, 'y', '“More than twice” = 3 or more lates. Exactly 2 is still fine.'),
           (2, 'y', 'Not in the table directly! Missed = homeworks set − completed by deadline. 3 or more is out.'),
           (3, 'b', 'Non-A = homeworks set − grade A. Only compare pupils who survive the two rules.'),
           (4, 'p', 'Red herring: lessons missed (and year group) are not in any rule.')],
    steps=[
        f"""<p>Rule 1: late 3 or more times? Only <b>Grace</b> (3). She is out.</p>""",
        f"""<p>Rule 2: work out missed deadlines = set − completed:</p>
{calc('Andrew 60 − 56 = 4 ' + cross(), 'Carole 56 − 56 = 0 ' + tick(), 'Edward 59 − 56 = 3 ' + cross(), 'Ian 54 − 53 = 1 ' + tick())}""",
        f"""<p>Only Carole and Ian are left. Count non-A pieces = set − grade A:</p>{_knockout()}
{calc(f'Carole 3, Ian 2 {ar()} fewest = {boxed("Ian")}')}
{note('Ian missed 10 lessons, the most of anyone. It does not matter: no rule mentions missed lessons.', 'trap')}""",
    ],
    answer_text='Ian: he passes both rules and has only 2 non-A pieces (Carole has 3).',
    why={'A': 'Andrew has only 2 non-A pieces, but he missed 4 deadlines, so he is out.',
         'B': 'Carole passes both rules but has 3 non-A pieces, one more than Ian.',
         'C': 'Edward is the trap: only 1 non-A piece, the best of all, but 59 − 56 = 3 missed deadlines rules him out.',
         'D': 'Grace was late 3 times, which is “more than twice”.'},
    fast='Cross out Grace (late 3), Andrew (4 missed) and Edward (3 missed). Non-A: Carole 3, Ian 2. Ian.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _seasons():
    x0, w = 120, 40
    months = 'JFMAMJJASOND'
    parts, lab = [], []
    for row, (y, title, winter) in enumerate(((80, 'North', (11, 0, 1)), (220, 'South', (5, 6, 7)))):
        lab.append(text(x0 - 12, y + 25, title, k='ink', size=19, anchor='end'))
        for i, m in enumerate(months):
            parts.append(rect(x0 + i * w, y, w, 36, k='ink', fill='b' if i in winter else 'paper', sw=1.4))
            lab.append(text(x0 + i * w + w / 2, y + 25, m, k='ink', size=16, font='print'))

    def hill(i, y, k, label, up=True):
        cx = x0 + i * w + w / 2
        d = -1 if up else 1
        p = path(f'M{cx - 32} {y} Q{cx} {y + d * 48} {cx + 32} {y}', k=k, sw=3)
        t = text(cx, y - 32 if up else y + 50, label, k=k, size=18, font='scrawl')
        return p, t
    for i, y, k, label, up in ((5, 80, 'green', 'plant peak', True), (9, 80, 'orange', 'animal peak', True),
                               (11, 256, 'green', 'plant peak', False), (3, 256, 'orange', 'animal peak', False)):
        p, t = hill(i, y, k, label, up)
        parts.append(p)
        lab.append(t)
    parts += [arrow(x0 + 5.5 * w + 10, 122, x0 + 11.5 * w - 6, 214, k='green', bend=0.08),
              arrow(x0 + 9.5 * w - 10, 122, x0 + 3.5 * w + 6, 214, k='orange', bend=-0.08)]
    lab += [text(x0 + 8.9 * w, 162, '+6 months', k='green', size=19, font='scrawl', anchor='start'),
            text(x0 + 4.2 * w, 162, '+6 months (wraps round)', k='orange', size=19, font='scrawl', anchor='end'),
            text(12, 24, 'blue = winter', k='pen', size=16, anchor='start')]
    return svg(620, 320, rough(*parts) + ''.join(lab),
               'Month strips: north polar plant peak in June and animal peak in October; in the south both move 6 months, to December and April')

Q.append(dict(
    n=4, orig=8, answer='D', topic='Graphs & seasons',
    question=f"""<p>Plankton are small plants and animals present in the sea. The animal plankton feed on the plant
plankton. The rate at which the plant plankton are produced depends on sea temperature and
the amount of sunlight.</p>
<p>In tropical regions there is little variation of plankton production through the year. {hl('Variations are much bigger at temperate and polar latitudes', 'y', 1)}. {hl('Plant plankton production always rises before that of animal plankton', 'y', 2)}.</p>
<p>The following graphs show the production rates of plankton in the {hl('northern hemisphere', 'p', 3)}:</p>
{fig(Y, 'ps_q04_north', 'Three graphs for the north: polar (plant peaks about 60 in June, animal about 40 in October), temperate (smaller peaks), tropical (almost flat)', 600)}
<p>In the northern hemisphere winter is in December, January and February. {hl('In the southern hemisphere it is in June, July and August', 'g', 4)}.</p>
<p class="stem">Which one of the following graphs provides a good representation of plankton production in the
{hl('southern polar region', 'b', 5)}?</p>
{fig(Y, 'ps_q04_opts', 'Five plankton graphs A to E', 600)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'y', 'Polar = big swings. A nearly flat graph is tropical.'),
           (2, 'y', 'The plant peak comes first, then the animal peak follows (the animals eat the plants).'),
           (3, 'p', 'The given graphs are for the <b>north</b>. You must convert to the south.'),
           (4, 'g', 'Southern seasons are 6 months out of step with the north.'),
           (5, 'b', 'Polar shape, southern timing.')],
    steps=[
        f"""<p>Start from the northern <b>polar</b> graph: plant peak in <b>June</b> (about 60), animal peak in <b>October</b> (about 40).</p>
<p>The south has its seasons 6 months later, so slide both peaks along by 6 months:</p>{_seasons()}
{calc(f'plant: June + 6 {ar()} <b>December</b> (high at both ends of the graph)',
      f'animal: October + 6 {ar()} <b>April</b>')}""",
        f"""<p>Look for: big swings, plant high around December/January, animal peak around April.</p>
{calc('A: almost flat = tropical ' + cross(),
      'B: small peaks, plant peak in August = southern winter ' + cross(),
      'C: exactly the northern graph, not shifted ' + cross(),
      'E: plant peak in August, animal peak first ' + cross(),
      f'D: plant high in Dec and Jan, animal peak in April {tick()} {ar()} {boxed("D")}')}""",
    ],
    answer_text='Graph D: the northern polar pattern moved on by 6 months.',
    why={'A': 'A is almost flat, like the tropical graph. Polar regions have big swings.',
         'B': 'B’s plant peak is in August, the middle of the southern winter, and its peaks are only temperate-sized.',
         'C': 'C is the <b>northern</b> polar graph copied out. It hasn’t been shifted by 6 months.',
         'E': 'E puts the plant peak in August (southern winter), and the animal peak comes before it, but plant production always rises first.'},
    fast='South = north + 6 months. Northern polar peaks June (plant) and October (animal) become December and April: only D.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _drinks():
    rows = [('Prefer A', 122, 'b'), ('Prefer B', 103, 'g'), ('No preference', 101, 'o'), ("Don't know", 74, 'v')]
    X = lambda v: 150 + v * 3.0
    parts, lab = [], []
    for i, (name, v, f) in enumerate(rows):
        y = 40 + i * 50
        parts.append(rect(X(0), y, X(v) - X(0), 32, k='ink', fill=f, sw=1.6))
        lab.append(text(140, y + 22, name, k='ink', size=17, anchor='end'))
        lab.append(text(X(v) - 8, y + 23, v, k='ink', size=18, anchor='end'))
    parts.append(line(X(80), 28, X(80), 250, k='red', w=2.2, dash=True))
    parts.append(path(f'M{X(103) + 8} 106 q12 0 12 12 L{X(103) + 20} 144 q0 12 -12 12', k='green', sw=2.2))
    lab += [text(X(80), 270, '20% of 400 = 80', k='red', size=17, font='scrawl'),
            text(X(103) + 28, 138, '103 &gt; 101, just!', k='green', size=20, font='scrawl', anchor='start'),
            text(X(0), 24, 'add the 4 age groups (out of 400)', k='muted', size=15, anchor='start')]
    return svg(620, 280, rough(*parts) + ''.join(lab),
               'Totals out of 400: prefer A 122, prefer B 103, no preference 101, do not know 74, below the 20 percent line at 80')

Q.append(dict(
    n=5, orig=12, answer='B', topic='Tables & percentages',
    question=f"""<p>A market research company conducted a survey into the relative popularity of two soft drinks
with the following results ({hl('all figures are percentages', 'y', 1)}):</p>
{table([['Prefer Drink A', '28', '38', '32', '24'],
        ['Prefer Drink B', '20', '31', '33', '19'],
        ['No preference', '33', '12', '22', '34'],
        ["Don't know", '19', '19', '13', '23']],
       head=['', 'Age 5-15', 'Age 15-25', 'Age 25-35', 'Age over 35'])}
<p>{hl('The same number of people were surveyed in each age group', 'y', 2)}.</p>
<p class="stem">Which one of the following conclusions can be {hl('justifiably drawn', 'b', 3)} from the results?</p>""",
    options={'A': 'Drink A is consistently more popular than Drink B.',
             'B': 'There were more people with a preference for Drink B than with no preference.',
             'C': 'More people in the age group 5-15 expressed a preference than did not.',
             'D': 'Fewer people had a preference than those who did not.',
             'E': 'More than 20% of people did not know which they preferred.'},
    notes=[(1, 'y', 'Each column is out of 100.'),
           (2, 'y', 'Equal group sizes, so you can simply <b>add</b> the percentages across a row (total out of 400).'),
           (3, 'b', 'Must be definitely true from the numbers. Test each option.')],
    steps=[
        f"""<p>Add each row across the four groups (each group counts equally):</p>
{calc('Prefer A: 28 + 38 + 32 + 24 = 122', 'Prefer B: 20 + 31 + 33 + 19 = 103',
      'No preference: 33 + 12 + 22 + 34 = 101', "Don't know: 19 + 19 + 13 + 23 = 74", 'check: 122 + 103 + 101 + 74 = 400 ' + tick())}""",
        f"""{_drinks()}
{calc('A: age 25-35 has B 33 &gt; A 32, so not consistent ' + cross(),
      f'B: Drink B 103 &gt; no preference 101 {tick()}',
      'C: 5-15: preference 28 + 20 = 48, not 33 + 19 = 52 ' + cross(),
      'D: preference 225, no preference or unsure 175 ' + cross(),
      "E: don't know 74 out of 400 = 18.5% " + cross())}
{calc(f'answer = {boxed("B")}')}""",
    ],
    answer_text='B: 103 points for Drink B against 101 for no preference (out of 400).',
    why={'A': 'Not consistent: in the 25-35 group Drink B (33) beats Drink A (32).',
         'C': 'In the 5-15 group, 48% had a preference but 52% did not (33 + 19).',
         'D': 'The other way round: 225 out of 400 had a preference, only 175 did not.',
         'E': '74 out of 400 is 18.5%, under 20%. Two columns show 19 and one 23, which tempts you, but the average is below 20.'},
    fast='Same group sizes, so add rows: B 103, no preference 101. B is true. Quick-check E: 74 ÷ 4 = 18.5%, under 20.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _tariff():
    X = lambda u: 80 + (u - 50) * 4.7
    Yc = lambda c: 300 - (c - 30) * 11.5
    parts, lab = [line(X(50), Yc(30), X(162), Yc(30), k='ink', head=True),
                  line(X(50), Yc(30), X(50), Yc(51.5), k='ink', head=True)], []
    for u in range(50, 161, 25):
        lab.append(text(X(u), Yc(30) + 22, u, k='muted', size=15))
    for c in range(30, 51, 5):
        lab.append(text(X(50) - 8, Yc(c) + 5, f'£{c}', k='muted', size=15, anchor='end'))
    parts.append(line(X(50), Yc(35), X(160), Yc(46), k='pen', w=2.4))
    parts.append(line(X(50), Yc(30), X(150), Yc(50), k='orange', w=2.4))
    old = [(125, 42.5), (150, 45), (130, 43), (110, 41), (95, 39.5), (75, 37.5), (60, 36), (70, 37)]
    new = [(80, 36), (100, 40), (110, 42), (130, 46)]
    for u, c in old:
        parts.append(circle(X(u), Yc(c), 5.5, k='pen', fill='b', sw=2))
    for u, c in new:
        parts.append(circle(X(u), Yc(c), 5.5, k='orange', fill='o', sw=2))
    parts += [circle(X(80), Yc(36), 13, k='red', sw=2.4),
              line(X(80), Yc(36) - 14, X(80), Yc(38) + 6, k='red', w=2, dash=True),
              circle(X(100), Yc(40), 13, k='violet', sw=2)]
    lab += [text(X(80) + 18, Yc(36) + 30, 'Sep: £36, but old tariff says £38', k='red', size=17, anchor='start'),
            text(X(100) - 16, Yc(40) - 24, 'Oct fits both', k='violet', size=16, anchor='end'),
            circle(X(50) + 26, 52, 6, k='pen', fill='b', sw=2),
            text(X(50) + 40, 58, 'Jan–Aug: old, £30 + 10p a unit', k='pen', size=17, anchor='start'),
            circle(X(50) + 26, 82, 6, k='orange', fill='o', sw=2),
            text(X(50) + 40, 88, 'Sep–Dec: new, £20 + 20p a unit', k='orange', size=17, anchor='start'),
            text(X(105), Yc(30) + 44, 'units used', k='ink', size=15)]
    return svg(620, 356, rough(*parts) + ''.join(lab),
               'Charge against units: January to August lie on the old line (30 pounds plus 10p a unit), September to December on the new line (20 pounds plus 20p a unit)')

Q.append(dict(
    n=6, orig=13, answer='D', topic='Bills & tariffs',
    question=f"""<p>My monthly electricity bill is calculated as a {hl('standing charge plus an amount per unit used', 'y', 1)}. At
the beginning of one month my electricity company decided to change the tariff by {hl('reducing the standing charge and increasing the cost per unit', 'y', 2)}. This was intended to help customers who use
less electricity.</p>
<p>The table below shows my consumption and monthly charges for the whole year.</p>
{table([['Jan', '125', '42.50', 'Jul', '60', '36.00'],
        ['Feb', '150', '45.00', 'Aug', '70', '37.00'],
        ['Mar', '130', '43.00', 'Sep', '80', '36.00'],
        ['Apr', '110', '41.00', 'Oct', '100', '40.00'],
        ['May', '95', '39.50', 'Nov', '110', '42.00'],
        ['June', '75', '37.50', 'Dec', '130', '46.00']],
       head=['Month', 'Units used', 'Charge (£)', 'Month', 'Units used', 'Charge (£)'])}
<p class="stem">At the {hl('beginning of which month', 'b', 3)} was the tariff changed?</p>""",
    options={'A': 'February', 'B': 'April', 'C': 'August', 'D': 'September', 'E': 'December'},
    notes=[(1, 'y', 'Bill = fixed amount + (price per unit × units). Two months on the same tariff give both numbers.'),
           (2, 'y', 'After the change: smaller fixed amount, bigger price per unit.'),
           (3, 'b', 'Find the first month that does not fit the old tariff.')],
    steps=[
        f"""<p>Find the old tariff from January and February:</p>
{calc(f'25 more units cost £2.50 more {ar()} <b>10p a unit</b>',
      f'standing charge = £42.50 − 125 × 10p = £42.50 − £12.50 = <b>£30</b>')}""",
        f"""<p>Test each month with £30 + 10p a unit:</p>
{calc('Mar 30 + 13 = 43 ' + tick() + ' · Apr 30 + 11 = 41 ' + tick() + ' · May 30 + 9.50 = 39.50 ' + tick(),
      'Jun 30 + 7.50 = 37.50 ' + tick() + ' · Jul 30 + 6 = 36 ' + tick() + ' · Aug 30 + 7 = 37 ' + tick(),
      f'Sep 30 + 8 = 38, but the bill is £36 {cross()} {ar()} changed in <b>September</b>')}""",
        f"""<p>Check with the new tariff from October and November: 10 more units cost £2 more, so 20p a unit and a standing charge of £40 − £20 = £20.</p>
{calc('Sep 20 + 16 = 36 ' + tick() + ' · Dec 20 + 26 = 46 ' + tick())}
{_tariff()}
{calc(f'answer = {boxed("September")}')}
{note('October (100 units, £40) fits <b>both</b> tariffs, because the two lines cross at 100 units. That is why you must test month by month.', 'trap')}""",
    ],
    answer_text='September: it is the first month that the old tariff (£30 + 10p a unit) does not fit.',
    why={'A': 'February fits the old tariff: 30 + 15 = £45.',
         'B': 'April fits the old tariff: 30 + 11 = £41.',
         'C': 'August fits the old tariff: 30 + 7 = £37.',
         'E': 'December is on the new tariff, but so are September to November. The change came earlier.'},
    fast='Jan and Feb give £30 + 10p a unit. Run down the months: the first that fails is September (should be £38, is £36).',
))


# ---------------------------------------------------------------- 7 (Q14)
def _two_tables():
    X = lambda v: 60 + v * 62
    parts, lab = [], []
    for y, title, lo, hi, col in ((84, "by parents' job", 1.6, 7.3, 'orange'), (194, 'by type of school', 3.8, 7.2, 'pen')):
        parts.append(line(X(0), y, X(8), y, k='ink', w=1.6))
        for v in range(0, 9):
            parts.append(line(X(v), y - 5, X(v), y + 5, k='ink', w=1.3))
            lab.append(text(X(v), y + 24, v, k='muted', size=13))
        parts.append(line(X(lo), y, X(hi), y, k=col, w=7))
        parts.append(circle(X(lo), y, 6, k=col, fill='paper', sw=2.4))
        parts.append(circle(X(hi), y, 6, k=col, fill='paper', sw=2.4))
        lab.append(text(X(0), y - 40, title, k=col, size=18, anchor='start'))
        lab.append(text(X(lo), y - 14, lo, k=col, size=16))
        lab.append(text(X(hi), y - 14, hi, k=col, size=16))
    lab += [text(X(4), 256, 'two separate tables: nothing links a child’s school to a parent’s job', k='red', size=16),
            text(X(4), 280, 'so you can only say that both factors line up with results', k='ink', size=16)]
    return svg(620, 292, rough(*parts) + ''.join(lab),
               'Two number lines of average GCSEs: by parents job from 1.6 to 7.3, by school type from 3.8 to 7.2, with no link between them')

Q.append(dict(
    n=7, orig=14, answer='E', topic='Interpreting data',
    question=f"""<p>A survey has shown the following relationships between parental occupation, type of school and
educational success at GCSE level:</p>
{table([['Professional', '7.3'], ['Managerial', '7.2'], ['Routine office work', '6.1'], ['Skilled manual', '3.3'],
        ['Semi-skilled manual', '2.4'], ['Unskilled manual', hl('1.6', 'g', 2)]],
       head=[hl('Parental occupation', 'y', 1), 'Average no. of GCSEs at Grade C or above'])}
{table([['Independent (i.e. private)', '7.2'], ['Specialist maintained schools', '7.0'], ['Local authority comprehensive', '4.3'],
        ['Local authority girls', '4.4'], ['Local authority boys', '3.8']],
       head=[hl('Type of school', 'y', 1), 'Average no. of GCSEs at Grade C or above'])}
<p class="stem">Which one of the following {hl('can be inferred', 'b', 3)} from these tables?</p>""",
    options={'A': 'All children of managerial-class parents attend independent schools.',
             'B': 'The majority of children whose parents are office workers attend independent schools.',
             'C': 'School type is more important than parental occupation in determining educational success.',
             'D': 'The parental background of children in independent schools is more restricted than that of children in comprehensive schools.',
             'E': 'Factors other than type of school attended may be important in determining educational success.'},
    notes=[(1, 'y', 'Two <b>separate</b> tables. Neither says which children go to which school.'),
           (2, 'g', 'Results swing hugely with parents’ jobs: from 7.3 down to 1.6.'),
           (3, 'b', 'Must follow from the tables alone. Cautious words like “may” are easier to support.')],
    steps=[
        f"""<p>The tables give averages for groups of children, but the two groupings are never linked.
You cannot tell whose parents are managers <b>and</b> at independent schools.</p>{_two_tables()}""",
        f"""<p>Parental occupation alone goes with very different results (7.3 against 1.6). So something other than school type
<b>may</b> matter. That is all E claims {tick()}</p>""",
        f"""<p>Every other option needs a link between the two tables, or a comparison of the two factors:</p>
{calc('A, B, D: need to know who goes to which school ' + cross(),
      'C: says which factor matters <b>more</b>, which the tables cannot separate ' + cross(),
      f'answer = {boxed("E")}')}""",
    ],
    answer_text='E: parental occupation also lines up with results, so other factors may matter.',
    why={'A': '“All” is far too strong, and the tables never say where managers’ children go to school. Two averages of about 7.2 being similar proves nothing.',
         'B': 'Nothing links office workers to any school type. (Their 6.1 average is not the independent 7.2 anyway.)',
         'C': 'The tables can’t separate the two factors, because the same children appear in both. If anything, parental occupation shows the bigger spread.',
         'D': 'There is no information about the backgrounds of children in each type of school.'},
    fast='Two unlinked tables: rule out anything about who attends which school (A, B, D) or which factor wins (C). E only says “may”.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _rooms():
    caps = [26, 20, 24, 28, 24, 20, 24, 16, 20, 18, 26]
    s, base, x = 5.0, 200, 24
    parts, lab = [], []
    gap = 3.3
    for c in caps:
        h = c * s
        parts.append(rect(x, base - h, 40, h, k='ink', fill='paper', sw=1.6))
        parts.append(rect(x, base - h + gap * s, 40, h - gap * s, k='ink', fill='b', sw=1.2))
        lab.append(text(x + 20, base + 20, c, k='ink', size=15))
        x += 48
    parts.append(line(20, base, x, base, k='ink', w=2))
    lab += [text(300, 30, 'every room: the same empty strip on top', k='red', size=23, font='scrawl'),
            text(300, 248, 'desks: 246 in total. Students: 420 − 210 = 210', k='ink', size=16),
            text(300, 272, 'empty: 246 − 210 = 36, shared by 11 rooms (blue = students)', k='pen', size=16)]
    return svg(600, 284, rough(*parts) + ''.join(lab),
               'Eleven room bars of different heights, each with the same empty strip at the top; 246 desks, 210 students, 36 empty')

Q.append(dict(
    n=8, orig=18, answer='C', topic='Choosing a method',
    question=f"""<p>There are {hl('420 candidates', 'g', 1)} sitting a public exam in a college. The sports hall can accommodate
{hl('210 students', 'g', 1)}; once this has been filled there are other rooms available that are much smaller.
The following is a list of the number of single desks that have been set up in each room:</p>
<p>{hl('26, 20, 24, 28, 24, 20, 24, 16, 20, 18, 26', 'g', 2)}.</p>
<p>The rooms have sufficient space for all the candidates who are not in the sports hall. The
exams officer wants to {hl('leave the same number of empty desks in each of these rooms', 'b', 3)}.</p>
<p class="stem">What {hl('procedure', 'p', 4)} should the exams officer adopt to work out how many students to have in each
room?</p>""",
    options={'A': 'Divide the total number of candidates by the total number of workspaces in each room and take that number away from the capacity of each of the rooms.',
             'B': 'Add up the total capacity of the rooms, subtract that number from the total number of candidates, divide the result by the total number of rooms and then subtract that number from the capacity of each room.',
             'C': 'Add up the total capacity of the rooms, subtract the total number of candidates from that figure, divide the result by the total number of rooms and subtract that number from the capacity of each room.',
             'D': 'Divide the total capacity by the number of students and then take that number away from the capacity of each room.',
             'E': 'Add up the total capacity of the rooms and divide by the total number of candidates. Multiply the result by the total number of rooms, which gives the number of students to place in each room.'},
    notes=[(1, 'g', 'The sports hall takes 210, so 420 − 210 = 210 go into the small rooms.'),
           (2, 'g', '11 rooms. Total capacity 246.'),
           (3, 'b', 'Equal <b>empty</b> desks, not equal students. Students in a room = its capacity − empty desks.'),
           (4, 'p', 'They want the method, so do it with the numbers, then match the steps.')],
    steps=[
        f"""<p>Do it with the real numbers first:</p>
{calc('total desks: 26 + 20 + 24 + 28 + 24 + 20 + 24 + 16 + 20 + 18 + 26 = 246',
      'candidates for these rooms: 420 − 210 = 210',
      f'empty desks overall: 246 − 210 = 36 {ar()} capacity <b>minus</b> candidates',
      f'empty desks per room: 36 ÷ 11 {ar()} divide by the number of rooms',
      f'students in a room = its capacity − that number')}""",
        f"""{_rooms()}
<p>That is exactly option C, step for step: add capacities, subtract candidates, divide by rooms, subtract from each room’s capacity.</p>
{calc(f'answer = {boxed("C")}')}
{note('36 ÷ 11 isn’t a whole number (about 3.3), so in practice you’d leave about 3 empty desks per room. The question only asks for the method. “Candidates” here means the 210 not in the sports hall.', 'check')}""",
    ],
    answer_text='C: (total capacity − candidates) ÷ number of rooms gives the empty desks per room; subtract from each capacity.',
    why={'A': 'Candidates ÷ desks (210 ÷ 246 ≈ 0.85) is a fraction, not a number of desks. Taking 0.85 away from a room size is meaningless.',
         'B': 'B subtracts the wrong way round: 210 − 246 = −36. Taking away a negative would <b>add</b> desks.',
         'D': 'Capacity ÷ students (246 ÷ 210 ≈ 1.2) is a ratio, not a count of empty desks.',
         'E': 'E gives the <b>same</b> number of students in every room (246 ÷ 210 × 11 ≈ 13), which can’t leave equal empty desks in rooms of different sizes.'},
    fast='Empty desks per room = (capacity − candidates) ÷ rooms; students = capacity − that. Only C says it in that order.',
))
