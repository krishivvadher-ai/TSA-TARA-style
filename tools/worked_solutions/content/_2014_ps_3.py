import math
from wslib import *
from _2014_ps_2 import _pie

Y = 2014
Q = []

# ---------------------------------------------------------------- 18 (Q37)
def _squash():
    rows = [('Bronze 1 yr + 12 lockers', 32, 'p'), ('Silver 1 yr (free locker)', 28, 'g'), ('Silver 6 m, twice', 36, 'p'),
            ('Gold 1 yr', 52, 'p'), ('Gold 6 m, twice', 64, 'p')]
    X = lambda v: 250 + v * 5
    parts, lab = [], []
    for i, (name, v, f) in enumerate(rows):
        y = 34 + i * 36
        parts.append(rect(X(0), y, X(v) - X(0), 24, k='ink', fill=f, sw=1.6))
        lab.append(text(240, y + 18, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(v) + 8, y + 18, f'£{v}', k='green' if f == 'g' else 'ink', size=17, anchor='start'))
    lab.append(text(X(28) + 60, 34 + 36 + 18, '← cheapest', k='green', size=18, font='scrawl', anchor='start'))
    lab.append(text(250, 22, 'a full year from now (renewal prices)', k='muted', size=15, anchor='start'))
    return svg(640, 222, rough(*parts) + ''.join(lab), 'Cost of a year: Bronze plus lockers 32, Silver one year 28, Silver six months twice 36, Gold 52 or 64')

Q.append(dict(
    n=18, orig=37, answer='C', topic='Tables & best deal', attempt='',
    question=f"""<p>My current membership of the squash club is about to expire and so I wish to renew it. The
options available to me are given in the table below and have not changed since {hl('I joined as a new member six months ago', 'p', 1)} ({hl('a change in membership type counts as a renewal', 'y', 2)}, not a new
member).</p>
{table([['Bronze', '1 year', 'none', '10', '8'],
        ['Silver', '6 months', 'free locker', '25', '18'],
        ['Silver', '1 year', 'free locker', '45', hl('28', 'g')],
        ['Gold', hl('6 months', 'p'), 'free locker, free competition entry', hl('40', 'p'), '32'],
        ['Gold', '1 year', 'free locker, free competition entry', '75', '52']],
       head=['Membership type', 'Length', 'Extras', 'New member (£)', 'Renewal price (£)'])}
<p>I am currently a Gold member, but I do not want to enter competitions any more as I {hl('play only once a month', 'g', 3)}. I do need a locker when I visit and the {hl('normal cost to hire a locker is £2 per visit', 'g', 4)}. I
want to choose a membership that will give me the {hl('smallest possible total cost for a full year', 'b', 5)}.</p>
<p class="stem">What will be the difference between the amount that I will pay now and the amount I paid six
months ago?</p>""",
    options={'A': 'I will pay £32 less.', 'B': 'I will pay £30 less.', 'C': 'I will pay £12 less.',
             'D': 'I will pay £8 less.', 'E': 'I will pay £5 more.'},
    notes=[(1, 'p', 'Six months ago they joined Gold, as a <b>new</b> member, for 6 months: that cost <b>£40</b>.'),
           (2, 'y', 'Switching type still uses the cheaper renewal prices.'),
           (3, 'g', 'Once a month = 12 visits a year.'),
           (4, 'g', 'Without a free locker: 12 × £2 = £24 extra a year.'),
           (5, 'b', 'Cover a whole year as cheaply as possible.')],
    steps=[
        f"""<p>What did they pay six months ago? They joined as a new member and the membership is ending now,
so it was a 6-month Gold, new member: <b>£40</b>.</p>""",
        f"""<p>Now find the cheapest full year (renewal prices, locker every visit):</p>{_squash()}
{calc('Bronze: 8 + 12 × 2 = 8 + 24 = £32', 'Silver 1 year: £28, locker free', 'Silver 6 months twice: 18 + 18 = £36', 'Gold: £52 (or 32 + 32 = £64)')}""",
        f"""{calc(f'£40 then, £28 now {ar()} 40 − 28 = {boxed("£12 less")}')}""",
    ],
    answer_text='£12 less: £28 (Silver, 1 year) now against £40 (Gold, 6 months, new) then.',
    why={'A': '£32 less is 40 − 8: Bronze without paying for any lockers.',
         'B': '£30 less doesn’t come from any sensible plan.',
         'D': '£8 less is 40 − 32: Bronze with lockers (£32), which isn’t the cheapest. Or a Gold 6-month renewal.',
         'E': '£5 more is 45 − 40: paying the Silver 1-year <b>new member</b> price. A change of type is a renewal.'},
    fast='Then: Gold 6 months new = £40. Now: Silver 1 year renewal £28 (Bronze + 12 lockers = £32 is dearer). Difference £12.',
))

# ---------------------------------------------------------------- 19 (Q38)
def _ratios():
    rows = [('Swimming', 104, 150), ('Football', 120, 181), ('Cricket', 120, 133), ('Hockey', 55, 66), ('Tennis', 123, 149), ('Squash', 51, 97)]
    X = lambda v: 120 + v * 380
    parts, lab = [], []
    for i, (name, a, b) in enumerate(rows):
        y = 30 + i * 34
        r = a / b
        f = 'y' if name == 'Swimming' else 'g' if name == 'Football' else 'paper'
        parts.append(rect(X(0), y, X(r) - X(0), 22, k='ink', fill=f, sw=1.6))
        lab.append(text(110, y + 17, name, k='ink', size=16, anchor='end'))
        lab.append(text(X(r) + 8, y + 17, f'{a} ÷ {b} ≈ {r:.2f}', k='ink', size=15, anchor='start'))
    sw = 104 / 150
    parts.append(line(X(sw), 20, X(sw), 236, k='orange', w=2.2, dash=True))
    lab.append(text(X(sw), 254, 'swimming ≈ 0.69', k='orange', size=17, font='scrawl'))
    return svg(640, 264, rough(*parts) + ''.join(lab), 'Ratio of 11-year-olds to 16-year-olds for each sport; football at 0.66 is closest to swimming at 0.69')

Q.append(dict(
    n=19, orig=38, answer='A', topic='Ratio & proportion', attempt='',
    question=f"""<p>The table shows the number of children in the town of Lancester aged 11 and 16 who play
various sports after school.</p>
{table([['Football', '120', '181'], ['Cricket', '120', '133'], ['Hockey', '55', '66'], [hl('Swimming', 'g'), hl('104', 'g'), hl('150', 'g')],
        ['Tennis', '123', '149'], ['Squash', '51', '97']], head=['Sport', '11-year-olds', '16-year-olds'])}
<p class="stem">In which sport was the {hl('proportion of 11-year-old to 16-year-old children', 'y', 1)} {hl('nearest to that for swimming', 'b', 2)}?</p>""",
    options={'A': 'Football', 'B': 'Cricket', 'C': 'Hockey', 'D': 'Tennis', 'E': 'Squash'},
    notes=[(1, 'y', 'For each sport: 11-year-olds ÷ 16-year-olds.'),
           (2, 'b', 'Find swimming’s value, then the closest one to it.')],
    steps=[
        f"""<p>Swimming first: {frac(104, 150)} is a bit more than {frac(100, 150)} = {frac(2, 3)}, so about <b>0.69</b>.</p>""",
        f"""<p>Now estimate the others. Is the top number about two-thirds of the bottom?</p>
{calc('Football: ⅔ of 181 ≈ 121, and the top is 120 ✓ about ⅔ (0.66)', 'Cricket: 120 is nearly all of 133 (0.90)',
      'Hockey: 55 ÷ 66 = ⅚ (0.83)', 'Tennis: 123 is most of 149 (0.83)', 'Squash: 51 is about half of 97 (0.53)')}
{_ratios()}
{calc(f'closest to 0.69 is football (0.66) {ar()} {boxed("A")}')}""",
    ],
    answer_text='Football: 120/181 ≈ 0.66, closest to swimming’s 104/150 ≈ 0.69.',
    why={'B': 'Cricket is about 0.90, far above 0.69.',
         'C': 'Hockey is 55/66 = 0.83.',
         'D': 'Tennis is about 0.83.',
         'E': 'Squash is about 0.53, too low.'},
    fast='Swimming ≈ ⅔. Which top number is about ⅔ of its bottom number? Football: 120 against 181.',
))

# ---------------------------------------------------------------- 20 (Q42)
def _windows():
    years = [(1905, '13.4'), (1906, '14.4'), (1907, '13.4'), (1908, '13.7'), (1909, 'x'), (1910, '13.3'), (1911, '14.9')]
    parts, lab = [], []
    for i, (yr, v) in enumerate(years):
        x = 40 + i * 78
        f = 'y' if i in (2, 3, 4) else 'paper'
        parts.append(rect(x, 70, 70, 40, k='ink', fill=f, sw=1.6))
        lab.append(text(x + 35, 60, yr, k='muted', size=15))
        lab.append(text(x + 35, 97, v, k='ink', size=18))
    parts.append(brace(40, 40 + 5 * 78 - 8, 120, 'y = average of 1905–1909', k='pen'))
    parts.append(path(f'M{40 + 2 * 78} 50 q0 -12 10 -12 L{40 + 7 * 78 - 18} 38 q10 0 10 12', k='orange', sw=2))
    lab.append(text(40 + 4.5 * 78, 28, '13.66 = average of 1907–1911', k='orange', size=17))
    return svg(600, 170, rough(*parts) + ''.join(lab), 'Two five-year windows: 1905 to 1909 for y and 1907 to 1911 for 13.66; they share 1907, 1908 and 1909')

Q.append(dict(
    n=20, orig=42, answer='C', topic='Averages', attempt='',
    question=f"""<p>The table below shows the mean maximum daily temperature for Oxford for each year from
1905 to 1920 along with a moving 5-year average ({hl('the value shown beside 1920 is the average from 1916 to 1920 inclusive', 'y', 1)}). Three values are missing from the table.</p>
{table([['1905', '13.4', '13.40'], ['1906', '14.4', '13.56'], ['1907', '13.4', '13.60'], ['1908', '13.7', '13.66'],
        ['1909', hl('x', 'p', 3), hl('y', 'b', 2)], ['1910', '13.3', 'z'], ['1911', '14.9', hl('13.66', 'g', 4)], ['1912', '13.7', '13.72'],
        ['1913', '14.2', '13.82'], ['1914', '14.7', '14.16'], ['1915', '13.6', '14.22'], ['1916', '13.3', '13.90'],
        ['1917', '12.8', '13.72'], ['1918', '13.8', '13.64'], ['1919', '13.0', '13.30'], ['1920', '13.8', '13.34']],
       head=['Year', 'Mean maximum daily temperature', '5-year moving average'])}
<p class="stem">What value should be in the position marked 'y'?</p>""",
    options={'A': '13.30', 'B': '13.64', 'C': '13.58', 'D': '13.66', 'E': '13.72'},
    notes=[(1, 'y', 'Each average = that year + the 4 years before it.'),
           (2, 'b', 'y sits beside 1909, so y = average of 1905 to 1909.'),
           (3, 'p', 'But 1909’s own temperature (x) is missing too: find x first.'),
           (4, 'g', 'A later average that includes x and lets you find it.')],
    steps=[
        f"""<p>Find x using an average that includes 1909. The 1911 average covers 1907–1911:</p>{_windows()}
{calc('5 × 13.66 = 68.3 (the five temperatures add to 68.3)', '13.4 + 13.7 + 13.3 + 14.9 = 55.3', 'x = 68.3 − 55.3 = <b>13.0</b>')}""",
        f"""<p>Now y, the average of 1905–1909:</p>
{calc('13.4 + 14.4 + 13.4 + 13.7 + 13.0 = 67.9', f'67.9 ÷ 5 = {boxed("13.58")}')}
{note('Shortcut: the two windows share 1907–09, so y = 13.66 + (1905 + 1906 − 1910 − 1911) ÷ 5 = 13.66 + (27.8 − 28.2) ÷ 5 = 13.66 − 0.08 = 13.58.', 'tip')}""",
    ],
    answer_text='13.58.',
    why={'A': '13.30 is copied from 1919’s average.',
         'B': '13.64 is copied from 1918’s average.',
         'D': '13.66 is the 1908 (and 1911) average, a neighbour, not y.',
         'E': '13.72 is copied from 1912’s average.'},
    fast='x from the 1911 window: 68.3 − 55.3 = 13.0. Then y = (13.4 + 14.4 + 13.4 + 13.7 + 13.0) ÷ 5 = 13.58.',
))

# ---------------------------------------------------------------- 21 (Q43)
def _fish():
    rows = [('Dark Y1', 77, 5), ('Dark Y2', 125, 30), ('Fare Y1', 85, 20), ('Fare Y2', 35, 8), ('Gwynt Y1', 71, 19),
            ('Gwynt Y2', 132, 2), ('Tine Y1', 105, 43), ('Tine Y2', 66, 19), ('Yarrow Y1', 80, 18), ('Yarrow Y2', 150, 25)]
    parts, lab = [], []
    for i, (name, s, a) in enumerate(rows):
        v = s / a
        x = 40 + i * 58
        h = v * 3
        parts.append(rect(x, 230 - h, 40, h, k='ink', fill='g' if name == 'Gwynt Y2' else 'b', sw=1.5))
        lab.append(text(x + 20, 224 - h, f'{v:.0f}' if v >= 10 else f'{v:.1f}', k='ink', size=15))
        lab.append(text(x + 20, 248, name.split()[0], k='ink', size=13))
        lab.append(text(x + 20, 264, name.split()[1], k='muted', size=13))
    parts.append(line(30, 230, 630, 230, k='ink', w=2))
    lab.append(text(390, 50, '132 sets ÷ 2 anglers = 66 each!', k='green', size=19, font='scrawl', anchor='start'))
    return svg(640, 276, rough(*parts) + ''.join(lab), 'Average fish per angler for each river and year; Gwynt year 2 is 66, far higher than any other')

Q.append(dict(
    n=21, orig=43, answer='C', topic='Tables & rates', attempt='',
    question=f"""<p>Fred is carrying out a three-year biological survey which depends on anglers sending in scale
samples of fish that they catch. The survey covers five rivers and Fred has set a target for the
numbers of sets of fish scales returned from each river each year. Unfortunately, by the end of
the second year the number of scale sets returned has fallen well short of target.</p>
{table([['Dark', '250', hl('77', 'g'), hl('125', 'g'), hl('5', 'g'), hl('30', 'g'), '31', '50'],
        ['Fare', '100', hl('85', 'g'), hl('35', 'g'), hl('20', 'g'), hl('8', 'g'), '85', '35'],
        ['Gwynt', '500', hl('71', 'g'), hl('132', 'g'), hl('19', 'g'), hl('2', 'g'), '14', '26'],
        ['Tine', '250', hl('105', 'g'), hl('66', 'g'), hl('43', 'g'), hl('19', 'g'), '42', '26'],
        ['Yarrow', '250', hl('80', 'g'), hl('150', 'g'), hl('18', 'g'), hl('25', 'g'), '32', '60']],
       head=['River', 'Annual target of scale sets', 'Scale sets Year 1', 'Scale sets Year 2', 'Anglers Year 1', 'Anglers Year 2',
             hl('% of target Year 1', 'p', 4), hl('% of target Year 2', 'p')])}
<p>{hl('The anglers who participated in the survey sent scales from all the fish they caught', 'y', 2)}.</p>
<p class="stem">For which river was the {hl('average catch per angler sending in scales', 'b', 1)} the highest {hl('in any one year', 'b', 3)}?</p>""",
    options={'A': 'Dark', 'B': 'Fare', 'C': 'Gwynt', 'D': 'Tine', 'E': 'Yarrow'},
    notes=[(1, 'b', 'Average catch per angler = scale sets ÷ number of anglers.'),
           (2, 'y', 'So one scale set = one fish caught.'),
           (3, 'b', 'Check both years and pick the single biggest.'),
           (4, 'p', 'The target and % columns are a distraction: you don’t need them.')],
    steps=[
        f"""<p>Divide scale sets by anglers for every river and year (rough is fine):</p>
{calc('Dark: 77 ÷ 5 ≈ 15, 125 ÷ 30 ≈ 4', 'Fare: 85 ÷ 20 ≈ 4, 35 ÷ 8 ≈ 4', 'Gwynt: 71 ÷ 19 ≈ 4, <b>132 ÷ 2 = 66</b>',
      'Tine: 105 ÷ 43 ≈ 2, 66 ÷ 19 ≈ 3', 'Yarrow: 80 ÷ 18 ≈ 4, 150 ÷ 25 = 6')}{_fish()}
{calc(f'biggest by miles: Gwynt, year 2 {ar()} {boxed("C")}')}""",
    ],
    answer_text='Gwynt: in year 2 just 2 anglers sent 132 scale sets, 66 each.',
    why={'A': 'Dark’s best is about 15 per angler (year 1).',
         'B': 'Fare is only about 4 per angler.',
         'D': 'Tine is only 2 to 3 per angler.',
         'E': 'Yarrow’s best is 6 per angler.'},
    fast='Look for a tiny number of anglers with lots of scale sets: Gwynt year 2, 132 from just 2 anglers.',
))

# ---------------------------------------------------------------- 22 (Q44)
SEG = {'a': (0, 0, 1, 0), 'b': (1, 0, 1, 1), 'c': (1, 1, 1, 2), 'd': (0, 2, 1, 2), 'e': (0, 1, 0, 2), 'f': (0, 0, 0, 1), 'g': (0, 1, 1, 1)}
DIG = {'G': 'afedc', '1': 'bc', '2': 'abged', '3': 'abgcd', '4': 'fgbc', '5': 'afgcd', '6': 'fgedc', '7': 'abc', '8': 'abcdefg', '9': 'afbgc'}


def _digits():
    parts, lab = [], []
    order = ['G', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i, d in enumerate(order):
        x0, y0, w, h = 22 + i * 62, 40, 28, 34
        on = DIG[d]
        for s, (xa, ya, xb, yb) in SEG.items():
            lit = s in on
            parts.append(line(x0 + xa * w, y0 + ya * h, x0 + xb * w, y0 + yb * h,
                              k='pen' if lit else 'muted', w=4.5 if lit else 1.2, dash=not lit))
        n = len(on)
        good = n == 5 and d != 'G'
        lab.append(text(x0 + w / 2, 30, 'floor ' + d if d != 'G' else 'ground', k='ink', size=13))
        lab.append(text(x0 + w / 2, 134, f'{n} bars', k='green' if good else 'muted', size=15))
        if good:
            parts.append(rect(x0 - 11, y0 - 9, w + 22, 2 * h + 18, k='green', sw=2.2, rx=10))
    lab.append(text(320, 168, '5 bars lit = could look like an 8 with 2 dead bars', k='green', size=18, font='scrawl'))
    return svg(650, 182, rough(*parts) + ''.join(lab), 'Floor display digits with lit bars; floors 2, 3, 5, 6 and 9 use exactly 5 bars')

Q.append(dict(
    n=22, orig=44, answer='A', topic='Displays & logic', attempt='',
    question=f"""<p>Allan wishes to visit a client on floor 8 of a building with 10 floors (including the ground floor). He
enters the lift on the ground floor. His client has explained by email that the floors are indicated
by an illuminated matrix but there is a notice stating that {hl('two of the lights are not working', 'p', 1)}.</p>
{fig(Y, 'q22_lift', 'The lift display: an 8 showing all seven bars, and how floors G and 1 to 9 look when all lights work', 470)}
<p>Allan enters the lift and pushes the button. Just then he starts to sneeze, distracting his attention
from the display. {hl('The lift leaves the ground floor', 'y', 2)}, travels, then stops. He glances at the display
and concludes {hl('he could be on floor 8', 'b', 3)} so he gets out. In fact he is on the wrong floor.</p>
<p class="stem">On how many of the floors could Allan have got out by mistake?</p>""",
    options={'A': '5', 'B': '6', 'C': '7', 'D': '8', 'E': '9'},
    notes=[(1, 'p', 'Two bars are dead (always off), the same two whatever floor it shows.'),
           (2, 'y', 'So he is not on the ground floor.'),
           (3, 'b', 'An 8 needs all 7 bars, so with 2 dead an 8 shows only 5 bars. He saw a 5-bar shape.')],
    steps=[
        f"""<p>An 8 lights all 7 bars. With 2 bars dead, floor 8 would show just <b>5 bars</b>.
Another floor looks the same only if it lights exactly those 5 bars, and its 2 unused bars are the dead ones.</p>""",
        f"""<p>Count the bars each floor uses on this display:</p>{_digits()}
{calc('5 bars: floors 2, 3, 5, 6, 9 (and G, but he left the ground floor)', '1 (2 bars), 4 (4 bars), 7 (3 bars) have too few lights to look like that',
      f'so {boxed("5")} floors')}""",
    ],
    answer_text='5 floors: 2, 3, 5, 6 and 9.',
    why={'B': '6 wrongly counts the ground floor, but the lift had left it.',
         'C': '7 includes floors with too few bars (they can’t show 5 lit bars).',
         'D': '8 counts nearly every floor, ignoring the number of bars.',
         'E': '9 counts every floor except 8.'},
    fast='8 with 2 dead bars = 5 lit bars. Floors that use exactly 5 bars: 2, 3, 5, 6, 9 (G excluded): 5.',
))

# ---------------------------------------------------------------- 23 (Q48)
def _tree():
    parts, lab = [], []
    W = 640
    def xs(n, pad=40):
        return [pad + (W - 2 * pad) * (i + 0.5) / n for i in range(n)]
    amy = (W / 2, 330)
    par = [(x, 270) for x in xs(2, 160)]
    gp = [(x, 210) for x in xs(4, 90)]
    ggp = [(x, 145) for x in xs(8)]
    # great-great: sisters (ggp0, ggp2) share parents S1 S2; brothers (ggp1, ggp3) share B1 B2; others 2 each
    top_x = xs(12, 30)
    gg2 = [(x, 50) for x in top_x]
    for p in par:
        parts.append(line(*amy, *p, k='muted', w=1.5))
    for i, g in enumerate(gp):
        parts.append(line(*par[i // 2], *g, k='muted', w=1.5))
    for i, g in enumerate(ggp):
        parts.append(line(*gp[i // 2], *g, k='muted', w=1.5))
    links = {0: (0, 1), 2: (0, 1), 1: (2, 3), 3: (2, 3), 4: (4, 5), 5: (6, 7), 6: (8, 9), 7: (10, 11)}
    for i, (a, b2) in links.items():
        parts.append(line(*ggp[i], *gg2[a], k='pen' if i in (0, 2) else 'orange' if i in (1, 3) else 'muted', w=1.6))
        parts.append(line(*ggp[i], *gg2[b2], k='pen' if i in (0, 2) else 'orange' if i in (1, 3) else 'muted', w=1.6))
    for j, p in enumerate(gg2):
        f = 'b' if j < 2 else 'o' if j < 4 else 'paper'
        parts.append(circle(*p, 11, k='ink', fill=f, sw=1.6))
    for i, p in enumerate(ggp):
        f = 'b' if i in (0, 2) else 'o' if i in (1, 3) else 'paper'
        parts.append(circle(*p, 11, k='ink', fill=f, sw=1.6))
        if i < 4:
            lab.append(text(p[0], p[1] + 30, 'sister' if i in (0, 2) else 'brother', k='pen' if i in (0, 2) else 'orange', size=13))
    for p in gp + par:
        parts.append(circle(*p, 11, k='ink', fill='paper', sw=1.6))
    parts.append(circle(*amy, 13, k='red', fill='y', sw=2))
    lab += [text(amy[0] + 24, amy[1] + 6, 'Amy', k='red', size=18, anchor='start', font='scrawl'),
            text(W - 8, 54, '12', k='green', size=26, anchor='end', font='scrawl'),
            text(W - 8, 150, '8', k='muted', size=20, anchor='end'), text(W - 8, 214, '4', k='muted', size=20, anchor='end'),
            text(W - 8, 274, '2', k='muted', size=20, anchor='end'),
            text(150, 20, 'the sisters share 2 parents', k='pen', size=15), text(150 + 160, 20, '· the brothers share 2', k='orange', size=15, anchor='start')]
    return svg(W, 350, rough(*parts) + ''.join(lab), 'Family tree from Amy up to great-great-grandparents: the two sisters share parents and the two brothers share parents, giving 12')

Q.append(dict(
    n=23, orig=48, answer='C', topic='Family trees & counting', attempt='',
    question=f"""<p>Amy is researching her family history. She has two parents and four grandparents. However,
she discovers that, {hl('among her great grandparents, two sisters from one family married two brothers from another', 'p', 1)}.</p>
<p class="stem">How many {hl('great-great grandparents', 'b', 2)} has she?</p>""",
    options={'A': '8', 'B': '10', 'C': '12', 'D': '14', 'E': '16'},
    notes=[(1, 'p', 'Two sisters = <b>same</b> parents. Two brothers = <b>same</b> parents.'),
           (2, 'b', 'One generation above the great-grandparents. Normally the numbers double: 2, 4, 8, 16.')],
    steps=[
        f"""<p>Normally: 2 parents → 4 grandparents → 8 great-grandparents → <b>16</b> great-great-grandparents.</p>""",
        f"""<p>But two of the 8 great-grandparents are sisters: they have the <b>same</b> 2 parents (2 people, not 4).
The two brothers also share their 2 parents (2 people, not 4).</p>{_tree()}
{calc('16 − 2 (sisters’ shared parents) − 2 (brothers’ shared parents)', f'= {boxed("12")}')}""",
    ],
    answer_text='12 great-great-grandparents.',
    why={'A': '8 is the number of great-grandparents, one generation too low.',
         'B': '10 takes away too many (6).',
         'D': '14 only counts one of the two families sharing parents.',
         'E': '16 is the normal doubling, ignoring the shared parents.'},
    fast='Normally 16. Two sisters share 2 parents (save 2), two brothers share 2 parents (save 2): 12.',
))

# ---------------------------------------------------------------- 24 (Q49)
def _canoes():
    parts, lab = [], []
    for g in range(3):
        gx = 30 + g * 205
        parts.append(rect(gx, 24, 190, 128, k='muted', sw=1.4, rx=12))
        for i in range(6):
            cx, cy = gx + 32 + (i % 3) * 52, 58 + (i // 3) * 48
            parts.append(path(f'M{cx - 22} {cy} Q{cx} {cy + 14} {cx + 22} {cy} Q{cx} {cy - 6} {cx - 22} {cy}Z', k='pen', fill='b', sw=1.6))
        lab.append(stick_person(gx + 170, 140, k='orange', s=0.75))
        lab.append(text(gx + 95, 172, '6 students + 1 instructor', k='ink', size=15))
    lab.append(text(320, 204, '18 students × £12 = £216   −   3 instructors × £12 = £36   →   £180', k='green', size=18, font='scrawl'))
    return svg(650, 218, rough(*parts) + ''.join(lab), 'Three groups of six students in canoes, each with an instructor: 216 minus 36 is 180')

Q.append(dict(
    n=24, orig=49, answer='B', topic='Best deal & ratio', attempt='',
    question=f"""<p>The West Water Canoe School offers tuition in basic canoeing skills. There are {hl('18 canoes', 'g', 1)} for
students to use. The school offers a {hl('minimum instructor to student ratio of 1:6 and a minimum of two instructors', 'p', 2)} for any group.</p>
<p>Instructors are hired by the centre on a casual basis and are paid only for the time they actually
work. {hl('Instructors are paid £6 per hour', 'g', 3)} and are expected to use their own canoes.</p>
<p>The cost for students depends on the numbers in the group and the length of the session.
Costs are set out in the table below.</p>
{table([['1 to 2', '£12', '£10'], ['3 to 6', '£10', '£8'], ['7 to 10', '£8', '£6'], [hl('more than 10', 'y'), hl('£7', 'y'), hl('£5', 'y')]],
       head=['Number in group', 'Cost per student for first hour', 'Cost per student for subsequent hours'])}
<p class="stem">What is the {hl('maximum profit', 'b', 4)} the centre can make from a group {hl('after paying the instructors', 'p', 5)} for a
{hl('two-hour session', 'g', 6)}?</p>""",
    options={'A': '£108', 'B': '£180', 'C': '£198', 'D': '£216', 'E': '£360'},
    notes=[(1, 'g', 'At most 18 students (instructors bring their own canoes).'),
           (2, 'p', 'At least 1 instructor per 6 students, and never fewer than 2.'),
           (3, 'g', 'Each instructor costs £6 × 2 hours = £12 for the session.'),
           (4, 'b', 'Try the sensible group sizes and compare.'),
           (5, 'p', 'Profit = what students pay − instructors’ pay.'),
           (6, 'g', 'Two hours = first hour + one subsequent hour.')],
    steps=[
        f"""<p>Price per student for 2 hours (first hour + one more):</p>
{calc('1–2 students: 12 + 10 = £22 each', '3–6: 10 + 8 = £18 each', '7–10: 8 + 6 = £14 each', 'more than 10: 7 + 5 = <b>£12 each</b>')}""",
        f"""<p>Try the biggest group of each kind (instructors cost £12 each):</p>
{calc('18 students: 18 × 12 = 216, needs 3 instructors (36) → <b>£180</b>', '12 students: 144, needs 2 (24) → £120',
      '10 students: 140 − 24 → £116', '6 students: 108 − 24 → £84')}{_canoes()}
{calc(f'maximum profit = {boxed("£180")}')}""",
    ],
    answer_text='£180: 18 students pay £216, and 3 instructors cost £36.',
    why={'A': '£108 is just what 6 students pay, before any instructors.',
         'C': '£198 = 216 − 18: paying the 3 instructors for only <b>one</b> hour.',
         'D': '£216 is the income before paying the instructors.',
         'E': '£360 is more than any group can ever pay (the most is £216).'},
    fast='Fill all 18 canoes: 18 × (7 + 5) = 216. Need 18 ÷ 6 = 3 instructors × £12 = 36. Profit 180.',
))

# ---------------------------------------------------------------- 25 (Q50)
def _museum():
    parts, lab = [], []
    X = lambda m: 40 + m * 0.72
    segs = [(0, 390, 'Adults ≈ £390', 'b'), (390, 525, 'Children ≈ £135', 'g'), (525, 679, 'Seniors ≈ £154', 'o')]
    for a, b2, name, f in segs:
        parts.append(rect(X(a), 30, X(b2) - X(a), 36, k='ink', fill=f, sw=1.6))
        lab.append(text((X(a) + X(b2)) / 2, 54, name, k='ink', size=14))
    people = [('÷ 7', '≈ 56 adults', X(195)), ('÷ 4', '≈ 34 children', X(457)), ('÷ 5', '≈ 30 seniors', X(602))]
    for op, res, x in people:
        parts.append(line(x, 70, x, 104, k='red', head=True, w=2))
        lab.append(text(x + 8, 92, op, k='red', size=16, anchor='start'))
        lab.append(text(x, 124, res, k='pen', size=17))
    p2, l2 = _pie(170, 230, 70, [56, 34, 30], ['b', 'g', 'o'], ['Adults', 'Children', 'Seniors'])
    p3, l3 = _pie(470, 230, 70, [390, 135, 154], ['b', 'g', 'o'], ['Adults', 'Children', 'Seniors'])
    lab += [text(170, 322, 'PEOPLE (what they ask)', k='green', size=17, font='scrawl'),
            text(170, 342, 'adults just under half', k='ink', size=15),
            text(470, 322, 'MONEY (the trap = pie A)', k='red', size=17, font='scrawl')]
    return svg(640, 352, rough(*parts, *p2, *p3) + ''.join(lab + l2 + l3),
               'Money split converted to people by dividing by the ticket price; the people pie has adults just under half, unlike the money pie')

Q.append(dict(
    n=25, orig=50, answer='B', topic='Charts & proportion', attempt='',
    question=f"""<p>The cost of entry to the Victoria and David Museum is as follows:</p>
<p>{hl('Adults £7', 'g', 1)}<br>{hl('Children £4', 'g', 1)}<br>{hl('Senior Citizens £5', 'g', 1)}</p>
<p>This chart shows the breakdown of yesterday's {hl('total takings of £679', 'p', 2)} by age group.</p>
{fig(Y, 'q25_bar', 'Bar split by takings: Adults from 0 to about 390 pounds, Children to about 525, Senior Citizens to 679', 470)}
<p class="stem">Which one of the following pie charts shows the {hl('number of visitors', 'b', 3)} in each age group that paid
to enter the museum yesterday?</p>
{fig(Y, 'q25_pies', 'Five pie charts A to E of Adults, Children and Senior Citizens', 400)}""",
    options={'A': 'pie A', 'B': 'pie B', 'C': 'pie C', 'D': 'pie D', 'E': 'pie E'},
    notes=[(1, 'g', 'Divide money by these prices to get people.'),
           (2, 'p', 'The bar shows <b>money</b>, not people.'),
           (3, 'b', 'They want <b>people</b>, so convert first.')],
    steps=[
        f"""<p>Read the bar roughly (it doesn’t need to be exact), then turn money into people by dividing by the ticket price:</p>{_museum()}
{calc('total ≈ 56 + 34 + 30 = 120 people', 'adults ≈ 56 ÷ 120 ≈ 47% (just under half)', 'children ≈ 28%, seniors ≈ 25% (about a quarter each)')}""",
        f"""<p>Find the pie with adults <b>just under half</b> and children and seniors about a quarter each: pie {boxed('B')}.</p>
{note('Pie A is the money split (adults ≈ 57% of the takings). That is the trap for anyone who forgets to divide by the prices.', 'trap')}""",
    ],
    answer_text='Pie B: adults just under half, children and seniors about a quarter each.',
    why={'A': 'Pie A matches the <b>money</b> (adults ≈ 58%), not the number of people.',
         'C': 'Adults are only about 38% and seniors far too big.',
         'D': 'Adults are exactly half, which would need 56 adults = 64 others. Not true.',
         'E': 'Adults are about 69%, far too many.'},
    fast='People = £ ÷ price: about 56, 34, 30. Adults just under half, the other two about equal: B. A is the money trap.',
))
