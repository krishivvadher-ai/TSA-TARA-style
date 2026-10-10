from wslib import *

Y = 2018
Q = []

# ---------------------------------------------------------------- 17 (Q36)
def _profits():
    rows = [('pens', 12, 150), ('crayons', 6, 180), ('rulers', 25, 40), ('felt tips', 6, 150), ('pencils', 4, 200)]
    X = lambda p: 130 + p * 0.18
    parts, lab = [line(X(0), 22, X(0), 214, k='ink', w=2)], []
    for i, (name, each, n) in enumerate(rows):
        y = 30 + i * 37
        tot = each * n
        top = i < 2
        parts.append(rect(X(0), y, X(tot) - X(0), 24, k='ink', fill='g' if top else 'b', sw=1.5))
        lab.append(text(120, y + 18, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(tot) + 8, y + 18, f'{each}p × {n} = £{tot / 100:.2f}', k='green' if top else 'ink', size=15, anchor='start',
                        weight='700' if top else None))
    lab.append(text(X(0), 236, 'profit in one week', k='muted', size=14, anchor='start'))
    return svg(660, 246, rough(*parts) + ''.join(lab),
               'Weekly profit: pens 18 pounds, crayons 10.80, rulers 10, felt tips 9, pencils 8; pens and crayons are the top two')

Q.append(dict(
    n=17, orig=36, answer='B', topic='Profit & unit costs',
    question=f"""<p>At the start of the school year, a village shop stocks and sells a range of stationery items.
The table below shows details of the wholesale costs and retail prices for a number of the items
sold.</p>
{table([['crayons', '48p', '10p', '180'], ['felt tips', '72p', '12p', '150'], ['pencils', '24p', '6p', '200'],
        ['pens', '36p', '15p', '150'], ['rulers', '60p', '30p', '40']],
       head=['<i>items</i>', f'<i>wholesale cost {hl("per pack of 12", "p", 1)}</i>', f'<i>retail selling price {hl("per 1 item", "p", 2)}</i>',
             f'<i>{hl("number sold in one week", "g", 3)}</i>'])}
<p class="stem">Of the five items sold, which two together made the {hl('most profit', 'b', 4)} for the shop owner?</p>""",
    options={'A': 'crayons and pencils', 'B': 'crayons and pens', 'C': 'felt tips and pencils', 'D': 'felt tips and rulers', 'E': 'pens and rulers'},
    notes=[(1, 'p', 'Cost is for 12 items: divide by 12 to get the cost of one.'),
           (2, 'p', 'Selling price is for one item. Compare like with like.'),
           (3, 'g', 'Total profit = profit per item × number sold.'),
           (4, 'b', 'Most total profit in the week, not the biggest profit on one item.')],
    steps=[
        f"""<p>Profit on one item = selling price − (pack cost ÷ 12):</p>
{calc('crayons: 10 − 48 ÷ 12 = 10 − 4 = 6p', 'felt tips: 12 − 72 ÷ 12 = 12 − 6 = 6p', 'pencils: 6 − 24 ÷ 12 = 6 − 2 = 4p',
      'pens: 15 − 36 ÷ 12 = 15 − 3 = 12p', 'rulers: 30 − 60 ÷ 12 = 30 − 5 = 25p')}""",
        f"""<p>Times by the number sold:</p>{_profits()}
{calc(f'top two: pens £18.00 + crayons £10.80 = £28.80 {ar()} {boxed("crayons and pens")}')}
{note('Rulers make the most per item (25p) but only 40 are sold: £10, just behind crayons’ £10.80.', 'trap')}""",
    ],
    answer_text='Crayons and pens: £10.80 + £18.00 = £28.80 profit.',
    why={'A': 'Crayons and pencils make £10.80 + £8.00 = £18.80.',
         'C': 'Felt tips and pencils make £9.00 + £8.00 = £17.00, the two smallest.',
         'D': 'Felt tips and rulers make £9.00 + £10.00 = £19.00.',
         'E': 'Pens and rulers make £18.00 + £10.00 = £28.00: close, but rulers (£10) are just behind crayons (£10.80). Tempting because rulers have the biggest profit per item.'},
    fast='Profit per item 6, 6, 4, 12, 25p; times sales: 1080, 900, 800, 1800, 1000p. Top two are pens and crayons.',
))

# ---------------------------------------------------------------- 18 (Q37)
def _booth():
    X = lambda t: 50 + t * 34
    parts = [line(X(0), 110, X(17), 110, k='ink', w=2, head=True)]
    lab = []
    for t in range(0, 17):
        parts.append(line(X(t), 104, X(t), 116, k='muted', w=1.2))
        if t % 3 == 0:
            lab.append(text(X(t), 136, f'{t}', k='ink', size=15))
    for i in range(6):
        t = 3 * i
        me = i == 5
        parts.append(circle(X(t), 80, 13, k='green', fill='g', sw=2))
        lab.append(text(X(t), 86, i + 1, k='ink', size=16, weight='700'))
        if i:
            parts.append(arrow(X(t - 3) + 14, 60, X(t) - 14, 60, k='red', bend=-0.3))
            lab.append(text(X(t - 1.5), 38, '3 min', k='red', size=14))
    parts.append(circle(X(15), 80, 20, k='red', sw=2.4))
    lab += [text(X(15), 160, 'me: 15 min', k='red', size=19, font='scrawl'),
            text(X(17), 136, 'min', k='muted', size=14),
            text(X(0), 160, 'green light on', k='green', size=15, anchor='start'),
            text(X(0), 180, '(person 1 pays at once)', k='green', size=14, anchor='start')]
    # photo timing for person 1 (irrelevant)
    parts.append(rect(X(0), 196, X(6) - X(0), 18, k='muted', fill='paper', sw=1.4))
    parts.append(line(X(2), 196, X(2), 214, k='muted', w=1.4))
    lab += [text(X(1), 210, 'photo', k='muted', size=12), text(X(4), 210, 'developing', k='muted', size=12),
            text(X(6) + 10, 210, 'person 1’s photos: don’t affect the queue', k='muted', size=14, anchor='start')]
    return svg(660, 226, rough(*parts) + ''.join(lab),
               'Timeline: the green light comes on every 3 minutes, so people pay at 0, 3, 6, 9, 12 and the sixth person at 15 minutes')

Q.append(dict(
    n=18, orig=37, answer='A', topic='Timings & queues',
    question=f"""<p>There is an automatic photograph booth in my local shopping centre. {hl('It takes exactly 2 minutes from the time that the money is inserted for the photographs to be taken, then the developed photographs appear 4 minutes later', 'p', 1)}.</p>
<p>{hl('Money may only be inserted when the green light is on', 'y', 2)}. This light goes out immediately after
money is inserted, and {hl('comes back on again exactly 3 minutes later', 'g', 3)}.</p>
<p>This morning, I arrived at the booth just as it was being switched on, and I was {hl('sixth in the queue', 'g', 4)}. {hl('The first person inserted their money immediately', 'y', 5)}, and the rest of us all inserted our
money as soon as we were allowed to.</p>
<p class="stem">How long after I arrived at the booth did {hl('I insert my money', 'b', 6)}?</p>""",
    options={'A': '15 minutes', 'B': '18 minutes', 'C': '21 minutes', 'D': '25 minutes', 'E': '30 minutes'},
    notes=[(1, 'p', 'Red herring! The 2 + 4 minutes of photo time doesn’t control when the next person can pay.'),
           (2, 'y', 'The only rule for paying: wait for the green light.'),
           (3, 'g', 'So a new person can pay every 3 minutes.'),
           (4, 'g', 'Five people pay before me.'),
           (5, 'y', 'Person 1 pays at 0 minutes, not at 3.'),
           (6, 'b', 'When I <b>pay</b>, not when my photos come out.')],
    steps=[
        f"""<p>The light allows one payment every 3 minutes, starting at 0:</p>{_booth()}""",
        f"""{calc('person 1 at 0, 2 at 3, 3 at 6, 4 at 9, 5 at 12', f'me (6th): 5 gaps × 3 = {boxed("15 minutes")}')}
{note('Fence-post trap: 6 people means only 5 gaps of 3 minutes, because person 1 pays at time 0.', 'trap')}""",
    ],
    answer_text='15 minutes: payments at 0, 3, 6, 9, 12 and then mine at 15.',
    why={'B': '18 = 6 × 3 counts six gaps. Person 1 paid straight away, so there are only five.',
         'C': '21 adds the 6 minutes for my own photos (15 + 6), but the question asks when I put my money in.',
         'D': '25 = 5 × 5: it thinks the light comes back 3 minutes after the photos are taken (2 + 3).',
         'E': '30 = 5 × 6: it waits for each person’s photos to come out (2 + 4) before the next person pays.'},
    fast='One payment every 3 minutes from time 0. Sixth person: 5 × 3 = 15.',
))

# ---------------------------------------------------------------- 19 (Q38)
def _map():
    X = lambda e: 70 + (e - 75) * 58
    Yn = lambda n: 24 + (66 - n) * 40
    parts, lab = [], []
    for e in range(75, 85):
        parts.append(line(X(e), Yn(66), X(e), Yn(60), k='muted', w=1.2))
        lab.append(text(X(e), Yn(60) + 20, e, k='pen', size=15))
    for n in range(60, 67):
        parts.append(line(X(75), Yn(n), X(84), Yn(n), k='muted', w=1.2))
        lab.append(text(X(75) - 8, Yn(n) + 5, n, k='pen', size=15, anchor='end'))
    places = [('Hilltop', 76.3, 61.3, ''), ('Riverside', 78.1, 61.4, 'Y'), ('Topfield', 77.7, 63.4, 'V'),
              ('Longwood', 78.7, 63.4, 'W'), ('High Moor', 79.2, 62.6, 'X'), ('Sunnybank', 80.4, 61.3, 'Z'),
              ('Stakefell', 79.3, 65.8, ''), ('Highscar', 77.3, 64.9, ''), ('Little Tarn', 82.5, 60.5, ''),
              ('Lower Green', 83.7, 65.4, ''), ('West Pasture', 81.5, 64.2, '')]
    for name, e, n, letter in places:
        key = name in ('Topfield', 'Longwood')
        col = 'red' if name == 'Longwood' else ('orange' if key else 'ink')
        parts.append(circle(X(e), Yn(n), 5 if key else 4, k=col, fill='ink' if not key else 'paper', sw=2))
        tag = f'{letter} = {name}' if letter else name
        dy = -10 if name not in ('Riverside', 'Little Tarn') else 18
        anchor, dx = 'middle', 0
        if name == 'Lower Green':
            anchor, dx = 'end', 6
        elif name == 'Topfield':
            anchor, dx = 'end', -6
        elif name == 'Longwood':
            anchor, dx = 'start', 6
        elif name == 'High Moor':
            anchor, dx, dy = 'start', 9, 5
        lab.append(text(X(e) + dx, Yn(n) + dy, tag, k=col, size=13 if not key else 15, anchor=anchor,
                        weight='700' if key else None))
    lab.append(brace(X(77.7), X(78.7), Yn(63.4) + 10, '1 square', k='red', size=12))
    lab.append(text(X(79.5), Yn(60) + 42, 'gridline numbers filled in (eastings along the bottom, northings up the side)', k='muted', size=14))
    return svg(660, 316, rough(*parts) + ''.join(lab),
               'The map with eastings 75 to 84 and northings 60 to 66: V is Topfield at 777634 and W is Longwood at 787634, one square to its right')

Q.append(dict(
    n=19, orig=38, answer='B', topic='Maps & grid references',
    question=f"""<p>The diagram below shows part of a map of Ruralia.</p>
{fig(Y, 'ps_q19_map', 'A 9 by 6 grid with eleven dots, five labelled V, W, X, Y and Z; V and W are side by side in the third row', 320)}
<p>A group of students are on an expedition and must meet their teacher at {hl('Longwood, grid reference 787634', 'b', 1)}. Unfortunately, they have been given a version of the map with the {hl('numbers missing from the gridlines', 'p', 2)}, and the place names have been omitted too. They have a list of grid
references for some places on the map, and are trying to work out which point to head for in
order to be sure of meeting their teacher.</p>
{fig(Y, 'ps_q19_grid', 'Example square: gridlines 16, 17, 18 across and 42, 43, 44 up, with P just right of 17 and just above 42', 130)}
<p>They have a set of instructions showing how the grid references work:</p>
<p>The grid reference of point P is 172427. Go to vertical line to the west of the point, read the
number 17. Estimate how many tenths across the square the point appears at, hence 172. Go
to horizontal line to the south of point P, read the number 42, estimate how many tenths up the
square the point is, hence 427. This gives 172427 as the complete grid reference number.</p>
<p>Here is the list of the grid references / place names the students have been given.</p>
{table([['Hilltop', '763613', 'Riverside', '781614'], ['Sunnybank', '804613', hl('Topfield', 'y', 3), hl('777634', 'y')],
        ['High Moor', '792626', hl('Longwood', 'y'), hl('787634', 'y')], ['Highscar', '773649', 'Stakefell', '793658'],
        ['West Pasture', '815642', 'Lower Green', '837654'], ['Little Tarn', '825605', '', '']])}
<p class="stem">Using this information to help you, which of the places marked on the map is Longwood?</p>""",
    options={'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z'},
    notes=[(1, 'b', '787634: easting 78.7 (across), northing 63.4 (up).'),
           (2, 'p', 'You can’t just read it off. Use the pattern of the places to work out the numbers.'),
           (3, 'y', 'Look! Topfield 777634 has the <b>same</b> northing as Longwood, and its easting is exactly 10 less = one square to the west.')],
    steps=[
        f"""<p>Hunt for a pair in the list that makes an easy shape. Topfield 777<b>634</b> and Longwood 787<b>634</b>:</p>
{calc('same northing 634 → same height on the map', 'eastings 777 and 787 → 1 whole square apart', 'Longwood has the bigger easting → it is the one on the right')}
<p>On the map only V and W sit at the same height exactly one square apart. So V is Topfield and {boxed("W is Longwood")}.</p>""",
        f"""<p>Check by filling in the numbers (left edge 75, bottom edge 60); every dot then matches the list:</p>{_map()}
{note('Second check: Hilltop 763613 and Sunnybank 804613 share a northing and are 4.1 squares apart. That is the dot in the 2nd row from the bottom on the left and Z.', 'check')}""",
    ],
    answer_text='W: it is one square east of V (Topfield), at the same height.',
    why={'A': 'V is Topfield (777634): same height as Longwood but one square further west.',
         'C': 'X is High Moor (792626).',
         'D': 'Y is Riverside (781614): it has a 78 easting like Longwood, but sits two squares lower.',
         'E': 'Z is Sunnybank (804613).'},
    fast='Topfield 777634 and Longwood 787634: same height, one square apart. Only V and W fit; the eastern one, W, is Longwood.',
))

# ---------------------------------------------------------------- 20 (Q42)
def _tiles():
    nums = ['8', '9', '15', '26', '37', '40']
    parts, lab = [], []
    x = 40
    for n in nums:
        for ch in n:
            f = 'o' if ch in '1234' and len(n) == 2 and ch == n[0] else ('g' if ch == '0' else ('b' if len(n) == 1 else 'paper'))
            parts.append(rect(x, 40, 38, 46, k='ink', fill=f, sw=1.8, rx=4))
            lab.append(text(x + 19, 72, ch, k='ink', size=26, font='print'))
            x += 40
        x += 26
    lab += [text(80, 30, 'one-digit balls', k='pen', size=15),
            text(420, 30, 'tens digits must be 1, 2, 3, 4', k='orange', size=15)]
    Xn = lambda v: 40 + v * 13.5
    parts.append(line(Xn(0), 150, Xn(45), 150, k='ink', w=2))
    for v in (8, 9, 15, 26, 37, 40):
        parts.append(circle(Xn(v), 150, 7, k='pen', fill='paper', sw=2))
        lab.append(text(Xn(v), 178, v, k='pen', size=15))
    parts.append(line(Xn(8), 124, Xn(40), 124, k='red', w=2, head=True, tail=True))
    lab += [text(Xn(24), 116, 'range = 40 − 8 = 32', k='red', size=19, font='scrawl'),
            text(Xn(0), 204, 'all ten digits 0–9 used once; 0 hides in 40, 8 and 9 are the two single balls', k='ink', size=15, anchor='start')]
    return svg(660, 214, rough(*parts) + ''.join(lab),
               'The draw 8, 9, 15, 26, 37, 40 uses each digit once; on a number line the range from 8 to 40 is 32')

Q.append(dict(
    n=20, orig=42, answer='E', topic='Digits & logic',
    question=f"""<p>In the main draw of a lottery, six of the balls (which are {hl('numbered from 1 to 49', 'y', 1)}) are selected at
random, then the numbers chosen are rearranged and displayed in ascending numerical order.</p>
<p>For instance: &nbsp; 3 &nbsp; 17 &nbsp; 20 &nbsp; 29 &nbsp; 34 &nbsp; 45</p>
<p>In one draw recently, I noticed that the six numbers were made up of {hl('a total of ten digits, all different', 'g', 2)}. The lowest number on this occasion was 1 and the highest number was 49, so the
range of the six numbers was 48, the greatest possible range for the lottery main draw.</p>
<p class="stem">What is the {hl('smallest possible range', 'b', 3)} when the six numbers in the main draw of the lottery have
a total of ten digits, all different?</p>""",
    options={'A': '21', 'B': '23', 'C': '27', 'D': '31', 'E': '32'},
    notes=[(1, 'y', 'Two-digit balls can only start with 1, 2, 3 or 4. There is no ball 0.'),
           (2, 'g', 'Ten different digits = every digit 0 to 9 exactly once.'),
           (3, 'b', 'Range = highest − lowest. Make the top small and the bottom big.')],
    steps=[
        f"""<p>How many two-digit numbers? Six numbers with ten digits:</p>
{calc('6 numbers + 1 extra digit per two-digit number = 10', f'{ar()} <b>four</b> two-digit numbers and <b>two</b> one-digit numbers')}""",
        f"""<p>The four two-digit numbers need four different tens digits, and only 1, 2, 3, 4 are allowed:</p>
{calc('tens digits are exactly 1, 2, 3 and 4 → the top number is in the 40s',
      '0 can’t be a ball on its own, so it is a units digit: put it in 40 → top = <b>40</b>',
      'the two single balls come from 5, 6, 7, 8, 9 → biggest choice 8 and 9 → lowest = <b>8</b>')}""",
        f"""{_tiles()}
{calc(f'range = 40 − 8 = {boxed("32")}')}""",
    ],
    answer_text='32, for example 8, 9, 15, 26, 37, 40.',
    why={'A': '21 would need the top ball in the 20s or 30s, but four different tens digits force a ball in the 40s.',
         'B': '23 has the same problem: the top ball is at least 40, and the lowest is at most 8, so the range is at least 32.',
         'C': '27 would need a top of 35 or so: impossible, since one two-digit ball must start with 4.',
         'D': '31 is 40 − 9: it forgets there are <b>two</b> single-digit balls. If 9 is one, the other is smaller and becomes the lowest.'},
    fast='Four two-digit balls → tens 1, 2, 3, 4 → top at least 40 (use the 0). Two single balls from 5–9, best 8 and 9. 40 − 8 = 32.',
))

# ---------------------------------------------------------------- 21 (Q43)
def _parking():
    X = lambda h: 110 + h * 60
    parts, lab = [], []
    parts.append(rect(X(0), 34, X(7.5) - X(0), 22, k='ink', fill='y', sw=1.5))
    lab.append(text(100, 50, 'at work', k='ink', size=15, anchor='end'))
    lab.append(text((X(0) + X(7.5)) / 2, 50, '7½ hours', k='ink', size=15))
    parts.append(rect(X(0), 72, X(8) - X(0), 26, k='ink', fill='p', sw=1.5))
    lab.append(text(100, 90, 'one ticket', k='ink', size=15, anchor='end'))
    lab.append(text((X(0) + X(8)) / 2, 90, '8 hours £6.20', k='ink', size=15))
    x0 = 0
    for h, cost, f in ((3, '£1.70', 'g'), (3, '£1.70', 'g'), (2, '£1.20', 'b')):
        parts.append(rect(X(x0), 116, X(x0 + h) - X(x0), 26, k='ink', fill=f, sw=1.5))
        lab.append(text((X(x0) + X(x0 + h)) / 2, 134, f'{h} h {cost}', k='ink', size=15))
        x0 += h
    lab.append(text(100, 134, 'best mix', k='green', size=15, anchor='end'))
    for h in range(0, 9):
        parts.append(line(X(h), 156, X(h), 164, k='muted', w=1.2))
        lab.append(text(X(h), 182, h, k='muted', size=13))
    parts.append(line(X(0), 160, X(8), 160, k='muted', w=1.2))
    lab += [text(X(4), 210, '£1.70 + £1.70 + £1.20 = £4.60   →   saves £6.20 − £4.60 = £1.60', k='red', size=17, font='scrawl')]
    return svg(660, 222, rough(*parts) + ''.join(lab),
               'Timeline: 7.5 hours at work; one 8-hour ticket at 6.20 against 3 + 3 + 2 hours of tickets at 4.60')

Q.append(dict(
    n=21, orig=43, answer='C', topic='Best deal',
    question=f"""<p>Car parking charges are shown in the table below. Brian wants to park his car for a period
of {hl('7.5 hours', 'g', 1)}, whilst he is at work. He buys a ticket in the morning when he arrives at the car
park. Due to the close proximity of the car park to his place of work, he is able to {hl('return to his car to buy a new ticket as many times as needed', 'y', 2)}.</p>
{table([['1 hour', '£0.80'], ['2 hours', '£1.20'], [hl('3 hours', 'g'), hl('£1.70', 'g')], ['4 hours', '£2.40'], ['5 hours', '£3.50'],
        ['6 hours', '£4.20'], ['7 hours', '£5.20'], [hl('8 hours', 'p', 4), hl('£6.20', 'p')], ['over 8 hours', '£8.20']],
       head=[f'<i>{hl("up to", "y", 3)}</i>', '<i>car parking charges</i>'])}
<p class="stem">What is the {hl('most Brian can save', 'b', 5)} by returning to the car to buy new tickets compared to buying
one 8-hour ticket?</p>""",
    options={'A': '£1.10', 'B': '£1.40', 'C': '£1.60', 'D': '£2.10', 'E': '£3.60'},
    notes=[(1, 'g', 'Tickets come in whole hours, so he needs tickets adding up to at least 8 hours (7 isn’t enough).'),
           (2, 'y', 'He can chain several short tickets.'),
           (3, 'y', '“Up to”: a 3-hour ticket covers anything up to 3 hours.'),
           (4, 'p', 'Compare with this £6.20 ticket, not the “over 8 hours” price.'),
           (5, 'b', 'Most saving = cheapest mix of tickets.')],
    steps=[
        f"""<p>Which ticket is the best value per hour?</p>
{calc('1 h: 80p an hour', '2 h: 120 ÷ 2 = 60p an hour', '3 h: 170 ÷ 3 ≈ 57p an hour ← best', '4 h: 240 ÷ 4 = 60p an hour', '5 h and up: 70p an hour or more')}""",
        f"""<p>Make 8 hours using as many 3-hour tickets as possible:</p>
{calc('3 + 3 + 2 = 8 h: 1.70 + 1.70 + 1.20 = <b>£4.60</b>', 'other tries: 4 + 4 = £4.80, 2 + 2 + 2 + 2 = £4.80, 3 + 3 + 3 = £5.10')}
{_parking()}
{calc(f'saving = 6.20 − 4.60 = {boxed("£1.60")}')}""",
    ],
    answer_text='£1.60: two 3-hour tickets and one 2-hour ticket cost £4.60 instead of £6.20.',
    why={'A': '£1.10 uses three 3-hour tickets (£5.10), which buys a whole hour he doesn’t need.',
         'B': '£1.40 uses two 4-hour tickets (or four 2-hour tickets) for £4.80, not the cheapest mix.',
         'D': '£2.10 uses 4 + 3 hours (£4.10), but 7 hours doesn’t cover his 7½ hours.',
         'E': '£3.60 compares £4.60 with the “over 8 hours” price (£8.20) instead of the 8-hour ticket.'},
    fast='3-hour tickets are best value. 8 h = 3 + 3 + 2 = £4.60. 6.20 − 4.60 = £1.60.',
))

# ---------------------------------------------------------------- 22 (Q44)
NETS22 = {1: ['LR', 'B', 'B', 'B', 'BT', 'LR'], 2: ['BT', 'B', 'T', 'B', 'BT', 'LR'], 3: ['LR', 'T', 'B', 'T', 'BT', 'LR'],
          4: ['LR', 'B', 'T', 'T', 'BT', 'LR'], 5: ['BT', 'B', 'T', 'B', 'BT', 'BT']}


def _net(ox, oy, w, cells, singles=True, sw=1.4):
    parts = []
    pos = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1)]
    for i, ((c, r), tri) in enumerate(zip(pos, cells)):
        x, y = ox + c * w, oy + r * w
        single = singles and i in (1, 2, 3)
        parts.append(rect(x, y, w, w, k='ink', fill='y' if single else 'paper', sw=sw))
        cx, cy = x + w / 2, y + w / 2
        corners = {'T': [(x, y), (x + w, y)], 'R': [(x + w, y), (x + w, y + w)], 'B': [(x + w, y + w), (x, y + w)], 'L': [(x, y + w), (x, y)]}
        for t in tri:
            parts.append(poly(corners[t] + [(cx, cy)], k='ink', fill='ink', sw=1))
        parts.append(line(x, y, x + w, y + w, k='ink', w=1))
        parts.append(line(x + w, y, x, y + w, k='ink', w=1))
    return parts


def _cube22():
    cx, cy, s = 150, 128, 84
    h = 0.866 * s
    Bk, Rt, F, Lt = (cx, cy - s), (cx + h, cy - s / 2), (cx, cy), (cx - h, cy - s / 2)
    Lb, Fb, Rb = (cx - h, cy + s / 2), (cx, cy + s), (cx + h, cy + s / 2)
    Ct, Cl, Cr = (cx, cy - s / 2), (cx - h / 2, cy + s / 4), (cx + h / 2, cy + s / 4)
    parts = [poly([Bk, Rt, F, Lt], k='ink', fill='paper', sw=2), poly([Lt, F, Fb, Lb], k='ink', fill='paper', sw=2),
             poly([F, Rt, Rb, Fb], k='ink', fill='paper', sw=2),
             poly([Lt, F, Ct], k='ink', fill='ink', sw=1), poly([F, Fb, Cl], k='ink', fill='ink', sw=1), poly([Rt, Rb, Cr], k='ink', fill='ink', sw=1),
             line(*Lt, *Rt, k='ink', w=1), line(*Bk, *F, k='ink', w=1), line(*Lt, *Fb, k='ink', w=1), line(*F, *Lb, k='ink', w=1),
             line(*F, *Rb, k='ink', w=1), line(*Rt, *Fb, k='ink', w=1)]
    lab = [text(cx, cy - s - 10, 'top', k='pen', size=17), text(Lb[0] - 8, Lb[1] + 10, 'left', k='pen', size=17, anchor='end'),
           text(Rb[0] + 8, Rb[1] + 10, 'right', k='pen', size=17, anchor='start')]
    tx = 330
    lab += [text(tx, 40, 'Only 3 faces have ONE black triangle;', k='ink', size=16, anchor='start'),
            text(tx, 60, 'the other 3 have two (a bow-tie).', k='ink', size=16, anchor='start'),
            text(tx, 98, 'Which edge does each lone', k='pen', size=17, font='scrawl', anchor='start'),
            text(tx, 118, 'triangle lean on?', k='pen', size=17, font='scrawl', anchor='start'),
            text(tx, 150, 'top → leans on LEFT', k='red', size=17, anchor='start'),
            text(tx, 176, 'left → leans on RIGHT', k='red', size=17, anchor='start'),
            text(tx, 202, 'right → leans on the outside', k='red', size=17, anchor='start'),
            text(tx, 236, 'a chain: top → left → right → out', k='ink', size=16, anchor='start')]
    return svg(660, 250, rough(*parts) + ''.join(lab),
               'The cube: the top face’s triangle touches the left face, the left face’s touches the right face, the right face’s touches its outer edge')


def _nets22():
    parts, lab = [], []
    w = 30
    spots = {1: (20, 40), 2: (240, 40), 3: (460, 40), 4: (130, 170), 5: (350, 170)}
    verdict = {1: ('two lean on S3', 'red'), 2: ('two lean outwards', 'red'), 3: ('S2, S3 lean on each other', 'red'),
               4: ('a chain ✓', 'green'), 5: ('two lean outwards', 'red')}
    for n, (ox, oy) in spots.items():
        parts += _net(ox, oy, w, NETS22[n])
        lab.append(text(ox + 2.5 * w, oy - 10, f'net {n}', k='ink', size=16, weight='700'))
        lab.append(text(ox + 2.5 * w, oy + 2 * w + 22, verdict[n][0] + (' ✗' if n != 4 else ''), k=verdict[n][1], size=15))
    return svg(660, 280, rough(*parts) + ''.join(lab),
               'The five nets with their three single-triangle squares shaded; only net 4 has the chain the cube needs')


def _net4():
    w, ox, oy = 58, 40, 40
    parts = _net(ox, oy, w, NETS22[4], sw=2)
    s1, s2, s3 = (ox + w, oy), (ox + 2 * w, oy), (ox + 2 * w, oy + w)
    parts += [arrow(s1[0] + w / 2, s1[1] + w - 8, s3[0] + 10, s3[1] + w / 2 + 6, k='red', bend=0.4),
              arrow(s3[0] + w / 2 + 18, s3[1] + 12, s2[0] + w / 2 + 18, s2[1] + w - 12, k='red', bend=-0.6)]
    lab = [text(s1[0] + w / 2, oy + w * 0.3 + 5, 'S1', k='pen', size=14, weight='700'),
           text(s2[0] + w / 2 - 8, oy + w * 0.8 + 5, 'S2', k='pen', size=14, weight='700'),
           text(s3[0] + w / 2, oy + w + w * 0.8 + 5, 'S3', k='pen', size=14, weight='700'),
           text(s2[0] + w / 2, oy - 10, 'outside edge', k='red', size=14),
           text(ox, oy + w + 72, 'S1’s bottom zips', k='red', size=14, anchor='start'),
           text(ox, oy + w + 90, 'onto S3’s left side', k='red', size=14, anchor='start')]
    tx = 380
    lab += [text(tx, 50, 'net 4:', k='pen', size=18, font='scrawl', anchor='start'),
            text(tx, 76, 'S1 leans on S3', k='ink', size=16, anchor='start'),
            text(tx, 100, 'S3 leans on S2', k='ink', size=16, anchor='start'),
            text(tx, 124, 'S2 leans on the outside', k='ink', size=16, anchor='start'),
            text(tx, 158, 'so S1 = top, S3 = left,', k='green', size=16, anchor='start'),
            text(tx, 180, 'S2 = right ✓', k='green', size=16, anchor='start')]
    return svg(660, 206, rough(*parts) + ''.join(lab),
               'Net 4 enlarged: S1’s triangle leans on S3 across the corner zip, S3’s leans on S2, S2’s leans on the outside edge')

Q.append(dict(
    n=22, orig=44, answer='D', topic='Cubes & nets',
    question=f"""<p>Here is a diagram of a cube.</p>
{fig(Y, 'ps_q22_cube', 'A cube with each face split into four triangles by its diagonals; one triangle is black on each visible face', 140)}
<p class="stem">Which one of the following nets {hl('<b>could</b>', 'b', 1)} be folded to make this cube?</p>
{fig(Y, 'ps_q22_nets', 'Five step-shaped nets of six squares, each square split by diagonals with some triangles black', 520)}""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'b', 'Only one net works. The three faces you see each have <b>one</b> black triangle; check where it sits.')],
    steps=[
        f"""<p>On the cube, each visible face has a single black triangle, and each triangle sits against one edge:</p>{_cube22()}""",
        f"""<p>In every net the single-triangle squares are the same three (shaded): S1 and S2 are the 2nd and 3rd squares of the top row, S3 is the square under S2. They meet at one corner when folded, because S1’s bottom edge zips onto S3’s left edge. Now see what each lone triangle leans on:</p>
{_nets22()}
{calc('net 1: S1 → S3, S2 → S3 (both on S3) ✗', 'net 2: S1 → S3, S2 → outside, S3 → outside ✗', 'net 3: S2 → S3 and S3 → S2 (on each other) ✗',
      'net 4: S1 → S3 → S2 → outside, a chain ✓', 'net 5: same single squares as net 2 ✗')}""",
        f"""{_net4()}
{note('Fold net 4 with S1 on top: S3 is on its left and S2 on its right, the same clockwise order as the picture, so it really matches.', 'check')}
{calc(f'answer: net {boxed("4")}')}""",
    ],
    answer_text='Net 4.',
    why={'A': 'Net 1: the lone triangles of S1 and S2 both lean on S3. On the cube they lean on two different faces.',
         'B': 'Net 2: S2’s and S3’s triangles both lean on outside edges. On the cube only one does.',
         'C': 'Net 3: S2’s and S3’s triangles lean on each other, across the same edge. On the cube no two triangles share an edge.',
         'E': 'Net 5 has the same three single-triangle squares as net 2 (only a hidden bow-tie differs), so it fails for the same reason.'},
    fast='Look only at the three squares with one black triangle. The cube needs a chain: top leans on left, left on right, right on the outside. Only net 4 does that.',
))

# ---------------------------------------------------------------- 23 (Q48)
def _journey():
    X = lambda m: 40 + (m - 375) * 1.55  # minutes after midnight
    parts, lab = [], []
    legs = [(375, 390, 'y', '15 km', '15 min'), (390, 690, 'b', 'motorway (incl. 2 stops)', '5 h'), (690, 720, 'g', '20 km', '30 min')]
    for a, b, f, name, t in legs:
        parts.append(rect(X(a), 60, X(b) - X(a), 40, k='ink', fill=f, sw=1.6))
        lab.append(text((X(a) + X(b)) / 2, 52, t, k='ink', size=16, weight='700'))
        lab.append(text((X(a) + X(b)) / 2, 30, name, k='ink', size=14))
    for (m, lbl), ly in zip(((375, '6:15'), (390, '6:30'), (690, '11:30'), (720, '12:00')), (132, 152, 132, 152)):
        parts.append(line(X(m), 100, X(m), 116 + (ly - 132), k='red', w=2))
        lab.append(text(X(m), ly + 4, lbl, k='red', size=16, weight='700' if m in (375, 720) else None))
    parts.append(arrow(X(718), 178, X(380), 178, k='pen', bend=0.08))
    lab.append(text(X(550), 206, 'work backwards from 12:00: 30 min, 5 h, 15 min', k='pen', size=16))
    return svg(660, 218, rough(*parts) + ''.join(lab),
               'Timeline from 6:15: 15 minutes to 6:30, 5 hours of motorway to 11:30, 30 minutes to arrive at 12:00')

Q.append(dict(
    n=23, orig=48, answer='D', topic='Speed, distance & time',
    question=f"""<p>A car journey begins with a {hl('15 km drive at an average speed of 60 km/hour', 'g', 1)}, then {hl('5 hours on the motorway, including two 15-minute rest stops', 'p', 2)}, travelling at an average driving speed of
{hl('80 km/hour', 'p', 3)}, and finally a {hl('20 km drive at an average speed of 40 km/hour', 'g', 4)} from the motorway to
the destination.</p>
<p class="stem">If the destination is reached at 12:00 midday, at what time did the journey {hl('begin', 'b', 5)}?</p>""",
    options={'A': '5:18 am', 'B': '5:25 am', 'C': '5:45 am', 'D': '6:15 am', 'E': '6:45 am'},
    notes=[(1, 'g', 'Time = distance ÷ speed = 15 ÷ 60 hour = 15 minutes.'),
           (2, 'p', 'The 5 hours already <b>includes</b> the stops. Don’t add them again.'),
           (3, 'p', 'Red herring: you already know the motorway time, so the speed isn’t needed.'),
           (4, 'g', '20 ÷ 40 = ½ hour = 30 minutes.'),
           (5, 'b', 'Work backwards from 12:00.')],
    steps=[
        f"""{calc('first leg: 15 km at 60 km/h → 1 km a minute → 15 min', 'motorway: 5 h (stops already inside it)', 'last leg: 20 km at 40 km/h → ½ hour → 30 min',
                  'total = 5 h 45 min')}""",
        f"""{_journey()}
{calc(f'12:00 − 5 h 45 min = {boxed("6:15 am")}')}""",
    ],
    answer_text='6:15 am: the whole trip takes 5 hours 45 minutes.',
    why={'A': '5:18 am would mean a 6 h 42 min trip, 57 minutes too long; no sensible slip gives this.',
         'B': '5:25 am comes from averaging the three speeds to 60 km/h and dividing the total distance (395 km) by it. You can’t average speeds like that.',
         'C': '5:45 am adds the two 15-minute stops on top of the 5 hours, but they are already included.',
         'E': '6:45 am leaves out the final 30-minute drive.'},
    fast='15 min + 5 h + 30 min = 5 h 45 min. 12:00 − 5:45 = 6:15.',
))

# ---------------------------------------------------------------- 24 (Q49)
def _boards():
    X = lambda m: 140 + m * 110
    parts, lab = [], []
    rows = [('4.00 m, $9.30', [(1.8, 'g', '1.8'), (1.8, 'g', '1.8'), (0.4, 'paper', '')]),
            ('4.00 m, $9.30', [(1.8, 'g', '1.8'), (1.8, 'g', '1.8'), (0.4, 'paper', '')]),
            ('2.00 m, $4.95', [(1.8, 'g', '1.8'), (0.2, 'paper', '')])]
    for i, (name, segs) in enumerate(rows):
        y = 40 + i * 50
        x0 = 0
        for m, f, l in segs:
            parts.append(rect(X(x0), y, X(x0 + m) - X(x0), 30, k='ink', fill=f, sw=1.5))
            if l:
                lab.append(text((X(x0) + X(x0 + m)) / 2, y + 21, f'shelf {l} m', k='ink', size=14))
            x0 += m
        lab.append(text(130, y + 21, name, k='ink', size=15, anchor='end'))
        lab.append(text(X(x0) + 10, y + 21, 'waste', k='muted', size=13, anchor='start'))
    lab += [text(330, 24, 'all 45 cm deep (30 cm is too shallow, 60 cm costs more)', k='pen', size=15),
            text(330, 210, '9.30 + 9.30 + 4.95 = $23.55 for 5 shelves', k='red', size=19, font='scrawl')]
    return svg(660, 222, rough(*parts) + ''.join(lab),
               'Two 4-metre boards each give two 1.8 m shelves and one 2-metre board gives the fifth: 23.55 dollars')

Q.append(dict(
    n=24, orig=49, answer='C', topic='Best deal',
    question=f"""<p>Fiona is going to put some shelves up in her living room. The shelves must each be {hl('1.80 m long', 'g', 1)} and have a {hl('depth of at least 40 cm', 'y', 2)}. There will be {hl('five shelves', 'g', 3)} in total. The different prices
for wood are shown in the table below.</p>
{table([['0.50 m', '$0.90', '$1.35', '$1.50'], ['1.00 m', '$1.70', '$2.55', '$2.80'], ['1.50 m', '$2.50', '$3.75', '$4.20'],
        ['2.00 m', '$3.30', hl('$4.95', 'g'), '$5.50'], ['3.00 m', '$4.80', '$7.20', '$8.00'], ['4.00 m', '$6.20', hl('$9.30', 'g'), '$10.00']],
       head=['<i>length</i>', '<i>depth</i> 30 cm', '45 cm', '60 cm'])}
<p>Fiona can cut pieces of wood to make more than one piece of the correct size, but she wants
{hl('each of the shelves to be made of one complete piece of wood', 'p', 4)}.</p>
<p class="stem">What is the {hl('cheapest total cost', 'b', 5)} for which Fiona can make her shelves?</p>""",
    options={'A': '$21.15', 'B': '$23.25', 'C': '$23.55', 'D': '$24.75', 'E': '$25.50'},
    notes=[(1, 'g', 'Each shelf needs a board at least 1.8 m long: 2 m, 3 m or 4 m (4 m gives two shelves).'),
           (2, 'y', '30 cm is too shallow. 45 cm is enough and cheaper than 60 cm.'),
           (3, 'g', 'Five shelves: an odd number, so one board will give only one shelf.'),
           (4, 'p', 'No joining offcuts together to make a shelf.'),
           (5, 'b', 'Cheapest mix of boards.')],
    steps=[
        f"""<p>Use the 45 cm column. Cost per shelf:</p>
{calc('2.00 m board: 1 shelf for $4.95', '3.00 m board: still only 1 shelf, $7.20 ✗', '4.00 m board: 2 shelves (3.6 m) for $9.30 → $4.65 each ← best')}""",
        f"""<p>Four shelves from two 4 m boards; the fifth needs its own board, and the cheapest that is long enough is 2 m:</p>{_boards()}
{calc(f'9.30 × 2 + 4.95 = 18.60 + 4.95 = {boxed("$23.55")}')}""",
    ],
    answer_text='$23.55: two 4.00 m boards and one 2.00 m board, all 45 cm deep.',
    why={'A': '$21.15 = 18.60 + 2.55: it makes the fifth shelf from a 1 m board plus the two 0.4 m offcuts, but each shelf must be one complete piece.',
         'B': '$23.25 = 5 × $4.65: it pays for half a 4 m board for the fifth shelf. You can’t buy half a board.',
         'D': '$24.75 = 5 × $4.95: five separate 2 m boards, missing the 4 m saving.',
         'E': '$25.50 uses the 60 cm wood (10.00 + 10.00 + 5.50). 45 cm is deep enough and cheaper.'},
    fast='45 cm wood. 4 m board = 2 shelves for 9.30. Two of those + one 2 m board = 9.30 + 9.30 + 4.95 = 23.55.',
))

# ---------------------------------------------------------------- 25 (Q50)
def _bump(ox, oy, perm, title, sub, bad=(), right_lab=None, h=150, w=110):
    parts, lab = [], []
    ys = [oy + i * h / 5 for i in range(6)]
    parts += [line(ox, oy - 10, ox, oy + h + 10, k='ink', w=2), line(ox + w, oy - 10, ox + w, oy + h + 10, k='ink', w=2)]
    for i in range(6):
        j = perm[i] - 1
        parts.append(line(ox, ys[i], ox + w, ys[j], k='red' if (i + 1) in bad else 'pen', w=2.4 if (i + 1) in bad else 1.8))
        lab.append(text(ox - 8, ys[i] + 5, i + 1, k='muted', size=13, anchor='end'))
        lab.append(text(ox + w + 8, ys[i] + 5, (right_lab or list(range(1, 7)))[i], k='muted', size=13, anchor='start'))
    lab.append(text(ox + w / 2, oy - 24, title, k='ink', size=16, weight='700'))
    lab.append(text(ox + w / 2, oy + h + 34, sub, k='ink', size=14))
    return parts, lab


def _bumps():
    p1, l1 = _bump(50, 50, [1, 3, 2, 6, 5, 4], 'C as printed', 'L1–R1, L2–R3, L4–R6 …')
    p2, l2 = _bump(270, 50, [6, 4, 5, 1, 2, 3], 'right axis flipped', 'L1–R6, L2–R4, L3–R5 …', bad=(1,))
    p3, l3 = _bump(490, 50, [4, 5, 6, 2, 3, 1], 'its mirror image', 'every line moved ✗', bad=(6,))
    lab = [text(225, 130, '→', k='ink', size=28), text(445, 130, '→', k='ink', size=28),
           text(330, 262, 'the mirror turns L1–R6 into L6–R1, but the flipped chart has L6–R3 ✗', k='red', size=17, font='scrawl')]
    return svg(660, 276, rough(*p1, *p2, *p3) + ''.join(l1 + l2 + l3 + lab),
               'Chart C, then C with the right axis flipped, then its mirror image: they differ, so C is not symmetrical')

Q.append(dict(
    n=25, orig=50, answer='C', topic='Patterns & symmetry',
    question=f"""<p>Keith likes to draw ‘bump charts’ to look at relationships. For instance, if 6 individuals were
ordered by height, and it happened that the order was the same by weight, the bump chart
would look like this:</p>
{fig(Y, 'ps_q25_chart1', 'Bump chart with six horizontal lines joining heights 172 to 159 cm on the left to weights 100 to 52 kg on the right', 240)}
<p>Or if height was maintained for order on the left hand but {hl('lightness rather than heaviness on the right hand', 'y', 1)}, the bump chart would be this:</p>
{fig(Y, 'ps_q25_chart2', 'The same data with the weight axis reversed: all six lines cross at one point in the middle', 240)}
<p class="stem">If {hl('one axis is reversed in order', 'p', 2)} (as in heaviness goes to lightness), which one of the following
bump charts {hl('would <b>not</b> be symmetrical about a vertical line midway between the axes', 'b', 3)}?</p>
{fig(Y, 'ps_q25_opts', 'Five bump charts A to E, each with six lines between two vertical axes', 470)}""",
    options={'A': 'chart A', 'B': 'chart B', 'C': 'chart C', 'D': 'chart D', 'E': 'chart E'},
    notes=[(1, 'y', 'Reversing an axis flips its order upside down: position 1 becomes 6, 2 becomes 5, 3 becomes 4.'),
           (2, 'p', 'Do the flip <b>first</b>, then test the symmetry. (Flipping either axis gives the same answer.)'),
           (3, 'b', 'Mirror symmetry: every line from left a to right b needs a twin from left b to right a (a flat line a to a is its own twin).')],
    steps=[
        f"""<p>Number the positions 1 (top) to 6 on both axes and write each chart as “left → right”. Flipping the right axis turns every right-hand number r into 7 − r:</p>
{calc('A: 1→2, 2→3, 3→4, 4→5, 5→6, 6→1  flip → 1→5, 2→4, 3→3, 4→2, 5→1, 6→6 ✓ pairs',
      'B: 1→6, 2→3, 3→4, 4→5, 5→1, 6→2  flip → 1→1, 2→4, 3→3, 4→2, 5→6, 6→5 ✓',
      'C: 1→1, 2→3, 3→2, 4→6, 5→5, 6→4  flip → 1→6, 2→4, 3→5, 4→1, 5→2, 6→3 ✗',
      'D: 1→1, 2→2, 3→4, 4→3, 5→5, 6→6  flip → 1→6, 2→5, 3→3, 4→4, 5→2, 6→1 ✓',
      'E: 1→6, 2→2, 3→1, 4→3, 5→5, 6→4  flip → 1→1, 2→5, 3→6, 4→4, 5→2, 6→3 ✓')}""",
        f"""<p>In C, 1→6 needs 6→1, but 6→3. Picture it:</p>{_bumps()}
{calc(f'not symmetrical: {boxed("C")}')}
{note('Shortcut: flipping one axis and then mirroring is the same as turning the original chart upside down (half a turn). C turned upside down puts its top flat line at the bottom, but C has no flat line at the bottom (its other flat line is 5th). A, B, D and E all look the same upside down.', 'tip')}""",
    ],
    answer_text='Chart C: after flipping an axis its lines don’t pair up (1→6 but 6→3).',
    why={'A': 'A flips to 1↔5, 2↔4 with 3 and 6 flat: symmetrical. (Turned upside down, A looks the same.)',
         'B': 'B flips to 2↔4, 5↔6 with 1 and 3 flat: symmetrical.',
         'D': 'D flips to 1↔6, 2↔5 with 3 and 4 flat: symmetrical.',
         'E': 'E flips to 2↔5, 3↔6 with 1 and 4 flat: symmetrical.'},
    fast='Turn each chart upside down: if it looks the same, it passes. C’s flat lines are 1st and 5th, so upside down they become 6th and 2nd. C fails.',
))
