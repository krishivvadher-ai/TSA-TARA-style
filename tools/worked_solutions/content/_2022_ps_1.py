from wslib import *

Y = 2022
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _quiz():
    sc = [14, 16, 6, 20, 10, 18, 4]
    parts, lab = [], []
    x0, w = 22, 86
    for i, s in enumerate(sc):
        x = x0 + i * w
        f = 'y' if i == 2 else 'g' if i in (1, 3) else 'paper'
        parts.append(rect(x, 44, w - 8, 54, k='ink', fill=f, sw=1.6))
        lab.append(text(x + (w - 8) / 2, 34, f'round {i + 1}', k='muted', size=15))
        lab.append(text(x + (w - 8) / 2, 80, s, k='ink', size=24))
        if i in (1, 2, 3):
            m = '×3' if i == 2 else '×2'
            extra = 2 * s if i == 2 else s
            lab.append(text(x + (w - 8) / 2, 124, m, k='red', size=24, font='scrawl'))
            lab.append(text(x + (w - 8) / 2, 150, f'+{extra} extra', k='pen', size=17))
    parts.append(brace(x0 + w, x0 + 4 * w - 8, 160, 'extra = 16 + 12 + 20 = 48', k='red', size=18))
    lab.append(text(320, 232, 'normal total 88  +  extra 48  =  136 ✓', k='green', size=23, font='scrawl'))
    return svg(640, 246, rough(*parts) + ''.join(lab),
               'Seven rounds with round 3 tripled and rounds 2 and 4 doubled: the extra points are 16, 12 and 20, which is 48, and 88 plus 48 is 136')


Q.append(dict(
    n=1, orig=2, answer='B', topic='Arithmetic & trial',
    question=f"""<p>A quiz consists of 7 rounds, each of which contains 20 questions. Each question is worth one
point. At the end of the quiz, but before any of the answers or scores are revealed, each team
is allowed to select one of the rounds and {hl('the score for that round is tripled', 'y', 1)}. In addition, {hl('the scores for the rounds immediately before and after the chosen round are doubled', 'y', 2)}. The winning
team at last week’s quiz had the following scores in each of the rounds.</p>
{table([['<i>score</i>', '14', '16', '6', '20', '10', '18', '4']], head=['<i>round</i>', '1', '2', '3', '4', '5', '6', '7'])}
<p>The winning team’s {hl('final score was 136', 'g', 3)}.</p>
<p class="stem">{hl('Which round', 'b', 4)} did the winning team choose to have the score tripled?</p>""",
    options={'A': 'round 2', 'B': 'round 3', 'C': 'round 4', 'D': 'round 5', 'E': 'round 6'},
    notes=[(1, 'y', 'Tripled = the round counts 3 times, so it adds <b>2 extra</b> lots of its score.'),
           (2, 'y', 'Doubled = each neighbour adds <b>1 extra</b> lot of its own score.'),
           (3, 'g', 'Compare 136 with the normal total to see how many extra points there were.'),
           (4, 'b', 'Only 5 choices (rounds 2 to 6). Just test them.')],
    steps=[
        f"""<p>Normal total first (no tripling or doubling):</p>
{calc('14 + 16 + 6 + 20 + 10 + 18 + 4 = <b>88</b>', f'136 − 88 = <b>48 extra points</b> to find')}""",
        f"""<p>Choosing a round gives extra = 2 × (that round) + (round before) + (round after). Try round 3:</p>
{_quiz()}""",
        f"""<p>Check the other options too (it only takes a few seconds):</p>
{calc(f'round 2: 2 × 16 + 14 + 6 = 52 {ar()} 140', f'round 3: 2 × 6 + 16 + 20 = 48 {ar()} 136 ' + tick(),
      f'round 4: 2 × 20 + 6 + 10 = 56 {ar()} 144', f'round 5: 2 × 10 + 20 + 18 = 58 {ar()} 146',
      f'round 6: 2 × 18 + 10 + 4 = 50 {ar()} 138')}
{calc(f'answer: {boxed("round 3")}')}
{note('Work with the <b>extra</b> points (48), not the whole new total. The numbers stay small and you add up the 7 rounds only once.', 'tip')}""",
    ],
    answer_text='Round 3: the extra points are 12 + 16 + 20 = 48, and 88 + 48 = 136.',
    why={'A': 'Round 2 gives 2 × 16 + 14 + 6 = 52 extra, so a final score of 140.',
         'C': 'Round 4 gives 2 × 20 + 6 + 10 = 56 extra, so 144. Choosing the highest-scoring round feels right but gives too much.',
         'D': 'Round 5 gives 2 × 10 + 20 + 18 = 58 extra, so 146.',
         'E': 'Round 6 gives 2 × 18 + 10 + 4 = 50 extra, so 138. Close, but not 136.'},
    fast='Normal total 88, so 48 extra. Extra = 2 × chosen + both neighbours. Round 3: 12 + 16 + 20 = 48.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _seesaw():
    X = lambda p: 60 + (p - 30) * 10
    parts, lab = [], []
    parts += [line(X(36), 128, X(76), 128, k='ink', w=3.5),
              poly([(X(50), 130), (X(50) - 16, 162), (X(50) + 16, 162)], k='ink', fill='y', sw=2),
              line(X(32), 162, X(78), 162, k='muted', w=1.6),
              rect(X(40) - 52, 50, 104, 76, k='orange', fill='o', sw=2, rx=6),
              rect(X(70) - 32, 88, 64, 38, k='pen', fill='b', sw=2, rx=6)]
    lab += [text(X(40), 80, 'mixture 1', k='ink', size=16), text(X(40), 108, '4 litres', k='orange', size=22, font='scrawl'),
            text(X(70), 80, 'mixture 2', k='ink', size=16), text(X(70), 114, '2 L', k='pen', size=22, font='scrawl')]
    for p, name in ((40, '40% apple'), (50, '50% apple'), (70, '70% apple')):
        parts.append(line(X(p), 168, X(p), 180, k='ink', w=1.8))
        lab.append(text(X(p), 200, name, k='green' if p == 50 else 'ink', size=17))
    parts.append(line(X(40), 214, X(50), 214, k='red', head=True, tail=True, w=2))
    parts.append(line(X(50), 214, X(70), 214, k='red', head=True, tail=True, w=2))
    lab += [text(X(45), 236, '10 away', k='red', size=17), text(X(60), 236, '20 away', k='red', size=17),
            text(300, 270, 'twice as far away → half as much:  4 : 2', k='green', size=21, font='scrawl')]
    return svg(600, 286, rough(*parts) + ''.join(lab),
               'A see-saw balanced at 50 percent: mixture 1 at 40 percent is 10 away and gets 4 litres, mixture 2 at 70 percent is 20 away and gets 2 litres')


Q.append(dict(
    n=2, orig=6, answer='B', topic='Mixtures & percentages',
    question=f"""<p>Rob has two different mixtures of apple juice and orange juice.</p>
<p>mixture 1&nbsp;&nbsp; {hl('40% apple juice', 'g', 1)} and 60% orange juice<br>
mixture 2&nbsp;&nbsp; {hl('70% apple juice', 'g', 1)} and 30% orange juice</p>
<p>Rob wants to use these two mixtures to make {hl('6 litres', 'g', 2)} of a juice mixture which is {hl('50% apple juice', 'y', 3)} and 50% orange juice.</p>
<p class="stem">How much of {hl('mixture 2', 'b', 4)} does Rob need to use?</p>""",
    options={'A': '1 litre', 'B': '2 litres', 'C': '3 litres', 'D': '4 litres', 'E': '5 litres'},
    notes=[(1, 'g', 'Just follow the <b>apple</b>. If the apple comes out right, the orange is right too.'),
           (2, 'g', 'Total volume. Half of it (3 litres) must be apple.'),
           (3, 'y', '50% is nearer to 40% than to 70%, so he needs <b>more</b> of mixture 1.'),
           (4, 'b', 'They want the 70% one, which is the smaller share.')],
    steps=[
        f"""<p>Target: 50% of 6 litres = <b>3 litres of apple</b>.</p>
<p>Think of a see-saw. The mix sits at 50%, which is 10 away from mixture 1 and 20 away from mixture 2.
The nearer mixture must be the heavier one:</p>{_seesaw()}""",
        f"""<p>So mixture 1 : mixture 2 = 20 : 10 = <b>2 : 1</b>. Split 6 litres in the ratio 2 : 1:</p>
{calc('6 ÷ 3 = 2 litres per share', f'mixture 1 = 4 litres, mixture 2 = {boxed("2 litres")}')}""",
        f"""<p>Check the apple:</p>
{calc('4 × 40% = 1.6 litres', '2 × 70% = 1.4 litres', f'1.6 + 1.4 = 3 litres = half of 6 ' + tick())}
{note('No ratio trick needed: just test the options. 2 litres of mixture 2 means 4 of mixture 1, and the apple is 1.6 + 1.4 = 3. Done.', 'tip')}""",
    ],
    answer_text='2 litres of mixture 2 (with 4 litres of mixture 1).',
    why={'A': '1 litre of mixture 2 + 5 of mixture 1 gives 0.7 + 2.0 = 2.7 litres of apple: only 45%.',
         'C': '3 litres of each just averages 40% and 70%, which is 55% apple, not 50%.',
         'D': '4 litres is the amount of <b>mixture 1</b>. Giving the bigger share to mixture 2 gets the ratio upside down (60% apple).',
         'E': '5 litres of mixture 2 gives 3.5 + 0.4 = 3.9 litres of apple: 65%.'},
    fast='50% is twice as close to 40% as to 70%, so the ratio is 2 : 1. A third of 6 litres = 2 litres of mixture 2.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _extensions():
    nums = [('117', 3), ('232', 1), ('239', 0), ('387', 2), ('558', 0), ('661', 2)]
    parts, lab = [], []
    for i, (n, c) in enumerate(nums):
        x = 24 + i * 100
        used = c > 0
        parts.append(rect(x, 40, 84, 54, k='ink' if used else 'red', fill='g' if used else 'p', sw=2 if used else 2.6, rx=10))
        lab.append(text(x + 42, 76, n, k='ink', size=24, font='print'))
        if used:
            lab.append(text(x + 42, 124, f'✓ used {c}×', k='green', size=18))
        else:
            lab.append(text(x + 42, 124, 'never!', k='red', size=22, font='scrawl'))
    lab += [text(24, 26, 'all the extension numbers in the table:', k='muted', size=16, anchor='start'),
            text(320, 166, 'Fran (lecturer column) never needs 239 or 558  →  2', k='red', size=20, font='scrawl')]
    return svg(640, 182, rough(*parts) + ''.join(lab),
               'The six different extension numbers; Fran uses 117, 232, 387 and 661 but never 239 or 558')


Q.append(dict(
    n=3, orig=7, answer='C', topic='Tables & counting',
    question=f"""<p>The extension numbers needed to contact eight different departments in a university depend
on whether the caller is calling as a student, parent, lecturer, journalist or researcher. The
appropriate numbers are shown below.</p>
{table([['Accounts', '387', '387', hl('661', 'b'), '387', '661'],
        ['Administration', '117', '387', hl('117', 'b'), '232', '232'],
        ['Enquiries', '239', '387', hl('387', 'b'), '661', '387'],
        ['Complaints', '558', '239', hl('117', 'b'), '387', '117'],
        ['Quality Assurance', '239', '239', hl('117', 'b'), '558', '239'],
        ['Marketing', '387', '239', hl('232', 'b'), '661', '232'],
        ['Public Relations', '239', '117', hl('387', 'b'), '239', '232'],
        ['Human Resources', '239', '239', hl('661', 'b'), '117', '239']],
       head=['', '<i>student</i>', '<i>parent</i>', hl('<i>lecturer</i>', 'y', 3), '<i>journalist</i>', '<i>researcher</i>'])}
<p>{hl('Fran is a lecturer', 'y', 1)} and regularly needs to contact all of the departments in the university.</p>
<p class="stem">How many of the extension numbers are {hl('<b>never</b>', 'b', 2)} needed by Fran?</p>""",
    options={'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4'},
    notes=[(1, 'y', 'Only the lecturer column matters for Fran.'),
           (2, 'b', 'Numbers that appear somewhere in the table but <b>not</b> in Fran’s column.'),
           (3, 'y', 'Read down this one column only. The neighbouring columns are traps.')],
    steps=[
        f"""<p>List every different number in the whole table: 117, 232, 239, 387, 558, 661. That’s <b>6</b> numbers.</p>""",
        f"""<p>Now read down the lecturer column:</p>
{calc('661, 117, 387, 117, 117, 232, 387, 661', f'Fran uses {ar()} 117, 232, 387, 661 (4 numbers)')}""",
        f"""<p>Tick them off:</p>{_extensions()}
{calc(f'6 − 4 = {boxed("2")} numbers never needed')}
{note('Each wrong option matches reading the wrong column: journalist uses all 6 (answer 0), researcher misses only 558 (answer 1), parent misses 3. Keep your finger on the lecturer column.', 'trap')}""",
    ],
    answer_text='2: Fran never needs 239 or 558.',
    why={'A': '0 is what you get from the <b>journalist</b> column, which uses all six numbers.',
         'B': '1 comes from the <b>researcher</b> column (only 558 is missing), or from spotting 558 but missing 239.',
         'D': '3 comes from the <b>parent</b> column (232, 558 and 661 missing).',
         'E': '4 is how many numbers Fran <b>does</b> use, not how many she never uses.'},
    fast='Six different numbers overall. Lecturer column uses 117, 232, 387, 661. Missing: 239 and 558, so 2.',
))


# ---------------------------------------------------------------- 4 (Q8)
def _chain():
    vals = [(2013, '16/18', 89), (2014, '20/25', 80), (2015, '35/50', 70), (2016, '45/90', 50),
            (2017, '70/120', 58), (2018, '100/200', 50), (2019, '130/270', 48)]
    Yv = lambda v: 250 - v * 2
    parts, lab = [line(50, Yv(0), 600, Yv(0), k='ink', w=2)], []
    parts.append(line(50, Yv(50), 600, Yv(50), k='muted', w=1.4, dash=True))
    lab.append(text(46, Yv(50) + 5, '50%', k='muted', size=14, anchor='end'))
    for i, (yr, fr, v) in enumerate(vals):
        x = 66 + i * 76
        f = 'y' if yr in (2017, 2019) else 'b'
        parts.append(rect(x, Yv(v), 50, Yv(0) - Yv(v), k='ink', fill=f, sw=1.6))
        lab.append(text(x + 25, Yv(v) - 8, f'{v}%', k='ink', size=18))
        lab.append(text(x + 25, Yv(0) + 20, yr, k='muted', size=14))
        lab.append(text(x + 25, Yv(0) + 40, fr, k='pen', size=14))
    lab += [text(66 + 4 * 76 + 25, 28, 'goes UP!', k='red', size=20, font='scrawl'),
            text(66 + 6 * 76 + 20, 120, 'just under ½', k='red', size=17, font='scrawl'),
            text(330, 318, 'chain shops as a % of each year’s total (the black part)', k='ink', size=16)]
    parts.append(arrow(66 + 4 * 76 + 25, 36, 66 + 4 * 76 + 25, Yv(58) - 26, k='red', bend=0.1))
    return svg(620, 332, rough(*parts) + ''.join(lab),
               'Chain shops as a percentage of each year: 89, 80, 70, 50, 58, 50, 48; it rises in 2017 and ends just under half')


Q.append(dict(
    n=4, orig=8, answer='B', topic='Charts & percentages',
    question=f"""<p>Over the past decade the popularity of coffee has soared in the United Kingdom. As a result,
the number of coffee shops across the UK has risen. The table below shows a breakdown of
the number of chain and independent coffee shops in East London between 2013 and 2019.</p>
{table([['<i>chain</i>', '16', '20', '35', '45', '70', '100', '130'],
        ['<i>independent</i>', '2', '5', '15', '45', '50', '100', '140'],
        [hl('<i>total</i>', 'g', 2), hl('18', 'g'), hl('25', 'g'), hl('50', 'g'), hl('90', 'g'), hl('120', 'g'), hl('200', 'g'), hl('270', 'g')]],
       head=['', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])}
<p class="stem">{hl('Which graph shows the information', 'b', 1)} in the table above?</p>
{fig(Y, 'ps_q04_graphs', 'Key: grey = independent coffee shops, black = chain coffee shops. Five stacked bar charts A to E, each bar going up to 100, for 2013 to 2019', 640)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'b', 'Every bar reaches 100, so the graphs show <b>percentages</b> of each year’s shops, not numbers. Black = chain.'),
           (2, 'g', 'Use the totals to turn chain shops into a percentage.')],
    steps=[
        f"""<p>Every bar is full height (100), so each bar shows the <b>share</b> of that year’s shops. From the key, the black part is chain shops.</p>""",
        f"""<p>Chain share = chain ÷ total:</p>
{calc('2013: 16 ÷ 18 ≈ 89%', '2014: 20 ÷ 25 = 80%', '2015: 35 ÷ 50 = 70%', '2016: 45 ÷ 90 = 50%',
      '2017: 70 ÷ 120 ≈ 58%', '2018: 100 ÷ 200 = 50%', '2019: 130 ÷ 270 ≈ 48%')}
{_chain()}""",
        f"""<p>Now look for the two giveaways: black <b>rises</b> in 2017, and 2019 is <b>just under 50</b>.</p>
{calc(f'A: keeps falling after 2016 {cross()}', f'C: 2017 too high (about 63), 2019 too low (about 43) {cross()}',
      f'D, E: black starts at about 11%: that’s the independent share {cross()}', f'B: 89, 80, 70, 50, 58, 50, 48 {tick()}')}
{calc(f'answer: {boxed("graph B")}')}""",
    ],
    answer_text='Graph B: chain shops fall from 89% to 50%, rise to 58% in 2017, then 50% and 48%.',
    why={'A': 'A keeps falling after 2016 (about 40%, 32%, 31%). But in 2017 chain shops are 70 of 120, which is more than half.',
         'C': 'C has the right shape, but 2017 is too high (about 63%, not 58%) and 2019 too low (about 43%, not 48%).',
         'D': 'D starts with black at about 11%. In 2013 the chain shops were 16 of 18, nearly all of them.',
         'E': 'E is the <b>independent</b> share drawn in black: the colours are swapped. The key says black is chain.'},
    fast='2013: 16 of 18 is about 89% chain (kills D and E). 2017: 70 of 120 is 58%, up from 50% (kills A). 2019: 130 of 270 is just under half (kills C).',
))


# ---------------------------------------------------------------- 5 (Q12)
def _bottles():
    parts, lab = [], []

    def bottle(x, y, w, h, f, k):
        parts.append(path(f'M{x} {y + 30} Q{x} {y + 10} {x + w * 0.3} {y + 8} L{x + w * 0.3} {y - 4} '
                          f'L{x + w * 0.7} {y - 4} L{x + w * 0.7} {y + 8} Q{x + w} {y + 10} {x + w} {y + 30} '
                          f'L{x + w} {y + h} L{x} {y + h} Z', k=k, fill=f, sw=2.2))
        parts.append(rect(x + w * 0.27, y - 18, w * 0.46, 16, k='ink', fill='paper', sw=1.8, rx=3))

    bottle(70, 60, 90, 130, 'b', 'pen')
    bottle(370, 54, 96, 136, 'o', 'orange')
    lab += [text(115, 120, '500 ml', k='ink', size=17), text(115, 150, '£1.96', k='ink', size=22, font='scrawl'),
            text(418, 120, '550 ml', k='ink', size=17), text(418, 150, '£1.60', k='ink', size=22, font='scrawl'),
            text(115, 30, 'normal', k='pen', size=19), text(418, 26, 'new', k='orange', size=19),
            text(470, 168, '(1.96 − 0.36)', k='muted', size=14, anchor='start')]
    parts.append(rect(115 - 80, 212, 160, 18, k='pen', fill='b', sw=1.6))
    parts.append(rect(418 - 50, 212, 100, 18, k='orange', fill='o', sw=1.6))
    lab += [text(115, 252, 'lasts 40 days', k='pen', size=17), text(418, 252, 'lasts only 25 days', k='orange', size=17),
            text(115, 282, '196 ÷ 40 = 4.9p a day', k='pen', size=19), text(418, 282, '160 ÷ 25 = 6.4p a day', k='orange', size=19),
            text(300, 318, '6.4 − 4.9 = 1.5p a day cheaper to stick with normal', k='green', size=21, font='scrawl')]
    return svg(620, 332, rough(*parts) + ''.join(lab),
               'Normal bottle 1.96 pounds lasting 40 days costs 4.9p a day; new bottle 1.60 pounds lasting 25 days costs 6.4p a day; difference 1.5p')


Q.append(dict(
    n=5, orig=12, answer='A', topic='Best value & rates',
    question=f"""<p>The shampoo that I normally buy costs {hl('£1.96', 'g', 1)} for a {hl('500 ml', 'p', 2)} bottle and always {hl('lasts for 40 days', 'g', 1)}.</p>
<p>Last month I decided to try a new brand that is {hl('36p cheaper', 'g', 3)} and contains {hl('550 ml', 'p', 2)}. However,
because of the amount that I have had to use to wash my hair properly, it has {hl('run out after only 25 days', 'g', 4)}.</p>
<p class="stem">Based upon my experience, by how many {hl('pence per day', 'b', 5)} is my normal shampoo better value
than the new brand?</p>""",
    options={'A': '1.5', 'B': '2.4', 'C': '4.9', 'D': '6.4', 'E': '9.5'},
    notes=[(1, 'g', 'Normal: 196p over 40 days.'),
           (2, 'p', 'The ml are a distraction. What matters is how many <b>days</b> each bottle lasts.'),
           (3, 'g', 'New price = 196 − 36 = <b>160p</b>.'),
           (4, 'g', 'New: 160p over 25 days.'),
           (5, 'b', 'Cost per day for each, then the <b>difference</b>.')],
    steps=[
        f"""<p>Cost per day = price ÷ days it lasts. Work in pence.</p>{_bottles()}""",
        f"""{calc('normal: 196 ÷ 40 = 4.9p a day', 'new: 160 ÷ 25 = 6.4p a day', f'difference: 6.4 − 4.9 = {boxed("1.5p")}')}
{note('196 ÷ 40: 200 ÷ 40 = 5, then take off 4 ÷ 40 = 0.1, so 4.9. And 160 ÷ 25 = 160 × 4 ÷ 100 = 6.4.', 'tip')}""",
    ],
    answer_text='1.5p a day: 4.9p (normal) against 6.4p (new).',
    why={'B': '2.4 uses the new price for both: 160 ÷ 25 − 160 ÷ 40 = 6.4 − 4.0.',
         'C': '4.9 is the normal shampoo’s cost per day, not the difference.',
         'D': '6.4 is the new shampoo’s cost per day, not the difference.',
         'E': '9.5 is far too big: the daily costs are only 4.9p and 6.4p, so the gap must be less than 6.4p.'},
    fast='196 ÷ 40 = 4.9p. (196 − 36) ÷ 25 = 6.4p. Difference 1.5p. Ignore the ml.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _cottages():
    rows = [('Acorns', '3', 'n', 'y', 'n', 'y', 2, '$460'),
            ('Beeches', '3', 'y', 'y', 'n', 'y', 3, '$490'),
            ('Chestnuts', '4', 'n', 'y', 'y', 'y', 3, '$510'),
            ('Denders', '4', 'y', 'y', 'y', 'n', 3, '$500'),
            ('Eglers', '2', 'n', 'y', 'y', 'y', 3, '$450')]
    cols = [150, 222, 288, 360, 440, 516, 590]
    heads = ['beds', 'garden', 'wifi', 'parking', 'store ≤ 3 km', 'wishes', 'cost']
    parts, lab = [], []
    for x, h in zip(cols, heads):
        lab.append(text(x, 30, h, k='muted', size=15))
    for i, (name, beds, *w, n, cost) in enumerate(rows):
        y = 64 + i * 40
        lab.append(text(20, y, name, k='ink', size=18, anchor='start'))
        lab.append(text(cols[0], y, beds, k='red' if beds == '2' else 'ink', size=18))
        for x, v in zip(cols[1:5], w):
            lab.append(text(x, y, '✓' if v == 'y' else '✗', k='green' if v == 'y' else 'red', size=20))
        lab.append(text(cols[5], y, n, k='green' if n >= 3 else 'red', size=20, weight=700))
        lab.append(text(cols[6], y, cost, k='ink', size=18))
        parts.append(line(14, y + 14, 626, y + 14, k='muted', w=1))
    parts.append(line(14, 64 + 4 * 40 - 6, 626, 64 + 4 * 40 - 6, k='red', w=2.6))
    parts.append(rect(cols[6] - 34, 64 + 40 - 24, 68, 34, k='green', sw=2.6, rx=14))
    parts.append(rect(cols[5] - 22, 64 - 24, 44, 34, k='red', sw=2, rx=14))
    lab += [text(320, 286, 'Eglers: only 2 bedrooms, out!   Acorns: only 2 wishes', k='red', size=18, font='scrawl'),
            text(320, 314, 'suitable: Beeches $490, Denders $500, Chestnuts $510 → cheapest Beeches', k='green', size=18, font='scrawl')]
    return svg(640, 328, rough(*parts) + ''.join(lab),
               'Checklist of wishes for each cottage: Eglers out for bedrooms, Acorns meets only 2 wishes, Beeches, Chestnuts and Denders meet 3; Beeches is the cheapest')


Q.append(dict(
    n=6, orig=13, answer='B', topic='Tables & rules',
    question=f"""<p>Kate and Tek are choosing a cottage to rent for their family holiday. They have searched online
and reduced their choice to five cottages. The facilities offered by these cottages are shown in
the following table.</p>
{table([['Acorns', '3', 'no', 'yes', 'no', 'yes', '2 km', '$460'],
        ['Beeches', '3', 'yes', 'yes', 'no', 'yes', '1 km', '$490'],
        ['Chestnuts', '4', 'no', 'yes', 'yes', 'no', '2 km', '$510'],
        ['Denders', '4', 'yes', 'yes', 'yes', 'no', '4 km', '$500'],
        ['Eglers', '2', 'no', 'yes', 'yes', 'no', '2 km', '$450']],
       head=['<i>cottage</i>', '<i>number of bedrooms</i>', '<i>large garden</i>', '<i>wifi</i>', '<i>parking</i>',
             hl('<i>pets allowed</i>', 'p', 4), '<i>distance to nearest store</i>', '<i>cost per week</i>'])}
<p>Ideally, Kate and Tek would like a cottage with at least three bedrooms, {hl('a large garden, wifi, parking, and they would like to be within 3 km of a store', 'g', 2)}. They realise that it is unlikely that all
their wishes will be met, so they decide to compromise. They insist that the cottage {hl('must have at least three bedrooms', 'y', 1)}, but they will be happy if {hl('at least three of their other wishes', 'y', 3)} are
satisfied. If more than one cottage is suitable, then they will choose the one that is the
{hl('cheapest', 'b', 5)} to rent.</p>
<p class="stem">Which cottage will Kate and Tek choose?</p>""",
    options={'A': 'Acorns', 'B': 'Beeches', 'C': 'Chestnuts', 'D': 'Denders', 'E': 'Eglers'},
    notes=[(1, 'y', 'A must. Anything with fewer than 3 bedrooms is out straight away.'),
           (2, 'g', 'The other wishes: garden, wifi, parking, store within 3 km. That’s <b>4</b> wishes.'),
           (3, 'y', 'They need 3 or 4 of those 4.'),
           (4, 'p', 'Pets are not on their wish list. Don’t count this column.'),
           (5, 'b', 'Only compare prices among the cottages that pass.')],
    steps=[
        f"""<p>Bedrooms first: Eglers has only 2, so it’s out (even though it’s the cheapest).</p>""",
        f"""<p>Count the 4 other wishes for each of the rest (ignore pets):</p>{_cottages()}""",
        f"""{calc(f'Beeches $490 &lt; Denders $500 &lt; Chestnuts $510', f'cheapest {ar()} {boxed("Beeches")}')}""",
    ],
    answer_text='Beeches: 3 bedrooms, garden, wifi and a store 1 km away, for $490.',
    why={'A': 'Acorns ($460) meets only 2 wishes: wifi and the store. Count “pets allowed” as a wish by mistake and it seems to pass.',
         'C': 'Chestnuts is suitable, but at $510 it is the dearest of the three that pass.',
         'D': 'Denders is suitable (the store is 4 km away, so 3 wishes), but $500 is more than Beeches.',
         'E': 'Eglers is the cheapest of all ($450) but has only 2 bedrooms, and 3 bedrooms is a must.'},
    fast='Cut Eglers (2 bedrooms). Acorns has only wifi + store. Of Beeches, Chestnuts and Denders, Beeches is cheapest at $490.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _tiles():
    parts, lab = [], []

    def word(x, y, letters, fills):
        for i, (ch, f) in enumerate(zip(letters, fills)):
            parts.append(rect(x + i * 46, y, 40, 40, k='ink', fill=f, sw=1.8, rx=4))
            lab.append(text(x + i * 46 + 20, y + 28, ch, k='ink', size=22, font='print', weight=700))

    word(30, 30, 'MOON', ['paper', 'paper', 'y', 'paper'])
    word(30, 82, 'MOAN', ['paper', 'paper', 'y', 'paper'])
    lab += [text(230, 58, '= 8', k='ink', size=22), text(230, 110, '= 7', k='ink', size=22),
            text(290, 70, 'same except O ↔ A', k='pen', size=18, anchor='start'),
            text(290, 98, 'so O is 1 more than A', k='red', size=20, anchor='start', font='scrawl')]
    word(30, 158, 'NOON', ['b', 'b', 'g', 'g'])
    parts += [brace(30, 116, 204, 'N + O', k='pen', size=16), brace(122, 208, 204, 'O + N', k='green', size=16)]
    lab += [text(230, 186, '= 10', k='ink', size=22),
            text(290, 186, 'two lots of N + O, so N + O = 5', k='pen', size=18, anchor='start')]
    word(30, 262, 'ANNA', ['b', 'b', 'g', 'g'])
    parts += [brace(30, 116, 308, 'A + N', k='pen', size=16), brace(122, 208, 308, 'N + A', k='green', size=16)]
    lab += [text(230, 290, '= ?', k='ink', size=22),
            text(290, 278, 'A + N is 1 less than O + N, so 4', k='pen', size=18, anchor='start'),
            text(290, 308, 'ANNA = 4 + 4 = 8', k='red', size=24, anchor='start', font='scrawl')]
    return svg(640, 350, rough(*parts) + ''.join(lab),
               'Letter tiles: MOON and MOAN differ only in O and A, so O is one more than A; NOON is two lots of N plus O, so N plus O is 5; ANNA is two lots of A plus N, which is 4 each, so 8')


Q.append(dict(
    n=7, orig=14, answer='C', topic='Equations & logic',
    question=f"""<p>Alex and Anita play a game where they need to form words from letters. The value of each
letter is a {hl('whole number of points (which can be 0)', 'p', 1)}. Alex and Anita earn points by adding
together the value of the letters in the words they form.</p>
<p>The value of the last three words they formed is shown in the table below.</p>
{table([['MOAN', hl('7', 'g')], ['MOON', hl('8', 'g')], ['NOON', hl('10', 'g')]], head=['<i>word</i>', '<i>value</i>'])}
<p>Anita has just formed the word ANNA.</p>
<p class="stem">What is the value of the word {hl('ANNA', 'b', 2)}?</p>""",
    options={'A': '4', 'B': '6', 'C': '8', 'D': '10', 'E': '12'},
    notes=[(1, 'p', 'You can’t find every letter exactly, and you don’t need to.'),
           (2, 'b', 'ANNA = 2 A + 2 N. You only need A + N.')],
    steps=[
        f"""<p>Compare words that are almost the same, and pair up the letters:</p>{_tiles()}""",
        f"""{calc('MOON − MOAN: O − A = 8 − 7 = 1', 'NOON: 2N + 2O = 10, so N + O = 5', 'A + N = (O − 1) + N = 5 − 1 = 4',
              f'ANNA = 2 × (A + N) = 2 × 4 = {boxed("8")}')}
{note('Try real values to check: O = 3, N = 2, A = 2, M = 0. MOAN = 7, MOON = 8, NOON = 10 ✓, ANNA = 8. Other values that fit (say O = 1, N = 4, A = 0, M = 2) also give 8.', 'check')}""",
    ],
    answer_text='8: A + N = 4, and ANNA is two lots of A + N.',
    why={'A': '4 is A + N, only half the word. ANNA has two As and two Ns.',
         'B': '6 would need A + N = 3, meaning A is 2 less than O. MOON and MOAN differ by only 1.',
         'D': '10 treats A as worth the same as O, as if ANNA were NOON.',
         'E': '12 gets the difference the wrong way round (A = O + 1), so A + N = 6. MOAN is the smaller word, so A is worth less.'},
    fast='MOON − MOAN gives O = A + 1. NOON gives N + O = 5, so N + A = 4. ANNA = 2 × 4 = 8.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _island():
    parts, lab = [], []
    # home
    parts += [rect(30, 186, 50, 40, k='ink', fill='y', sw=2), poly([(24, 188), (55, 160), (86, 188)], k='ink', fill='o', sw=2)]
    lab.append(text(55, 248, 'home', k='ink', size=17))
    # road
    parts.append(line(86, 218, 262, 218, k='ink', w=3))
    lab += [text(174, 206, '38 miles', k='ink', size=17), text(174, 244, 'fuel 38 × $1.50 = $57', k='muted', size=15),
            text(174, 266, 'same for both options!', k='red', size=16, font='scrawl')]
    # terminal
    parts.append(rect(262, 176, 70, 60, k='ink', fill='paper', sw=2))
    lab += [text(297, 202, 'port +', k='ink', size=14), text(297, 220, 'airport', k='ink', size=14)]
    # sea and island
    parts.append(rect(340, 24, 220, 250, k='pen', fill='b', sw=1.4, rx=16))
    parts.append(path('M560 70 Q624 64 632 150 Q632 240 560 240 Z', k='green', fill='g', sw=2))
    lab.append(text(598, 290, 'Sunny Island', k='green', size=16))
    # plane route
    parts.append(arrow(336, 66, 556, 66, k='orange', bend=0.06))
    parts.append(path('M430 50 L470 50 L480 44 L484 50 L470 56 L430 56 Z M448 50 L440 38 L452 38 L460 50 M448 56 L440 68 L452 68 L460 56', k='ink', fill='paper', sw=1.5))
    lab += [text(450, 96, 'plane $50', k='orange', size=17), text(450, 118, '+ car shipped $100', k='orange', size=17),
            text(450, 142, '= $150', k='orange', size=20, font='scrawl')]
    # ferry route
    parts.append(path('M410 190 L470 190 L462 204 L418 204 Z', k='ink', fill='paper', sw=1.8))
    parts.append(rect(426, 178, 26, 12, k='ink', fill='paper', sw=1.5))
    parts.append(arrow(336, 214, 556, 214, k='green', bend=0))
    lab += [text(450, 240, 'ferry, car + Sean:', k='green', size=17), text(450, 262, '$80', k='green', size=20, font='scrawl')]
    lab.append(text(330, 322, 'saving: 150 − 80 = $70 (the $57 of fuel cancels out)', k='red', size=20, font='scrawl'))
    return svg(660, 336, rough(*parts) + ''.join(lab),
               'Map: the same 38-mile drive to the port and airport for both options, then ferry for 80 dollars or plane 50 plus car shipping 100 dollars; saving 70 dollars')


Q.append(dict(
    n=8, orig=18, answer='D', topic='Money & comparing costs',
    question=f"""<p>Sean is taking his car to Sunny Island. He lives {hl('38 miles away from the mainland terminal where the seaport and airport are based', 'p', 1)}. He has researched the travel costs and come up with
two possible options. The {hl('ferry ticket (car and passenger) is $80', 'g', 2)}. Alternatively, a {hl('plane ticket is $50 and the seaport company will transport his car (port to port) for $100', 'g', 3)}. {hl('Fuel costs are $1.50 per mile', 'p', 4)}.</p>
<p class="stem">How much money will Sean {hl('save', 'b', 5)} by taking the cheaper option?</p>""",
    options={'A': '$13', 'B': '$20', 'C': '$30', 'D': '$70', 'E': '$127'},
    notes=[(1, 'p', 'The seaport and the airport are in the <b>same place</b>. He drives the same 38 miles whichever he picks.'),
           (2, 'g', 'Option 1: $80 covers both Sean and his car.'),
           (3, 'g', 'Option 2: $50 for Sean + $100 for the car = $150.'),
           (4, 'p', 'Fuel is the same for both options, so it cancels out of the saving.'),
           (5, 'b', 'Saving = dearer option − cheaper option.')],
    steps=[
        f"""<p>Draw the two journeys:</p>{_island()}""",
        f"""{calc('ferry: $80', 'plane + car shipped: $50 + $100 = $150', f'saving = 150 − 80 = {boxed("$70")}')}
{note('Anything that is the same in both options (here the 38-mile drive) can be ignored when you only want the difference.', 'tip')}""",
    ],
    answer_text='$70: the ferry ($80) is $70 cheaper than the plane plus car shipping ($150).',
    why={'A': '$13 = 70 − 57: takes the $57 of fuel off one option only. Both options need the same drive.',
         'B': '$20 = 100 − 80: compares the car shipping with the ferry and forgets Sean’s $50 plane ticket.',
         'C': '$30 = 80 − 50: compares the ferry with the plane ticket alone and forgets the $100 for the car.',
         'E': '$127 = 70 + 57: adds the fuel to the plane option only. He drives to the terminal either way.'},
    fast='Same drive both ways, so ignore fuel. Plane + car = $150, ferry = $80. Save $70.',
))
