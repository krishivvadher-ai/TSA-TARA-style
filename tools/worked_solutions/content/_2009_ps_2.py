from wslib import *

Y = 2009
Q = []


# ---------------------------------------------------------------- 9 (Q19)
def _april():
    days = [(8, None, 0), (9, 'Denmark', 0), (10, 'Denmark', 3), (11, 'Israel', 0), (12, 'Italy', 0),
            (13, 'Italy', 5), (14, None, 0)]
    cw, x0, y0 = 82, 34, 40
    parts, lab = [], []
    for i, (d, who, more) in enumerate(days):
        x = x0 + i * cw
        parts.append(rect(x, y0, cw - 6, 92, k='ink' if who else 'muted', fill='g' if who else 'paper', sw=1.8))
        lab.append(text(x + (cw - 6) / 2, y0 + 26, f'{d} Apr', k='ink', size=18, font='print'))
        if who:
            lab.append(text(x + (cw - 6) / 2, y0 + 56, who, k='pen', size=17))
            if more:
                lab.append(text(x + (cw - 6) / 2, y0 + 78, f'+{more} more', k='muted', size=14))
        else:
            lab.append(text(x + (cw - 6) / 2, y0 + 58, 'nothing', k='red', size=16))
            lab.append(text(x + (cw - 6) / 2, y0 + 80, '✗', k='red', size=18))
    parts.append(brace(x0 + cw, x0 + 6 * cw - 6, y0 + 100, '', k='red'))
    lab.append(text(x0 + 3.5 * cw - 3, y0 + 144, '9 to 13 April: 5 days in a row', k='red', size=20, font='scrawl'))
    lab.append(text(x0 + 3.5 * cw - 3, y0 + 172, 'Denmark → Israel → Italy', k='pen', size=17))
    lab.append(text(x0 + 3.5 * cw - 3, y0 - 14, 'blue = one country she could be in that day', k='muted', size=15))
    return svg(640, 228, rough(*parts) + ''.join(lab),
               'Calendar strip for 8 to 14 April: 9 to 13 April each have a holiday somewhere, 8 and 14 April have none')


def _hols(cells):
    cells = [c.replace(',', ',<wbr>') for c in cells]
    return [hl(c, 'g') if c and i == 4 else c for i, c in enumerate(cells)]


Q.append(dict(
    n=9, orig=19, answer='D', topic='Tables & calendars',
    question=f"""<p>My friend's grandmother went on an overseas trip last year visiting several countries.
When he visited her this summer she claimed she had not been able to buy him a gift as
{hl('every country she visited was having a public holiday while she was there', 'y', 1)}. He was very
suspicious and consulted his diary to find out whether this was possible.</p>
<p>International Public Holidays:</p>
{table([_hols(['Denmark', '1', '', '', '9,10,13', '8,21', '1,5', '', '', '', '', '', '25,26']),
        _hols(['Finland', '1,6', '', '', '10,13', '1,21,31', '20', '', '', '', '31', '', '6,25,26']),
        _hols(['France', '1', '', '', '13', '1,8,21', '1', '14', '15', '', '', '1,11', '25']),
        _hols(['Germany', '1,6', '', '', '10,13', '1,21', '1,11', '', '15', '', '3,31', '1', '25,26']),
        _hols(['Greece', '1,6', '', '2,25', '17,20', '1', '8', '', '15', '', '28', '', '25,26']),
        _hols(['Hong Kong', '1,28,29,30', '', '', '5,10,13', '30', '13,15', '', '29,31', '5', '', '', '25,26, 31']),
        _hols(['Israel', '', '11', '12', '11,17,30', '24,31', '', '', '2', '21,22,30', '5', '', '14']),
        _hols(['Italy', '1,6', '', '', '12,13,25', '1', '', '', '15', '', '', '1', '8,25,26'])],
       head=['', 'Jan', 'Feb', 'Mar', hl('Apr', 'g', 3), 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])}
<p class="stem">What was the {hl('longest time', 'b', 2)} she could have been away?</p>""",
    options={'A': '2 days', 'B': '3 days', 'C': '4 days', 'D': '5 days', 'E': '6 days'},
    notes=[(1, 'y', 'Every day of the trip, she must be in <b>some</b> country with a holiday that day. She can hop between countries.'),
           (2, 'b', 'Find the longest run of dates in a row where at least one country has a holiday.'),
           (3, 'g', 'April is packed with holidays: look there for a long run.')],
    steps=[
        f"""<p>Merge all eight countries: for each month, which dates are a holiday <b>somewhere</b>? Look for dates in a row:</p>
{calc('Jan: 1, 6, 28, 29, 30 → 28 to 30 (3 days)', 'Apr: 5, 9, 10, 11, 12, 13, 17, 20, 25, 30 → 9 to 13 (5 days)',
      'May/Jun: 30, 31 May, 1 June → 3 days', 'Oct/Nov: 31 Oct, 1 Nov → 2 days; Dec: 25, 26 → 2 days')}""",
        f"""<p>Zoom in on April:</p>{_april()}""",
        f"""{calc(f'9 (Denmark), 10, 11 (Israel), 12 (Italy), 13 {ar()} {boxed("5 days")}')}
{note('8 April and 14 April are not holidays anywhere, so the run can’t stretch to 6 days.', 'check')}""",
    ],
    answer_text='5 days: 9 to 13 April, e.g. Denmark, then Israel, then Italy.',
    why={'A': '2 days is a run like Christmas (25 and 26 December), the first one most people spot.',
         'B': '3 days is the longest run in a <b>single</b> country (Hong Kong, 28 to 30 January). She could change countries.',
         'C': '4 days (10 to 13 April) misses Denmark’s holiday on 9 April.',
         'E': '6 days would need 8 or 14 April to be a holiday somewhere, and neither is.'},
    fast='Scan the April column: 9 (Denmark), 10, 11 (Israel), 12 (Italy), 13. Five in a row, with 8 and 14 free. 5 days.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _pulleys():
    A, B, C = (70, 196), (240, 172), (500, 140)
    rA, rBo, rBi, rC = 16, 32, 16, 64
    parts = [line(A[0], A[1] - rA, B[0], B[1] - rBo, k='ink', w=2), line(A[0], A[1] + rA, B[0], B[1] + rBo, k='ink', w=2),
             circle(*A, rA, k='ink', fill='b', sw=2), circle(*B, rBo, k='ink', fill='o', sw=2),
             line(B[0], B[1] - rBi, C[0], C[1] - rC, k='ink', w=2), line(B[0], B[1] + rBi, C[0], C[1] + rC, k='ink', w=2),
             circle(*B, rBi, k='ink', fill='b', sw=2), circle(*C, rC, k='ink', fill='g', sw=2),
             arrow(A[0] - 14, A[1] - 30, A[0] + 16, A[1] - 28, k='red', bend=-0.3),
             arrow(B[0] - 22, B[1] - 46, B[0] + 26, B[1] - 44, k='red', bend=-0.3),
             arrow(C[0] - 40, C[1] - 82, C[0] + 44, C[1] - 80, k='red', bend=-0.3)]
    lab = [text(A[0], A[1] - 48, '8 turns', k='red', size=20, font='scrawl'),
           text(B[0], B[1] - 66, '4 turns', k='red', size=20, font='scrawl'),
           text(C[0], C[1] - 100, '1 turn', k='red', size=22, font='scrawl'),
           text(A[0], A[1] + 40, 'A: 1 m', k='ink', size=16),
           text(B[0], B[1] + 52, 'B: 2 m outside,', k='ink', size=16),
           text(B[0], B[1] + 72, '1 m inside', k='ink', size=16),
           text(C[0], C[1] + 90, 'C: 4 m', k='ink', size=16),
           text(140, 276, 'belt 1: 8 × 1 = 4 × 2', k='pen', size=17),
           text(400, 276, 'belt 2: 4 × 1 = 1 × 4', k='pen', size=17),
           text(320, 302, 'turns × diameter is the same on both ends of a belt', k='muted', size=15)]
    return svg(640, 314, rough(*parts) + ''.join(lab),
               'Pulley A turns 8 times a second, so B’s 2 m wheel turns 4 times; B’s 1 m wheel then drives the 4 m pulley C once a second')


Q.append(dict(
    n=10, orig=20, answer='A', topic='Pulleys & ratio',
    question=f"""<p>The diagram shows three pulleys driven by belts. {hl('Pulley A and the small, inner pulley at B are 1 m across', 'g', 1)}, {hl('the outer pulley at B is 2 m across', 'g', 2)} and pulley C is {hl('4 m across', 'g')}.</p>
{fig(Y, 'ps_q10_pulleys', 'Pulley A belted to the outer ring of B; the inner wheel of B belted to the big pulley C', 520)}
<p class="stem">Pulley A rotates at a rate of {hl('8 complete turns every second', 'g', 3)}. If the {hl('belts do not slip', 'y', 4)}, then
how many complete turns every second will pulley C make?</p>""",
    options={'A': '1', 'B': '4', 'C': '8', 'D': '16', 'E': '64'},
    notes=[(1, 'g', 'A and B’s inner wheel are the same size: 1 m.'),
           (2, 'g', 'Look at the picture: A’s belt goes round B’s <b>outer</b> (2 m) wheel, and C’s belt round B’s <b>inner</b> (1 m) wheel.'),
           (3, 'g', 'The starting speed.'),
           (4, 'y', 'No slipping: each belt moves the same length of rim on both pulleys it touches.')],
    steps=[
        f"""<p>First check which part of B each belt uses. A’s belt reaches the top and bottom of the big grey ring;
C’s belt starts from the small dark wheel in the middle. Both parts of B turn together.</p>""",
        f"""<p>Belt rule: a pulley twice as wide turns half as often. So <b>turns × diameter</b> is the same at both ends of a belt.</p>
{calc(f'A → B outer: 8 × 1 m = B × 2 m {ar()} B turns 4 times', f'B inner → C: 4 × 1 m = C × 4 m {ar()} C turns {boxed("1")} time')}
{_pulleys()}""",
        f"""{note('Rim length is π × diameter, but π is on both sides, so it cancels. Just use the diameters.', 'tip')}""",
    ],
    answer_text='1 turn a second: A to B halves the speed (8 → 4), B’s small wheel to C quarters it (4 → 1).',
    why={'B': '4 is B’s speed. You stopped one belt too early.',
         'C': '8 assumes every pulley turns at the same rate, ignoring their sizes.',
         'D': '16 multiplies by 2 instead of dividing: a bigger pulley turns <b>more slowly</b>, not faster.',
         'E': '64 = 8 × 2 × 4: multiplies by both size ratios, upside down twice.'},
    fast='Bigger wheel, fewer turns. 8 ÷ 2 = 4 (A onto B’s 2 m ring), then 4 ÷ 4 = 1 (B’s 1 m wheel onto C).',
))


# ---------------------------------------------------------------- 11 (Q24)
def _lanes():
    X = lambda m: 120 + m * 5
    parts, lab = [], []
    y0, rh = 46, 21
    for i in range(11):
        y = y0 + i * rh
        fixed = i < 2
        parts.append(rect(X(0), y, X(70) - X(0), rh - 4, k='ink', fill='b' if fixed else 'y', sw=1.4))
    lab += [text(110, y0 + 14, 'Roger', k='pen', size=16, anchor='end'),
            text(110, y0 + rh + 14, 'goalkeeper', k='pen', size=16, anchor='end'),
            text(110, y0 + 6 * rh + 10, '9 shared', k='orange', size=16, anchor='end'),
            text(110, y0 + 6 * rh + 30, 'places', k='orange', size=16, anchor='end'),
            text(X(0), y0 - 10, '0', k='muted', size=14), text(X(35), y0 - 10, '35', k='muted', size=14),
            text(X(70), y0 - 10, '70 min', k='muted', size=14)]
    yt, yb = y0 + 2 * rh, y0 + 11 * rh - 4
    ym = (yt + yb) / 2
    parts.append(path(f'M{X(70) + 8} {yt} q10 0 10 10 L{X(70) + 18} {ym - 10} q0 10 10 10 q-10 0 -10 10 L{X(70) + 18} {yb - 10} q0 10 -10 10',
                      k='red', sw=2.2))
    lab += [text(X(70) + 38, ym - 28, '9 × 70', k='red', size=18, anchor='start'),
            text(X(70) + 38, ym - 6, '= 630 minutes', k='red', size=18, anchor='start'),
            text(X(70) + 38, ym + 18, 'shared by', k='red', size=18, anchor='start'),
            text(X(70) + 38, ym + 40, '14 players', k='red', size=18, anchor='start'),
            text(X(35), y0 + 11 * rh + 22, '11 places on the pitch, each filled for 70 minutes', k='ink', size=16)]
    return svg(640, 316, rough(*parts) + ''.join(lab),
               'Eleven 70-minute bars: Roger and the goalkeeper fill two; the other nine, 630 minutes, are shared by 14 players')


Q.append(dict(
    n=11, orig=24, answer='B', topic='Sharing time',
    question=f"""<p>Hockey is an {hl('11-a-side', 'g', 1)} game, but a team may consist of up to 16 players, with unlimited
substitutions allowed throughout a match of {hl('70 minutes', 'g', 2)} duration.</p>
<p>Roger captains the Buccaneers hockey team. He has {hl('16 players', 'g', 3)} for today's match. He
will {hl('play the whole match himself, as will the goalkeeper', 'p', 4)}. He intends to rotate all the
others in such a way that each of them spends the {hl('same total amount of time', 'y', 5)} on the
pitch.</p>
<p class="stem">How much time should each player (except Roger and the goalkeeper) spend on the pitch
during today's match?</p>""",
    options={'A': '39 3/8 minutes', 'B': '45 minutes', 'C': '46 2/3 minutes', 'D': '48 1/8 minutes', 'E': '55 minutes'},
    notes=[(1, 'g', 'There are always 11 players on the pitch.'),
           (2, 'g', '11 places × 70 minutes = 770 “player-minutes” to fill.'),
           (3, 'g', 'The 16 includes Roger and the goalkeeper.'),
           (4, 'p', 'Two places are taken for the full 70 minutes, so only 9 places are shared.'),
           (5, 'y', 'Share those 9 places equally among the other 14 players.')],
    steps=[
        f"""<p>Picture 11 places on the pitch, each filled for 70 minutes:</p>{_lanes()}""",
        f"""{calc('Roger and the goalkeeper fill 2 places all match', '9 places × 70 min = 630 player-minutes', '16 − 2 = 14 players share them',
      f'630 ÷ 14 = {boxed("45 minutes")}')}
{note('630 ÷ 14: halve both first, 315 ÷ 7 = 45.', 'tip')}""",
    ],
    answer_text='45 minutes each: 9 shared places × 70 minutes = 630, split between 14 players.',
    why={'A': '39⅜ = 630 ÷ 16: shares the 9 places among all 16 players, including Roger and the goalkeeper.',
         'C': '46⅔ = 700 ÷ 15: only takes Roger out, forgetting the goalkeeper also plays all match.',
         'D': '48⅛ = 770 ÷ 16: shares all 11 places among all 16 players.',
         'E': '55 = 770 ÷ 14: forgets to take Roger’s and the goalkeeper’s 140 minutes out first.'},
    fast='9 shared places × 70 = 630 minutes, ÷ 14 players = 45.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _zones():
    Z = lambda h: 60 + (h + 8) * 30
    parts = [line(Z(-8), 70, Z(9), 70, k='ink', w=2)]
    lab = [text(Z(-8) - 6, 146, 'hours from London', k='muted', size=14, anchor='start')]
    for name, h, col in (('Vancouver', -8, 'muted'), ('New York', -5, 'pen'), ('London', 0, 'ink'), ('Tokyo', 9, 'red')):
        parts.append(circle(Z(h), 70, 6, k=col, fill='paper', sw=2.4))
        lab.append(text(Z(h), 98, name, k=col, size=16))
        lab.append(text(Z(h), 118, f'{h:+d}' if h else '0', k=col, size=15))
    parts.append(brace(Z(-5), Z(9), 52, '', k='orange', down=False))
    lab.append(text((Z(-5) + Z(9)) / 2, 30, '5 + 9 = 14 hours apart', k='orange', size=18, font='scrawl'))
    T = lambda h: 60 + (h - 12) * 25
    yl = 220
    parts.append(line(T(12), yl, T(32), yl, k='ink', w=2, head=True))
    for h, s in ((12, 'Wed 12:00'), (16, '16:00'), (20, '20:00'), (24, 'midnight'), (28, 'Thu 04:00'), (32, '08:00')):
        parts.append(line(T(h), yl - 6, T(h), yl + 6, k='ink', w=1.6))
        lab.append(text(T(h), yl + 24, s, k='muted', size=14))
    lab.append(text(T(32) + 12, yl + 44, 'London time', k='muted', size=14, anchor='end'))
    parts += [circle(T(14.5), yl, 7, k='green', fill='g', sw=2.4), circle(T(28.5), yl, 7, k='red', fill='p', sw=2.4),
              arrow(T(14.5) + 8, yl - 14, T(28.5) - 8, yl - 14, k='red', bend=-0.12)]
    lab += [text(T(14.5), yl + 64, 'expected: 23.30 Tokyo', k='green', size=15),
            text(T(14.5), yl + 82, '= 14.30 Wed London', k='green', size=15),
            text(T(28.5), yl + 64, 'rang: 23.30 New York', k='red', size=15),
            text(T(28.5), yl + 82, '= 04.30 Thu London', k='red', size=15),
            text((T(14.5) + T(28.5)) / 2, yl - 50, '14 hours late', k='red', size=22, font='scrawl')]
    return svg(640, 318, rough(*parts) + ''.join(lab),
               'Time zones: New York is 5 hours behind London and Tokyo 9 ahead, so the same clock time is 14 hours apart; on a London timeline the expected call is 14.30 Wednesday and the real call 04.30 Thursday')


Q.append(dict(
    n=12, orig=25, answer='C', topic='Time zones',
    question=f"""<p>Julie lives in London. She has three daughters; April, who lives in New York (where the
local time is {hl('5 hours behind London', 'g', 1)}), May, who lives in Vancouver ({hl('8 hours behind London', 'g', 2)}), and June, who lives in Tokyo ( {hl('9 hours ahead of London', 'g', 3)}). They all communicate
with each other regularly.</p>
<p>Last week April received a text message from May that said "call me on Wednesday at
{hl('23.30 your time', 'y', 4)}." Unfortunately, the message had been sent to April by mistake and was
{hl('intended for June', 'p', 5)}.</p>
<p class="stem">How much later than expected did {hl("May's phone", 'b', 6)} eventually ring?</p>""",
    options={'A': '12 hours', 'B': '13 hours', 'C': '14 hours', 'D': '17 hours', 'E': '22 hours'},
    notes=[(1, 'g', 'New York = London − 5 h.'),
           (2, 'g', 'Vancouver = London − 8 h. That’s May’s home, but you don’t actually need it.'),
           (3, 'g', 'Tokyo = London + 9 h.'),
           (4, 'y', '“Your time” means the reader’s time. June would call at 23.30 <b>Tokyo</b> time; April calls at 23.30 <b>New York</b> time.'),
           (5, 'p', 'Expected = June’s 23.30. What happened = April’s 23.30.'),
           (6, 'b', 'Compare the two moments on one clock (London is easiest).')],
    steps=[
        f"""<p>Put both moments into London time:</p>
{calc(f'expected: Wed 23.30 in Tokyo − 9 h {ar()} Wed 14.30 London', f'actual: Wed 23.30 in New York + 5 h {ar()} Thu 04.30 London')}""",
        f"""{_zones()}""",
        f"""{calc(f'Wed 14.30 → Thu 04.30 = 9½ + 4½ = {boxed("14 hours")}')}
{note('Shortcut: the same clock time in two places is as far apart as the zones are. Tokyo is 9 ahead and New York 5 behind, so 9 + 5 = 14 hours. Tokyo reaches 23.30 first, so the call is late.', 'tip')}""",
    ],
    answer_text='14 hours: 23.30 in New York happens 14 hours after 23.30 in Tokyo.',
    why={'A': '12 hours doesn’t match any pair of zones. You get it by mixing up gaps, e.g. 9 + 3 (using the 3-hour New York to Vancouver gap).',
         'B': '13 hours = 5 + 8, the gaps for New York and Vancouver. May lives in Vancouver, but the call times are set in Tokyo and New York.',
         'D': '17 hours = 8 + 9, the gap between Vancouver and Tokyo. That’s how far apart May and June are, not how late the call was.',
         'E': '22 hours = 5 + 8 + 9: adds up every gap.'},
    fast='Same clock reading in Tokyo (+9) and New York (−5): 9 + 5 = 14 hours apart.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _metallica():
    pos = {'P': (118, 196), 'Q': (139, 303), 'R': (280, 271), 'W': (323, 111), 'V': (409, 131), 'U': (485, 100),
           'S': (430, 176), 'T': (540, 207)}
    roads = [('P', 'W', 63, (205, 140)), ('P', 'R', 47, (210, 222)), ('P', 'Q', 28, (114, 256)), ('Q', 'R', 30, (205, 307)),
             ('R', 'S', 44, (368, 244)), ('W', 'V', 28, (362, 108)), ('V', 'U', 23, (444, 102)), ('V', 'S', 12, (432, 150)),
             ('S', 'T', 28, (490, 214))]
    tree = {'PR', 'QR', 'RS', 'WV', 'VU', 'VS', 'ST'}
    dist = {'P': 119, 'Q': 102, 'R': 72, 'S': 28, 'U': 63, 'V': 40, 'W': 68}
    lpos = {'P': (60, 192), 'Q': (148, 324), 'R': (268, 298), 'W': (298, 96), 'V': (376, 114), 'U': (497, 106), 'S': (440, 202)}
    parts, lab = [], []
    for a, b, km, (lx, ly) in roads:
        on = (a + b) in tree
        parts.append(line(*pos[a], *pos[b], k='orange' if on else 'muted', w=3.4 if on else 1.8, dash=not on))
        lab.append(text(lx, ly, km, k='muted', size=14, anchor='start' if km == 12 else ('end' if (a, b) == ('P', 'Q') else 'middle')))
    for t, (x, y) in pos.items():
        parts.append(circle(x, y, 7 if t == 'T' else 5, k='red' if t == 'T' else 'ink', fill='p' if t == 'T' else 'ink', sw=2))
    for t, (lx, ly) in lpos.items():
        lab.append(text(lx, ly, t, k='ink', size=18, font='print', anchor='start'))
        lab.append(text(lx + 19, ly, dist[t], k='red', size=18, anchor='start'))
    lab += [text(552, 232, 'T', k='red', size=18, font='print', anchor='start'),
            text(330, 30, 'red = shortest distance from T', k='red', size=17),
            text(330, 52, 'orange = the roads those shortest routes use', k='orange', size=15)]
    return svg(620, 340, rough(*parts) + ''.join(lab),
               'Map redrawn with the shortest distance from T to every town: S 28, V 40, U 63, W 68, R 72, Q 102, P 119')


Q.append(dict(
    n=13, orig=26, answer='D', topic='Maps & distance charts',
    question=f"""<p>This is a map of the island of Metallica showing the eight main towns (labelled P - W) and
the roads that connect them, together with a chart giving the {hl('shortest distance (in km) by road between each pair of towns', 'y', 1)}:</p>
{fig(Y, 'ps_q13_map', 'Map: roads P-W 63, P-R 47, P-Q 28, Q-R 30, R-S 44, W-V 28, V-U 23, V-S 12, S-T 28', 470)}
{fig(Y, 'ps_q13_chart', 'Triangular distance chart for Copper, Gold, Iron, Lead, Nickel, Silver, Tin and Zinc', 360)}
<p class="stem">Which of the towns on the map is {hl('Nickel', 'b', 2)}?</p>""",
    options={'A': 'Q', 'B': 'R', 'C': 'S', 'D': 'T', 'E': 'W'},
    notes=[(1, 'y', 'Shortest route <b>along the roads</b>, often passing through other towns.'),
           (2, 'b', 'Read Nickel’s seven distances (along its row and down its column), then find the town with exactly those distances.')],
    steps=[
        f"""<p>Nickel’s row (to Copper, Gold, Iron, Lead) and column (to Silver, Tin, Zinc):</p>
{calc('102, 28, 119, 40, 68, 63, 72', f'nearest town: 28 km {ar()} furthest: 119 km')}""",
        f"""<p>119 is the <b>biggest number in the whole chart</b>, so Nickel and Iron are the two towns furthest apart.
On the map those are the two ends, T and P:</p>
{calc('T → S → R → P = 28 + 44 + 47 = 119 ✓', f'so Nickel is T or P. P is 47 km from R, but Nickel has no 47 {ar()} Nickel = T')}""",
        f"""<p>Check: shortest distances from T to every town.</p>{_metallica()}
{calc(f'from T: 28, 40, 63, 68, 72, 102, 119 = exactly Nickel’s list {tick()} {ar()} {boxed("T")}')}
{note('Shortest routes can be roundabout: T to W is 28 + 12 + 28 = 68 (via S and V), and T to Q is 28 + 44 + 30 = 102.', 'check')}""",
    ],
    answer_text='T: its distances to the other towns (28, 40, 63, 68, 72, 102, 119) match Nickel’s.',
    why={'A': 'Q’s two nearest towns are P (28) and R (30). Nickel has nothing 30 km away. (Q is Copper.)',
         'B': 'R has three towns within 47 km (Q 30, S 44, P 47). Nickel has no 30, 44 or 47. (R is Zinc.)',
         'C': 'S is only 12 km from V, but Nickel’s nearest town is 28 km away. (S is Gold.)',
         'E': 'W fits 28, 40, 63 and 68, but its furthest town (Q) is only 91 km away. Nickel has 102 and 119. (W is Silver.)'},
    fast='Biggest number, 119, = the two far ends of the island, T and P. Nickel has no 47 (that’s P to R), so Nickel = T. Check T–S = 28 ✓.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _jan(x0, y0, start, title, ok):
    cw, ch = 34, 28
    parts, lab = [], []
    lab.append(text(x0 + 3.5 * cw, y0 - 30, title, k='green' if ok else 'red', size=18, font='scrawl'))
    for i, d in enumerate('MTWTFSS'):
        lab.append(text(x0 + i * cw + cw / 2, y0 - 8, d, k='red' if i == 4 else 'muted', size=15))
    fridays = 0
    for day in range(1, 32):
        idx = start + day - 1
        r, c = idx // 7, idx % 7
        x, y = x0 + c * cw, y0 + r * ch
        fri = c == 4
        fridays += fri
        parts.append(rect(x + 1, y + 1, cw - 2, ch - 2, k='ink' if fri else 'muted',
                          fill=('g' if ok else 'p') if fri else ('y' if day in (1, 2, 3, 29, 30, 31) else 'paper'), sw=1.2))
        lab.append(text(x + cw / 2, y + 19, day, k='ink', size=14, font='print'))
    rows = (start + 31 + 6) // 7
    lab.append(text(x0 + 3.5 * cw, y0 + rows * ch + 24, f'{fridays} Fridays {"✓" if ok else "✗"}', k='green' if ok else 'red', size=18))
    return parts, lab


def _januaries():
    p1, l1 = _jan(40, 60, 2, '1st = Wednesday', True)
    p2, l2 = _jan(350, 60, 5, '31st = Monday, so 1st = Saturday', False)
    lab = l1 + l2 + [text(320, 316, 'yellow = days 1, 2, 3 and 29, 30, 31 (the only weekdays that get a 5th turn)', k='muted', size=14)]
    return svg(640, 328, rough(*p1, *p2) + ''.join(lab),
               'Two January calendars: starting on Wednesday gives five Fridays; ending on Monday means starting on Saturday, with only four Fridays')


Q.append(dict(
    n=14, orig=30, answer='E', topic='Calendars & days of the week',
    question=f"""<p>In a particular year the month of January ({hl('which has 31 days', 'g', 1)}) contains {hl('five Fridays', 'y', 2)}.</p>
<p class="stem">Which one of the following {hl('could <b>NOT</b> be true', 'b', 3)}?</p>""",
    options={'A': 'The first Friday in the month occurs before the 4th.', 'B': 'The 1st of January is a Wednesday.',
             'C': 'There are only 4 Tuesdays.', 'D': 'There are also 5 Sundays.', 'E': 'The 31st of January is a Monday.'},
    notes=[(1, 'g', '31 days = 4 whole weeks (28 days) + 3 extra days.'),
           (2, 'y', 'Only the weekdays of the 1st, 2nd and 3rd get a fifth turn. So one of those three days must be a Friday.'),
           (3, 'b', 'Four statements can happen in some year; find the one that never can.')],
    steps=[
        f"""<p>31 = 28 + 3. The 29th, 30th and 31st fall on the same weekdays as the 1st, 2nd and 3rd.
Those three weekdays appear <b>5 times</b>; every other weekday appears 4 times.</p>""",
        f"""<p>So a Friday is on the 1st, 2nd or 3rd. Only three Januaries are possible:</p>
{calc('Friday 1st: five Fridays, Saturdays, Sundays', 'Thursday 1st: five Thursdays, Fridays, Saturdays', 'Wednesday 1st: five Wednesdays, Thursdays, Fridays')}""",
        f"""<p>Test each statement:</p>
{calc(f'A: first Friday is the 1st, 2nd or 3rd {tick()} always', f'B: Wednesday 1st is one of the three {tick()}',
      f'C: Tuesday never gets a fifth turn {tick()} always', f'D: Friday 1st gives five Sundays {tick()}',
      f'E: 31st Monday {ar()} 3rd Monday (31 − 28) {ar()} 1st Saturday {cross()}')}
{_januaries()}
{calc(f'a January starting on Saturday has only 4 Fridays {ar()} {boxed("E")}')}""",
    ],
    answer_text='E: if the 31st is a Monday, the 1st is a Saturday, and there are only four Fridays.',
    why={'A': 'Always true: the first Friday must be the 1st, 2nd or 3rd.',
         'B': 'Possible: starting on Wednesday gives five Wednesdays, Thursdays and Fridays.',
         'C': 'Always true: Tuesday can never be one of the three extra days.',
         'D': 'Possible: if the 1st is a Friday, then Friday, Saturday and Sunday all appear five times.'},
    fast='31st Monday ⇒ 3rd Monday ⇒ 1st Saturday ⇒ five Saturdays, Sundays and Mondays only. No fifth Friday.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _restaurant():
    cw, x0, y0 = 58, 110, 40
    parts, lab = [], []
    for i, d in enumerate(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']):
        lab.append(text(x0 + i * cw + cw / 2, y0 - 10, d, k='muted', size=15))
        for r, open_ in enumerate((i <= 4, 1 <= i <= 5)):
            x, y = x0 + i * cw, y0 + r * 40
            parts.append(rect(x + 2, y + 2, cw - 4, 36, k='ink' if open_ else 'muted', fill='g' if open_ else 'paper', sw=1.4))
            lab.append(text(x + cw / 2, y + 26, '20' if open_ else '–', k='ink' if open_ else 'muted', size=16))
    lab += [text(x0 - 10, y0 + 26, 'lunch', k='ink', size=16, anchor='end'),
            text(x0 - 10, y0 + 66, 'dinner', k='ink', size=16, anchor='end'),
            text(x0 + 7 * cw + 14, y0 + 30, '10 openings', k='red', size=19, font='scrawl', anchor='start'),
            text(x0 + 7 * cw + 14, y0 + 54, '× 20 = 200', k='red', size=17, anchor='start'),
            text(x0 + 7 * cw + 14, y0 + 74, 'meals a week', k='red', size=17, anchor='start')]
    X = lambda k: 40 + k * 5.0
    yb = 170
    for a, b, f, s in ((0, 54, 'b', 'wages £54 000'), (54, 90, 'o', 'rent £36 000'), (90, 99, 'v', '£9k')):
        parts.append(rect(X(a), yb, X(b) - X(a), 36, k='ink', fill=f, sw=1.6))
        lab.append(text((X(a) + X(b)) / 2, yb + 24, s, k='ink', size=16 if b - a > 20 else 14))
    lab += [text(X(99) + 10, yb + 24, '= £99 000', k='ink', size=17, anchor='start'),
            text(320, yb + 66, '£99 000 ÷ 9000 meals = £11, plus £5 food = £16', k='green', size=19, font='scrawl')]
    return svg(640, 252, rough(*parts) + ''.join(lab),
               'Week grid: lunch Monday to Friday and dinner Tuesday to Saturday make 10 openings of 20 meals; yearly costs of 99 000 pounds shared over 9000 meals')


Q.append(dict(
    n=15, orig=31, answer='C', topic='Costs & break-even',
    question=f"""<p>A small restaurant is open for {hl('45 weeks', 'g', 1)} each year. It employs 6 people at {hl('total wages of £1200 per week', 'g', 2)} (they are not paid when the restaurant is closed). It is open for {hl('lunch on Monday to Friday and dinner on Tuesday to Saturday', 'y', 3)} and on average {hl('20 people eat at each opening', 'g', 4)}. The owners pay rental on the premises of {hl('£36 000 per year', 'g')}. Other
expenses (insurance, gas electricity, water, rates etc.) come to {hl('£9000 per year', 'g')}. The cost
of buying food works out at {hl('£5 per meal served', 'p', 5)}.</p>
<p class="stem">How much must the owner charge for each meal to {hl('cover expenses', 'b', 6)}?</p>""",
    options={'A': '£ 10', 'B': '£ 11', 'C': '£ 16', 'D': '£ 22', 'E': '£ 27'},
    notes=[(1, 'g', 'Open (and paying wages) for 45 weeks, not 52.'),
           (2, 'g', '“Total” wages: £1200 a week is for all 6 people together. Don’t multiply by 6.'),
           (3, 'y', '5 lunches + 5 dinners = <b>10 openings</b> a week.'),
           (4, 'g', '20 meals at every opening.'),
           (5, 'p', 'Food is an extra £5 on top of each meal’s share of the other costs. Easy to forget!'),
           (6, 'b', 'Break even: money in = money out.')],
    steps=[
        f"""<p>How many meals a year?</p>{_restaurant()}
{calc('10 openings × 20 = 200 meals a week', '200 × 45 weeks = 9000 meals a year')}""",
        f"""<p>The yearly bills (apart from food):</p>
{calc('wages: 45 × £1200 = £54 000', 'rent: £36 000', 'other: £9000', 'total = £99 000')}""",
        f"""{calc('share per meal: 99 000 ÷ 9000 = £11', f'plus food: £11 + £5 = {boxed("£16")}')}
{note('Knock the thousands off first: 99 ÷ 9 = 11.', 'tip')}""",
    ],
    answer_text='£16 a meal: £11 towards wages, rent and bills, plus £5 of food.',
    why={'A': '£10 leaves out the wages: 45 000 ÷ 9000 = £5, plus £5 food.',
         'B': '£11 covers the wages, rent and bills but forgets the £5 of food in every meal.',
         'D': '£22 counts only 5 openings a week (4500 meals) and also forgets the food.',
         'E': '£27 counts only 5 openings a week: 99 000 ÷ 4500 = £22, + £5. Lunch and dinner are separate openings, so it’s 10.'},
    fast='10 openings × 20 × 45 = 9000 meals. 54 000 + 36 000 + 9000 = 99 000, so £11 a meal, + £5 food = £16.',
))


# ---------------------------------------------------------------- 16 (Q32)
_MAPS = {
    'A': dict(box=(143.7, 205.1), nodes={'a': (143.7, 205.1), 'b': (197.8, 205.1), 'c': (143.7, 260.8), 'd': (197.8, 260.8),
                                          'e': (170.8, 232.9), 'f': (170.8, 287.7)},
              edges=[('a', 'b'), ('a', 'c'), ('c', 'f'), ('f', 'd'), ('d', 'b'), ('a', 'e'), ('e', 'd'), ('c', 'e')]),
    'B': dict(box=(357.1, 199.9), nodes={'a': (405.1, 199.9), 'b': (453.3, 199.9), 'c': (405.1, 248.1), 'd': (453.3, 248.1),
                                          'e': (405.1, 296.0), 'f': (453.3, 296.0)},
              edges=[('c', 'a'), ('a', 'b'), ('b', 'd'), ('c', 'd'), ('d', 'f'), ('f', 'e'), ('e', 'c'), ('e', 'a', 48, 48)]),
    'C': dict(box=(141.7, 330.2), nodes={'t': (189.7, 330.2), 'l': (141.7, 380.2), 'r': (237.6, 380.2), 'm': (189.7, 406.3),
                                          'p': (159.6, 416.8), 'q': (219.7, 416.8)},
              edges=[('t', 'r', 48, 48), ('r', 'q', 48, 48), ('q', 'p', 48, 48), ('p', 'l', 48, 48), ('l', 't', 48, 48),
                     ('r', 'm', 48, 26), ('m', 'l', 48, 26), ('t', 'm'), ('m', 'q')]),
    'D': dict(box=(365.1, 333.2), nodes={'t': (423.0, 333.2), 'r': (452.1, 362.3), 'm': (423.0, 391.3), 'l': (394.0, 362.3),
                                          'x': (365.1, 391.1), 'b': (423.0, 449.1)},
              edges=[('t', 'r', 29, 29), ('r', 'm', 29, 29), ('m', 'l', 29, 29), ('l', 't', 29, 29), ('b', 'x', 58, 58),
                     ('x', 't', 58, 58), ('x', 'l'), ('m', 'b')]),
    'E': dict(box=(139.7, 486.6), nodes={'t': (182.8, 486.6), 'm': (182.8, 524.1), 'n': (182.8, 561.6), 'b': (182.8, 600.3),
                                          'r': (225.9, 524.1), 'l': (139.7, 524.1)},
              edges=[('t', 'l'), ('l', 'b'), ('r', 'n'), ('t', 'm'), ('m', 'n'), ('n', 'b'), ('l', 'm'), ('t', 'r')]),
}


def _networks():
    sc = 1.0
    parts, lab = [], []
    for i, (name, m) in enumerate(_MAPS.items()):
        xs = [p[0] for p in m['nodes'].values()]
        ys = [p[1] for p in m['nodes'].values()]
        w = (max(xs) - min(xs)) * sc
        if name in 'B':
            w = (max(xs) - 357.1) * sc
        ox = 10 + i * 128 + (118 - w) / 2
        oy = 40
        bx = m['box'][0]
        by = min(ys)
        P = lambda q: (round(ox + (q[0] - bx) * sc, 1), round(oy + (q[1] - by) * sc, 1))
        deg = {k: 0 for k in m['nodes']}
        for e in m['edges']:
            a, b = e[0], e[1]
            deg[a] += 1
            deg[b] += 1
            (x1, y1), (x2, y2) = P(m['nodes'][a]), P(m['nodes'][b])
            if len(e) == 4:
                parts.append(path(f'M{x1} {y1} A{e[2] * sc:.1f} {e[3] * sc:.1f} 0 0 1 {x2} {y2}', k='ink', sw=2))
            else:
                parts.append(line(x1, y1, x2, y2, k='ink', w=2))
        bad = name == 'C'
        for k, q in m['nodes'].items():
            x, y = P(q)
            four = deg[k] == 4
            lab.append(circle(x, y, 10, k='red' if four else 'ink', fill='p' if four else 'paper', sw=2))
            lab.append(text(x, y + 5, deg[k], k='red' if four else 'ink', size=14, font='print', weight='bold'))
        links = len(m['edges'])
        cx = 10 + i * 128 + 59
        lab.append(text(cx, 22, name, k='ink', size=20, font='print', weight='bold'))
        lab.append(text(cx, 190, f'{links} links', k='red' if bad else 'green', size=19, font='scrawl'))
        lab.append(text(cx, 212, '4 3 3 3 3 2' if bad else '3 3 3 3 2 2', k='red' if bad else 'ink', size=15))
    return svg(650, 226, rough(*parts) + ''.join(lab),
               'The five maps redrawn with the number of links at each station: A, B, D and E have 8 links (3,3,3,3,2,2); C has 9 links and a station with 4')


Q.append(dict(
    n=16, orig=32, answer='C', topic='Networks',
    question=f"""<p>Boland City has just installed a new tram system. Several artists have been asked to
come up with a map of the system which, whilst it {hl('may not show the exact relative positions of the stations', 'p', 1)}, {hl('shows the connections between them correctly', 'y', 2)}.</p>
<p>The five maps are shown below (the names of the stations are not marked).</p>
<p>Four of the artists drew possible maps, but the fifth got the connections wrong. Which
map below is {hl('based on incorrect connections', 'b', 3)}?</p>
{fig(Y, 'ps_q16_maps', 'Five network maps A to E, each with six stations joined by straight and curved lines', 470)}""",
    options={'A': 'map A', 'B': 'map B', 'C': 'map C', 'D': 'map D', 'E': 'map E'},
    notes=[(1, 'p', 'Lines can be bent, stretched, curved or moved around. Shapes and distances don’t matter.'),
           (2, 'y', 'Only “what joins to what” matters, like the London Underground map.'),
           (3, 'b', 'Four maps show the same network; one shows a different network.')],
    steps=[
        f"""<p>Redrawing a network can’t change three things: the number of <b>stations</b>, the number of <b>links</b>
(track between two stations), and <b>how many links meet at each station</b>. Count them.</p>""",
        f"""<p>Number in each circle = links at that station:</p>{_networks()}""",
        f"""{calc(f'A, B, D, E: 6 stations, 8 links, stations 3, 3, 3, 3, 2, 2 {tick()}',
      f'C: 6 stations, <b>9</b> links, and one station with <b>4</b> {cross()}')}
<p>C can’t be the same network as the others {ar()} {boxed('C')}</p>
{note('Watch the lines that pass through a station. In A, the diagonal from the top-left corner goes through the middle station: that’s two links, not one. In C, the curve from left to right passes through the bottom-middle station, which also has the vertical line and the short line: 4 links.', 'check')}""",
    ],
    answer_text='Map C: it has 9 links and a station with 4 links; the other four maps all have 8 links (3, 3, 3, 3, 2, 2).',
    why={'A': 'Same network as B, D and E: 8 links, with 3, 3, 3, 3, 2, 2 at the stations.',
         'B': 'Same network: the big curve is just a bent track from the bottom-left station to the top-left one.',
         'D': 'Same network: the small circle is four tracks between four stations, the big arc two more.',
         'E': 'Same network: 8 straight links, with 3, 3, 3, 3, 2, 2 at the stations.'},
    fast='Count links: A, B, D and E have 8, C has 9 (its bottom-middle station has 4). C is the odd one out.',
))
