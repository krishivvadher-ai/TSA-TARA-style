from wslib import *

Y = 2022
Q = []


def _dbl(x1, y1, x2, y2, k='red', bend=0.0, w=2.2):
    """Curved arrow with heads at both ends."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    cx, cy = mx - (y2 - y1) * bend, my + (x2 - x1) * bend
    return (f'<path d="M{x1} {y1} Q{cx:.1f} {cy:.1f} {x2} {y2}" class="k-{k}" stroke-width="{w}" fill="none" '
            f'marker-start="url(#ah-{k})" marker-end="url(#ah-{k})"/>')


# ---------------------------------------------------------------- 9 (Q19)
ROTA = [('Mon', ['Mel', 'Rod', 'Sam']), ('Tue', ['Eve', 'Fay', 'Tim']), ('Wed', ['Jan', 'Leo', 'Sam']),
        ('Thu', ['Mel', 'Pat', 'Tim']), ('Fri', ['Eve', 'Jan', 'Rod']), ('Sat', ['Fay', 'Leo', 'Pat'])]


def _rota():
    parts, lab = [], []
    x0, y0, cw, ch = 40, 80, 96, 40
    for i, (day, names) in enumerate(ROTA):
        x = x0 + i * cw
        lab.append(text(x + cw / 2, y0 - 12, day, k='muted', size=17))
        for j, nm in enumerate(names):
            y = y0 + j * ch
            f = 'y' if nm == 'Fay' else 'o' if nm == 'Pat' else 'paper'
            parts.append(rect(x + 3, y + 3, cw - 6, ch - 6, k='ink', fill=f, sw=1.5))
            lab.append(text(x + cw / 2, y + 27, nm, k='ink', size=18))
    fx, px = x0 + 1 * cw + cw / 2, x0 + 3 * cw + cw / 2
    parts.append(_dbl(fx + 26, 60, px - 26, 60, k='red', bend=-0.14))
    lab += [text((fx + px) / 2, 30, 'swap Fay (Tue) and Pat (Thu)', k='red', size=18, font='scrawl'),
            text(40, 236, 'After the swap:   Tue: Eve, Pat, Tim     Thu: Mel, Fay, Tim', k='pen', size=17, anchor='start'),
            text(40, 264, 'Fay works Thu + Sat, Pat works Tue + Sat: never two evenings in a row ✓', k='green', size=16, anchor='start'),
            text(40, 290, 'Fay–Tim and Pat–Tim now meet only once; Fay–Pat only on Sat ✓', k='green', size=16, anchor='start')]
    return svg(660, 306, rough(*parts) + ''.join(lab),
               'The rota grid with Fay on Tuesday swapping with Pat on Thursday; after the swap no one works two evenings in a row and no pair meets twice')


Q.append(dict(
    n=9, orig=19, answer='B', topic='Rotas & logic',
    question=f"""<p>A youth club is open six evenings every week. There are nine volunteers who run the club.
Each evening three of the volunteers are on duty.</p>
<p>When the rota is drawn up for any week, the following conditions must be met:</p>
<ul><li>Each volunteer has two evenings of duty, but {hl('never two consecutive evenings', 'y', 1)}.</li>
<li>{hl('No two volunteers are on duty together twice in the same week', 'y', 2)}.</li></ul>
<p>Next week’s rota has just been published, as follows:</p>
{table([['Mel', 'Eve', 'Jan', 'Mel', 'Eve', 'Fay'], ['Rod', hl('Fay', 'b'), 'Leo', 'Pat', 'Jan', 'Leo'], ['Sam', 'Tim', 'Sam', 'Tim', 'Rod', 'Pat']],
       head=['<i>Monday</i>', '<i>Tuesday</i>', '<i>Wednesday</i>', '<i>Thursday</i>', '<i>Friday</i>', '<i>Saturday</i>'])}
<p>Fay wants to {hl('swap her Tuesday duty with one of the others to be on duty on Monday or Thursday instead', 'b', 3)}.</p>
<p class="stem">Who is the {hl('only', 'p', 4)} volunteer on the rota for Monday or Thursday that Fay could swap with if the
conditions described above are still to be met?</p>""",
    options={'A': 'Mel', 'B': 'Pat', 'C': 'Rod', 'D': 'Sam', 'E': 'Tim'},
    notes=[(1, 'y', 'Rule 1: no Mon + Tue, Tue + Wed, and so on, for anybody.'),
           (2, 'y', 'Rule 2: any two people can share at most <b>one</b> evening.'),
           (3, 'b', 'A swap moves two people: Fay goes to their Monday or Thursday, and they go to Fay’s Tuesday.'),
           (4, 'p', 'Check the rules for <b>both</b> people after the swap, and for whoever they end up working with.')],
    steps=[
        f"""<p>The people on Monday or Thursday are Mel, Rod, Sam (Mon) and Mel, Pat, Tim (Thu). Whoever swaps moves to <b>Tuesday</b>, joining Eve and Tim.</p>""",
        f"""<p>Knock them out one by one:</p>
{calc(f'Tim: already on Tuesday, can’t take a second Tuesday {cross()}',
      f'Sam (Mon, Wed): would work Tue + Wed, two in a row {cross()}',
      f'Rod (Mon, Fri): on Tuesday he’d meet Eve, and he meets Eve on Friday too {cross()}',
      f'Mel’s Monday: Mel works Tue + Thu, meeting Tim on both {cross()}',
      f'Mel’s Thursday: Mel works Mon + Tue, two in a row {cross()}')}""",
        f"""<p>Only Pat is left. Check it really works:</p>{_rota()}
{calc(f'the only one who can swap {ar()} {boxed("Pat")}')}""",
    ],
    answer_text='Pat: Fay takes Pat’s Thursday and Pat takes Fay’s Tuesday, and both rules still hold.',
    why={'A': 'Mel fails both ways: swapping Monday puts Mel with Tim on Tuesday and Thursday; swapping Thursday gives Mel Monday and Tuesday in a row.',
         'C': 'Rod moving to Tuesday would be on duty with Eve twice (Tuesday and Friday).',
         'D': 'Sam moving to Tuesday would work Tuesday and Wednesday, two evenings in a row.',
         'E': 'Tim is already on Tuesday, so swapping would give him Tuesday twice and lose his Thursday.'},
    fast='Tim (already Tue) and Sam (Wed is next to Tue) are out at once. Rod meets Eve twice. Mel meets Tim twice or works Mon + Tue. Pat is left.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _scatter():
    X = lambda m: 70 + 4 * m
    Yp = lambda m: 300 - 2.6 * m
    parts, lab = [], []
    for v in range(0, 101, 10):
        parts.append(line(X(v), Yp(0), X(v), Yp(100), k='muted', w=0.8))
        parts.append(line(X(0), Yp(v), X(100), Yp(v), k='muted', w=0.8))
        lab.append(text(X(v), Yp(0) + 20, v, k='muted', size=13))
        lab.append(text(X(0) - 8, Yp(v) + 5, v, k='muted', size=13, anchor='end'))
    pts = [('Naz', 25, 25, 1), ('Huw', 40, 35, -1), ('Ivy', 30, 45, -1), ('Pete', 40, 50, -1), ('Ken', 48, 60, -1),
           ('Ffion', 60, 56, 1), ('Mei', 60, 80, 1), ('Lee', 65, 70, 1), ('Jim', 70, 80, 1), ('Quin', 80, 85, 1), ('Oli', 85, 95, 1)]
    for nm, a, b, side in pts:
        parts.append(circle(X(a), Yp(b), 5, k='ink', fill='ink', sw=1))
        lab.append(text(X(a) + 9 * side, Yp(b) + 5, nm, k='ink', size=14, anchor='start' if side > 0 else 'end'))
    parts.append(line(X(48), Yp(100), X(48), Yp(0), k='orange', w=1.8, dash=True))
    parts.append(circle(X(48), Yp(80), 7, k='red', fill='p', sw=2.4))
    parts.append(circle(X(48), Yp(50), 7, k='green', fill='paper', sw=2.4))
    parts.append(arrow(X(48) + 12, Yp(77), X(48) + 12, Yp(55), k='red', bend=-0.3))
    lab += [text(X(48) - 30, Yp(80) + 5, 'Gary is here ✗', k='red', size=15, anchor='end'),
            text(X(48) + 4, Yp(50) + 24, 'should be (48, 50)', k='green', size=15, anchor='start'),
            text(X(48), Yp(100) - 10, 'start mark 48: Gary and Ken', k='orange', size=15),
            text(X(50), Yp(0) + 42, 'starting mark →', k='ink', size=16),
            text(26, Yp(50), 'end mark →', k='ink', size=16, rotate=-90)]
    return svg(520, 354, rough(*parts) + ''.join(lab),
               'The scatter graph with axes 0 to 100 and each student named; the dot at starting mark 48 and end mark 80 should be Gary at 48, 50')


Q.append(dict(
    n=10, orig=20, answer='B', topic='Scatter graphs',
    question=f"""<p>Students studying geography at college were tested at the start of the year and at the end of
the year. Their marks are shown in the following table.</p>
{table([['<i>starting mark</i>', '60', hl('48', 'g', 3), '40', '30', '70', hl('48', 'g'), '65', '60', '25', '85', '40', '80'],
        ['<i>end mark</i>', '56', '50', '35', '45', '80', '60', '70', '80', '25', '95', '50', '85']],
       head=['<i>student</i>', 'Ffion', 'Gary', 'Huw', 'Ivy', 'Jim', 'Ken', 'Lee', 'Mei', 'Naz', 'Oli', 'Pete', 'Quin'])}
<p>The following scatter graph shows the marks for the 12 students, but {hl('one of the points has been incorrectly plotted', 'y', 1)}.</p>
{fig(Y, 'ps_q10_scatter', 'Scatter graph on a 10 by 10 grid with no axis labels and 12 dots', 440)}
<p class="stem">{hl('Which student', 'b', 2)} has a mark that is incorrectly plotted on the scatter graph?</p>""",
    options={'A': 'Ffion', 'B': 'Gary', 'C': 'Huw', 'D': 'Ken', 'E': 'Mei'},
    notes=[(1, 'y', 'No numbers on the axes! The grid is 10 × 10 and marks go up to 100, so each square = 10 marks.'),
           (2, 'b', 'Only 5 students to check: Ffion, Gary, Huw, Ken, Mei.'),
           (3, 'g', 'Gary and Ken both started on 48, so their dots must be in the same column.')],
    steps=[
        f"""<p>Work out the axes. Each square is 10 marks. The lowest dot is at (25, 25): that’s Naz. The top dot is at (85, 95): that’s Oli.
So across = starting mark, up = end mark.</p>""",
        f"""<p>Gary and Ken both have starting mark 48, so look up the 48 column (just before the 50 line).
There should be dots at 50 (Gary) and 60 (Ken). The graph has dots at <b>60</b> and <b>80</b>:</p>{_scatter()}""",
        f"""{calc('Ken (48, 60) ' + tick(), 'Gary should be (48, 50), but the dot is at (48, 80) ' + cross(),
              'Ffion (60, 56) ' + tick() + '   Mei (60, 80) ' + tick() + '   Huw (40, 35) ' + tick(), f'wrong one {ar()} {boxed("Gary")}')}
{note('Pairs that share a starting mark (Gary and Ken on 48; Ffion and Mei on 60; Huw and Pete on 40) are the quickest to check: just look up one column.', 'tip')}""",
    ],
    answer_text='Gary: his point is at (48, 80) instead of (48, 50).',
    why={'A': 'Ffion (60, 56) is there: in the 60 column, just above the 50 line.',
         'C': 'Huw (40, 35) is there: on the 40 line, halfway between 30 and 40.',
         'D': 'Ken (48, 60) is there: the lower dot in the 48 column, on the 60 line. That column is where Gary’s mistake shows up.',
         'E': 'Mei (60, 80) is there. The stray dot sits right next to Mei’s on the 80 line, which makes Mei easy to blame by mistake.'},
    fast='Gary and Ken both start on 48. The 48 column has dots at 60 and 80, not 50 and 60. Ken is fine, so Gary is wrong.',
))


# ---------------------------------------------------------------- 11 (Q24)
def _race():
    X = lambda t: 70 + t * 21
    parts, lab = [], []
    parts.append(line(X(0), 186, X(26), 186, k='ink', w=2, head=True))
    for t in range(0, 26, 5):
        parts.append(line(X(t), 180, X(t), 192, k='ink', w=1.6))
        lab.append(text(X(t), 212, f'{t} s', k='muted', size=14))
    parts.append(rect(X(0), 40, X(25) - X(0), 32, k='pen', fill='b', sw=2))
    parts.append(rect(X(2), 124, X(22) - X(2), 32, k='orange', fill='o', sw=2))
    lab += [text(X(12.5), 62, 'Maya runs 25 s', k='ink', size=18), text(X(12), 146, 'Iman runs 20 s', k='ink', size=18),
            text(X(0) - 8, 62, 'Maya', k='pen', size=17, anchor='end'), text(X(0) - 8, 146, 'Iman', k='orange', size=17, anchor='end')]
    parts.append(line(X(2), 76, X(2), 120, k='muted', w=1.4, dash=True))
    parts.append(line(X(22), 76, X(22), 120, k='muted', w=1.4, dash=True))
    parts.append(line(X(0), 100, X(2), 100, k='red', head=True, tail=True, w=2))
    parts.append(line(X(22), 100, X(25), 100, k='red', head=True, tail=True, w=2))
    lab += [text(X(2) + 8, 105, 'starts 2 s late', k='red', size=16, anchor='start'),
            text(X(22) - 8, 105, 'finishes 3 s early', k='red', size=16, anchor='end'),
            text(X(12.5), 244, 'Iman’s time = Maya’s time − 5 s', k='green', size=20, font='scrawl')]
    return svg(640, 258, rough(*parts) + ''.join(lab),
               'Timeline: Maya runs from 0 to 25 seconds; Iman starts at 2 seconds and finishes at 22 seconds, running for 20 seconds')


Q.append(dict(
    n=11, orig=24, answer='C', topic='Speed, distance & time',
    question=f"""<p>Iman and Maya ran a 100 metre race. {hl('Iman started 2 seconds after Maya and finished 3 seconds before her', 'y', 1)}.</p>
<p class="stem">If each girl ran at a {hl('constant speed', 'y', 2)} throughout the race, and {hl('Iman’s speed was 25% faster than Maya’s', 'p', 3)}, {hl('for how many seconds did Iman run', 'b', 4)}?</p>""",
    options={'A': '15 seconds', 'B': '18 seconds', 'C': '20 seconds', 'D': '22 seconds', 'E': '25 seconds'},
    notes=[(1, 'y', 'Iman’s running time is 2 + 3 = <b>5 seconds less</b> than Maya’s.'),
           (2, 'y', 'So time = 100 m ÷ speed for each girl.'),
           (3, 'p', 'Trap! 25% faster does <b>not</b> mean 25% less time. Speed × 1.25 means time × 0.8.'),
           (4, 'b', 'Iman’s own running time, not the clock time when she finishes.')],
    steps=[
        f"""<p>Picture the race on a clock that starts when Maya sets off:</p>{_race()}""",
        f"""<p>Same distance, so time goes the opposite way to speed:</p>
{calc(f'speed × 1.25 = speed × {frac(5, 4)}', f'so time × {frac(4, 5)}: Iman takes {frac(4, 5)} of Maya’s time',
      f'the missing {frac(1, 5)} of Maya’s time = 5 s', f'Maya = 25 s, Iman = 25 − 5 = {boxed("20 s")}')}""",
        f"""<p>Check with speeds:</p>
{calc('Maya: 100 ÷ 25 = 4 m/s', 'Iman: 100 ÷ 20 = 5 m/s', '5 is 25% more than 4 ' + tick())}
{note('Quickest exam route: test the options. Iman t, Maya t + 5, and (t + 5) ÷ t must be 1.25. Only 20 works: 25 ÷ 20 = 1.25.', 'tip')}""",
    ],
    answer_text='20 seconds: Maya takes 25 s at 4 m/s, Iman takes 20 s at 5 m/s.',
    why={'A': '15 s treats “25% faster” as “25% less time” (Maya 20 s, Iman 15 s). Then Iman’s speed is 6.67 m/s against 5 m/s: 33% faster, not 25%.',
         'B': '18 s would make Maya’s time 23 s, and 23 ÷ 18 ≈ 1.28: Iman would be about 28% faster, not 25%.',
         'D': '22 s is the clock time when Iman crosses the line (she started at 2 s). She only ran for 20 s.',
         'E': '25 s is Maya’s time, not Iman’s.'},
    fast='Iman’s time is 5 s less. 25% faster means time × 4/5, so 1/5 of Maya’s time = 5 s. Maya 25, Iman 20.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _fish():
    rows = [('Arctic', '90 g ÷ £3', 30), ('Banquet', '80 g ÷ £2.50', 32), ('Chilco', '165 g ÷ £5', 33),
            ('Dyner', '150 g ÷ £4', 37.5), ('Evertop', '35 g ÷ £1', 35)]
    X = lambda v: 250 + (v - 20) * 18
    parts, lab = [], []
    for i, (nm, w, v) in enumerate(rows):
        y = 40 + i * 44
        f = 'g' if nm == 'Dyner' else 'b'
        parts.append(rect(X(20), y, X(v) - X(20), 28, k='ink', fill=f, sw=1.6))
        lab.append(text(14, y + 20, nm, k='ink', size=18, anchor='start'))
        lab.append(text(240, y + 20, w, k='pen', size=15, anchor='end'))
        lab.append(text(X(v) + 8, y + 20, f'{v:g} g' + (' ✓' if nm == 'Dyner' else ''), k='green' if nm == 'Dyner' else 'ink', size=17, anchor='start'))
    lab.append(text(X(20), 28, 'grams of fish for every £1 (bars start at 20)', k='muted', size=14, anchor='start'))
    return svg(640, 264, rough(*parts) + ''.join(lab),
               'Grams of fish per pound: Arctic 30, Banquet 32, Chilco 33, Dyner 37.5, Evertop 35; Dyner is the most')


Q.append(dict(
    n=12, orig=25, answer='D', topic='Best value & percentages',
    question=f"""<p>Five popular makes of fishcake are shown in the table below, with comparisons of their
ingredients, the weight of each type and the cost for a {hl('pack of two', 'p', 1)}.</p>
{table([['Arctic', hl('45%', 'g'), '40%', '15%', hl('100 g', 'g'), hl('£3.00', 'g')],
        ['Banquet', hl('40%', 'g'), '50%', '10%', hl('100 g', 'g'), hl('£2.50', 'g')],
        ['Chilco', hl('55%', 'g'), '35%', '10%', hl('150 g', 'g'), hl('£5.00', 'g')],
        ['Dyner', hl('50%', 'g'), '35%', '15%', hl('150 g', 'g'), hl('£4.00', 'g')],
        ['Evertop', hl('35%', 'g'), '45%', '20%', hl('50 g', 'g'), hl('£1.00', 'g')]],
       head=['<i>type</i>', '<i>fish</i>', '<i>potato</i>', '<i>coating</i>', hl('<i>weight of each fishcake</i>', 'p', 2), '<i>cost of pack of 2 fishcakes</i>'])}
<p>Ester wants to buy the fishcakes that contain the {hl('greatest amount of fish per pound spent', 'b', 3)}.</p>
<p class="stem">Which make of fishcake should Ester buy?</p>""",
    options={'A': 'Arctic', 'B': 'Banquet', 'C': 'Chilco', 'D': 'Dyner', 'E': 'Evertop'},
    notes=[(1, 'p', 'The price is for <b>2</b> fishcakes.'),
           (2, 'p', 'The weight is for <b>1</b> fishcake. So a pack holds twice this.'),
           (3, 'b', 'Grams of fish ÷ price. The highest % of fish is not enough on its own.')],
    steps=[
        f"""<p>Fish in a pack = 2 × weight × fish %. Then divide by the pack price:</p>
{calc('Arctic: 200 g × 45% = 90 g, ÷ £3 = 30 g per £',
      'Banquet: 200 g × 40% = 80 g, ÷ £2.50 = 32 g per £',
      'Chilco: 300 g × 55% = 165 g, ÷ £5 = 33 g per £',
      'Dyner: 300 g × 50% = 150 g, ÷ £4 = <b>37.5 g per £</b>',
      'Evertop: 100 g × 35% = 35 g, ÷ £1 = 35 g per £')}""",
        f"""{_fish()}
{calc(f'most fish per pound {ar()} {boxed("Dyner")}')}
{note('Every price is for 2 fishcakes, so the “× 2” doesn’t change the order. You could use one fishcake per half-price instead and still pick Dyner.', 'tip')}""",
    ],
    answer_text='Dyner: 150 g of fish for £4, which is 37.5 g per pound.',
    why={'A': 'Arctic gives only 90 g of fish for £3: 30 g per pound, the worst.',
         'B': 'Banquet gives 80 g for £2.50: 32 g per pound.',
         'C': 'Chilco has the highest fish % (55%), but at £5 it gives only 33 g per pound.',
         'E': 'Evertop is the cheapest pack and gives 35 g per pound: close, but less than Dyner’s 37.5 g.'},
    fast='Fish grams per £: 90/3 = 30, 80/2.5 = 32, 165/5 = 33, 150/4 = 37.5, 35/1 = 35. Dyner wins.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _salaries():
    X = lambda v: 40 + v * 2.85
    vals = [182.0, 114.8, 130.7, 174.0, 149.7, 154.0, 201.2, 154.0, 112.5, 119.5, 120.4, 105.4, 3.5, 64.0, 25.3, 85.9]
    parts, lab = [line(X(0), 110, X(212), 110, k='ink', w=2)], []
    for v in range(0, 201, 50):
        parts.append(line(X(v), 104, X(v), 116, k='ink', w=1.4))
        lab.append(text(X(v), 134, v, k='muted', size=14))
    for v in vals:
        parts.append(circle(X(v), 110, 4, k='muted', fill='paper', sw=1.4))
    parts += [circle(X(3.5), 110, 7, k='green', fill='g', sw=2.2), circle(X(201.2), 110, 7, k='green', fill='g', sw=2.2),
              circle(X(182.0), 110, 6, k='red', fill='p', sw=2), circle(X(85.9), 110, 6, k='red', fill='p', sw=2),
              circle(X(25.3), 110, 6, k='orange', fill='o', sw=2)]
    lab += [text(X(182) - 6, 70, 'Italy 182.0', k='red', size=15, anchor='end'), text(X(182) - 6, 88, '(top of chart)', k='red', size=13, anchor='end'),
            text(X(85.9), 70, 'France 85.9', k='red', size=15), text(X(85.9), 88, '(bottom of chart)', k='red', size=13),
            text(X(25.3) + 4, 158, 'Malaysia 25.3', k='orange', size=14, anchor='start'),
            text(X(3.5), 70, 'Pakistan 3.5', k='green', size=15, anchor='start'),
            text(X(201.2), 40, 'Australia 201.2', k='green', size=15, anchor='end')]
    parts.append(line(X(3.5), 190, X(201.2), 190, k='green', head=True, tail=True, w=2.2))
    lab.append(text(X(102), 216, '201.2 − 3.5 = 197.7 thousand dollars', k='green', size=20, font='scrawl'))
    lab.append(text(X(0), 40, '$’000', k='muted', size=14, anchor='start'))
    return svg(660, 232, rough(*parts) + ''.join(lab),
               'All sixteen salaries on a number line: lowest Pakistan 3.5, highest Australia 201.2; Italy at the top of the chart and France at the bottom are neither')


Q.append(dict(
    n=13, orig=26, answer='E', topic='Reading charts',
    question=f"""<p>The following chart shows the {hl('average salary of politicians in selected countries in absolute terms on the left (in thousands of dollars)', 'y', 1)} and {hl('as a multiple of their country’s gross domestic product (GDP) per person on the right', 'p', 2)}.</p>
{fig(Y, 'ps_q13_chart', 'Chart: salary in thousands of dollars beside each country (Italy 182.0, Israel 114.8, Hong Kong 130.7, United States 174.0, Japan 149.7, Singapore 154.0, Australia 201.2, Canada 154.0, New Zealand 112.5, Germany 119.5, Ireland 120.4, Britain 105.4, Pakistan 3.5, Saudi Arabia 64.0, Malaysia 25.3, France 85.9), with bars for the multiple of GDP per person', 380)}
<p class="stem">What is the difference between the {hl('highest and lowest average salaries', 'b', 3)} of politicians in the
countries listed above?</p>""",
    options={'A': '$96 100', 'B': '$115 300', 'C': '$175 900', 'D': '$178 500', 'E': '$197 700'},
    notes=[(1, 'y', 'Use these numbers on the left. They are in thousands, so 182.0 means $182 000.'),
           (2, 'p', 'The countries are in order of the <b>bars</b>, not the salaries. The top one isn’t the highest salary!'),
           (3, 'b', 'Scan the whole salary column for the biggest and smallest numbers.')],
    steps=[
        f"""<p>The list is sorted by the bar lengths (multiple of GDP), so the salaries are jumbled. Scan every number:</p>{_salaries()}""",
        f"""{calc('highest: Australia 201.2', 'lowest: Pakistan 3.5', f'201.2 − 3.5 = 197.7 thousand = {boxed("$197 700")}')}
{note('The dot sizes help: Australia has the biggest dot, Pakistan the tiny one.', 'tip')}""",
    ],
    answer_text='$197 700: Australia ($201 200) minus Pakistan ($3 500).',
    why={'A': '$96 100 = 182.0 − 85.9: Italy (top of the chart) minus France (bottom of the chart).',
         'B': '$115 300 = 201.2 − 85.9: right highest, but takes France, the last country listed, as the lowest.',
         'C': '$175 900 = 201.2 − 25.3: uses Malaysia as the lowest and misses Pakistan’s tiny 3.5.',
         'D': '$178 500 = 182.0 − 3.5: takes Italy, at the top of the chart, as the highest.'},
    fast='Ignore the order. Biggest salary 201.2 (Australia), smallest 3.5 (Pakistan). 201.2 − 3.5 = 197.7 thousand.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _tickets():
    groups = [('1, 1, 8', ['118', '181', '811'], 'b'), ('1, 2, 4', ['124', '142', '214', '241', '412', '421'], 'g'),
              ('2, 2, 2', ['222'], 'o')]
    parts, lab = [], []
    for r, (digits, nums, f) in enumerate(groups):
        y = 30 + r * 66
        lab.append(text(16, y + 28, digits, k='ink', size=19, anchor='start'))
        for i, n in enumerate(nums):
            x = 110 + i * 74
            parts.append(rect(x, y, 64, 40, k='ink', fill=f, sw=1.6, rx=6))
            parts.append(circle(x, y + 20, 6, k='ink', fill='paper', sw=1.2))
            lab.append(text(x + 36, y + 28, n, k='ink', size=19, font='print'))
        lab.append(text(110 + 6 * 74 + 14, y + 28, f'= {len(nums)}', k='red', size=22, font='scrawl', anchor='start'))
    lab.append(text(320, 238, '3 + 6 + 1 = 10 winning tickets', k='green', size=23, font='scrawl'))
    return svg(640, 254, rough(*parts) + ''.join(lab),
               'Ticket numbers whose digits multiply to 8: 118, 181, 811; 124, 142, 214, 241, 412, 421; and 222. Ten in all')


Q.append(dict(
    n=14, orig=30, answer='C', topic='Counting & arrangements',
    question=f"""<p>In a prize draw, tickets are printed with {hl('3-digit numbers from 001 to 999', 'y', 1)}. Contestants pay to
take a ticket at random. A major prize is awarded for all tickets where the {hl('product of the 3 digits on the ticket drawn is 8', 'y', 2)} and a minor prize is awarded when the product is 12. For example 143
wins a minor prize because 1 × 4 × 3 = 12.</p>
<p class="stem">What is the {hl('maximum number of major prizes', 'b', 3)} which could be won?</p>""",
    options={'A': '7', 'B': '9', 'C': '10', 'D': '13', 'E': '14'},
    notes=[(1, 'y', 'Each number is printed once, so count the different ticket numbers that win.'),
           (2, 'y', 'Product = multiply. Any 0 makes the product 0, so no zeros.'),
           (3, 'b', 'The most possible = every winning ticket number is sold. Minor prizes (12) are a distraction.')],
    steps=[
        f"""<p>Which three digits multiply to 8? Split 8 into three factors (each from 1 to 9):</p>
{calc('8 = 1 × 1 × 8', '8 = 1 × 2 × 4', '8 = 2 × 2 × 2', 'that’s all: no zeros allowed, and no other digit divides into 8')}""",
        f"""<p>Now write out every order of each set:</p>{_tickets()}
{note('Three different digits can be ordered in 3 × 2 × 1 = 6 ways. With two the same there are only 3 ways (where does the odd one go?). All three the same: just 1.', 'tip')}""",
        f"""{calc(f'3 + 6 + 1 = {boxed("10")}')}""",
    ],
    answer_text='10: 118, 181, 811, 124, 142, 214, 241, 412, 421 and 222.',
    why={'A': '7 = 6 + 1: forgets the 1, 1, 8 tickets (118, 181, 811).',
         'B': '9 = 3 + 6: forgets 222.',
         'D': '13 = 6 + 6 + 1: counts 1, 1, 8 as six orders, as if the two 1s were different. There are only 3.',
         'E': '14 is 4 more than exist. Listing them all shows there are only 10.'},
    fast='Digit sets: 118 (3 orders), 124 (6 orders), 222 (1). Total 10.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _cups():
    parts, lab = [], []

    def cup(x, y, f, letter, k='ink'):
        parts.append(path(f'M{x} {y} L{x + 30} {y} L{x + 26} {y + 36} L{x + 4} {y + 36} Z', k=k, fill=f, sw=1.8))
        parts.append(path(f'M{x + 29} {y + 8} q12 2 8 14 q-3 6 -10 6', k=k, sw=1.8))
        lab.append(text(x + 15, y + 26, letter, k='ink', size=16, font='print', weight=700))

    for i in range(5):
        base = 20 + i * 88
        cup(base + 6, 40, 'y', 'T')
        cup(base + 42, 40, 'o', 'C')
        parts.append(rect(base, 30, 84, 56, k='muted', sw=1.2, rx=8))
        lab.append(text(base + 42, 106, '£4', k='pen', size=16))
    for i in range(4):
        cup(470 + i * 44, 40, 'v', 'H')
    lab += [text(230, 136, '5 pairs × £4 = £20', k='pen', size=19), text(554, 106, '4 × £3', k='violet', size=16),
            text(554, 136, '= £12', k='violet', size=19),
            text(330, 176, '£20 + £12 = £32 ✓    5 + 5 + 4 = 14 drinks', k='green', size=22, font='scrawl'),
            text(330, 210, '(the only other way: 2 pairs + 8 chocolates = £32, just 12 drinks)', k='muted', size=16)]
    return svg(660, 224, rough(*parts) + ''.join(lab),
               'Five tea and coffee pairs at 4 pounds each plus four hot chocolates at 3 pounds each make 32 pounds and 14 drinks')


Q.append(dict(
    n=15, orig=31, answer='E', topic='Money & combinations',
    question=f"""<p>The table shows the cost of hot drinks in a local café.</p>
{table([[hl('£1.50', 'g'), hl('£2.50', 'g'), hl('£3.00', 'g')]], head=['<i>tea</i>', '<i>coffee</i>', '<i>chocolate</i>'])}
<p>Belle bought a number of hot drinks, {hl('including at least one of each', 'p', 1)} tea, coffee and chocolate.
She was charged {hl('£32.00', 'g', 2)}.</p>
<p class="stem">If she bought the {hl('same number of teas as coffees', 'y', 3)}, what was the {hl('maximum number of hot drinks', 'b', 4)} that Belle could have bought for the £32.00?</p>""",
    options={'A': '9', 'B': '10', 'C': '12', 'D': '13', 'E': '14'},
    notes=[(1, 'p', 'At least 1 chocolate, so you can’t spend it all on teas and coffees.'),
           (2, 'g', 'Exactly £32, no change.'),
           (3, 'y', 'So teas and coffees come in pairs: 1 tea + 1 coffee = <b>£4</b> for 2 drinks.'),
           (4, 'b', 'Cheap drinks give more drinks: use as many £4 pairs and as few £3 chocolates as possible.')],
    steps=[
        f"""<p>Pairs cost £4 for 2 drinks (£2 each). A chocolate costs £3 for 1 drink. So pairs are better: use as <b>few</b> chocolates as possible.</p>""",
        f"""<p>After the chocolates, the rest of the £32 must be a multiple of £4 (whole pairs):</p>
{calc(f'1 chocolate: 32 − 3 = 29 {ar()} not a multiple of 4 {cross()}', f'2 chocolates: 32 − 6 = 26 {cross()}',
      f'3 chocolates: 32 − 9 = 23 {cross()}', f'4 chocolates: 32 − 12 = 20 {ar()} 5 pairs ' + tick())}""",
        f"""{_cups()}
{calc(f'5 teas + 5 coffees + 4 chocolates = {boxed("14")} drinks')}
{note('Check: 5 × 1.50 + 5 × 2.50 + 4 × 3 = 7.50 + 12.50 + 12 = £32 ✓', 'check')}""",
    ],
    answer_text='14 drinks: 5 teas, 5 coffees and 4 chocolates.',
    why={'A': '9 can’t cost exactly £32. The chocolates must be 4 or 8 (an even number), so the total number of drinks is always even.',
         'B': '10 counts only the 5 teas and 5 coffees and forgets the 4 chocolates.',
         'C': '12 is the other way to spend £32 (2 teas, 2 coffees, 8 chocolates), but it isn’t the maximum.',
         'D': '13 is odd, and as shown the total must be even (pairs plus 4 or 8 chocolates).'},
    fast='Tea + coffee = £4 a pair. Fewest chocolates leaving a multiple of £4: 4 chocolates (£12), then £20 = 5 pairs. 10 + 4 = 14.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _cube():
    c, ox, oy = 34, 70, 120
    dx, dy = 13, -10
    n = 5
    parts, lab = [], []
    # front face (green)
    parts.append(rect(ox, oy, n * c, n * c, k='ink', fill='g', sw=2))
    for i in range(1, n):
        parts.append(line(ox + i * c, oy, ox + i * c, oy + n * c, k='ink', w=1.2))
        parts.append(line(ox, oy + i * c, ox + n * c, oy + i * c, k='ink', w=1.2))
    # top face (red)
    tl, tr = (ox, oy), (ox + n * c, oy)
    parts.append(poly([tl, tr, (tr[0] + n * dx, tr[1] + n * dy), (tl[0] + n * dx, tl[1] + n * dy)], k='ink', fill='p', sw=2))
    for i in range(1, n):
        parts.append(line(ox + i * c, oy, ox + i * c + n * dx, oy + n * dy, k='ink', w=1.2))
        parts.append(line(ox + i * dx, oy + i * dy, ox + n * c + i * dx, oy + i * dy, k='ink', w=1.2))
    # right face (blue)
    rx = ox + n * c
    parts.append(poly([(rx, oy), (rx + n * dx, oy + n * dy), (rx + n * dx, oy + n * c + n * dy), (rx, oy + n * c)], k='ink', fill='b', sw=2))
    for i in range(1, n):
        parts.append(line(rx + i * dx, oy + i * dy, rx + i * dx, oy + n * c + i * dy, k='ink', w=1.2))
        parts.append(line(rx, oy + i * c, rx + n * dx, oy + i * c + n * dy, k='ink', w=1.2))
    # the green-blue edge: rx column, mark rows
    for r in range(n):
        cy = oy + r * c + c / 2
        cx = rx - c / 2
        if r in (0, n - 1):
            lab.append(text(cx, cy + 8, '✗', k='red', size=24))
        else:
            parts.append(circle(cx, cy, 9, k='orange', fill='y', sw=2.4))
    parts.append(rect(rx - c - 4, oy - 4, c + 8, n * c + 8, k='orange', sw=2.6, rx=6))
    lab += [text(ox + n * c / 2, oy + n * dy - 18, 'red top (and bottom)', k='red', size=17),
            text(ox + n * c / 2, oy + n * c + 30, 'green front (and back)', k='green', size=17),
            text(rx + n * dx + 14, oy + 2 * c, 'blue side', k='pen', size=17, anchor='start'),
            text(rx + n * dx + 14, oy + 2 * c + 22, '(and other side)', k='pen', size=15, anchor='start'),
            text(rx + n * dx + 14, oy + 3.6 * c, 'green meets blue on', k='orange', size=17, anchor='start'),
            text(rx + n * dx + 14, oy + 3.6 * c + 24, 'this edge: 5 cubes,', k='orange', size=17, anchor='start'),
            text(rx + n * dx + 14, oy + 3.6 * c + 48, 'but the ✗ ends touch red', k='red', size=17, anchor='start'),
            text(330, oy + n * c + 64, '4 green–blue edges × 3 middle cubes = 12', k='green', size=22, font='scrawl')]
    return svg(640, oy + n * c + 80, rough(*parts) + ''.join(lab),
               'A 5 by 5 by 5 cube with red top, green front and blue side; on the green-blue edge the 3 middle cubes count and the 2 corner cubes touch red')


Q.append(dict(
    n=16, orig=32, answer='C', topic='3D shapes & counting',
    question=f"""<p>I have a wooden cube with edges that are {hl('5 cm', 'g', 1)} long. I paint it in the following way:</p>
<ul><li>{hl('one pair of opposite faces is red', 'y', 2)}</li><li>one pair of opposite faces is green</li><li>one pair of opposite faces is blue</li></ul>
<p>Now I cut the cube into small cubes, each of whose edges are {hl('1 cm', 'g', 1)} long, in the following manner:</p>
{fig(Y, 'ps_q16_cube', 'The big cube drawn cut into a 5 by 5 by 5 grid of small cubes', 170)}
<p class="stem">How many of the small cubes have {hl('one green face, one blue face, but no red face', 'b', 3)}?</p>""",
    options={'A': '6', 'B': '8', 'C': '12', 'D': '16', 'E': '24'},
    notes=[(1, 'g', '5 small cubes along every edge (125 small cubes in all).'),
           (2, 'y', 'Opposite faces share a colour, so each colour is on 2 faces that never touch each other.'),
           (3, 'b', 'Exactly green + blue, no red: a cube on a green–blue edge, but not at a corner.')],
    steps=[
        f"""<p>A small cube with a green face <b>and</b> a blue face must sit on an <b>edge</b> where a green face meets a blue face.</p>
{calc('each green face meets each blue face along one edge', '2 green × 2 blue = <b>4</b> green–blue edges')}""",
        f"""<p>Look along one of those edges:</p>{_cube()}""",
        f"""{calc('5 cubes on each edge − 2 corners (they have a red face too) = 3', f'4 edges × 3 = {boxed("12")}')}
{note('The 4 green–blue edges are the 4 edges that run between the two red faces, like the 4 upright edges of a box with red lid and red base.', 'tip')}""",
    ],
    answer_text='12: 3 middle cubes on each of the 4 green–blue edges.',
    why={'A': '6 counts the middle cubes on only 2 of the green–blue edges. There are 4 such edges.',
         'B': '8 is the number of corner cubes, but every corner has a red face as well.',
         'D': '16 = 4 × 4: takes off only one corner from each edge. Both ends of each edge are corners touching red.',
         'E': '24 counts each cube twice (once for its green face, once for its blue face), or adds in edges with red.'},
    fast='Green meets blue on 4 edges. Each edge has 5 cubes, minus 2 red corners = 3. 4 × 3 = 12.',
))


# ---------------------------------------------------------------- 17 (Q36)
def _books():
    kids = [('Miya', 7, '7 × 1 h', 21, [('£8', 'Hungry Dinosaurs'), ('£13', 'Fly Away')], 'b'),
            ('Harriet', 10, '4 × 1 + 3 × 2', 30, [('£14', 'Come Back'), ('£16', 'The Biraffe')], 'o'),
            ('Mehran', 3, '2 × 1.5 h', 9, [('£9', 'The Celebrated Six')], 'g')]
    parts, lab = [], []
    lab += [text(100, 26, 'hours a week', k='muted', size=15, anchor='start'), text(258, 26, '£3 per hour', k='muted', size=15),
            text(300, 26, 'books', k='muted', size=15, anchor='start')]
    for i, (nm, h, how, share, books, f) in enumerate(kids):
        y = 46 + i * 84
        lab.append(text(14, y + 26, nm, k='ink', size=19, anchor='start'))
        parts.append(rect(100, y + 6, h * 14, 30, k='ink', fill=f, sw=1.6))
        lab.append(text(100 + h * 14 / 2, y + 27, f'{h} h', k='ink', size=16))
        lab.append(text(100, y + 58, how, k='muted', size=14, anchor='start'))
        lab.append(text(258, y + 28, f'£{share}', k='red', size=22, font='scrawl'))
        for j, (p, t) in enumerate(books):
            x = 300 + j * 150
            parts.append(rect(x, y, 142, 52, k='ink', fill='paper', sw=1.8, rx=4))
            parts.append(line(x + 10, y, x + 10, y + 52, k='ink', w=1.4))
            lab.append(text(x + 76, y + 22, p, k='ink', size=18))
            lab.append(text(x + 76, y + 42, t, k='pen', size=14))
    lab.append(text(320, 300, '7 + 10 + 3 = 20 hours, £60 ÷ 20 = £3 an hour', k='green', size=20, font='scrawl'))
    return svg(620, 316, rough(*parts) + ''.join(lab),
               'Miya reads 7 hours and gets 21 pounds of books (8 and 13), Harriet 10 hours and 30 pounds (14 and 16), Mehran 3 hours and 9 pounds (9)')


Q.append(dict(
    n=17, orig=36, answer='E', topic='Ratio & sharing',
    question=f"""<p>Grandma has spent {hl('£60 on five books', 'g', 1)} which she is intending to give to her three
grandchildren, Miya, Harriet and Mehran. She is going to give the books in a way that {hl('relates the cost to the time they normally spend reading', 'y', 2)} (i.e. spend the most on the child who reads
the most). {hl('Miya reads for an hour a day', 'g', 3)}. {hl('Harriet reads for an hour a day on Monday to Thursday and 2 hours a day on Friday to Sunday', 'g', 3)}. {hl('Mehran doesn’t read on weekdays but does an hour and a half on each of Saturday and Sunday', 'g', 3)}. The details of the books are shown in the
table below.</p>
{table([['Hungry Dinosaurs', '£8'], ['The Celebrated Six', '£9'], ['Fly Away', '£13'], ['Come Back', '£14'], ['The Biraffe', '£16']],
       head=['<i>title</i>', '<i>cost</i>'])}
<p class="stem">Which one of the following statements is {hl('true', 'b', 4)}?</p>""",
    options={'A': 'Harriet was given ‘The Celebrated Six’.', 'B': 'Harriet was given ‘Fly Away’.',
             'C': 'Mehran was given ‘The Biraffe’.', 'D': 'Miya was given ‘Come Back’.',
             'E': 'Miya was given ‘Hungry Dinosaurs’.'},
    notes=[(1, 'g', '8 + 9 + 13 + 14 + 16 = 60, so every book is given away.'),
           (2, 'y', 'Share the £60 in proportion to reading time.'),
           (3, 'g', 'Work out hours in a whole week for each child.'),
           (4, 'b', 'Find who gets which book, then test the statements.')],
    steps=[
        f"""<p>Reading time in a week:</p>
{calc('Miya: 7 days × 1 h = 7 h', 'Harriet: 4 × 1 h + 3 × 2 h = 10 h', 'Mehran: 2 × 1.5 h = 3 h', 'total = 20 h')}""",
        f"""<p>Share £60 in the ratio 7 : 10 : 3:</p>
{calc('£60 ÷ 20 = £3 per hour', 'Miya £21, Harriet £30, Mehran £9')}""",
        f"""<p>Now match the books to the money:</p>{_books()}
{calc('Mehran £9 = The Celebrated Six (the only £9 book)', 'Miya £21 = 8 + 13 (Hungry Dinosaurs + Fly Away)',
      'Harriet £30 = 14 + 16 (Come Back + The Biraffe)', f'true statement {ar()} {boxed("E")}')}""",
    ],
    answer_text='E: Miya gets Hungry Dinosaurs (£8) and Fly Away (£13), making her £21.',
    why={'A': 'The Celebrated Six (£9) is exactly Mehran’s £9 share.',
         'B': 'Fly Away (£13) goes to Miya, with Hungry Dinosaurs, to make £21.',
         'C': 'The Biraffe (£16) is more than Mehran’s whole £9 share. It goes to Harriet, the biggest reader.',
         'D': 'Come Back (£14) goes to Harriet. Miya’s £21 can only be 8 + 13.'},
    fast='Hours 7 : 10 : 3, so £21 : £30 : £9. Mehran = £9 book, Miya = 8 + 13, Harriet = 14 + 16. Miya has Hungry Dinosaurs.',
))
