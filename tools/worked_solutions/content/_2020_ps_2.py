from wslib import *
from _2020_ps_1 import _tk, _cx

Y = 2020
Q = []


# ---------------------------------------------------------------- 9 (Q19)
def _june():
    cw, ch, x0, y0 = 62, 50, 20, 40
    parts, lab = [], []
    for i, d in enumerate('MTWTFSS'):
        lab.append(text(x0 + i * cw + cw / 2, 30, d, k='muted', size=16))
    for r, start in enumerate((10, 17, 24)):
        for c in range(7):
            d = start + c
            x, y = x0 + c * cw, y0 + r * ch
            show, hol = d <= 22, 19 <= d <= 26
            fill = 'g' if show and hol else 'y' if show else 'b' if hol else 'paper'
            parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k='ink', fill=fill, sw=1.5))
            lab.append(text(x + 8, y + 19, d, k='ink', size=14, font='print', anchor='start'))
            if d in (19, 22):
                lab.append(text(x + cw / 2, y + 40, 'matinee', k='pen', size=14))
    # Mondays 17 and 24
    for r in (1, 2):
        x, y = x0, y0 + r * ch
        parts.append(_cx(x + cw / 2 + 10, y + 32, 0.9))
    lab += [text(x0 + 7 * cw + 20, 62, 'yellow: Oliver! is on', k='ink', size=16, anchor='start'),
            text(x0 + 7 * cw + 20, 86, 'blue: we are there', k='ink', size=16, anchor='start'),
            text(x0 + 7 * cw + 20, 110, 'green: both', k='green', size=17, anchor='start'),
            text(x0 + 7 * cw + 20, 132, '= Wed 19 to Sat 22', k='green', size=17, anchor='start'),
            text(x0 + 7 * cw + 20, 166, 'Mon 17: not here yet', k='red', size=16, anchor='start'),
            text(x0 + 7 * cw + 20, 188, 'Mon 24: show over', k='red', size=16, anchor='start')]
    return svg(650, 200, rough(*parts) + ''.join(lab),
               'June calendar: the show runs to Saturday 22nd, the family is there from Wednesday 19th, so the overlap is Wednesday 19th to Saturday 22nd with no Monday')


_ADVERT = '<br>'.join([
    'The Southbourne Songsters present', 'OLIVER!', 'at the Pavilion Theatre',
    hl('from Monday 3rd June to Saturday 22nd June', 'p', 3), 'Nightly at 7.30pm',
    'Matinees Wednesdays &amp; Saturdays at 3pm', 'Adults: £12 (Matinees £10)', 'Children: £6 (Matinees £5)',
    hl('Family Ticket: £28 (all performances)', 'y', 4), '(2 adults and 2 children)',
    hl('Monday nights: £5 (all tickets)', 'p', 5)])

Q.append(dict(
    n=9, orig=19, answer='C', topic='Calendars & best price',
    question=f"""<p>I have booked {hl('myself, my wife and our three children', 'g', 1)} into The Wavecrest Hotel, Southbourne, for {hl('seven nights from June 19th', 'y', 2)}. The hotel has sent us a ‘What’s on’ booklet, and we are particularly keen to see <i>Oliver!</i>, the advertisement for which is shown below:</p>
<div style="line-height:2.1">{table([[_ADVERT]])}</div>
<p class="stem">What is the <b>{hl('least', 'b', 6)}</b> it could cost for us all to see <i>Oliver!</i> during our holiday in Southbourne?</p>""",
    options={'A': '£25', 'B': '£28', 'C': '£33', 'D': '£34', 'E': '£35'},
    notes=[(1, 'g', '2 adults + 3 children = 5 tickets.'),
           (2, 'y', 'They are there from the 19th to the 26th.'),
           (3, 'p', 'Monday 3rd, so the 10th, 17th and 24th are Mondays and the 19th is a Wednesday. The show <b>ends Saturday 22nd</b>.'),
           (4, 'y', 'Covers 2 adults + 2 children only. The 3rd child needs their own ticket.'),
           (5, 'p', '£5 each looks the cheapest, but is there a Monday they can actually go?'),
           (6, 'b', 'Cheapest possible way for all 5 to see it.')],
    steps=[
        f"""<p>Which days can they actually go? Draw June:</p>{_june()}
<p>No Monday falls in the green days, so the £5 Monday deal is out.</p>""",
        f"""<p>Price the best options for 5 people (2 adults, 3 children):</p>
{calc('5 separate matinee tickets: 2 × £10 + 3 × £5 = £35',
      'family ticket + 3rd child (evening): £28 + £6 = £34',
      f'family ticket + 3rd child (matinee, Wed 19 or Sat 22): £28 + £5 = {boxed("£33")}')}
{note('The family ticket is £28 at any performance, so use it at a matinee, where the extra child ticket is only £5.', 'tip')}""",
    ],
    answer_text='£33: the £28 family ticket plus a £5 child matinee ticket (Wednesday 19th or Saturday 22nd).',
    why={'A': '5 × £5 on a Monday night. But Monday 17th is before they arrive and Monday 24th is after the show has ended.',
         'B': 'The family ticket covers only 2 adults and 2 children. The third child still needs a ticket.',
         'D': 'Family ticket + a child’s <b>evening</b> ticket (£6). A matinee child ticket is £1 cheaper.',
         'E': 'Five separate matinee tickets (2 × 10 + 3 × 5). The family ticket saves £2.'},
    fast='They can go Wed 19 to Sat 22: no Monday. Family £28 + child matinee £5 = £33.',
))


# ---------------------------------------------------------------- 10 (Q20)
def _bits():
    parts, lab = [], []
    bits, x0, cw = '01000111', 150, 44
    lab.append(text(x0 - 14, 58, 'start', k='ink', size=19, anchor='end'))
    for i, b in enumerate(bits):
        parts.append(rect(x0 + i * cw, 30, cw - 4, 40, k='ink', fill='b' if b == '1' else 'paper', sw=1.6))
        lab.append(text(x0 + i * cw + (cw - 4) / 2, 58, b, k='ink', size=22, font='print'))
    lab.append(text(x0 + 8 * cw + 12, 58, 'four 1s', k='pen', size=20, font='scrawl', anchor='start'))
    lab.append(text(20, 108, 'What one move (flip two neighbours) can do:', k='ink', size=18, font='scrawl', anchor='start'))
    cases = [('00', '11', 'two more 1s (+2)', 'green'), ('11', '00', 'two fewer 1s (−2)', 'red'), ('01', '10', 'same number (0)', 'pen')]
    for r, (a, b, msg, col) in enumerate(cases):
        y = 124 + r * 50
        for j, (pair, px) in enumerate(((a, 40), (b, 200))):
            for i, ch_ in enumerate(pair):
                parts.append(rect(px + i * 38, y, 34, 36, k='ink', fill='b' if ch_ == '1' else 'paper', sw=1.5))
                lab.append(text(px + i * 38 + 17, y + 26, ch_, k='ink', size=20, font='print'))
        parts.append(arrow(124, y + 18, 190, y + 18, k='muted', bend=-0.15))
        lab.append(text(300, y + 25, msg, k=col, size=19, anchor='start'))
    lab.append(text(320, 296, 'The count of 1s only jumps by 2 or 0, so it stays EVEN', k='red', size=20, font='scrawl'))
    return svg(640, 312, rough(*parts) + ''.join(lab),
               'The start byte 01000111 has four 1s; a move changes the number of 1s by plus 2, minus 2 or 0, so it stays even')


Q.append(dict(
    n=10, orig=20, answer='C', topic='Patterns & parity',
    question=f"""<p>In computer technology, a bit can take two values: 0 or 1. A byte is composed of 8 bits.</p>
<p>I start with the following byte: {hl('01000111', 'g', 1)}</p>
<p>I {hl('choose two adjacent bits and change each of them to the opposite value', 'y', 2)} (that is, a 0 becomes a 1, and a 1 becomes a 0). {hl('I repeat this procedure a number of times.', 'p', 3)}</p>
<p class="stem">Which one of the following bytes <b>{hl('cannot', 'b', 4)}</b> be the result?</p>""",
    options={'A': '01001011', 'B': '11111111', 'C': '10101011', 'D': '10111101', 'E': '00001111'},
    notes=[(1, 'g', 'Count its 1s: there are 4.'),
           (2, 'y', 'Every move flips <b>two</b> neighbouring bits at the same time.'),
           (3, 'p', 'Any number of moves, so don’t try to trace paths. Look for something that never changes.'),
           (4, 'b', 'Find the one that is impossible.')],
    steps=[
        f"""<p>Look at what one move does to the <b>number of 1s</b>:</p>{_bits()}""",
        f"""<p>The start has four 1s (even), so every result must have an even number of 1s. Count them:</p>
{calc(f'A 01001011 {ar()} 4 {tick()}', f'B 11111111 {ar()} 8 {tick()}', f'C 10101011 {ar()} <b>5</b> {cross()} odd!',
      f'D 10111101 {ar()} 6 {tick()}', f'E 00001111 {ar()} 4 {tick()}')}
<p>Only C has an odd number of 1s {ar()} {boxed('C')}</p>""",
        f"""{note('The even ones really can be reached. E: 01000111 → 00100111 → 00010111 → 00001111 (slide the 1 along). A: flip bits 5 and 6 once.', 'check')}""",
    ],
    answer_text='10101011: it has five 1s, but every move keeps the number of 1s even.',
    why={'A': 'Four 1s. Flipping bits 5 and 6 of 01000111 gives 01001011 in one move.',
         'B': 'Eight 1s. Flip bits 1–2 (10000111), then 2–3 (11100111), then 4–5 (11111111).',
         'D': 'Six 1s. Flip 1–2, 3–4, 5–6, then 6–7: 10000111 → 10110111 → 10111011 → 10111101.',
         'E': 'Four 1s. Flip 2–3, 3–4, 4–5 to slide the first 1 along: 00001111.'},
    fast='Each move changes the number of 1s by 2 or 0. Start has four (even). Only C has an odd number (five).',
))


# ---------------------------------------------------------------- 11 (Q24)
def _daytrip():
    x0 = 46
    X = lambda h, m: x0 + ((h * 60 + m) - 690) * 2
    parts, lab = [], []
    # time axis
    for h, name in ((12, '12:00'), (13, '1:00'), (14, '2:00'), (15, '3:00'), (16, '4:00')):
        parts.append(line(X(h, 0), 30, X(h, 0), 250, k='muted', w=1, dash=True))
        lab.append(text(X(h, 0), 22, name, k='muted', size=14))
    lab.append(text(x0, 22, '11:30', k='ink', size=14))
    parts.append(line(x0, 30, x0, 250, k='green', w=2.4))
    parts.append(line(X(16, 15), 30, X(16, 15), 250, k='red', w=2.4))
    lab.append(text(X(16, 15) - 4, 268, 'leave 4:15', k='red', size=15, anchor='end'))
    lab.append(text(x0 + 4, 268, 'arrive 11:30', k='green', size=15, anchor='start'))
    # row 1: the fixed slots
    lab.append(text(x0 + 6, 52, 'Fixed slots:', k='ink', size=18, font='scrawl', anchor='start'))
    parts.append(rect(X(13, 0), 62, X(14, 20) - X(13, 0), 28, k='ink', fill='o', sw=1.6))
    lab.append(text((X(13, 0) + X(14, 20)) / 2 - 16, 82, 'tour 1:00', k='ink', size=15))
    parts.append(rect(X(14, 0), 96, X(14, 55) - X(14, 0), 28, k='ink', fill='v', sw=1.6))
    lab.append(text((X(14, 0) + X(14, 55)) / 2, 116, 'museum 2:00', k='ink', size=15))
    parts.append(rect(X(14, 0), 58, X(14, 20) - X(14, 0), 70, k='red', sw=3))
    lab.append(text(X(14, 10), 146, 'clash!', k='red', size=20, font='scrawl'))
    parts.append(rect(X(15, 0), 62, X(16, 20) - X(15, 0), 28, k='red', sw=1.6, rx=2))
    lab.append(text((X(15, 0) + X(16, 15)) / 2, 82, '3 pm tour: too late', k='red', size=14))
    # row 2: the plan without the tour
    lab.append(text(x0 + 6, 178, 'Miss the tour:', k='ink', size=18, font='scrawl', anchor='start'))
    blocks = [((11, 45), (12, 40), 'maze', 'b'), ((12, 40), (13, 5), 'lunch', 'y'),
              ((14, 0), (14, 55), 'museum', 'v'), ((14, 55), (16, 10), 'walk', 'g')]
    for (h1, m1), (h2, m2), name, f in blocks:
        parts.append(rect(X(h1, m1), 188, X(h2, m2) - X(h1, m1), 32, k='ink', fill=f, sw=1.6))
        lab.append(text((X(h1, m1) + X(h2, m2)) / 2, 210, name, k='ink', size=15))
    for (h, m), s in (((11, 45), '11:45'), ((12, 40), '12:40'), ((13, 5), '1:05'), ((14, 55), '2:55'), ((16, 10), '4:10')):
        lab.append(text(X(h, m), 240, s, k='pen', size=14))
    parts.append(_tk(X(15, 40), 166))
    return svg(650, 280, rough(*parts) + ''.join(lab),
               'Timeline from 11:30 to 4:15: the 1 pm tour and the 2 pm museum overlap; without the tour, maze, lunch, museum and walk all fit')


Q.append(dict(
    n=11, orig=24, answer='C', topic='Timetables & scheduling',
    question=f"""<p>I had planned my day trip to the stately home very carefully, but then the bus was late. I won’t arrive until {hl('11:30 am', 'g', 1)} and will have to leave by {hl('4:15 pm', 'g', 2)}. There were five things that I had wanted to do and I had written these down in the table below:</p>
{table([['visit the museum', '55 minutes', hl('11 am or 2 pm', 'p', 3)],
        ['visit the maze', '55 minutes', 'every half hour (at quarter past and quarter to the hour)'],
        ['take the guided tour', '80 minutes', hl('1 pm or 3 pm', 'p', 4)],
        ['walk in the grounds', '75 minutes', 'any time'],
        ['have lunch in the café', '25 minutes', hl('between 12:30 pm and 2:00 pm', 'y', 5)]],
       head=['<i>activity</i>', '<i>length of time</i>', '<i>start times</i>'])}
<p class="stem">Which activity should I {hl('miss out so that I can still do the other four', 'b', 6)}?</p>""",
    options={'A': 'visit the museum', 'B': 'visit the maze', 'C': 'take the guided tour', 'D': 'walk in the grounds',
             'E': 'have lunch in the café'},
    notes=[(1, 'g', 'Too late for the 11 am museum visit!'),
           (2, 'g', '11:30 to 4:15 is 4 h 45 min = 285 minutes.'),
           (3, 'p', 'Only the 2 pm museum is left: 2:00 to 2:55.'),
           (4, 'p', 'The 3 pm tour ends at 4:20, after you must leave. So the tour can only be 1:00 to 2:20.'),
           (5, 'y', 'Lunch has to start inside this window.'),
           (6, 'b', 'Drop one activity so the other four fit with no overlaps.')],
    steps=[
        f"""<p>Two activities have no choice of time:</p>
{calc('museum: 11 am is gone, so 2:00 → 2:55', 'tour: 3 pm ends 4:20 (too late), so 1:00 → 2:20',
      f'they overlap from 2:00 to 2:20 {ar()} you must drop the museum or the tour')}
{note('Also, all five add up to 55 + 55 + 80 + 75 + 25 = 290 minutes, but there are only 285. Something has to go.', 'check')}""",
        f"""<p>Try dropping the <b>museum</b>. The tour fills 1:00–2:20. Lunch must start by 2:00, so it has to be before the tour (about 12:30–12:55).</p>
<ul><li>Before lunch: 11:30–12:30 is only 60 min. The maze starts 11:45 and ends 12:40 {cross()}; the walk needs 75 min {cross()}</li>
<li>After the tour: 2:20–4:15 is 115 min, but maze + walk = 55 + 75 = 130 min {cross()}</li></ul>
<p>So keeping the tour doesn’t work.</p>""",
        f"""<p>Drop the <b>tour</b> instead:</p>{_daytrip()}
{calc('maze 11:45–12:40, lunch 12:40–1:05, museum 2:00–2:55, walk 2:55–4:10 ' + tick(), f'miss out {boxed("the guided tour")}')}""",
    ],
    answer_text='Miss the guided tour: then maze, lunch, museum (2 pm) and the walk all fit before 4:15.',
    why={'A': 'Without the museum the tour (1:00–2:20) forces lunch before 1 pm, and then the maze and walk (130 min) can’t fit in the 115 min after 2:20.',
         'B': 'Dropping the maze leaves the museum (2:00) and the tour (1:00–2:20) still clashing.',
         'D': 'Dropping the walk still leaves the museum and tour clash.',
         'E': 'Dropping lunch still leaves the museum and tour clash.'},
    fast='Museum must be 2:00 (11:00 is gone). Tour must be 1:00 (3:00 ends 4:20). They overlap, so the answer is A or C. Without the tour it all fits.',
))


# ---------------------------------------------------------------- 12 (Q25)
def _april():
    cw, ch, x0, y0 = 54, 42, 16, 40
    parts, lab = [], []
    for i, d in enumerate('MTWTFSS'):
        lab.append(text(x0 + i * cw + cw / 2, 30, d, k='muted', size=16))
    days = [('30', 'm'), ('31', 'm')] + [(str(d), 'a') for d in range(1, 31)] + [(f'{d}', 'May') for d in range(1, 7)]
    for idx, (d, kind) in enumerate(days):
        r, c = divmod(idx, 7)
        x, y = x0 + c * cw, y0 + r * ch
        n = int(d)
        april = kind == 'a'
        wed, fri = c == 2, c == 4
        away = april and 22 <= n <= 27
        if wed and april and n == 22:
            fill, tag, tk = 'g', 'break', 'green'
        elif wed and kind != 'm':
            fill, tag, tk = 'p', 'lecture', 'red'
        elif away:
            fill, tag, tk = 'g', 'no fly' if fri else '', 'muted'
        else:
            fill, tag, tk = 'paper', 'no fly' if fri else '', 'muted'
        sw, kk = (3, 'green') if (april and n in (21, 28)) else (1.4, 'muted' if kind == 'm' else 'ink')
        parts.append(rect(x + 2, y + 2, cw - 4, ch - 4, k=kk, fill=fill, sw=sw))
        lab.append(text(x + 7, y + 17, d if kind != 'May' or n > 1 else '1 May', k='muted' if kind == 'm' else 'ink',
                        size=14, font='print', anchor='start'))
        if april and n == 21:
            tag, tk = 'out', 'green'
        if april and n == 28:
            tag, tk = 'back', 'green'
        if tag:
            lab.append(text(x + cw / 2, y + 35, tag, k=tk, size=14))
    tx = 410
    lines = [('A  4 → 6: only 1 day there', 'red'), ('B  9 → 14: 15 + 24 = £39', 'ink'),
             ('C  9 → 28: away on Wed 15', 'red'), ('D  21 → 28: 20 + 10 = £30', 'green'),
             ('E  30 → 5 May: 24 + 20 = £44', 'ink')]
    lab.append(text(tx, 52, 'The options:', k='ink', size=18, font='scrawl', anchor='start'))
    for i, (s, col) in enumerate(lines):
        lab.append(text(tx, 84 + i * 30, s, k=col, size=16, anchor='start'))
    lab.append(text(tx, 248, 'only Wed 22 can be missed', k='green', size=16, anchor='start'))
    return svg(660, 300, rough(*parts) + ''.join(lab),
               'April calendar with lecture Wednesdays in pink, Wednesday 22nd free, and trip D from Tuesday 21st to Tuesday 28th in green')


Q.append(dict(
    n=12, orig=25, answer='D', topic='Calendars & charts',
    question=f"""<p>Steven would like to book return flights from London to Pescara, Italy. He would like to spend {hl('at least 3 days in Pescara excluding the days of his flights', 'y', 1)}. Steven has {hl('lectures in London every Wednesday that he must attend', 'p', 2)}. However, {hl('there are no lectures during the 20th–24th April spring break', 'y', 3)}.</p>
<p>The prices of flights between London and Pescara are shown for the time period Steven would like to make the trip. {hl('The airline does not have any flights between these destinations on Fridays.', 'g', 4)}</p>
{fig(Y, 'ps_q12_flights', 'Two bar charts of flight prices: London to Pescara for each day of April, and Pescara to London from 4 April to 8 May', 620)}
<p class="stem">If he books the {hl('cheapest flights possible to allow him to travel according to his requirements', 'b', 5)}, on which days will he depart and return?</p>""",
    options={'A': 'Depart: Saturday 04 April; Return: Monday 06 April',
             'B': 'Depart: Thursday 09 April; Return: Tuesday 14 April',
             'C': 'Depart: Thursday 09 April; Return: Tuesday 28 April',
             'D': 'Depart: Tuesday 21 April; Return: Tuesday 28 April',
             'E': 'Depart: Thursday 30 April; Return: Tuesday 05 May'},
    notes=[(1, 'y', 'Count only the full days <b>between</b> the two flights: need 3 or more.'),
           (2, 'p', 'He must be in London on Wednesdays 1, 8, 15 and 29 April and 6 May.'),
           (3, 'y', 'Wednesday 22nd is free: the only Wednesday he may be away.'),
           (4, 'g', 'Gaps in the charts = no flight that day.'),
           (5, 'b', 'Throw out trips that break a rule, then add the two prices and take the cheapest.')],
    steps=[
        f"""<p>Check each option against the rules on a calendar:</p>{_april()}""",
        f"""<p>A and C break the rules. Read the prices for the rest (out + back):</p>
{calc('B: Thu 9 out £15, Tue 14 back £24 = £39', f'D: Tue 21 out £20, Tue 28 back £10 = <b>£30</b> {tick()}',
      'E: Thu 30 out £24, Tue 5 May back £20 = £44', f'cheapest allowed {ar()} {boxed("D")}')}
{note('A (£30) and C (£25) look cheap, which is the trap. A gives only one full day (Sunday 5th); C misses the lecture on Wednesday 15th.', 'trap')}""",
    ],
    answer_text='Depart Tuesday 21 April (£20), return Tuesday 28 April (£10): £30, and the only Wednesday missed is the 22nd.',
    why={'A': 'Only Sunday 5th is a full day in Pescara; he needs at least 3.',
         'B': 'Allowed, but £15 + £24 = £39, more than D’s £30.',
         'C': 'The cheapest pair (£15 + £10), but he would be away on Wednesday 15th, a lecture day.',
         'E': 'Allowed, but £24 + £20 = £44.'},
    fast='Strike out A (1 day) and C (misses Wed 15). Then B £39, D £30, E £44. D.',
))


# ---------------------------------------------------------------- 13 (Q26)
def _offers():
    rows = [('Twinpack 25% off', 'pay 1½ for 2', 75, 'g'), ('A  2nd half price', 'pay 1½ for 2', 75, 'g'),
            ('B  50% extra free', 'pay 1 for 1½', 66.7, 'p'), ('C  3 for 2', 'pay 2 for 3', 66.7, 'p'),
            ('D  25% off next one', 'pay 1¾ for 2', 87.5, 'p'), ('E  5 for 4', 'pay 4 for 5', 80, 'p')]
    s, bx = 3.6, 220
    parts, lab = [], []
    lab.append(text(bx, 26, 'cost of each item, as % of the normal price', k='muted', size=15, anchor='start'))
    for i, (name, pay, v, f) in enumerate(rows):
        y = 40 + i * 42
        parts.append(rect(bx, y, v * s, 30, k='ink', fill=f, sw=1.6))
        lab.append(text(bx - 10, y + 21, name, k='green' if f == 'g' else 'ink', size=16, anchor='end'))
        lab.append(text(bx + 8, y + 21, pay, k='ink', size=15, anchor='start'))
        lab.append(text(bx + v * s + 8, y + 21, f'{v:g}%', k='green' if f == 'g' else 'ink', size=16, anchor='start'))
    parts.append(line(bx + 75 * s, 34, bx + 75 * s, 300, k='green', w=2, dash=True))
    lab.append(text(bx + 75 * s, 318, '75% line', k='green', size=15))
    return svg(640, 326, rough(*parts) + ''.join(lab),
               'Bars of price per item: twinpack 75 percent, A 75, B 66.7, C 66.7, D 87.5, E 80; only A matches')


Q.append(dict(
    n=13, orig=26, answer='A', topic='Percentages & offers',
    question=f"""<p>The current 'Special Offer' gimmick at Fareprice involves putting a band marked {hl("'TWINPACK - 25% OFF'", 'y', 1)} around {hl('pairs', 'g', 2)} of selected items, such as washing powder.</p>
<p class="stem">Which one of the following 'Special Offers' is {hl('exactly the same', 'b', 3)} as Fareprice's?</p>""",
    options={'A': "'Buy one - Get a second for half price.'", 'B': 'A larger packet containing 50% extra for no extra cost.',
             'C': "'Three for the price of two.'", 'D': 'A coupon on each packet which gives 25% off the cost of the next packet.',
             'E': "'Five for the price of four.'"},
    notes=[(1, 'y', '25% off the <b>pair</b>: you pay 75% of 2 items = 1½ items’ worth.'),
           (2, 'g', 'You get 2 items each time.'),
           (3, 'b', 'Same deal = same goods for the same money, not just “a discount”.')],
    steps=[
        f"""<p>Twinpack in plain numbers:</p>
{calc('2 items at 100% = 200%', f'25% off {ar()} pay 150% {ar()} “2 for the price of 1½”', 'each item costs 75% of normal')}""",
        f"""<p>Work out the cost of each item for every offer:</p>{_offers()}
{calc(f'A: 100% + 50% = 150% for 2 {ar()} 75% each {tick()}', 'B: 100% for 1½ → 66.7% each', 'C: 200% for 3 → 66.7% each',
      'D: 100% + 75% = 175% for 2 → 87.5% each', 'E: 400% for 5 → 80% each')}""",
        f"""<p>Only A gives 2 items for the price of 1½ {ar()} {boxed('A')}</p>""",
    ],
    answer_text='“Buy one, get a second half price”: 2 items for 1½ times the price, exactly like 25% off a pair.',
    why={'B': '50% extra free = 1½ for the price of 1, so each costs ⅔ of normal: a bigger saving (33%).',
         'C': '3 for 2 = 33⅓% off each item, more than 25%.',
         'D': 'Only the <b>next</b> packet is 25% off, so 2 packets cost 1¾: just 12.5% off overall (and you have to come back).',
         'E': '5 for 4 = 20% off each item, less than 25%.'},
    fast='Twinpack = pay 1.5 for 2. Buy one + second half price = 1 + 0.5 = 1.5 for 2. Same.',
))


# ---------------------------------------------------------------- 14 (Q30)
def _joyce():
    parts, lab = [], []
    bw, bh = 118, 54

    def box(x, y, t, sub, k='ink', fill='paper'):
        parts.append(rect(x, y, bw, bh, k=k, fill=fill, sw=2, rx=8))
        lab.append(text(x + bw / 2, y + 24, t, k=k if k != 'ink' else 'ink', size=21, weight='bold'))
        lab.append(text(x + bw / 2, y + 44, sub, k='ink', size=14))

    y1, y2 = 58, 204
    xs = [500, 340, 180, 20]
    box(xs[0], y1, '13:45', 'bus home', k='pen', fill='b')
    box(xs[1], y1, '13:40', 'leave shop')
    box(xs[2], y1, '9:40', 'start work')
    box(xs[3], y1, '9:35', 'off the bus')
    for (a, b), lbl in zip(((xs[0], xs[1]), (xs[1], xs[2]), (xs[2], xs[3])), ('5 min walk', '4 hours', '5 min walk')):
        parts.append(arrow(a - 4, y1 + bh / 2, b + bw + 4, y1 + bh / 2, k='red', bend=-0.12))
        lab.append(text((a + b + bw) / 2, y1 - 10, lbl, k='red', size=16))
    parts.append(arrow(xs[3] + bw / 2, y1 + bh + 4, xs[3] + bw / 2, y2 - 6, k='red', bend=0.0))
    lab.append(text(xs[3] + bw / 2 + 10, (y1 + bh + y2) / 2 + 6, '− 30 min (slowest bus)', k='red', size=16, anchor='start'))
    box(20, y2, '9:05', 'latest bus time')
    box(220, y2, '9:00', 'the 9:00 bus')
    box(420, y2, '8:55', 'leave home', k='green', fill='g')
    parts.append(arrow(20 + bw + 4, y2 + bh / 2, 220 - 4, y2 + bh / 2, k='red', bend=0.12))
    lab.append(text(20 + bw + 41, y2 - 12, 'buses at :00, :30', k='red', size=15))
    parts.append(arrow(220 + bw + 4, y2 + bh / 2, 420 - 4, y2 + bh / 2, k='red', bend=0.12))
    lab.append(text(220 + bw + 41, y2 - 12, '5 min walk', k='red', size=15))
    lab.append(text(20, 20, 'Work backwards from the bus home:', k='ink', size=18, font='scrawl', anchor='start'))
    return svg(640, 276, rough(*parts) + ''.join(lab),
               'Chain working backwards: 13:45 bus, 13:40 leave shop, 9:40 start, 9:35 off bus, 9:05 latest bus, so the 9:00 bus, leave home 8:55')


Q.append(dict(
    n=14, orig=30, answer='C', topic='Time & working backwards',
    question=f"""<p>Joyce has decided to volunteer to work in the local High Street Charity Shop. She has agreed to be in the shop for {hl('4 hours', 'g', 1)} on a Saturday.</p>
<p>To get from her home to the High Street, Joyce will have to travel by bus. Her {hl('walk from home to the bus stop is no more than 5 minutes', 'g', 2)}, and the bus journey each way takes {hl('between 20 and 30 minutes', 'p', 3)} depending on traffic.</p>
<p>Buses from Joyce’s home leave for the High Street at 30 minute intervals, {hl('on the hour and on the half hour', 'y', 4)}. Return buses for Joyce leave the High Street at 30 minute intervals, at 15 minutes past the hour and 15 minutes to the hour.</p>
<p>The {hl('walk to and from the bus stops to the Charity Shop is no more than 5 minutes', 'g', 5)}.</p>
<p>Joyce wants to catch the {hl('13:45 bus home', 'g', 6)} after working in the shop.</p>
<p class="stem">What is the {hl('latest time that she should leave home', 'b', 7)} for work?</p>""",
    options={'A': '08:25', 'B': '08:30', 'C': '08:55', 'D': '09:00', 'E': '09:25'},
    notes=[(1, 'g', '4 full hours inside the shop.'),
           (2, 'g', 'Allow the full 5 minutes.'),
           (3, 'p', 'Plan for the worst case: <b>30</b> minutes, or she could be late.'),
           (4, 'y', 'Buses out only at :00 and :30.'),
           (5, 'g', '5 minutes at the shop end, both before and after work.'),
           (6, 'g', 'Start here and work backwards.'),
           (7, 'b', 'Latest time that is <b>always</b> safe, whatever the traffic.')],
    steps=[
        f"""<p>Work backwards from the 13:45 bus, always assuming the slowest times:</p>{_joyce()}""",
        f"""{calc('13:45 − 5 min walk = 13:40 (leave shop)', '13:40 − 4 h = 9:40 (start work)', '9:40 − 5 min walk = 9:35 (off the bus)',
      f'9:35 − 30 min = 9:05 {ar()} last bus at or before 9:05 is the <b>9:00</b>', f'9:00 − 5 min walk = {boxed("08:55")}')}
{note('The 9:30 bus could arrive at 10:00, twenty minutes after she should start. Too risky.', 'check')}""",
    ],
    answer_text='08:55: walk 5 minutes to catch the 9:00 bus, which arrives by 9:30 at the latest.',
    why={'A': '08:25 catches the 8:30 bus. Safe, but she could leave half an hour later.',
         'B': '08:30 is the time of an earlier bus, and leaving then means missing it (5 min walk).',
         'D': '09:00 is when the bus leaves. She needs 5 minutes to walk to the stop.',
         'E': '09:25 means the 9:30 bus, which could arrive at 10:00. (It comes from 13:45 − 4 h − 20 min, using the fastest bus and no walks.)'},
    fast='13:45 − 5 − 4 h − 5 − 30 = 9:05, so the 9:00 bus, so leave at 8:55.',
))


# ---------------------------------------------------------------- 15 (Q31)
def _tickets():
    parts, lab = [], []
    X = lambda t: 30 + t * 0.58
    bands = [(0, 200, 'g', '$20', 'first 200'), (200, 500, 'y', '$30', 'next 300'), (500, 1000, 'o', '$35', 'next 500')]
    for a, b, f, p, name in bands:
        parts.append(rect(X(a), 44, X(b) - X(a), 34, k='ink', fill=f, sw=1.6))
        lab.append(text((X(a) + X(b)) / 2, 67, p, k='ink', size=18))
        lab.append(text((X(a) + X(b)) / 2, 36, name, k='muted', size=14))
    for t in (200, 500):
        lab.append(text(X(t), 96, t, k='red', size=15))
    lab.append(text(30, 20, 'Saturday’s 1000 tickets, in the order they are sold:', k='ink', size=16, anchor='start'))
    fills = {'20': 'g', '30': 'y', '35': 'o'}
    rows = [(['30'] * 10, 'all 10 in one band: 10 × $30 = $300', 'ink'),
            (['20'] * 5 + ['30'] * 5, 'across 200: 5 × $20 + 5 × $30 = $250', 'ink'),
            (['30'] * 5 + ['35'] * 5, 'across 500: 5 × $30 + 5 × $35 = $325', 'ink')]
    for r, (cells, msg, col) in enumerate(rows):
        y = 120 + r * 46
        for i, c in enumerate(cells):
            parts.append(rect(30 + i * 22, y, 19, 30, k='ink', fill=fills[c], sw=1.3, rx=2))
        lab.append(text(260, y + 21, msg, k=col, size=17, anchor='start'))
    lab.append(text(30, 286, '$20/$30 mix: 210, 220, 230 … 290 (always ends in 0)', k='pen', size=17, anchor='start'))
    lab.append(text(30, 312, '$30/$35 mix: 305, 310, 315 … 345', k='pen', size=17, anchor='start'))
    lab.append(text(610, 300, '$275?', k='red', size=24, font='scrawl', anchor='end'))
    parts.append(_cx(620, 292, 0.8))
    return svg(640, 326, rough(*parts) + ''.join(lab),
               'Saturday price bands 20, 30 and 35 dollars, with ten tickets in a row falling inside one band or across a boundary')


Q.append(dict(
    n=15, orig=31, answer='B', topic='Price bands',
    question=f"""<p>The prices for tickets to a concert are set based on the day of the performance and {hl('the number of tickets that have been sold so far', 'p', 1)}. The table below shows the ticket prices. There are 1000 tickets on sale for each performance.</p>
{table([['Monday–Thursday', '$15', '$20', '$25'], ['Friday', '$20', '$25', '$30'],
        [hl('Saturday', 'y', 2), hl('$20', 'y'), hl('$30', 'y'), hl('$35', 'y')], ['Sunday', '$25', '$35', '$45']],
       head=['<i>Day</i>', '<i>First 200 tickets</i>', '<i>Next 300 tickets</i>', '<i>Next 500 tickets</i>'])}
<p>I need to buy {hl('10 tickets', 'g', 3)} for Saturday’s performance. I will buy {hl('all of them in one purchase', 'y', 4)} this afternoon.</p>
<p class="stem">Which of the following is <b>{hl('not', 'b', 5)}</b> a price that I might have to pay for the tickets?</p>""",
    options={'A': '$250', 'B': '$275', 'C': '$300', 'D': '$325', 'E': '$350'},
    notes=[(1, 'p', 'We don’t know how many are sold already, so the 10 tickets could land anywhere, even across a price change.'),
           (2, 'y', 'Saturday only: $20, then $30, then $35.'),
           (3, 'g', '10 tickets.'),
           (4, 'y', 'One purchase = 10 tickets in a row. Some can be in one band and the rest in the next.'),
           (5, 'b', 'Find the total that can never happen.')],
    steps=[
        f"""<p>Picture the 10 tickets as a block sliding along the 1000:</p>{_tickets()}""",
        f"""<p>List every possible total:</p>
{calc('all in one band: $200, $300 or $350', 'some at $20, rest at $30: each $20 → $30 swap adds $10 → 210, 220 … 290',
      'some at $30, rest at $35: each swap adds $5 → 305, 310 … 345')}
{calc(f'A $250 {tick()}  C $300 {tick()}  D $325 {tick()}  E $350 {tick()}', f'B $275: between 200 and 300 but not a multiple of 10 {ar()} {boxed("impossible")}')}""",
    ],
    answer_text='$275: totals between $200 and $300 come from mixing $20 and $30 tickets, so they always end in 0.',
    why={'A': '$250 = 5 tickets at $20 + 5 at $30 (if 195 are already sold).',
         'C': '$300 = all 10 at $30.',
         'D': '$325 = 5 at $30 + 5 at $35 (if 495 are already sold).',
         'E': '$350 = all 10 at $35.'},
    fast='Below $300 the tickets are a mix of $20s and $30s, so the total is a multiple of 10. $275 isn’t.',
))


# ---------------------------------------------------------------- 16 (Q32)
def _ribbons():
    s, x0 = 6, 112
    rows = [('60 cm, £6', [12] * 5, 0, '5 × 12'), ('60 cm, £6', [12] * 5, 0, '5 × 12'),
            ('50 cm, £5', [12] * 4, 2, '4 × 12, 2 cm spare'), ('50 cm, £5', [7] * 7, 1, '7 × 7, 1 cm spare'),
            ('50 cm, £5', [7] * 7, 1, '7 × 7, 1 cm spare')]
    parts, lab = [], []
    for r, (name, pieces, waste, msg) in enumerate(rows):
        y = 40 + r * 48
        lab.append(text(x0 - 10, y + 22, name, k='ink', size=16, anchor='end'))
        x = x0
        for p in pieces:
            parts.append(rect(x, y, p * s, 32, k='ink', fill='b' if p == 12 else 'o', sw=1.5))
            lab.append(text(x + p * s / 2, y + 22, p, k='ink', size=15))
            x += p * s
        if waste:
            parts.append(rect(x, y, waste * s, 32, k='red', fill='p', sw=1.5))
        lab.append(text(x0 + 60 * s + 12, y + 22, msg, k='pen', size=16, anchor='start'))
    lab.append(text(x0, 24, 'blue = 12 cm pieces, orange = 7 cm pieces, pink = waste', k='muted', size=15, anchor='start'))
    lab.append(text(330, 300, '14 twelves ✓  14 sevens ✓  £6 + £6 + £5 + £5 + £5 = £27', k='green', size=19, font='scrawl'))
    return svg(660, 316, rough(*parts) + ''.join(lab),
               'Cutting plan: two 60 cm ribbons give ten 12 cm pieces, one 50 cm gives four more, two 50 cm ribbons give fourteen 7 cm pieces; total 27 pounds')


Q.append(dict(
    n=16, orig=32, answer='B', topic='Best buy & cutting',
    question=f"""<p>Bert has agreed to make {hl('14 decorations', 'g', 1)} for his daughter’s birthday. Each decoration will require {hl('two gold ribbons, one 12 cm long and the other 7 cm long', 'g', 2)}.</p>
<p>The table shows the lengths and prices of available gold ribbon.</p>
<p style="margin-bottom:.2em"><i>gold ribbon price list</i></p>
{table([['30 cm', '£4.00'], ['50 cm', '£5.00'], ['60 cm', '£6.00']], head=['gold ribbon length', 'price'])}
<p>The ribbon {hl('can be easily cut to size', 'y', 3)} for the decorations, but {hl('short pieces of ribbon cannot be joined to make longer lengths', 'p', 4)}.</p>
<p class="stem">What is the {hl('least amount', 'b', 5)} that Bert will need to spend on gold ribbon for the 14 decorations?</p>""",
    options={'A': '£26.00', 'B': '£27.00', 'C': '£28.00', 'D': '£29.00', 'E': '£30.00'},
    notes=[(1, 'g', 'So 14 pieces of 12 cm and 14 pieces of 7 cm.'),
           (2, 'g', 'Total length: 14 × (12 + 7) = 14 × 19 = 266 cm.'),
           (3, 'y', 'One long ribbon can be cut into lots of pieces.'),
           (4, 'p', 'Each piece must come from a single ribbon. Leftover scraps are wasted.'),
           (5, 'b', 'Cheapest set of ribbons that can be cut into all 28 pieces.')],
    steps=[
        f"""<p>Price per cm:</p>
{calc('30 cm for £4 = 13.3p per cm (worst)', '50 cm for £5 = 10p per cm', '60 cm for £6 = 10p per cm')}
<p>So only use 50s and 60s, at 10p per cm. 266 cm at 10p is £26.60, so it costs <b>at least £27</b>.</p>
{note('£26 buys at most 260 cm (for example 4 × 50 + 60), which is less than 266 cm. So £26 is impossible.', 'check')}""",
        f"""<p>£27 buys 3 × 50 cm + 2 × 60 cm = 270 cm, just 4 cm spare. Can we cut it with almost no waste? Cut the 12s and 7s separately:</p>
{calc('60 = 5 × 12 exactly', '50 = 7 × 7 + 1 spare', '50 = 4 × 12 + 2 spare')}
{_ribbons()}""",
        f"""{calc(f'2 × £6 + 3 × £5 = {boxed("£27")}')}""",
    ],
    answer_text='£27: two 60 cm ribbons and three 50 cm ribbons, cut as shown with only 4 cm wasted.',
    why={'A': '£26 buys at most 260 cm of ribbon, but 14 × 19 = 266 cm is needed.',
         'C': 'Cutting the 7 cm pieces from 60 cm ribbons (8 per ribbon) needs 60 + 50 = £11 for the sevens instead of 50 + 50 = £10.',
         'D': 'Making whole decorations (19 cm sets) from each ribbon: 4 × 60 cm (3 sets each) + 1 × 50 cm (2 sets) = £29. That wastes ribbon.',
         'E': 'Five 60 cm ribbons: 300 cm, 34 cm more than needed.'},
    fast='Need 266 cm at best 10p/cm, so at least £27. It works: 12s from 60 + 60 + 50, 7s from 50 + 50.',
))
