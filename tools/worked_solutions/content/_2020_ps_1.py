from wslib import *

Y = 2020
Q = []


# small hand-drawn tick and cross for sketches (shared with the other parts)
def _tk(x, y, s=1.0):
    return path(f'M{x - 8 * s} {y - 1 * s} L{x - 2 * s} {y + 6 * s} L{x + 9 * s} {y - 9 * s}', k='green', sw=2.8)


def _cx(x, y, s=1.0):
    d = 7 * s
    return (line(x - d, y - d, x + d, y + d, k='red', w=2.8) + line(x - d, y + d, x + d, y - d, k='red', w=2.8))


# ---------------------------------------------------------------- 1 (Q2)
def _tig_blocks():
    u = 16
    parts, lab = [], []

    def blk(x, y, pts, fill, label, k='ink'):
        parts.append(rect(x, y, pts * u, 34, k=k, fill=fill, sw=1.8, rx=4))
        lab.append(text(x + pts * u / 2, y + 23, label, k='ink', size=17))
        return x + pts * u

    # the three building blocks
    lab.append(text(20, 26, 'The only building blocks:', k='ink', size=19, font='scrawl', anchor='start'))
    blk(20, 40, 5, 'y', '5')
    lab.append(text(20 + 40, 94, 'penalty', k='muted', size=15))
    blk(140, 40, 8, 'b', '8')
    lab.append(text(140 + 64, 94, 'tigdown', k='muted', size=15))
    x = blk(310, 40, 8, 'b', '8')
    blk(x, 40, 3, 'g', '+3')
    lab.append(text(310 + 88, 94, 'tigdown + transformation = 11', k='muted', size=15))
    # option B: both scores work
    lab.append(text(20, 140, '11 =', k='pen', size=20, anchor='start'))
    x = blk(70, 118, 8, 'b', '8')
    x = blk(x, 118, 3, 'g', '+3')
    parts.append(_tk(x + 24, 134))
    lab.append(text(20, 198, '21 =', k='pen', size=20, anchor='start'))
    x = blk(70, 176, 5, 'y', '5')
    x = blk(x, 176, 8, 'b', '8')
    x = blk(x, 176, 8, 'b', '8')
    parts.append(_tk(x + 24, 192))
    # a lone 3 is not allowed
    lab.append(text(20, 256, '9 =', k='red', size=20, anchor='start'))
    x = 70
    for _ in range(3):
        x = blk(x, 234, 3, 'g', '3', k='red')
        x += 6
    parts.append(_cx(x + 18, 251))
    lab.append(text(x + 40, 256, 'a 3 can only ride on its own 8', k='red', size=17, anchor='start'))
    return svg(640, 284, rough(*parts) + ''.join(lab),
               'Scoring blocks are 5, 8 and 8 plus 3; 11 is 8 plus 3 and 21 is 5 plus 8 plus 8; 9 as three 3s is not allowed')


def _tig_strip():
    bad = {1, 2, 3, 4, 6, 7, 9, 12, 14, 17}
    opt = {9: 'A', 23: 'A', 11: 'B', 21: 'B', 12: 'C', 20: 'C', 13: 'D', 14: 'D', 15: 'E', 17: 'E'}
    cw, ch, x0 = 50, 40, 20
    parts, lab = [], []
    for n in range(24):
        r, c = divmod(n, 12)
        x, y = x0 + c * cw, 30 + r * 84
        parts.append(rect(x + 2, y, cw - 4, ch, k='ink', fill='p' if n in bad else 'g', sw=1.5, rx=3))
        lab.append(text(x + cw / 2, y + 27, n, k='red' if n in bad else 'ink', size=19, font='print',
                        weight='bold' if n in opt else None))
        if n in opt:
            lab.append(text(x + cw / 2, y + ch + 22, opt[n], k='pen', size=18, font='scrawl'))
    lab.append(text(20, 20, 'green = can be scored, pink = impossible, letters = the options', k='muted', size=15, anchor='start'))
    return svg(640, 210, rough(*parts) + ''.join(lab),
               'Totals 0 to 23: impossible ones are 1, 2, 3, 4, 6, 7, 9, 12, 14 and 17; only option B has both scores possible')


Q.append(dict(
    n=1, orig=2, answer='B', topic='Scores & combinations',
    question=f"""<p>In the game of tigball, two teams compete against each other to try to score points.</p>
<p>Points are scored as follows:</p>
<p>A ‘penalty’ scores {hl('5 points', 'g')}.<br>
A ‘tigdown’ scores {hl('8 points', 'g')}.<br>
A ‘transformation’ scores {hl('3 points', 'g', 1)}, but {hl('teams only have the opportunity to achieve a transformation after scoring a tigdown', 'p', 2)}.</p>
<p>{hl('There are no other ways of scoring points.', 'y', 3)}</p>
<p class="stem">Which of the following is the only one that is a possible {hl('scoreline', 'b', 4)} in the game of tigball?</p>""",
    options={'A': '9–23', 'B': '11–21', 'C': '12–20', 'D': '13–14', 'E': '15–17'},
    notes=[(1, 'g', 'Three ways to score: 5, 8 and 3.'),
           (2, 'p', 'A 3 only comes straight after an 8. So it is never on its own: one 3 at most per tigdown.'),
           (3, 'y', 'So every score is built from blocks of <b>5</b>, <b>8</b> and <b>11</b> (8 + 3).'),
           (4, 'b', 'A scoreline is two scores. <b>Both</b> sides must be possible.')],
    steps=[
        f"""<p>Turn the rule into building blocks. A transformation is a bonus stuck onto a tigdown:</p>{_tig_blocks()}""",
        f"""<p>Mark which totals can be made from 5s, 8s and 11s:</p>
{calc('5s only: 5, 10, 15, 20', 'one 8: 8, 13, 18, 23', 'one 11: 11, 16, 21', 'two of 8/11: 16, 19, 22 … and 5 + 8 + 8 = 21')}
{_tig_strip()}""",
        f"""<p>Now check each scoreline. One impossible side kills it:</p>
{calc(f'A: 9 {cross()} (only 3 + 3 + 3)', f'B: 11 = 8 + 3 {tick()}, 21 = 5 + 8 + 8 {tick()} {ar()} {boxed("11–21")}',
      f'C: 12 {cross()}', f'D: 14 {cross()} (8 + 3 + 3 needs two tigdowns)', f'E: 17 {cross()} (11 + 3 + 3 again)')}
{note('Quick test for a number: take away 5s and see if you land on 0, 8, 11, 16, 19 or 22. For 12: 12, 7, 2. None work, so 12 is impossible.', 'tip')}""",
    ],
    answer_text='11–21: 11 = tigdown + transformation, 21 = penalty + two tigdowns.',
    why={'A': '23 = 5 + 5 + 5 + 8 is fine, but 9 would need 3 + 3 + 3: three transformations with no tigdown.',
         'C': '20 is four penalties, but 12 can’t be made: 12 − 5 = 7 and 12 − 8 = 4 don’t work, and 3 + 3 + 3 + 3 needs four tigdowns first.',
         'D': '13 = 5 + 8 is fine, but 14 = 8 + 3 + 3 uses two transformations after only one tigdown.',
         'E': '15 is three penalties, but 17 = 11 + 3 + 3 (or 5 + 3 + 3 + 3 + 3) needs transformations without tigdowns.'},
    fast='Blocks of 5, 8 and 11 only. Hunt the impossible side: 9, 12, 14, 17 all fail. 11 = 8 + 3 and 21 = 5 + 8 + 8 both work.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _zoo():
    parts, lab = [], []
    for g in range(3):
        gx = 16 + g * 142
        parts.append(rect(gx, 34, 132, 104, k='green', sw=1.8, rx=12))
        for i in range(4):
            lab.append(stick_person(gx + 18 + i * 22, 118, k='green', s=0.8))
        lab.append(stick_person(gx + 112, 118, k='orange', s=1.2))
        lab.append(text(gx + 66, 26, f'group {g + 1}', k='muted', size=15))
    lab.append(text(16 + 213, 162, '12 under-16s, so 12 ÷ 4 = 3 teachers', k='green', size=18))
    lab.append(text(16 + 213, 186, '12 × child £9.95', k='green', size=19, font='scrawl'))
    # older students
    parts.append(rect(452, 34, 180, 104, k='pen', sw=1.8, rx=12))
    for i in range(8):
        r, c = divmod(i, 4)
        lab.append(stick_person(478 + c * 42, 82 + r * 50, k='pen', s=0.9))
    lab.append(text(542, 26, 'aged 16–18', k='muted', size=15))
    lab.append(text(542, 162, 'count as adults!', k='pen', size=18))
    lab.append(text(330, 226, '8 students + 3 teachers = 11 × adult £12.95', k='orange', size=21, font='scrawl'))
    lab.append(text(542, 186, 'orange = teacher', k='orange', size=15))
    return svg(650, 244, rough(*parts) + ''.join(lab),
               'Three groups of four under-16s each with one teacher, and eight 16 to 18 year olds who pay the adult price')


Q.append(dict(
    n=2, orig=6, answer='D', topic='Prices & groups',
    question=f"""<p>A teacher is organising a trip to the local zoo for 20 students. Of the 20 students, {hl('12 are aged 11–15', 'g', 1)} and {hl('8 are 16–18 years of age', 'g', 2)}. Tickets cost {hl('£12.95 per adult (16 years of age and over)', 'y', 3)} and £9.95 per child (2–15 years of age). {hl('For every 4 students under 16 they must have one teacher supervising them', 'p', 4)}. They will take the {hl('minimum number of teachers', 'y', 5)}.</p>
<p class="stem">What was the total admissions price {hl('for the group', 'b', 6)}?</p>""",
    options={'A': '£199.00', 'B': '£223.00', 'C': '£259.00', 'D': '£261.85', 'E': '£287.75'},
    notes=[(1, 'g', '12 pay the child price.'),
           (2, 'g', '16 and over = adult. These 8 students pay the <b>adult</b> price.'),
           (3, 'y', 'Teachers are adults too: £12.95 each.'),
           (4, 'p', 'Only the <b>under-16s</b> need supervising: 12 ÷ 4 = 3 teachers. The 16–18s don’t count.'),
           (5, 'y', 'So exactly 3 teachers, no spares.'),
           (6, 'b', 'The group = students <b>and</b> teachers. Everyone needs a ticket.')],
    steps=[
        f"""<p>Picture who is going and which ticket each person needs:</p>{_zoo()}""",
        f"""<p>Add up the two kinds of ticket:</p>
{calc('children: 12 × £9.95 = 12 × £10 − 12 × 5p = £120 − 60p = <b>£119.40</b>',
      'adults: 11 × £12.95 = 11 × £13 − 11 × 5p = £143 − 55p = <b>£142.45</b>',
      f'total = £119.40 + £142.45 = {boxed("£261.85")}')}
{note('Prices ending in 95p: round up to the whole pound, then take off 5p for each ticket.', 'tip')}""",
        f"""{note('Pence check: 12 × 95p ends in 40p, 11 × 95p ends in 45p, so the total ends in 85p. Only D does!', 'check')}""",
    ],
    answer_text='£261.85: 12 child tickets (£119.40) + 11 adult tickets for 8 students and 3 teachers (£142.45).',
    why={'A': '20 × £9.95: every student at the child price and no teachers.',
         'B': '£119.40 + 8 × £12.95 = £223.00: the students are right, but the 3 teachers are forgotten.',
         'C': '20 × £12.95: every student at the adult price and no teachers.',
         'E': 'Takes 5 teachers (one per 4 of all 20 students). Only the 12 under-16s need supervising, so 3 teachers.'},
    fast='Only the 12 under-16s need teachers: 3. So 12 × 9.95 + (8 + 3) × 12.95 = 119.40 + 142.45 = £261.85 (only answer ending in 85p).',
))


# ---------------------------------------------------------------- 3 (Q7)
def _race_grid():
    data = [('Colin', [7, 2, 1, 2, 5], '4th twice'), ('Jason', [1, 3, 2, 7, 1], '5th twice'),
            ('Kyle', [3, 7, 5, 3, 7], '1st and 3rd twice'), ('Noel', [2, 5, 7, 1, 3], 'all different!'),
            ('Ray', [5, 1, 3, 5, 2], '2nd twice')]
    place = {7: '1st', 5: '2nd', 3: '3rd', 2: '4th', 1: '5th'}
    cw, ch, x0, y0 = 80, 40, 86, 44
    parts, lab = [], []
    for j in range(5):
        lab.append(text(x0 + j * cw + cw / 2, 32, f'race {j + 1}', k='muted', size=15))
    for i, (name, pts, verdict) in enumerate(data):
        y = y0 + i * ch
        good = name == 'Noel'
        lab.append(text(x0 - 10, y + 26, name, k='green' if good else 'ink', size=18, anchor='end'))
        counts = {p: pts.count(p) for p in pts}
        for j, p in enumerate(pts):
            x = x0 + j * cw
            rep = counts[p] > 1
            parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='ink', fill='g' if good else ('p' if rep else 'paper'), sw=1.4))
            lab.append(text(x + cw / 2 - 6, y + 26, place[p], k='red' if rep else 'ink', size=17))
            lab.append(text(x + cw - 6, y + 26, f'({p})', k='muted', size=14, anchor='end'))
        lab.append(text(x0 + 5 * cw + 14, y + 26, verdict, k='green' if good else 'red', size=18, font='scrawl', anchor='start'))
    lab.append(text(x0, y0 + 5 * ch + 26, '(points scored in that race)', k='muted', size=14, anchor='start'))
    return svg(650, 278, rough(*parts) + ''.join(lab),
               'Grid of each athlete’s finishing place in races 1 to 5; only Noel has five different places')


Q.append(dict(
    n=3, orig=7, answer='D', topic='Tables & scoring',
    question=f"""<p>The Pentarathon Challenge is a competition in which five athletes compete against each other in five marathon races, run on consecutive days.</p>
<p>{hl('Points are awarded in each race', 'g', 1)}, as follows:</p>
<p>first place 7 points<br>second place 5 points<br>third place 3 points<br>fourth place 2 points<br>fifth place 1 point</p>
<p>This table shows the {hl('total points', 'p', 2)} of the competitors in this year’s Pentarathon Challenge {hl('after each race', 'p')}.</p>
{table([['Colin', '7', '9', '10', '12', '17'],
        ['Jason', '1', '4', '6', '13', '14'],
        ['Kyle', '3', '10', '15', '18', '25'],
        ['Noel', '2', '7', '14', '15', '18'],
        ['Ray', '5', '6', '9', '14', '16']],
       head=['<i>name</i>', '<i>total points after race 1</i>', '<i>total points after race 2</i>', '<i>total points after race 3</i>',
             '<i>total points after race 4</i>', '<i>total points after race 5</i>'])}
<p class="stem">Who finished in a {hl('different position in each of the five races', 'b', 3)}?</p>""",
    options={'A': 'Colin', 'B': 'Jason', 'C': 'Kyle', 'D': 'Noel', 'E': 'Ray'},
    notes=[(1, 'g', 'Points tell you the place: 7 = 1st, 5 = 2nd, 3 = 3rd, 2 = 4th, 1 = 5th. Each race hands out one of each.'),
           (2, 'p', '<b>Running</b> totals! Take each column from the next to get the points for one race.'),
           (3, 'b', 'We want someone whose five race scores are 7, 5, 3, 2, 1 in some order.')],
    steps=[
        f"""<p>Undo the running totals. For each person, subtract column from column:</p>
{calc('Colin: 7, 9 − 7 = 2, 10 − 9 = 1, 12 − 10 = 2, 17 − 12 = 5',
      'Noel: 2, 7 − 2 = 5, 14 − 7 = 7, 15 − 14 = 1, 18 − 15 = 3')}""",
        f"""<p>Do the same for everyone and turn points into places:</p>{_race_grid()}""",
        f"""<p>Only Noel came 4th, 2nd, 1st, 5th and 3rd: a different place every time {ar()} {boxed('Noel')}</p>
{note('Each race gives out 7 + 5 + 3 + 2 + 1 = 18 points. Check one race: race 3 gives 1 + 2 + 5 + 7 + 3 = 18. ✓', 'check')}""",
    ],
    answer_text='Noel: 2, 5, 7, 1, 3 points, so 4th, 2nd, 1st, 5th and 3rd.',
    why={'A': 'Colin scored 7, 2, 1, 2, 5: 4th place twice (races 2 and 4).',
         'B': 'Jason scored 1, 3, 2, 7, 1: last in both race 1 and race 5.',
         'C': 'Kyle scored 3, 7, 5, 3, 7: two wins and two 3rd places. (He has the most points, but that isn’t what’s asked.)',
         'E': 'Ray scored 5, 1, 3, 5, 2: 2nd in both race 1 and race 4.'},
    fast='One of each place = 7 + 5 + 3 + 2 + 1 = 18 points in total. Only Noel finished on 18. Quick check: 2, 5, 7, 1, 3. ✓',
))


# ---------------------------------------------------------------- 4 (Q8)
def _singles():
    parts, lab = [], []
    base, s = 322, 3.0
    Yv = lambda v: base - v * s
    # left panel: 1988 and 1989 stacked bars
    parts.append(line(40, base, 250, base, k='ink', w=2))
    for v in (0, 20, 40, 60, 80):
        lab.append(text(34, Yv(v) + 5, v, k='muted', size=14, anchor='end'))
        parts.append(line(40, Yv(v), 250, Yv(v), k='muted', w=0.8, dash=True))
    bars = [(70, '1988', [(0, 40, 'y'), (40, 71, 'b'), (71, 76, 'paper')]),
            (160, '1989', [(0, 36.5, 'y'), (36.5, 71, 'b'), (71, 74, 'v'), (74, 80.5, 'paper')])]
    for x, yr, segs in bars:
        for a, b, f in segs:
            parts.append(rect(x, Yv(b), 56, (b - a) * s, k='ink', fill=f, sw=1.6))
        lab.append(text(x + 28, base + 22, yr, k='ink', size=16))
    lab += [text(98, Yv(20) + 5, '7″', k='ink', size=16), text(188, Yv(18) + 5, '7″', k='ink', size=16),
            text(98, Yv(56) + 5, '12″', k='pen', size=17), text(188, Yv(54) + 5, '12″', k='pen', size=17),
            text(130, Yv(55.5) + 6, '31', k='red', size=22, font='scrawl', anchor='start'),
            text(220, Yv(54) + 6, '35', k='red', size=22, font='scrawl', anchor='start')]
    parts.append(line(60, Yv(71), 236, Yv(71), k='red', w=1.8, dash=True))
    lab.append(text(40, 30, 'red dashes: both 12″ slices end at 71,', k='red', size=15, anchor='start'))
    lab.append(text(40, 50, 'but in 1989 it starts lower (36, not 40)', k='red', size=15, anchor='start'))
    # right panel: size of the 12-inch slice each year
    vals = [('87', 34), ('88', 31), ('89', 35), ('90', 34), ('91', 25), ('92', 18)]
    bx = 350
    parts.append(line(340, base, 630, base, k='ink', w=2))
    for i, (yr, v) in enumerate(vals):
        x = bx + i * 46
        parts.append(rect(x, Yv(v), 30, v * s, k='ink', fill='b', sw=1.6))
        lab.append(text(x + 15, Yv(v) - 6, v, k='ink', size=15))
        lab.append(text(x + 15, base + 22, f"’{yr}", k='ink', size=15))
    parts.append(arrow(bx + 15 + 46, Yv(31) - 30, bx + 15 + 92, Yv(35) - 30, k='red', bend=-0.4))
    lab.append(text(bx + 84, Yv(35) - 52, 'UP!', k='red', size=22, font='scrawl'))
    lab.append(text(485, 110, 'size of the 12″ slice (£m)', k='pen', size=17))
    return svg(650, 356, rough(*parts) + ''.join(lab),
               'Left: 1988 and 1989 bars; the 12-inch slice is 31 then 35. Right: 12-inch slice sizes 34, 31, 35, 34, 25, 18, rising from 1988 to 1989')


Q.append(dict(
    n=4, orig=8, answer='C', topic='Reading graphs',
    question=f"""<p>Between 1987 and 1992 there were four formats of singles recordings: 7", 12", cassette and CD. The accompanying graph shows {hl('how total sales of singles were split between the four different formats', 'y', 1)} in the years 1987 to 1992.</p>
{fig(Y, 'ps_q04_chart', 'Stacked bar chart of revenue from 7-inch, 12-inch, cassette and CD singles, 1987 to 1992', 460)}
<p class="stem">Which one of the following statements is {hl('false', 'b', 2)}?</p>""",
    options={'A': f'The revenue from sales of CD singles grew {hl("every year", "p", 3)}.',
             'B': f'The revenue from sales of 7" singles fell {hl("every year", "p")}.',
             'C': f'The revenue from sales of 12" singles fell {hl("every year", "p")}.',
             'D': 'Sales of 7", 12" and cassette singles accounted for approximately 60% of the revenue from singles in 1992.',
             'E': '1989 is the first year of those shown in which 7" singles accounted for less than half the revenue from singles.'},
    notes=[(1, 'y', 'Stacked bars: each format is a <b>slice</b>. Its size = top of the slice − bottom of the slice.'),
           (2, 'b', 'Four statements are true. Hunt for the one that breaks.'),
           (3, 'p', '“Every year” means 5 changes in a row, all the same way. One exception makes it false.')],
    steps=[
        f"""<p>Read each slice as top minus bottom (£m, roughly):</p>
{table([['7″ (bottom)', '43', '40', '36', '29', '24', '14'],
        ['12″ (black)', '77 − 43 = 34', '71 − 40 = 31', hl('71 − 36 = 35', 'p'), '63 − 29 = 34', '49 − 24 = 25', '32 − 14 = 18'],
        ['CD (top)', '3', '5', '6', '9', '19', '33']],
       head=['', '1987', '1988', '1989', '1990', '1991', '1992'])}""",
        f"""<p>Zoom in on 1988 and 1989. The black slice ends at 71 both years, but in 1989 it starts lower, so it is <b>taller</b>:</p>{_singles()}
<p>12″ sales went <b>up</b> from 1988 to 1989, so “fell every year” is false {ar()} {boxed('C')}</p>
{note('Don’t read the top of the black slice (77, 71, 71, 63…). That makes 12″ look like it never rose. Measure the slice itself.', 'trap')}""",
        f"""<p>Quick check that the others are true:</p>
{calc(f'A: CD 3 → 5 → 6 → 9 → 19 → 33 {tick()}', f'B: 7″ 43 → 40 → 36 → 29 → 24 → 14 {tick()}',
      f'D: 1992 first three slices reach 49 out of 82: 49 ÷ 82 ≈ 0.6 = 60% {tick()}',
      f'E: 7″ share: 43/80 and 40/76 are over half, 36/80 is under half {tick()}')}""",
    ],
    answer_text='C is false: the 12″ slice grew from about £31m in 1988 to about £35m in 1989.',
    why={'A': 'True: the white CD slice gets bigger every year (about 3, 5, 6, 9, 19, 33).',
         'B': 'True: the bottom 7″ slice shrinks every year (43, 40, 36, 29, 24, 14).',
         'D': 'True: in 1992 the 7″, 12″ and cassette slices stack up to about 49 of the 82 total, about 60%.',
         'E': 'True: 7″ is over half in 1987 (43 of 80) and 1988 (40 of 76) but under half in 1989 (36 of 80).'},
    fast='Measure the black slice, not its top: 1988 is 40 to 71 (31), 1989 is 36 to 71 (35). It rose, so C is false.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _mix():
    s = 4.4
    x0 = 110
    parts, lab = [], []
    # have
    lab.append(text(x0 - 12, 66, 'have', k='ink', size=19, anchor='end'))
    parts.append(rect(x0, 44, 8 * s, 34, k='ink', fill='y', sw=1.6))
    parts.append(rect(x0 + 8 * s, 44, 24 * s, 34, k='ink', fill='b', sw=1.6))
    lab.append(text(x0 + 4 * s, 67, '8', k='ink', size=16))
    lab.append(text(x0 + 20 * s, 67, '24 cement', k='ink', size=16))
    lab.append(text(x0 + 32 * s + 10, 67, '32 kg', k='muted', size=16, anchor='start'))
    # need
    y = 130
    lab.append(text(x0 - 12, y + 22, 'need', k='ink', size=19, anchor='end'))
    parts.append(rect(x0, y, 8 * s, 34, k='ink', fill='y', sw=1.6))
    parts.append(rect(x0 + 8 * s, y, 72 * s, 34, k='red', fill='y', sw=2.4))
    parts.append(rect(x0 + 80 * s, y, 24 * s, 34, k='ink', fill='b', sw=1.6))
    parts.append(rect(x0 + 104 * s, y, 16 * s, 34, k='red', fill='b', sw=2.4))
    lab.append(text(x0 + 4 * s, y + 23, '8', k='ink', size=16))
    lab.append(text(x0 + 44 * s, y + 23, '+72 sand', k='red', size=19, font='scrawl'))
    lab.append(text(x0 + 92 * s, y + 23, '24', k='ink', size=16))
    lab.append(text(x0 + 112 * s, y + 23, '+16', k='red', size=17, font='scrawl'))
    parts.append(brace(x0, x0 + 80 * s, y + 40, '', k='ink'))
    parts.append(brace(x0 + 80 * s, x0 + 120 * s, y + 40, '', k='ink'))
    lab.append(text(x0 + 40 * s, y + 80, '80 sand (2 parts)', k='ink', size=16))
    lab.append(text(x0 + 100 * s, y + 80, '40 cement (1 part)', k='ink', size=16))
    lab.append(text(x0 + 60 * s, 26, 'yellow = sand, blue = cement', k='muted', size=15))
    lab.append(text(x0 + 60 * s, 254, 'add 72 : 16 = 9 : 2', k='red', size=24, font='scrawl'))
    return svg(660, 270, rough(*parts) + ''.join(lab),
               'Bar model: have 8 kg sand and 24 kg cement; need 80 sand and 40 cement; so add 72 sand and 16 cement')


Q.append(dict(
    n=5, orig=12, answer='D', topic='Ratio & mixtures',
    question=f"""<p>A builder has {hl('32 kg of a mix of sand and cement, of which 25% is sand', 'g', 1)}. For a new job, he needs {hl('120 kg', 'g', 2)} of a mix of sand and cement in which {hl('the ratio of sand to cement is 2 : 1', 'y', 3)}. To obtain this, he {hl('starts with his initial 32 kg mix and adds more sand and cement', 'p', 4)}.</p>
<p class="stem">What is the ratio of the masses of sand and cement that {hl('he needs to add', 'b', 5)}?</p>""",
    options={'A': '4 : 7', 'B': '3 : 4', 'C': '5 : 3', 'D': '9 : 2', 'E': '12 : 1'},
    notes=[(1, 'g', '25% of 32 = 8 kg sand, so 24 kg is cement.'),
           (2, 'g', 'The <b>finished</b> mix is 120 kg (not 120 kg extra).'),
           (3, 'y', '2 : 1 = 3 parts. Sand is 2 parts, cement 1 part.'),
           (4, 'p', 'What’s already in the 32 kg counts. Only add the difference.'),
           (5, 'b', 'Ratio of the <b>extra</b> sand to the <b>extra</b> cement.')],
    steps=[
        f"""<p>What he has now:</p>{calc('sand = 25% of 32 = 32 ÷ 4 = 8 kg', 'cement = 32 − 8 = 24 kg')}""",
        f"""<p>What he needs: 120 kg split 2 : 1.</p>{calc('3 parts = 120 kg, so 1 part = 40 kg', 'sand = 2 × 40 = 80 kg, cement = 40 kg')}""",
        f"""<p>Top up the difference:</p>{_mix()}
{calc('sand: 80 − 8 = 72 kg', 'cement: 40 − 24 = 16 kg', f'72 : 16 {ar()} ÷ 8 {ar()} {boxed("9 : 2")}')}
{note('Check: 32 + 72 + 16 = 120 kg ✓', 'check')}""",
    ],
    answer_text='9 : 2 (add 72 kg of sand and 16 kg of cement).',
    why={'A': 'Turns the target round to sand : cement = 1 : 2 (40 sand, 80 cement). Then he adds 32 sand and 56 cement = 4 : 7.',
         'B': 'Adding 88 kg as 3 : 4 gives about 38 sand + 50 cement, so 46 sand and 74 cement in total: more cement than sand.',
         'C': 'Adding 88 kg as 5 : 3 gives 55 sand + 33 cement, so 63 sand and 57 cement: nowhere near 2 : 1.',
         'E': 'Far too little cement: 88 kg as 12 : 1 is about 81 sand + 7 cement, giving 31 kg cement instead of 40.'},
    fast='Have 8 sand + 24 cement. Need 80 + 40. Add 72 + 16 = 9 : 2.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _laptops():
    heads = ['≥ 2.7 GHz', '≥ 8 GB', '≥ 600 GB', 'graphics ≥ 4', 'screen ≥ 15', 'price']
    rows = [('Racer', ['2.7', '4', '500', '2', '15.6'], [1, 0, 0, 0, 1], '£600'),
            ('Ledd', ['2.8', '8', '1000', '4', '17.3'], [1, 1, 1, 1, 1], '£850'),
            ('SNSV', ['2.5', '4', '750', '6', '15.6'], [0, 0, 1, 1, 1], '£500'),
            ('Pear', ['2.8', '8', '1000', '4', '13.3'], [1, 1, 1, 1, 0], '£1300'),
            ('Elovon', ['3.0', '16', '1000', '8', '15.6'], [1, 1, 1, 1, 1], '£700')]
    cw, ch, x0, y0 = 86, 40, 96, 44
    parts, lab = [], []
    for j, h in enumerate(heads):
        lab.append(text(x0 + j * cw + cw / 2, 32, h, k='pen' if j < 5 else 'ink', size=15))
    for i, (name, vals, ok, price) in enumerate(rows):
        y = y0 + i * ch
        allok = all(ok)
        lab.append(text(x0 - 10, y + 26, name, k='green' if allok else 'ink', size=18, anchor='end'))
        for j, (v, good) in enumerate(zip(vals, ok)):
            x = x0 + j * cw
            parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='ink', fill='paper' if good else 'p', sw=1.3))
            lab.append(text(x + 34, y + 26, v, k='ink' if good else 'red', size=16))
            parts.append(_tk(x + 66, y + 20, 0.8) if good else _cx(x + 66, y + 20, 0.7))
        x = x0 + 5 * cw
        parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='green' if allok else 'muted', fill='g' if allok else 'paper', sw=1.6))
        lab.append(text(x + cw / 2, y + 26, price, k='ink' if allok else 'muted', size=17))
    lab.append(text(x0 + 5 * cw + cw / 2, y0 + 5 * ch + 26, '£700 is cheaper', k='green', size=19, font='scrawl'))
    return svg(620, 290, rough(*parts) + ''.join(lab),
               'Checklist of the five laptops against each requirement; only Ledd at 850 pounds and Elovon at 700 pounds pass everything')


Q.append(dict(
    n=6, orig=13, answer='E', topic='Tables & requirements',
    question=f"""<p>I am planning to buy a new laptop. The following table shows the specifications and the prices of my shortlist.</p>
{table([['<i>Racer</i>', '2.7', '4', '500', '2', '15.6', '600'],
        ['<i>Ledd</i>', '2.8', '8', '1000', '4', '17.3', '850'],
        ['<i>SNSV</i>', '2.5', '4', '750', '6', '15.6', '500'],
        ['<i>Pear</i>', '2.8', '8', '1000', '4', '13.3', '1300'],
        ['<i>Elovon</i>', '3.0', '16', '1000', '8', '15.6', '700']],
       head=['<i>laptop</i>', '<i>processor speed</i> (GHz)', '<i>memory</i> (GB)', '<i>storage</i> (GB)',
             '<i>graphics card memory</i> (GB)', '<i>screen size</i> (inches)', '<i>price</i> (£)'])}
<p>In terms of storage, {hl('the operating system and my files take up 300 GB', 'p', 1)}. I would also like a laptop with a {hl('screen size of at least 15 inches', 'y', 2)}. I am looking for the {hl('cheapest laptop that can run the following games', 'b', 3)} (the minimum system requirements indicate {hl('the lowest possible value for each characteristic', 'y', 4)} that would enable me to play these games):</p>
{table([['<i>OTAD</i>', hl('2.7', 'g'), '6', '70', hl('4', 'g')],
        ['<i>Kickman</i>', '2.5', '4', '80', hl('4', 'g')],
        ['<i>Earthcraft</i>', '2.2', '4', '50', '2'],
        ['<i>Near Scream</i>', '2.6', hl('8', 'g'), '100', hl('4', 'g')]],
       head=['<i>game</i>', '<i>processor speed</i> (GHz)', '<i>memory</i> (GB)', '<i>storage</i> (GB)', '<i>graphics card memory</i> (GB)'])}
<p class="stem">Which laptop should I buy?</p>""",
    options={'A': 'Racer', 'B': 'Ledd', 'C': 'SNSV', 'D': 'Pear', 'E': 'Elovon'},
    notes=[(1, 'p', 'Storage has to hold 300 GB <b>plus</b> all four games.'),
           (2, 'y', 'Rules out anything under 15 inches.'),
           (3, 'b', 'Pass every test first, <b>then</b> pick the cheapest.'),
           (4, 'y', 'To run <b>all</b> the games, beat the biggest number in each column.')],
    steps=[
        f"""<p>Set the bar for each column (toughest game wins):</p>
{calc('processor ≥ 2.7 GHz (OTAD)', 'memory ≥ 8 GB (Near Scream)', 'graphics ≥ 4 GB',
      'storage ≥ 300 + 70 + 80 + 50 + 100 = 600 GB', 'screen ≥ 15 inches')}""",
        f"""<p>Tick off each laptop:</p>{_laptops()}""",
        f"""<p>Two laptops pass everything: Ledd (£850) and Elovon (£700). Cheapest {ar()} {boxed('Elovon')}</p>""",
    ],
    answer_text='Elovon: it meets every requirement and is £150 cheaper than Ledd, the only other laptop that does.',
    why={'A': 'Racer has only 4 GB memory (Near Scream needs 8), 2 GB graphics, and 500 GB storage is under the 600 GB needed.',
         'B': 'Ledd passes every test, but costs £850. Elovon passes too and is cheaper.',
         'C': 'SNSV is the cheapest, but 2.5 GHz is too slow for OTAD and 4 GB memory is too little.',
         'D': 'Pear’s screen is 13.3 inches, under 15 (and it is the dearest).'},
    fast='Need 2.7 GHz, 8 GB, 4 GB graphics, 15 inch screen. Only Ledd and Elovon qualify; Elovon is cheaper.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _dials():
    dials = ['owtbafdm', 'nhwodaei', 'eobdlnat']
    cw, ch, x0, y0 = 62, 32, 40, 52
    parts, lab = [], []
    for d, letters in enumerate(dials):
        x = x0 + d * (cw + 26)
        parts.append(rect(x, y0, cw, ch * 8, k='ink', fill='paper', sw=2, rx=10))
        lab.append(text(x + cw / 2, y0 - 12, f'dial {d + 1}', k='muted', size=16))
        for i, ch_ in enumerate(letters):
            yy = y0 + i * ch
            if i:
                parts.append(line(x + 6, yy, x + cw - 6, yy, k='muted', w=1))
            hit = (d == 1 and ch_ == 'a') or (d == 2 and ch_ == 't')
            if hit:
                parts.append(circle(x + cw / 2, yy + ch / 2, 13, k='green', sw=2.4))
            lab.append(text(x + cw / 2, yy + 23, ch_, k='green' if hit else 'ink', size=21, font='print'))
    lab.append(text(x0 + cw / 2, y0 + ch * 8 + 28, 'no h!', k='red', size=22, font='scrawl'))
    parts.append(_cx(x0 + cw / 2 + 44, y0 + ch * 8 + 20))
    lab.append(text(20, y0 + ch * 8 + 58, 'each dial already shows 8 different letters: full!', k='muted', size=15, anchor='start'))
    tx = 330
    tests = [('win', 'w ✓  i ✓  n ✓', 'green'), ('deb', 'd ✓  e ✓  b ✓', 'green'), ('hat', 'h ✗  (not on dial 1)', 'red'),
             ('men', 'm ✓  e ✓  n ✓', 'green'), ('bad', 'b ✓  a ✓  d ✓', 'green')]
    for i, (w, res, col) in enumerate(tests):
        yy = y0 + 30 + i * 46
        lab.append(text(tx, yy, w, k='ink', size=22, font='print', anchor='start', weight='bold'))
        lab.append(text(tx + 62, yy, res, k=col, size=19, anchor='start'))
    lab.append(text(tx, y0 + 30 + 5 * 46 - 4, 'h is on dial 2 (who), but hat needs it first', k='muted', size=15, anchor='start'))
    return svg(640, 380, rough(*parts) + ''.join(lab),
               'Three dials each listing eight letters; dial 1 has o, w, t, b, a, f, d, m and no h, so hat is impossible')


Q.append(dict(
    n=7, orig=14, answer='C', topic='Logic & letters',
    question=f"""<p>A combination lock has {hl('three dials, each dial has eight letters', 'y', 1)}. It is known that the following combinations {hl('have been used', 'g', 2)} - one, who, two, bob, add, owl, fab, den, mia and tat.</p>
<p class="stem">Which one of the following words is {hl('not possible', 'b', 3)} to use on this combination lock?</p>""",
    options={'A': 'win', 'B': 'deb', 'C': 'hat', 'D': 'men', 'E': 'bad'},
    notes=[(1, 'y', 'Letter 1 comes from dial 1, letter 2 from dial 2, letter 3 from dial 3. Only 8 letters on each.'),
           (2, 'g', 'Each used word proves which letters are on each dial.'),
           (3, 'b', 'Find a word needing a letter its dial can’t have.')],
    steps=[
        f"""<p>Collect the letters each dial must have, position by position:</p>
{calc('1st letters: o, w, t, b, a, o, f, d, m, t → <b>o w t b a f d m</b> (8!)',
      '2nd letters: n, h, w, o, d, w, a, e, i, a → <b>n h w o d a e i</b> (8!)',
      '3rd letters: e, o, o, b, d, l, b, n, a, t → <b>e o b d l n a t</b> (8!)')}
<p>Every dial already has 8 known letters, so there is no room for anything else.</p>""",
        f"""<p>Now test each word on the dials:</p>{_dials()}
<p>Dial 1 has no h, so hat can’t be set {ar()} {boxed('hat')}</p>""",
    ],
    answer_text='hat: dial 1’s eight letters are o, w, t, b, a, f, d, m, with no h.',
    why={'A': 'win: w is on dial 1 (who), i on dial 2 (mia), n on dial 3 (den).',
         'B': 'deb: d on dial 1 (den), e on dial 2 (den), b on dial 3 (bob, fab).',
         'D': 'men: m on dial 1 (mia), e on dial 2 (den), n on dial 3 (den).',
         'E': 'bad: b on dial 1 (bob), a on dial 2 (fab), d on dial 3 (add).'},
    fast='First letters of the 10 words: o, w, t, b, a, f, d, m. That’s 8, so dial 1 is full and has no h. hat is impossible.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _cans():
    parts, lab = [], []

    def can(x, y, fill='b', k='ink'):
        parts.append(rect(x, y, 16, 28, k=k, fill=fill, sw=1.5, rx=5))

    lab.append(text(20, 26, 'Usual:', k='ink', size=20, font='scrawl', anchor='start'))
    for p in range(3):
        px = 20 + p * 116
        parts.append(rect(px, 38, 104, 44, k='muted', sw=1.4, rx=6))
        for i in range(4):
            can(px + 10 + i * 22, 46)
        lab.append(text(px + 52, 104, '£2.60', k='ink', size=16))
    lab.append(text(380, 68, '3 packs = £7.80', k='ink', size=21, anchor='start'))
    lab.append(text(20, 148, 'Offer week:', k='ink', size=20, font='scrawl', anchor='start'))
    for p in range(2):
        px = 20 + p * 140
        parts.append(rect(px, 160, 128, 44, k='muted', sw=1.4, rx=6))
        for i in range(4):
            can(px + 10 + i * 22, 168)
        can(px + 102, 168, fill='g', k='green')
        lab.append(text(px + 52, 226, '£2.60', k='ink', size=16))
        lab.append(text(px + 110, 226, 'free', k='green', size=15))
    can(312, 168)
    can(342, 168, fill='y')
    lab.append(text(320, 226, '80p', k='ink', size=15))
    lab.append(text(350, 226, '40p', k='orange', size=15))
    lab.append(text(390, 190, '10 + 2 = 12 cans', k='ink', size=19, anchor='start'))
    lab.append(text(390, 216, '= £6.40', k='ink', size=21, anchor='start'))
    lab.append(text(320, 268, 'saving: £7.80 − £6.40 = £1.40', k='red', size=23, font='scrawl'))
    return svg(640, 286, rough(*parts) + ''.join(lab),
               'Usual: three packs of four for 7.80. Offer: two packs of four plus a free can, and a pair of single cans at 80p and 40p, for 6.40')


Q.append(dict(
    n=8, orig=18, answer='E', topic='Best deal',
    question=f"""<p>Every week I buy 12 cans of lemonade. The shop that I always buy them from sells individual cans for {hl('80p each', 'g')} and {hl('packs of 4 cans for £2.60, so I buy three packs', 'g', 1)} of cans.</p>
<p>Last week the shop had a special offer, as follows:</p>
<p>Individual cans – {hl('buy one, get another half price', 'y', 2)}</p>
<p>Pack of 4 cans – {hl('buy one pack, get a 5<sup>th</sup> can free', 'y', 3)}</p>
<p>{hl('I didn’t want more than 12 cans', 'p', 4)}, and I managed to get 12 cans for the lowest possible total price.</p>
<p class="stem">How much {hl('less than usual', 'b', 5)} did I pay for my 12 cans last week?</p>""",
    options={'A': '20p', 'B': '60p', 'C': '80p', 'D': '£1.00', 'E': '£1.40'},
    notes=[(1, 'g', 'Usual cost: 3 × £2.60 = £7.80.'),
           (2, 'y', 'Two single cans: 80p + 40p = £1.20 (60p a can).'),
           (3, 'y', 'A pack now gives 5 cans for £2.60 (52p a can): best value.'),
           (4, 'p', 'Exactly 12 cans. Three packs would give 15, too many.'),
           (5, 'b', 'Answer = usual price − offer price.')],
    steps=[
        f"""<p>Price per can on offer:</p>
{calc('pack: £2.60 for 5 cans = 52p each (best)', 'pair of singles: 80p + 40p = £1.20 for 2 = 60p each', 'a lone single: 80p')}""",
        f"""<p>Use as many packs as fit in 12 cans: 2 packs = 10 cans. That leaves 2 cans, which is exactly one half-price pair.</p>{_cans()}""",
        f"""<p>Check the other ways of making 12:</p>
{calc('1 pack (5) + 7 singles: 2.60 + 3 × 1.20 + 0.80 = £7.00', '12 singles: 6 × 1.20 = £7.20', f'2 packs + a pair: 5.20 + 1.20 = <b>£6.40</b> (cheapest) {tick()}')}
{calc(f'£7.80 − £6.40 = {boxed("£1.40")}')}""",
    ],
    answer_text='£1.40 less: £6.40 (two packs with free cans, plus one half-price pair) instead of £7.80.',
    why={'A': 'Forgets the free 5th can: 2 packs (8 cans) + 4 singles as two pairs = 5.20 + 2.40 = £7.60, only 20p less.',
         'B': 'Buys all 12 as single-can pairs: 6 × £1.20 = £7.20, 60p less.',
         'C': 'Uses only one pack: 2.60 + 7 singles (3 pairs + 1) = £7.00, 80p less.',
         'D': 'Right cans (2 packs + 2 singles) but pays full price for both singles: 5.20 + 1.60 = £6.80. The second is half price.'},
    fast='2 packs = 10 cans for £5.20, plus a pair at 80p + 40p = £1.20. £6.40 against £7.80: £1.40.',
))
