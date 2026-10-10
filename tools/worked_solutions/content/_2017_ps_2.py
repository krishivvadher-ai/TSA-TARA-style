from wslib import *

Y = 2017
Q = []


# ---------------------------------------------------------------- 9 (Q19)
_PTS = [
    [1498, 1484, 1470, 1456, 1442, 1428, 1414, 1400, 1386, 1373, 1359, 1345, 1332, 1318, 1305,
     1291, 1278, 1264, 1251, 1237, 1224, 1211, 1198, 1184, 1171, 1158, 1145, 1132, 1119, 1106],
    [1093, 1080, 1067, 1054, 1041, 1029, 1016, 1003, 991, 978, 966, 953, 941, 928, 916,
     903, 891, 879, 867, 855, 842, 830, 818, 806, 795, 783, 771, 759, 747, 736],
    [724, 712, 701, 689, 678, 666, 655, 644, 632, 621, 610, 599, 588, 577, 566,
     555, 544, 534, 523, 512, 502, 491, 481, 470, 460, 449, 439, 429, 419, 409],
    [399, 389, 379, 369, 359, 350, 340, 331, 321, 312, 302, 293, 284, 275, 266,
     257, 248, 239, 231, 222, 214, 205, 197, 188, 180, 172, 164, 156, 149, 141],
]


def _jump_table():
    rows = []
    for i in range(30):
        row = []
        for col in range(4):
            h = 219 - 30 * col - i
            row += [f'{h // 100}.{h % 100:02d}', str(_PTS[col][i])]
        rows.append(row)
    return table(rows, head=['<i>performance</i>', '<i>points</i>'] * 4)


def _highjump():
    Yh = lambda h: 210 - (h - 1.56) * 610
    parts, lab = [], []
    parts += [line(150, 60, 150, 306, k='ink', w=3), line(390, 60, 390, 306, k='ink', w=3),
              line(110, 306, 430, 306, k='muted', w=2)]
    for h, k, t, pts in ((1.56, 'muted', 'old best 1.56 m', '689 points'), (1.74, 'red', 'new best 1.74 m', '903 points')):
        parts.append(line(150, Yh(h), 390, Yh(h), k=k, w=4 if k == 'red' else 3, dash=k == 'muted'))
        lab.append(text(400, Yh(h) - 4, t, k=k if k == 'red' else 'ink', size=18, anchor='start'))
        lab.append(text(400, Yh(h) + 18, pts, k=k if k == 'red' else 'ink', size=18, anchor='start'))
    parts.append(line(120, Yh(1.56), 120, Yh(1.74) + 4, k='pen', w=2.4, head=True))
    lab.append(text(110, (Yh(1.56) + Yh(1.74)) / 2 + 6, '+18 cm', k='pen', size=20, anchor='end', font='scrawl'))
    parts.append(line(560, Yh(1.56) + 8, 560, Yh(1.74) + 12, k='green', w=2.4, head=True))
    lab.append(text(570, (Yh(1.56) + Yh(1.74)) / 2 + 14, '+214', k='green', size=22, anchor='start', font='scrawl'))
    lab.append(text(570, (Yh(1.56) + Yh(1.74)) / 2 + 36, 'points', k='green', size=16, anchor='start'))
    lab.append(stick_person(270, 306, k='pen', s=1.6))
    lab.append(text(270, 330, 'not to scale', k='muted', size=13))
    return svg(640, 340, rough(*parts) + ''.join(lab),
               'High jump bar raised from 1.56 m (689 points) to 1.74 m (903 points): 18 cm higher and 214 points more')


Q.append(dict(
    n=9, orig=19, answer='C', topic='Reading tables',
    question=f"""<p>The heptathlon is a seven-event athletics competition. In each event the time or distance
recorded is converted into a points score. This is the scoring table that is used for the high
jump:</p>
{_jump_table()}
<p>Daphne is competing in a heptathlon competition and has just {hl('beaten her previous best high jump performance by 18 cm', 'g', 1)}. This has {hl('increased her best points score in the high jump by 214', 'p', 2)}.</p>
<p class="stem">What is Daphne’s {hl('<b>new</b>', 'b', 3)} personal-best high jump performance?</p>""",
    options={'A': '1.09 metres', 'B': '1.44 metres', 'C': '1.74 metres', 'D': '1.89 metres', 'E': '2.09 metres'},
    notes=[(1, 'g', 'Old height = new height − 0.18 m. Performances are in metres, so 18 cm = 0.18.'),
           (2, 'p', '214 is the <b>increase</b> in points, not her points. (1.09 m scores exactly 214: a trap!)'),
           (3, 'b', 'The higher of the two heights.')],
    steps=[
        f"""<p>Work backwards from the options. For each one: old = new − 0.18, look up both scores, subtract.</p>
{calc(f'A 1.09 → 214, old 0.91 isn’t even in the table {cross()}',
      f'B 1.44 → 555, 1.26 → 369: 555 − 369 = 186 {cross()}',
      f'C 1.74 → 903, 1.56 → 689: 903 − 689 = <b>214</b> {tick()}',
      f'D 1.89 → 1093, 1.71 → 867: 226 {cross()}',
      f'E 2.09 → 1359, 1.91 → 1119: 240 {cross()}')}""",
        f"""{_highjump()}
{calc(f'new personal best = {boxed("1.74 metres")}')}
{note('Shortcut: 214 points ÷ 18 cm ≈ 12 points per cm. Points per cm grow as the bar rises (about 8 per cm near 1.00 m, about 14 per cm near 2.00 m). 12 per cm happens in the 1.60–1.89 column, so C is the one to check first.', 'tip')}""",
    ],
    answer_text='1.74 m: up from 1.56 m, and 903 − 689 = 214 points.',
    why={'A': '1.09 m <b>scores</b> 214 points, but 214 is the increase. Also 1.09 − 0.18 = 0.91 m is below the table.',
         'B': '1.26 m → 1.44 m only adds 186 points.',
         'D': '1.71 m → 1.89 m adds 226 points, too many.',
         'E': '1.91 m → 2.09 m adds 240 points, far too many.'},
    fast='214 ÷ 18 ≈ 12 points per cm, which fits the middle of the table. Check 1.74: 903 − 689 (1.56) = 214. Done.',
))


# ---------------------------------------------------------------- 10 (Q20)
_REG = [('Jan', 124.1, 161.2), ('Feb', 61.4, 71.5), ('Mar', 367.9, 445.3), ('Apr', 138.0, 167.9), ('May', 159.0, 184.8),
        ('Jun', 185.5, 220.6), ('Jul', 141.7, 175.3), ('Aug', 57.5, 76.2), ('Sep', 359.0, 419.1), ('Oct', 149.7, 168.0),
        ('Nov', 150.3, 160.5), ('Dec', 123.1, 139.8)]


def _diff_bars():
    parts, lab = [], []
    base, s = 250, 2.5
    parts.append(line(40, base, 620, base, k='ink', w=1.6))
    for i, (m, a, b) in enumerate(_REG):
        d = b - a
        x = 52 + i * 47
        big = m in ('Mar', 'Sep')
        small = m in ('Feb', 'Nov')
        f = 'p' if big else ('y' if small else 'b')
        parts.append(rect(x, base - d * s, 30, d * s, k='ink', fill=f, sw=1.5))
        lab.append(text(x + 15, base - d * s - 7, f'{d:.0f}', k='red' if (big or small) else 'ink', size=15))
        lab.append(text(x + 15, base + 20, m, k='ink', size=15))
    lab += [text(330, 24, 'my sketch: 2007 minus 2012 (thousands)', k='muted', size=16),
            text(330, 290, 'Mar tallest, Sep second; Feb and Nov the two shortest, about equal', k='red', size=18, font='scrawl')]
    return svg(640, 304, rough(*parts) + ''.join(lab),
               'Bar chart of monthly differences: Jan 37, Feb 10, Mar 77, Apr 30, May 26, Jun 35, Jul 34, Aug 19, Sep 60, Oct 18, Nov 10, Dec 17')


Q.append(dict(
    n=10, orig=20, answer='D', topic='Charts & data',
    question=f"""<p>After the financial crash there were fewer new car registrations in the UK in 2012 than there
were in 2007. The monthly figures for new car registrations for both years are given in the table
below.</p>
{table([[m + ' 2012', f'{a:.1f}', m + ' 2007', f'{b:.1f}'] for m, a, b in _REG])}
<p class="stem">Which one of the following charts {hl('best represents', 'y', 1)} the {hl('<b>monthly differences</b>', 'b', 2)} between new car
registrations for these two years?</p>
{fig(Y, 'ps_q10_charts', 'Five bar charts A to E, each with twelve monthly bars and no numbers on the axis', 560)}""",
    options={'A': 'chart A', 'B': 'chart B', 'C': 'chart C', 'D': 'chart D', 'E': 'chart E'},
    notes=[(1, 'y', 'No numbers on the charts, so match the <b>shape</b>: which bars are tallest, which are shortest, which are equal.'),
           (2, 'b', 'For each month: 2007 figure − 2012 figure. Not either year’s totals.')],
    steps=[
        f"""<p>Work out each month’s difference (2007 − 2012). Rounding to whole numbers is plenty:</p>
{calc('Jan 37, Feb 10, <b>Mar 77</b>, Apr 30, May 26, Jun 35',
      'Jul 34, Aug 19, <b>Sep 60</b>, Oct 18, <b>Nov 10</b>, Dec 17')}
{_diff_bars()}""",
        f"""<p>Now test the charts on the stand-out features:</p>
<ul><li>March must be the tallest bar, clearly taller than September. {ar()} A and E have September taller; C has them equal. {cross()}</li>
<li>February and November must be the two shortest and about the same. {ar()} B’s November is more than twice its February. {cross()}</li>
<li>D: March tallest, September next, February and November tiny and level. {tick()}</li></ul>
{calc(f'the chart of differences is {boxed("D")}')}
{note('With picture options, pick two or three features you are sure of (the biggest, the smallest, any equal pairs) and knock charts out. You rarely need every bar.', 'tip')}""",
    ],
    answer_text='Chart D matches the differences: March biggest, then September, with February and November the smallest.',
    why={'A': 'A makes September’s bar taller than March’s, but March fell by 77 and September by only 60. Its August bar is also far too tall.',
         'B': 'B makes November more than twice as tall as February, but both differences are about 10. January is also too short.',
         'C': 'C has the shape of the 2012 figures themselves (March and September both off the top), not the differences.',
         'E': 'E makes September taller than March, and its November bar is as tall as October’s instead of being one of the smallest.'},
    fast='Mar (77) > Sep (60) knocks out A, C and E. Feb ≈ Nov ≈ 10 knocks out B. D.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _mixbars():
    s = 64
    x0 = 120
    parts, lab = [], []
    # before
    parts += [rect(x0, 40, 1.5 * s, 44, k='ink', fill='o', sw=1.8), rect(x0 + 1.5 * s, 40, 4.5 * s, 44, k='ink', fill='b', sw=1.8)]
    lab += [text(x0 - 12, 68, 'before', k='ink', size=18, anchor='end'),
            text(x0 + 0.75 * s, 68, 'X 1.5', k='ink', size=17), text(x0 + 3.75 * s, 68, 'Y 4.5', k='ink', size=17),
            text(x0 + 6 * s + 10, 68, '6 kg', k='ink', size=18, anchor='start')]
    # after
    parts += [rect(x0, 130, 1.5 * s, 44, k='ink', fill='o', sw=1.8), rect(x0 + 1.5 * s, 130, 1.5 * s, 44, k='red', fill='y', sw=2.4),
              rect(x0 + 3 * s, 130, 4.5 * s, 44, k='ink', fill='b', sw=1.8)]
    lab += [text(x0 - 12, 158, 'after', k='ink', size=18, anchor='end'),
            text(x0 + 0.75 * s, 158, 'X 1.5', k='ink', size=17), text(x0 + 2.25 * s, 158, '+ 1.5', k='red', size=20, font='scrawl'),
            text(x0 + 5.25 * s, 158, 'Y 4.5 (same!)', k='ink', size=17),
            text(x0 + 7.5 * s + 10, 158, '7.5 kg', k='ink', size=18, anchor='start')]
    parts.append(brace(x0, x0 + 3 * s, 180, 'X = 3.0 kg = 40%', k='orange'))
    parts.append(brace(x0 + 3 * s, x0 + 7.5 * s, 180, 'Y = 4.5 kg = 60%', k='pen'))
    return svg(660, 230, rough(*parts) + ''.join(lab),
               'Bar model: before 1.5 kg X and 4.5 kg Y; after adding 1.5 kg X there is 3 kg X (40%) and 4.5 kg Y (60%) in 7.5 kg')


Q.append(dict(
    n=11, orig=24, answer='B', topic='Percentages & mixtures',
    question=f"""<p>A laboratory technician has made up a stock mixture of two chemicals, X and Y, ready for use
by all of the groups in Year 9 at a High School. He has mixed {hl(f'6.0 kg which is {frac(1, 4)} of X and {frac(3, 4)} of Y', 'g', 1)}. He realises that he has used the wrong mix and, rather than waste the chemicals he has
used so far, he is going to {hl('add some more of chemical X', 'y', 2)} so that the mix consists of {hl('40% of X and 60% of Y', 'g', 3)}.</p>
<p class="stem">What mass of chemical X must he {hl('<b>add</b>', 'b', 4)}?</p>""",
    options={'A': '1.0 kg', 'B': '1.5 kg', 'C': '2.0 kg', 'D': '2.5 kg', 'E': '3.0 kg'},
    notes=[(1, 'g', 'X is a quarter of 6 kg = 1.5 kg. Y is three quarters = 4.5 kg.'),
           (2, 'y', 'Only X is added, so the <b>Y stays at 4.5 kg</b>. That’s the key.'),
           (3, 'g', 'The new mix: Y must be 60% of the new total.'),
           (4, 'b', 'The extra X, not the final amount of X.')],
    steps=[
        f"""{calc(f'X = {frac(1, 4)} × 6 = 1.5 kg', f'Y = {frac(3, 4)} × 6 = 4.5 kg')}""",
        f"""<p>Y doesn’t change, so use it to find the new total:</p>
{calc(f'60% of new total = 4.5 kg', f'10% = 4.5 ÷ 6 = 0.75 kg', f'100% = 7.5 kg')}""",
        f"""{_mixbars()}
{calc(f'added X = 7.5 − 6.0 = {boxed("1.5 kg")}', 'check: X = 1.5 + 1.5 = 3.0 kg, and 3.0 ÷ 7.5 = 40% ✓')}
{note('Use the thing that stays the same (Y) to find the new total. Adding X changes X’s amount and the total, so X itself is awkward to work with.', 'tip')}""",
    ],
    answer_text='1.5 kg of X: the mix becomes 3 kg X and 4.5 kg Y (40% and 60% of 7.5 kg).',
    why={'A': 'Adding 1.0 kg gives 2.5 kg X in 7 kg, about 36%, not 40%.',
         'C': 'Adding 2.0 kg gives 3.5 kg X in 8 kg, about 44%.',
         'D': 'Adding 2.5 kg gives 4 kg X in 8.5 kg, about 47%.',
         'E': '3.0 kg is how much X the <b>final</b> mix holds, not how much is added. Adding 3 kg would make X 50%.'},
    fast='Y fixed at 4.5 kg = 60%, so total = 7.5 kg. Add 7.5 − 6 = 1.5 kg.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _podium():
    parts, lab = [], []
    blocks = [(240, 'Portugal', 6, 'b', 110), (360, 'Tenerife', 7, 'g', 150), (480, 'Majorca', 4, 'o', 70), (600, 'Greece', 4, 'o', 70)]
    base = 250
    for x, name, pts, f, h in blocks:
        parts.append(rect(x - 55, base - h, 110, h, k='ink', fill=f, sw=2))
        lab.append(text(x, base - h - 10, name, k='ink', size=19))
        lab.append(text(x, base - h / 2 + 10, f'{pts}', k='ink', size=30, font='scrawl'))
    parts.append(line(160, base, 670, base, k='ink', w=2))
    # France crossed out
    parts += [rect(20, 130, 110, 120, k='muted', fill='paper', sw=1.6), line(14, 124, 136, 256, k='red', w=2.2),
              line(136, 124, 14, 256, k='red', w=2.2)]
    lab += [text(75, 118, 'France', k='ink', size=19), text(75, 160, '9 points', k='ink', size=16),
            text(75, 76, 'nobody’s', k='red', size=16), text(75, 96, '1st choice!', k='red', size=16),
            text(360, 46, 'winner!', k='green', size=22, font='scrawl')]
    return svg(680, 270, rough(*parts) + ''.join(lab),
               'Podium of points: Tenerife 7, Portugal 6, Majorca 4, Greece 4; France scored 9 but is crossed out because it was nobody’s first choice')


Q.append(dict(
    n=12, orig=25, answer='E', topic='Scoring & rules',
    question=f"""<p>Five friends wanted to go on holiday together, but they found it difficult to decide where to go.
Jo and Mel both wanted to go to Portugal, with France as their second choice. Kim wanted to
go to Majorca, while Lexy’s first choice was Greece and Naz’s was Tenerife. Naz and Kim both
put France as their second choice, while Lexy gave it as her third choice, preferring Tenerife as
her second choice. Kim and Mel put Tenerife as their third choice. Jo’s third choice was
Greece, and Naz’s was Majorca.</p>
<p>They agreed to allocate {hl('three points for a 1<sup>st</sup> choice, two points for a 2<sup>nd</sup> choice and one point for a 3<sup>rd</sup> choice', 'y', 1)}. The friends decided that they {hl('would not go anywhere which was not someone’s first choice', 'p', 2)}.</p>
<p class="stem">{hl('<b>Where did they go</b>', 'b', 3)} on holiday?</p>""",
    options={'A': 'France', 'B': 'Greece', 'C': 'Majorca', 'D': 'Portugal', 'E': 'Tenerife'},
    notes=[(1, 'y', '3, 2, 1 points. Put the choices in a grid first, then add up.'),
           (2, 'p', 'A place nobody put first is banned, however many points it gets.'),
           (3, 'b', 'Most points among the places that are allowed.')],
    steps=[
        f"""<p>Long sentences, so make a grid of everyone’s choices before adding anything:</p>
{table([['Jo', 'Portugal', 'France', 'Greece'], ['Mel', 'Portugal', 'France', 'Tenerife'],
        ['Kim', 'Majorca', 'France', 'Tenerife'], ['Lexy', 'Greece', 'Tenerife', 'France'],
        ['Naz', 'Tenerife', 'France', 'Majorca']],
       head=['', '1st (3 points)', '2nd (2 points)', '3rd (1 point)'])}""",
        f"""<p>Add up each place:</p>
{calc('France: 2 + 2 + 2 + 1 + 2 = 9, but nobody chose it first ' + cross(),
      'Tenerife: 3 (Naz) + 2 (Lexy) + 1 (Mel) + 1 (Kim) = <b>7</b>',
      'Portugal: 3 (Jo) + 3 (Mel) = 6',
      'Majorca: 3 (Kim) + 1 (Naz) = 4', 'Greece: 3 (Lexy) + 1 (Jo) = 4')}
{_podium()}
{calc(f'highest allowed score {ar()} {boxed("Tenerife")}')}""",
    ],
    answer_text='Tenerife, with 7 points (France scores 9 but is ruled out).',
    why={'A': 'France scores the most (9) but it is nobody’s first choice, so the rule bans it.',
         'B': 'Greece only gets 4 points.',
         'C': 'Majorca only gets 4 points.',
         'D': 'Portugal has two first choices (6 points), but Tenerife collects points from four friends and gets 7.'},
    fast='Grid it. France is banned. Tenerife 3 + 2 + 1 + 1 = 7 beats Portugal 6.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _cube_net():
    c = 74
    x0, y0 = 30, 58
    squares = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)]
    diags = [((1, 0), (2, 1)), ((0, 2), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (3, 1)), ((3, 2), (4, 1)), ((1, 2), (2, 3))]
    names = {(1, 0): 'T', (2, 0): 'U', (0, 1): 'T', (1, 1): 'P', (2, 1): 'Q', (3, 1): 'U', (4, 1): 'T',
             (0, 2): 'W', (1, 2): 'S', (2, 2): 'R', (3, 2): 'V', (4, 2): 'W', (1, 3): 'W', (2, 3): 'V'}
    two = {'P', 'R', 'T', 'V'}
    P = lambda gx, gy: (x0 + gx * c, y0 + gy * c)
    parts = [rect(*P(*sq), c, c, k='ink', fill='paper', sw=2) for sq in squares]
    parts += [line(*P(*a), *P(*b), k='pen', w=3) for a, b in diags]
    lab = []
    for (gx, gy), nm in names.items():
        x, y = P(gx, gy)
        lab.append(circle(x, y, 12, k='green' if nm in two else 'muted', fill='g' if nm in two else 'paper', sw=2))
        lab.append(text(x, y + 6, nm, k='ink', size=16, weight='700'))
    face = {(1, 0): ('top', 0.3), (0, 1): ('left', 0.7), (1, 1): ('front', 0.3), (2, 1): ('right', 0.7),
            (3, 1): ('back', 0.7), (1, 2): ('bottom', 0.32)}
    for (gx, gy), (t, fx) in face.items():
        x, y = P(gx, gy)
        lab.append(text(x + c * fx, y + c * 0.8, t, k='muted', size=13))
    return x0, y0, c, parts, lab


def _cube_pics():
    x0, y0, c, parts, lab = _cube_net()
    # the folded cube (front face P Q R S, back face T U V W shifted up and right)
    fx, fy, s, dx, dy = 446, 112, 126, 50, -40
    Pp, Qp, Rp, Sp = (fx, fy), (fx + s, fy), (fx + s, fy + s), (fx, fy + s)
    Tp, Up, Vp, Wp = (fx + dx, fy + dy), (fx + s + dx, fy + dy), (fx + s + dx, fy + s + dy), (fx + dx, fy + s + dy)
    seg = lambda a, b, **kw: line(a[0], a[1], b[0], b[1], **kw)
    parts += [seg(Pp, Qp, k='ink'), seg(Qp, Rp, k='ink'), seg(Rp, Sp, k='ink'), seg(Sp, Pp, k='ink'),
              seg(Pp, Tp, k='ink'), seg(Qp, Up, k='ink'), seg(Rp, Vp, k='ink'), seg(Tp, Up, k='ink'), seg(Up, Vp, k='ink'),
              seg(Wp, Tp, k='muted', dash=True), seg(Wp, Vp, k='muted', dash=True), seg(Wp, Sp, k='muted', dash=True)]
    parts += [seg(Pp, Rp, k='pen', w=3), seg(Tp, Qp, k='pen', w=3), seg(Rp, Up, k='pen', w=3),
              seg(Vp, Tp, k='pen', w=2.2, dash=True), seg(Wp, Pp, k='pen', w=2.2, dash=True), seg(Sp, Vp, k='pen', w=2.2, dash=True)]
    for nm, pt, ox, oy in (('P', Pp, -16, -8), ('Q', Qp, 2, -14), ('R', Rp, 16, 16), ('S', Sp, -16, 16),
                           ('T', Tp, -16, -10), ('U', Up, 16, -10), ('V', Vp, 18, 6), ('W', Wp, -18, -2)):
        if nm in 'PRTV':
            lab.append(circle(pt[0], pt[1], 9, k='green', fill='none', sw=2.6))
        lab.append(text(pt[0] + ox, pt[1] + oy + 5, nm, k='green' if nm in 'PRTV' else 'ink', size=17, weight='700'))
    lab += [text(x0 + 2 * c, 24, 'net with the cube’s corners labelled', k='ink', size=16),
            text(fx + 90, 30, 'folded (dashed = hidden)', k='ink', size=16),
            text(fx + 90, fy + s + 48, 'green = exactly 2 diagonals', k='green', size=17)]
    return svg(660, 320, rough(*parts) + ''.join(lab),
               'The net with every corner labelled by the cube corner it becomes (P to W), and the folded cube with the six diagonals; P, R, T and V each touch two diagonals')


Q.append(dict(
    n=13, orig=26, answer='C', topic='Nets & cubes',
    question=f"""<p>The following net is folded up to make a cube.</p>
{fig(Y, 'ps_q13_net', 'A cross-shaped cube net of six squares, each with one diagonal line', 260)}
<p class="stem">At how many {hl('corners of the cube', 'y', 1)} do {hl('<b>exactly two</b>', 'b', 2)} of the diagonal lines on the faces meet?</p>""",
    options={'A': '2', 'B': '3', 'C': '4', 'D': '5', 'E': '6'},
    notes=[(1, 'y', 'A cube has 8 corners. When you fold, several corners of the net join up into one cube corner.'),
           (2, 'b', 'Not 1, not 3: exactly 2 diagonal ends at that corner.')],
    steps=[
        f"""<p>Make the middle square the <b>front</b>. Call its corners P (top left), Q (top right), R (bottom right), S (bottom left).
The corners behind them are T (behind P), U (behind Q), V (behind R), W (behind S). Now label every corner of the net
with the cube corner it becomes when folded:</p>{_cube_pics()}""",
        f"""<p>List the two ends of each face’s diagonal:</p>
{calc('front: P–R', 'top: T–Q', 'left: W–P', 'right: R–U', 'back: V–T', 'bottom: S–V')}""",
        f"""<p>Tally how many diagonal ends land on each corner:</p>
{calc('P 2, R 2, T 2, V 2', 'Q 1, S 1, U 1, W 1', f'corners with exactly two = {boxed("4")}')}
{note('6 diagonals have 12 ends in total. 4 × 2 + 4 × 1 = 12 ✓.', 'check')}
{note('Folding tip: the back face is the far right square. Its right-hand edge wraps round to meet the left face, so the far-right corners are T (top) and W (bottom), the same as the far-left ones.', 'tip')}""",
    ],
    answer_text='4 corners (P, R, T and V) have exactly two diagonals meeting.',
    why={'A': '2 is too few: P, R, T and V all have two.',
         'B': '3 misses one of the four, often T or V, which only meet on the back face after the net wraps round.',
         'D': '5 would need another corner with two ends, but Q, S, U and W each have only one.',
         'E': '6 is too many: the 12 diagonal ends are shared as 2, 2, 2, 2, 1, 1, 1, 1.'},
    fast='Label the 8 cube corners on the net, write the two ends of each diagonal, tally: P, R, T, V get 2 each. Answer 4.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _bundles():
    parts, lab = [], []

    def bundle(x, y, kinds, colour):
        out = []
        for i, kd in enumerate(kinds):
            out.append(rect(x + i * 40, y, 36, 36, k='ink', fill='y' if kd == 'M' else colour, sw=1.6, rx=5))
            lab.append(text(x + i * 40 + 18, y + 25, '5' if kd == 'M' else '3', k='ink', size=18, font='scrawl'))
        return out

    lab.append(text(20, 40, 'Blues', k='pen', size=21, anchor='start', font='scrawl'))
    lab.append(text(20, 64, 'majors = 2 × minors', k='ink', size=15, anchor='start'))
    for i in range(4):
        parts += bundle(170 + i * 128, 30, 'MMm', 'b')
        lab.append(text(170 + i * 128 + 58, 86, '13', k='muted', size=14))
    lab.append(text(330, 112, '4 bundles of 13 = 52 → 8 majors, 4 minors', k='pen', size=18))
    lab.append(text(20, 160, 'Reds', k='red', size=21, anchor='start', font='scrawl'))
    lab.append(text(20, 184, 'minors = 2 × majors', k='ink', size=15, anchor='start'))
    for i in range(7):
        row, col = divmod(i, 4)
        parts += bundle(170 + col * 128, 148 + row * 58, 'Mmm', 'p')
    lab.append(text(330, 278, '7 bundles of 11 = 77 → 7 majors, 14 minors', k='red', size=18))
    lab.append(text(566, 230, 'yellow = major (5)', k='muted', size=14, anchor='start'))
    return svg(680, 296, rough(*parts) + ''.join(lab),
               'Blues scored in bundles of 2 majors and 1 minor (13 points), 4 bundles make 52; Reds in bundles of 1 major and 2 minors (11 points), 7 bundles make 77')


Q.append(dict(
    n=14, orig=30, answer='C', topic='Ratio & scoring',
    question=f"""<p>There are two ways of scoring points in a ball game: a {hl('‘major’ scores 5 points and a ‘minor’ scores 3 points', 'g', 1)}.</p>
<p>In a match played yesterday, the Reds beat the Blues {hl('77–52', 'g', 2)} despite the fact that the {hl('Blues scored exactly twice as many majors as minors', 'y', 3)}, whilst the {hl('Reds scored exactly half as many majors as minors', 'p', 4)}.</p>
<p class="stem">How many majors were scored {hl('<b>altogether</b>', 'b', 5)} in yesterday’s match?</p>""",
    options={'A': '9', 'B': '12', 'C': '15', 'D': '18', 'E': '21'},
    notes=[(1, 'g', 'Major = 5, minor = 3.'),
           (2, 'g', 'Reds 77, Blues 52.'),
           (3, 'y', 'Blues come in bundles of <b>2 majors + 1 minor</b>.'),
           (4, 'p', 'Careful with the wording: half as many majors means twice as many <b>minors</b>. Bundles of 1 major + 2 minors.'),
           (5, 'b', 'Add both teams’ majors.')],
    steps=[
        f"""<p>Think in bundles that keep each team’s ratio:</p>
{calc('Blues bundle: 2 majors + 1 minor = 10 + 3 = 13 points', f'52 ÷ 13 = 4 bundles {ar()} 8 majors, 4 minors')}
{calc('Reds bundle: 1 major + 2 minors = 5 + 6 = 11 points', f'77 ÷ 11 = 7 bundles {ar()} 7 majors, 14 minors')}""",
        f"""{_bundles()}
{calc(f'majors altogether = 8 + 7 = {boxed("15")}')}
{note('Blues 8 × 5 + 4 × 3 = 40 + 12 = 52 ✓. Reds 7 × 5 + 14 × 3 = 35 + 42 = 77 ✓.', 'check')}""",
    ],
    answer_text='15 majors: 8 by the Blues and 7 by the Reds.',
    why={'A': '9 is too few: the Blues alone scored 8 majors and the Reds 7.',
         'B': '12 is the Blues’ total number of scores (8 majors + 4 minors), not the majors in the match.',
         'D': '18 is the number of <b>minors</b> (4 + 14): majors and minors mixed up.',
         'E': '21 is the Reds’ total number of scores (7 majors + 14 minors).'},
    fast='Blues: 13-point bundles, 52 ÷ 13 = 4, so 8 majors. Reds: 11-point bundles, 77 ÷ 11 = 7, so 7 majors. 15.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _oatcakes():
    parts, lab = [], []
    parts.append(rect(30, 40, 600, 150, k='orange', fill='o', sw=2.4, rx=14))
    for i in range(24):
        r, cidx = divmod(i, 12)
        cx, cy = 70 + cidx * 47, 88 + r * 56
        parts.append(circle(cx, cy, 20, k='ink', fill='y', sw=1.8))
        lab.append(text(cx, cy + 5, i + 1, k='ink', size=13, font='print'))
    lab += [text(330, 30, '300 g packet', k='orange', size=18),
            text(330, 220, 'energy: 3 × 427 = 1281 kcal ÷ 53 ≈ 24.2', k='pen', size=18),
            text(330, 246, 'fat: 3 × 17.6 = 52.8 g ÷ 2.2 = 24 exactly', k='pen', size=18),
            text(330, 274, '24 oatcakes of 12.5 g each', k='red', size=22, font='scrawl')]
    return svg(660, 290, rough(*parts) + ''.join(lab),
               'A packet holding 24 oatcakes; energy gives 1281 divided by 53, about 24, and fat gives 52.8 divided by 2.2, exactly 24')


Q.append(dict(
    n=15, orig=31, answer='D', topic='Proportion & rounding',
    question=f"""<p>The following ingredient and nutrition information ({hl('rounded to the nearest 0.1 g or 1 kcal', 'p', 1)})
appears on a {hl('300 g packet', 'g', 2)} of oatcakes.</p>
<p>Each oatcake provides:</p>
{table([['energy', hl('53 kcal', 'g', 3)], ['fat', hl('2.2 g', 'g')], ['saturated fat', '0.6 g'], ['salt', hl('0.2 g', 'p')], ['sugars', '0.3 g']])}
<p><b>Ingredients:</b> oatmeal (77%), vegetable oils, wheat flour, sugar, salt, raising agent: sodium
hydrogen carbonate.</p>
<p><b>Typical values {hl('per 100 g', 'y', 4)}:</b> energy 1792 kJ, {hl('427 kcal', 'g')}; protein 10.7 g; carbohydrate 56.45 g of
which sugars 2.4 g, starch 53.7 g; {hl('fat 17.6 g', 'g')} of which saturates 5.0 g, mono-unsaturates 7.9 g,
polyunsaturates 4.5 g; fibre 8.9 g; salt 1.4 g of which sodium 0.6 g.</p>
<p class="stem">How many {hl('<b>oatcakes</b>', 'b', 5)} are there in a packet?</p>""",
    options={'A': '7', 'B': '8', 'C': '21', 'D': '24', 'E': '27'},
    notes=[(1, 'p', 'Small numbers like 0.2 g are very rough (anything from 0.15 to 0.25!). Use the <b>big</b> numbers.'),
           (2, 'g', 'The packet is 3 lots of 100 g.'),
           (3, 'g', 'Per oatcake: 53 kcal, 2.2 g fat.'),
           (4, 'y', 'These are for 100 g, not the whole packet. Multiply by 3.'),
           (5, 'b', 'Oatcakes = whole packet ÷ one oatcake, for the same nutrient.')],
    steps=[
        f"""<p>Pick a nutrient with big, accurate numbers. Energy:</p>
{calc('whole packet: 3 × 427 = 1281 kcal', f'1281 ÷ 53 ≈ 24.2 {ar()} about 24 oatcakes')}""",
        f"""<p>Check with fat (also a fairly big number):</p>
{calc(f'whole packet: 3 × 17.6 = 52.8 g', f'52.8 ÷ 2.2 = 24 exactly {tick()}')}
{_oatcakes()}
{calc(f'oatcakes in a packet = {boxed("24")}')}
{note('Fast division: 53 × 24 = 1272, which is just under 1281. 53 × 25 = 1325 is too big.', 'tip')}""",
    ],
    answer_text='24 oatcakes (1281 ÷ 53 ≈ 24, and 52.8 ÷ 2.2 = 24).',
    why={'A': '7 is salt per 100 g ÷ salt per oatcake (1.4 ÷ 0.2). It forgets the packet is 300 g, and 0.2 g is badly rounded.',
         'B': '8 is oatcakes per <b>100 g</b> (427 ÷ 53 or 17.6 ÷ 2.2). The packet is 300 g, so × 3.',
         'C': '21 uses salt: 4.2 ÷ 0.2. But 0.2 g is rounded so much that salt can’t be trusted.',
         'E': '27 oatcakes would weigh about 11 g each and give only about 47 kcal each, not 53.'},
    fast='3 × 17.6 = 52.8 g of fat; 52.8 ÷ 2.2 = 24.',
))


# ---------------------------------------------------------------- 16 (Q32)
_GRIDS = {
    'A': {(0, 2), (1, 0), (1, 3), (2, 2), (3, 2)},
    'B': {(0, 2), (1, 0), (1, 3), (3, 0), (3, 2)},
    'C': {(0, 2), (1, 3), (2, 0), (3, 1), (3, 2)},
    'D': {(0, 1), (0, 2), (1, 0), (1, 3), (3, 2)},
    'E': {(0, 2), (1, 0), (1, 3), (2, 0), (3, 2)},
}


def _tally():
    c = 62
    x0, y0 = 40, 74
    parts, lab = [], []
    for r in range(4):
        for col in range(4):
            n = sum((r, col) in g for g in _GRIDS.values())
            fill = 'g' if n >= 2 else ('p' if n == 1 else 'none')
            parts.append(rect(x0 + col * c, y0 + r * c, c, c, k='ink', fill=fill, sw=1.6))
            if n:
                lab.append(text(x0 + col * c + c / 2, y0 + r * c + c / 2 + 9, n, k='ink', size=26, font='scrawl'))
    lab += [text(x0 + 2 * c, y0 - 14, 'Top', k='ink', size=17),
            text(x0 + 2 * c, 30, 'how many grids shade each square', k='ink', size=16),
            text(x0 + 2 * c, y0 + 4 * c + 28, 'green: shaded 2+ times', k='green', size=16),
            text(x0 + 2 * c, y0 + 4 * c + 50, 'pink: only once = a mistake', k='red', size=16)]
    # the four wrong grids, compared with E
    m = 22
    for i, L in enumerate('ABCD'):
        gx, gy = 360 + (i % 2) * 150, 60 + (i // 2) * 160
        lab.append(text(gx + 2 * m, gy - 8, L, k='ink', size=18, weight='700'))
        for r in range(4):
            for col in range(4):
                on = (r, col) in _GRIDS[L]
                missing = (r, col) in _GRIDS['E'] and not on
                extra = on and (r, col) not in _GRIDS['E']
                fill = 'p' if extra else ('ink' if on else 'none')
                parts.append(rect(gx + col * m, gy + r * m, m, m, k='red' if missing else 'muted',
                                  fill=fill if not missing else 'none', sw=2.4 if missing else 1))
        lab.append(text(gx + 2 * m, gy + 4 * m + 22, 'one square moved', k='red', size=15))
    lab.append(text(500, 392, 'red box = E’s square they missed', k='muted', size=15))
    lab.append(text(500, 412, 'pink = their wrong square', k='muted', size=15))
    return svg(660, 424, rough(*parts) + ''.join(lab),
               'Tally grid: five squares are shaded by two or more grids and match grid E; each of A to D has exactly one square moved compared with E')


Q.append(dict(
    n=16, orig=32, answer='E', topic='Logic & elimination',
    question=f"""<p>Instructions were given to shade {hl('5 particular squares', 'g', 1)} on a grid of 16 squares. {hl('One student shaded in the squares as instructed, but the other four got exactly 1 square wrong', 'y', 2)}.</p>
<p class="stem">Which one of the five grids below shows the {hl('<b>correct shading</b>', 'b', 3)}?</p>
{fig(Y, 'ps_q16_grids', 'Five 4 by 4 grids A to E, each with five shaded squares and the word Top above', 520)}""",
    options={'A': 'grid A', 'B': 'grid B', 'C': 'grid C', 'D': 'grid D', 'E': 'grid E'},
    notes=[(1, 'g', 'Every grid has 5 shaded squares.'),
           (2, 'y', 'Each wrong grid = the right grid with <b>one</b> square moved. So the right grid shares 4 squares with every other grid.'),
           (3, 'b', 'Find the grid that is “one move away” from all four others.')],
    steps=[
        f"""<p>Count, for every square, how many of the five grids shade it. A correct square is shaded by nearly every grid.
A misplaced square shows up in just one grid.</p>{_tally()}""",
        f"""<p>The five squares shaded two or more times are: top row 3rd, second row 1st and 4th, third row 1st, bottom row 3rd.
That is exactly grid E.</p>
{calc(f'the correct shading = {boxed("E")}')}
{note('The other way round: compared with E, A, B, C and D each have exactly one square in a different place (see the mini grids). ✓', 'check')}""",
    ],
    answer_text='Grid E: every other grid differs from it by exactly one square.',
    why={'A': 'If A were correct, grid C would have 2 squares wrong (it has neither A’s second-row left square nor its third-row square).',
         'B': 'If B were correct, grid C would have 2 squares wrong.',
         'C': 'If C were correct, grid A would have 2 squares wrong.',
         'D': 'If D were correct, grid C would have 2 squares wrong.'},
    fast='Tally each square across the five grids. Squares with a count of 1 are the mistakes; the five squares counted 2 or more are grid E.',
))


# ---------------------------------------------------------------- 17 (Q36)
def _ferries():
    X = lambda t: 80 + t * 4.4
    YM, YI = 250, 80
    parts, lab = [], []
    parts += [line(X(0), YM, X(120), YM, k='ink', w=2), line(X(0), YI, X(120), YI, k='ink', w=2)]
    lab += [text(X(0) - 8, YM + 5, 'mainland', k='ink', size=16, anchor='end'),
            text(X(0) - 8, YI + 5, 'island', k='ink', size=16, anchor='end')]
    for t in range(0, 121, 20):
        parts.append(line(X(t), YM, X(t), YM + 8, k='ink', w=1.4))
        lab.append(text(X(t), YM + 26, f'{9 + (t // 60)}:{t % 60:02d}', k='muted', size=14))
    boats = [  # (colour, list of (time, place)) place 0 = mainland, 1 = island
        ('pen', [(5, 0), (45, 1), (55, 1), (95, 0), (105, 0), (145, 1)]),
        ('orange', [(25, 0), (65, 1), (75, 1), (115, 0), (125, 0)]),
        ('green', [(45, 0), (85, 1), (95, 1), (135, 0)]),
        ('violet', [(15, 1), (55, 0), (65, 0), (105, 1), (115, 1), (155, 0)]),
        ('red', [(35, 1), (75, 0), (85, 0), (125, 1)]),
    ]
    for n, (k, pts) in enumerate(boats, 1):
        xy = []
        for (t0, p0), (t1, p1) in zip(pts, pts[1:]):
            y0, y1 = (YM, YI)[p0], (YM, YI)[p1]
            if t1 > 120:
                y1 = y0 + (y1 - y0) * (120 - t0) / (t1 - t0)
                t1 = 120
            if not xy:
                xy.append((X(t0), y0))
            xy.append((X(t1), y1))
            if t1 == 120:
                break
        parts.append(poly(xy, k=k, sw=3, closed=False))
        t0, p0 = pts[0]
        lab.append(circle(X(t0), (YM, YI)[p0], 11, k=k, fill='paper', sw=2))
        lab.append(text(X(t0), (YM, YI)[p0] + 5, n, k=k, size=15, weight='700'))
    parts.append(brace(X(5), X(105), YM + 36, 'boat 1: away 100 minutes', k='pen', size=16))
    lab.append(text(X(60), 40, 'flat bits = turnaround + waiting for the next slot', k='muted', size=15))
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'Timeline from 9:00 to 11:00 with five boats zig-zagging between mainland and island; boat 1 leaves at 9:05 and is next ready at 10:45, 100 minutes later')


Q.append(dict(
    n=17, orig=36, answer='C', topic='Timetables & scheduling',
    question=f"""<p>Fergus Castle is a tourist attraction on a small island off the coast of the mainland. A ferry
service runs between the mainland and the island, and takes {hl('40 minutes', 'g', 1)} to make a single
journey in either direction. There is a {hl('turnaround time of 5 minutes', 'p', 2)} at the end of each single
journey. Each day, {hl('ferries leave the mainland every 20 minutes, at 5, 25 and 45 minutes past each hour, starting at 09:05', 'y', 3)}. {hl('Ferries leave the island at 15, 35 and 55 minutes past each hour, starting at 09:15', 'y', 4)}.</p>
<p class="stem">What is the {hl('<b>minimum number of boats</b>', 'b', 5)} needed?</p>""",
    options={'A': '3', 'B': '4', 'C': '5', 'D': '6', 'E': '7'},
    notes=[(1, 'g', 'Each crossing: 40 minutes.'),
           (2, 'p', 'After landing, a boat can’t leave for 5 minutes. Then it must wait for the next timetabled slot!'),
           (3, 'y', 'Mainland departures: :05, :25, :45.'),
           (4, 'y', 'Island departures: :15, :35, :55. Ferries leave the island from 09:15, so some boats must <b>start</b> there.'),
           (5, 'b', 'Fewest boats that can run this timetable.')],
    steps=[
        f"""<p>Follow one boat round the whole loop:</p>
{calc(f'leave mainland 09:05 {ar()} arrive island 09:45',
      f'ready 09:50 {ar()} next island slot <b>09:55</b>',
      f'arrive mainland 10:35 {ar()} ready 10:40 {ar()} next mainland slot <b>10:45</b>',
      'round trip = 09:05 to 10:45 = <b>100 minutes</b>')}""",
        f"""<p>While boat 1 is away, the mainland still needs a boat every 20 minutes:</p>
{calc('09:05, 09:25, 09:45, 10:05, 10:25 → 5 departures', f'100 ÷ 20 = {boxed("5 boats")}')}
{_ferries()}
{note('At the start of the day: 3 boats wait at the mainland (09:05, 09:25, 09:45) and 2 at the island (09:15, 09:35). From then on, every departure has a boat ready.', 'check')}""",
    ],
    answer_text='5 boats: each boat needs 100 minutes per round trip, and a boat leaves each side every 20 minutes.',
    why={'A': '3 boats only cover the first three mainland departures. The island’s 09:15 and 09:35 ferries would have no boat.',
         'B': '4 assumes a round trip of 80 or 90 minutes. It forgets that after the 5-minute turnaround a boat must wait for the next slot (:55 and :45), so the loop is 100 minutes.',
         'D': '6 boats would work, but the timetable can be run with one fewer, so 6 isn’t the minimum.',
         'E': '7 is even more boats than needed.'},
    fast='One loop: 09:05 → 09:55 → 10:45 = 100 minutes. A departure every 20 minutes needs 100 ÷ 20 = 5 boats.',
))
