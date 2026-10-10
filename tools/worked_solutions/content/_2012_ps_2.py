from wslib import *

Y = 2012
Q = []


# ---------------------------------------------------------------- 9 (Q19)
def _salt():
    s = 4.2  # px per percent
    x0 = 100
    parts, lab = [], []
    for i, (who, low, k) in enumerate((('Men', 11, 'pen'), ('Women', 30, 'orange'))):
        y = 40 + i * 80
        parts.append(rect(x0, y, low * s, 40, k='ink', fill='paper', sw=1.6))
        parts.append(rect(x0 + low * s, y, (100 - low) * s, 40, k='ink', fill='p', sw=1.6))
        lab += [text(x0 - 10, y + 26, who, k=k, size=18, anchor='end'),
                text(x0 + low * s / 2, y + 26, f'{low}%', k='muted', size=15),
                text(x0 + low * s + (100 - low) * s / 2, y + 26, f'above 6 g: {100 - low}%', k='ink', size=17)]
    lab += [text(x0 + 11 * s / 2, 30, '6 g or less', k='muted', size=13),
            text(x0 + 50 * s, 200, 'equal numbers, so average: (89 + 70) ÷ 2 = 79.5 → 80%', k='red', size=17)]
    return svg(540, 214, rough(*parts) + ''.join(lab),
               'Bars to 100 percent: men 11 percent at or below 6 g and 89 percent above; women 30 percent at or below and 70 percent above; average 79.5 percent')


Q.append(dict(
    n=9, orig=19, answer='D', topic='Tables & percentages',
    question=f"""<p>The table below shows the {hl('cumulative', 'y', 1)} percentage distribution of salt consumption in England in
2004.</p>
<p><b>Percentage distribution of estimated salt intake (g/day)</b></p>
{table([['3 g or less', '1', '3'], [hl('6 g or less', 'g', 2), hl('11', 'g'), hl('30', 'g')], ['9 g or less', '44', '73'],
        ['12 g or less', '68', '93'], ['15 g or less', '92', '99'], ['18 g or less', '96', '100']],
       head=['', 'Men', 'Women'])}
<p class="stem">Assuming {hl('equal numbers of men and women', 'y', 3)} in the population, what percentage of all people
consumed {hl('above', 'p', 4)} the recommended level of 6g per day? (Give your answer to the nearest 1%)</p>""",
    options={'A': '20 %', 'B': '59 %', 'C': '70 %', 'D': '80 %', 'E': '89 %'},
    notes=[(1, 'y', 'Cumulative = each row is a running total. “6 g or less” already includes the “3 g or less” people.'),
           (2, 'g', 'The only row you need.'),
           (3, 'y', 'Equal numbers, so you can simply average the two percentages.'),
           (4, 'p', '<b>Above</b> 6 g is everyone <b>not</b> in the “6 g or less” row: 100 minus it.')],
    steps=[
        f"""<p>Above 6 g = 100% minus the “6 g or less” figure:</p>
{calc('men: 100 − 11 = <b>89%</b>', 'women: 100 − 30 = <b>70%</b>')}{_salt()}""",
        f"""{calc(f'(89 + 70) ÷ 2 = 159 ÷ 2 = 79.5 {ar()} nearest 1% = {boxed("80%")}')}
{note('Don’t add up rows! The table is already cumulative, so one row tells you everything.', 'trap')}""",
    ],
    answer_text='80%: men 89% and women 70% are above 6 g, and with equal numbers the average is 79.5%.',
    why={'A': '20% is the average of 11 and 30: the people at or <b>below</b> 6 g, the wrong side.',
         'B': '59% averages the “9 g or less” row (44 and 73). Wrong row, wrong side.',
         'C': '70% is the women only.',
         'E': '89% is the men only.'},
    fast='Men above 6 g: 89. Women: 70. Average 79.5, so 80%.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _discs():
    parts, lab = [], []
    h = 150  # px per 2 GB
    sizes = [('1.5', 'b'), ('1.2', 'g'), ('1.0', 'o'), ('0.8', 'g'), ('0.7', 'o'), ('0.5', 'b')]
    lab.append(text(20, 26, 'programs, biggest first (GB):', k='ink', size=16, anchor='start'))
    x = 250
    for v, f in sizes:
        w = float(v) * 40
        parts.append(rect(x, 10, w, 24, k='ink', fill=f, sw=1.4))
        lab.append(text(x + w / 2, 27, v, k='ink', size=13))
        x += w + 6
    discs = [[('1.5', 'b', 1), ('0.5', 'b', 6)], [('1.2', 'g', 2), ('0.8', 'g', 4)], [('1.0', 'o', 3), ('0.7', 'o', 5)], []]
    for i, stack in enumerate(discs):
        x0, ybase = 70 + i * 140, 230
        parts.append(rect(x0, ybase - h, 80, h, k='ink', fill='paper', sw=2))
        lab.append(text(x0 + 40, ybase + 22, f'disc {i + 1}', k='muted', size=15))
        y = ybase
        for v, f, order in stack:
            hh = float(v) / 2 * h
            parts.append(rect(x0 + 4, y - hh, 72, hh, k='ink', fill=f, sw=1.4))
            lab.append(text(x0 + 40, y - hh / 2 + 6, f'#{order}: {v}', k='ink', size=14))
            y -= hh
    lab.append(text(330, 278, 'each one goes in the FIRST disc with room', k='red', size=17))
    return svg(620, 290, rough(*parts) + ''.join(lab),
               'Programs sorted biggest first, 1.5, 1.2, 1.0, 0.8, 0.7, 0.5 GB, dropped into the first disc with room: disc 1 gets 1.5 and 0.5, disc 2 gets 1.2 and 0.8, disc 3 gets 1.0 and 0.7')


Q.append(dict(
    n=10, orig=20, answer='B', topic='Same method',
    question=f"""<p>A software manufacturer wants to fit some computer programs on to four 2GB discs. He {hl('reorders the programs in order of decreasing size', 'y', 1)} and {hl('places the next programs to be saved in the first available disc that can take that program', 'y', 2)}.</p>
<p class="stem">Which one of the following uses the {hl('same method', 'b', 3)} as that above?</p>""",
    options={'A': 'A plumber is using lengths of pipe 12 feet long and wishes to cut some lengths. He looks at the combination of lengths to add up to 12 feet and cuts these lengths first. For the remainder he cuts the next length from the first available pipe that is long enough.',
             'B': 'A plumber is using lengths of pipe 12 feet long and wishes to cut some lengths. He reorders the lengths in descending order and cuts the next length from the first available pipe that is long enough.',
             'C': 'A plumber is using lengths of pipe 12 feet long and wishes to cut some lengths. He takes the lengths in the order listed and cuts the next length from the first available pipe that is long enough.',
             'D': 'A plumber is using lengths of pipe 12 feet long and wishes to cut some lengths. He alternately cuts the longest and shortest pieces still needed from the first available pipe which is long enough.',
             'E': 'A plumber is using lengths of pipe 12 feet long and wishes to cut some lengths. He reorders the lengths in ascending order and cuts the next length from the first available pipe that is long enough.'},
    notes=[(1, 'y', 'Rule 1: sort them, <b>biggest first</b>.'),
           (2, 'y', 'Rule 2: each one goes into the <b>first</b> container with enough room.'),
           (3, 'b', 'Discs ↔ pipes, programs ↔ lengths. The match must keep <b>both</b> rules.')],
    steps=[
        f"""<p>The method has two rules. Picture it with some example programs:</p>{_discs()}""",
        f"""<p>Now check each plumber against both rules:</p>
{table([['A', 'no: hunts for combinations that make 12 ft', 'yes (for the rest)'],
        ['B', '<b>yes: descending order</b>', '<b>yes</b>'],
        ['C', 'no: order listed', 'yes'],
        ['D', 'no: longest, shortest, longest…', 'yes'],
        ['E', 'no: ascending = smallest first', 'yes']],
       head=['', 'Rule 1: biggest first?', 'Rule 2: first one with room?'])}
{calc(f'only B keeps both rules {ar()} {boxed("B")}')}""",
    ],
    answer_text='B: sort the lengths biggest first, then cut each from the first pipe that is long enough.',
    why={'A': 'A looks for combinations that add up to exactly 12 feet first. That is a different plan, and nothing is sorted.',
         'C': 'C keeps the list order instead of sorting biggest first.',
         'D': 'D alternates longest and shortest pieces, which is not decreasing order.',
         'E': 'E sorts the right way round for the wrong job: ascending is smallest first.'},
    fast='Two rules: biggest first + first container with room. Every option has the second rule; only B has “descending order”.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _jug():
    parts, lab = [], []
    steps = [('buy', -80, 'pen'), ('sell', 100, 'green'), ('buy back', -110, 'pen'), ('sell', 120, 'green')]
    bal = 0
    for i, (what, amt, k) in enumerate(steps):
        x = 30 + i * 150
        bal += amt
        parts.append(rect(x, 40, 120, 70, k=k, fill='g' if amt > 0 else 'p', sw=2, rx=10))
        lab += [text(x + 60, 66, what, k='ink', size=17),
                text(x + 60, 96, f'{"+" if amt > 0 else "−"}£{abs(amt)}', k='green' if amt > 0 else 'red', size=22, font='scrawl'),
                text(x + 60, 140, f'running total: {"+" if bal > 0 else "−"}£{abs(bal)}', k='ink', size=15)]
        if i < 3:
            parts.append(arrow(x + 122, 75, x + 148, 75, k='muted', bend=0, w=1.8))
    lab += [text(110, 180, 'in: 100 + 120 = 220', k='green', size=18), text(320, 180, 'out: 80 + 110 = 190', k='pen', size=18),
            text(530, 180, 'profit £30', k='red', size=22, font='scrawl')]
    return svg(630, 196, rough(*parts) + ''.join(lab),
               'Four deals: buy for 80, sell for 100, buy back for 110, sell for 120; running total ends at plus 30')


Q.append(dict(
    n=11, orig=24, answer='C', topic='Money & profit',
    question=f"""<p>Alan {hl('bought a silver jug at an auction for £80', 'g', 1)}. A year later, the price of antique silver had risen and
he decided to sell it at auction, for which he {hl('received £100', 'g', 1)}. He immediately regretted his decision
and approached the buyer, who sold it back to him but {hl('he had to pay £110', 'p', 2)}. Another year later, he
needed some money so {hl('sold the jug to a dealer for £120', 'g', 1)}.</p>
<p class="stem">How much profit did he make on the jug {hl('overall', 'b', 3)}?</p>""",
    options={'A': '£10', 'B': '£20', 'C': '£30', 'D': '£40', 'E': '£50'},
    notes=[(1, 'g', 'Money in and out. Write each one down with a + or −.'),
           (2, 'p', 'Buying it back costs him £110, more than he sold it for.'),
           (3, 'b', 'Overall = all the money in minus all the money out.')],
    steps=[
        f"""<p>Follow the cash, one deal at a time:</p>{_jug()}""",
        f"""{calc('money in: 100 + 120 = 220', 'money out: 80 + 110 = 190', f'profit = 220 − 190 = {boxed("£30")}')}
{note('Another way: two separate deals. 80 → 100 makes £20, then 110 → 120 makes £10. Total £30.', 'tip')}""",
    ],
    answer_text='£30: he took in £220 and paid out £190.',
    why={'A': '£10 is only the second deal (bought at 110, sold at 120).',
         'B': '£20 is only the first deal (bought at 80, sold at 100).',
         'D': '£40 is 120 − 80: it ignores the extra £10 he lost by buying back for more than he sold.',
         'E': '£50 counts the £10 gap between 100 and 110 as a gain instead of a loss.'},
    fast='In 100 + 120 = 220, out 80 + 110 = 190. Profit £30.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _flights():
    X = lambda h, m=0: 40 + (h + m / 60 - 9) * 52
    parts, lab = [line(X(9), 110, X(20.3), 110, k='ink', w=2)], []
    for h in range(9, 21):
        parts.append(line(X(h), 104, X(h), 116, k='ink', w=1.4))
        lab.append(text(X(h), 134, f'{h}', k='muted', size=14))
    lab.append(text(X(14.5), 156, 'Rome clock (hours)', k='muted', size=14))
    legs = [((9, 5), (10, 55), 'out', 'b'), ((11, 30), (13, 45), 'back', 'o'), ((15, 5), (16, 55), 'out', 'b'), ((17, 30), (19, 45), 'back', 'o')]
    for (h1, m1), (h2, m2), name, f in legs:
        parts.append(rect(X(h1, m1), 70, X(h2, m2) - X(h1, m1), 30, k='ink', fill=f, sw=1.6))
        lab.append(text((X(h1, m1) + X(h2, m2)) / 2, 90, name, k='ink', size=14))
    lab += [text(X(9, 5), 60, 'take off 09:05', k='pen', size=15, anchor='start'),
            text(X(19, 45), 60, 'land 19:45', k='orange', size=15, anchor='end')]
    parts.append(line(X(9, 5), 180, X(19, 45), 180, k='red', w=2.4, head=True, tail=True))
    lab.append(text(X(14, 25), 204, '10 h 40 min', k='red', size=22, font='scrawl'))
    lab.append(text(X(14, 25), 30, 'flying in Rome time (London is 1 hour behind)', k='muted', size=15))
    return svg(640, 216, rough(*parts) + ''.join(lab),
               'Timeline in Rome time from 09:05 take-off to 19:45 landing with four flights, 10 hours 40 minutes')


def _timetable():
    rows = [['09:05', '09:55', '10:30', '13:45'], ['12:05', '12:55', '13:30', '16:45'],
            ['15:05', '15:55', '16:30', '19:45'], ['18:05', '18:55', '19:30', '22:45']]
    used = {(0, 0), (0, 1), (0, 2), (0, 3), (2, 0), (2, 1), (2, 2), (2, 3)}
    body = ''.join('<tr>' + ''.join(f'<td>{hl(c, "g") if (i, j) in used else c}</td>' for j, c in enumerate(r)) + '</tr>'
                   for i, r in enumerate(rows))
    return ('<div class="tbl-wrap"><table class="ptable"><thead>'
            '<tr><th colspan="2">Rome – London</th><th colspan="2">London - Rome</th></tr>'
            '<tr><th>Depart</th><th>Arrive</th><th>Depart</th><th>Arrive</th></tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


Q.append(dict(
    n=12, orig=25, answer='D', topic='Timetables',
    question=f"""<p>An airplane flight crew starts its day in Rome and does {hl('two round trips', 'y', 1)} to London in the day. On
each arrival at an airport {hl('they take the next scheduled flight back', 'y', 2)}. The timetable is shown below ({hl('all times are local', 'p', 3)}):</p>
{_timetable()}
<p class="stem">How long is it from {hl('take-off on their first flight to landing on their last flight', 'b', 4)} of the day?</p>""",
    options={'A': '4h 40min', 'B': '7h 40min', 'C': '8h 10min', 'D': '10h 40min', 'E': '13h 40min'},
    notes=[(1, 'y', 'Rome → London → Rome, twice. Four flights.'),
           (2, 'y', 'They can’t catch a flight that leaves before they land.'),
           (3, 'p', 'London is an hour behind Rome. But the day starts <b>and</b> ends in Rome, so both times are on the same clock.'),
           (4, 'b', 'The whole working day: first take-off to last landing, waiting included.')],
    steps=[
        f"""<p>Follow the crew through the timetable (the used flights are highlighted):</p>
{calc(f'09:05 Rome {ar()} 09:55 London', f'next back: 10:30 London {ar()} 13:45 Rome',
      f'next out after 13:45: 15:05 Rome {ar()} 15:55 London (the 12:05 has already gone)',
      f'next back: 16:30 London {ar()} 19:45 Rome')}""",
        f"""<p>First take-off 09:05 and last landing 19:45 are both Rome times, so just subtract:</p>{_flights()}
{calc(f'09:05 → 19:05 = 10 h, → 19:45 = 40 min {ar()} {boxed("10h 40min")}')}
{note('Local times make the flights look odd (50 minutes out, 3 h 15 back). They really take 1 h 50 and 2 h 15. You don’t need this, because the start and end are in the same city.', 'tip')}""",
    ],
    answer_text='10h 40min: from 09:05 to 19:45, both Rome times.',
    why={'A': '4h 40min (09:05 to 13:45) is only the first round trip.',
         'B': '7h 40min (09:05 to 16:45) uses the 12:05 flight for the second trip, but that leaves before they land at 13:45.',
         'C': '8h 10min adds up the flight times from the table (50 min + 3h 15) twice and leaves out the waiting.',
         'E': '13h 40min (09:05 to 22:45) waits for the last flight of the day instead of the next one.'},
    fast='09:05 out, back 13:45, out 15:05, back 19:45. 19:45 − 09:05 = 10h 40min.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _fold():
    parts, lab = [], []
    s, c = 34, 13
    # panel A: both holes are the same shape after flipping
    ax, ay = 130, 120
    hexa = [(ax - s, ay - s), (ax + s - c, ay - s), (ax + s, ay - s + c), (ax + s, ay + s), (ax - s + c, ay + s), (ax - s, ay + s - c)]
    parts += [poly(hexa, k='pen', fill='p', sw=2.4), poly(hexa, k='red', sw=2, closed=True)]
    lab += [text(ax, 34, 'A: flip the left hole over', k='ink', size=17, font='scrawl'),
            text(ax, 196, 'it lands exactly on the right hole', k='ink', size=15),
            text(ax, 218, 'overlap has 6 sides ✗', k='red', size=18, font='scrawl')]
    # panel C: square on diamond gives an octagon
    cx, cy, d = 420, 120, 46
    sq = [(cx - s, cy - s), (cx + s, cy - s), (cx + s, cy + s), (cx - s, cy + s)]
    di = [(cx, cy - d), (cx + d, cy), (cx, cy + d), (cx - d, cy)]
    e = d - s
    octo = [(cx + s, cy - e), (cx + e, cy - s), (cx - e, cy - s), (cx - s, cy - e), (cx - s, cy + e), (cx - e, cy + s), (cx + e, cy + s), (cx + s, cy + e)]
    parts += [poly(octo, k='green', fill='g', sw=1), poly(sq, k='red', sw=2.2), poly(di, k='pen', sw=2.2)]
    lab += [text(cx, 34, 'C: square flipped onto diamond', k='ink', size=17, font='scrawl'),
            text(cx, 196, 'you only see through where both', k='ink', size=15),
            text(cx, 218, 'layers have a hole: 8 sides ✓', k='green', size=18, font='scrawl')]
    return svg(580, 232, rough(*parts) + ''.join(lab),
               'Option A: the flipped left hole matches the right hole exactly, a six-sided overlap. Option C: a square on a diamond overlaps in an octagon')


Q.append(dict(
    n=13, orig=26, answer='A', topic='Folding & symmetry',
    question=f"""<p>A sheet of paper has {hl('two holes', 'y', 1)} cut from it. When it is {hl('folded in half', 'y', 2)} the hole shown in the diagram
below is seen.</p>
{fig(Y, 'ps_q13_folded', 'The folded sheet with one regular octagon-shaped hole', 130)}
<p class="stem">Which one of the following could {hl('<b>not</b>', 'b', 3)} be the unfolded sheet of paper? (The dotted line indicates
where it was folded.)</p>
{fig(Y, 'ps_q13_opts', 'Five unfolded sheets A to E, each with a dashed fold line and one shape either side', 480)}""",
    options={'A': 'sheet A', 'B': 'sheet B', 'C': 'sheet C', 'D': 'sheet D', 'E': 'sheet E'},
    notes=[(1, 'y', 'One hole in each half of the sheet.'),
           (2, 'y', 'Folding flips one half over onto the other: the left hole becomes its <b>mirror image</b>.'),
           (3, 'b', 'You can only see through where <b>both</b> layers have a hole, so the octagon is the overlap.')],
    steps=[
        f"""<p>Folding along the dotted line flips the left half over onto the right. Light only gets through where the flipped left hole
<b>and</b> the right hole overlap. That overlap must be the octagon.</p>""",
        f"""<p>Test the overlaps:</p>{_fold()}""",
        f"""<ul><li><b>A</b>: the left hole has its top-left and bottom-right corners cut off. Flipped, those become top-right and bottom-left,
exactly like the right hole. The overlap is that same 6-sided shape, not an octagon {cross()}</li>
<li><b>B</b>: a downward arrow over an upward arrow: the box parts and the points trim each other into an octagon {tick()}</li>
<li><b>C</b>: square over diamond: the diamond trims the square’s corners into an octagon {tick()}</li>
<li><b>D</b>: tall hexagon over wide hexagon: each trims the other’s points, an octagon {tick()}</li>
<li><b>E</b>: flipped, the left arrow points left, so you get a left arrow over a right arrow, an octagon (like B on its side) {tick()}</li></ul>
{calc(f'cannot be the sheet: {boxed("A")}')}""",
    ],
    answer_text='A: when folded, its two holes line up exactly, so the hole you see has only 6 sides.',
    why={'B': 'B works: the down-arrow and up-arrow overlap in an octagon.',
         'C': 'C works: a square and a diamond overlap in an octagon.',
         'D': 'D works: a tall hexagon and a wide hexagon overlap in an octagon.',
         'E': 'E works: once flipped, the left arrow points the other way, and opposite arrows overlap in an octagon.'},
    fast='The octagon is the overlap of mirror(left) and right. In A, mirror(left) = right, so the overlap keeps only 2 cut corners: 6 sides.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _mixes():
    parts, lab = [], []
    W = 500
    for i, (n, ml, k) in enumerate(((16, 750, 'pen'), (25, 480, 'orange'))):
        y = 44 + i * 96
        w = W / n
        for j in range(n):
            parts.append(rect(40 + j * w, y, w, 34, k='ink', fill='g' if j == 0 else 'b', sw=1.2))
        lab += [text(40, y - 10, f'application {i + 1}: 1 + {n - 1} = {n} parts in 12 litres', k=k, size=17, anchor='start'),
                text(40 + W / 2, y + 58, f'1 part = 12 000 ml ÷ {n} = {ml} ml of Greatgrass', k='green', size=16)]
    lab.append(text(290, 232, 'total: 750 + 480 = 1230 ml', k='red', size=21, font='scrawl'))
    return svg(580, 246, rough(*parts) + ''.join(lab),
               '12 litres split into 16 equal parts gives 750 ml of Greatgrass; split into 25 parts gives 480 ml; total 1230 ml')


Q.append(dict(
    n=14, orig=30, answer='B', topic='Ratio',
    question=f"""<p>Today I am going to treat my lawn with Greatgrass liquid lawn food. The instructions on the bottle
tell me to dilute {hl('1 part Greatgrass with 15 parts water', 'y', 1)}, then apply evenly. Three hours later the
treatment should be repeated, but with a mixture of {hl('1 part Greatgrass and 24 parts water', 'y', 1)}. I have
worked out that I need to make up {hl('a total of 12 litres of diluted liquid for each application', 'p', 2)}.</p>
<p class="stem">How much Greatgrass will I use {hl('altogether', 'b', 3)} today?</p>""",
    options={'A': '960ml', 'B': '1230ml', 'C': '1300ml', 'D': '1500ml', 'E': '2460ml'},
    notes=[(1, 'y', 'Count all the parts: 1 + 15 = <b>16</b>, and 1 + 24 = <b>25</b>.'),
           (2, 'p', 'The 12 litres is the <b>finished mixture</b> (Greatgrass + water), not just the water.'),
           (3, 'b', 'Add both applications together.')],
    steps=[
        f"""<p>Ratio trick: total parts first, then one part.</p>{_mixes()}""",
        f"""{calc('12 000 ÷ 16 = 750 ml', '12 000 ÷ 25 = 480 ml', f'750 + 480 = {boxed("1230 ml")}')}
{note('12 000 ÷ 25: there are 4 lots of 25 in 100, so 120 × 4 = 480.', 'tip')}""",
    ],
    answer_text='1230 ml: 750 ml in the first mix and 480 ml in the second.',
    why={'A': '960 ml uses the weaker 1 : 24 mix (480 ml) for both applications.',
         'C': '1300 ml divides by 15 and 24 (800 + 500), as if the 12 litres were water only. The Greatgrass is part of the 12 litres.',
         'D': '1500 ml uses the stronger 1 : 15 mix (750 ml) for both applications.',
         'E': '2460 ml is double the right answer, as if each application were 24 litres.'},
    fast='12 000 ÷ 16 = 750, 12 000 ÷ 25 = 480. Total 1230 ml.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _mock():
    parts, lab = [], []
    x0, y0, c = 200, 60, 110
    vals = [[90, 25], [25, 60]]
    for r in range(2):
        for k in range(2):
            ok = r == k
            parts.append(rect(x0 + k * c, y0 + r * 60, c, 60, k='ink', fill='g' if ok else 'p', sw=1.6))
            lab.append(text(x0 + k * c + c / 2, y0 + r * 60 + 38, vals[r][k], k='green' if ok else 'red', size=24, font='scrawl'))
    lab += [text(x0 + c / 2, y0 - 12, 'A–C', k='ink', size=16), text(x0 + 1.5 * c, y0 - 12, 'other', k='ink', size=16),
            text(x0 + c, y0 - 34, 'actual GCSE', k='muted', size=15),
            text(x0 - 10, y0 + 36, 'mock A–C', k='ink', size=16, anchor='end'), text(x0 - 10, y0 + 96, 'mock other', k='ink', size=16, anchor='end'),
            text(x0 + 2 * c + 20, y0 + 36, 'green = predicted right', k='green', size=16, anchor='start'),
            text(x0 + 2 * c + 20, y0 + 96, 'pink = predicted wrong', k='red', size=16, anchor='start'),
            text(320, 214, 'right: 90 + 60 = 150 out of 200 = 75%', k='green', size=19, font='scrawl')]
    return svg(640, 228, rough(*parts) + ''.join(lab),
               'Two by two grid: 90 and 60 on the diagonal are correct predictions, 25 and 25 off the diagonal are wrong; 150 out of 200 is 75 percent')


Q.append(dict(
    n=15, orig=31, answer='E', topic='Two-way tables',
    question=f"""<p>The mock examination and actual GCSE results for English in one year at Morgan College are
shown below:</p>
<div class="tbl-wrap"><table class="ptable"><thead>
<tr><th colspan="2"></th><th colspan="2">Actual GCSE exams</th></tr>
<tr><th colspan="2"></th><th>Grades A-C</th><th>Other Grades</th></tr></thead>
<tbody><tr><td rowspan="2">Mock GCSE exams</td><td>Grades A-C</td><td>{hl('90', 'g', 2)}</td><td>25</td></tr>
<tr><td>Other grades</td><td>25</td><td>{hl('60', 'g', 2)}</td></tr></tbody></table></div>
<p class="stem">What percentage of pupils had their GCSE results {hl('correctly predicted', 'b', 1)} by their mock examination
results?</p>""",
    options={'A': '25.0 %', 'B': '50.0 %', 'C': '57.5 %', 'D': '60.0 %', 'E': '75.0 %'},
    notes=[(1, 'b', 'Correct = the mock grade band and the real grade band agree.'),
           (2, 'g', 'Those are the two cells where mock and actual match.')],
    steps=[
        f"""<p>Mock and actual agree on the diagonal of the table:</p>{_mock()}""",
        f"""{calc('correct: 90 + 60 = 150', 'all pupils: 90 + 25 + 25 + 60 = 200', f'150 ÷ 200 = {frac(3, 4)} = {boxed("75%")}')}""",
    ],
    answer_text='75%: 150 of the 200 pupils got the grade band their mock predicted.',
    why={'A': '25% is the share predicted <b>wrongly</b> (25 + 25 = 50 of 200).',
         'B': '50% would mean only 100 of the 200 were right, but 90 + 60 = 150 were.',
         'C': '57.5% is 115 ÷ 200: the mock A–C row (90 + 25), which includes 25 wrong predictions.',
         'D': '60% is 90 ÷ 150: the A–C successes as a share of the correct ones, not of all pupils.'},
    fast='Diagonal 90 + 60 = 150 out of 200 = 75%.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _trap():
    u = 30
    ox, oy = 40, 280
    P = lambda x, y: (ox + x * u, oy - y * u)
    parts, lab = [], []
    for x in range(0, 17):
        parts.append(line(*P(x, 0), *P(x, 8), k='muted', w=0.6))
    for y in range(0, 9):
        parts.append(line(*P(0, y), *P(16, y), k='muted', w=0.6))
    pieces = [([(0, 0), (5, 0), (5, 8), (4, 8)], 'b', 'A', (3.6, 3)),
              ([(5, 0), (10, 0), (6, 8), (5, 8)], 'g', 'A', (6.6, 3)),
              ([(10, 0), (11, 0), (11, 8), (6, 8)], 'o', 'A', (9.5, 5)),
              ([(11, 0), (16, 0), (12, 8), (11, 8)], 'v', 'A', (12.4, 3))]
    for pts, f, name, (tx, ty) in pieces:
        parts.append(poly([P(*p) for p in pts], k='ink', fill=f, sw=2.2))
        lab.append(text(*P(tx, ty), name, k='ink', size=24, font='scrawl'))
    lab += [text(*P(2.2, 8.4), 'A', k='pen', size=15), text(*P(13.5, 8.4), 'A flipped', k='violet', size=15),
            text(*P(8, 9.2), 'middle 6 × 8 rectangle = A + A upside down', k='ink', size=16),
            text(*P(8, -1.1), 'bottom 16, top 8, height 8 squares: area 96 → each piece 24', k='red', size=16)]
    return svg(560, 330, rough(*parts) + ''.join(lab),
               'The trapezium on a grid split into four copies of piece A: one in each corner and two, one upside down, filling the middle rectangle')


Q.append(dict(
    n=16, orig=32, answer='A', topic='Shapes & tiling',
    question=f"""<p>The trapezium below may be cut into {hl('four identical pieces', 'y', 1)}.</p>
{fig(Y, 'ps_q16_trap', 'A trapezium whose bottom edge is twice as long as its top edge', 240)}
<p class="stem">Which of the following pieces can be used four times ({hl('flips and rotations are allowed', 'p', 2)}) to make up
the trapezium?</p>
{fig(Y, 'ps_q16_opts', 'Pieces: A a tall right-angled trapezium, B a scalene triangle, C an isosceles triangle, D a five-sided piece, E a parallelogram', 420)}""",
    options={'A': 'piece A', 'B': 'piece B', 'C': 'piece C', 'D': 'piece D', 'E': 'piece E'},
    notes=[(1, 'y', 'Each piece must be exactly a <b>quarter</b> of the trapezium’s area, and the four must fit with no gaps.'),
           (2, 'p', 'You may turn pieces over, so mirror images are fine.')],
    steps=[
        f"""<p>Put the trapezium on squared paper. Its height = its top edge, and the bottom is twice the top. Using 8 squares for the height:</p>
{calc('top 8, bottom 16, height 8', 'area = (8 + 16) ÷ 2 × 8 = 96 squares', f'each piece must be 96 ÷ 4 = <b>24 squares</b>')}""",
        f"""<p>Piece A is as tall as the trapezium (8), with a top of 1 and a bottom of 5, and its slope matches the trapezium’s sides:</p>
{calc('A: (1 + 5) ÷ 2 × 8 = 24 squares ✓')}
<p>Now fit four of them in:</p>{_trap()}""",
        f"""<p>Quick checks on the others:</p>
<ul><li><b>C</b> is half of a 8 × 8 square, 32 squares: too big. (Three C’s make the trapezium, not four.)</li>
<li><b>D</b> is about 29 squares: too big.</li>
<li><b>E</b> is 6 × 4 = 24 squares, the right size, but its sides are 6 and about 4½ long. The trapezium’s top edge is 8, and no mix of 6s and 4½s makes exactly 8, so there would be a gap.</li>
<li><b>B</b> has sides of about 5, 9 and 9: again nothing adds up to the top edge of 8.</li></ul>
{calc(f'answer = {boxed("A")}')}""",
    ],
    answer_text='A: one in each bottom corner and two (one upside down) filling the middle rectangle.',
    why={'B': 'B’s sides (about 5, 9 and 9) can’t add up to the top edge of 8, so four B’s leave gaps. It is also a little too small.',
         'C': 'C has area 32, a third of the trapezium: three C’s make it, not four.',
         'D': 'D is too big (about 29 squares instead of 24).',
         'E': 'E is the right size, but its sides (6 and about 4½) can’t make the top edge of 8 exactly.'},
    fast='Try A first: two in the corners, the middle is a rectangle that two A’s (one upside down) fill. Done.',
))


# ---------------------------------------------------------------- 17 (Q36)
def _stairs():
    sal = [29000, 32000, 35500, 39500, 43500, 48000, 53000, 58500, 64500]
    parts, lab = [], []
    for i, v in enumerate(sal):
        x = 30 + i * 66
        h = (v - 20000) / 210
        f = 'g' if i == 8 else 'b'
        parts.append(rect(x, 250 - h, 52, h, k='ink', fill=f, sw=1.6))
        lab.append(text(x + 26, 244 - h, f'{v // 1000}.{(v % 1000) // 100}k' if v % 1000 else f'{v // 1000}k', k='ink', size=14))
        lab.append(text(x + 26, 270, 'start' if i == 0 else f'rise {i}', k='muted', size=13))
    lab.append(text(320, 30, 'each rise: 10%, then round UP to the next £500', k='red', size=17))
    return svg(640, 282, rough(*parts) + ''.join(lab),
               'Bar chart of Anton’s salary after each rise: 29k, 32k, 35.5k, 39.5k, 43.5k, 48k, 53k, 58.5k, 64.5k')


Q.append(dict(
    n=17, orig=36, answer='C', topic='Percentages & rounding',
    question=f"""<p>When Anton joined the company that he works for, 8 years ago, his salary was {hl('£29000', 'g', 1)}. Each of his
{hl('8 annual salary increases', 'g', 2)} has been {hl('10% of his previous salary', 'y', 3)} {hl('rounded <b>up</b> to the next multiple of £500', 'p', 4)}.</p>
<p class="stem">What is Anton's current salary?</p>""",
    options={'A': '£52500', 'B': '£58500', 'C': '£64500', 'D': '£67000', 'E': '£71000'},
    notes=[(1, 'g', 'Starting salary.'),
           (2, 'g', 'Eight rises: count them carefully.'),
           (3, 'y', 'Each rise is 10% of the <b>latest</b> salary, so the rises grow.'),
           (4, 'p', 'It is the <b>rise</b> that gets rounded up to a multiple of £500.')],
    steps=[
        f"""<p>10% is easy: move the decimal point. Then round the rise up to the next £500.</p>
{calc('29 000 → rise 2 900 → 3 000 → <b>32 000</b>', '32 000 → 3 200 → 3 500 → <b>35 500</b>',
      '35 500 → 3 550 → 4 000 → <b>39 500</b>', '39 500 → 3 950 → 4 000 → <b>43 500</b>',
      '43 500 → 4 350 → 4 500 → <b>48 000</b>', '48 000 → 4 800 → 5 000 → <b>53 000</b>',
      '53 000 → 5 300 → 5 500 → <b>58 500</b>', f'58 500 → 5 850 → 6 000 → {boxed("64 500")}')}""",
        f"""{_stairs()}
{note('Tick off the rises as you go: B (58 500) is where you land if you stop after 7.', 'trap')}""",
    ],
    answer_text='£64,500 after eight rounded-up 10% rises.',
    why={'A': '£52,500 is about what you get by adding the same £2,900 (10% of the <b>first</b> salary) every year and rounding up: the rises should grow.',
         'B': '£58,500 is the salary after only 7 rises.',
         'D': '£67,000 is too high: after exactly eight rounded-up rises the salary is £64,500.',
         'E': '£71,000 is one rise too many: a 9th rise (6,450 → 6,500) on top of £64,500.'},
    fast='Rises 3000, 3500, 4000, 4000, 4500, 5000, 5500, 6000 add to 35 500. 29 000 + 35 500 = 64 500.',
))
