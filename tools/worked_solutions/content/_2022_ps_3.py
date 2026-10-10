import math
from wslib import *

Y = 2022
Q = []


# ---------------------------------------------------------------- 18 (Q37)
def _shots():
    parts, lab = [], []
    items = [(90, 'glink', 'g', '2', 'y'), (250, 'creamer', '2g', '4', 'b'), (410, 'chop', '2g + 1', '5', 'g'), (570, 'yip', 'y', '3', 'o')]
    for x, name, alg, val, f in items:
        parts.append(circle(x, 84, 48, k='ink', fill=f, sw=2))
        lab.append(text(x, 72, name, k='ink', size=18))
        lab.append(text(x, 102, alg, k='pen', size=22, font='scrawl'))
        lab.append(text(x, 164, f'= {val}', k='green', size=26, font='scrawl'))
    parts.append(arrow(140, 70, 200, 70, k='red', bend=-0.2))
    parts.append(arrow(300, 70, 360, 70, k='red', bend=-0.2))
    lab += [text(170, 40, '× 2', k='red', size=20), text(330, 40, '+ 1', k='red', size=20),
            text(570, 22, 'on its own', k='muted', size=14),
            text(330, 206, 'glink 2 → creamer 4 → chop 5, and yip 3', k='green', size=20, font='scrawl')]
    return svg(660, 220, rough(*parts) + ''.join(lab),
               'Glink g, creamer 2g, chop 2g plus 1, yip y; solving gives glink 2, creamer 4, chop 5, yip 3')


Q.append(dict(
    n=18, orig=37, answer='C', topic='Equations & scoring',
    question=f"""<p>In a ball game points are accumulated by different combinations of four winning shots called a
chop, a creamer, a glink and a yip. Playing the game for the first time, the only knowledge I
have about the scoring system is that {hl('a chop is worth one point more than a creamer', 'y', 1)}, and {hl('a creamer is worth twice as many points as a glink', 'y', 1)}. I lose narrowly by {hl('47 points', 'g', 2)} to {hl('50', 'g', 3)}, scoring
{hl('3 chops, 4 yips, 3 creamers and 4 glinks', 'g', 2)}. My victorious opponent scored {hl('5 chops, 3 yips, 3 creamers and 2 glinks', 'g', 3)}.</p>
<p class="stem">Which one of the following statements about the scoring system is the {hl('only one that is true', 'b', 4)}?</p>""",
    options={'A': 'A creamer is worth more points than a chop.', 'B': 'Two chops are worth less than three yips.',
             'C': 'A glink is worth 2 points.', 'D': 'Three yips are worth more than three creamers.', 'E': 'A chop is worth 6 points.'},
    notes=[(1, 'y', 'Everything except the yip can be written using the glink: creamer = 2 × glink, chop = creamer + 1.'),
           (2, 'g', 'My 47 points.'),
           (3, 'g', 'The opponent’s 50 points.'),
           (4, 'b', 'Find the actual values, then test all five statements.')],
    steps=[
        f"""<p>Call a glink <b>g</b> and a yip <b>y</b>. Then everything else follows:</p>{_shots()}""",
        f"""<p>Write each score using g and y:</p>
{calc('me: 3(2g + 1) + 3(2g) + 4g + 4y = 16g + 3 + 4y = 47', f'{ar()} 16g + 4y = 44 {ar()} ÷ 4: <b>4g + y = 11</b>',
      'opponent: 5(2g + 1) + 3(2g) + 2g + 3y = 18g + 5 + 3y = 50', f'{ar()} 18g + 3y = 45 {ar()} ÷ 3: <b>6g + y = 15</b>')}""",
        f"""<p>The two short equations differ only in the g’s:</p>
{calc('(6g + y) − (4g + y) = 15 − 11', '2g = 4, so g = 2, and y = 11 − 8 = 3', 'creamer = 4, chop = 5')}
{calc('me: 3 × 5 + 3 × 4 + 4 × 2 + 4 × 3 = 15 + 12 + 8 + 12 = 47 ' + tick(),
      'opponent: 5 × 5 + 3 × 4 + 2 × 2 + 3 × 3 = 25 + 12 + 4 + 9 = 50 ' + tick())}
{note('No algebra? Try glink = 1: then 4 + y = 11 gives y = 7, and the opponent would need 6 + 7 = 15, but it’s 13. Try glink = 2: y = 3 and 12 + 3 = 15 ✓.', 'tip')}""",
        f"""<p>Test the statements:</p>
{calc(f'A: creamer 4 more than chop 5? {cross()}', f'B: 2 chops = 10 less than 3 yips = 9? {cross()}',
      f'C: glink = 2 ' + tick(), f'D: 3 yips = 9 more than 3 creamers = 12? {cross()}', f'E: chop = 6? No, 5 {cross()}',
      f'answer {ar()} {boxed("C")}')}""",
    ],
    answer_text='A glink is worth 2 points (creamer 4, chop 5, yip 3).',
    why={'A': 'A chop is a creamer + 1, so a creamer can never be worth more than a chop (4 against 5).',
         'B': 'Two chops are 10 points and three yips are 9. The chops are worth more.',
         'D': 'Three yips are 9 points but three creamers are 12. The yips are worth less.',
         'E': 'A chop is 5 points, not 6. (6 would make the glink 2.5 and the scores wouldn’t fit.)'},
    fast='Glink g, creamer 2g, chop 2g + 1. My score gives 4g + y = 11, the opponent’s 6g + y = 15. So 2g = 4, glink = 2.',
))


# ---------------------------------------------------------------- 19 (Q38)
CAT = [('hatch', 'y'), ('saloon', 'b'), ('utility', 'g'), ('estate', 'paper'), ('carrier', 'v')]


def _pie(cx, cy, r, counts):
    parts, lab, a0 = [], [], -90.0
    total = sum(counts)
    for n, (_, f) in zip(counts, CAT):
        a1 = a0 + 360 * n / total
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        big = 1 if a1 - a0 > 180 else 0
        parts.append(path(f'M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f} Z', k='ink', fill=f, sw=1.8))
        am = math.radians((a0 + a1) / 2)
        lr = r * 0.66
        lab.append(text(cx + lr * math.cos(am), cy + lr * math.sin(am) + 8, n, k='ink', size=22, weight=700))
        a0 = a1
    return parts, lab


def _vehicles():
    p1, l1 = _pie(120, 130, 86, [12, 8, 6, 4, 2])
    p2, l2 = _pie(380, 130, 86, [1, 2, 2, 2, 1])
    parts, lab = p1 + p2, l1 + l2
    lab += [text(120, 32, 'start: 32 vehicles', k='ink', size=18), text(380, 32, 'end: 8 left', k='ink', size=18),
            text(250, 140, '−', k='red', size=40)]
    for i, (name, f) in enumerate(CAT):
        y = 66 + i * 30
        parts.append(rect(505, y - 15, 22, 20, k='ink', fill=f, sw=1.4))
        lab.append(text(536, y + 1, name, k='ink', size=17, anchor='start'))
    x, X0, s = 0, 60, 21
    sold = [11, 6, 4, 2, 1]
    for n, (name, f) in zip(sold, CAT):
        parts.append(rect(X0 + x * s, 270, n * s, 40, k='ink', fill=f, sw=1.8))
        lab.append(text(X0 + x * s + n * s / 2, 297, n, k='ink', size=20, weight=700))
        x += n
    lab += [text(X0, 258, 'sold = start − end (24 in all)', k='ink', size=17, anchor='start'),
            text(X0 + 24 * s + 14, 298, '= bar 4', k='green', size=24, font='scrawl', anchor='start')]
    return svg(660, 326, rough(*parts) + ''.join(lab),
               'Start pie of 32: hatch 12, saloon 8, utility 6, estate 4, carrier 2. End pie of 8: 1, 2, 2, 2, 1. Sold: 11, 6, 4, 2, 1, which is bar 4')


Q.append(dict(
    n=19, orig=38, answer='D', topic='Pie charts & bar charts',
    question=f"""<p>At the beginning of the day, a showroom had {hl('32 vehicles', 'g', 1)} for sale. The vehicles were advertised
in five categories: hatchback, saloon, utility, estate car and people carrier. By the end of the
day, {hl('24 vehicles had been sold', 'g', 2)}.</p>
<p>The first chart shows a comparison of the numbers of vehicles in each category in the
showroom at the beginning of the day, and the second chart shows a comparison of the
numbers in the same categories in the showroom at the end of the day.</p>
{fig(Y, 'ps_q19_pies', 'Two pie charts, beginning of the day and end of the day, split into hatch, saloon, utility, estate and carrier', 560)}
<p class="stem">Which one of the following shows a comparison of the {hl('numbers of cars in each category that were sold', 'b', 3)}?</p>
{fig(Y, 'ps_q19_bars', 'Five stacked bars, bar 1 to bar 5, on a scale from 0 to 25, split into the same five categories', 560)}""",
    options={'A': 'bar 1', 'B': 'bar 2', 'C': 'bar 3', 'D': 'bar 4', 'E': 'bar 5'},
    notes=[(1, 'g', 'The first pie is 32 vehicles: each one is 360 ÷ 32 = 11.25°.'),
           (2, 'g', 'So only 32 − 24 = <b>8</b> are left: the second pie is just 8 vehicles (45° each).'),
           (3, 'b', 'Sold = start − end, for each category. The pies are different sizes of total, so you can’t compare angles directly.')],
    steps=[
        f"""<p>Turn each pie into numbers using simple fractions:</p>
{calc('start (32): saloon is a right angle = ¼ = 8; carrier is a thin sliver = 1/16 = 2',
      'estate = ⅛ = 4; hatch = ⅜ = 12; utility = the rest = 32 − 26 = 6',
      'end (8): every slice is a whole number of eighths (45°)',
      'hatch ⅛ = 1, saloon ¼ = 2, utility ¼ = 2, estate ¼ = 2, carrier ⅛ = 1')}""",
        f"""<p>Subtract to get the numbers sold:</p>{_vehicles()}
{calc('hatch 12 − 1 = 11', 'saloon 8 − 2 = 6', 'utility 6 − 2 = 4', 'estate 4 − 2 = 2', 'carrier 2 − 1 = 1',
      f'total 24 ' + tick() + f' {ar()} {boxed("bar 4")}')}""",
    ],
    answer_text='Bar 4: 11 hatchbacks, 6 saloons, 4 utilities, 2 estates and 1 carrier sold.',
    why={'A': 'Bar 1 sells 10 hatchbacks and 3 estates. That would leave 2 hatchbacks and 1 estate, but the end pie has 1 hatchback and 2 estates.',
         'B': 'Bar 2 swaps saloon and utility (4 saloons, 6 utilities). Selling 6 utilities leaves none, but the end pie still has 2.',
         'C': 'Bar 3 sells 11 utilities, but there were only 6 utilities to start with.',
         'E': 'Bar 5 sells 11 saloons, but there were only 8 saloons to start with.'},
    fast='Start: 12, 8, 6, 4, 2. End (8 left, eighths): 1, 2, 2, 2, 1. Sold: 11, 6, 4, 2, 1 = bar 4.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _coins():
    parts, lab = [], []
    stages = [(90, [(200, 28), (20, 20)], 'start', '220p'), (330, [(100, 26), (10, 18)], 'change after day 1', '110p'),
              (570, [(50, 24), (5, 15)], 'change after day 2', '55p')]
    for cx, coins, title, tot in stages:
        lab.append(text(cx, 34, title, k='muted', size=16))
        for (v, r), dx in zip(coins, (-32, 32)):
            parts.append(circle(cx + dx, 92, r, k='orange', fill='o', sw=2.2))
            lab.append(text(cx + dx, 98, f'{v}p', k='ink', size=15 if v < 100 else 14))
        lab.append(text(cx, 156, f'= {tot}', k='pen', size=21, font='scrawl'))
    parts.append(arrow(150, 92, 268, 92, k='red', bend=0))
    parts.append(arrow(390, 92, 508, 92, k='red', bend=0))
    lab += [text(209, 72, 'pay 2 bars', k='red', size=16), text(209, 118, '110p', k='red', size=17),
            text(449, 72, 'pay 1 bar', k='red', size=16), text(449, 118, '55p', k='red', size=17),
            text(330, 200, 'six different coins, each used once ✓   bar = 55p', k='green', size=20, font='scrawl')]
    return svg(660, 214, rough(*parts) + ''.join(lab),
               'Start with 200p and 20p, pay 110p for two bars, get 100p and 10p change; pay 55p for one bar, get 50p and 5p change')


Q.append(dict(
    n=20, orig=42, answer='D', topic='Money & logic',
    question=f"""<p>In my currency, there are {hl('six types of coin', 'g', 1)} in circulation:</p>
<p>200p&nbsp;&nbsp;&nbsp; 100p&nbsp;&nbsp;&nbsp; 50p&nbsp;&nbsp;&nbsp; 20p&nbsp;&nbsp;&nbsp; 10p&nbsp;&nbsp;&nbsp; 5p</p>
<p>I start with two coins. I visit a shop and {hl('purchase two bars of chocolate and pay using the two coins', 'y', 2)}. My change consists of two coins.</p>
<p>The next day I re-visit the shop and {hl('purchase another one bar of chocolate with that change', 'y', 2)}.
My new change, again, consists of two coins.</p>
<p>{hl('The six coins I possess during these two days are all different', 'p', 3)}. I only have two coins at any
particular time. {hl('The price of a bar of chocolate does not change', 'y', 4)}.</p>
<p class="stem">What is the {hl('price of a bar of chocolate', 'b', 5)}?</p>""",
    options={'A': '15p', 'B': '25p', 'C': '30p', 'D': '55p', 'E': '60p'},
    notes=[(1, 'g', 'Six types, and six different coins: so I have each coin exactly once. Total 200 + 100 + 50 + 20 + 10 + 5 = 385p.'),
           (2, 'y', 'Day 1: start pair − 2 bars = change pair. Day 2: change pair − 1 bar = final pair.'),
           (3, 'p', 'The key clue! The 6 coins split into 3 pairs: start, middle, final.'),
           (4, 'y', 'The same price P both days.'),
           (5, 'b', 'Test the options.')],
    steps=[
        f"""<p>Call the price P. Working back from the final pair:</p>
{calc('middle pair = final pair + P', 'start pair = middle pair + 2P = final pair + 3P',
      'all six coins: 3 × final pair + 4P = 385p')}""",
        f"""<p>Try each option: (385 − 4P) ÷ 3 must be a total two coins can make.</p>
{calc(f'15p: (385 − 60) ÷ 3 = 108⅓ {cross()}', f'25p: (385 − 100) ÷ 3 = 95, but no two coins make 95p {cross()}',
      f'30p: (385 − 120) ÷ 3 = 88⅓ {cross()}', f'55p: (385 − 220) ÷ 3 = 55 = 50p + 5p ' + tick(),
      f'60p: (385 − 240) ÷ 3 = 48⅓ {cross()}')}""",
        f"""<p>Check 55p all the way through:</p>{_coins()}
{calc('final 50p + 5p = 55p', 'middle 55 + 55 = 110p = 100p + 10p ' + tick(), 'start 110 + 110 = 220p = 200p + 20p ' + tick(),
      f'price = {boxed("55p")}')}""",
    ],
    answer_text='55p: start with 200p + 20p, change 100p + 10p, then change 50p + 5p.',
    why={'A': '15p doesn’t split the six coins into three pairs: the final pair would have to be 108⅓p.',
         'B': '25p needs a final pair worth 95p, and no two of the coins make 95p.',
         'C': '30p: the final pair would be 88⅓p, impossible.',
         'E': '60p: the final pair would be 48⅓p, impossible.'},
    fast='Each coin used once, total 385p. 3 × final pair + 4 × price = 385. Only 55p works: final 55 (50 + 5), middle 110 (100 + 10), start 220 (200 + 20).',
))


# ---------------------------------------------------------------- 21 (Q43)
GRID = [[3, 1, 5, 1, 2], [1, 2, 0, 4, 5], [2, 1, 2, 3, 1], [1, 2, 2, 5, 2], [5, 4, 3, 2, 4]]
GREY = {(0, 0), (0, 4), (1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 0), (4, 4)}


def _score(r, c):
    s = 0
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < 5 and 0 <= cc < 5:
            s += GRID[rr][cc] + (0 if (rr, cc) in GREY else 1)
    return s


def _tokens():
    parts, lab = [], []
    # zoom on the winning square
    c, cx, cy = 58, 130, 150
    cells = [(0, 0, '0', 'paper'), (0, -1, '5', 'paper'), (-1, 0, '2', 'v'), (1, 0, '4', 'v'), (0, 1, '2', 'v')]
    for dx, dy, v, f in cells:
        x, y = cx + dx * c - c / 2, cy + dy * c - c / 2
        parts.append(rect(x, y, c, c, k='red' if (dx, dy) == (0, 0) else 'ink', fill=f, sw=2.6 if (dx, dy) == (0, 0) else 1.8))
        lab.append(text(x + c / 2, y + c / 2 + 9, v, k='ink', size=26, font='print'))
    lab += [text(cx + 44, cy - c - 6, '+1 white', k='green', size=17, anchor='start'),
            text(cx, cy + c + 56, '5 + 2 + 4 + 2 = 13 tokens', k='pen', size=18),
            text(cx, cy + c + 82, '+ 1 white neighbour = 14', k='green', size=20, font='scrawl'),
            text(cx, 30, 'place it on the 0 square', k='red', size=17)]
    # score map
    x0, y0, s = 330, 56, 54
    lab.append(text(x0 + 2.5 * s, 36, 'score if the token goes here', k='ink', size=17))
    for r in range(5):
        for cc in range(5):
            f = 'v' if (r, cc) in GREY else 'paper'
            parts.append(rect(x0 + cc * s, y0 + r * s, s, s, k='ink', fill=f, sw=1.5))
            v = _score(r, cc)
            lab.append(text(x0 + cc * s + s / 2, y0 + r * s + s / 2 + 8, v, k='red' if v == 14 else 'ink', size=22 if v == 14 else 19,
                            weight=700 if v >= 13 else None))
    parts.append(circle(x0 + 2.5 * s, y0 + 1.5 * s, 22, k='red', sw=2.6))
    lab.append(text(x0 + 2.5 * s, y0 + 5 * s + 30, 'shaded = grey square (no bonus)', k='muted', size=15))
    return svg(640, 360, rough(*parts) + ''.join(lab),
               'Zoom on the 0 square with neighbours 5 white, 2, 4 and 2 grey, scoring 14; and a map of the score for every square, with 14 the highest')


Q.append(dict(
    n=21, orig=43, answer='E', topic='Grids & scoring',
    question=f"""<p>In a game, players take it in turns to place tokens onto squares of a grid. The squares on the
grid are coloured white and grey. When a player places a token they {hl('score one point for every token on an adjacent square (either horizontally or vertically)', 'y', 1)}. {hl('For every adjacent square that is white an extra point is scored', 'p', 2)}.</p>
<p>The diagram below shows a position in one game. The number on each square shows the
number of tokens currently placed on that square:</p>
{fig(Y, 'ps_q21_grid', 'A 5 by 5 grid of numbers with grey squares in an X pattern: row 1: 3 grey, 1, 5, 1, 2 grey; row 2: 1, 2 grey, 0, 4 grey, 5; row 3: 2, 1, 2 grey, 3, 1; row 4: 1, 2 grey, 2, 5 grey, 2; row 5: 5 grey, 4, 3, 2, 4 grey', 190)}
<p class="stem">What is the {hl('maximum', 'b', 3)} number of points that could be scored when the next token is placed on
the board?</p>""",
    options={'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14'},
    notes=[(1, 'y', 'Only the 4 squares up, down, left and right count. No diagonals.'),
           (2, 'p', '+1 per white <b>square</b>, however many tokens are on it. Grey neighbours give no bonus.'),
           (3, 'b', 'Find the best square. It can be any square, even one with 0 tokens.')],
    steps=[
        f"""<p>Score for a square = tokens on its 4 neighbours + 1 for each neighbour that is white.
The grey squares make an X (the corners, the middle and the 4 in between), so the best spots are next to big numbers.</p>""",
        f"""<p>The 0 square in row 2 is surrounded by 5, 2, 4 and 2. Work out every square to be sure:</p>{_tokens()}""",
        f"""{calc('0 square: 5 + 2 + 4 + 2 = 13, and only the 5 above is white: + 1', f'= {boxed("14")}, the highest anywhere')}
{note('Squares at the edge have only 2 or 3 neighbours, so they rarely win. Start with the middle squares next to the biggest numbers.', 'tip')}""",
    ],
    answer_text='14: on the 0 square (row 2), next to 5 (white), 2, 4 and 2 (grey).',
    why={'A': '10 is the score in the very centre (0 + 1 + 3 + 2 = 6 tokens + 4 white). Lots of white bonus, but too few tokens nearby.',
         'B': '11 is what several edge squares score, such as the 1 at the top next to 3, 5 and 2.',
         'C': '12 is what you get on the 1 in the top row next to 5, 2 and 4 (11 tokens + 1 white). Good, but not the best.',
         'D': '13 is the next best (for example the grey 4 in row 2: 1 + 0 + 5 + 3 = 9, + 4 white). Or the 0 square without its white bonus.'},
    fast='Look for big numbers around one square: the 0 square has 5, 2, 4, 2 = 13, plus 1 for the white 5 above. 14.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _cards():
    parts, lab = [], []
    gone = {1, 2, 5, 7, 8, 10, 11, 13, 14, 15}
    show = {3: ('M', 'b'), 12: ('C', 'o'), 16: ('= 7?', 'paper'), 4: ('?', 'paper'), 6: ('?', 'paper'), 9: ('?', 'paper'),
            8: ('M', 'paper'), 10: ('C', 'paper')}
    for n in range(1, 17):
        i, j = (n - 1) % 4, (n - 1) // 4
        x, y = 24 + i * 68, 30 + j * 78
        if n in gone:
            parts.append(rect(x, y, 56, 66, k='muted', fill='paper', sw=1.4, rx=5))
            lab.append(text(x + 28, y + 60, 'kept', k='muted', size=13))
        else:
            parts.append(rect(x, y, 56, 66, k='ink', fill=show[n][1], sw=2.2, rx=5))
        lab.append(text(x + 6, y + 15, n, k='muted' if n in gone else 'ink', size=13, anchor='start'))
        if n in show:
            big, _ = show[n]
            lab.append(text(x + 28, y + 42, big, k='muted' if n in gone else 'red' if n in (3, 12) else 'ink',
                            size=24 if len(big) == 1 else 17, font='print', weight=700))
    tx = 312
    rows = [('My turn: 3 & 8 were two mice (I saw them)', 'pen'), ('so 3 = mouse and 8 = mouse', 'pen'),
            ('Sister: 8 & 10 were a pair, so 10 = cat', 'pen'), ('Sister: 10 & 12 went back (same),', 'pen'),
            ('so 12 = cat', 'pen'), ('3 (mouse) + 12 (cat) = sure pair!', 'green'),
            ('16 matched 7, but 7’s animal is unknown', 'muted'), ('4, 6 and 9 have never been seen', 'muted')]
    for k, (t, col) in enumerate(rows):
        lab.append(text(tx, 52 + k * 34, t, k=col, size=17 if col != 'green' else 20, anchor='start', font='scrawl' if col == 'green' else 'hand'))
    return svg(660, 350, rough(*parts) + ''.join(lab),
               'The 16 cards: those already kept are greyed out; card 3 is a mouse, card 12 is a cat, card 16 matches 7, and 4, 6 and 9 are unknown')


Q.append(dict(
    n=22, orig=44, answer='D', topic='Logic & deduction',
    question=f"""<p>In <i>Cat and Mouse</i>, a game for two players, 16 cards are shuffled and then placed face down on
a table as shown below:</p>
{fig(Y, 'ps_q22_cards', 'Sixteen face-down cards in a 4 by 4 grid numbered 1 to 16', 150)}
<p>[The numbers below the cards are for identification purposes.]</p>
<p>Cats are pictured on 8 of the cards and mice on the other 8. Both players pick up two cards at
each turn, taking care not to show the cards to the other player. {hl('If the two cards are a cat and a mouse, the player <b>keeps the cards</b> and scores a point', 'y', 1)}, but {hl('does not reveal which was the cat and which was the mouse', 'p', 2)}. {hl('If, however, the two cards are both cats or both mice, the player must put the cards back in the same places', 'y', 3)}.</p>
<p>My sister and I are currently playing a game, and I am leading by 3 points to 2. The game has
progressed so far as follows:</p>
{table([['me', 'cards 2 &amp; 13', 'cat and mouse pair', '1 point'], ['sister', 'cards 7 &amp; 16', 'cards replaced', ''],
        ['me', 'cards 5 &amp; 11', 'cat and mouse pair', '1 point'], ['sister', hl('cards 10 &amp; 12', 'g'), hl('cards replaced', 'g'), ''],
        [hl('me', 'g', 4), hl('cards 3 &amp; 8', 'g'), hl('two mice; cards replaced', 'g'), ''], ['sister', 'cards 7 &amp; 14', 'cat and mouse pair', '1 point'],
        ['me', 'cards 1 &amp; 15', 'cat and mouse pair', '1 point'], ['sister', hl('cards 8 &amp; 10', 'g'), hl('cat and mouse pair', 'g'), '1 point']])}
<p>It is my turn again and {hl('I know for certain', 'b', 5)} that the two cards I am going to pick up will be a cat
and mouse pair.</p>
<p class="stem">Which two cards am I going to pick up?</p>""",
    options={'A': '3 &amp; 4', 'B': '3 &amp; 6', 'C': '3 &amp; 9', 'D': '3 &amp; 12', 'E': '3 &amp; 16'},
    notes=[(1, 'y', 'Kept cards leave the table. A kept pair is always one cat + one mouse.'),
           (2, 'p', 'So you never learn which card in a kept pair was which… unless you know one of them already.'),
           (3, 'y', 'Replaced cards are the <b>same</b> animal as each other.'),
           (4, 'g', 'My own turn: I saw these! 3 and 8 are both mice.'),
           (5, 'b', 'I need a card I <b>know</b> is a cat to go with mouse 3.')],
    steps=[
        f"""<p>First, which cards are still on the table? Kept: 2, 13, 5, 11, 7, 14, 1, 15, 8, 10.
Left: <b>3, 4, 6, 9, 12, 16</b>.</p>""",
        f"""<p>Follow the chain of clues from what I saw:</p>
{calc(f'3 & 8: two mice {ar()} 3 = mouse, 8 = mouse', f'8 & 10: cat and mouse pair, and 8 is a mouse {ar()} 10 = cat',
      f'10 & 12: put back, so the same animal {ar()} 12 = cat')}{_cards()}""",
        f"""{calc(f'3 (mouse) + 12 (cat) {ar()} {boxed("3 &amp; 12")}')}
{note('Card 16 is a trap: it matched 7, but 7 went off in a cat and mouse pair, so nobody knows if 7 (and 16) is a cat or a mouse.', 'trap')}""",
    ],
    answer_text='3 and 12: 3 is a mouse (I saw it) and 12 must be a cat.',
    why={'A': 'Card 4 has never been picked up, so it could be a cat or a mouse.',
         'B': 'Card 6 has never been picked up either. No way to know.',
         'C': 'Card 9 has never been picked up. It might be another mouse.',
         'E': 'Card 16 is the same animal as 7, but 7 left in a cat and mouse pair, so its animal is unknown.'},
    fast='3 is a mouse (I saw it with 8). 8 & 10 were a pair, so 10 is a cat. 10 & 12 matched, so 12 is a cat. Pick 3 & 12.',
))


# ---------------------------------------------------------------- 23 (Q46)
POSSIBLE = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 26, 30}


def _strip():
    parts, lab = [], []
    x0, y0, w, h = 30, 26, 56, 42
    for n in range(1, 31):
        i, j = (n - 1) % 10, (n - 1) // 10
        x, y = x0 + i * w, y0 + j * (h + 6)
        ok = n in POSSIBLE
        parts.append(rect(x + 2, y, w - 4, h, k='ink' if ok else 'red', fill='g' if ok else 'p', sw=1.4 if ok else 2))
        lab.append(text(x + w / 2, y + 28, n, k='ink' if ok else 'red', size=19, weight=None if ok else 700))
    parts.append(circle(x0 + 3 * w + w / 2, y0 + 2 * (h + 6) + h / 2, 30, k='red', sw=3))
    lab += [text(x0, y0 + 3 * (h + 6) + 26, 'green = can be made from up to three of 10, 6, 3, 1', k='green', size=16, anchor='start'),
            text(x0, y0 + 3 * (h + 6) + 54, '24: 10 + 10 + 4 ✗   10 + 6 + 8 ✗   6 + 6 + 12 ✗', k='red', size=18, anchor='start'),
            text(x0, y0 + 3 * (h + 6) + 82, 'the first gap is 24 (25, 27, 28, 29 fail too, but later)', k='red', size=18, font='scrawl', anchor='start')]
    return svg(620, y0 + 3 * (h + 6) + 98, rough(*parts) + ''.join(lab),
               'Totals 1 to 30: 1 to 23 are all possible, 24 is the first impossible total, then 25, 27, 28 and 29 are also impossible')


Q.append(dict(
    n=23, orig=46, answer='C', topic='Number & combinations',
    question=f"""<p>On Sports Day at St Jude's College points are awarded in each event as follows:</p>
{table([['1st place', hl('10 points', 'g', 1)], ['2nd place', hl('6 points', 'g', 1)], ['3rd place', hl('3 points', 'g', 1)], ['4th place', hl('1 point', 'g', 1)]])}
<p>Each student may enter a {hl('maximum of three events', 'y', 2)}.</p>
<p class="stem">What is the {hl('lowest', 'b', 3)} score that is {hl('<b>not</b>', 'p', 4)} possible for a student to achieve?</p>""",
    options={'A': '15', 'B': '22', 'C': '24', 'D': '27', 'E': '31'},
    notes=[(1, 'g', 'Each event gives 10, 6, 3, 1, or 0 if they don’t place.'),
           (2, 'y', 'Up to three scores added together. They can win the same place more than once (10 + 10 is fine).'),
           (3, 'b', 'Check the options from the smallest up and stop at the first impossible one.'),
           (4, 'p', 'Looking for what you <b>can’t</b> make.')],
    steps=[
        f"""<p>Test the options in order, smallest first:</p>
{calc(f'15 = 6 + 6 + 3 ' + tick(), f'22 = 10 + 6 + 6 ' + tick(), '24 = ?')}""",
        f"""<p>Try to make 24 from three scores:</p>
{calc(f'two 10s: need 4 more from one event {cross()} (no 4)', f'one 10: need 14 from two events: 10 + 4? 6 + 8? {cross()}',
      f'no 10s: at most 6 + 6 + 6 = 18 {cross()}', f'so 24 is impossible')}""",
        f"""<p>And everything below 24 can be made, so 24 is the lowest:</p>{_strip()}
{calc(f'lowest impossible score = {boxed("24")}')}""",
    ],
    answer_text='24: it needs a 4 or an 8 that no single event gives.',
    why={'A': '15 is possible: 6 + 6 + 3 (three 2nd and 3rd places).',
         'B': '22 is possible: 10 + 6 + 6.',
         'D': '27 is impossible too, but 24 is lower.',
         'E': '31 is impossible (more than the maximum of 30), but 24 is lower.'},
    fast='15 = 6 + 6 + 3, 22 = 10 + 6 + 6. 24: 10 + 10 + 4, 10 + 6 + 8 and 6 + 6 + 12 all fail. Answer 24.',
))


# ---------------------------------------------------------------- 24 (Q48)
def _baskets():
    parts, lab = [], []

    def roll(x, y):
        parts.append(rect(x - 19, y - 11, 38, 22, k='orange', fill='o', sw=2, rx=11))
        parts.append(path(f'M{x - 8} {y - 9} q4 9 0 18 M{x + 4} {y - 10} q4 10 0 20', k='orange', sw=1.4))

    def apple(x, y):
        parts.append(circle(x, y + 2, 14, k='green', fill='g', sw=2))
        parts.append(path(f'M{x} {y - 12} q2 -8 6 -10', k='green', sw=2))

    def choc(x, y):
        parts.append(rect(x - 11, y - 17, 22, 34, k='violet', fill='v', sw=2, rx=2))
        parts.append(line(x - 11, y, x + 11, y, k='violet', w=1.2))
        parts.append(line(x, y - 17, x, y + 17, k='violet', w=1.2))

    draw = {'R': roll, 'A': apple, 'C': choc}
    rows = [('Hector', 'RRRA', '$3.50', 'ink'), ('Lee', 'ACCCC', '$8.00', 'ink'), ('Olga', 'RCC', '$3.50', 'ink'),
            ('Olga × 2', 'RRCCCC', '$7.00', 'pen')]
    for i, (nm, items, cost, col) in enumerate(rows):
        y = 44 + i * 58
        lab.append(text(16, y + 6, nm, k=col, size=18, anchor='start'))
        for j, ch in enumerate(items):
            draw[ch](120 + j * 50, y)
        lab.append(text(440, y + 6, '= ' + cost, k=col, size=20, anchor='start'))
    parts.append(line(10, 44 + 2.5 * 58, 520, 44 + 2.5 * 58, k='muted', w=1.2, dash=True))
    lab += [text(560, 44 + 58 + 6, 'Lee', k='red', size=16, anchor='start'),
            text(560, 44 + 3 * 58 + 6, 'same 4 bars', k='red', size=16, anchor='start'),
            text(300, 44 + 4 * 58 + 6, 'Lee − (Olga × 2): 1 apple − 2 rolls = $1.00', k='red', size=19, font='scrawl')]
    parts.append(arrow(600, 44 + 58 + 14, 600, 44 + 3 * 58 - 14, k='red', bend=0.3))
    return svg(660, 44 + 4 * 58 + 20, rough(*parts) + ''.join(lab),
               'Baskets: Hector 3 rolls and an apple 3.50; Lee an apple and 4 bars 8.00; Olga a roll and 2 bars 3.50, doubled to 2 rolls and 4 bars 7.00')


Q.append(dict(
    n=24, orig=48, answer='C', topic='Equations & prices',
    question=f"""<p>My three friends bought food at the supermarket. When I asked them, they did not remember
the prices of the items, only the final amount they paid.</p>
<ul><li>{hl('Hector paid $3.50 for 3 bread rolls and 1 apple', 'g', 1)}.</li>
<li>{hl('Lee paid $8.00 for 1 apple and 4 chocolate bars', 'g', 1)}.</li>
<li>{hl('Olga paid $3.50 for 1 bread roll and 2 chocolate bars', 'g', 1)}.</li></ul>
<p>I want to buy {hl('1 bread roll, 1 apple and 1 chocolate bar', 'b', 2)}.</p>
<p class="stem">How much do I need to pay?</p>""",
    options={'A': '$3.00', 'B': '$3.50', 'C': '$4.00', 'D': '$4.50', 'E': '$5.00'},
    notes=[(1, 'g', 'Three baskets, three unknown prices. Compare baskets to cancel things out.'),
           (2, 'b', 'One of each: find all three prices, then add.')],
    steps=[
        f"""<p>Double Olga’s basket so it has 4 chocolate bars, like Lee’s:</p>{_baskets()}""",
        f"""<p>Now swap the apple into Hector’s basket:</p>
{calc('apple = 2 rolls + $1.00', 'Hector: 3 rolls + apple = 5 rolls + $1.00 = $3.50', f'5 rolls = $2.50 {ar()} <b>roll = 50c</b>',
      f'apple = 2 × 50c + $1.00 = <b>$2.00</b>', f'Olga: 50c + 2 bars = $3.50 {ar()} 2 bars = $3.00 {ar()} <b>bar = $1.50</b>')}""",
        f"""{calc(f'roll + apple + bar = 0.50 + 2.00 + 1.50 = {boxed("$4.00")}')}
{note('Check every basket: Hector 1.50 + 2 = 3.50 ✓, Lee 2 + 6 = 8 ✓, Olga 0.50 + 3 = 3.50 ✓.', 'check')}""",
    ],
    answer_text='$4.00: roll 50c, apple $2.00, chocolate bar $1.50.',
    why={'A': '$3.00 is too little: the apple alone is $2 and the chocolate bar $1.50.',
         'B': '$3.50 just copies Hector’s (or Olga’s) total, but their baskets are different.',
         'D': '$4.50 would need, say, a $2 chocolate bar, but then Olga’s roll + 2 bars would cost more than $4, not $3.50.',
         'E': '$5.00 is the three bills added ($15) and divided by 3 people. The baskets hold different things, so that doesn’t work.'},
    fast='Lee − 2 × Olga: apple − 2 rolls = $1. Hector: 5 rolls + $1 = $3.50, so roll 50c, apple $2, bar $1.50. Total $4.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _ring():
    L, T, R, B, rad = 70, 60, 550, 280, 50
    parts, lab = [], []
    parts.append(rect(L, T, R - L, B - T, k='ink', sw=3.2, rx=rad))
    towns = [('Portville', 250, T, 250, T - 14, 'middle'), ('Queensgate', 535, 75, 560, 62, 'start'),
             ('Radcliffe', 450, B, 450, B + 26, 'middle'), ('Southtown', 220, B, 220, B + 26, 'middle'),
             ('Tunborough', L, 170, L + 16, 176, 'start')]
    for nm, x, y, tx, ty, anc in towns:
        parts.append(circle(x, y, 8, k='ink', fill='ink', sw=1))
        lab.append(text(tx, ty, nm, k='ink', size=17, anchor=anc))
    gaps = [('19', 395, T - 14, 'middle'), ('22', R + 12, 175, 'start'), ('17', 335, B + 26, 'middle'),
            ('15', 130, B + 26, 'middle'), ('24', L - 12, 100, 'end')]
    for g, x, y, anc in gaps:
        lab.append(text(x, y, g + ' km', k='green', size=19, anchor=anc, weight=700))
    for nm, x, y in (('s1', 395, T), ('s2', R, 140), ('s3', 285, B), ('s4', 85, 265), ('s5', 85, 75)):
        parts.append(line(x - 7, y - 7, x + 7, y + 7, k='red' if nm == 's4' else 'muted', w=2.4))
        parts.append(line(x - 7, y + 7, x + 7, y - 7, k='red' if nm == 's4' else 'muted', w=2.4))
    lab += [text(395, T + 26, 'sign 1', k='muted', size=14), text(R - 12, 145, 'sign 2', k='muted', size=14, anchor='end'),
            text(285, B - 14, 'sign 3', k='muted', size=14), text(104, 258, 'sign 4', k='red', size=15, anchor='start'),
            text(104, 90, 'sign 5', k='muted', size=14, anchor='start')]
    parts.append(arrow(260, 120, 360, 120, k='pen', bend=-0.25))
    lab += [text(310, 92, 'clockwise', k='pen', size=16),
            text(310, 160, 'round the whole ring = 97 km', k='ink', size=17),
            text(310, 196, 'sign 4 says Portville 31,', k='red', size=18, font='scrawl'),
            text(310, 222, 'but 9 + 24 = 33 ✗', k='red', size=18, font='scrawl')]
    return svg(660, B + 46, rough(*parts) + ''.join(lab),
               'The ring road with the true distances between towns: Portville to Queensgate 19, to Radcliffe 22, to Southtown 17, to Tunborough 15, back to Portville 24 km; sign 4 gives Portville as 31 instead of 33')


Q.append(dict(
    n=25, orig=50, answer='D', topic='Distances & tables',
    question=f"""<p>There are five towns at various positions along a major ring road that encircles a city. {hl('Traffic travelling clockwise', 'y', 1)} around the ring road is provided with information in the form of five
‘distance’ signs at various points along the road as shown.</p>
{fig(Y, 'ps_q25_map', 'Ring road map: clockwise from the top, Portville, sign 1, Queensgate, sign 2, Radcliffe, sign 3, Southtown, sign 4, Tunborough, sign 5', 460)}
<p>The signs display the following information (all distances in km):</p>
{table([['Queensgate 10', 'Radcliffe 17', 'Southtown 4', 'Tunborough 9', 'Portville 13'],
        ['Radcliffe 32', 'Southtown 34', 'Tunborough 19', 'Portville 31', 'Queensgate 32'],
        ['Southtown 49', 'Tunborough 49', 'Portville 43', 'Queensgate 52', 'Radcliffe 54'],
        ['Tunborough 64', 'Portville 73', 'Queensgate 62', 'Radcliffe 74', 'Southtown 71'],
        ['Portville 88', 'Queensgate 92', 'Radcliffe 84', 'Southtown 91', 'Tunborough 86']],
       head=['sign 1', 'sign 2', 'sign 3', 'sign 4', 'sign 5'])}
<p>{hl('One of the signs contains an error in one of the distances indicated', 'p', 2)}.</p>
<p class="stem">{hl('Which one of the signs', 'b', 3)} contains the error?</p>""",
    options={'A': 'sign 1', 'B': 'sign 2', 'C': 'sign 3', 'D': 'sign 4', 'E': 'sign 5'},
    notes=[(1, 'y', 'Every sign lists the towns in the same clockwise order, each further on than the last.'),
           (2, 'p', 'Just one wrong number. The gaps between neighbouring towns must agree on every sign.'),
           (3, 'b', 'Find the sign whose gaps don’t match the others.')],
    steps=[
        f"""<p>The distance from one town to the next is the same whichever sign you read it from. So subtract neighbouring numbers on each sign:</p>
{calc('sign 1: Q→R 22, R→S 17, S→T 15, T→P 24', 'sign 2: R→S 17, S→T 15, T→P 24, P→Q 19',
      'sign 3: S→T 15, T→P 24, P→Q 19, Q→R 22', 'sign 4: T→P <b>22</b>, P→Q <b>21</b>, Q→R 22, R→S 17 ' + cross(),
      'sign 5: P→Q 19, Q→R 22, R→S 17, S→T 15')}""",
        f"""<p>Every sign agrees except sign 4. Draw the ring with the agreed gaps:</p>{_ring()}
{calc('sign 4: Tunborough 9, so Portville should be 9 + 24 = 33 (not 31)', 'then Queensgate 33 + 19 = 52 ' + tick() + ' (matches the sign)',
      f'the faulty sign {ar()} {boxed("sign 4")}')}
{note('Fixing one number (31 → 33) mends both bad gaps on sign 4 at once, which confirms it is a single error.', 'check')}""",
    ],
    answer_text='Sign 4: Portville should be 33 km, not 31 km.',
    why={'A': 'Sign 1 gives gaps 22, 17, 15, 24, all matching the other signs.',
         'B': 'Sign 2 gives gaps 17, 15, 24, 19, all matching.',
         'C': 'Sign 3 gives gaps 15, 24, 19, 22, all matching.',
         'E': 'Sign 5 gives gaps 19, 22, 17, 15, all matching.'},
    fast='Subtract neighbours on each sign. Tunborough → Portville is 24 everywhere except sign 4 (31 − 9 = 22). Sign 4.',
))
