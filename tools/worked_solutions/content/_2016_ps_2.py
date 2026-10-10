from wslib import *

Y = 2016
Q = []


# ---------------------------------------------------------------- 9 (Q19)
def _casualties():
    parts, lab = [], []
    x0, w = 40, 580
    bu = w * 7389 / 13828
    parts += [rect(x0, 50, bu, 46, k='ink', fill='b', sw=1.8), rect(x0 + bu, 50, w - bu, 46, k='ink', fill='o', sw=1.8)]
    lab += [text(x0, 36, 'all car users injured: 13,828', k='ink', size=18, anchor='start'),
            text(x0 + bu / 2, 80, 'built-up 7,389', k='ink', size=18),
            text(x0 + bu + (w - bu) / 2, 80, 'non-built-up 6,439', k='ink', size=18)]
    parts += [line(x0 + bu, 98, x0, 170, k='muted', w=1.6, dash=True), line(x0 + w, 98, x0 + w, 170, k='muted', w=1.6, dash=True)]
    lab.append(text(x0 + w / 2 + 70, 140, 'zoom in on non-built-up roads', k='muted', size=16))
    fat = 90
    parts += [rect(x0, 176, fat, 50, k='ink', fill='p', sw=1.8), rect(x0 + fat, 176, w - fat, 50, k='ink', fill='g', sw=1.8)]
    lab += [text(x0 + fat / 2, 207, 'died 187', k='ink', size=17),
            text(x0 + fat + (w - fat) / 2, 207, 'serious, not fatal: 1,724 − 187 = 1,537', k='green', size=19, weight='bold')]
    parts.append(brace(x0, x0 + w, 232, 'fatally or seriously injured: 1,724', k='red'))
    lab.append(text(x0 + w / 2, 300, '(the slightly injured make up the rest of the 6,439)', k='muted', size=15))
    return svg(660, 312, rough(*parts) + ''.join(lab),
               'Bar of 13,828 car users split into built-up 7,389 and non-built-up 6,439; the non-built-up fatal or serious bar of 1,724 split into 187 deaths and 1,537 serious')


Q.append(dict(
    n=9, orig=19, answer='A', topic='Reading data',
    question=f"""<p>The following is from a report on road accidents in Scotland in 1998:</p>
<p>A total of 13,828 car users were injured in road accidents, representing 62% of all casualties.
Of these people, a total of 2,386 were either fatally or seriously injured, 223 of whom died.
{hl('Roads in built-up areas', 'p', 5)} accounted for a little over half of all car-user casualties (53%: 7,389 out
of 13,828). Presumably because average speeds are higher in non-built-up areas, they
accounted for much higher percentages of the total numbers of car users who were {hl('fatally injured (84%: 187 out of 223)', 'g', 3)} or were {hl('fatally or seriously injured (72%: 1,724 out of 2,386)', 'g', 4)}.</p>
<p class="stem">How many car users suffered {hl('serious, but not fatal,', 'b', 1)} injuries in accidents on roads in Scotland in
{hl('non-built-up areas', 'b', 2)} in 1998?</p>""",
    options={'A': '1,537', 'B': '1,724', 'C': '2,199', 'D': '6,439', 'E': '7,389'},
    notes=[(1, 'b', 'Serious ones only. The deaths must come out.'),
           (2, 'b', 'Only the non-built-up roads (the faster, country roads).'),
           (3, 'g', '187 = deaths on non-built-up roads.'),
           (4, 'g', '1,724 = deaths <b>plus</b> serious injuries on non-built-up roads.'),
           (5, 'p', 'The 7,389 is for <b>built-up</b> roads: the wrong group.')],
    steps=[
        f"""<p>Picture the groups. Each figure in the bracket is “part out of whole”:</p>{_casualties()}""",
        f"""<p>“Fatally or seriously injured” <b>includes</b> the people who died. Take them out:</p>
{calc(f'non-built-up, fatal or serious = 1,724', f'non-built-up, fatal = 187', f'serious, not fatal = 1,724 − 187 = {boxed("1,537")}')}
{note('Ignore the percentages. They just describe the numbers in the brackets.', 'tip')}""",
    ],
    answer_text='1,537 = 1,724 (fatal or serious, non-built-up) − 187 (fatal, non-built-up).',
    why={'B': '1,724 still includes the 187 who died. The question wants serious but <b>not</b> fatal.',
         'C': '2,199 = 2,386 − 187: it takes the non-built-up deaths away from the fatal-or-serious total for <b>all</b> roads.',
         'D': '6,439 = 13,828 − 7,389: every car-user casualty on non-built-up roads, slight injuries included.',
         'E': '7,389 is all the casualties on <b>built-up</b> roads.'},
    fast='Non-built-up: fatal or serious 1,724, fatal 187. 1,724 − 187 = 1,537.',
))


# ---------------------------------------------------------------- 10 (Q20)
H10 = {(0, 1): 2, (0, 3): 1, (1, 0): 2, (1, 1): 3, (1, 2): 2, (1, 3): 2, (2, 0): 1, (2, 2): 2, (3, 2): 1}
ROWF = {0: 'g', 1: 'b', 2: 'o', 3: 'p'}
ROWK = {0: 'green', 1: 'pen', 2: 'orange', 3: 'red'}


def _cube_plan():
    ox, oy = 330, 46
    u, v = (58, 29), (-58, 29)
    P = lambda X, Yy: (ox + X * u[0] + Yy * v[0], oy + X * u[1] + Yy * v[1])
    parts, lab = [], []
    for X in range(4):
        for Yy in range(4):
            a, b, c, d = P(X, Yy), P(X + 1, Yy), P(X + 1, Yy + 1), P(X, Yy + 1)
            h = H10.get((X, Yy), 0)
            parts.append(poly([a, b, c, d], k='ink' if h else 'muted', fill=ROWF[X] if h else 'none', sw=1.8 if h else 1))
            if h:
                cx, cy = P(X + 0.5, Yy + 0.5)
                lab.append(text(cx, cy + 8, h, k='ink', size=22, weight='bold'))
    for X in range(4):
        tallest = max(H10.get((X, Yy), 0) for Yy in range(4))
        cx, cy = P(X + 0.5, 4.45)
        lab.append(text(cx, cy + 6, f'tallest {tallest}', k=ROWK[X], size=17))
    parts.append(arrow(640, 22, 566, 59, k='red', bend=0, w=2.6))
    lab += [text(646, 50, 'look', k='red', size=17, anchor='start'),
            text(470, 300, 'each coloured row runs along the arrow', k='ink', size=16),
            text(470, 322, 'and becomes one column of the side view', k='ink', size=16)]
    return svg(680, 336, rough(*parts) + ''.join(lab),
               'Plan of the arrangement drawn from above in the same direction as the picture, with the height of each stack; rows along the arrow have tallest stacks 1, 2, 3 and 2')


def _side_view():
    s = 50
    heights = [(3, 1), (2, 2), (1, 3), (0, 2)]
    x0, base = 200, 200
    parts, lab = [], []
    for i, (X, h) in enumerate(heights):
        for k in range(h):
            parts.append(rect(x0 + i * s, base - (k + 1) * s, s, s, k='ink', fill=ROWF[X], sw=2))
        lab.append(text(x0 + i * s + s / 2, base + 24, h, k=ROWK[X], size=20, weight='bold'))
    parts.append(line(x0 - 30, base, x0 + 4 * s + 30, base, k='ink', w=2))
    lab += [text(x0 - 40, base - 10, 'your left', k='ink', size=17, anchor='end'),
            text(x0 - 40, base - 32, 'front row', k='red', size=15, anchor='end'),
            text(x0 + 4 * s + 40, base - 10, 'your right', k='ink', size=17, anchor='start'),
            text(x0 + 4 * s + 40, base - 32, 'back row', k='green', size=15, anchor='start'),
            text(x0 + 2 * s, base + 52, '1, 2, 3, 2 = option E', k='red', size=22, font='scrawl')]
    return svg(600, 266, rough(*parts) + ''.join(lab), 'Side view seen along the arrow: columns of 1, 2, 3 and 2 squares from left to right')


Q.append(dict(
    n=10, orig=20, answer='E', topic='3D views',
    question=f"""<p>One of the exhibits in the Interactive Art Exhibition at the Hanson Gallery consists of {hl('16 identical free-standing cubes', 'g', 1)}. Visitors to the exhibition are invited to handle these cubes and
rearrange them to create their own work of art.</p>
<p>This is the arrangement that I have made:</p>
{fig(Y, 'ps_q10_cubes', 'Sixteen cubes in stacks of different heights, with an arrow at the top right pointing down and to the left', 280)}
<p class="stem">What is the {hl('side view', 'y', 2)} of my arrangement {hl('from the direction indicated by the arrow', 'b', 3)}?</p>
{fig(Y, 'ps_q10_opts', 'Five side views A to E, each four squares wide with columns of different heights', 380)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'g', '16 cubes. “Free-standing” means every cube sits on the floor or on another cube, so some cubes are hidden underneath.'),
           (2, 'y', 'A flat outline: in each column you only see the <b>tallest</b> stack.'),
           (3, 'b', 'Stand where the arrow starts (top right) and look along it. Which end is on your left?')],
    steps=[
        f"""<p>Look down on the arrangement from above and write the height of each stack on a plan drawn the same way round as the picture:</p>
{_cube_plan()}
{calc('2 + 1 + 2 + 3 + 2 + 2 + 1 + 2 + 1 = 16 cubes ' + tick())}""",
        f"""<p>The arrow looks along the coloured rows. Each row shows up as <b>one column</b>, as tall as its tallest stack:</p>
{calc('front row (bottom right of picture): 1', 'next row: 2', 'middle row with the 3-high stack: 3', 'back row (top left): 2')}""",
        f"""<p>Which way round? Standing at the arrow and looking down-left, your <b>left</b> hand points to the front of the picture (bottom right).
So the front row is on the left:</p>{_side_view()}
{calc(f'1, 2, 3, 2 {ar()} {boxed("E")}')}""",
    ],
    answer_text='View E: columns 1, 2, 3, 2 from left to right.',
    why={'A': 'A ends with a column of 1, but the back row has a stack of 2 (the cube top at the upper left of the picture, partly hidden behind the tall stack).',
         'B': 'B (2, 3, 2, 1) is E back to front: the view from the opposite side, or left and right swapped.',
         'C': 'C has a second column of only 1, but that row includes the 2-high stack just below the tall stack in the picture.',
         'D': 'D has no column of height 1, but the front row is just one cube on its own.'},
    fast='Plan + heights. Rows along the arrow: tallest 1, 2, 3, 2 from the front. The front is on your left, so 1-2-3-2: E.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _quiz():
    rounds = [('Round 1', 5, 1, 'b'), ('Round 2', 1, 2, 'o'), ('Round 3', 3, 5, 'p')]
    parts, lab = [], []
    x = 30
    for name, wrong, pts, f in rounds:
        w = 40 + wrong * 34
        parts.append(rect(x, 50, w, 70, k='ink', fill=f, sw=1.8, rx=8))
        lab.append(text(x + w / 2, 38, f'{name} (−{pts} each)', k='ink', size=17))
        for i in range(wrong):
            lab.append(text(x + 37 + i * 34, 96, '✗', k='red', size=26))
        lab.append(text(x + w / 2, 148, f'{wrong} wrong = −{wrong * pts}', k='ink', size=18))
        x += w + 26
    lab += [text(330, 196, '5 + 1 + 3 = 9 wrong ✓     5 + 2 + 15 = 22 points lost ✓', k='green', size=21, font='scrawl'),
            text(330, 224, 'Round 1 has the most wrong ✓', k='green', size=21, font='scrawl')]
    return svg(660, 240, rough(*parts) + ''.join(lab),
               'Wrong answers by round: 5 in round 1 losing 5 points, 1 in round 2 losing 2, 3 in round 3 losing 15; 9 wrong and 22 points lost')


Q.append(dict(
    n=11, orig=24, answer='B', topic='Number puzzles',
    question=f"""<p>Last night I took part in a quiz night, and my team won first prize.</p>
<p>The quiz consisted of three rounds:</p>
<p>Round 1 was 20 easy questions {hl('worth 1 point each', 'g', 1)};<br>Round 2 was 20 medium questions {hl('worth 2 points each', 'g')};<br>Round 3 was 20 hard questions {hl('worth 5 points each', 'g')}.</p>
<p>Our winning score was {hl('138 points', 'g', 2)}, having answered {hl('just nine questions incorrectly', 'g', 3)}.</p>
<p>The runners-up were annoyed because they had fewer incorrect answers, but fortunately for us
(although a little embarrassing) {hl('we had more incorrect answers in Round 1 (the easy questions) than in either of the other two rounds', 'y', 4)}.</p>
<p class="stem">How many questions did we answer {hl('incorrectly in Round 1', 'b', 5)}?</p>""",
    options={'A': '4', 'B': '5', 'C': '6', 'D': '7', 'E': '8'},
    notes=[(1, 'g', 'Full marks = 20 × 1 + 20 × 2 + 20 × 5 = 20 + 40 + 100 = 160.'),
           (2, 'g', 'So they lost 160 − 138 = <b>22 points</b>.'),
           (3, 'g', '9 wrong answers in total.'),
           (4, 'y', 'Round 1 wrong is <b>bigger than</b> Round 2 wrong and bigger than Round 3 wrong. This picks out the answer.'),
           (5, 'b', 'Wrong answers in Round 1.')],
    steps=[
        f"""<p>Work with the points <b>lost</b>. A wrong answer loses 1, 2 or 5 points depending on the round.
Call the wrong answers in each round R1, R2, R3:</p>
{calc('R1 + R2 + R3 = 9 (wrong answers)', 'R1 + 2 × R2 + 5 × R3 = 22 (points lost: 160 − 138)')}""",
        f"""<p>Every wrong answer loses at least 1 point: that’s 9. The other 22 − 9 = 13 points come from the
<b>extra</b> 1 point for each Round 2 miss and the extra 4 points for each Round 3 miss:</p>
{calc('R2 + 4 × R3 = 13')}""",
        f"""<p>Try R3 = 0, 1, 2, 3:</p>
{calc(f'R3 = 0 {ar()} R2 = 13, more than 9 in total {cross()}',
      f'R3 = 1 {ar()} R2 = 9, R1 = −1 {cross()}',
      f'R3 = 2 {ar()} R2 = 5, R1 = 2 {cross()} Round 1 is not the biggest',
      f'R3 = 3 {ar()} R2 = 1, R1 = 5 {tick()}')}
{_quiz()}
{calc(f'Round 1 wrong = {boxed("5")}')}
{note('R3 = 2 also fits both totals (2 + 5 + 2 = 9 and 2 + 10 + 10 = 22). Only the “more wrong in Round 1” clue rules it out.', 'trap')}""",
    ],
    answer_text='5 wrong in Round 1 (with 1 in Round 2 and 3 in Round 3).',
    why={'A': 'With 4 wrong in Round 1, the other 5 misses must lose 18 points. 5 misses at 2 or 5 points can make 10, 13, 16, 19… never 18.',
         'C': 'With 6 in Round 1, the other 3 misses must lose 16 points. 3 misses can make 6, 9, 12 or 15, never 16.',
         'D': 'With 7 in Round 1, the other 2 misses must lose 15 points. 2 misses make 4, 7 or 10, never 15.',
         'E': 'With 8 in Round 1, the last miss must lose 14 points. One miss loses 2 or 5, never 14.'},
    fast='160 − 138 = 22 lost over 9 misses. Extra over 1 each: R2 + 4·R3 = 13. R3 = 3, R2 = 1 gives R1 = 5, the only split where Round 1 is biggest.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _per_metre():
    rows = [('25 m roll, single', 9.96, '£2.49', 'p', True), ('25 m roll, pack of 6', 8.76, '£13.14', 'p', True),
            ('50 m roll, single', 8.38, '£4.19', 'p', True), ('100 m roll, single', 7.49, '£7.49', 'y', True),
            ('50 m roll, pack of 6', 6.98, '£20.94', 'g', True), ('100 m roll, pack of 6', 6.35, '£38.10', 'none', False)]
    X = lambda v: 200 + v * 30
    parts, lab = [], []
    lab.append(text(X(0), 22, 'pence per metre', k='muted', size=15, anchor='start'))
    for i, (name, ppm, price, f, ok) in enumerate(rows):
        y = 36 + i * 38
        parts.append(rect(X(0), y, X(ppm) - X(0), 26, k='ink' if ok else 'muted', fill=f, sw=1.6))
        lab.append(text(190, y + 19, name, k='ink' if ok else 'muted', size=16, anchor='end'))
        lab.append(text(X(ppm) + 8, y + 19, f'{ppm:.2f}p   ({price})', k='ink' if ok else 'muted', size=16, anchor='start'))
    y5 = 36 + 5 * 38
    parts.append(line(X(0) - 6, y5 + 13, X(6.35) + 160, y5 + 13, k='red', w=2.4))
    lab += [text(X(6.35) + 170, y5 + 19, 'over £30!', k='red', size=18, anchor='start', font='scrawl'),
            text(X(6.98) + 130, 36 + 4 * 38 + 19, '← best buy', k='green', size=19, anchor='start', font='scrawl')]
    return svg(660, 272, rough(*parts) + ''.join(lab),
               'Price per metre of each roll that fits: 9.96p, 8.38p, 8.76p, 7.49p, 6.98p for the 50 m pack and 6.35p for the 100 m pack, which is over budget')


Q.append(dict(
    n=12, orig=25, answer='D', topic='Tables & best value',
    question=f"""<p>I need to buy new printer paper for my fax machine. The paper comes in rolls. My machine
needs paper {hl('210 mm wide', 'y', 1)} and will take a roll {hl('up to 25.4 mm in diameter', 'y', 2)}.</p>
<p>I do not really care how long the paper in the roll is and {hl('will buy rolls in bulk if they are cheaper', 'g', 3)}.
I will just buy the {hl('most economical paper to use', 'b', 4)}. I {hl('cannot, however, afford to spend more than £30.00', 'p', 5)}.</p>
<p>The prices in the catalogue are as follows:</p>
<div class="tbl-wrap"><table class="ptable"><thead>
<tr><th colspan="3"></th><th colspan="3">Single rolls</th><th colspan="3">Packs of 6 rolls</th></tr>
<tr><th>Width (mm)</th><th>Length (m)</th><th>Diameter (mm)</th><th>RRP</th><th>Price</th><th>Saving</th><th>RRP</th><th>Price</th><th>Saving</th></tr></thead>
<tbody>
<tr><td>{hl('216', 'p')}</td><td>100</td><td>25.4</td><td>£12.84</td><td>£7.99</td><td>38%</td><td>£77.04</td><td>£39.54</td><td>49%</td></tr>
<tr><td>210</td><td>25</td><td>12.7</td><td>£4.16</td><td>£2.49</td><td>40%</td><td>£24.96</td><td>£13.14</td><td>47%</td></tr>
<tr><td>210</td><td>100</td><td>25.4</td><td>£12.13</td><td>£7.49</td><td>38%</td><td>£72.78</td><td>£38.10</td><td>48%</td></tr>
<tr><td>210</td><td>100</td><td>{hl('50.8', 'p')}</td><td>£12.24</td><td>£7.59</td><td>38%</td><td>£73.44</td><td>£38.94</td><td>47%</td></tr>
<tr><td>210</td><td>50</td><td>25.4</td><td>£6.62</td><td>£4.19</td><td>37%</td><td>£39.72</td><td>£20.94</td><td>47%</td></tr>
</tbody></table></div>
<p>(RRP=Recommended Retail Price)</p>
<p class="stem">How much will the transaction cost me?</p>""",
    options={'A': '£2.49', 'B': '£4.16', 'C': '£7.49', 'D': '£20.94', 'E': '£24.96'},
    notes=[(1, 'y', 'Exactly 210 mm wide. The 216 mm roll is out.'),
           (2, 'y', 'Diameter 25.4 mm or less. The 50.8 mm roll won’t fit.'),
           (3, 'g', 'Packs of 6 are allowed, and they are cheaper per metre.'),
           (4, 'b', 'Most economical = cheapest <b>per metre</b> of paper, not the cheapest thing to buy.'),
           (5, 'p', 'Budget cap: the very best deal might cost too much.')],
    steps=[
        f"""<p>Cross out the rolls that don’t fit the machine: 216 mm wide {cross()}, 50.8 mm across {cross()}.
That leaves the <b>25 m</b>, <b>100 m</b> and <b>50 m</b> rolls (use the Price columns, not the RRP).</p>""",
        f"""<p>Price per metre (in pence) for each way of buying them:</p>
{calc('25 m single: 249 ÷ 25 = 9.96p', '25 m pack: 1314 ÷ 150 = 8.76p',
      '100 m single: 749 ÷ 100 = 7.49p', '100 m pack: 3810 ÷ 600 = 6.35p, but £38.10 is over £30 ' + cross(),
      '50 m single: 419 ÷ 50 = 8.38p', '50 m pack: 2094 ÷ 300 = 6.98p')}
{_per_metre()}""",
        f"""<p>The cheapest per metre that he can afford is the pack of six 50 m rolls:</p>
{calc(f'cost = {boxed("£20.94")}')}
{note('A pack of 6 has 6 rolls, so divide by 6 × the length (e.g. 6 × 50 = 300 m).', 'tip')}""",
    ],
    answer_text='£20.94: a pack of six 50 m rolls, 6.98p a metre (the 6.35p pack costs £38.10, over budget).',
    why={'A': '£2.49 is the cheapest thing to buy, but at 9.96p a metre it is the <b>worst</b> value.',
         'B': '£4.16 is the RRP of a 25 m roll. Nobody pays the RRP: the price is £2.49.',
         'C': '£7.49 buys one 100 m roll at 7.49p a metre. Good, but the 50 m pack is cheaper per metre (6.98p).',
         'E': '£24.96 is the RRP of a pack of 25 m rolls. The actual price is £13.14.'},
    fast='Only 210 mm rolls of 25.4 mm or less. Best per metre is the 100 m pack (6.35p) but it costs £38.10. Next best: the 50 m pack at 6.98p a metre, £20.94.',
))


# ---------------------------------------------------------------- 13 (Q26)
PIECES = {'V': [(0, 0), (0, 1), (1, 1)], 'W': [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], 'X': [(0, 0), (1, 0)],
          'Y': [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], 'Z': [(1, 0), (0, 1), (1, 1), (2, 1)]}
PF = {'V': 'v', 'W': 'b', 'X': 'o', 'Y': 'g', 'Z': 'p'}


def _pieces():
    s = 28
    parts, lab = [], []
    xs = {'V': 20, 'W': 110, 'X': 230, 'Y': 320, 'Z': 510}
    for name, cells in PIECES.items():
        for (c, r) in cells:
            parts.append(rect(xs[name] + c * s, 30 + r * s, s, s, k='ink', fill=PF[name], sw=1.6))
        w = (max(c for c, r in cells) + 1) * s
        lab.append(text(xs[name] + w / 2, 140, f'{name} = {len(cells)}', k='ink', size=20))
    lab.append(text(330, 178, '3 + 5 + 2 + 7 + 4 = 21 squares', k='red', size=22, font='scrawl'))
    return svg(640, 192, rough(*parts) + ''.join(lab), 'The five pieces split into unit squares: V 3, W 5, X 2, Y 7, Z 4, total 21')


def _mat():
    layout = ['WYYYYY', 'WWWYZY', 'XXWZZZ']
    s = 56
    x0, y0 = 150, 30
    parts, lab = [], []
    for r, row in enumerate(layout):
        for c, ch in enumerate(row):
            parts.append(rect(x0 + c * s, y0 + r * s, s, s, k='ink', fill=PF[ch], sw=1.4))
    done = set()
    for r, row in enumerate(layout):
        for c, ch in enumerate(row):
            if ch not in done and (ch != 'Y' or c == 3):
                done.add(ch)
                lab.append(text(x0 + c * s + s / 2, y0 + r * s + s / 2 + 9, ch, k='ink', size=26, font='print', weight='bold'))
    lab += [text(x0 + 3 * s, y0 - 10, '6', k='red', size=20), text(x0 - 14, y0 + 1.5 * s + 7, '3', k='red', size=20, anchor='end'),
            text(x0 + 3 * s, y0 + 3 * s + 34, 'W + X + Y + Z make a 3 × 6 mat. V is left over.', k='green', size=20, font='scrawl')]
    return svg(640, 240, rough(*parts) + ''.join(lab), 'A 3 by 6 rectangle made from pieces W, X, Y and Z')


Q.append(dict(
    n=13, orig=26, answer='A', topic='Shapes & area',
    question=f"""<p>After having some carpets fitted recently I was left with these five remnants.</p>
{fig(Y, 'ps_q13_pieces', 'Five pieces V, W, X, Y and Z made of squares', 460)}
<p>I have stitched {hl('four of these pieces', 'g', 1)} together to create a rectangular ‘patchwork’ mat whose {hl('length is twice its width', 'y', 2)}.</p>
<p class="stem">Which one of the pieces is {hl('<b>not</b>', 'b', 3)} part of my mat?</p>""",
    options={'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z'},
    notes=[(1, 'g', 'Exactly four pieces: one is left over.'),
           (2, 'y', 'Width w, length 2w, so the area is 2 × w × w: <b>2, 8, 18, 32…</b>'),
           (3, 'b', 'The leftover piece.')],
    steps=[
        f"""<p>The pieces are drawn on a square grid. Count the squares in each:</p>{_pieces()}""",
        f"""<p>The mat’s area must be 2 × (a square number): 2, 8, 18, 32… Take away each piece in turn:</p>
{calc(f'leave out V: 21 − 3 = 18 = 2 × 9 {tick()} (3 by 6)', f'leave out W: 21 − 5 = 16 {cross()}', f'leave out X: 21 − 2 = 19 {cross()}',
      f'leave out Y: 21 − 7 = 14 {cross()}', f'leave out Z: 21 − 4 = 17 {cross()}')}""",
        f"""<p>Check that the other four really fit a 3 × 6 mat:</p>{_mat()}
{calc(f'piece not used = {boxed("V")}')}""",
    ],
    answer_text='V: the other four pieces have 18 squares and make a 3 by 6 mat.',
    why={'B': 'Without W there are 16 squares. A mat twice as long as wide has area 2, 8, 18, 32…, never 16.',
         'C': 'Without X there are 19 squares: odd, so it can’t be 2 × anything.',
         'D': 'Without Y there are 14 squares: 14 = 2 × 7, and 7 isn’t a square number.',
         'E': 'Without Z there are 17 squares: odd, so it can’t be 2 × anything.'},
    fast='Squares: 3 + 5 + 2 + 7 + 4 = 21. Area must be 2, 8, 18, 32… Only 21 − 3 = 18 works, so V is left out.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _sheet():
    k = 10
    x0, y0 = 60, 40
    W, H, m = 18 * k, 24 * k, 3 * k
    parts = [rect(x0, y0, W, H, k='ink', fill='paper', sw=2.4),
             rect(x0 + m, y0 + m, W - 2 * m, H - 2 * m, k='pen', fill='b', sw=2.2)]
    parts += [line(x0, y0 - 14, x0 + W, y0 - 14, k='ink', w=1.6, head=True, tail=True),
              line(x0 - 14, y0, x0 - 14, y0 + H, k='ink', w=1.6, head=True, tail=True),
              line(x0, y0 + H / 2, x0 + m, y0 + H / 2, k='red', w=2, head=True, tail=True),
              line(x0 + W / 2, y0, x0 + W / 2, y0 + m, k='red', w=2, head=True, tail=True)]
    lab = [text(x0 + W / 2, y0 - 22, '18 cm', k='ink', size=18), text(x0 - 22, y0 + H / 2 + 6, '24', k='ink', size=18, anchor='end'),
           text(x0 + m / 2, y0 + H / 2 - 8, 'm', k='red', size=18), text(x0 + W / 2 + 12, y0 + m / 2 + 6, 'm', k='red', size=18, anchor='start'),
           text(x0 + W / 2, y0 + H / 2 - 6, 'text', k='pen', size=20), text(x0 + W / 2, y0 + H / 2 + 18, '18 − 2m by 24 − 2m', k='pen', size=15)]
    lab += [text(310, 80, 'whole page: 24 × 18 = 432 cm²', k='ink', size=19, anchor='start'),
            text(310, 112, 'text must be 432 ÷ 2 = 216 cm²', k='ink', size=19, anchor='start'),
            text(310, 160, 'try m = 3:', k='red', size=20, anchor='start', font='scrawl'),
            text(310, 190, '(24 − 6) × (18 − 6)', k='ink', size=19, anchor='start'),
            text(310, 220, '= 18 × 12 = 216 ✓', k='green', size=21, anchor='start', font='scrawl')]
    return svg(620, 300, rough(*parts) + ''.join(lab),
               'The 24 by 18 cm sheet with a margin m all round and the text area 24 minus 2m by 18 minus 2m; with m = 3 the text is 18 by 12 = 216')


Q.append(dict(
    n=14, orig=30, answer='A', topic='Area',
    question=f"""<p>A company is producing a one-page flysheet {hl('24 cm high by 18 cm wide', 'g', 1)}. It will have a text area
in the centre which has {hl('a margin of the same width all the way around', 'y', 2)}. The text must occupy
{hl('exactly half of the total area', 'y', 3)}:</p>
{fig(Y, 'ps_q14_sheet', 'A rectangle with a smaller shaded text area in the middle and an equal margin all round', 230)}
<p class="stem">What is the {hl('width of the margin', 'b', 4)}?</p>""",
    options={'A': '3.00 cm', 'B': '4.50 cm', 'C': '5.25 cm', 'D': '6.00 cm', 'E': '12.00 cm'},
    notes=[(1, 'g', 'Whole page: 24 × 18 = 432 cm².'),
           (2, 'y', 'Margin m on <b>both</b> sides of each length, so the text is (24 − 2m) by (18 − 2m).'),
           (3, 'y', 'Text area = 432 ÷ 2 = 216 cm².'),
           (4, 'b', 'Find m.')],
    steps=[
        f"""<p>Sketch it. Each side loses a margin at <b>both</b> ends:</p>{_sheet()}""",
        f"""<p>Quickest: test the options in (24 − 2m) × (18 − 2m) and look for 216.</p>
{calc(f'm = 3: 18 × 12 = 216 {tick()}', f'm = 4.5: 15 × 9 = 135 {cross()}', f'm = 5.25: 13.5 × 7.5 = 101.25 {cross()}',
      f'm = 6: 12 × 6 = 72 {cross()}', f'm = 12: 0 × (−6) {cross()} no text left at all')}
{calc(f'margin = {boxed("3.00 cm")}')}
{note('Halving the height and width (12 by 9) gives only a <b>quarter</b> of the area, not half.', 'trap')}""",
    ],
    answer_text='3.00 cm: the text is 18 cm by 12 cm = 216 cm², half of 432 cm².',
    why={'B': '4.5 cm halves the width (18 → 9) and splits the rest into two margins. The text would only be 15 × 9 = 135 cm².',
         'C': '5.25 cm is the average of 4.5 and 6. The text would be 13.5 × 7.5 = 101.25 cm².',
         'D': '6 cm halves the height (24 → 12). The text would be 12 × 6 = 72 cm², a sixth of the page.',
         'E': '12 cm is half the height. Two 12 cm margins use up all 24 cm, leaving no text at all.'},
    fast='Half of 432 is 216. Try m = 3: (24 − 6)(18 − 6) = 18 × 12 = 216. Done.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _theatre():
    rows = [('Balcony', 312.80, 325.40), ('Box', 320.00, 320.00), ('Dress Circle −15%', 324.70, 339.97),
            ('Orchestra Stalls', 328.00, 344.00), ('Grand Circle', 355.96, 372.80)]
    X = lambda v: 200 + (v - 300) * 5.4
    parts, lab = [], []
    lab.append(text(X(300), 22, 'cost for 4 people (axis starts at £300)', k='muted', size=15, anchor='start'))
    for i, (name, wd, we) in enumerate(rows):
        y = 36 + i * 50
        best = name == 'Balcony'
        parts.append(rect(X(300), y, X(wd) - X(300), 18, k='ink', fill='g' if best else 'b', sw=1.5))
        parts.append(rect(X(300), y + 20, X(we) - X(300), 18, k='ink', fill='o', sw=1.5))
        lab.append(text(190, y + 26, name, k='green' if best else 'ink', size=17, anchor='end', weight='bold' if best else None))
        lab.append(text(X(wd) + 6, y + 15, f'£{wd:.2f}', k='ink', size=15, anchor='start'))
        lab.append(text(X(we) + 6, y + 35, f'£{we:.2f}', k='muted', size=15, anchor='start'))
    lab += [text(420, 300, 'blue/green = Mon to Fri,  orange = weekend', k='ink', size=16),
            text(420, 326, 'cheapest: Balcony on a weekday, £312.80', k='green', size=20, font='scrawl')]
    return svg(660, 340, rough(*parts) + ''.join(lab),
               'Cost for four people on a weekday and at the weekend for each part of the theatre; the weekday Balcony at 312.80 is cheapest')


Q.append(dict(
    n=15, orig=31, answer='A', topic='Best deal',
    question=f"""<p>{hl('Daria and her three friends', 'g', 1)} are planning a trip to London to see a musical in the West End.
Ticket prices vary according to the location of seats in the theatre. {hl('Monday to Friday', 'y', 2)}, Balcony
seats are £78.20 per person; seats in the Dress Circle cost £95.50 per person; seats in the
Grand Circle £88.99 per person; and seats in the Orchestra Stalls £82.00 per person.</p>
<p>{hl('At the weekend (Saturday and Sunday)', 'p', 3)}, Balcony seats are £81.35 per person, seats in the
Dress Circle cost £99.99 per person; seats in the Grand Circle £93.20 per person; and seats in
the Orchestra Stalls £86.00 per person.</p>
<p>The theatre also sells Boxes which seat four people and {hl('cost £320.00 in total', 'g', 4)}. A special offer of
{hl('15% off group booking for four or more people is available on seats in the Dress Circle', 'y', 5)}.</p>
<p class="stem">Daria and her friends decide that they want to sit together in the same part of the theatre. What
is their {hl('cheapest option', 'b', 6)}?</p>""",
    options={'A': 'Balcony', 'B': 'Box', 'C': 'Dress Circle', 'D': 'Grand Circle', 'E': 'Orchestra Stalls'},
    notes=[(1, 'g', 'Daria + 3 friends = <b>4 people</b>.'),
           (2, 'y', 'Weekday prices. They can choose the day, so use the cheaper days.'),
           (3, 'p', 'Every seat costs more at the weekend, but the Box price never changes. Careful!'),
           (4, 'g', 'Already the price for all four.'),
           (5, 'y', 'Only the Dress Circle gets the 15% discount.'),
           (6, 'b', 'Cheapest total for the 4 of them.')],
    steps=[
        f"""<p>Cost for 4 people on a weekday:</p>
{calc('Balcony: 4 × 78.20 = <b>£312.80</b>', 'Box: £320.00',
      'Dress Circle: 4 × 95.50 = 382.00, minus 15% (57.30) = £324.70',
      'Orchestra Stalls: 4 × 82.00 = £328.00', 'Grand Circle: 4 × 88.99 = £355.96')}
{note('15% of 382: 10% = 38.20, 5% = 19.10, together 57.30. And 4 × 88.99 = 4 × 89 − 0.04 = 355.96.', 'tip')}""",
        f"""<p>Weekend prices are higher for every seat, so they never beat the weekday Balcony:</p>{_theatre()}
{calc(f'cheapest option = {boxed("Balcony")} (Monday to Friday)')}
{note('At the weekend the Box (£320) beats the Balcony (£325.40). If you only check weekend prices you pick the Box.', 'trap')}""",
    ],
    answer_text='Balcony on a weekday: 4 × £78.20 = £312.80.',
    why={'B': 'The Box (£320) is only cheapest at the weekend. On a weekday the Balcony is £312.80.',
         'C': 'Even with 15% off, the Dress Circle is £324.70 on a weekday.',
         'D': 'The Grand Circle is the dearest choice: £355.96 on a weekday.',
         'E': 'Orchestra Stalls cost £328.00 on a weekday, £15.20 more than the Balcony.'},
    fast='Weekday × 4: Balcony 312.80, Box 320, Dress Circle 324.70 after 15% off. Balcony wins.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _bottle_graphs():
    parts, lab = [], []

    def axes(x0, y0):
        return [line(x0, y0, x0, y0 - 210, k='ink', w=2, head=True), line(x0, y0, x0 + 170, y0, k='ink', w=2, head=True)]

    # panel 1: bottle D and its graph
    parts.append(path('M52 40 L52 92 Q20 98 20 126 L20 250 L100 250 L100 126 Q100 98 72 92 L72 40', k='ink', sw=2.4))
    parts += [line(21, 230, 99, 230, k='pen', w=1.5, dash=True), line(21, 160, 99, 160, k='pen', w=1.5, dash=True)]
    lab += [text(60, 210, 'wide', k='pen', size=15), text(60, 132, 'shoulder', k='orange', size=14), text(80, 60, 'neck', k='red', size=14, anchor='start')]
    parts += axes(150, 252)
    parts.append(path('M150 252 L222 206 Q250 190 262 140 L282 52', k='violet', sw=3.2))
    lab += [text(140, 52, 'h', k='ink', size=16), text(310, 266, 't', k='ink', size=16),
            text(172, 216, 'gentle', k='pen', size=14), text(270, 168, 'smooth', k='orange', size=14, anchor='start'),
            text(270, 186, 'bend', k='orange', size=14, anchor='start'), text(288, 80, 'steep', k='red', size=14, anchor='start'),
            text(170, 22, 'D: the lost graph', k='violet', size=19, font='scrawl')]
    # panel 2: E and graph 3
    parts.append(path('M378 40 L378 120 L350 120 L350 250 L426 250 L426 120 L398 120 L398 40', k='ink', sw=2.4))
    lab += [text(388, 200, 'wide', k='pen', size=15), text(406, 66, 'neck', k='red', size=14, anchor='start'),
            text(430, 114, 'flat', k='orange', size=14, anchor='start')]
    parts += axes(480, 252)
    parts.append(path('M480 252 L572 196 L612 52', k='green', sw=3.2))
    parts.append(circle(572, 196, 9, k='orange', sw=2))
    lab += [text(470, 52, 'h', k='ink', size=16), text(640, 266, 't', k='ink', size=16),
            text(584, 214, 'sharp corner', k='orange', size=14, anchor='start'),
            text(500, 22, 'E: graph 3', k='green', size=19, font='scrawl')]
    return svg(660, 280, rough(*parts) + ''.join(lab),
               'Left: bottle D and its graph, gentle then a smooth bend then steep. Right: container E and graph 3 with a sharp corner')


Q.append(dict(
    n=16, orig=32, answer='D', topic='Graphs & shapes',
    question=f"""<p>Water was poured into five containers {hl('at a steady rate', 'y', 1)} until each was full. A graph of the depth
of water (h) in the container against time (t) was sketched for each container. {hl('One of the graphs has been lost', 'p', 2)}.</p>
{fig(Y, 'ps_q16_graphs', 'Four depth-time graphs: 1 a straight line; 2 gentle then a jump to steep that bends over; 3 gentle then steep with a sharp corner; 4 steep, flattening, then steepening, then straight', 480)}
<p class="stem">Which one of the following containers is {hl('<b>not</b>', 'b', 3)} represented by any of the above graphs?</p>
{fig(Y, 'ps_q16_containers', 'Five containers: A a box with a widening funnel on top; B a ball with a narrow neck; C a straight-sided tub; D a bottle with rounded shoulders; E a box with a flat shoulder and a narrow neck', 400)}""",
    options={'A': 'container A', 'B': 'container B', 'C': 'container C', 'D': 'container D', 'E': 'container E'},
    notes=[(1, 'y', 'Same amount of water every second. <b>Narrow</b> part: the level shoots up (steep). <b>Wide</b> part: it creeps up (gentle).'),
           (2, 'p', '4 graphs, 5 containers. Match four of them; the one left is the answer.'),
           (3, 'b', 'The container with no graph.')],
    steps=[
        f"""<p>Rules for these graphs:</p>
<ul><li>straight sides {ar()} straight line</li><li>narrow {ar()} steep, wide {ar()} gentle</li>
<li>width changing gradually {ar()} curve; width changing suddenly {ar()} sharp corner</li></ul>""",
        f"""<p>Match each graph:</p>
{calc(f'graph 1, one straight line {ar()} C (straight-sided tub)',
      f'graph 2, gentle, then steep but getting gentler {ar()} A (box, then a funnel that widens)',
      f'graph 3, gentle, sharp corner, steep {ar()} E (wide box, flat shoulder, narrow neck)',
      f'graph 4, steep, flatter, steeper, then straight {ar()} B (ball: narrow, wide, narrow, then neck)')}""",
        f"""<p>D is left. Its graph would bend <b>smoothly</b> at the rounded shoulder. Graph 3 has a sharp corner, which needs E’s flat shoulder:</p>
{_bottle_graphs()}
{calc(f'no graph for {boxed("D")}')}""",
    ],
    answer_text='Container D: its rounded shoulders would give a smooth bend, and no graph has one.',
    why={'A': 'A is graph 2: gentle in the box, then steep at the narrow bottom of the funnel, getting gentler as it widens.',
         'B': 'B is graph 4: steep at the narrow bottom of the ball, gentle across the wide middle, steep again near the top, then straight up the neck.',
         'C': 'C is graph 1: straight sides all the way, so one straight line.',
         'E': 'E is graph 3: a gentle line in the wide box, a sudden switch at the flat shoulder (sharp corner), then steep in the neck.'},
    fast='Narrow = steep, wide = gentle, sudden change = sharp corner. C, A, E, B match graphs 1–4; D’s rounded shoulder needs a smooth bend, which isn’t there.',
))


# ---------------------------------------------------------------- 17 (Q36)
def _service():
    X = lambda v: 60 + v * 34
    parts, lab = [], []
    for y, ok, label, k in ((70, {1, 6, 11, 16}, 'coffee: 121 − s divides by 5', 'pen'),
                            (170, {2, 6, 10, 14}, 'tea: 82 − s divides by 4', 'orange')):
        parts.append(line(X(0), y, X(16.8), y, k='ink', w=2))
        lab.append(text(X(0), y - 30, label, k=k, size=18, anchor='start'))
        for v in range(17):
            parts.append(line(X(v), y - 6, X(v), y + 6, k='ink', w=1.4))
            lab.append(text(X(v), y + 26, v, k='muted', size=14))
            if v in ok:
                parts.append(circle(X(v), y, 8, k=k, fill='b' if k == 'pen' else 'o', sw=2.2))
    parts.append(rect(X(6) - 20, 36, 40, 168, k='green', sw=2.6, rx=14))
    lab.append(text(X(6) + 30, 232, 's = 6p is the first in both lists', k='green', size=20, font='scrawl', anchor='start'))
    return svg(660, 246, rough(*parts) + ''.join(lab),
               'Two number lines from 0 to 16: coffee works for 1, 6, 11, 16; tea works for 2, 6, 10, 14; 6 is the first in both')


Q.append(dict(
    n=17, orig=36, answer='D', topic='Number puzzles',
    question=f"""<p>The payment systems which use pre-paid magnetic swipe cards are not all that wonderful. We
had one put into the office last week to operate the tea and coffee dispensing machine. I was
somewhat surprised to find, after having {hl('five coffees, that I had spent 121p', 'g', 1)}, and my colleague,
after {hl('four teas, had spent 82p', 'g', 2)}. We were assured that there had been no changes in the prices;
the problem appears to be that if you ask the machine how much you have left, it deducts a
‘service’ charge for this ‘service’. {hl('We both enquired once', 'y', 3)}. Charges for tea, coffee and service
are {hl('whole numbers', 'y', 4)}.</p>
<p class="stem">What is the {hl('minimum', 'b', 5)} that the service charge could be?</p>""",
    options={'A': '1p', 'B': '2p', 'C': '4p', 'D': '6p', 'E': '14p'},
    notes=[(1, 'g', '5 coffees + 1 service charge = 121p.'),
           (2, 'g', '4 teas + 1 service charge = 82p.'),
           (3, 'y', 'One service charge in each total.'),
           (4, 'y', 'Whole pence: 121 − s must divide by 5, and 82 − s must divide by 4.'),
           (5, 'b', 'The smallest s that works for <b>both</b>.')],
    steps=[
        f"""<p>Call the service charge s:</p>
{calc('5 × coffee + s = 121', '4 × tea + s = 82')}""",
        f"""<p>Coffee: 121 − s must be a multiple of 5 (ends in 0 or 5), so s ends in 1 or 6.<br>
Tea: 82 − s must be a multiple of 4.</p>
{calc('coffee works: s = 1, 6, 11, 16…', 'tea works: s = 2, 6, 10, 14…')}
{_service()}""",
        f"""<p>The smallest in both lists is 6:</p>
{calc('coffee = (121 − 6) ÷ 5 = 115 ÷ 5 = 23p ' + tick(), 'tea = (82 − 6) ÷ 4 = 76 ÷ 4 = 19p ' + tick(),
      f'minimum service charge = {boxed("6p")}')}""",
    ],
    answer_text='6p (coffee 23p, tea 19p).',
    why={'A': '1p works for coffee (120 ÷ 5 = 24p) but not for tea: 81 ÷ 4 isn’t whole.',
         'B': '2p works for tea (80 ÷ 4 = 20p) but not for coffee: 119 ÷ 5 isn’t whole.',
         'C': '4p fails both: 117 ÷ 5 and 78 ÷ 4 aren’t whole.',
         'E': '14p works for tea (68 ÷ 4 = 17p) but not coffee: 107 ÷ 5 isn’t whole. And 6p is smaller anyway.'},
    fast='s = 121 − (multiple of 5): 1, 6, 11… and s = 82 − (multiple of 4): 2, 6, 10… First match: 6p.',
))
