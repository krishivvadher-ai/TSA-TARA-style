from wslib import *
from _2018_ps_1 import DIG7, seg7

Y = 2018
Q = []

# ---------------------------------------------------------------- 9 (Q19)
def _prize():
    rows = [('David', 2, 16, 13, 32), ('John', 1, 10, 9, 26), ('Colin', 1, 13, 9, 30), ('Mike', 2, 12, 10, 29), ('Graham', 3, 8, 7, 36)]
    parts, lab = [], []
    heads = [(170, 'missed 2 in a row'), (330, 'penalties failed'), (500, 'goals')]
    for x, h in heads:
        lab.append(text(x, 30, h, k='ink', size=16))
    lab += [text(170, 50, 'out if more than 2', k='red', size=14), text(330, 50, 'out if more than 2', k='red', size=14)]
    for i, (name, miss, taken, scored, goals) in enumerate(rows):
        y = 84 + i * 40
        fail = taken - scored
        out1, out2 = miss > 2, fail > 2
        win = name == 'Mike'
        lab.append(text(70, y + 6, name, k='green' if win else 'ink', size=18, anchor='end', weight='700' if win else None))
        lab.append(text(170, y + 6, f'{miss} ' + ('✗' if out1 else '✓'), k='red' if out1 else 'ink', size=18))
        lab.append(text(330, y + 6, f'{taken} − {scored} = {fail} ' + ('✗' if out2 else '✓'), k='red' if out2 else 'ink', size=18))
        lab.append(text(500, y + 6, goals, k='green' if win else ('muted' if out1 or out2 else 'ink'), size=20, weight='700' if win else None))
        if out1 or out2:
            parts.append(line(20, y, 540, y, k='red', w=1.4))
    parts.append(circle(500, 84 + 3 * 40, 18, k='green', sw=2.4))
    lab.append(text(600, 84 + 3 * 40 + 6, 'winner', k='green', size=19, font='scrawl'))
    return svg(660, 284, rough(*parts) + ''.join(lab),
               'Graham is out for missing sessions; David and Colin are out for failing more than two penalties; Mike beats John 29 goals to 26')

Q.append(dict(
    n=9, orig=19, answer='D', topic='Rules & filters',
    question=f"""<p>A Youth Centre runs a number of football teams for boys of different ages. Each season, one
prize is awarded to the player who has given the best all-round performance. Five players have
been nominated as possible recipients of this year’s prize. The manager has decided {hl('not to reward any player who has missed two consecutive training sessions more than twice', 'y', 1)}, and the
manager will also {hl('exclude anyone who has failed to score a goal from a penalty kick more than twice', 'p', 2)}. After these criteria have been applied, the prize will go to the player who has scored the
{hl('highest number of goals', 'b', 3)}.</p>
{table([['David', '2', '3', '2', '16', '13', '32'], ['John', '3', '2', '1', '10', '9', '26'], ['Colin', '2', '4', '1', '13', '9', '30'],
        ['Mike', '1', '2', '2', '12', '10', '29'], ['Graham', '2', '0', '3', '8', '7', '36']],
       head=['<i>player</i>', '<i>no. of years in a team</i>', f'<i>{hl("no. of times late for training", "p", 4)}</i>',
             '<i>no. of times missed two consecutive training sessions</i>', '<i>no. of penalty kicks taken</i>',
             '<i>no. of penalties scoring a goal</i>', '<i>total no. of goals scored</i>'])}
<p class="stem">Which player will receive the best all-round performance prize?</p>""",
    options={'A': 'David', 'B': 'John', 'C': 'Colin', 'D': 'Mike', 'E': 'Graham'},
    notes=[(1, 'y', 'Rule 1: “more than twice” means 3 or more. Exactly 2 is still allowed.'),
           (2, 'p', 'Rule 2 needs a subtraction: penalties <b>missed</b> = taken − scored. That number isn’t in the table.'),
           (3, 'b', 'Only after both rules: most goals wins.'),
           (4, 'p', 'Red herring! Being late doesn’t matter, and nor do years in a team.')],
    steps=[
        f"""<p>Rule 1 (missed two sessions in a row more than twice): only Graham, with 3, is out.</p>
<p>Rule 2 (failed penalties = taken − scored, out if more than 2):</p>
{calc('David 16 − 13 = 3 ✗', 'John 10 − 9 = 1 ✓', 'Colin 13 − 9 = 4 ✗', 'Mike 12 − 10 = 2 ✓ (exactly 2 is fine)', 'Graham 8 − 7 = 1 (already out)')}""",
        f"""{_prize()}
{calc(f'left: John 26 goals, Mike 29 goals {ar()} {boxed("Mike")}')}""",
    ],
    answer_text='Mike: John and Mike survive both rules, and Mike has more goals (29 against 26).',
    why={'A': 'David failed with 3 penalties (16 taken, 13 scored), which is more than twice.',
         'B': 'John passes both rules but only has 26 goals, fewer than Mike’s 29.',
         'C': 'Colin failed with 4 penalties (13 taken, 9 scored). His 4 late arrivals don’t matter at all.',
         'E': 'Graham has the most goals (36) but missed two sessions in a row 3 times.'},
    fast='Cross out Graham (3 missed runs), then work out misses: David 3 and Colin 4 are out. Mike 29 beats John 26.',
))

# ---------------------------------------------------------------- 10 (Q20)
FACE_UV = {'top': ((0.866, 0.5), (0.866, -0.5)), 'left': ((0.866, 0.5), (0, -1)), 'right': ((0.866, -0.5), (0, -1))}


def _letter(cx, cy, uv, up, L, F, k):
    u, v = uv
    neg = lambda a: (-a[0], -a[1])
    U, R = {'v': (v, u), 'u': (u, neg(v)), '-v': (neg(v), neg(u)), '-u': (neg(u), v)}[up]
    return (f'<text x="0" y="{0.36 * F:.1f}" transform="matrix({R[0]:.3f} {R[1]:.3f} {-U[0]:.3f} {-U[1]:.3f} {cx:.1f} {cy:.1f})" '
            f'class="t-print c-{k}" font-size="{F}" font-weight="700" text-anchor="middle">{L}</text>')


def iso_cube(cx, cy, s, top=None, left=None, right=None, fills=('paper', 'paper', 'paper')):
    """Isometric cube; top/left/right = (letter, up, colour) with up in u, -u, v, -v."""
    h = 0.866 * s
    Bk, Rt, F, Lt = (cx, cy - s), (cx + h, cy - s / 2), (cx, cy), (cx - h, cy - s / 2)
    Lb, Fb, Rb = (cx - h, cy + s / 2), (cx, cy + s), (cx + h, cy + s / 2)
    parts = [poly([Bk, Rt, F, Lt], k='ink', fill=fills[0], sw=2), poly([Lt, F, Fb, Lb], k='ink', fill=fills[1], sw=2),
             poly([F, Rt, Rb, Fb], k='ink', fill=fills[2], sw=2)]
    labs = []
    centres = {'top': (cx, cy - s / 2), 'left': (cx - h / 2, cy + s / 4), 'right': (cx + h / 2, cy + s / 4)}
    for face, spec in (('top', top), ('left', left), ('right', right)):
        if spec:
            L, up, k = spec
            labs.append(_letter(*centres[face], FACE_UV[face], up, L, s * 0.62, k))
    return parts, labs


def _andrew_net():
    w, ox, oy = 62, 30, 34
    cells = {'A': (0, 0), 'N': (1, 0), 'D': (1, 1), 'R': (2, 1), 'E': (3, 1), 'W': (3, 2)}
    parts, lab = [], []
    for L, (c, r) in cells.items():
        parts.append(rect(ox + c * w, oy + r * w, w, w, k='ink', fill='y' if L == 'A' else 'paper', sw=2))
        lab.append(text(ox + c * w + w / 2, oy + r * w + w / 2 + 12, L, k='ink', size=34, font='print'))
    # zip arrow: A bottom edge meets D left edge
    parts.append(arrow(ox + 24, oy + w + 10, ox + w - 10, oy + w + 40, k='red', bend=0.35))
    lab += [text(ox + 6, oy + w + 74, 'A’s bottom zips', k='red', size=15, anchor='start'),
            text(ox + 6, oy + w + 92, 'onto D’s left side', k='red', size=15, anchor='start')]
    tx = 300
    lab += [text(tx, 40, 'Opposite faces: D–E, N–W, A–R', k='ink', size=17, anchor='start'),
            text(tx, 74, 'Where A’s four sides go:', k='pen', size=18, font='scrawl', anchor='start'),
            text(tx, 100, 'right side → N   (joined on the net)', k='ink', size=16, anchor='start'),
            text(tx, 124, 'bottom → D   (the corner zip)', k='ink', size=16, anchor='start'),
            text(tx, 148, 'top → E   (E is opposite D)', k='ink', size=16, anchor='start'),
            text(tx, 172, 'left side → W   (W is opposite N)', k='ink', size=16, anchor='start'),
            text(tx, 206, 'So A’s feet always point at D,', k='red', size=16, anchor='start'),
            text(tx, 226, 'and its point always aims at E.', k='red', size=16, anchor='start')]
    return svg(660, 250, rough(*parts) + ''.join(lab),
               'The net with A highlighted: A’s right side touches N, its bottom zips onto D, its top meets E and its left side meets W')


def _andrew_views():
    true = {1: (('E', 'v', 'ink'), ('W', 'v', 'ink'), ('A', 'v', 'red')),
            2: (('R', 'v', 'ink'), ('W', 'u', 'ink'), ('E', 'u', 'ink')),
            3: (('N', '-u', 'ink'), ('A', '-u', 'green'), ('D', 'v', 'ink')),
            4: (('N', '-u', 'ink'), ('A', '-u', 'red'), ('D', 'v', 'ink')),
            5: (('N', '-v', 'ink'), ('E', 'v', 'ink'), ('A', '-u', 'red'))}
    note_ = {1: ('A should stand', 'upright ✗'), 2: ('matches', 'the paper ✓'), 3: ('matches', 'the paper ✓'),
             4: ('A’s point should', 'face away from D ✗'), 5: ('A should point', 'towards E ✗')}
    parts, lab = [], []
    for i in range(1, 6):
        cx = 66 + (i - 1) * 130
        p, l = iso_cube(cx, 86, 46, *true[i])
        parts += p
        lab += l
        ok = i in (2, 3)
        lab.append(text(cx, 168, str(i), k='ink', size=18, weight='700'))
        lab.append(text(cx, 192, note_[i][0], k='green' if ok else 'red', size=14))
        lab.append(text(cx, 210, note_[i][1], k='green' if ok else 'red', size=14))
    lab.append(text(330, 238, 'the real cube, turned to show the same three faces as each view', k='muted', size=15))
    return svg(660, 250, rough(*parts) + ''.join(lab),
               'The real folded cube drawn for each view: views 2 and 3 match; in views 1, 4 and 5 the letter A is turned the wrong way')

Q.append(dict(
    n=10, orig=20, answer='B', topic='Cubes & nets',
    question=f"""<p>The diagram below shows the net of a cube.</p>
{fig(Y, 'ps_q10_net', 'Net: A and N in the top row; D, R, E in the middle row with D under N; W under E', 240)}
<p>The following diagrams show five suggested views of the cube {hl('once it has been assembled', 'y', 1)}.</p>
{fig(Y, 'ps_q10_views', 'Five cube views: 1 E on top, W left, A right on its side; 2 R top, W left, E right; 3 N top, A left pointing away from D, D right; 4 the same but A pointing towards D; 5 N top, E left, A right upright', 520)}
<p class="stem">Which {hl('two', 'b', 2)} of the above are possible views of the cube?</p>""",
    options={'A': '1 and 2', 'B': '2 and 3', 'C': '3 and 4', 'D': '1 and 4', 'E': '4 and 5'},
    notes=[(1, 'y', 'Every view shows three faces that really are neighbours, so you must check which way each letter is <b>turned</b>.'),
           (2, 'b', 'Exactly two views work. 3 and 4 show the same faces with A turned differently, so at most one of them can be right.')],
    steps=[
        f"""<p>First, opposite faces (they can never be seen together): D–E, N–W, A–R. All five views pass, so the letters’ turns decide it.</p>
<p>A appears in four views, so pin down A’s four sides:</p>{_andrew_net()}""",
        f"""<p>Now check A in each view:</p>
<ul><li>View 1: E is on top and A sits below it, so A’s point should aim up at E. It is lying on its side. {cross()}</li>
<li>View 3: A’s right side touches the top face N, and its feet face D across the middle edge. {tick()}</li>
<li>View 4: A’s point aims at D. But A’s feet must touch D. {cross()}</li>
<li>View 5: A’s right side should touch N on top and its point should aim at E, sideways. It stands upright. {cross()}</li>
<li>View 2 has no A. E’s left side touches R ✓ (joined on the net), E’s bottom touches W’s top ✓ (joined on the net), W’s left side meets R’s bottom ✓ (they zip round E’s corner).</li></ul>""",
        f"""<p>The real cube, turned to match each view:</p>{_andrew_views()}
{calc(f'possible views: 2 and 3 {ar()} {boxed("B")}')}
{note('N looks the same upside down, so a sideways N (looking like Z) only tells you which way its uprights run, not which end is the top.', 'tip')}""",
    ],
    answer_text='Views 2 and 3 are possible.',
    why={'A': 'View 1 is impossible: with E on top, A must stand upright beneath it, not on its side.',
         'C': 'Views 3 and 4 can’t both be right: same three faces, but A is turned the opposite way. In 4 A’s point aims at D, yet A’s feet touch D.',
         'D': 'Both 1 and 4 are impossible (see A’s turns).',
         'E': 'Both are impossible: in 5 A stands upright, but its right side should touch N on top.'},
    fast='Fix A: feet on D, point at E, right side on N. Views 1, 4 and 5 all turn A wrongly, leaving 2 and 3.',
))

# ---------------------------------------------------------------- 11 (Q24)
def _segments():
    parts, lab = [], []
    lab.append(text(20, 24, 'Segments in each digit of this clock:', k='ink', size=17, anchor='start'))
    for i, d in enumerate('0123456789'):
        x = 36 + i * 62
        parts += seg7(x, 42, 28, 58, DIG7[d], k='ink', sw=4, gap=3)
        n = len(DIG7[d])
        lab.append(text(x + 14, 126, f'{d}: {n}', k='red' if n >= 6 else 'ink', size=16, weight='700' if n >= 6 else None))
    places = [('0', 'hours tens', '0, 1 or 2', '0 → 6'), ('8', 'hours units', 'any after 0 or 1', '8 → 7'),
              ('0', 'minutes tens', '0 to 5 only', '0 → 6'), ('8', 'minutes units', 'any', '8 → 7')]
    for i, (d, name, allowed, best) in enumerate(places):
        x = 70 + i * 140 + (26 if i >= 2 else 0)
        parts += seg7(x, 168, 40, 82, DIG7[d], k='pen', sw=6, gap=4)
        lab += [text(x + 20, 158, name, k='muted', size=14), text(x + 20, 276, allowed, k='ink', size=14),
                text(x + 20, 298, best, k='green', size=17, weight='700')]
    parts += [circle(313, 190, 4, k='pen', fill='paper'), circle(313, 228, 4, k='pen', fill='paper')]
    lab.append(text(330, 330, '08:08 → 6 + 7 + 6 + 7 = 26 segments', k='red', size=20, font='scrawl'))
    return svg(660, 344, rough(*parts) + ''.join(lab),
               'The ten digits with their segment counts (8 has 7; 0 and 6 have 6), then the best time 08:08 using 6, 7, 6 and 7 segments')

Q.append(dict(
    n=11, orig=24, answer='D', topic='Digital displays',
    question=f"""<p>I have a digital clock that works in {hl('24-hour format (that is, after 23:59, it goes to 00:00)', 'y', 1)}. The
patterns for each number are made up of segments, {hl('as shown below', 'p', 2)}:</p>
{fig(Y, 'ps_q11_digits', 'Seven-segment digits 1 2 3 4 5 6 7 8 9 0', 440)}
<p class="stem">What is the {hl('maximum number of segments', 'b', 3)} that can be displayed at once, {hl('while still showing a valid time', 'y', 4)}?</p>""",
    options={'A': '20', 'B': '23', 'C': '24', 'D': '26', 'E': '28'},
    notes=[(1, 'y', 'Hours run 00 to 23, and minutes 00 to 59. A leading 0 is shown.'),
           (2, 'p', 'Count from <b>this</b> picture: here 7 has 3 segments and 9 has only 5 (no bottom bar).'),
           (3, 'b', 'Choose the digit with the most segments in each place.'),
           (4, 'y', 'So 88:88 (28 segments) is not allowed.')],
    steps=[
        f"""<p>Count the segments of each digit from the picture, then pick the best allowed digit for each place:</p>{_segments()}""",
        f"""{calc('hours: 08 gives 6 + 7 = 13 (20 to 23 only gives 5 + 6 = 11 at best)',
                  'minutes: tens digit can only be 0 to 5, best is 0 (6); units 8 (7) → 13',
                  f'total = 13 + 13 = {boxed("26")}  (at 08:08)')}
{note('8 is the best digit, then 0 and 6. The minutes tens digit stops at 5, so 6 is not allowed there.', 'check')}""",
    ],
    answer_text='26 segments, at 08:08.',
    why={'A': '20 is what 23:59 gives (5 + 5 + 5 + 5): the “last” time isn’t the one with most segments. It is also 8:08 with the leading zero left off.',
         'B': '23 comes from 08:59 (6 + 7 + 5 + 5), thinking 59 is the biggest minutes. 5 and 9 have fewer segments than 0 and 8.',
         'C': '24 is 20:08 (5 + 6 + 6 + 7): starting with 2 forces the second digit to be 0–3.',
         'E': '28 is 88:88, all four digits 8, which isn’t a valid time.'},
    fast='Best digits: 8 (7), then 0 (6). Hours 08 = 13, minutes 08 = 13. Total 26.',
))

# ---------------------------------------------------------------- 12 (Q25)
def _vote_table():
    names = ['Sam', 'Val', 'Kim', 'Pat', 'Jo']
    data = [('Sam', ['–', '37 304', '34 493', '38 206', '22 871']), ('Val', ['37 862', '–', '25 517', '27 818', '20 143']),
            ('Kim', ['23 148', '31 690', '–', '30 247', '42 620']), ('Pat', ['26 493', '24 485', '29 681', '–', '31 354']),
            ('Jo', ['28 506', '27 530', '25 308', '24 763', '–']), ('no second choice', ['822', '1027', '1263', '952', '848'])]
    head = (f'<tr><th></th><th colspan="5"><i>{hl("first-choice votes", "y", 3)}</i></th></tr>'
            f'<tr><th><i>{hl("second-choice votes", "p", 4)}</i></th>' + ''.join(f'<th>{n}</th>' for n in names) + '</tr>')
    body = ''
    for r, vals in data:
        cells = ''.join(f'<td>{hl(v, "g") if (r, i) == ("Val", 0) else v}</td>' for i, v in enumerate(vals))
        body += f'<tr><td>{r}</td>{cells}</tr>'
    return f'<div class="tbl-wrap"><table class="ptable"><thead>{head}</thead><tbody>{body}</tbody></table></div>'


def _election():
    first = [('Sam', 116.831), ('Val', 122.036), ('Kim', 116.262), ('Pat', 121.986), ('Jo', 117.836)]
    X = lambda v: 110 + v * 2.2
    parts, lab = [], []
    lab.append(text(20, 22, 'Stage 1: first choices (thousands)', k='ink', size=17, anchor='start'))
    for i, (n, v) in enumerate(first):
        y = 34 + i * 28
        top2 = n in ('Val', 'Pat')
        parts.append(rect(X(0), y, X(v) - X(0), 20, k='ink', fill='b' if top2 else 'paper', sw=1.4))
        lab.append(text(100, y + 16, n, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 8, y + 16, f'{v:.1f}' + ('  ✓ through' if top2 else ''), k='pen' if top2 else 'muted', size=15, anchor='start'))
    lab.append(text(X(122) + 110, 34 + 2 * 28 + 16, 'Val leads Pat by only 50', k='pen', size=16, font='scrawl', anchor='start'))
    Xs = lambda v: 110 + v * 2.2
    lab.append(text(20, 196, 'Stage 2: add the eliminated voters’ second choices', k='ink', size=17, anchor='start'))
    for i, (n, a, b) in enumerate((('Val', 122.036, 83.522), ('Pat', 121.986, 87.528))):
        y = 210 + i * 36
        parts.append(rect(Xs(0), y, Xs(a) - Xs(0), 24, k='ink', fill='b', sw=1.4))
        parts.append(rect(Xs(a), y, Xs(a + b) - Xs(a), 24, k='ink', fill='g' if n == 'Pat' else 'o', sw=1.4))
        lab.append(text(100, y + 18, n, k='ink', size=16, anchor='end'))
        lab.append(text(Xs(a) + 40, y + 18, f'+{b:.1f}', k='ink', size=14))
        lab.append(text(Xs(a + b) + 8, y + 18, f'{a + b:.1f}', k='green' if n == 'Pat' else 'ink', size=16, anchor='start',
                        weight='700' if n == 'Pat' else None))
    return svg(660, 290, rough(*parts) + ''.join(lab),
               'Stage 1: Val 122.0 thousand and Pat 122.0 thousand lead; stage 2: Val reaches 205.6 thousand and Pat 209.5 thousand')

Q.append(dict(
    n=12, orig=25, answer='D', topic='Tables & voting',
    question=f"""<p>The President of Bugaria is elected using the supplementary vote system, which is conducted
as follows:</p>
<p>Voters vote for their first-choice and second-choice candidates (though a second choice is
optional).</p>
<p>{hl('The two candidates with the most first-choice votes go through to a second stage', 'y', 1)}, whilst the
others are eliminated. {hl('The second-choice votes for these two from the ballot papers of the eliminated candidates are added to their first-choice votes', 'p', 2)}, and the candidate with the greater
total is elected President.</p>
<p>The table below shows a summary of the votes cast for the five candidates in last week’s
Bugarian Presidential Election. For example, {hl('37 862 voters cast their first vote for Sam and their second vote for Val', 'g', 5)}.</p>
{_vote_table()}
<p class="stem">Who has been elected President of Bugaria?</p>""",
    options={'A': 'Sam', 'B': 'Val', 'C': 'Kim', 'D': 'Pat', 'E': 'Jo'},
    notes=[(1, 'y', 'First-choice total = add up a <b>column</b> (including “no second choice”).'),
           (2, 'p', 'Only votes from the three knocked-out candidates move across. Votes between the two finalists don’t move.'),
           (3, 'y', 'Columns = who they voted for first.'),
           (4, 'p', 'Rows = who they put second.'),
           (5, 'g', 'Use this example to check you’re reading the table the right way round: Sam’s column, Val’s row.')],
    steps=[
        f"""<p>Stage 1: add each column (rounding to the nearest hundred is enough to spot the top two):</p>
{calc('Sam: 37.9 + 23.1 + 26.5 + 28.5 + 0.8 ≈ 116.8 thousand', 'Val: 37.3 + 31.7 + 24.5 + 27.5 + 1.0 ≈ 122.0 thousand',
      'Kim: 34.5 + 25.5 + 29.7 + 25.3 + 1.3 ≈ 116.3 thousand', 'Pat: 38.2 + 27.8 + 30.2 + 24.8 + 1.0 ≈ 122.0 thousand',
      'Jo: 22.9 + 20.1 + 42.6 + 31.4 + 0.8 ≈ 117.8 thousand')}
<p>Val (122 036) and Pat (121 986) go through. Val leads by just 50.</p>""",
        f"""<p>Stage 2: from the Sam, Kim and Jo columns, take the second choices for Val and for Pat:</p>
{calc('Val gets 37 862 + 25 517 + 20 143 = 83 522', 'Pat gets 26 493 + 29 681 + 31 354 = 87 528',
      'Pat gains 4006 more, far more than Val’s 50 lead')}
{_election()}
{calc(f'Val 205 558, Pat 209 514 {ar()} {boxed("Pat")}')}""",
    ],
    answer_text='Pat: 121 986 + 87 528 = 209 514 beats Val’s 122 036 + 83 522 = 205 558.',
    why={'A': 'Sam has the most <b>second</b>-choice votes overall (add the Sam row), but is knocked out in stage 1.',
         'B': 'Val tops the first-choice count, but only by 50 votes; Pat picks up 4006 more second choices.',
         'C': 'Kim has the fewest first-choice votes, so is eliminated straight away.',
         'E': 'Jo is third on first choices (about 117 800), so doesn’t reach stage 2. Jo’s big 42 620 cell is Jo’s voters choosing Kim second.'},
    fast='Column totals: Val and Pat both ≈ 122 000 (Val by 50). Transfers from Sam, Kim and Jo: Pat 87 528 against Val 83 522. Pat.',
))

# ---------------------------------------------------------------- 13 (Q26)
def _boxes():
    c, ox, oy = 56, 250, 40
    cells = {(0, 1): '5', (1, 0): '≤6', (1, 1): '≤6', (1, 2): '≤6', (2, 1): '≤7', (2, 2): '≤7', (3, 2): '5'}
    parts, lab = [], []
    for (r, col), v in cells.items():
        f = {0: 'paper', 1: 'b', 2: 'o', 3: 'paper'}[r]
        parts.append(rect(ox + col * c, oy + r * c, c, c, k='ink', fill=f, sw=2))
        lab.append(text(ox + col * c + c / 2, oy + r * c + c / 2 + 7, v, k='ink', size=19))
    # Amy on the left
    lab.append(eye(120, oy + 2 * c, facing='right'))
    lab.append(text(120, oy + 2 * c + 34, 'Amy', k='ink', size=17))
    for r, h in enumerate((5, 6, 7, 5)):
        parts.append(circle(196, oy + r * c + c / 2, 15, k='red', sw=2))
        lab.append(text(196, oy + r * c + c / 2 + 6, h, k='red', size=18, weight='700'))
    lab.append(text(196, oy - 12, 'Amy sees', k='red', size=14))
    # Ben below
    lab.append(eye(ox + 1.5 * c, oy + 4 * c + 76, facing='up'))
    lab.append(text(ox + 1.5 * c + 30, oy + 4 * c + 82, 'Ben', k='ink', size=17, anchor='start'))
    for col, t in enumerate(('≤ 6', '5 to 7', '5 to 7')):
        lab.append(text(ox + col * c + c / 2, oy + 4 * c + 24, t, k='pen', size=15))
    lab.append(text(ox + 1.5 * c, oy + 4 * c + 46, 'Ben sees (left to right)', k='pen', size=14))
    tx = 440
    lab += [text(tx, 60, 'Each column Ben sees =', k='ink', size=16, anchor='start'),
            text(tx, 80, 'its tallest stack.', k='ink', size=16, anchor='start'),
            text(tx, 116, 'Left column: just one', k='ink', size=16, anchor='start'),
            text(tx, 136, 'stack, in Amy’s “6” row', k='ink', size=16, anchor='start'),
            text(tx, 156, '→ at most 6.', k='red', size=16, anchor='start'),
            text(tx, 192, 'Amy’s “7” row: the 7 is in', k='ink', size=16, anchor='start'),
            text(tx, 212, 'the middle or right column.', k='ink', size=16, anchor='start'),
            text(tx, 256, 'E: 7 on the left ✗', k='red', size=20, font='scrawl', anchor='start')]
    return svg(660, 360, rough(*parts) + ''.join(lab),
               'Plan of the pile with Amy on the left seeing heights 5, 6, 7, 5 by row and Ben below; the left column can be at most 6 high')

Q.append(dict(
    n=13, orig=26, answer='E', topic='Views of 3D shapes',
    question=f"""<p>A number of identical boxes are piled up, waiting to be loaded into a delivery van. Amy and
Ben are about to load them into the van.</p>
<p>The appearance of the pile of boxes and the positions of Amy and Ben at present are shown
below:</p>
{fig(Y, 'ps_q13_plan', 'Plan view from above: four rows of stacks; Amy stands to the left, Ben below', 330)}
<p>{hl('Amy’s view of the pile', 'g', 1)} is:</p>
{fig(Y, 'ps_q13_amy', 'Amy’s view: four columns of boxes 5, 6, 7 and 5 high', 90)}
<p class="stem">Which one of the following {hl('could <b>not</b>', 'b', 2)} be {hl('Ben’s view', 'y', 3)} of the pile?</p>
{fig(Y, 'ps_q13_opts', 'Five possible views from Ben, three columns each: A 5 6 7, B 5 7 6, C 6 5 7, D 6 7 5, E 7 5 6', 470)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'g', 'Amy looks along the rows: she sees the tallest stack in each row, north to south: 5, 6, 7, 5.'),
           (2, 'b', 'Four views are possible; find the one that breaks a rule.'),
           (3, 'y', 'Ben looks along the columns (west to east): he sees the tallest stack in each column.')],
    steps=[
        f"""<p>Amy stands on the left, so her view goes row by row (top row of the plan on her left). Ben stands below, so his view goes column by column.</p>{_boxes()}""",
        f"""<p>What must be true of Ben’s view (left, middle, right):</p>
{calc('left column: only one stack, in the “6” row → at most 6',
      'the “7” row has stacks only in the middle and right columns → one of those shows 7',
      'middle column includes the “5” stack at the top → at least 5; right column includes the bottom “5” → at least 5')}
{calc('A 5 6 7 ✓   B 5 7 6 ✓   C 6 5 7 ✓   D 6 7 5 ✓', f'E 7 5 6: left column 7 ✗ (and no 7 in the middle or right) {ar()} {boxed("E")}')}""",
    ],
    answer_text='E: its left column is 7 high, but that stack can be at most 6.',
    why={'A': 'A (5, 6, 7) works: the 7 is on the right in the “7” row, and a 6 sits in the “6” row.',
         'B': 'B (5, 7, 6) works: the 7 is in the middle column, and the right column’s 6 can be in the “6” row.',
         'C': 'C (6, 5, 7) works: the lone left stack is the 6, the right column holds the 7.',
         'D': 'D (6, 7, 5) works: left stack 6, middle column has the 7, the right column is never more than 5.'},
    fast='Left column = one stack in Amy’s 6-row, so ≤ 6. E shows 7 there. E.',
))

# ---------------------------------------------------------------- 14 (Q30)
def _coupons():
    parts, lab = [], []
    groups = [('9p', 2, 'o', 'orange'), ('14p', 8, 'b', 'pen'), ('20p', 1, 'g', 'green')]
    x = 34
    for val, n, f, col in groups:
        x0 = x
        for i in range(n):
            parts.append(circle(x, 70, 22, k=col, fill=f, sw=2))
            lab.append(text(x, 76, val, k='ink', size=14))
            x += 50
        lab.append(text((x0 + x - 50) / 2, 124, f'{n} × {val}', k=col, size=17, weight='700'))
        x += 16
    lab += [text(330, 160, '2 × 9 + 8 × 14 + 1 × 20 = 18 + 112 + 20 = 150p ✓', k='ink', size=18),
            text(330, 186, '8 > 2 > 1 ✓   so 2 + 8 + 1 = 11 coupons', k='red', size=19, font='scrawl')]
    return svg(660, 200, rough(*parts) + ''.join(lab),
               'Two 9p coupons, eight 14p coupons and one 20p coupon make 150p: 11 coupons')

Q.append(dict(
    n=14, orig=30, answer='C', topic='Systematic search',
    question=f"""<p>Recently, packets of Amblers crisps have had ‘money-off’ coupons inside them. Some coupons
are worth {hl('9p', 'g')}, some are worth {hl('14p', 'g')} and some are worth {hl('20p', 'g')}.</p>
<p>George has been collecting these coupons. He has {hl('more 14p coupons than 9p coupons, and more 9p coupons than 20p coupons', 'y', 1)}. The total value of all of his coupons is {hl('exactly £1.50', 'g', 2)}.</p>
<p class="stem">How many coupons has George collected?</p>""",
    options={'A': '9', 'B': '10', 'C': '11', 'D': '12', 'E': '13'},
    notes=[(1, 'y', 'Order rule: number of 14p &gt; number of 9p &gt; number of 20p. So he has at least one 9p and at least two 14p.'),
           (2, 'g', '150p. Several mixes make 150p, so the order rule picks the right one.')],
    steps=[
        f"""<p>The 20p count is the smallest, so try 0, 1, 2, … 20p coupons and see what the 9p and 14p coupons must make:</p>
{calc('1 × 20p: 9s and 14s make 130 → 2 × 9 + 8 × 14 = 18 + 112 = 130 ✓',
      '2 × 20p: 9s and 14s make 110 → 6 × 9 + 4 × 14 ✗ (fewer 14s than 9s)',
      '0 × 20p: 9s and 14s make 150 → 12 × 9 + 3 × 14 ✗ (fewer 14s than 9s)',
      '3 or more × 20p: then at least four 9p and five 14p, already 36 + 70 + 60 = 166p ✗')}
{note('Finding 9s and 14s that make 130: 130 − 14 × 8 = 18 = 2 × 9. Try counting down the 14s from 9: 130 − 126 = 4 ✗, 130 − 112 = 18 ✓.', 'tip')}""",
        f"""{_coupons()}
{calc(f'2 + 8 + 1 = {boxed("11")} coupons')}""",
    ],
    answer_text='11 coupons: two 9p, eight 14p and one 20p.',
    why={'A': '9 coupons is 5 × 14p + 4 × 20p = 150p, but that has no 9p at all, breaking the order rule.',
         'B': '10 coupons is 4 × 9p + 1 × 14p + 5 × 20p = 150p, but it has more 20p than 14p.',
         'D': '12 coupons is 6 × 9p + 4 × 14p + 2 × 20p = 150p, but it has more 9p than 14p.',
         'E': '13 coupons is 10 × 9p + 3 × 20p = 150p, with no 14p coupons at all.'},
    fast='Smallest group is 20p, so try one 20p: 130p left = 2 × 9 + 8 × 14. Order 8 > 2 > 1 works. 11.',
))

# ---------------------------------------------------------------- 15 (Q31)
def _books():
    books = [('History of the 20th C.', 1900, 2000, 45), ('Illustrated Guide', 1750, 2000, 50),
             ('Beginner’s Guide', 1700, 1850, 40), ('History for All', 1750, 1950, 60), ('All About History', 1800, 1900, 55)]
    X = lambda yr: 196 + (yr - 1700) * 1.45
    parts = [rect(X(1900), 30, X(1950) - X(1900), 196, k='red', fill='p', sw=1.8)]
    lab = [text((X(1900) + X(1950)) / 2, 22, '1900–1950', k='red', size=16, weight='700')]
    for i, (name, a, b, price) in enumerate(books):
        y = 42 + i * 36
        ok = a <= 1900 and b >= 1950
        parts.append(rect(X(a), y, X(b) - X(a), 22, k='ink', fill='g' if ok else 'paper', sw=1.5))
        lab.append(text(188, y + 16, f'{name}', k='ink' if ok else 'muted', size=15, anchor='end'))
        sale = price * 0.8
        lab.append(text(X(a) + 8, y + 16, f'£{price} → £{sale:.0f}' + (' ✓' if ok else ' ✗'), k='green' if ok else 'muted',
                        size=14, anchor='start'))
    for yr in (1700, 1800, 1900, 2000):
        parts.append(line(X(yr), 226, X(yr), 234, k='ink', w=1.5))
        lab.append(text(X(yr), 252, yr, k='muted', size=14))
    parts.append(line(X(1700), 230, X(2000), 230, k='ink', w=1.5))
    return svg(660, 262, rough(*parts) + ''.join(lab),
               'Timeline of the five books: only History of the 20th Century, the Illustrated Guide and History for All cover 1900 to 1950')

Q.append(dict(
    n=15, orig=31, answer='E', topic='Tables & best deal',
    question=f"""<p>Joanne is {hl('studying the period 1900–1950', 'y', 1)} and has decided to buy a new book to help with her
studies. There are five different books available at her local bookshop, the details of which are
summarised below:</p>
{table([['History of the 20th Century', '1900–2000', 'yes', 'no', '£45'],
        ['The Illustrated Guide to History', '1750–2000', 'no', 'yes', '£50'],
        ['Beginner’s Guide to History', '1700–1850', 'no', 'no', '£40'],
        ['History for All', '1750–1950', 'yes', 'yes', '£60'],
        ['All About History', '1800–1900', 'yes', 'no', '£55']],
       head=['<i>title</i>', '<i>period covered</i>', '<i>hardback?</i>', '<i>illustrated?</i>', '<i>price</i>'])}
<p>On Tuesday, Joanne chose to buy the {hl('cheapest book that would satisfy her requirements', 'g', 2)}, and
went away to get the {hl('exact amount of money', 'g', 3)} needed to buy it. When she returned the following
day to buy her chosen book she found that there was a sale and {hl('all of the books had been reduced by 20%', 'p', 4)}. She then decided instead to buy the {hl('most expensive book that she could with the money she had', 'b', 5)}, and which still satisfied her requirements.</p>
<p class="stem">How much money did Joanne have left over once she had bought the book?</p>""",
    options={'A': '£0', 'B': '£1', 'C': '£2', 'D': '£3', 'E': '£5'},
    notes=[(1, 'y', 'Her only requirement: the book must cover <b>all</b> of 1900 to 1950. Hardback and pictures don’t matter.'),
           (2, 'g', 'Cheapest book that covers 1900–1950.'),
           (3, 'g', 'So she brings exactly that book’s full price.'),
           (4, 'p', 'Sale price = 80% of the old price.'),
           (5, 'b', 'Dearest suitable book whose <b>sale</b> price fits her money.')],
    steps=[
        f"""<p>Which books cover 1900–1950?</p>{_books()}""",
        f"""{calc('suitable: 20th Century £45, Illustrated Guide £50, History for All £60',
                  'cheapest suitable = £45 → she brings <b>£45</b>',
                  'sale (× 0.8): £36, £40, £48',
                  'dearest she can afford with £45: Illustrated Guide at £40',
                  f'left over: 45 − 40 = {boxed("£5")}')}
{note('20% off: find 10% and double it. 10% of £50 is £5, so 20% is £10 and the sale price is £40.', 'tip')}""",
    ],
    answer_text='£5: she brings £45, then buys the Illustrated Guide for £40 in the sale.',
    why={'A': '£0 comes from choosing the cheapest book of all on Tuesday (Beginner’s Guide, £40), which doesn’t cover 1900–1950.',
         'B': '£1 means buying All About History at £44, but it stops at 1900.',
         'C': '£2 would need a suitable book at £43 in the sale. None costs that.',
         'D': '£3 would need a suitable book at £42 in the sale. None costs that.'},
    fast='Covers 1900–1950: £45, £50, £60. She brings £45. Sale prices £36, £40, £48: buy the £40 one. £5 left.',
))

# ---------------------------------------------------------------- 16 (Q32)
U = 26


def _poly_u(pts, ox, oy, k='ink', fill='none', sw=2, rot=False, u=U):
    out = []
    for x, y in pts:
        if rot:
            x, y = (x - y) * 0.7071, (x + y) * 0.7071
        out.append((ox + x * u, oy - y * u))
    return poly(out, k=k, fill=fill, sw=sw)


def _pieces():
    parts, lab = [], []
    P1 = [(0, 0), (2, 0), (2, 2), (1, 2), (0, 1)]
    P2 = [(0, 0), (2.5, 0), (3, 0.5), (3, 1), (1, 1), (1, 2), (0, 1)]
    u, ox1, ox2, oy = 44, 130, 340, 120
    for gx in range(2):
        for gy in range(2):
            parts.append(rect(ox1 + gx * u, oy - (gy + 1) * u, u, u, k='muted', sw=0.8))
    for gx in range(3):
        parts.append(rect(ox2 + gx * u, oy - u, u, u, k='muted', sw=0.8))
    parts.append(rect(ox2, oy - 2 * u, u, u, k='muted', sw=0.8))
    parts.append(_poly_u(P1, ox1, oy, k='ink', fill='b', sw=2.4, u=u))
    parts.append(_poly_u(P2, ox2, oy, k='ink', fill='o', sw=2.4, u=u))
    parts.append(circle(ox2 + 2.75 * u, oy - 0.25 * u, 17, k='red', sw=2.4))
    lab += [text(ox1 + u, oy + 26, 'piece 1: 2 × 2 square', k='pen', size=16),
            text(ox1 + u, oy + 46, 'one big slanted corner', k='pen', size=16),
            text(ox2 + 1.5 * u, oy + 26, 'piece 2: 3 × 1 bar + half-square', k='orange', size=16),
            text(ox2 + 1.5 * u, oy + 46, 'with a TINY snipped corner', k='red', size=16),
            text(ox2 + 3 * u + 26, oy - 0.25 * u + 5, '← tiny snip', k='red', size=18, font='scrawl', anchor='start'),
            text(ox1 - 8, oy - 1.6 * u, 'big slant →', k='pen', size=16, font='scrawl', anchor='end'),
            text(ox1 - 8, oy - 1.6 * u + 18, '(1 square across)', k='pen', size=13, anchor='end')]
    return svg(600, 180, rough(*parts) + ''.join(lab),
               'The two pieces on a grid: a 2 by 2 square with a big slanted corner, and a 3 by 1 bar with a half-square on top and a tiny snipped corner')


def _logo_opts():
    opts = {
        'A': ([(0, 0), (2, 0), (2, 1), (1, 2), (0, 2)], [(2, 1), (3, 1), (3, 3.5), (2.5, 4), (2, 4), (2, 2), (1, 2)], (2.75, 3.75), False, (30, 170)),
        'B': ([(2, 0), (4, 0), (4, 1), (3, 2), (2, 2)], [(1, 0), (2, 0), (2, 2.5), (1.5, 3), (1, 3), (1, 1), (0, 1)], (1.75, 2.75), False, (150, 170)),
        'C': ([(1, 1), (2, 1), (2, 3), (0, 3), (0, 2)], [(1, 1), (2, 0), (3, 0), (3, 2.5), (2.5, 3), (2, 3), (2, 1)], (2.75, 2.75), True, (330, 206)),
        'D': ([(1, 1), (3, 1), (3, 2), (2, 3), (1, 3)], [(0, 0), (2.5, 0), (3, 0.5), (3, 1), (1, 1), (1, 2), (0, 1)], (2.75, 0.25), False, (420, 170)),
    }
    parts, lab = [], []
    for k, (p1, p2, snip, rot, (ox, oy)) in opts.items():
        parts.append(_poly_u(p1, ox, oy, fill='b', rot=rot))
        parts.append(_poly_u(p2, ox, oy, fill='o', rot=rot))
        sx, sy = snip
        if rot:
            sx, sy = (sx - sy) * 0.7071, (sx + sy) * 0.7071
        parts.append(circle(ox + sx * U, oy - sy * U, 12, k='red', sw=2.4))
        lab.append(text(ox + (1.5 if not rot else 0) * U, 216, f'{k} ✓', k='green', size=20, font='scrawl'))
    E = [(0, 1), (1, 0), (3, 0), (3, 2), (4, 2), (3, 3), (2, 3), (2, 2), (0, 2)]
    ox, oy = 530, 170
    parts.append(_poly_u(E, ox, oy, k='ink', fill='paper'))
    lab += [text(ox + 2 * U, 216, 'E ✗', k='red', size=20, font='scrawl'),
            text(ox + 2 * U, 240, 'no tiny snip', k='red', size=15),
            text(330, 268, 'blue = piece 1, orange = piece 2, red ring = the tiny snip', k='muted', size=15)]
    return svg(660, 280, rough(*parts) + ''.join(lab),
               'Options A to D each split into the two pieces with the tiny snipped corner ringed on the outline; E has no tiny snip')

Q.append(dict(
    n=16, orig=32, answer='E', topic='Shapes & jigsaws',
    question=f"""<p>Connem Ltd. has recently adopted a new company logo.</p>
<p>A large plastic version of the logo has just been delivered to the office, to be attached to the
outside of the building. Unfortunately, in transit, the plastic has {hl('broken into two pieces', 'y', 1)}, as
shown below:</p>
{fig(Y, 'ps_q16_pieces', 'Piece 1: a square with its top-left corner cut off at 45 degrees. Piece 2: a bar with a half-square triangle on top at one end and a small corner snipped off at the other end', 300)}
<p class="stem">Which one of the following {hl('could <b>not</b>', 'b', 2)} be Connem’s new logo?</p>
{fig(Y, 'ps_q16_opts', 'Five outlines A to E made of straight and 45-degree edges', 440)}""",
    options={'A': 'shape A', 'B': 'shape B', 'C': 'shape C', 'D': 'shape D', 'E': 'shape E'},
    notes=[(1, 'y', 'The logo is just the two pieces put back together (they may be turned round).'),
           (2, 'b', 'Four can be made. Look for a feature the pieces force onto every logo.')],
    steps=[
        f"""<p>Measure the pieces in squares. Piece 2 has a <b>tiny</b> snipped corner (half a square), much smaller than any other slanted edge:</p>{_pieces()}""",
        f"""<p>That tiny snip is on the outside corner of the bar, and piece 1 has nothing that could fill it. So it must show on the outline of <b>every</b> possible logo.</p>
{_logo_opts()}
{calc('A, B, C, D: each has one short slanted edge = the tiny snip, and splits into the two pieces ✓',
      f'E: both slanted edges are full-size (one square across) {ar()} {boxed("E")} cannot be made')}
{note('Area check too: the pieces cover 3½ + 3⅜ = 6⅞ squares; E covers 7.', 'check')}""",
    ],
    answer_text='E: it has no tiny snipped corner, so piece 2 can’t be in it.',
    why={'A': 'A is piece 1 (turned) with piece 2 standing upright beside it; the snip is at the top right.',
         'B': 'B is piece 2 standing upright with its half-square poking out at the bottom left, piece 1 to its right.',
         'C': 'C is the logo turned 45°: piece 2 stands upright, piece 1 fits against its half-square. The short top edge is the snip.',
         'D': 'D is piece 2 as drawn with piece 1 sitting on top of the bar, against the half-square. The snip is bottom right.'},
    fast='Spot the tiny snip on piece 2. Every real logo shows it; E doesn’t.',
))
