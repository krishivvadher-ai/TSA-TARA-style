import math
from wslib import *

Y = 2016
Q = []


# ---------------------------------------------------------------- 18 (Q37)
def _mushrooms():
    g = 24
    x0, y0 = 40, 40
    parts, lab = [], []
    for i in range(6):
        for j in range(6):
            ring = max(abs(i - 2.5), abs(j - 2.5))
            k, f = ('orange', 'o') if ring < 1 else ('green', 'g') if ring < 2 else ('pen', 'b')
            parts.append(circle(x0 + i * g + g / 2, y0 + j * g + g / 2, 6, k=k, fill=f, sw=1.8))
    for n, k in ((2, 'orange'), (4, 'green'), (6, 'pen')):
        off = (6 - n) / 2 * g
        parts.append(rect(x0 + off, y0 + off, n * g, n * g, k=k, sw=1.6))
    lab += [text(x0 + 3 * g, y0 + 6 * g + 28, 'Mon 2, Tue 4, Wed 6', k='ink', size=17),
            text(x0 + 3 * g, y0 + 6 * g + 50, 'per side', k='muted', size=15),
            text(x0 + 3 * g, y0 - 12, 'each owns a 1 m square', k='muted', size=14)]
    pos = {1: 270, 2: 340, 3: 410, 48: 610}
    parts.append(line(250, 120, 630, 120, k='ink', w=2, head=True))
    for d, x in pos.items():
        parts.append(line(x, 112, x, 128, k='ink', w=1.8))
    lab += [text(270, 104, '6', k='pen', size=19), text(340, 104, '8', k='pen', size=19),
            text(410, 104, '10', k='pen', size=19), text(510, 104, '… +2 a day …', k='muted', size=16),
            text(610, 104, '100', k='green', size=20, weight='bold'),
            text(270, 150, 'today', k='ink', size=15), text(270, 168, 'day 1', k='muted', size=14),
            text(340, 150, 'day 2', k='muted', size=14), text(410, 150, 'day 3', k='muted', size=14),
            text(610, 150, 'day 48', k='green', size=17), text(610, 170, 'field full!', k='green', size=15),
            text(440, 70, 'mushrooms along one side (not to scale)', k='ink', size=16),
            text(440, 214, '100 − 6 = 94 more, 94 ÷ 2 = 47 more days', k='red', size=19, font='scrawl'),
            text(440, 242, '47 + today = 48 days', k='red', size=21, font='scrawl')]
    return svg(660, 262, rough(*parts) + ''.join(lab),
               'Six by six grid of mushrooms showing the 2, 4 and 6 squares, and a number line of mushrooms per side from 6 today to 100 on day 48')


Q.append(dict(
    n=18, orig=37, answer='A', topic='Sequences',
    question=f"""<p>I have a square field which is exactly one hectare {hl('(100 m × 100 m)', 'g', 1)}. On Monday I was surprised
to find {hl('4 mushrooms growing in a 1 m square formation', 'g', 2)}, in the centre of my field. On Tuesday
the group of mushrooms had {hl('expanded to 16, which were all 1 m apart', 'g', 3)}.</p>
{fig(Y, 'ps_q18_tue', 'Tuesday: a 4 by 4 square of mushroom dots, 1 m apart, around the centre', 190)}
<p>When I looked at the group of mushrooms {hl('today (Wednesday), it had expanded to 36', 'g', 4)}.</p>
{fig(Y, 'ps_q18_wed', 'Wednesday: a 6 by 6 square of mushroom dots, 1 m apart, around the centre', 250)}
<p class="stem">If the area covered by mushrooms {hl('continues to expand at this rate', 'y', 5)}, how many days {hl('(including today)', 'p', 6)} will it be until my field is covered in mushrooms?</p>""",
    options={'A': '48', 'B': '50', 'C': '96', 'D': '100', 'E': '192'},
    notes=[(1, 'g', '100 mushrooms 1 m apart, each in the middle of its own 1 m square, fill a 100 m side.'),
           (2, 'g', 'Monday: 2 by 2.'),
           (3, 'g', 'Tuesday: 4 by 4.'),
           (4, 'g', 'Wednesday: 6 by 6. One more mushroom at <b>each end</b> of every row each day: +2 per side.'),
           (5, 'y', 'Same growth every day: +2 per side.'),
           (6, 'p', 'Count today (Wednesday) as day 1.')],
    steps=[
        f"""<p>Count mushrooms along one side: 4 = 2 × 2, 16 = 4 × 4, 36 = 6 × 6.</p>
{calc('Mon 2, Tue 4, Wed 6 per side', f'+2 a day {ar()} one new mushroom at each end of every row')}""",
        f"""<p>Each mushroom sits in the middle of its own 1 m × 1 m square (36 mushrooms cover 6 m × 6 m = 36 m²).
So the 100 m × 100 m field is full when there are <b>100 per side</b>.</p>{_mushrooms()}""",
        f"""<p>Count the days, with today as day 1:</p>
{calc('today: 6 per side', 'still needed: 100 − 6 = 94 more per side', '94 ÷ 2 = 47 more days',
      f'47 + 1 (today) = {boxed("48 days")}')}
{note('Check: 2 × 48 + 4 = 100. The number per side on day n (from today) is 2n + 4.', 'check')}""",
    ],
    answer_text='48 days: 6 per side today, +2 a day, 100 per side on day 48.',
    why={'B': '50 counts from Monday (2 per side on day 1, 100 on day 50). The question counts from today, Wednesday.',
         'C': '96 treats the square as growing 1 m a day (from 5 m across today to 100 m is 95 more days, 96 with today). It grows at both ends, so 2 m a day.',
         'D': '100 is just the length of the field’s side, as if one mushroom were added per side each day from nothing.',
         'E': '192 is 4 × 48: it counts growth on each of the four sides separately, but one day’s growth adds to every side at once.'},
    fast='Per side: 2, 4, 6… (+2 a day). From 6 to 100 is 94, so 47 more days. Including today: 48.',
))


# ---------------------------------------------------------------- 19 (Q38)
def _bowling():
    rows = [('Pip', 28, 54), ('Eve', 27, 56), ('Bob', 24, 63), ('Viv', 22, 68), ('Nan', 21, 72)]
    X = lambda v: 260 + (v - 1400) * 2.6
    parts, lab = [], []
    lab.append(text(X(1400), 20, 'money raised (axis starts at £1,400)', k='muted', size=15, anchor='start'))
    for i, (name, h, r) in enumerate(rows):
        y = 34 + i * 40
        amt = h * r
        odd = name == 'Viv'
        parts.append(rect(X(1400), y, X(amt) - X(1400), 26, k='red' if odd else 'ink', fill='p' if odd else 'g', sw=1.8))
        lab.append(text(250, y + 19, f'{name}: {h} × £{r}', k='red' if odd else 'ink', size=17, anchor='end'))
        lab.append(text(X(1512) + 8, y + 19, f'£{amt:,}', k='red' if odd else 'green', size=17, anchor='start', weight='bold'))
    parts.append(line(X(1512), 28, X(1512), 236, k='green', w=1.8, dash=True))
    lab.append(text(X(1512) - 4, 254, 'four of them: £1,512', k='green', size=18, font='scrawl', anchor='end'))
    return svg(660, 266, rough(*parts) + ''.join(lab),
               'Money raised: Pip, Eve, Bob and Nan each 1,512 pounds; Viv 1,496 pounds')


Q.append(dict(
    n=19, orig=38, answer='E', topic='Multiplication',
    question=f"""<p>Bob, Eve, Nan, Pip and Viv took part in a 6-hour sponsored bowling marathon to raise money
for charity. They were all sponsored {hl('per complete 100 points scored', 'p', 1)}.</p>
<p>Bob was sponsored for a total of £63 per 100 points.<br>Eve was sponsored for a total of £56 per 100 points.<br>
Nan was sponsored for a total of £72 per 100 points.<br>Pip was sponsored for a total of £54 per 100 points.<br>
Viv was sponsored for a total of £68 per 100 points.</p>
<p>During the 6-hour marathon:</p>
<p>Pip scored 2,835 points.<br>Eve scored 2,782 points.<br>Bob scored 2,407 points.<br>Viv scored 2,293 points.<br>Nan scored 2,169 points.</p>
<p class="stem">Remarkably, {hl('four of them raised exactly the same amount', 'y', 2)}. {hl('Who raised a different amount', 'b', 3)} to
the other four?</p>""",
    options={'A': 'Bob', 'B': 'Eve', 'C': 'Nan', 'D': 'Pip', 'E': 'Viv'},
    notes=[(1, 'p', 'Only <b>complete</b> hundreds count: 2,835 points = 28 hundreds (the 35 earns nothing).'),
           (2, 'y', 'Four totals match. Find the common amount, then the odd one out.'),
           (3, 'b', 'The one whose total is different.')],
    steps=[
        f"""<p>Complete hundreds: just drop the last two digits.</p>
{calc('Pip 2,835 → 28', 'Eve 2,782 → 27', 'Bob 2,407 → 24', 'Viv 2,293 → 22', 'Nan 2,169 → 21')}""",
        f"""<p>Multiply by each person’s rate:</p>
{calc('Pip: 28 × 54 = 1,400 + 112 = £1,512', 'Eve: 27 × 56 = 1,512', 'Bob: 24 × 63 = 1,512',
      'Nan: 21 × 72 = 1,512', 'Viv: 22 × 68 = <b>1,496</b> ' + cross())}
{_bowling()}
{calc(f'odd one out = {boxed("Viv")}')}
{note('28 × 54: do 28 × 50 = 1,400 and 28 × 4 = 112. Once you know the target is 1,512 you only need to check the others against it.', 'tip')}""",
    ],
    answer_text='Viv: 22 × £68 = £1,496; the other four all raised £1,512.',
    why={'A': 'Bob: 24 complete hundreds × £63 = £1,512, the same as three others.',
         'B': 'Eve: 27 × £56 = £1,512.',
         'C': 'Nan: 21 × £72 = £1,512.',
         'D': 'Pip: 28 × £54 = £1,512. (If you use all 2,835 points instead of complete hundreds, every total comes out different.)'},
    fast='Drop the last two digits: 28, 27, 24, 22, 21. Times the rates: four make £1,512, Viv makes 22 × 68 = £1,496.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _sacks():
    sacks = [('Sat morning', '25p a kilo', 12, 'o', 'orange'), ('weekday', '20p a kilo', 15, 'b', 'pen'),
             ('Sat afternoon', '15p a kilo', 20, 'g', 'green')]
    parts, lab = [], []
    x = 40
    for name, price, kg, f, k in sacks:
        w = 60 + kg * 5
        h = 40 + kg * 6
        top = 230 - h
        parts.append(path(f'M{x} {230} L{x} {top + 20} Q{x} {top} {x + w / 2} {top} Q{x + w} {top} {x + w} {top + 20} L{x + w} 230 Z',
                          k=k, fill=f, sw=2.2))
        lab += [text(x + w / 2, top + h / 2 + 10, f'{kg} kg', k='ink', size=22, weight='bold'),
                text(x + w / 2, 256, name, k=k, size=17), text(x + w / 2, 278, price, k='muted', size=15)]
        x += w + 70
    parts += [arrow(206, 108, 140, 128, k='red', bend=-0.3, w=2), arrow(290, 96, 404, 70, k='red', bend=-0.3, w=2)]
    lab += [text(184, 98, '3 kg less', k='red', size=17), text(352, 62, '5 kg more', k='red', size=17),
            text(330, 312, 'all for £3 = 300p:  300 ÷ 25 = 12,  300 ÷ 20 = 15,  300 ÷ 15 = 20', k='ink', size=17)]
    return svg(660, 326, rough(*parts) + ''.join(lab),
               'Three sacks bought for 3 pounds: 12 kg at 25p, 15 kg at 20p, 20 kg at 15p; 3 kg less in the morning and 5 kg more in the afternoon')


Q.append(dict(
    n=20, orig=42, answer='C', topic='Trial & improvement',
    question=f"""<p>Anna buys potatoes in the local market. She has noticed that the price on Saturday morning is
{hl('5p per kilo more than the normal weekday price', 'g', 1)}. However, an hour before the stall closes on a
Saturday afternoon, the price drops to {hl('5p per kilo below the weekday price', 'g', 2)}. {hl('She spends £3.00 a week on potatoes', 'g', 3)}. This will buy her {hl('3 kilos less', 'y', 4)} in weight on a Saturday morning than on a
weekday, but {hl('5 kilos more', 'y', 5)} in weight at the low Saturday afternoon price than on a weekday.</p>
<p class="stem">What is the {hl('weekday price', 'b', 6)} of potatoes per kilo?</p>""",
    options={'A': '12p', 'B': '15p', 'C': '20p', 'D': '25p', 'E': '30p'},
    notes=[(1, 'g', 'Saturday morning price = weekday + 5p.'),
           (2, 'g', 'Saturday afternoon price = weekday − 5p.'),
           (3, 'g', 'Always 300p. Kilos bought = 300 ÷ price per kilo.'),
           (4, 'y', 'Morning: 3 kg fewer than on a weekday.'),
           (5, 'y', 'Afternoon: 5 kg more than on a weekday.'),
           (6, 'b', 'Find the weekday price.')],
    steps=[
        f"""<p>Kilos for £3 = 300p ÷ price. Test the options; both differences must work:</p>
{calc('12p: 25 kg; at 17p 17.6 kg ' + cross(),
      '15p: 20 kg; at 20p 15 kg (5 less, not 3) ' + cross(),
      f'20p: 15 kg; at 25p 12 kg (3 less {tick()}); at 15p 20 kg (5 more {tick()})',
      '25p: 12 kg; at 30p 10 kg (2 less, not 3) ' + cross(),
      '30p: 10 kg; at 25p 12 kg (2 more, not 5) ' + cross())}""",
        f"""<p>Picture the three buys for 20p:</p>{_sacks()}
{calc(f'weekday price = {boxed("20p")}')}
{note('Pick prices that divide 300 nicely first. 20p, 25p and 15p all do, which is a strong hint.', 'tip')}""",
    ],
    answer_text='20p a kilo: 15 kg on a weekday, 12 kg at 25p, 20 kg at 15p.',
    why={'A': '12p gives 25 kg on a weekday but only about 17.6 kg at 17p: over 7 kg less, not 3.',
         'B': '15p gives 20 kg, but at 20p she gets 15 kg (5 less, not 3) and at 10p 30 kg (10 more, not 5).',
         'D': '25p gives 12 kg, then 10 kg at 30p (2 less) and 15 kg at 20p (3 more). Both differences are wrong.',
         'E': '30p gives 10 kg, then 12 kg at 25p: only 2 more, not 5.'},
    fast='Try 20p: 300 ÷ 25 = 12, 300 ÷ 20 = 15, 300 ÷ 15 = 20. That is 3 less and 5 more.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _depreciation():
    rows = [('Rover 820', 8.57, '6,000 ÷ 70,000'), ('Renault Laguna', 7.5, '6,000 ÷ 80,000'),
            ('Rover 825', 5.0, '500 ÷ 10,000'), ('Ford Sierra', 3.33, '1,000 ÷ 30,000')]
    X = lambda v: 170 + v * 36
    parts, lab = [], []
    lab.append(text(X(0), 20, 'value lost per mile (pence)', k='muted', size=15, anchor='start'))
    for i, (name, p, sum_) in enumerate(rows):
        y = 32 + i * 46
        best = name == 'Ford Sierra'
        parts.append(rect(X(0), y, X(p) - X(0), 30, k='ink', fill='g' if best else 'b', sw=1.6))
        lab.append(text(160, y + 21, name, k='green' if best else 'ink', size=17, anchor='end', weight='bold' if best else None))
        lab.append(text(X(p) + 8, y + 21, f'{sum_} = {p:.1f}p'.replace('.0p', 'p'), k='ink', size=16, anchor='start'))
    lab.append(text(X(3.33) + 230, 32 + 3 * 46 + 21, '← lowest', k='green', size=19, anchor='start', font='scrawl'))
    return svg(660, 222, rough(*parts) + ''.join(lab),
               'Value lost per mile: Rover 820 8.6p, Renault Laguna 7.5p, Rover 825 5p, Ford Sierra 3.3p, the lowest')


Q.append(dict(
    n=21, orig=43, answer='A', topic='Tables & rates',
    question=f"""<p>Mike wants to buy a second-hand car that offers the {hl('lowest depreciation per mile', 'b', 1)}. He is not
worried about the model. His family insist that the car has {hl('4 or 5 doors', 'y', 2)} and an engine of {hl('at least 1.6 litres', 'y', 3)} so that it can tow a caravan. Mike plans to keep the car {hl('until it has covered 100 000 miles and then sell it for £1,000', 'g', 4)}. He scans the following price list from his local garage:</p>
{table([['Ford', 'Escort 3 door', '1.6 litre', '70 000', '£2,500'], ['Rover', '214 SLi 3 door', '1.4 litre', '30 000', '£4,500'],
        ['Rover', '414 Si 4 door', '1.4 litre', '40 000', '£4,500'], ['VW', 'Golf CL 3 door', '1.6 litre', '95 000', '£1,200'],
        ['Rover', hl('820 4 door', 'g'), hl('1.6 litre', 'g'), '30 000', '£7,000'], ['Vauxhall', 'Vectra 3 door', '1.8 litre', '10 000', '£8,000'],
        ['Vauxhall', 'Astra 3 door', '1.4 litre', '50 000', '£3,500'], ['Ford', 'Escort 5 door', '1.4 litre', '40 000', '£4,000'],
        ['Renault', 'Clio 3 door', '1.6 litre', '80 000', '£2,000'], ['Renault', hl('Laguna 5 door', 'g'), hl('1.8 litre', 'g'), '20 000', '£7,000'],
        ['Rover', hl('825 4 door', 'g'), hl('2.5 litre', 'g'), '90 000', '£1,500'], ['Ford', hl('Sierra 4 door', 'g'), hl('2.0 litre', 'g'), '70 000', '£2,000']],
       head=['Make', 'Model', 'Engine', 'Mileage', 'Price'])}
<p class="stem">Which {hl('make', 'b', 5)} of car does Mike buy?</p>""",
    options={'A': 'Ford', 'B': 'Rover', 'C': 'VW', 'D': 'Vauxhall', 'E': 'Renault'},
    notes=[(1, 'b', 'Value lost ÷ miles he will drive. Lowest wins.'),
           (2, 'y', 'Every 3-door car is out.'),
           (3, 'y', '1.4 litre engines are out. 1.6 is fine (“at least”).'),
           (4, 'g', 'Value lost = price − £1,000. Miles he drives = 100,000 − mileage now.'),
           (5, 'b', 'The maker (Ford, Rover…), not the model.')],
    steps=[
        f"""<p>Filter first. 4 or 5 doors <b>and</b> 1.6 litres or more leaves only four cars (green in the table):</p>
{calc('Rover 820, Renault Laguna, Rover 825, Ford Sierra')}
{note('The Rover 414 and the Ford Escort 5 door have enough doors but only 1.4 litre engines.', 'trap')}""",
        f"""<p>Depreciation per mile = (price − £1,000) ÷ (100,000 − mileage):</p>
{calc('Rover 820: 6,000 ÷ 70,000 ≈ 8.6p', 'Laguna: 6,000 ÷ 80,000 = 7.5p', 'Rover 825: 500 ÷ 10,000 = 5p',
      'Ford Sierra: 1,000 ÷ 30,000 ≈ 3.3p')}
{_depreciation()}
{calc(f'lowest is the Sierra {ar()} make = {boxed("Ford")}')}""",
    ],
    answer_text='Ford (the Sierra): it loses £1,000 over 30,000 miles, about 3.3p a mile.',
    why={'B': 'The best Rover, the 825, loses £500 over 10,000 miles = 5p a mile. The Sierra is cheaper per mile.',
         'C': 'The VW Golf is a 3-door, which the family won’t accept. (It would be 4p a mile.)',
         'D': 'Both Vauxhalls are 3-door cars.',
         'E': 'The Laguna loses 7.5p a mile, and the Clio is a 3-door.'},
    fast='Keep 4/5-door cars of 1.6 l or more: Rover 820, Laguna, Rover 825, Sierra. Loss ÷ miles left: Sierra 1,000 ÷ 30,000 ≈ 3.3p is lowest. Ford.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _old_groups():
    X = lambda n: 150 + n / 1000 * 0.33
    parts, lab = [], []
    for i, (name, m, f) in enumerate((('80–84', 545800, 786900), ('85+', 417900, 856400))):
        y = 44 + i * 74
        parts += [rect(X(0), y, X(m) - X(0), 36, k='ink', fill='b', sw=1.6),
                  rect(X(m), y, X(m + f) - X(m), 36, k='ink', fill='p', sw=1.6)]
        lab += [text(140, y + 25, name, k='ink', size=19, anchor='end'),
                text((X(0) + X(m)) / 2, y + 24, f'men {m:,}', k='ink', size=14),
                text((X(m) + X(m + f)) / 2, y + 24, f'women {f:,}', k='ink', size=14),
                text(X(m + f) + 8, y + 25, f'{m + f:,}', k='red' if name == '85+' else 'ink', size=18, anchor='start', weight='bold')]
    lab += [text(330, 30, 'the two smallest groups, men + women', k='muted', size=15),
            text(330, 196, '85+ is smaller than 80–84, so D is false', k='red', size=20, font='scrawl')]
    return svg(660, 210, rough(*parts) + ''.join(lab),
               'Stacked bars: 80 to 84 has 1,332,700 people; 85 plus has 1,274,300, which is fewer')


Q.append(dict(
    n=22, orig=44, answer='D', topic='Reading charts',
    question=f"""<p>The population pyramid below shows the {hl('age and gender distribution', 'y', 2)} of the residents in
England and Wales in 2010.</p>
{fig(Y, 'ps_q22_pyramid', 'Population pyramid for England and Wales 2010: number of males on the left and females on the right for each 5-year age group from under 1 to 85 plus', 470)}
<p class="stem">Which one of the following statements is {hl('not true', 'b', 1)}?</p>""",
    options={'A': 'Over the age of 34, the number of women is higher than that of men for every age group.',
             'B': 'Below the age of 35, the number of men is higher than that of women in every age group.',
             'C': 'There are more than twice as many women as men in the 85+ age group.',
             'D': 'Not taking children below the age of 1 into consideration, the least numerous age group is that of people aged 80 to 84.',
             'E': 'The most numerous age group consists of people aged between 40 and 44.'},
    notes=[(1, 'b', 'Four statements are true. Check each one against the numbers and find the false one.'),
           (2, 'y', 'Each bar is labelled with its exact number: men on the left, women on the right. An age group = men + women.')],
    steps=[
        f"""<p>D talks about the <b>least numerous</b> group, so look at the shortest bars, at the top. Add men and women:</p>
{calc('80–84: 545,800 + 786,900 = 1,332,700', '85+: 417,900 + 856,400 = 1,274,300')}
{_old_groups()}
{calc(f'85+ is the smallest group (after under-1s), not 80–84 {ar()} D is false')}""",
        f"""<p>Quick checks that the others are true:</p>
{calc(f'A: 35–39 upwards, every female number is bigger (e.g. 1,882,100 &gt; 1,862,900) {tick()}',
      f'B: under 35, every male number is bigger (e.g. 1,745,000 &gt; 1,718,100) {tick()}',
      f'C: 2 × 417,900 = 835,800, and 856,400 is more {tick()}',
      f'E: 40–44 = 2,043,200 + 2,069,800 = 4,113,000, the biggest (45–49 is 4,036,200) {tick()}')}
{calc(f'not true = {boxed("D")}')}""",
    ],
    answer_text='D is false: the 85+ group (1,274,300) is smaller than the 80–84 group (1,332,700).',
    why={'A': 'True: from 35–39 upwards each female number is larger than the male one.',
         'B': 'True: in every group under 35 the male number is larger (e.g. 20–24: 1,963,300 against 1,855,700).',
         'C': 'True: 856,400 women against 417,900 men, and 2 × 417,900 = 835,800.',
         'E': 'True: 40–44 totals 4,113,000, more than any other group.'},
    fast='Add the top two groups: 80–84 ≈ 1.33 million, 85+ ≈ 1.27 million. 85+ is smaller, so D is false.',
))


# ---------------------------------------------------------------- 23 (Q48)
def _orbits():
    parts, lab = [], []

    def panel(cx, cy, laps, title, good):
        pr, lr = [], []
        for r in (38, 62, 86):
            pr.append(circle(cx, cy, r, k='muted', sw=1.4))
        pr.append(circle(cx, cy, 9, k='ink', fill='paper', sw=2))
        a0 = 40
        pr.append(line(cx, cy, cx + 100 * math.cos(math.radians(a0)), cy - 100 * math.sin(math.radians(a0)), k='muted', w=1.4, dash=True))
        for (r, name, lap, k) in zip((38, 62, 86), ('O', 'H', 'R'), laps, ('pen', 'orange', 'violet')):
            a = math.radians(a0 + 360 * (lap % 1))
            x, y = cx + r * math.cos(a), cy - r * math.sin(a)
            pr.append(circle(x, y, 8, k=k, fill='paper', sw=2.4))
            lr.append(text(x, y + 5, name, k=k, size=13, weight='bold'))
        lr += [text(cx, cy + 118, title, k='green' if good else 'red', size=19, font='scrawl')]
        return pr, lr

    p1, l1 = panel(160, 112, (3.6, 1.6, 0.6), 'after 72 days ✓', True)
    p2, l2 = panel(480, 112, (9, 4, 1.5), 'after 180 days ✗', False)
    lab += [text(160, 254, '3.6, 1.6, 0.6 laps: all 0.6 round', k='ink', size=15),
            text(480, 254, '9, 4, 1.5 laps: Romeo on the far side', k='ink', size=15),
            text(330, 22, 'dashed line = where they started', k='muted', size=14)]
    return svg(660, 268, rough(*p1, *p2) + ''.join(l1 + l2 + lab),
               'Two orbit sketches: after 72 days Othello, Hamlet and Romeo are lined up on the same side; after 180 days Romeo is on the opposite side')


def _lineups():
    X = lambda d: 250 + d * 1.75
    parts, lab = [], []
    for y, step, l1, l2, k in ((60, 36, 'Othello catches Hamlet', 'every 36 days', 'pen'),
                               (140, 72, 'Hamlet catches Romeo', 'every 72 days', 'orange')):
        parts.append(line(X(0), y, X(222), y, k='ink', w=2))
        lab += [text(232, y - 4, l1, k=k, size=16, anchor='end'), text(232, y + 16, l2, k=k, size=16, anchor='end')]
        for d in range(step, 217, step):
            parts.append(circle(X(d), y, 7, k=k, fill='b' if k == 'pen' else 'o', sw=2))
            lab.append(text(X(d), y + 28, d, k='muted', size=14))
    for d in (72, 144, 216):
        parts.append(rect(X(d) - 17, 42, 34, 108, k='green', sw=2.4, rx=12))
    lab.append(text(X(108), 190, 'all three line up every 72 days', k='green', size=20, font='scrawl'))
    return svg(660, 204, rough(*parts) + ''.join(lab),
               'Two timelines: Othello and Hamlet line up at 36, 72, 108, 144, 180, 216; Hamlet and Romeo at 72, 144, 216; both at 72, 144 and 216')


Q.append(dict(
    n=23, orig=48, answer='B', topic='Cycles & LCM',
    question=f"""<p>The planet Melpomene has three moons, Othello, Hamlet and Romeo, each moving at a
{hl('constant speed in the same direction', 'y', 1)} in circular orbits.</p>
{fig(Y, 'ps_q23_orbits', 'Three circular orbits round Melpomene; Othello, Hamlet and Romeo are in a straight line out from the planet, on the same side', 300)}
<p>Othello takes {hl('20 days', 'g', 2)} to complete one orbit of Melpomene, whereas Hamlet takes {hl('45 days', 'g')} and
Romeo takes {hl('120 days', 'g')}.</p>
<p class="stem">{hl('How often', 'b', 4)} are Melpomene and all three of its moons in line with each other {hl('in the order shown in the diagram', 'p', 3)}?</p>""",
    options={'A': 'every 36 days', 'B': 'every 72 days', 'C': 'every 132 days', 'D': 'every 180 days', 'E': 'every 216 days'},
    notes=[(1, 'y', 'All go round the same way, each at its own steady speed.'),
           (2, 'g', 'Time for one lap: Othello 20 days, Hamlet 45, Romeo 120.'),
           (3, 'p', 'All on the <b>same side</b> of the planet, one behind the other, like the picture. They don’t have to be back at their starting points.'),
           (4, 'b', 'The time from one line-up to the next.')],
    steps=[
        f"""<p>Laps done = days ÷ lap time. The moons line up (same side, like the picture) when they have all gone the
<b>same fraction of a lap</b> past the start. Test the options:</p>
{calc(f'36 days: 1.8, 0.8, 0.3 laps {cross()}', f'72 days: 3.6, 1.6, 0.6 laps {tick()} all 0.6 of a lap round',
      f'132 days: 6.6, 2.93, 1.1 laps {cross()}', f'180 days: 9, 4, 1.5 laps {cross()} Romeo is half a lap out',
      f'216 days: 10.8, 4.8, 1.8 laps {tick()} but that is later than 72')}
{_orbits()}""",
        f"""<p>Why 72? Think of a race track. Each day Othello gains on Hamlet, and Hamlet gains on Romeo:</p>
{calc(f'Othello gains {frac(1, 20)} − {frac(1, 45)} = {frac(9, 180)} − {frac(4, 180)} = {frac(1, 36)} of a lap a day {ar()} catches Hamlet every 36 days',
      f'Hamlet gains {frac(1, 45)} − {frac(1, 120)} = {frac(8, 360)} − {frac(3, 360)} = {frac(1, 72)} of a lap a day {ar()} catches Romeo every 72 days')}
{_lineups()}
{calc(f'first time both happen together = {boxed("every 72 days")}')}""",
    ],
    answer_text='Every 72 days: Othello catches Hamlet every 36 days and Hamlet catches Romeo every 72 days.',
    why={'A': 'Every 36 days Othello and Hamlet line up, but Romeo is somewhere else (only 0.3 of a lap round).',
         'C': 'At 132 days the moons have done 6.6, 2.93 and 1.1 laps: three different places.',
         'D': '180 is when Othello and Hamlet are both back at the start (LCM of 20 and 45). Romeo has done 1½ laps and is on the far side: in a straight line, but not in the order shown.',
         'E': 'They are lined up at 216 days, but that is the third time: it happens every 72 days.'},
    fast='Laps = days ÷ period. 72 days gives 3.6, 1.6 and 0.6 laps: the same 0.6 for all three. 36 fails (0.8, 0.8, 0.3).',
))


# ---------------------------------------------------------------- 24 (Q49)
def _van_graph():
    X = lambda m: 70 + m * 4.3
    Yc = lambda c: 270 - (c - 40) * 9
    parts, lab = [], []
    parts += [line(X(0), Yc(40), X(125), Yc(40), k='ink', w=2, head=True), line(X(0), Yc(40), X(0), Yc(68), k='ink', w=2, head=True)]
    for m in (0, 40, 80, 120):
        parts.append(line(X(m), Yc(40) - 5, X(m), Yc(40) + 5, k='ink', w=1.6))
        lab.append(text(X(m), Yc(40) + 24, m, k='muted', size=14))
    for c in (47, 63):
        lab.append(text(X(0) - 8, Yc(c) + 5, f'£{c}', k='muted', size=14, anchor='end'))
    lab.append(text(X(62), Yc(40) + 46, 'miles', k='ink', size=16))
    four = [(0, 47), (40, 47), (110, 68)]
    parts.append(poly([(X(m), Yc(c)) for m, c in four], k='pen', sw=3, closed=False))
    parts.append(line(X(0), Yc(63), X(120), Yc(63), k='orange', w=3))
    parts.append(line(X(93.33), Yc(63), X(93.33), Yc(40), k='red', w=1.8, dash=True))
    parts.append(circle(X(93.33), Yc(63), 6, k='red', fill='paper', sw=2.4))
    lab += [text(X(14), Yc(47) - 10, '4 hours: £47', k='pen', size=16, anchor='start'),
            text(X(56), Yc(48.5), '+30p a mile after 40', k='pen', size=15, anchor='start'),
            text(X(8), Yc(63) - 10, '1 day: £63 (up to 120 miles)', k='orange', size=16, anchor='start'),
            text(X(93.33) + 10, Yc(40) - 10, '93⅓', k='red', size=17, anchor='start'),
            text(X(128), Yc(58), 'from 94 miles', k='red', size=18, anchor='end', font='scrawl'),
            text(X(128), Yc(56), 'the day is cheaper', k='red', size=18, anchor='end', font='scrawl')]
    return svg(660, 330, rough(*parts) + ''.join(lab),
               'Cost against miles for the 12 cubic metre van: the 4-hour line is flat at 47 pounds to 40 miles then rises 30p a mile and crosses the flat 63-pound day line at 93 and a third miles')


Q.append(dict(
    n=24, orig=49, answer='E', topic='Graphs & best deal',
    question=f"""<p>One of the options available to purchasers of furniture from Home Help Superstore is to hire
one of the store’s self-drive delivery vans. They have four models, with different capacities,
which can be hired for either 4 hours or 1 day.</p>
{table([['3 m³', '4 hours (40 miles included)', '£33', '20p'], ['3 m³', '1 day (120 miles included)', '£41', '20p'],
        ['8 m³', '4 hours (40 miles included)', '£42', '25p'], ['8 m³', '1 day (120 miles included)', '£54', '25p'],
        [hl('12 m³', 'g'), hl('4 hours (40 miles included)', 'p', 4), hl('£47', 'g'), hl('30p', 'g')],
        [hl('12 m³', 'g'), '1 day (120 miles included)', hl('£63', 'g'), hl('30p', 'g')],
        ['20 m³', '4 hours (40 miles included)', '£52', '35p'], ['20 m³', '1 day (120 miles included)', '£70', '35p']],
       head=['Capacity of Van', 'Duration of Hire', 'Basic Price', 'Price per Extra Mile'])}
<p class="stem">What is the {hl('minimum distance', 'b', 1)} for which it is cheaper to hire a {hl('12 m³ van', 'g', 2)} for a whole day, {hl('even if it could be returned within 4 hours', 'y', 3)}?</p>""",
    options={'A': '64 miles', 'B': '72 miles', 'C': '89 miles', 'D': '92 miles', 'E': '94 miles'},
    notes=[(1, 'b', 'The first whole number of miles where the day hire is <b>cheaper</b>.'),
           (2, 'g', 'Only the two 12 m³ rows matter: £47 for 4 hours, £63 for a day, 30p per extra mile.'),
           (3, 'y', 'Same trip, two ways to pay: compare the 4-hour price with the day price.'),
           (4, 'p', 'The first 40 miles are included: only miles <b>after 40</b> cost 30p.')],
    steps=[
        f"""<p>The day costs £16 more up front:</p>
{calc('£63 − £47 = £16 = 1600p')}""",
        f"""<p>How many extra miles at 30p does £16 pay for?</p>
{calc(f'1600 ÷ 30 = 53⅓ extra miles', f'40 + 53⅓ = 93⅓ miles {ar()} both deals cost £63 here')}
{_van_graph()}""",
        f"""<p>Check the whole numbers either side (the day deal still covers them, as 94 &lt; 120):</p>
{calc(f'93 miles: 47 + 53 × 0.30 = 47 + 15.90 = £62.90 {ar()} 4 hours still cheaper',
      f'94 miles: 47 + 54 × 0.30 = 47 + 16.20 = £63.20 {ar()} day is cheaper {tick()}',
      f'minimum = {boxed("94 miles")}')}
{note('Don’t forget the 40 included miles! 53⅓ on its own is far too low.', 'trap')}""",
    ],
    answer_text='94 miles: the 4-hour hire would cost £63.20, more than the £63 day hire.',
    why={'A': 'At 64 miles the 4-hour hire costs 47 + 24 × 30p = £54.20, much cheaper than £63.',
         'B': 'At 72 miles the 4-hour hire costs 47 + 32 × 30p = £56.60, still cheaper.',
         'C': '89 miles is the change-over for the <b>8 m³</b> van (£12 gap ÷ 25p = 48 extra miles). Wrong row.',
         'D': '92 miles is the change-over for the <b>20 m³</b> van (£18 ÷ 35p ≈ 51.4 extra miles). For the 12 m³ van, 92 miles costs £62.60 for 4 hours, still under £63.'},
    fast='£16 gap ÷ 30p = 53⅓ extra miles. 40 + 53⅓ = 93⅓, so the first whole number of miles where the day wins is 94.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _roll():
    X = lambda m: 30 + m * 60
    parts, lab = [], []
    y = 62
    parts.append(rect(X(0), y, X(10) - X(0), 46, k='ink', fill='paper', sw=2))
    for a in (0, 3, 6):
        parts.append(rect(X(a), y, X(a + 2.5) - X(a), 46, k='ink', fill='b', sw=1.6))
        lab.append(text((X(a) + X(a + 2.5)) / 2, y + 29, f'drop {a // 3 + 1}', k='ink', size=17))
    for a, b in ((2.5, 3), (5.5, 6), (8.5, 10)):
        parts.append(rect(X(a), y, X(b) - X(a), 46, k='red', fill='p', sw=1.4))
    lab.append(text((X(8.5) + X(10)) / 2, y + 29, 'waste', k='red', size=15))
    for i in range(17):
        m = i * 0.6
        parts.append(line(X(m), y - 10, X(m), y - 2, k='violet', w=1.6))
    for m in (0, 2.5, 3, 5.5, 6, 8.5, 10):
        lab.append(text(X(m), y + 68, f'{m:g}', k='muted', size=14))
    lab += [text(X(0), y - 18, 'pattern starts every 60 cm', k='violet', size=15, anchor='start'),
            text(X(5), y + 92, 'one 10 m roll: drops must start at 0, 3, 6 m (whole 60 cm steps)', k='ink', size=16),
            text(X(5), y + 118, '3 drops per roll; the last 1.5 m is too short for a 4th', k='red', size=17, font='scrawl')]
    # wall
    wy = 222
    for i in range(13):
        w = 0.5 if i < 12 else 0.2
        parts.append(rect(X(i * 0.5 * 1.55), wy, w * 1.55 * 60, 50, k='ink', fill='g' if i < 12 else 'y', sw=1.4))
    lab += [text(X(0), wy - 10, 'wall 6.2 m = 12 full drops + a bit = 13 drops', k='green', size=16, anchor='start'),
            text(X(5), wy + 80, '13 drops ÷ 3 per roll = 4⅓ → 5 rolls', k='red', size=21, font='scrawl')]
    return svg(660, 314, rough(*parts) + ''.join(lab),
               'A 10 m roll cut into three 2.5 m drops starting at 0, 3 and 6 m with waste between; the 6.2 m wall needs 13 drops, so 5 rolls')


Q.append(dict(
    n=25, orig=50, answer='C', topic='Measures & rounding',
    question=f"""<p>Rolls of a particular wallpaper have a {hl('repeating pattern every 60 cm', 'y', 1)} of their length. Each roll is
{hl('10 m long and 50 cm wide', 'g', 2)}. A wall {hl('2.5 m high and 6.2 m wide', 'g', 3)} is to be papered from ceiling to
floor with single lengths of paper hung vertically (drops).</p>
{fig(Y, 'ps_q25_wall', 'One length of the wallpaper pattern: shapes cut in half at both side edges so they join up with the next drop', 220)}
<p class="stem">How many rolls of wallpaper will be needed so that the {hl('pattern on each drop matches the next', 'p', 4)}?
({hl('No joins can be made in one vertical drop.', 'p', 5)})</p>""",
    options={'A': '3', 'B': '4', 'C': '5', 'D': '6', 'E': '7'},
    notes=[(1, 'y', 'The pattern repeats every 60 cm down the roll.'),
           (2, 'g', 'Each roll: 10 m of paper, 0.5 m wide.'),
           (3, 'g', 'Each drop is 2.5 m long, and 6.2 m of wall must be covered.'),
           (4, 'p', 'Every drop must start at the <b>same point</b> in the pattern, so drops can only start every 60 cm along the roll.'),
           (5, 'p', 'Each drop is one piece. Offcuts too short for a drop are wasted.')],
    steps=[
        f"""<p>How many drops?</p>
{calc(f'6.2 ÷ 0.5 = 12.4 {ar()} 12 is not enough, so <b>13 drops</b>')}""",
        f"""<p>How much roll does each drop use? It is 2.5 m long, but the next drop must start at the same point in the
pattern, so you skip to the next whole number of 60 cm steps:</p>
{calc('60, 120, 180, 240, <b>300</b> cm', f'2.5 m drop {ar()} uses <b>3 m</b> of roll (0.5 m wasted)')}""",
        f"""<p>Cut up one roll:</p>{_roll()}
{calc('drops start at 0, 3 and 6 m; a 4th would need 9 m to 11.5 m, but the roll is only 10 m',
      f'13 ÷ 3 = 4⅓ {ar()} round up {ar()} {boxed("5 rolls")}')}""",
    ],
    answer_text='5 rolls: 13 drops, and each roll gives only 3 pattern-matched drops.',
    why={'A': '3 rolls only covers 12 drops if you get 4 drops a roll and round 12.4 down. Both are wrong: 13 drops, 3 per roll.',
         'B': '4 rolls ignores the pattern: 4 plain drops of 2.5 m fit on a roll (13 ÷ 4 → 4). The same comes from wall area 15.5 m² ÷ 5 m² = 3.1 → 4. Both forget the waste.',
         'D': '6 rolls would mean only about 2 drops per roll (e.g. allowing 3.6 m per drop) for 12 drops. But 3 m per drop is enough, so 3 drops fit.',
         'E': '7 rolls is 13 drops at 2 per roll, from leaving an extra 60 cm repeat on every drop (3.6 m each). 3 m is already a whole number of repeats.'},
    fast='13 drops. Each uses 3 m (the first multiple of 60 cm that is at least 2.5 m), so 3 drops per 10 m roll. 13 ÷ 3 → 5 rolls.',
))
