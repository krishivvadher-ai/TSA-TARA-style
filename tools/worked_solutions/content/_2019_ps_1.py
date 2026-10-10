from wslib import *

Y = 2019
Q = []

# ---------------------------------------------------------------- 1 (Q2)
def _tax():
    rows = [('Tim', 3000), ('Neil', 5000), ('Veronica', 4500), ('David', 3000), ('Amy', 4000), ('Roz', 3600)]
    X = lambda v: 120 + v * 0.08
    parts, lab = [], []
    for i, (name, v) in enumerate(rows):
        y = 22 + i * 36
        f = 'g' if v == 3000 else 'paper'
        parts.append(rect(X(0), y, X(v) - X(0), 24, k='ink', fill=f, sw=1.6))
        lab.append(text(110, y + 18, name, k='ink', size=17, anchor='end'))
        lab.append(text(X(v) + 8, y + 18, f'${v:,}', k='green' if v == 3000 else 'ink', size=17, anchor='start'))
    parts.append(line(X(3000), 10, X(3000), 240, k='red', w=2.2, dash=True))
    lab.append(text(X(3000), 262, 'Tim pays $3,000', k='red', size=18, font='scrawl'))
    lab.append(text(X(3000) + 150, 262, 'David matches!', k='green', size=20, font='scrawl', anchor='start'))
    return svg(640, 274, rough(*parts) + ''.join(lab),
               'Bar chart of tax paid: Tim 3000, Neil 5000, Veronica 4500, David 3000, Amy 4000, Roz 3600; only David matches Tim')

Q.append(dict(
    n=1, orig=2, answer='C', topic='Percentages',
    question=f"""<p>Each region in the country of Bolandia sets its own tax rate which {hl('applies to the whole of an individual’s annual income', 'y', 1)}.</p>
<p>Below is a table showing tax information relating to six different people.</p>
{table([[hl('Tim', 'g', 2), 'North', hl('$10 000', 'g'), hl('30%', 'g')], ['Neil', 'Central', '$20 000', '25%'],
        ['Veronica', 'West', '$150 000', '3%'], ['David', 'North West', '$50 000', '6%'],
        ['Amy', 'East', '$80 000', '5%'], ['Roz', 'Frontier', '$12 000', '30%']],
       head=['<i>name</i>', '<i>region</i>', '<i>annual income</i>', '<i>tax rate</i>'])}
<p class="stem">Who pays the {hl('same amount of tax', 'b', 3)} in a year as Tim?</p>""",
    options={'A': 'Neil', 'B': 'Veronica', 'C': 'David', 'D': 'Amy', 'E': 'Roz'},
    notes=[(1, 'y', 'No tax-free allowance, no bands. Tax = rate × whole income. Simple!'),
           (2, 'g', 'Tim’s row is the target. Work out his tax first.'),
           (3, 'b', 'The same <b>amount in dollars</b>, not the same rate. Roz has the same rate, which is the trap.')],
    steps=[
        f"""<p>Tim first:</p>
{calc(f'30% of $10 000 = 0.3 × 10 000 = <b>$3 000</b>')}""",
        f"""<p>Now everyone else. Trick: find 1% (move the decimal point two places), then multiply by the rate.</p>
{calc('Neil: 1% = 200 → 25 × 200 = $5 000',
      'Veronica: 1% = 1 500 → 3 × 1 500 = $4 500',
      f'David: 1% = 500 → 6 × 500 = <b>$3 000</b> {tick()}',
      'Amy: 1% = 800 → 5 × 800 = $4 000',
      'Roz: 1% = 120 → 30 × 120 = $3 600')}""",
        f"""{_tax()}
{calc(f'same as Tim {ar()} {boxed("David")}')}
{note('Roz is the trap: same 30% rate as Tim, but her income is bigger, so she pays more.', 'trap')}""",
    ],
    answer_text='David: 6% of $50 000 = $3 000, exactly the same as Tim’s 30% of $10 000.',
    why={'A': 'Neil pays 25% of $20 000 = $5 000.',
         'B': 'Veronica pays 3% of $150 000 = $4 500. A tiny rate, but a huge income.',
         'D': 'Amy pays 5% of $80 000 = $4 000.',
         'E': 'Roz has the <b>same rate</b> as Tim (30%), but on $12 000 that is $3 600, not $3 000.'},
    fast='Tim pays $3 000. Scan for rate × income = 3 000: 6% of 50 000 = 6 × 500 = 3 000. David.',
))

# ---------------------------------------------------------------- 2 (Q6)
def _flag():
    u, ox, oy = 70, 40, 40
    parts = [rect(ox, oy, u, 2 * u, k='ink', fill='p', sw=2.2),
             rect(ox + 3 * u, oy, u, 2 * u, k='ink', fill='p', sw=2.2),
             rect(ox + u, oy, 2 * u, 2 * u, k='ink', fill='paper', sw=2.2)]
    for i in range(1, 4):
        parts.append(line(ox + i * u, oy, ox + i * u, oy + 2 * u, k='muted', w=1.2, dash=True))
    parts.append(line(ox, oy + u, ox + 4 * u, oy + u, k='muted', w=1.2, dash=True))
    parts.append(rect(ox + 1.5 * u + 4, oy + 0.5 * u + 4, u - 8, u - 8, k='red', fill='p', sw=2))
    lab = [text(ox + 0.5 * u, oy - 12, '1', k='ink', size=18), text(ox + 2 * u, oy - 12, '2', k='ink', size=18),
           text(ox + 3.5 * u, oy - 12, '1', k='ink', size=18), text(ox - 14, oy + u + 6, '2', k='ink', size=18),
           text(ox + 0.5 * u, oy + 0.5 * u + 6, '1', k='red', size=18), text(ox + 0.5 * u, oy + 1.5 * u + 6, '1', k='red', size=18),
           text(ox + 3.5 * u, oy + 0.5 * u + 6, '1', k='red', size=18), text(ox + 3.5 * u, oy + 1.5 * u + 6, '1', k='red', size=18),
           text(ox + 2 * u, oy + u - 4, 'leaf', k='red', size=16), text(ox + 2 * u, oy + u + 16, '= 1', k='red', size=16),
           text(ox + 2 * u, oy + 2 * u + 28, 'white square = 4 small squares', k='ink', size=16)]
    tx = ox + 4 * u + 40
    lab += [text(tx, 70, 'red = 2 + 2 + 1 = 5', k='red', size=22, font='scrawl', anchor='start'),
            text(tx, 108, 'white = 4 − 1 = 3', k='pen', size=22, font='scrawl', anchor='start'),
            text(tx, 150, 'red : white = 5 : 3', k='green', size=24, font='scrawl', anchor='start')]
    return svg(620, 230, rough(*parts) + ''.join(lab),
               'Flag on a grid of 8 unit squares: red strips 2 squares each, leaf 1 square, white 3 squares; red to white is 5 to 3')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Area & ratio',
    question=f"""<p>Below is a greyscale image of the flag of Canada. The flag consists of two red strips on the left
and the right, a white square in the middle, and a red maple leaf in the centre.</p>
{fig(Y, 'ps_q02_flag', 'Flag: grey strip, white square with a grey maple leaf, grey strip; widths marked 1, 2, 1', 430)}
<p>[diagram not to scale]</p>
<p>{hl('The width of the white square is twice as large as the width of a red strip', 'g', 1)}. {hl('The red maple leaf occupies a quarter of the square in the middle', 'p', 2)}.</p>
<p class="stem">What is the {hl('ratio of red to white', 'b', 3)} in the flag?</p>""",
    options={'A': '1 : 1', 'B': '2 : 1', 'C': '3 : 2', 'D': '5 : 3', 'E': '5 : 4'},
    notes=[(1, 'g', 'Widths 1 : 2 : 1. And it is a <b>square</b>, so it is 2 tall as well.'),
           (2, 'p', 'The leaf turns a quarter of the white square red. Add it to red <b>and</b> take it off white.'),
           (3, 'b', 'Compare areas: red area : white area.')],
    steps=[
        f"""<p>Give the strip width 1 unit. The square is 2 by 2, so the strips are 1 by 2. Draw it on a grid of unit squares:</p>
{_flag()}""",
        f"""{calc('flag = 4 × 2 = 8 small squares',
                  'red strips = 2 + 2 = 4',
                  'white square = 4, leaf = ¼ of 4 = 1',
                  f'red = 4 + 1 = 5, white = 4 − 1 = 3 {ar()} {boxed("5 : 3")}')}
{note('5 + 3 = 8, the whole flag. Always check the two parts add back up to the total.', 'check')}""",
    ],
    answer_text='5 : 3. Red = 4 (strips) + 1 (leaf) = 5 squares; white = 4 − 1 = 3 squares.',
    why={'A': '1 : 1 forgets the leaf: strips 4 against square 4.',
         'B': '2 : 1 would need the leaf to cover a third of the square (red 4 + 4/3 against white 8/3). It only covers a quarter.',
         'C': '3 : 2 would need the leaf to cover only a fifth of the square.',
         'E': '5 : 4 adds the leaf to the red but forgets to take it away from the white.'},
    fast='Units: strips 1 × 2 each, square 2 × 2. Red 2 + 2 + 1 = 5, white 4 − 1 = 3. 5 : 3.',
))

# ---------------------------------------------------------------- 3 (Q7)
def _gaps():
    rows = [('Arnold', 10, 'Rosenberg v Robson'), ('Betty', 30, 'Kettering v De Vere'), ('Clara', 10, 'Nolan v Robson'),
            ('Cora', 0, 'Kettering v Rosenberg'), ('Dave', 0, 'De Vere v Rosenberg'), ('Dennis', 10, 'Kettering v Nolan'),
            ('Hillary', 40, 'Robson v De Vere'), ('Janine', 10, 'Rosenberg v Nolan'), ('Laurence', 10, 'Nolan v De Vere')]
    X = lambda v: 110 + v * 7
    parts, lab = [], []
    for i, (name, g, pair) in enumerate(rows):
        y = 20 + i * 30
        f = 'y' if g == 40 else 'paper'
        if g:
            parts.append(rect(X(0), y, X(g) - X(0), 20, k='ink', fill=f, sw=1.6))
        else:
            parts.append(line(X(0), y, X(0), y + 20, k='ink', w=2))
        lab.append(text(100, y + 16, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(g) + 8, y + 16, f'{g}  ({pair})', k='red' if g == 40 else 'ink', size=15, anchor='start'))
    lab.append(text(X(0), 300, 'gap = |first mark − second mark|', k='muted', size=15, anchor='start'))
    return svg(640, 310, rough(*parts) + ''.join(lab),
               'Gap between the two examiners for each student; the biggest is 40 for Hillary, marked by Robson and De Vere')

Q.append(dict(
    n=3, orig=7, answer='E', topic='Reading tables',
    question=f"""<p>The table below shows the breakdown of marks awarded to students taking an exam.</p>
{table([['Arnold Jones', 'Ms Rosenberg', '80', 'Mr Robson', '70', '75'],
        ['Betty Markham', 'Mr Kettering', '90', 'Mrs De Vere', '60', '75'],
        ['Clara Bird', 'Ms Nolan', '60', 'Mr Robson', '50', '55'],
        ['Cora Smith', 'Mr Kettering', '80', 'Ms Rosenberg', '80', '80'],
        ['Dave Howard', 'Mrs De Vere', '90', 'Ms Rosenberg', '90', '90'],
        ['Dennis Garton', 'Mr Kettering', '80', 'Ms Nolan', '70', '75'],
        ['Hillary Gordon', 'Mr Robson', hl('50', 'g'), 'Mrs De Vere', hl('90', 'g'), '70'],
        ['Janine Turner', 'Ms Rosenberg', '80', 'Ms Nolan', '90', '85'],
        ['Laurence Rothman', 'Ms Nolan', '60', 'Mrs De Vere', '50', '55']],
       head=['<i>student</i>', '<i>first examiner</i>', f'<i>{hl("first mark", "g", 1)}</i>', '<i>second examiner</i>',
             f'<i>{hl("second mark", "g")}</i>', f'<i>{hl("final mark", "p", 2)}</i>'])}
<p>The mark scheme is as follows: 90 = excellent; 80 = good; 70 = satisfactory; 60 = acceptable;
50 = fail. The final mark is the average between the marks given by the first and second
examiners.</p>
<p class="stem">Which pair of examiners {hl('disagreed the most', 'b', 3)} on the marks they awarded a student?</p>""",
    options={'A': 'Mr Kettering and Mrs De Vere', 'B': 'Mr Robson and Ms Nolan', 'C': 'Ms Rosenberg and Ms Nolan',
             'D': 'Mr Kettering and Ms Rosenberg', 'E': 'Mrs De Vere and Mr Robson'},
    notes=[(1, 'g', 'The two marks for the same student: these are what you compare.'),
           (2, 'p', 'Red herring! The average hides the disagreement. Ignore this column.'),
           (3, 'b', 'Biggest gap between the two marks for one student.')],
    steps=[
        f"""<p>For each student, find the gap between the first and second marks:</p>{_gaps()}""",
        f"""{calc('biggest gap = 90 − 50 = 40 (Hillary Gordon)', f'marked by Mr Robson and Mrs De Vere {ar()} {boxed("E")}')}
{note('The mark-scheme words (excellent, fail…) are just decoration: 50 = fail and 90 = excellent is the widest possible split.', 'tip')}""",
    ],
    answer_text='Mrs De Vere and Mr Robson: 90 against 50 for Hillary Gordon, a gap of 40.',
    why={'A': 'Kettering and De Vere disagree by 30 on Betty (90 v 60): big, but not the biggest.',
         'B': 'Robson and Nolan only differ by 10 on Clara (60 v 50).',
         'C': 'Rosenberg and Nolan only differ by 10 on Janine (80 v 90).',
         'D': 'Kettering and Rosenberg <b>agree</b> completely on Cora (80 and 80).'},
    fast='Scan for the biggest jump between the two mark columns: 50 and 90 for Hillary. Robson and De Vere.',
))

# ---------------------------------------------------------------- 4 (Q8)
def _tickets():
    data = [('Thu', 8, 6), ('Fri', 6, 9), ('Sat', 12, 5)]
    s, x0 = 22, 70
    parts, lab = [], []
    for i, (day, ns, np_) in enumerate(data):
        y = 34 + i * 46
        lab.append(text(x0 - 10, y + 17, day, k='ink', size=18, anchor='end'))
        for j in range(ns):
            parts.append(rect(x0 + j * (s + 2), y, s, s, k='ink', fill='b', sw=1.3))
        px = x0 + ns * (s + 2) + 10
        for j in range(np_):
            parts.append(rect(px + j * (s + 2), y, s, s, k='ink', fill='o', sw=1.3))
        lab.append(text(px + np_ * (s + 2) + 8, y + 17, f'{ns * 25} S + {np_ * 25} P', k='muted', size=15, anchor='start'))
    parts += [rect(x0, 8, 14, 14, k='ink', fill='b', sw=1.3), rect(x0 + 190, 8, 14, 14, k='ink', fill='o', sw=1.3)]
    lab += [text(x0 + 22, 20, '= 25 Standard', k='ink', size=15, anchor='start'),
            text(x0 + 212, 20, '= 25 Premium (dearer)', k='ink', size=15, anchor='start'),
            text(x0, 196, 'Thu → Fri: swap 2 blue for 3 orange. Fewer cheap, more dear:', k='pen', size=16, anchor='start'),
            text(x0, 218, 'Friday ALWAYS beats Thursday.', k='pen', size=18, font='scrawl', anchor='start'),
            text(x0, 248, 'Fri → Sat: +6 blue but −4 orange. Who wins depends on prices.', k='orange', size=16, anchor='start')]
    return svg(640, 262, rough(*parts) + ''.join(lab),
               'Ticket blocks of 25: Thursday 8 standard and 6 premium, Friday 6 and 9, Saturday 12 and 5')

Q.append(dict(
    n=4, orig=8, answer='E', topic='Charts & reasoning',
    question=f"""<p>The bar chart shows the total {hl('numbers of tickets', 'p', 1)} sold for a concert over three nights.</p>
{fig(Y, 'ps_q04_chart', 'Bar chart: Thursday 200 standard, 150 premium; Friday 150 standard, 225 premium; Saturday 300 standard, 125 premium', 520)}
<p>{hl('Premium tickets are more expensive than Standard tickets', 'y', 2)}.</p>
<p class="stem">Which one of the following statements is correct?</p>""",
    options={'A': 'The highest total sales income was for Thursday.', 'B': 'The highest total sales income was for Friday.',
             'C': 'The highest total sales income could have been for Thursday or Friday.',
             'D': 'The highest total sales income could have been for Thursday or Saturday.',
             'E': 'The highest total sales income could have been for Friday or Saturday.'},
    notes=[(1, 'p', 'Numbers of tickets, not money. We don’t know the prices!'),
           (2, 'y', 'The only price fact: each Premium costs more than each Standard. Use it to compare nights.')],
    steps=[
        f"""<p>Read the chart:</p>
{calc('Thursday: 200 Standard, 150 Premium', 'Friday: 150 Standard, 225 Premium', 'Saturday: 300 Standard, 125 Premium')}""",
        f"""<p>Picture each night as blocks of 25 tickets:</p>{_tickets()}""",
        f"""<p><b>Thursday v Friday:</b> Friday has 50 fewer Standard but 75 more Premium. 75 dear tickets are worth more than 50 cheap ones, whatever the prices.
So Thursday can <b>never</b> be the highest {ar()} A, C, D are out.</p>""",
        f"""<p><b>Friday v Saturday:</b> try two price pairs.</p>
{calc('Standard £10, Premium £11: Fri = 1500 + 2475 = 3975, Sat = 3000 + 1375 = 4375 → Saturday wins',
      'Standard £10, Premium £20: Fri = 1500 + 4500 = 6000, Sat = 3000 + 2500 = 5500 → Friday wins',
      f'either could be highest {ar()} {boxed("E")}')}""",
    ],
    answer_text='Friday or Saturday: Friday always beats Thursday, but Friday v Saturday depends on the prices.',
    why={'A': 'Thursday always loses to Friday: Friday swaps 50 cheap tickets for 75 dear ones.',
         'B': 'Friday is not certain: if Premium is only a little dearer (e.g. £11 v £10), Saturday’s 300 Standard tickets win.',
         'C': 'Thursday can’t be highest, because Friday always beats it.',
         'D': 'Same problem: Thursday can’t be highest.'},
    fast='Fri v Thu: −50 S, +75 P → Fri always more. Fri v Sat: +150 S, −100 P → depends on prices. So Friday or Saturday.',
))

# ---------------------------------------------------------------- 5 (Q12)
def _lamps():
    s, x0 = 60, 130
    parts, lab = [], []
    for t in range(9):
        parts.append(line(x0 + t * s, 30, x0 + t * s, 176, k='muted', w=1, dash=True))
        lab.append(text(x0 + t * s, 196, t, k='muted', size=15))
    rows = [('lamp 1', [(0, 1), (2, 3), (4, 5), (6, 7)], 40), ('lamp 2', [(0, 2), (4, 6)], 90)]
    for name, ons, y in rows:
        lab.append(text(x0 - 12, y + 20, name, k='ink', size=17, anchor='end'))
        parts.append(rect(x0, y, 8 * s, 28, k='ink', fill='paper', sw=1.4))
        for a, b in ons:
            parts.append(rect(x0 + a * s, y, (b - a) * s, 28, k='ink', fill='y', sw=1.4))
            lab.append(text(x0 + (a + b) / 2 * s, y + 20, 'on', k='ink', size=15))
    y = 140
    lab.append(text(x0 - 12, y + 20, 'both dark', k='red', size=17, anchor='end'))
    for a in (3, 7):
        parts.append(rect(x0 + a * s, y, s, 28, k='red', fill='p', sw=2))
    lab.append(text(x0 + 4 * s, 216, 'seconds', k='muted', size=15))
    parts.append(path(f'M{x0} 26 q0 -10 10 -10 L{x0 + 4 * s - 10} 16 q10 0 10 10', k='green', sw=2))
    lab.append(text(x0 + 2 * s, 11, 'pattern repeats every 4 s', k='green', size=16))
    return svg(640, 228, rough(*parts) + ''.join(lab),
               'Timeline 0 to 8 seconds: lamp 1 on every other second, lamp 2 on two off two; both dark from 3 to 4 and 7 to 8')

Q.append(dict(
    n=5, orig=12, answer='C', topic='Cycles & timings',
    question=f"""<p>When riding my bike in the dark, I use two rear bike lamps. Both of the lamps are in ‘flashing
mode’, which means that they repeatedly emit light for a set period of time at set intervals. The
reasons for using two lights are that it reduces the amount of time when neither of the lamps
emit light, and that if one of the lamps stops working, other road users can still see me on the
road. {hl('One of the lamps shines for one second and goes dark for one second repeatedly', 'g', 1)}; {hl('the other lamp shines for two seconds and goes dark for two seconds repeatedly', 'g', 2)}. I always {hl('turn both lamps on simultaneously', 'y', 3)} at the start of my ride.</p>
<p class="stem">For how many seconds {hl('in each minute', 'g', 4)} do {hl('<b>neither</b>', 'b', 5)} of the lamps shine when they are in use?</p>""",
    options={'A': '10', 'B': '12', 'C': '15', 'D': '20', 'E': '30'},
    notes=[(1, 'g', 'Lamp 1: a 2-second cycle (on 1, off 1).'),
           (2, 'g', 'Lamp 2: a 4-second cycle (on 2, off 2).'),
           (3, 'y', 'Both start “on” at time 0, so the patterns are lined up.'),
           (4, 'g', '60 seconds.'),
           (5, 'b', 'Count only the moments when BOTH are dark.')],
    steps=[
        f"""<p>Draw both lamps on a timeline:</p>{_lamps()}""",
        f"""<p>The whole pattern repeats every 4 seconds (both cycles fit into 4). In each 4 seconds only 1 second is dark for both (from 3 s to 4 s).</p>
{calc('60 ÷ 4 = 15 repeats in a minute', f'15 × 1 second = {boxed("15")}')}
{note('Lamp 2 is dark for 2 s of every 4. Lamp 1 shines for half of that time. So both are dark for 1 s in every 4: a quarter of 60 = 15.', 'check')}""",
    ],
    answer_text='15 seconds: 1 dark second in every 4-second cycle, and 60 ÷ 4 = 15.',
    why={'A': '10 would mean one dark second every 6 seconds, but the pattern repeats every 4.',
         'B': '12 would mean one dark second every 5 seconds: the cycle is 4 seconds, not 5.',
         'D': '20 comes from a 3-second cycle (adding 1 + 2), but the lamps line up again every 4 seconds.',
         'E': '30 is how long <b>lamp 1</b> is dark. Lamp 2 is shining for half of those seconds.'},
    fast='Cycle = 4 s. Both dark only in second 4 of each cycle. 60 ÷ 4 = 15.',
))

# ---------------------------------------------------------------- 6 (Q13)
def _perkm():
    rows = [('Luton–London', 14, 56), ('Brandenburg–Berlin', 8, 69), ('Karis–Helsinki', 6, 75),
            ('Uppsala–Stockholm', 6, 72), ('Drogheda–Dublin', 5, 46)]
    X = lambda v: 190 + v * 1300
    parts, lab = [], []
    for i, (name, p, km) in enumerate(rows):
        y = 22 + i * 38
        v = p / km
        f = 'g' if name.startswith('Karis') else 'paper'
        parts.append(rect(X(0), y, X(v) - X(0), 24, k='ink', fill=f, sw=1.6))
        lab.append(text(180, y + 18, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 8, y + 18, f'{p} ÷ {km} ≈ {v:.3f}', k='green' if f == 'g' else 'ink', size=15, anchor='start'))
    lab.append(text(X(0), 222, '% of monthly wage per km (smaller = better)', k='muted', size=15, anchor='start'))
    return svg(640, 232, rough(*parts) + ''.join(lab),
               'Percentage per kilometre for each route: Luton 0.25, Brandenburg 0.116, Karis 0.080, Uppsala 0.083, Drogheda 0.109; Karis is smallest')

Q.append(dict(
    n=6, orig=13, answer='C', topic='Rates & proportion',
    question=f"""<p>The following table compares five selected commuting routes in different European countries
with respect to the length of the journey and the monthly cost of a season ticket as a
percentage of average monthly wages.</p>
<p style="text-align:center">comparison of selected commuting routes</p>
{table([['Luton–London', 'UK', '56', '14'], ['Brandenburg–Berlin', 'Germany', '69', '8'],
        ['Karis–Helsinki', 'Finland', '75', '6'], ['Uppsala–Stockholm', 'Sweden', '72', '6'],
        ['Drogheda–Dublin', 'Ireland', '46', '5']],
       head=['<i>journey</i>', '<i>country</i>', f'<i>{hl("length", "g", 1)}</i> (km)', f'<i>{hl("cost as a percentage of average monthly wages", "g")}</i>'])}
<p class="stem">On average, the commuters of which route spend the {hl('lowest proportion of their wages per kilometre', 'b', 2)} of the route?</p>""",
    options={'A': 'Luton–London', 'B': 'Brandenburg–Berlin', 'C': 'Karis–Helsinki', 'D': 'Uppsala–Stockholm', 'E': 'Drogheda–Dublin'},
    notes=[(1, 'g', 'The two numbers you need for each route.'),
           (2, 'b', '“Per kilometre” = divide the percentage by the length. Smallest answer wins.')],
    steps=[
        f"""<p>Percentage ÷ km for each route:</p>{_perkm()}""",
        f"""<p>Quick mental comparisons, no calculator needed:</p>
<ul><li>Karis (6% over 75 km) v Uppsala (6% over 72 km): same 6%, but Karis spreads it over more km {ar()} Karis is lower.</li>
<li>Karis: 6 ÷ 75 = 0.08. Drogheda: 5 ÷ 46 is more than 5 ÷ 50 = 0.1. Brandenburg: 8 ÷ 69 is more than 8 ÷ 80 = 0.1.</li></ul>
{calc(f'lowest = 0.08 {ar()} {boxed("Karis–Helsinki")}')}""",
    ],
    answer_text='Karis–Helsinki: 6% ÷ 75 km = 0.08% per km, the smallest.',
    why={'A': 'Luton–London is the <b>highest</b>: 14 ÷ 56 = 0.25% per km.',
         'B': 'Brandenburg–Berlin: 8 ÷ 69 ≈ 0.12% per km.',
         'D': 'Uppsala–Stockholm has the same 6% as Karis but a shorter route (72 km), so a bit more per km (≈ 0.083).',
         'E': 'Drogheda–Dublin has the lowest <b>percentage</b> (5%), but it is the shortest route, so per km it is ≈ 0.11.'},
    fast='Same 6% for Karis and Uppsala, Karis is longer. Others are 0.1 or more (5/46, 8/69, 14/56). Karis.',
))

# ---------------------------------------------------------------- 7 (Q14)
def _cars():
    parts, lab = [], []
    for gx, xl, yl, c1, c2, n1, n2 in ((60, 'age →', 'price ↑', (190, 120), (100, 50), 'older, cheaper', 'newer, dearer'),
                                       (380, 'size →', 'speed ↑', (445, 120), (560, 50), 'slower, smaller', 'faster, bigger')):
        parts += [line(gx, 170, gx + 230, 170, k='ink', head=True), line(gx, 170, gx, 20, k='ink', head=True)]
        lab += [text(gx + 200, 194, xl, k='muted', size=16), text(gx - 8, 30, yl, k='muted', size=16, anchor='end')]
        parts += [circle(*c1, 7, k='orange', fill='o'), circle(*c2, 7, k='pen', fill='b')]
        lab += [text(c1[0] + 12, c1[1] + 6, 'car 1', k='orange', size=16, anchor='start'),
                text(c1[0], c1[1] + 30, n1, k='orange', size=15),
                text(c2[0] + 12, c2[1] + 6, 'car 2', k='pen', size=16, anchor='start'),
                text(c2[0] + 20, c2[1] + 30, n2, k='pen', size=15)]
    lab += [text(320, 236, 'car 2: newer, dearer, faster, bigger', k='pen', size=20, font='scrawl'),
            text(320, 264, 'car 1: older, cheaper, slower, smaller', k='orange', size=20, font='scrawl')]
    return svg(660, 280, rough(*parts) + ''.join(lab),
               'Both diagrams redrawn: car 2 is newer, dearer, faster and bigger; car 1 is older, cheaper, slower and smaller')

Q.append(dict(
    n=7, orig=14, answer='B', topic='Reading graphs',
    question=f"""<p>Peter has drawn {hl('two diagrams', 'y', 1)} showing information about the two cars owned by his parents:</p>
{fig(Y, 'ps_q07_cars', 'Left: market price against age, car 2 high price low age, car 1 lower price greater age. Right: max speed against size, car 1 low and small, car 2 high and big', 470)}
<p class="stem">Which one of the following statements is {hl('<b>not</b>', 'b', 2)} correct?</p>""",
    options={'A': 'The more expensive car is newer.', 'B': 'The cheaper car is bigger.', 'C': 'The older car is slower.',
             'D': 'The newer car is bigger.', 'E': 'The slower car is smaller.'},
    notes=[(1, 'y', 'No numbers: just compare the two dots on each diagram. Further right = more, higher up = more.'),
           (2, 'b', 'Find the <b>false</b> statement. Four are true.')],
    steps=[
        f"""<p>Turn each diagram into words:</p>{_cars()}
<p>Careful with age: further right = <b>older</b>, so car 2 (on the left) is the newer one.</p>""",
        f"""<p>Now test each statement:</p>
{calc(f'A: dearer = car 2, newer = car 2 {tick()}',
      f'B: cheaper = car 1, but car 1 is <b>smaller</b> {cross()}',
      f'C: older = car 1, slower = car 1 {tick()}',
      f'D: newer = car 2, bigger = car 2 {tick()}',
      f'E: slower = car 1, smaller = car 1 {tick()}',
      f'not correct {ar()} {boxed("B")}')}""",
    ],
    answer_text='B: the cheaper car (car 1) is the smaller one, not the bigger one.',
    why={'A': 'True: car 2 is both dearer and newer (lower age).',
         'C': 'True: car 1 is older and slower.',
         'D': 'True: car 2 is newer and bigger.',
         'E': 'True: car 1 is slower and smaller.'},
    fast='Car 2 wins everything (newer, dearer, faster, bigger). B pairs “cheaper” (car 1) with “bigger” (car 2): false.',
))

# ---------------------------------------------------------------- 8 (Q18)
def _laps():
    s, x0 = 16, 110
    parts, lab = [], []
    rows = [('Alec', 3, 'pen', 40), ('Barry', 5, 'orange', 90), ('Colin', 6, 'violet', 140)]
    for name, t, k, y in rows:
        parts.append(line(x0, y, x0 + 30 * s, y, k='muted', w=1.5))
        lab.append(text(x0 - 12, y + 6, name, k=k, size=18, anchor='end'))
        for m in range(t, 31, t):
            parts.append(circle(x0 + m * s, y, 6, k=k, fill='paper', sw=2.2))
        lab.append(text(x0 + 30 * s + 18, y + 6, f'{30 // t} laps', k=k, size=17, anchor='start'))
    parts.append(line(x0 + 30 * s, 20, x0 + 30 * s, 162, k='green', w=2.6, dash=True))
    parts.append(line(x0 + 15 * s, 20, x0 + 15 * s, 162, k='muted', w=1.6, dash=True))
    for m in (0, 5, 10, 15, 20, 25, 30):
        lab.append(text(x0 + m * s, 186, m, k='muted', size=14))
    lab += [text(x0 + 15 * s, 206, 'minutes', k='muted', size=14),
            text(x0 + 30 * s, 14, 'all 3 together at 30 min', k='green', size=16),
            text(x0 + 15 * s, 14, '15 min: Colin is mid-lap', k='muted', size=14)]
    return svg(680, 214, rough(*parts) + ''.join(lab),
               'Timeline of start-line crossings: Alec every 3 minutes, Barry every 5, Colin every 6; all meet at 30 minutes')

Q.append(dict(
    n=8, orig=18, answer='B', topic='Cycles & LCM',
    question=f"""<p>Three friends are training to run a marathon. Part of this training involves running steadily
round a track in the local park. They are all at different stages in their training schedules so
they run at different speeds. {hl('Alec completes each lap in 3 minutes, Barry takes 5 minutes and Colin takes 6 minutes', 'g', 1)}.</p>
<p>{hl('They all leave the start line at the same time', 'y', 2)}.</p>
<p class="stem">If they each maintain their running speed throughout the session, {hl('how many more laps will Alec have completed compared to Barry', 'b', 3)} when {hl('the three of them next cross the start line together', 'p', 4)}?</p>""",
    options={'A': '2', 'B': '4', 'C': '5', 'D': '6', 'E': '10'},
    notes=[(1, 'g', 'Lap times 3, 5 and 6 minutes.'),
           (2, 'y', 'They start together at time 0.'),
           (3, 'b', 'Alec’s laps minus Barry’s laps.'),
           (4, 'p', 'All <b>three</b>, not just Alec and Barry. Find the first time that is in all three times tables.')],
    steps=[
        f"""<p>They are together at the line when the time is a multiple of 3, 5 <b>and</b> 6 (the lowest common multiple).</p>
{calc('multiples of 6: 6, 12, 18, 24, <b>30</b>', '30 is in the 3 and 5 times tables too ' + tick(), f'together again after <b>30 minutes</b>')}""",
        f"""{_laps()}
{calc('Alec: 30 ÷ 3 = 10 laps', 'Barry: 30 ÷ 5 = 6 laps', f'10 − 6 = {boxed("4")}')}
{note('At 15 minutes Alec and Barry are both at the line (5 and 3 laps), but Colin is halfway round. That gives the trap answer 2.', 'trap')}""",
    ],
    answer_text='4 more laps: after 30 minutes Alec has run 10 laps and Barry 6.',
    why={'A': '2 is the gap at 15 minutes, when only Alec and Barry are at the line. Colin isn’t there (15 ÷ 6 = 2.5 laps).',
         'C': '5 is Colin’s number of laps (or Alec minus Colin), not Alec minus Barry.',
         'D': '6 is Barry’s total number of laps, not the difference.',
         'E': '10 is Alec’s total, not how many more than Barry.'},
    fast='LCM of 3, 5, 6 = 30. Alec 10 laps, Barry 6. Difference 4.',
))
