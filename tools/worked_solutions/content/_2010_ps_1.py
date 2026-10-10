from wslib import *

Y = 2010
Q = []

# ---------------------------------------------------------------- 1 (Q2)
def _swim():
    parts, lab = [], []
    lab.append(text(150, 26, 'No card: every single visit', k='ink', size=19, font='scrawl'))
    lab.append(text(480, 26, 'With the Swimcard', k='ink', size=19, font='scrawl'))
    for x, s, p in ((40, 1.3, '£2'), (85, 1.3, '£2'), (135, 1, '£1'), (175, 1, '£1'), (215, 1, '£1'), (255, 1, '£1')):
        lab.append(stick_person(x, 112, k='pen', s=s))
        lab.append(text(x, 138, p, k='ink', size=17))
    lab.append(text(150, 176, '4 + 4 = £8 a visit', k='pen', size=18))
    lab.append(text(150, 204, '£8 × 40 visits = £320', k='pen', size=20, font='scrawl'))
    parts.append(rect(346, 50, 200, 100, k='green', sw=2, rx=12))
    for x, s in ((370, 1.3), (410, 1.3), (455, 1), (490, 1), (525, 1)):
        lab.append(stick_person(x, 112, k='green', s=s))
    lab.append(text(446, 140, 'all paid for by the card', k='green', size=14))
    lab.append(stick_person(592, 112, k='orange', s=1))
    lab.append(text(592, 138, '50p', k='orange', size=17))
    lab.append(text(592, 46, 'child 4', k='orange', size=14))
    lab.append(text(480, 176, '£50 + 40 × 50p', k='pen', size=18))
    lab.append(text(480, 204, '= £50 + £20 = £70', k='pen', size=20, font='scrawl'))
    lab.append(text(320, 244, 'saving = £320 − £70 = £250', k='red', size=22, font='scrawl'))
    return svg(640, 258, rough(*parts) + ''.join(lab),
               'Left: two adults at £2 and four children at £1, £8 a visit, £320 for 40 visits. Right: the card covers five of them, the fourth child pays 50p, £70 in all')

Q.append(dict(
    n=1, orig=2, answer='D', topic='Money & best deal',
    question=f"""<p>Splashford Swimming Pool charges {hl('£2 per session for adults and £1 for children', 'g', 1)}.</p>
<p>Also available is a Family Swimcard. At a cost of £50, the Family Swimcard allows unlimited use of the pool for one year for
{hl('2 adults and up to 3 children', 'y', 2)}. For larger families, {hl("every additional child must pay half the children's rate each time", 'p', 3)}.</p>
<p>Mr and Mrs Teal and their {hl('4 children', 'g', 4)} are keen swimmers. They used their Swimcard when the family went swimming {hl('40 times', 'g', 5)} last year.</p>
<p class="stem">How much did the Swimcard {hl('save', 'b', 6)} the Teal family last year?</p>""",
    options={'A': '£50', 'B': '£190', 'C': '£230', 'D': '£250', 'E': '£270'},
    notes=[(1, 'g', 'Normal prices, per person, per visit.'),
           (2, 'y', 'The card covers 5 people. The Teals are 6!'),
           (3, 'p', 'Child number 4 still pays, but only half of £1 = <b>50p</b> a visit.'),
           (4, 'g', '2 adults + 4 children = 6 swimmers.'),
           (5, 'g', 'Everything per visit gets × 40.'),
           (6, 'b', 'Saving = cost without the card − cost with the card.')],
    steps=[
        f"""<p>Cost with <b>no card</b>, one family visit:</p>
{calc('2 adults × £2 = £4', '4 children × £1 = £4', f'£8 a visit {ar()} 40 × £8 = <b>£320</b>')}""",
        f"""<p>Cost <b>with the card</b>: £50 covers 2 adults + 3 children. The 4th child pays half price every time.</p>
{calc(f'half of £1 = 50p {ar()} 40 × 50p = £20', 'card + extra child = £50 + £20 = <b>£70</b>')}""",
        f"""{_swim()}
{calc(f'saving = £320 − £70 = {boxed("£250")}')}
{note('Do not stop at “the card costs £50”. A saving question always compares two full totals.', 'trap')}""",
    ],
    answer_text='£250: £320 without the card against £70 with it.',
    why={'A': '£50 is just the price of the card, not what it saves.',
         'B': '£190 would mean the card plus extras cost £130. That happens if you charge the 4th child the adult £2 rate (50 + 80).',
         'C': '£230 charges the 4th child the full £1 each visit (50 + 40 = 90). The extra child pays <b>half</b> the children’s rate.',
         'E': '£270 forgets the 4th child completely (320 − 50). The card only covers 3 children.'},
    fast='No card: £8 × 40 = £320. Card: £50 + 40 × 50p = £70. Save £250.',
))

# ---------------------------------------------------------------- 2 (Q6)
def _dividends():
    X = lambda m: 112 + m * 6.7
    parts, lab = [], []
    rows = (('Acme 6', 6, 64, 'pen'), ('Better 8', 8, 102, 'orange'), ('Koffmore 18', 18, 140, 'violet'))
    for name, step, y, col in rows:
        parts.append(line(X(0), y, X(74), y, k='muted', w=1.2))
        lab.append(text(100, y + 5, name, k=col, size=16, anchor='end'))
        for m in range(0, 73, step):
            parts.append(circle(X(m), y, 6, k=col, fill='g' if m in (0, 72) else 'paper', sw=2))
    parts.append(line(X(0), 176, X(74), 176, k='ink', w=2))
    for m, lbl in ((0, 'Jan 90'), (12, 'Jan 91'), (24, 'Jan 92'), (36, 'Jan 93'), (48, 'Jan 94'), (60, 'Jan 95'), (72, 'Jan 96')):
        parts.append(line(X(m), 170, X(m), 182, k='ink', w=1.6))
        lab.append(text(X(m), 200, lbl, k='muted', size=14))
    parts.append(line(X(24), 44, X(24), 160, k='orange', w=2, dash=True))
    parts.append(line(X(72), 44, X(72), 160, k='green', w=2.6))
    lab += [text(X(24), 36, 'Acme + Better only', k='orange', size=15),
            text(X(72), 36, 'all three!', k='green', size=18, font='scrawl'),
            text(X(36), 226, 'months after Jan 1990 (each dot = a payment)', k='ink', size=15)]
    return svg(640, 238, rough(*parts) + ''.join(lab),
               'Payment dots every 6, 8 and 18 months from January 1990; all three line up for the first time at 72 months, January 1996')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Calendars & cycles',
    question=f"""<p>Acme Haulage pays dividends to its shareholders {hl('every six months', 'g', 1)}. Better Ball Bearings
pays its shareholders {hl('every eight months', 'g', 1)} and Koffmore Chemists pays {hl('every eighteen months', 'g', 1)}.</p>
<p>In {hl('January 1990', 'y', 2)} all three companies paid me a dividend.</p>
<p class="stem">In what month and year did this {hl('next', 'b', 3)} happen?</p>""",
    options={'A': 'July 1991', 'B': 'January 1992', 'C': 'July 1995', 'D': 'January 1996', 'E': 'January 2002'},
    notes=[(1, 'g', 'Three repeating cycles: 6, 8 and 18 months.'),
           (2, 'y', 'Month 0. Count months from here.'),
           (3, 'b', 'The <b>first</b> month after this that is in all three cycles: the lowest common multiple.')],
    steps=[
        f"""<p>We need the first number of months that is a multiple of 6, 8 <b>and</b> 18.
Quickest: go up in 18s (the biggest) and test each one.</p>
{calc('18 ÷ 8 ' + cross(), '36 ÷ 8 = 4.5 ' + cross(), '54 ÷ 8 ' + cross(), f'72 ÷ 8 = 9 {tick()} and 72 ÷ 6 = 12 {tick()}')}""",
        f"""{_dividends()}
{calc(f'72 months = 6 years {ar()} January 1990 + 6 years = {boxed("January 1996")}')}
{note('Every multiple of 18 is already a multiple of 6, so really you only need “a multiple of 18 that 8 divides into”.', 'tip')}""",
    ],
    answer_text='January 1996: 72 months is the first time all three cycles line up.',
    why={'A': 'July 1991 is 18 months on. Acme and Koffmore pay then, but 18 isn’t a multiple of 8.',
         'B': 'January 1992 is 24 months: Acme and Better line up, but 24 isn’t a multiple of 18.',
         'C': 'July 1995 is 66 months: 66 isn’t a multiple of 8 or of 18.',
         'E': 'January 2002 is 144 months = 8 × 18 multiplied straight out. All three do pay then, but it is the <b>second</b> time; 72 comes first.'},
    fast='Count in 18s: 18, 36, 54, 72. The first one 8 divides into is 72 months = 6 years, so January 1996.',
))

# ---------------------------------------------------------------- 3 (Q7)
SEG = {'a': ((12, 8), (48, 8)), 'b': ((54, 14), (54, 46)), 'c': ((54, 56), (54, 88)),
       'd': ((12, 94), (48, 94)), 'e': ((6, 56), (6, 88)), 'f': ((6, 14), (6, 46)), 'g': ((12, 51), (48, 51))}


def _digit(x, y, lit, extra=''):
    p = []
    for s, ((x1, y1), (x2, y2)) in SEG.items():
        if s in lit:
            p.append(line(x + x1, y + y1, x + x2, y + y2, k='ink', w=7))
        elif s in extra:
            p.append(line(x + x1, y + y1, x + x2, y + y2, k='orange', w=7))
        else:
            p.append(line(x + x1, y + y1, x + x2, y + y2, k='muted', w=1.5, dash=True))
    return p


def _clock_digits():
    parts, lab = [], []
    seen = ['ab', 'abc', 'adg', 'c']
    full = ['abcdef', 'abcdfg', 'acdfg', 'abcdfg']
    for panel, x0 in ((0, 22), (1, 352)):
        xs = [x0, x0 + 66, x0 + 152, x0 + 218]
        for i, x in enumerate(xs):
            if panel == 0:
                parts += _digit(x, 46, seen[i])
            else:
                parts += _digit(x, 46, seen[i], full[i])
                lab.append(text(x + 30, 172, '0959'[i], k='green', size=22, font='scrawl'))
        parts += [circle(x0 + 139, 82, 4, k='ink', fill='ink'), circle(x0 + 139, 112, 4, k='ink', fill='ink')]
    lab += [text(155, 28, 'what she sees', k='ink', size=19, font='scrawl'),
            text(485, 28, 'latest time it can be', k='ink', size=19, font='scrawl'),
            text(155, 172, 'dashed bars: lit or not? unknown', k='muted', size=14),
            text(320, 210, 'orange = bars that failed to show.  09:59 − 07:00 = 2 h 59 min late', k='red', size=17)]
    return svg(640, 224, rough(*parts) + ''.join(lab),
               'The four faint digits next to the latest time they can show, 09:59, with the missing bars filled in orange')

Q.append(dict(
    n=3, orig=7, answer='E', topic='Digital displays',
    question=f"""<p>A woman has to get up for work at {hl("seven o'clock in the morning", 'g', 1)}. She wakes up and looks
over at her digital clock. Unfortunately, the batteries are low and the figures on the
display, showing hours and minutes, {hl("aren't showing up properly", 'p', 2)}. All she can see is the
display below:</p>
{fig(Y, 'ps_q03_display', 'Digital clock with faint digits: first digit shows only the top and top-right bars; second the top and both right bars; after the colon the third shows top, middle and bottom bars; the fourth only the bottom-right bar', 300)}
<p>It is light outside, so she {hl('cannot be more than twelve hours late', 'y', 3)}.</p>
<p class="stem">What is the {hl('greatest', 'b', 4)} amount of time that she could be late waking up?</p>""",
    options={'A': '1h 39min', 'B': '1h 59min', 'C': '2h 25min', 'D': '2h 35min', 'E': '2h 59min'},
    notes=[(1, 'g', 'She should be up at 07:00, so lateness = time shown − 07:00.'),
           (2, 'p', 'Some bars are missing. Every bar you <b>can</b> see is really lit; more bars may be lit too.'),
           (3, 'y', 'So the time is between 07:00 and 19:00.'),
           (4, 'b', 'Make each digit as big as it is allowed to be.')],
    steps=[
        f"""<p>For each digit, list the numbers that contain <b>all</b> the bars you can see:</p>
{table([['1st (tens of hours)', 'top, top-right', '0, 2, 3, 7, 8, 9', '0 or 2'],
        ['2nd (hours)', 'top, both right', '0, 3, 7, 8, 9', 'any of these'],
        ['3rd (tens of minutes)', 'top, middle, bottom', '2, 3, 5, 6, 8, 9', 'only 2, 3, 5 (it must be 5 or less)'],
        ['4th (minutes)', 'bottom-right', 'everything except 2', '0, 1, 3, 4, 5, 6, 7, 8, 9']],
       head=['Digit', 'Bars you see', 'Numbers with those bars', 'Allowed in a time'])}""",
        f"""<p>Now the time must be from 07:00 to 19:00:</p>
<ul><li>1st digit 2 gives 20:xx or 23:xx: more than 12 hours late {cross()}</li>
<li>1st digit 1 is impossible: a “1” has no top bar.</li>
<li>So it is 0 then 7, 8 or 9. Biggest: <b>09</b>.</li>
<li>Minutes as big as possible: tens <b>5</b>, units <b>9</b>.</li></ul>""",
        f"""{_clock_digits()}
{calc(f'latest time 09:59 {ar()} 09:59 − 07:00 = {boxed("2h 59min")}')}
{note('The third digit looks like a 3, and that is the trap. A 5 also has a top, middle and bottom bar.', 'trap')}""",
    ],
    answer_text='2h 59min: the display could be showing 09:59.',
    why={'A': '1h 39min means 08:39. That misses that the 2nd digit can be a 9 and the 3rd a 5.',
         'B': '1h 59min means 08:59. A 9 also has the top and both right bars, so 09 is possible.',
         'C': '2h 25min means 09:25: reads the 3rd digit as a 2 only, when 3 and 5 fit too.',
         'D': '2h 35min means 09:35: reads the 3rd digit as the 3 it looks like. A 5 has the same three bars, and the last digit could be 9.'},
    fast='Biggest digit that contains the visible bars, within 07:00 to 19:00: 0, 9, 5, 9. So 09:59, which is 2h 59min late.',
))

# ---------------------------------------------------------------- 4 (Q8)
def _richter():
    parts = [circle(70, 112, 14, k='ink', fill='y'), circle(230, 112, 34, k='ink', fill='o'), circle(470, 112, 78, k='ink', fill='p'),
             arrow(92, 82, 192, 76, k='pen', bend=-0.25), arrow(272, 66, 398, 52, k='pen', bend=-0.2),
             arrow(70, 214, 462, 214, k='red', bend=0.05, w=2.6)]
    lab = [text(70, 156, 'X 2.0', k='ink', size=18), text(230, 172, 'Y 3.0', k='ink', size=18), text(470, 118, 'Z 4.0', k='ink', size=22),
           text(140, 50, '× 10', k='pen', size=20, font='scrawl'), text(330, 30, '× 10', k='pen', size=20, font='scrawl'),
           text(270, 250, 'X to Z: × 10 × 10 = × 100 (not × 20!)', k='red', size=19, font='scrawl')]
    return svg(600, 262, rough(*parts) + ''.join(lab), 'X, Y and Z as growing circles: each step up is times 10, so Z is 100 times X')

Q.append(dict(
    n=4, orig=8, answer='B', topic='Scales & multipliers',
    question=f"""<p>The Richter Scale is used to measure the strength of earthquakes. It has the property that
{hl('an increase of one unit on the scale represents a tenfold increase in the strength', 'y', 1)} of the
quake. Three earthquakes have the following values on the Richter Scale:</p>
<p style="text-align:center">{hl('X : 2.0', 'g', 2)}<br>{hl('Y : 3.0', 'g', 2)}<br>{hl('Z : 4.0', 'g', 2)}</p>
<p class="stem">Which one of the following statements about their {hl('relative strengths', 'b', 3)} is true?</p>""",
    options={'A': 'X is one-tenth the strength of Y and one-twentieth the strength of Z.',
             'B': 'X is one-tenth the strength of Y and one-hundredth the strength of Z.',
             'C': 'X is one-tenth the strength of Y and one-thousandth the strength of Z.',
             'D': 'Z is twice as strong as X and Y is one-and-a-half times as strong as X.',
             'E': 'Z is one-tenth stronger than Y which is one-tenth stronger than X.'},
    notes=[(1, 'y', 'Each +1 on the scale = <b>× 10</b> in strength. Steps multiply, they don’t add.'),
           (2, 'g', 'X to Y is 1 step. X to Z is 2 steps.'),
           (3, 'b', 'Compare X with Y, and X with Z.')],
    steps=[
        f"""<p>Count the steps and multiply by 10 for each one:</p>
{calc(f'X → Y: 2.0 → 3.0 = 1 step {ar()} Y = 10 × X', f'X → Z: 2.0 → 4.0 = 2 steps {ar()} Z = 10 × 10 × X = 100 × X')}""",
        f"""{_richter()}
{calc(f'X is {frac(1, 10)} of Y and {frac(1, 100)} of Z {ar()} {boxed("B")}')}""",
    ],
    answer_text='B: one step = × 10, two steps = × 100.',
    why={'A': 'One-twentieth <b>adds</b> the two tenfold jumps (10 + 10). Jumps multiply: 10 × 10 = 100.',
         'C': 'One-thousandth would be 3 steps (10 × 10 × 10). Z is only 2 steps above X.',
         'D': 'Treats the scale like ordinary numbers (4 is twice 2). Here each unit is a × 10 jump.',
         'E': '“One-tenth stronger” means only 10% more. Each step is ten <b>times</b> as strong.'},
    fast='1 step = × 10, 2 steps = × 100. So X is 1/10 of Y and 1/100 of Z.',
))

# ---------------------------------------------------------------- 5 (Q12)
def _sale():
    X = lambda v: 112 + v * 4.8
    parts = [rect(X(0), 40, X(64.32) - X(0), 36, k='ink', fill='b', sw=1.8), rect(X(64.32), 40, X(96) - X(64.32), 36, k='ink', fill='paper', sw=1.8),
             rect(X(0), 104, X(51) - X(0), 36, k='ink', fill='b', sw=1.8), rect(X(51), 104, X(102) - X(51), 36, k='ink', fill='paper', sw=1.8),
             line(X(51), 30, X(51), 150, k='red', w=2, dash=True), line(X(64.32), 30, X(64.32), 150, k='red', w=2, dash=True)]
    lab = [text(100, 64, '£96', k='ink', size=18, anchor='end'), text(100, 128, '£102', k='ink', size=18, anchor='end'),
           text((X(0) + X(64.32)) / 2, 64, 'pay £64.32', k='ink', size=16), text((X(64.32) + X(96)) / 2, 64, '33% off', k='muted', size=15),
           text((X(0) + X(51)) / 2, 128, 'pay £51', k='ink', size=16), text((X(51) + X(102)) / 2, 128, '50% off', k='muted', size=15),
           text(X(57.66), 22, '£13.32 less', k='red', size=18, font='scrawl')]
    return svg(640, 160, rough(*parts) + ''.join(lab),
               'Two bars: £96 marked, pay £64.32 after 33% off; £102 marked, pay £51 after 50% off; the gap is £13.32')

Q.append(dict(
    n=5, orig=12, answer='D', topic='Percentages & discounts',
    question=f"""<p>Sue and Ben are buying some kitchen goods at a shop which is having a sale. The terms
of the sale are as follows:</p>
{table([['Up to £50', '25'], [hl('Up to £100', 'y', 1), hl('33', 'y')], [hl('£100 or more', 'y', 2), hl('50', 'y')]],
       head=['Total marked price of purchases (before discount)', 'Reduction (%)'])}
<p>The marked prices of the goods they have chosen come to {hl('£96', 'g', 3)}.</p>
<p class="stem">How much {hl('less would they actually spend', 'b', 4)}, {hl('to the nearest £1', 'y', 5)}, if they chose {hl('extra goods to the value of £6', 'p', 6)}?</p>""",
    options={'A': '£2', 'B': '£6', 'C': '£10', 'D': '£13', 'E': '£16'},
    notes=[(1, 'y', '£96 sits in this band: 33% off.'),
           (2, 'y', 'Push the total to £100 or more and <b>everything</b> is half price.'),
           (3, 'g', 'The starting basket.'),
           (4, 'b', 'Compare what they pay: before vs after adding the extras.'),
           (5, 'y', 'Round only at the very end.'),
           (6, 'p', '£96 + £6 = £102. The extras get the 50% off too, so they only cost £3.')],
    steps=[
        f"""<p><b>Now</b>: £96 is “up to £100”, so 33% off. They pay 67%:</p>
{calc('96 × 0.67 = 67 − 4 × 0.67 = 67 − 2.68 = <b>£64.32</b>')}
{note('96 × 0.67: do 100 × 0.67 = 67, then take off 4 × 0.67 = 2.68.', 'tip')}""",
        f"""<p><b>With the extras</b>: £96 + £6 = £102, which is “£100 or more”, so half price:</p>
{calc('102 ÷ 2 = <b>£51</b>')}""",
        f"""{_sale()}
{calc(f'£64.32 − £51 = £13.32 {ar()} to the nearest £1 = {boxed("£13")}')}""",
    ],
    answer_text='£13 less: £64.32 for £96 of goods against £51 for £102 of goods.',
    why={'A': '£2 is how far £102 goes over the £100 line, not money saved.',
         'B': '£6 is the value of the extra goods, not a saving.',
         'C': '£10 takes the extra discount on the £96 (£16.32) and then knocks off the full £6 for the extras. But the extras are half price too, so they only add £3.',
         'E': '£16 is the extra discount on the original £96, forgetting they now pay £3 for the extra goods.'},
    fast='Before: 96 × 0.67 ≈ £64.32. After: 102 ÷ 2 = £51. Difference ≈ £13.',
))

# ---------------------------------------------------------------- 6 (Q13)
def _bills():
    s, base = 1.08, 262
    parts, lab = [], []

    def stack(x, segs, title, lx):
        y = base
        for v, f, name in segs:
            h = v * s
            parts.append(rect(x, y - h, 100, h, k='ink', fill=f, sw=1.6))
            lab.append(text(lx, y - h / 2 + 6, name, k='ink', size=15, anchor='start'))
            y -= h
        lab.append(text(x + 50, y - 12, title, k='pen', size=19, font='scrawl'))

    stack(60, [(168, 'b', 'standard 168'), (10, 'o', ''), (18, 'g', '')], 'old bill £196', 168)
    lab.append(text(168, base - 168 * s - 2, 'off-peak 10', k='ink', size=15, anchor='start'))
    lab.append(text(168, base - 178 * s - 14, 'fixed 18', k='ink', size=15, anchor='start'))
    stack(380, [(84, 'b', 'standard ÷ 2 ≈ 84'), (100, 'o', 'off-peak × 10 ≈ 100'), (18, 'g', 'fixed 18 (same)')], 'new ≈ £202', 488)
    parts.append(line(40, base, 620, base, k='ink', w=2))
    return svg(640, 280, rough(*parts) + ''.join(lab),
               'Stacked bars: old bill standard 168, off-peak 10, fixed 18; new bill standard 84, off-peak 100, fixed 18, about 202')

Q.append(dict(
    n=6, orig=13, answer='E', topic='Bills & estimation',
    question=f"""<p style="text-align:center"><i>QUARTERLY ELECTRICITY BILL</i></p>
{table([['45856', '47846', '1990', 'standard', '8.45', hl('168.15', 'g', 1)],
        ['', '', '', hl('FIXED CHARGES', 'p', 2), '', '12.30'],
        ['65026', '65284', '258', 'Off-peak', '3.90', hl('10.06', 'g', 1)],
        ['', '', '', hl('FIXED CHARGES', 'p'), '', '5.45'],
        ['', '', '', 'TOTAL AMOUNT DUE', '', '195.96']],
       head=['Meter reading: Previous', 'Meter reading: Present', 'Units Charged', 'Tariff', 'Pence per unit', 'Amount (£)'])}
<p>At the end of the quarterly charging period to which the above bill relates, the
householder changed her electricity consumption pattern. In the next quarter she {hl('roughly halved her standard consumption', 'y', 3)} and {hl('increased her off-peak consumption by about ten times', 'y', 3)}.</p>
<p class="stem">What {hl('approximate', 'b', 4)} total bill should she expect for the next charging period?</p>""",
    options={'A': '£90', 'B': '£120', 'C': '£150', 'D': '£170', 'E': '£200'},
    notes=[(1, 'g', 'The two parts that change: standard £168 and off-peak £10.'),
           (2, 'p', 'Fixed charges don’t depend on use, so they stay the same: 12.30 + 5.45 ≈ £18.'),
           (3, 'y', 'Halve the standard cost, multiply the off-peak cost by 10.'),
           (4, 'b', 'Round freely: options are £30 apart.')],
    steps=[
        f"""<p>Split the old bill into its parts (rounded):</p>
{calc('standard ≈ £168', 'off-peak ≈ £10', 'fixed ≈ 12 + 5.5 ≈ £18')}""",
        f"""<p>Apply the changes. Only the parts that depend on use change:</p>
{calc(f'standard: 168 ÷ 2 = <b>£84</b>', f'off-peak: 10 × 10 = <b>£100</b>', 'fixed: still <b>£18</b>')}
{_bills()}""",
        f"""{calc(f'84 + 100 + 18 = £202 {ar()} about {boxed("£200")}')}
{note('Same cost per unit, so the cost of each part changes exactly like its units: half the units = half the cost.', 'tip')}""",
    ],
    answer_text='About £200: £84 standard + £100 off-peak + £18 fixed.',
    why={'A': '£90 halves the standard part (84) and adds the old off-peak £10, forgetting both the ten-fold rise and the fixed charges.',
         'B': '£120 halves the standard part but leaves off-peak at £10 (84 + 10 + 18 = 112). The off-peak must go up ten times.',
         'C': '£150 would need the off-peak part to be only about £50: that is × 5, not × 10.',
         'D': '£170 is nearer to 84 + 100 = 184 than £200 is, so it comes from forgetting the £18 of fixed charges.'},
    fast='168 ÷ 2 ≈ 84, 10 × 10 = 100, fixed ≈ 18. Total ≈ 202, so £200.',
))

# ---------------------------------------------------------------- 7 (Q14)
def _star(cx, cy, R=118, r=25):
    tips = [(cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy)]
    inner = [(cx + r, cy - r), (cx + r, cy + r), (cx - r, cy + r), (cx - r, cy - r)]
    return tips, inner


def _window():
    parts, lab = [], []
    cx, cy = 150, 150
    tips, inner = _star(cx, cy)
    k = 0
    for i in range(4):
        t, a, b = tips[i], inner[i - 1], inner[i]
        for j, (p, q) in enumerate(((a, t), (t, b))):
            f = 'o' if (i, j) == (2, 0) else ('b' if k % 2 == 0 else 'paper')
            parts.append(poly([(cx, cy), p, q], k='ink', fill=f, sw=1.8))
            k += 1
    lab.append(text(cx + 30, cy + 76, 'A', k='orange', size=22, font='print', weight='700'))
    lab.append(text(cx, 296, '8 identical slivers', k='green', size=19, font='scrawl'))
    cx2 = 470
    tips2, inner2 = _star(cx2, cy)
    for i in range(4):
        parts.append(poly([inner2[i - 1], tips2[i], inner2[i]], k='ink', fill='g', sw=1.8))
    parts.append(rect(cx2 - 25, cy - 25, 50, 50, k='red', fill='p', sw=2.2))
    lab += [text(cx2, cy + 6, 'hole', k='red', size=16, font='scrawl'),
            text(cx2 + 36, cy - 66, 'D', k='green', size=20, font='print', weight='700'),
            text(cx2, 296, 'D (or C) leaves a square hole', k='red', size=19, font='scrawl')]
    return svg(640, 310, rough(*parts) + ''.join(lab),
               'Left: the star cut into 8 identical thin triangles from the centre, one marked A. Right: four D triangles fill the points but leave a square hole in the middle')

Q.append(dict(
    n=7, orig=14, answer='A', topic='Shapes & tiling',
    question=f"""<p>The diagram shows the outline of a window which is intended to be composed of a
number of panes of glass, {hl('all of the same size and shape', 'y', 1)}.</p>
{fig(Y, 'ps_q07_window', 'A four-pointed star with long thin points', 200)}
<p class="stem">Which one of the shapes below {hl('could be used to fill this window', 'b', 2)}?</p>
{fig(Y, 'ps_q07_panes', 'Five shapes: A a thin triangle with one long straight side; B a long rhombus; C a thin right-angled triangle; D a tall isosceles triangle; E a tall pointed shape with a square-ish base', 420)}""",
    options={'A': 'shape A', 'B': 'shape B', 'C': 'shape C', 'D': 'shape D', 'E': 'shape E'},
    notes=[(1, 'y', 'Every pane identical. They may be turned or flipped over.'),
           (2, 'b', 'Fill the whole star exactly: no gaps, no overlaps.')],
    steps=[
        f"""<p>The star has a centre, 4 tips and 4 inner corners. Join the centre to all 8 corners.
It splits into <b>8 identical thin triangles</b> (each point cut in half down its middle):</p>
{_window()}""",
        f"""<p>Each sliver has a long side (centre to tip), a short side (centre to an inner corner) and a slanting side
along the outline. The orange one is <b>exactly</b> shape A {ar()} {boxed('A')}</p>
{note('Half of the slivers are mirror images of the others. Glass can be flipped over, so they are all the same pane.', 'check')}""",
        f"""<p>Why the others fail:</p>
<ul><li>D is a whole point cut off at the inner corners. Four of them leave a <b>square hole</b> in the middle.</li>
<li>C is half of D: same square hole, and thin right-angled triangles can’t fill a square.</li>
<li>B is two opposite points joined. One fits across the middle, but the other two points would overlap it.</li>
<li>E is a point plus half the centre square. Four of them would cover the middle square twice.</li></ul>""",
    ],
    answer_text='Shape A: 8 copies (some flipped) fill the star, centre to every corner.',
    why={'B': 'B covers two opposite points and the middle. A second B can’t cross it without overlapping.',
         'C': 'C is half a point. The points get filled, but the square in the middle can’t be made from these.',
         'D': 'D is a whole point. Four Ds leave the middle square empty.',
         'E': 'E is a point plus half the middle square. Four of them use up two middle squares, so they overlap.'},
    fast='Draw lines from the centre to every corner: 8 equal slivers, each like A.',
))

# ---------------------------------------------------------------- 8 (Q18)
def _lift():
    parts = [rect(30, 30, 330, 212, k='ink', fill='paper', sw=2.6), line(30, 242, 360, 242, k='ink', w=3)]
    lab = [stick_person(72, 240, k='pen', s=1.7), text(72, 136, 'me', k='pen', size=17), text(72, 156, '80 kg', k='pen', size=15)]
    for row, y in enumerate((200, 158)):
        for i in range(4):
            parts.append(rect(118 + 56 * i, y, 50, 40, k='ink', fill='o', sw=1.6))
            lab.append(text(143 + 56 * i, y + 26, '25', k='ink', size=15))
    for row, y in enumerate((122, 86)):
        for i in range(3):
            parts.append(rect(140 + 56 * i, y, 44, 34, k='ink', fill='b', sw=1.6))
            lab.append(text(162 + 56 * i, y + 23, '20', k='ink', size=14))
    lab += [text(195, 60, 'one full trip', k='muted', size=16, font='scrawl'),
            text(385, 64, '8 × 25 kg = 200 kg', k='ink', size=17, anchor='start'),
            text(385, 92, '6 × 20 kg = 120 kg', k='ink', size=17, anchor='start'),
            text(385, 120, 'me = 80 kg', k='ink', size=17, anchor='start'),
            text(385, 154, 'total = 400 kg, full!', k='green', size=20, font='scrawl', anchor='start'),
            text(385, 198, '15 trips × 8 = 120 big ✓', k='pen', size=17, anchor='start'),
            text(385, 224, '15 trips × 6 = 90 small ✓', k='pen', size=17, anchor='start')]
    return svg(640, 256, rough(*parts) + ''.join(lab),
               'One lift load: me at 80 kg, eight 25 kg boxes and six 20 kg boxes, exactly 400 kg; 15 such trips move every box')

Q.append(dict(
    n=8, orig=18, answer='D', topic='Capacity & loading',
    question=f"""<p>I have been asked to move {hl('120 boxes weighing 25kg each and 90 boxes weighing 20kg each', 'g', 1)} from the ground floor to the fifth floor of the office block in which I
work. {hl('Unfortunately, nobody is available to give me any help.', 'y', 2)}</p>
<p>There is a sign in the lift which reads:</p>
{table([['MAXIMUM LOAD'], [hl('4 persons', 'p', 3) + ' or ' + hl('400 kg', 'y', 4)]])}
<p>{hl('I weigh 80kg.', 'g', 5)}</p>
<p class="stem">What is the {hl('minimum', 'b', 6)} number of journeys I will have to make from the ground floor to the
fifth floor?</p>""",
    options={'A': '10', 'B': '12', 'C': '13', 'D': '15', 'E': '16'},
    notes=[(1, 'g', 'Total box weight: 120 × 25 + 90 × 20.'),
           (2, 'y', 'No helper, so I must ride up with every load.'),
           (3, 'p', 'Boxes are not persons. Only the weight limit matters.'),
           (4, 'y', 'The real limit: 400 kg including me.'),
           (5, 'g', 'Room left for boxes: 400 − 80 = 320 kg a trip.'),
           (6, 'b', 'Pack each trip as full as possible.')],
    steps=[
        f"""<p>Weight of all the boxes:</p>
{calc('120 × 25 = 3000 kg', '90 × 20 = 1800 kg', 'total = <b>4800 kg</b>')}""",
        f"""<p>I travel with every load, so each trip carries at most:</p>
{calc(f'400 − 80 = <b>320 kg</b> of boxes', f'4800 ÷ 320 = 15 {ar()} at least 15 trips')}""",
        f"""<p>Can every trip be <b>exactly</b> 320 kg? Share the boxes evenly over 15 trips:</p>
{calc('120 ÷ 15 = 8 big boxes, 90 ÷ 15 = 6 small boxes', '8 × 25 + 6 × 20 = 200 + 120 = 320 kg ' + tick())}
{_lift()}
{calc(f'minimum = {boxed("15")} journeys')}""",
    ],
    answer_text='15 journeys: 8 big + 6 small boxes + me = exactly 400 kg each time.',
    why={'A': '10 only moves the 25 kg boxes (3000 ÷ 320 → 10 trips) and forgets the 20 kg ones.',
         'B': '12 is 4800 ÷ 400: forgets that I am in the lift too, using 80 kg of every load.',
         'C': '13 would need about 370 kg of boxes per trip, but only 320 kg fits once I am in.',
         'E': '16 moves the two sizes on separate trips (10 + 6). Mixing them fills every trip exactly, so 15 is enough.'},
    fast='Boxes 4800 kg; room per trip 400 − 80 = 320 kg; 4800 ÷ 320 = 15, and 8 big + 6 small = 320 exactly.',
))
