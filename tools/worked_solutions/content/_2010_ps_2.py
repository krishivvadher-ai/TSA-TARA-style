from wslib import *

Y = 2010
Q = []

# ---------------------------------------------------------------- 9 (Q19)
def _parking():
    X = lambda h: 50 + (h - 12) * 92
    parts = [line(X(12), 96, X(18.2), 96, k='ink', w=2),
             rect(X(12), 62, X(15.5) - X(12), 34, k='ink', fill='b', sw=1.8),
             rect(X(15.5), 62, X(17.5) - X(15.5), 34, k='ink', fill='y', sw=1.8),
             line(X(17.5), 50, X(17.5), 104, k='red', w=3)]
    lab = [text((X(12) + X(15.5)) / 2, 85, 'meeting: at least 3½ h', k='ink', size=16),
           text((X(15.5) + X(17.5)) / 2, 50, 'drive off somewhere here', k='orange', size=16),
           text(X(17.5) + 6, 40, 'leave by 5:30', k='red', size=15, anchor='start')]
    for h, s in ((12, 'noon'), (13, '1pm'), (14, '2pm'), (15, '3pm'), (16, '4pm'), (17, '5pm'), (18, '6pm')):
        parts.append(line(X(h), 90, X(h), 102, k='ink', w=1.6))
        lab.append(text(X(h), 120, s, k='muted', size=14))
    lab.append(text(320, 152, 'parked for at least 3½ h, but maybe almost 5½ h', k='red', size=18, font='scrawl'))
    return svg(640, 166, rough(*parts) + ''.join(lab),
               'Timeline from noon: the meeting fills at least 12:00 to 3:30, then the car could leave any time up to 5:30')

Q.append(dict(
    n=9, orig=19, answer='B', topic='Tables & best deal',
    question=f"""<p>It is {hl('12 noon', 'g', 1)} and I have just arrived in the centre of town for a meeting that is due to last
for {hl('at least three and a half hours', 'p', 2)}.</p>
<p>After this meeting, I have an important appointment at 6.00pm which requires me to {hl('leave before 5.30pm', 'y', 3)}.</p>
<p>There are 5 car parks in the town centre that charge as follows:</p>
{table([['Grove Street', '£6.00 per day, flat rate.'],
        ['Victoria Square', f'£1.00 per hour {hl("or part of an hour", "p", 4)}.'],
        ['Central Park', 'Free for 2 hours, then £2.00 per hour or part of an hour.'],
        ['Bonningtons', 'Free for 1 hour, then £1.50 per hour or part of an hour.'],
        ['Grange Road', '£2.50 for 3 hours, then £1.50 per hour or part of an hour.']])}
<p class="stem">In which car park should I leave my car in order to {hl('pay as little as possible', 'b', 5)} in parking
fees?</p>""",
    options={'A': 'Grove Street', 'B': 'Victoria Square', 'C': 'Central Park', 'D': 'Bonningtons', 'E': 'Grange Road'},
    notes=[(1, 'g', 'The clock starts at 12:00.'),
           (2, 'p', '“At least”: it could run on. We don’t know when it ends.'),
           (3, 'y', 'So the car is parked from 3½ hours up to nearly 5½ hours.'),
           (4, 'p', 'Any part of an hour costs a whole hour: always round up.'),
           (5, 'b', 'Cheapest whatever time the meeting finishes.')],
    steps=[
        f"""<p>How long will the car be parked? Somewhere from 12:00 until between 3:30 and 5:30:</p>{_parking()}""",
        f"""<p>Price each car park for the three possible lengths of stay (round every part-hour up):</p>
{table([['Grove Street', '£6', '£6', '£6'],
        [hl('<b>Victoria Square</b>', 'g'), hl('<b>£4</b>', 'g'), hl('<b>£5</b>', 'g'), hl('<b>£6</b>', 'g')],
        ['Central Park', '2 h free + 2 → £4', '+ 3 → £6', '+ 4 → £8'],
        ['Bonningtons', '1 h free + 3 → £4.50', '+ 4 → £6.00', '+ 5 → £7.50'],
        ['Grange Road', '£2.50 + 1 → £4.00', '+ 2 → £5.50', '+ 3 → £7.00']],
       head=['Car park', 'leave 3:30 to 4:00', 'leave 4:00 to 5:00', 'leave 5:00 to 5:30'])}""",
        f"""<p>Victoria Square is the cheapest (or joint cheapest) in <b>every</b> column, so it is the safe choice {ar()} {boxed('Victoria Square')}</p>
{note('If you only cost exactly 3½ hours you get a three-way tie at £4 (Victoria, Central, Grange). The “at least” is what breaks the tie.', 'trap')}""",
    ],
    answer_text='Victoria Square: £4 to £6, never beaten whenever the meeting ends.',
    why={'A': 'Grove Street is £6 whatever happens. Victoria is never more than £6 and usually less.',
         'C': 'Central Park ties at £4 if the meeting ends right on 3:30, but jumps to £6 or £8 if it overruns.',
         'D': 'Bonningtons is never below £4.50 (3½ h = 1 free + 3 charged part-hours).',
         'E': 'Grange Road ties at £4 up to 4 hours, but costs £5.50 or £7 if the meeting runs on.'},
    fast='Cost each one for “just over 3½ h” and “nearly 5½ h”: Victoria £4 to £6 is never beaten.',
))

# ---------------------------------------------------------------- 10 (Q20)
def _taxi():
    vals = [70, 40, 30, 25, 22, 20]
    base, s = 246, 2.9
    parts, lab = [line(50, base, 500, base, k='ink', w=2)], []
    for i, v in enumerate(vals):
        x = 66 + i * 72
        parts.append(rect(x, base - v * s, 54, v * s, k='ink', fill='b', sw=1.8))
        lab.append(text(x + 27, base - v * s - 8, f'£{v}', k='pen', size=18))
        lab.append(text(x + 27, base + 20, i + 1, k='ink', size=16))
        lab.append(text(x + 27, base + 42, f'{70 + 10 * i} ÷ {i + 1}', k='muted', size=13))
    lab += [text(275, base + 66, 'people sharing (total ÷ people)', k='ink', size=15),
            text(570, 120, 'matches', k='green', size=20, font='scrawl'),
            text(570, 150, 'graph D', k='green', size=26, font='scrawl')]
    return svg(640, 322, rough(*parts) + ''.join(lab),
               'Bar chart of cost per person for 1 to 6 people: 70, 40, 30, 25, 22, 20 pounds, which matches graph D')

Q.append(dict(
    n=10, orig=20, answer='D', topic='Graphs & sharing costs',
    question=f"""<p>A taxi service advertises its rates for travel to the local airport as shown below:</p>
{table([['AIRPORT TAXI SERVICE'], [hl('£70', 'g', 1) + '<br>(includes return journey)'],
        [hl('EXTRA PASSENGERS £10 EACH', 'p', 2) + '<br>(vehicles licensed to carry 6 passengers)']])}
<p class="stem">Which one of the following bar graphs correctly illustrates how the {hl('cost per person', 'b', 3)}
decreases as more people get together to share a taxi to the airport?</p>
{fig(Y, 'ps_q10_graphs', 'Five bar charts A to E of cost per person against number of passengers 1 to 6', 520)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'g', 'One passenger pays £70 in total.'),
           (2, 'p', 'Each extra passenger adds £10 to the <b>total</b> fare. The first passenger isn’t “extra”.'),
           (3, 'b', 'Per person = total fare ÷ number of people.')],
    steps=[
        f"""<p>Total fare for n people = £70 + £10 for each person after the first. Then share it out:</p>
{table([['1', '£70', '£70'], ['2', '£80', '£40'], ['3', '£90', '£30'], ['4', '£100', '£25'], ['5', '£110', '£22'], ['6', '£120', '£20']],
       head=['People', 'Total fare', 'Each pays'])}""",
        f"""{_taxi()}
<p>Look for a graph going 70, 40, 30, 25, 22, 20. The quick test is the second bar: it must be exactly <b>40</b> {ar()} {boxed('D')}</p>""",
    ],
    answer_text='Graph D: 70, 40, 30, 25, 22, 20.',
    why={'A': 'A drops by £10 a person each time (70, 60, 50…): it takes £10 off the price each instead of adding £10 to the total.',
         'B': 'B is £70 ÷ people (70, 35, 23…): it forgets the £10 for each extra passenger.',
         'C': 'C starts at £80: it charges the first passenger the £10 extra too (80, 45, 33…).',
         'E': 'E halves every time (70, 35, 17.5…), far cheaper than the real fares.'},
    fast='Two people: (70 + 10) ÷ 2 = £40. Six: 120 ÷ 6 = £20. Only D has 40 and 20.',
))

# ---------------------------------------------------------------- 11 (Q24)
def _letters():
    parts, lab = [], []
    names = ['A', 'B', 'C']
    for x0, mapping, title in ((30, [1, 2, 0], 'way 1: everyone gets the next one'),
                               (350, [2, 0, 1], 'way 2: pass the other way')):
        lab.append(text(x0 + 120, 26, title, k='ink', size=17, font='scrawl'))
        for i in range(3):
            parts.append(rect(x0 + 90 * i, 48, 64, 36, k='ink', fill='y', sw=1.8))
            parts.append(path(f'M{x0 + 90 * i} 48 L{x0 + 90 * i + 32} 68 L{x0 + 90 * i + 64} 48', k='ink', sw=1.4))
            lab.append(text(x0 + 90 * i + 32, 102, f'letter for {names[i]}', k='muted', size=13))
            lab.append(stick_person(x0 + 90 * i + 32, 214, k='pen'))
            lab.append(text(x0 + 90 * i + 32, 236, names[i], k='pen', size=18))
        for i, j in enumerate(mapping):
            parts.append(arrow(x0 + 90 * i + 32, 110, x0 + 90 * j + 32, 166, k='red', bend=0.08 if j > i else -0.08))
    return svg(640, 250, rough(*parts) + ''.join(lab),
               'Three letters and three people in two panels: the two ways where nobody gets their own letter')

Q.append(dict(
    n=11, orig=24, answer='B', topic='Counting arrangements',
    question=f"""<p>A secretary is in a bad mood with her boss and has to write {hl('three letters intended for three different people', 'g', 1)}. She makes sure that {hl('each of the recipients of the letters will receive one written to someone else', 'y', 2)}.</p>
<p class="stem">In {hl('how many different ways', 'b', 3)} can she send three different letters to achieve this?</p>""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '5', 'E': '6'},
    notes=[(1, 'g', 'Call the people A, B, C. Each has a letter meant for them.'),
           (2, 'y', '<b>Nobody</b> gets their own letter. Every single person gets a wrong one.'),
           (3, 'b', 'Count the whole arrangements, not single letters.')],
    steps=[
        f"""<p>A must get B’s or C’s letter. Try both:</p>
<ul><li>A gets B’s letter. Then B gets A’s or C’s.
B gets C’s {ar()} C gets A’s {tick()} &nbsp; B gets A’s {ar()} C is left with C’s own {cross()}</li>
<li>A gets C’s letter. B can’t have their own, so B gets A’s {ar()} C gets B’s {tick()}</li></ul>""",
        f"""{_letters()}
{calc(f'only {boxed("2")} ways')}
{note('Of the 6 ways to hand out 3 letters: 1 gives everyone their own, 3 swap just two people (so one person still gets their own), and 2 move everyone.', 'check')}""",
    ],
    answer_text='2 ways: everyone passes “one along” in one direction or the other.',
    why={'A': '1 finds one pattern but misses its mirror image (passing the other way).',
         'C': '3 counts the “swap two people” arrangements, but each of those leaves the third person with their own letter.',
         'D': '5 = 6 − 1 only removes the case where <b>everyone</b> gets their own letter.',
         'E': '6 is every way to send 3 letters, including ones where someone gets their own.'},
    fast='Nobody gets their own: the letters must all shift round one place, left or right. 2 ways.',
))

# ---------------------------------------------------------------- 12 (Q25)
def _claims():
    data = [('Jan', 3000, 5390, 2891), ('Mar', 3100, 5500, 2972), ('Jun', 2400, 5090, 3230), ('Oct', 3000, 4740, 3236), ('Nov', 2100, 5780, 2895)]
    X = lambda v: 64 + v * 0.042
    parts, lab = [], []
    for i, (m, w, s, l) in enumerate(data):
        y = 54 + i * 40
        x = 0
        for v, f in ((w, 'p'), (s, 'o'), (l, 'b')):
            parts.append(rect(X(x), y, X(x + v) - X(x), 28, k='ink', fill=f, sw=1.4))
            x += v
        lab.append(text(54, y + 20, m, k='ink', size=17, anchor='end'))
        lab.append(text(X(x) + 6, y + 20, f'{x:,}'.replace(',', ' '), k='green' if m == 'Mar' else 'ink', size=16, anchor='start'))
    for j, (lbl, f) in enumerate((('write-offs × 100', 'p'), ('serious × 10', 'o'), ('slight × 1', 'b'))):
        parts.append(rect(64 + j * 180, 16, 18, 18, k='ink', fill=f, sw=1.4))
        lab.append(text(90 + j * 180, 31, lbl, k='ink', size=15, anchor='start'))
    lab.append(text(320, 268, 'cost in “slight accident” units', k='muted', size=15))
    return svg(640, 280, rough(*parts) + ''.join(lab),
               'Stacked bars of weighted claim cost: January 11 281, March 11 572, June 10 720, October 10 976, November 10 775')

Q.append(dict(
    n=12, orig=25, answer='B', topic='Weighted totals',
    question=f"""<p>Anne is a researcher working for an insurance company which has decided to send out a
safety awareness mailshot to its customers during the {hl('month which costs it most in claims', 'b', 1)}. She examines the average accident statistics bearing in mind that {hl('an accident categorised as a write-off costs 10 times more than one categorised as serious', 'y', 2)} {hl('which, in turn, costs 10 times more than one categorised as slight', 'y', 3)}.</p>
{table([['January', '30', '539', '2891', '3460'], ['February', '24', '414', '2513', '2951'], ['March', '31', '550', '2972', '3553'],
        ['April', '19', '401', '2901', '3321'], ['May', '19', '440', '2993', '3452'], ['June', '24', '509', '3230', '3763'],
        ['July', '24', '515', '2899', '3438'], ['August', '26', '477', '2732', '3235'], ['September', '22', '510', '2867', '3399'],
        ['October', '30', '474', '3236', '3740'], ['November', '21', '578', '2895', '3494'], ['December', '26', '381', '2967', '3374']],
       head=['Month', 'Write-off', 'Serious', 'Slight', hl('Totals', 'p', 4)])}
<p class="stem">In which month does Anne conclude the mailshot should be made?</p>""",
    options={'A': 'January', 'B': 'March', 'C': 'June', 'D': 'October', 'E': 'November'},
    notes=[(1, 'b', 'Most <b>cost</b>, not most accidents.'),
           (2, 'y', 'Write-off = 10 serious.'),
           (3, 'y', 'Serious = 10 slight. So write-off = 100 slight.'),
           (4, 'p', 'Trap column! It counts a write-off the same as a scratch.')],
    steps=[
        f"""<p>Give each kind a cost in “slight” units: <b>slight 1, serious 10, write-off 100</b>.
Only the five option months need checking:</p>
{calc('Jan: 3000 + 5390 + 2891 = 11 281', '<b>Mar: 3100 + 5500 + 2972 = 11 572</b>', 'Jun: 2400 + 5090 + 3230 = 10 720',
      'Oct: 3000 + 4740 + 3236 = 10 976', 'Nov: 2100 + 5780 + 2895 = 10 775')}""",
        f"""{_claims()}
{calc(f'biggest cost = {boxed("March")}')}
{note('Shortcut: March beats January on every column (31 v 30, 550 v 539, 2972 v 2891), so January is out without adding anything.', 'tip')}""",
    ],
    answer_text='March: 11 572 units, the most costly month.',
    why={'A': 'January comes second (11 281). March has more of every kind of accident than January.',
         'C': 'June has the most accidents in the <b>Totals</b> column (3763), but most are cheap slight ones.',
         'D': 'October has the most slight accidents (3236), and they cost the least.',
         'E': 'November has the most serious accidents (578), but only 21 write-offs.'},
    fast='Weight 100 : 10 : 1. March beats January on every column; June, October and November all come out under 11 000.',
))

# ---------------------------------------------------------------- 13 (Q26)
def _balance_moves():
    vals = [1290, 1140, 1320, 1070, 950, 1100, 1100, 1220, 1040, 1220, 1170, 1270]
    months = 'JFMAMJJASOND'
    X = lambda i: 52 + i * 48
    Yv = lambda v: 252 - (v - 880) * 0.44
    parts, lab = [], []
    for i, v in enumerate(vals):
        parts.append(rect(X(i), Yv(v), 32, 262 - Yv(v), k='ink', fill='paper', sw=1.6))
        lab.append(text(X(i) + 16, 284, months[i], k='ink', size=16, font='print'))
    for i in range(1, 12):
        d = vals[i] - vals[i - 1]
        col = 'green' if d > 0 else 'red' if d < 0 else 'muted'
        parts.append(line(X(i - 1) + 16, Yv(vals[i - 1]), X(i) + 16, Yv(vals[i]), k=col, w=3))
        sym = '↑' if d > 0 else '↓' if d < 0 else '='
        lab.append(text(X(i) + 16, 312, sym, k=col, size=24, font='print', weight='700'))
    lab.append(text(X(0) + 16, 312, '?', k='muted', size=22, font='print'))
    parts.append(path(f'M40 262 L{X(11) + 44} 262', k='ink', sw=2))
    lab.append(text(X(5) + 40, 30, 'bar tops (bottoms cut off): green = rise, red = fall', k='muted', size=15))
    return svg(640, 326, rough(*parts) + ''.join(lab),
               'Balance bar tops joined month to month: Feb down, Mar up, Apr down, May down, Jun up, Jul level, Aug up, Sep down, Oct up, Nov down, Dec up')

Q.append(dict(
    n=13, orig=26, answer='D', topic='Graphs: change',
    question=f"""<p>The graph below shows Mr Evans' {hl('bank balance at the end of each month', 'y', 1)} in a year.</p>
{fig(Y, 'ps_q13_balance', 'Bar chart of the balance, about 900 to 1300 pounds each month, January to December', 230)}
<p class="stem">Which one of the following graphs {hl('could', 'b', 2)} show the {hl('actual change in his bank balance each month', 'b', 3)}?</p>
{fig(Y, 'ps_q13_options', 'Five bar charts A to E of monthly change, from minus 300 to plus 300', 520)}""",
    options={'A': 'graph A', 'B': 'graph B', 'C': 'graph C', 'D': 'graph D', 'E': 'graph E'},
    notes=[(1, 'y', 'The heights are balances, not changes.'),
           (2, 'b', 'No exact numbers needed: the change bars just have to go the right way each month.'),
           (3, 'b', 'Change in a month = this month’s balance − last month’s. Up = positive bar, down = negative bar.')],
    steps=[
        f"""<p>We can’t check January (we don’t know last December’s balance). For February to December,
just ask: did the bar go <b>up</b>, <b>down</b> or stay <b>level</b>?</p>{_balance_moves()}""",
        f"""<p>Now compare each option’s bars, month by month (✗ = first wrong month):</p>
{table([['needed', '↓', '↑', '↓', '↓', '↑', '=', '↑', '↓', '↑', '↓', '↑', ''],
        ['A', '↓', '↑', '↓', '↓', '↑', hl('↑', 'p'), '↑', '↓', '↑', '↓', '↑', cross()],
        ['B', hl('↑', 'p'), '↓', '↑', '↑', '↓', '=', '↓', '↑', '↓', '↑', '↓', cross()],
        ['C', '↓', '↑', '↓', '↓', '↑', '=', '↑', '↓', '↑', '↓', hl('↓', 'p'), cross()],
        ['D', '↓', '↑', '↓', '↓', '↑', '=', '↑', '↓', '↑', '↓', '↑', tick()],
        ['E', hl('↑', 'p'), hl('↓', 'p'), '↑', '↓', '↑', '=', '↑', '↓', '↑', '↓', '↑', cross()]],
       head=['', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D', ''])}
{calc(f'only D matches every month {ar()} {boxed("D")}')}
{note('July is the giveaway: June and July balances are the same height, so July’s change must be zero (no bar). That kills A at once.', 'tip')}""",
    ],
    answer_text='Graph D: falls, rises and the zero in July all match the balance chart.',
    why={'A': 'A has a rise in July, but the balance is the same at the end of June and July: the change is zero.',
         'B': 'B is upside down: it shows every fall as a rise and every rise as a fall.',
         'C': 'C shows a fall in December, but the balance went up from November to December.',
         'E': 'E shows a rise in February and a fall in March, but the balance fell in February and rose in March.'},
    fast='Check the obvious months: July level (no bar), December up, February down. Only D passes all three.',
))

# ---------------------------------------------------------------- 14 (Q30)
def _settle():
    parts, lab = [], []
    people = {'Bill': (320, 104), 'Fred': (100, 250), 'Joe': (540, 250)}
    for name, (x, y) in people.items():
        lab.append(stick_person(x, y, k='pen', s=1.3))
        lab.append(text(x, y + 22, name, k='pen', size=19))
    parts += [arrow(140, 214, 290, 90, k='red', bend=-0.1), arrow(350, 90, 500, 214, k='red', bend=-0.1),
              arrow(505, 238, 135, 238, k='red', bend=0.08)]
    lab += [text(150, 132, 'Fred pays Bill £100', k='red', size=16),
            text(160, 152, '(300 − 200)', k='muted', size=14),
            text(492, 132, 'Bill pays Joe £50', k='red', size=16),
            text(484, 152, '(250 − 200)', k='muted', size=14),
            text(320, 222, 'Joe pays Fred £50  (150 − 100)', k='red', size=16),
            text(320, 300, 'Fred −100 + 50 = −50 · Joe +50 − 50 = 0 · Bill +100 − 50 = +50', k='ink', size=16),
            text(320, 330, 'so Fred pays Bill £50', k='green', size=22, font='scrawl')]
    return svg(640, 344, rough(*parts) + ''.join(lab),
               'Fred, Joe and Bill in a triangle with net payments between each pair: Fred to Bill 100, Bill to Joe 50, Joe to Fred 50; overall Fred pays Bill 50')

Q.append(dict(
    n=14, orig=30, answer='B', topic='Settling debts',
    question=f"""<p>Fred, Joe and Bill do plumbing, electrics and plastering respectively and work together on
certain building jobs. They will each take on any job involving all three types of work,
sub-contract to the others where necessary and {hl('sort out any payments at the end of the month', 'y', 1)}.</p>
<p>At the end of March, {hl('Bill has done £300 of work for Fred and £200 of work for Joe', 'g', 2)}. {hl('Joe has done £100 of work for Fred and £250 of work for Bill', 'g', 2)}. {hl('Fred has done £150 of work for Joe and £200 of work for Bill', 'g', 2)}.</p>
<p class="stem">Which of the following will {hl('settle their accounts', 'b', 3)}?</p>""",
    options={'A': 'Bill and Joe each pay Fred £25.', 'B': 'Fred pays Bill £50.', 'C': 'Fred and Joe each pay Bill £75.',
             'D': 'Bill pays Fred and Joe £100 each.', 'E': 'Joe pays Bill £150 and Fred £50.'},
    notes=[(1, 'y', 'One payment round that makes everyone square.'),
           (2, 'g', 'If X did work for Y, then Y owes X.'),
           (3, 'b', 'Find who is up and who is down overall.')],
    steps=[
        f"""<p>Net off each pair first (who did more work for whom?):</p>
{calc(f'Bill & Fred: Bill did 300, Fred did 200 {ar()} Fred owes Bill £100',
      f'Bill & Joe: Bill did 200, Joe did 250 {ar()} Bill owes Joe £50',
      f'Joe & Fred: Joe did 100, Fred did 150 {ar()} Joe owes Fred £50')}""",
        f"""{_settle()}""",
        f"""<p>Joe gets £50 and pays £50, so he drops out. Fred is £50 down and Bill is £50 up {ar()} {boxed('Fred pays Bill £50')}</p>
{note('Check with totals: work done minus work received. Bill 500 − 450 = +50, Joe 350 − 350 = 0, Fred 350 − 400 = −50. The pluses and minuses always add to zero.', 'check')}""",
    ],
    answer_text='Fred pays Bill £50: Fred is £50 down overall, Bill £50 up, Joe square.',
    why={'A': 'A has Fred <b>receiving</b> money, but Fred received £400 of work and only did £350: he owes.',
         'C': 'C makes Joe pay, but Joe did £350 of work and received £350, so he is square. Bill is only £50 up, not £150.',
         'D': 'D has Bill paying out £200, but Bill is owed money overall.',
         'E': 'E makes Joe pay £200, but Joe’s accounts already balance.'},
    fast='Work done − work received: Bill +50, Joe 0, Fred −50. Fred pays Bill £50.',
))

# ---------------------------------------------------------------- 15 (Q31)
def _basket():
    parts, lab = [], []
    items = (('aftershave', 'Rex', 'b'), ('shower gel', 'James', 'b'), ('shower gel', 'Henry', 'o'),
             ('body spray', 'Magnus', 'o'), ('talc', 'Tom', 'g'))
    for i, (item, who, f) in enumerate(items):
        x = 24 + i * 122
        parts.append(rect(x, 92, 106, 52, k='ink', fill=f, sw=1.8, rx=8))
        lab.append(text(x + 53, 116, item, k='ink', size=16))
        lab.append(text(x + 53, 136, who, k='muted', size=14))
    lab.append(brace(24, 252, 84, 'aftershave &amp; shower gel £3.49', k='pen', size=15, down=False))
    lab.append(brace(268, 496, 84, 'shower gel &amp; body spray £2.99', k='orange', size=15, down=False))
    lab.append(brace(512, 618, 84, 'talc £1.99', k='green', size=15, down=False))
    lab.append(text(320, 186, '3.49 + 2.99 + 1.99 = £8.47', k='red', size=22, font='scrawl'))
    return svg(640, 200, rough(*parts) + ''.join(lab),
               'Five presents grouped into packs: aftershave and shower gel 3.49, shower gel and body spray 2.99, talc 1.99, total 8.47')

Q.append(dict(
    n=15, orig=31, answer='C', topic='Best combination',
    question=f"""<p>Rachel intends to buy some toiletries for her {hl('five brothers', 'g', 1)} as a present. She thinks that
Rex would like aftershave, Tom talc, Magnus body spray and {hl('the twins, James and Henry, would like shower gel', 'p', 2)}. They all have a liking for "Jasmine" brand. Her budget is a
maximum of £10.00 and if she can spend less so much the better. She finds that the
{hl('items are available in combination packs as well as individually', 'y', 3)}. Prices are:</p>
{table([['Aftershave', '£2.99'], ['Body spray', '£1.99'], ['Talc', '£1.99'], ['Shower gel', '£1.49'], ['Aftershave &amp; talc', '£4.49'],
        ['Shower gel &amp; body spray', '£2.99'], ['Body spray double pack with free talc', '£3.95'], ['Aftershave &amp; shower gel', '£3.49']])}
<p class="stem">What is the {hl('least amount', 'b', 4)} of money Rachel must spend?</p>""",
    options={'A': '£7.48', 'B': '£8.46', 'C': '£8.47', 'D': '£8.97', 'E': '£9.95'},
    notes=[(1, 'g', 'Five presents to buy.'),
           (2, 'p', 'Twins = <b>two</b> shower gels.'),
           (3, 'y', 'Mix packs and single items to cover the list.'),
           (4, 'b', 'Cheapest way to get exactly what she needs.')],
    steps=[
        f"""<p>Shopping list: aftershave, talc, body spray and <b>2</b> shower gels. All single: </p>
{calc('2.99 + 1.99 + 1.99 + 1.49 + 1.49 = <b>£9.95</b>')}""",
        f"""<p>How much does each pack save, compared with buying its items singly?</p>
{calc('aftershave &amp; shower gel: 2.99 + 1.49 − 3.49 = <b>99p</b> saved',
      'shower gel &amp; body spray: 1.49 + 1.99 − 2.99 = <b>49p</b> saved',
      'aftershave &amp; talc: 2.99 + 1.99 − 4.49 = 49p saved',
      'double body spray + talc: she only needs one spray, so 1.99 + 1.99 − 3.95 = just 3p saved')}""",
        f"""<p>Use the two biggest savers that don’t overlap: aftershave &amp; shower gel (99p) and shower gel &amp; body spray (49p).
That uses both shower gels. Add talc on its own.</p>
{_basket()}
{calc(f'£9.95 − 99p − 49p = {boxed("£8.47")}')}""",
    ],
    answer_text='£8.47: aftershave & shower gel + shower gel & body spray + talc.',
    why={'A': '£7.48 buys only <b>one</b> shower gel (aftershave &amp; talc + shower gel &amp; body spray). The twins need one each.',
         'B': '£8.46 is all single prices but with only one shower gel.',
         'D': '£8.97 (aftershave &amp; talc + shower gel &amp; body spray + shower gel) covers the list, but is 50p dearer.',
         'E': '£9.95 buys everything singly and uses no deals.'},
    fast='Two shower gels! Pair one with the aftershave (3.49), one with the body spray (2.99), talc alone (1.99): £8.47.',
))

# ---------------------------------------------------------------- 16 (Q32)
def _smokers():
    parts, lab = [], []
    for r in range(10):
        for c in range(10):
            idx, x, y = r * 10 + c, 34 + c * 24, 36 + r * 24
            f = 'o' if idx < 30 else 'p' if idx < 40 else 'paper'
            parts.append(circle(x, y, 9, k='ink' if idx < 40 else 'muted', fill=f, sw=1.4))
            if 30 <= idx < 40:
                parts += [line(x - 6, y - 6, x + 6, y + 6, k='red', w=2), line(x - 6, y + 6, x + 6, y - 6, k='red', w=2)]
    lab += [text(296, 46, '100 adults', k='ink', size=19, anchor='start', font='scrawl'),
            text(296, 80, '1990: 40 smoke (orange + crossed)', k='ink', size=16, anchor='start'),
            text(296, 106, '1991: 30 smoke (orange)', k='ink', size=16, anchor='start'),
            text(296, 132, '10 gave up (crossed)', k='red', size=16, anchor='start'),
            text(296, 178, '10 out of 100 adults = 10%', k='muted', size=17, anchor='start'),
            text(296, 200, '(the survey’s figure)', k='muted', size=15, anchor='start'),
            text(296, 238, '10 out of 40 smokers = 25%', k='green', size=19, anchor='start', font='scrawl'),
            text(296, 260, '(the campaign’s figure)', k='green', size=15, anchor='start')]
    return svg(640, 282, rough(*parts) + ''.join(lab),
               'Grid of 100 adults: 40 smoked in 1990, 10 of them gave up; 10 out of 100 is 10 percent but 10 out of 40 smokers is 25 percent')

Q.append(dict(
    n=16, orig=32, answer='C', topic='Percentages: of what?',
    question=f"""<p>A survey claimed that in 1990 {hl('40% of the adult British population smoked', 'g', 1)}. It claimed
further that in 1991, after an anti-smoking campaign, {hl('only 30% of the adult British population smoked', 'g', 1)}. It reported a {hl('10% fall', 'p', 2)} in the number of smokers. However, the
campaign organisers, in their advertising, reported a {hl('25% fall', 'b', 3)} in the number of smokers.</p>
<p class="stem">The campaign organisers' advertisement reflects:</p>""",
    options={'A': 'the change in the number of smokers expressed as a percentage of the population in 1990.',
             'B': 'the change in the number of smokers expressed as a percentage of the population in 1991.',
             'C': 'the change in the number of smokers expressed as a percentage of smokers in 1990.',
             'D': 'the change in the number of smokers expressed as a percentage of smokers in 1991.',
             'E': 'the change in the size of the population expressed as a percentage of the population in 1990.'},
    notes=[(1, 'g', 'Both are percentages of <b>all adults</b>.'),
           (2, 'p', 'This 10% is 40 − 30: ten percentage points of the whole population.'),
           (3, 'b', 'Where does 25% come from? 25% = ¼. A quarter of what?')],
    steps=[
        f"""<p>Imagine 100 adults: 40 smokers in 1990, 30 in 1991. So <b>10 people</b> stopped.</p>{_smokers()}""",
        f"""<p>Which “whole” turns 10 into 25%?</p>
{calc(f'10 ÷ 100 adults = 10% {ar()} survey', f'10 ÷ 40 smokers in 1990 = {frac(1, 4)} = 25% {ar()} campaign ' + tick(),
      f'10 ÷ 30 smokers in 1991 = 33% ' + cross())}
{calc(f'25% = change as a percentage of the 1990 smokers {ar()} {boxed("C")}')}""",
    ],
    answer_text='C: 10 fewer smokers out of the 40 who smoked in 1990 is a 25% fall.',
    why={'A': 'As a share of the 1990 population the fall is 10 out of 100 = 10%: the survey’s figure, not 25%.',
         'B': 'As a share of the 1991 population it is still about 10%.',
         'D': 'Out of the 30 smokers in 1991 it would be 10 ÷ 30 = 33%.',
         'E': 'The size of the population hasn’t changed in the story; only the number of smokers did.'},
    fast='Fall = 10 points. 25% = 10 ÷ 40, and 40 is the 1990 smokers. C.',
))

# ---------------------------------------------------------------- 17 (Q36)
def _road():
    X = lambda km: 40 + km * 7
    parts, lab = [], []
    segs = ((0, 20, 'country, 90 km/h', 'g', '6.0 per 100 km', '0.2 × 6.0 = 1.2 l'),
            (20, 60, 'motorway, 110 km/h', 'b', '6.5 per 100 km', '0.4 × 6.5 = 2.6 l'),
            (60, 80, 'town, 50 km/h', 'o', '7.5 per 100 km', '0.2 × 7.5 = 1.5 l'))
    for a, b, name, f, rate, litres in segs:
        parts.append(rect(X(a), 70, X(b) - X(a), 38, k='ink', fill=f, sw=1.8))
        mid = (X(a) + X(b)) / 2
        lab += [text(mid, 58, name, k='ink', size=15), text(mid, 95, f'{b - a} km', k='ink', size=17),
                text(mid, 132, rate, k='muted', size=14), text(mid, 156, litres, k='pen', size=16)]
    lab.append(text(320, 198, '1.2 + 2.6 + 1.5 = 5.3 litres × 80c = 424c = $4.24', k='red', size=19, font='scrawl'))
    return svg(640, 212, rough(*parts) + ''.join(lab),
               'The 80 km drive split into 20 km country, 40 km motorway and 20 km town, using 1.2, 2.6 and 1.5 litres')

Q.append(dict(
    n=17, orig=36, answer='B', topic='Rates & fuel',
    question=f"""<p>The fuel consumption of Ted's new car is given in the manufacturer's data sheet as
follows:</p>
{table([[hl('Consumption l/100km', 'y', 1), '7.5', '6.0', '6.5']], head=['Speed', '50km/h', '90km/h', '110km/h'])}
<p>The cost of fuel is {hl('80c per litre', 'g', 2)}. Ted's journey to work consists of {hl('20km on country roads normally at 90km/h', 'g', 3)}, {hl('40km on motorway at 110km/h', 'g', 3)} and {hl('20km in town at 50km/h', 'g', 3)}.</p>
<p class="stem">How much does his drive to work cost him?</p>""",
    options={'A': '$4.16', 'B': '$4.24', 'C': '$4.26', 'D': '$4.40', 'E': '$5.30'},
    notes=[(1, 'y', 'Litres used for every 100 km. 20 km = 0.2 of that, 40 km = 0.4 of that.'),
           (2, 'g', '80 cents = $0.80 a litre.'),
           (3, 'g', 'Match each stretch to its speed column: don’t mix them up!')],
    steps=[
        f"""<p>Litres for each stretch = (km ÷ 100) × rate:</p>
{calc('country: 20 km at 90 km/h → 0.2 × 6.0 = 1.2 l', 'motorway: 40 km at 110 km/h → 0.4 × 6.5 = 2.6 l',
      'town: 20 km at 50 km/h → 0.2 × 7.5 = 1.5 l', 'total = <b>5.3 litres</b>')}""",
        f"""{_road()}
{calc(f'5.3 × 80c = 424c = {boxed("$4.24")}')}
{note('5.3 × 80: do 5 × 80 = 400 and 0.3 × 80 = 24.', 'tip')}""",
    ],
    answer_text='$4.24: 5.3 litres at 80c.',
    why={'A': '$4.16 = 5.2 litres: swaps the country and motorway rates (6.5 for country, 6.0 for motorway).',
         'C': '$4.26 is about what averaging the three rates gives (6.67 per 100 km × 80 km). The stretches are different lengths, so you can’t average like that.',
         'D': '$4.40 = 5.5 litres: uses the town rate 7.5 for the 40 km of motorway.',
         'E': '$5.30 is the number of litres (5.3), forgetting to multiply by 80c.'},
    fast='1.2 + 2.6 + 1.5 = 5.3 litres; × 0.8 = $4.24.',
))
