from wslib import *

Y = 2017
Q = []


def _cells(cells, x0, y0, c, fill, k='muted', sw=1):
    return [rect(x0 + cx * c, y0 + cy * c, c, c, k=k, fill=fill, sw=sw) for cx, cy in cells]


def _outline(cells, x0, y0, c, k='ink', w=3):
    cs, out = set(cells), []
    for cx, cy in cells:
        x, y = x0 + cx * c, y0 + cy * c
        if (cx, cy - 1) not in cs:
            out.append(line(x, y, x + c, y, k=k, w=w))
        if (cx, cy + 1) not in cs:
            out.append(line(x, y + c, x + c, y + c, k=k, w=w))
        if (cx - 1, cy) not in cs:
            out.append(line(x, y, x, y + c, k=k, w=w))
        if (cx + 1, cy) not in cs:
            out.append(line(x + c, y, x + c, y + c, k=k, w=w))
    return out


# ---------------------------------------------------------------- 18 (Q37)
def _ratio_line():
    X = lambda r: 60 + (r - 14) * 95
    parts = [line(X(14), 90, X(20), 90, k='ink', w=1.8, head=True)]
    lab = []
    for r in range(14, 20):
        parts.append(line(X(r), 84, X(r), 96, k='ink', w=1.5))
        lab.append(text(X(r), 116, r, k='muted', size=15))
    pts = [('Scotland', 15.1, 'green', -1), ('N Ireland', 16.2, 'orange', -1), ('South', 17.9, 'ink', -1),
           ('Midlands', 18.3, 'ink', 1), ('Wales', 19.1, 'ink', -1)]
    for name, r, k, side in pts:
        parts.append(circle(X(r), 90, 7, k=k, fill='paper' if k == 'ink' else ('g' if k == 'green' else 'o'), sw=2.4))
        y = 64 if side < 0 else 148
        lab.append(text(X(r), y, name, k=k, size=17))
        lab.append(text(X(r), y + (18 if side > 0 else -20), f'{r}', k=k, size=15))
    lab.append(text(X(14) - 4, 160, '← fewer pupils', k='green', size=17, anchor='start', font='scrawl'))
    lab.append(text(X(14) - 4, 180, 'per teacher', k='green', size=17, anchor='start', font='scrawl'))
    return svg(640, 190, rough(*parts) + ''.join(lab),
               'Number line of pupils per teacher: Scotland 15.1, Northern Ireland 16.2, South 17.9, Midlands 18.3, Wales 19.1')


Q.append(dict(
    n=18, orig=37, answer='D', topic='Ratios from tables',
    question=f"""<p>The table below shows the numbers of pupils and teachers in all UK schools in 2003:</p>
{table([['England North', '2,418', '132'], ['England Midlands', '1,613', '88'], ['England East', '900', '50'],
        ['England London', '1,173', '66'], ['England South', '2,160', '121'], ['Wales', '497', '26'],
        ['Scotland', '893', '59'], ['Northern Ireland', '341', '21']],
       head=['', f'<i>pupils {hl("(thousands)", "g", 1)}</i>', '<i>teachers (thousands)</i>'])}
<p class="stem">Which region had the {hl('<b>lowest</b>', 'p', 2)} ratio of {hl('<b>pupils per teacher</b>', 'b', 3)}?</p>""",
    options={'A': 'England Midlands', 'B': 'England South', 'C': 'Wales', 'D': 'Scotland', 'E': 'Northern Ireland'},
    notes=[(1, 'g', 'Both columns are in thousands, so the thousands cancel. Just divide the numbers.'),
           (2, 'p', 'Lowest, not highest. Don’t pick the biggest number by habit.'),
           (3, 'b', 'Pupils per teacher = pupils ÷ teachers. Smallest answer wins.')],
    steps=[
        f"""<p>Only the five options matter. Divide pupils by teachers (roughly is fine):</p>
{calc('Midlands: 1613 ÷ 88 ≈ 18.3', 'South: 2160 ÷ 121 ≈ 17.9', 'Wales: 497 ÷ 26 ≈ 19.1',
      'Scotland: 893 ÷ 59 ≈ <b>15.1</b>', 'Northern Ireland: 341 ÷ 21 ≈ 16.2')}""",
        f"""{_ratio_line()}
{calc(f'lowest ratio = {boxed("Scotland")}')}
{note('No calculator? Test against 16 pupils per teacher: Scotland 59 × 16 = 944, more than 893, so it is <b>below</b> 16. Northern Ireland 21 × 16 = 336, less than 341, so it is just above 16. Every other option is well above 16 (e.g. 88 × 16 = 1408, less than 1613).', 'tip')}""",
    ],
    answer_text='Scotland: about 15 pupils per teacher, the lowest.',
    why={'A': 'England Midlands has about 18.3 pupils per teacher.',
         'B': 'England South has about 17.9.',
         'C': 'Wales has about 19.1, the <b>highest</b> of the options: the opposite of what’s asked.',
         'E': 'Northern Ireland is close (about 16.2) and has the fewest pupils, but Scotland’s ratio is lower.'},
    fast='Test each option against 16 per teacher: only Scotland (59 × 16 = 944 > 893) comes out under 16.',
))


# ---------------------------------------------------------------- 19 (Q38)
_CUT_D = [(-70.6, 0), (-32.6, 15.6), (-16.6, 15.6), (-16.6, 0), (16.6, 0), (16.6, -15.6), (32.6, -15.6), (70.6, 0)]
_CUT_C = [(-70.6, 0), (-52.4, 0), (-35.2, 32.6), (0, 32.6), (0, -9.4), (30.7, -9.4), (51.7, 0), (70.6, 0)]


def _disc_panel(cx, cy, cut, R, title, ok):
    k = R / 70.6
    pts = [(cx + x * k, cy + y * k) for x, y in cut]
    twin = [(cx - x * k, cy - y * k) for x, y in cut]
    d_cut = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    tok = d_cut + f' A{R} {R} 0 0 1 {pts[0][0]:.1f} {pts[0][1]:.1f} Z'
    d_tw = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in twin)
    tw = d_tw + f' A{R} {R} 0 0 1 {twin[0][0]:.1f} {twin[0][1]:.1f} Z'
    parts = [path(tok, k='pen', fill='b', sw=2.2), path(tw, k='orange', fill='o', sw=2.2)]
    lab = [text(cx, cy - R - 16, title, k='ink', size=17)]
    if ok:
        lab += [text(cx, cy + R + 30, 'a perfect disc ✓', k='green', size=21, font='scrawl')]
    else:
        g1 = [(-52.4, 0), (-35.2, 32.6), (0, 32.6), (0, 9.4), (-30.7, 9.4), (-51.7, 0)]
        for g in (g1, [(-x, -y) for x, y in g1]):
            parts.append(poly([(cx + x * k, cy + y * k) for x, y in g], k='red', fill='p', sw=2))
        lab += [text(cx - 22 * k, cy + 25 * k, 'gap', k='red', size=16),
                text(cx + 22 * k, cy - 14 * k, 'gap', k='red', size=16),
                text(cx, cy + R + 30, 'holes: they don’t match ✗', k='red', size=21, font='scrawl')]
    lab += [text(cx - R - 8, cy + R - 10, 'token', k='pen', size=15, anchor='end'),
            text(cx + R + 8, cy - R + 16, 'twin', k='orange', size=15, anchor='start')]
    return parts, lab


def _discs():
    p1, l1 = _disc_panel(170, 160, _CUT_D, 92, 'D + its twin, turned half a turn', True)
    p2, l2 = _disc_panel(480, 160, _CUT_C, 92, 'C + its twin, turned half a turn', False)
    return svg(660, 300, rough(*p1, *p2) + ''.join(l1 + l2),
               'Left: token D and an identical copy turned upside down make a complete disc. Right: token C and its copy leave two gaps')


Q.append(dict(
    n=19, orig=38, answer='C', topic='Shapes & symmetry',
    question=f"""<p>When a mixed doubles tournament is held at my tennis club, partners are chosen by the
following method.</p>
<p>The appropriate number of tokens, all with a different shape, are placed into a box, and the
male participants all pick one out. Each token has an {hl("identical 'twin'", 'y', 1)} in a second box, from
which the female participants all select one. {hl('Each pair of identical tokens fit together to make a complete disc', 'y', 2)}. Couples with identical tokens partner each other in the tournament.</p>
<p class="stem">Which one of the following {hl('can <b>not</b>', 'b', 3)} be a token used by my tennis club?</p>
{fig(Y, 'ps_q19_tokens', 'Five tokens A to E: each is a round-bottomed piece of a disc with a zig-zag or stepped top edge', 520)}""",
    options={'A': 'token A', 'B': 'token B', 'C': 'token C', 'D': 'token D', 'E': 'token E'},
    notes=[(1, 'y', 'The twin is the <b>same shape</b>. So two copies of the token must make the disc.'),
           (2, 'y', 'To fit, you turn the twin upside down (half a turn). Its cut edge must slot exactly into the first one.'),
           (3, 'b', 'Find the token whose two copies would <b>not</b> make a disc.')],
    steps=[
        f"""<p>Two identical pieces make a whole disc, so each token is exactly half, and the twin is the token turned half a turn.
That only works if the cut edge looks the same after a half turn: every bump on one side of the centre needs a
matching dip on the other side.</p>{_discs()}""",
        f"""<p>Check each cut from the middle outwards:</p>
<ul><li>A, B, D, E: the left half of the cut, turned upside down, is exactly the right half. {tick()}</li>
<li>C: the left side dips <b>deep</b> below the middle line, but the right side only rises a <b>little</b> above it. Turned round, they can’t meet. {cross()}</li></ul>
{calc(f'cannot be a token {ar()} {boxed("C")}')}
{note('Quick test: turn the page upside down in your head. A good token’s cut looks the same both ways up.', 'tip')}""",
    ],
    answer_text='Token C: its cut is not the same after a half turn, so two copies leave gaps.',
    why={'A': 'A’s stepped zig-zag goes up the same way on both sides of the centre, so a half-turned copy fits.',
         'B': 'B’s deep V on the left matches the tall block on the right, so its twin fits.',
         'D': 'D’s step down on the left matches its step up on the right (see the sketch).',
         'E': 'E’s two big zig-zags are the same shape, one upside down, so two copies make a disc.'},
    fast='A token works only if its cut looks the same after a half turn. C’s deep dip on the left has only a small bump to match on the right.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _receipts():
    parts, lab = [], []

    def receipt(x, title, lines, total, k):
        w, h = 270, 190
        zig = [(x + i * 15, 40 + h + (8 if i % 2 else 0)) for i in range(19)]
        parts.append(poly([(x, 40)] + zig + [(x + w, 40)], k=k, fill='paper', sw=2))
        lab.append(text(x + w / 2, 70, title, k=k, size=20, font='scrawl'))
        for i, (a, b) in enumerate(lines):
            lab.append(text(x + 18, 108 + i * 30, a, k='ink', size=15, anchor='start', font='print'))
            lab.append(text(x + w - 18, 108 + i * 30, b, k='ink', size=15, anchor='end', font='print'))
        parts.append(line(x + 14, 108 + len(lines) * 30 - 16, x + w - 14, 108 + len(lines) * 30 - 16, k='muted', w=1.2, dash=True))
        lab.append(text(x + 18, 108 + len(lines) * 30 + 10, 'per day', k='ink', size=17, anchor='start', weight='700', font='print'))
        lab.append(text(x + w - 18, 108 + len(lines) * 30 + 10, total, k=k, size=19, anchor='end', weight='700', font='print'))

    receipt(30, 'Pet shop', [('2 sachets × £1.00', '£2.00'), ('25 g × 1p', '£0.25')], '£2.25', 'red')
    receipt(350, 'Online', [('2 sachets × 65p', '£1.30'), ('25 g × 0.8p', '£0.20')], '£1.50', 'green')
    lab.append(text(320, 276, 'saving: £2.25 − £1.50 = 75p a day', k='pen', size=22, font='scrawl'))
    return svg(650, 290, rough(*parts) + ''.join(lab),
               'Two receipts for one day of cat food: pet shop 2.25 pounds, online 1.50 pounds, saving 75p')


Q.append(dict(
    n=20, orig=42, answer='B', topic='Unit prices',
    question=f"""<p>Joan has a cat called Tibber.</p>
<p>Every day Tibber is fed {hl('2 sachets of wet food and 25 grams of dry food', 'y', 1)}.</p>
<p>For some time, Joan has bought the cat food from the local pet shop where {hl('one box of 12 sachets costs £12.00', 'g', 2)} and {hl('one 400 gram packet of dry food costs £4.00', 'g', 3)}.</p>
<p>Joan has now decided to buy all of the cat food from an online distributor.</p>
<p>{hl('Four boxes, each of 24 sachets of wet food, will cost £62.40', 'p', 4)}, and {hl('one 2 kilogram packet of dry food will cost £16.00', 'g', 5)}.</p>
<p class="stem">How much money will Joan {hl('<b>save each day</b>', 'b', 6)} on cat food when she buys it from the online
distributor rather than the local pet shop?</p>""",
    options={'A': '40p', 'B': '75p', 'C': '93p', 'D': '£1.50', 'E': '£2.25'},
    notes=[(1, 'y', 'One day’s food: <b>2</b> sachets + 25 g. Work everything out for one day.'),
           (2, 'g', 'Shop: £12 ÷ 12 = £1 a sachet.'),
           (3, 'g', 'Shop: £4 ÷ 400 g = 1p a gram.'),
           (4, 'p', '£62.40 buys <b>4 × 24 = 96</b> sachets, not 24.'),
           (5, 'g', '2 kg = 2000 g. £16 ÷ 2000 = 0.8p a gram.'),
           (6, 'b', 'Shop cost per day − online cost per day.')],
    steps=[
        f"""<p>Find the price of one sachet and one gram in each place:</p>
{calc('shop sachet: £12 ÷ 12 = £1.00', 'shop dry food: £4 ÷ 400 g = 1p a gram',
      'online sachet: £62.40 ÷ 96 = 65p', 'online dry food: £16 ÷ 2000 g = 0.8p a gram')}
{note('£62.40 ÷ 96: try 65p. 100 × 65p = £65, take off 4 × 65p = £2.60, giving £62.40 ✓.', 'tip')}""",
        f"""<p>Now one day’s food in each place:</p>{_receipts()}
{calc(f'£2.25 − £1.50 = {boxed("75p")} a day')}""",
    ],
    answer_text='75p a day: £2.25 at the pet shop against £1.50 online.',
    why={'A': '40p forgets that Tibber eats <b>2</b> sachets a day: 35p saved on one sachet + 5p on the dry food.',
         'C': '93p comes from a slip with the online dry food: 2p a day instead of 20p.',
         'D': '£1.50 is what one day costs online, not the saving.',
         'E': '£2.25 is what one day costs at the pet shop, not the saving.'},
    fast='Shop: 2 × £1 + 25p = £2.25. Online: 2 × 65p + 20p = £1.50. Save 75p.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _critter(x, y, legs, horns, tail, k, fill):
    out = [path(f'M{x - 44} {y} a44 24 0 1 0 88 0 a44 24 0 1 0 -88 0', k=k, fill=fill, sw=2.2)]
    for i in range(legs):
        lx = x - 32 + (64 * i / (legs - 1) if legs > 1 else 32)
        out.append(line(lx, y + 20, lx + (-4 if i % 2 else 4), y + 44, k=k, w=2.4))
    for i in range(horns):
        hx = x - 14 + (28 * i / (horns - 1) if horns > 1 else 14)
        out.append(poly([(hx - 6, y - 22), (hx, y - 42), (hx + 6, y - 22)], k=k, fill='y', sw=2))
    if tail:
        out.append(path(f'M{x + 42} {y - 6} q22 -6 18 -28 q-2 -10 8 -12', k=k, sw=2.4))
    out.append(circle(x - 24, y - 6, 3.5, k='ink', fill='ink', sw=1))
    return out


def _critters():
    parts, lab = [], []
    data = [(110, 'Arp', 6, 3, True, 'pen', 'b', '6 legs, 3 horns, tail', '× 25'),
            (330, 'Orp', 4, 2, False, 'green', 'g', '4 legs, 2 horns', '× 12'),
            (540, 'Urp', 3, 0, True, 'orange', 'o', '3 legs, tail', '× 8')]
    for x, name, legs, horns, tail, k, f, desc, n in data:
        parts += _critter(x, 90, legs, horns, tail, k, f)
        lab += [text(x, 30, name, k=k, size=22, font='scrawl'),
                text(x, 162, desc, k='ink', size=15),
                text(x, 196, n, k='red', size=28, font='scrawl')]
    lab.append(text(330, 230, 'legs: 150 + 48 + 24 = 222 ✓', k='green', size=19, font='scrawl'))
    return svg(660, 244, rough(*parts) + ''.join(lab),
               'Doodles of an Arp (6 legs, 3 horns, tail) times 25, an Orp (4 legs, 2 horns) times 12 and an Urp (3 legs, tail) times 8')


Q.append(dict(
    n=21, orig=43, answer='A', topic='Simultaneous counting',
    question=f"""<p>A particular computer game involves the capturing of three types of mythical creatures: Arps,
Orps and Urps.</p>
<p>Arps have {hl('6 legs, 3 horns and a tail', 'g', 1)}.</p>
<p>Orps have 4 legs and 2 horns, {hl('but no tail', 'y', 2)}.</p>
<p>Urps have 3 legs and a tail, {hl('but no horns', 'y', 3)}.</p>
<p>The last time Billy played this game he captured {hl('45 creatures with a total of 222 legs, 99 horns and 33 tails', 'g', 4)}.</p>
<p class="stem">How many of the 45 creatures that Billy captured were {hl('<b>Urps</b>', 'b', 5)}?</p>""",
    options={'A': '8', 'B': '12', 'C': '15', 'D': '20', 'E': '25'},
    notes=[(1, 'g', 'Every creature has 1 tail or none. That makes tails the easiest clue.'),
           (2, 'y', 'Orps are the only ones <b>without</b> a tail.'),
           (3, 'y', 'Urps have no horns, so all 99 horns come from Arps and Orps.'),
           (4, 'g', 'Four totals. You only need three of them; the fourth (legs) is your check.'),
           (5, 'b', 'Number of Urps.')],
    steps=[
        f"""<p>Start with tails: each Arp and each Urp has exactly one.</p>
{calc('Arps + Urps = 33', f'Orps = 45 − 33 = <b>12</b>')}""",
        f"""<p>Horns come only from Arps (3 each) and Orps (2 each):</p>
{calc('3 × Arps + 2 × 12 = 99', '3 × Arps = 75', 'Arps = <b>25</b>')}""",
        f"""{calc(f'Urps = 33 − 25 = {boxed("8")}')}
{_critters()}
{note('Use the clue that involves the fewest creature types first (tails, then horns). Save the messy one (legs) for checking.', 'tip')}""",
    ],
    answer_text='8 Urps (with 25 Arps and 12 Orps).',
    why={'B': '12 is the number of Orps, not Urps.',
         'C': '15 Urps would mean 18 Arps, giving 18 × 3 + 12 × 2 = 78 horns, not 99.',
         'D': '20 Urps would mean 13 Arps, giving only 63 horns.',
         'E': '25 is the number of Arps.'},
    fast='Tails: Orps = 45 − 33 = 12. Horns: 3A + 24 = 99, A = 25. Urps = 33 − 25 = 8.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _l_face():
    c = 90
    x0, y0 = 200, 50
    tall = [(0, 0), (0, 1)]
    foot = [(1, 1)]
    parts = _cells(tall + foot, x0, y0, c, 'b', k='muted') + _outline(tall + foot, x0, y0, c, k='ink', w=3)
    edges = [  # (x1, y1, x2, y2, label, lx, ly, anchor, colour)
        (x0, y0, x0, y0 + 2 * c, 'tall side (2 long)', x0 - 12, y0 + c + 6, 'end', 'red'),
        (x0, y0, x0 + c, y0, 'top of tall part', x0 + c / 2, y0 - 12, 'middle', 'orange'),
        (x0 + c, y0, x0 + c, y0 + c, 'step', x0 + c + 12, y0 + c / 2 + 6, 'start', 'violet'),
        (x0 + c, y0 + c, x0 + 2 * c, y0 + c, 'top of foot', x0 + 1.5 * c + 10, y0 + c - 12, 'start', 'green'),
        (x0 + 2 * c, y0 + c, x0 + 2 * c, y0 + 2 * c, 'end of foot', x0 + 2 * c + 12, y0 + 1.5 * c + 6, 'start', 'pen'),
        (x0, y0 + 2 * c, x0 + 2 * c, y0 + 2 * c, 'bottom (2 long)', x0 + c, y0 + 2 * c + 26, 'middle', 'red'),
    ]
    lab = []
    for x1, y1, x2, y2, t, lx, ly, anc, k in edges:
        parts.append(line(x1, y1, x2, y2, k=k, w=6))
        lab.append(text(lx, ly, t, k=k, size=17, anchor=anc))
    lab += [text(x0 + c / 2, y0 + 1.5 * c + 6, 'L face', k='ink', size=16),
            text(280, 294, 'front L + back L + 6 faces round the edge = 3 + 3 + 8 = 14 squares', k='ink', size=16)]
    return svg(560, 308, rough(*parts) + ''.join(lab),
               'The L-shaped end face with the six faces that join along its edges: tall side, top of tall part, step, top of foot, end of foot, bottom')


def _net_a():
    c = 58
    x0, y0 = 60, 40
    faces = [
        ([(0, 0)], 'p', 'red', '?!'),
        ([(0, 1)], 'g', 'ink', 'foot top'),
        ([(1, 1), (0, 2), (1, 2)], 'b', 'ink', 'front L'),
        ([(2, 1), (2, 2)], 'y', 'ink', 'tall side'),
        ([(3, 1), (3, 2), (4, 2)], 'b', 'ink', 'back L'),
        ([(4, 1)], 'v', 'ink', 'step'),
        ([(4, 0)], 'o', 'ink', 'top'),
        ([(3, 3), (4, 3)], 'y', 'ink', 'bottom'),
    ]
    parts, lab = [], []
    for cells, f, k, t in faces:
        parts += _cells(cells, x0, y0, c, f, k='muted', sw=0.8)
    for cells, f, k, t in faces:
        parts += _outline(cells, x0, y0, c, k='red' if k == 'red' else 'ink', w=2.6)
    spots = {'?!': (0.5, 0.62), 'foot top': (0.5, 1.6), 'front L': (1.0, 2.62), 'tall side': (2.5, 2.1),
             'back L': (3.9, 2.62), 'step': (4.5, 1.6), 'top': (4.5, 0.62), 'bottom': (4.0, 3.62)}
    for t, (sx, sy) in spots.items():
        lab.append(text(x0 + sx * c, y0 + sy * c + 4, t, k='red' if t == '?!' else 'ink',
                        size=22 if t == '?!' else 15, font='scrawl' if t == '?!' else 'hand'))
    parts.append(arrow(x0 + c + 6, y0 + 0.3 * c, x0 + 3.4 * c, y0 + 2.3 * c, k='red', bend=-0.35))
    lab += [text(x0 + 6 * c - 10, y0 + 0.4 * c, 'This square is joined to the', k='red', size=16, anchor='start'),
            text(x0 + 6 * c - 10, y0 + 0.4 * c + 22, 'far edge of “foot top”, which', k='red', size=16, anchor='start'),
            text(x0 + 6 * c - 10, y0 + 0.4 * c + 44, 'is where the back L goes.', k='red', size=16, anchor='start'),
            text(x0 + 6 * c - 10, y0 + 0.4 * c + 76, 'Folded, it lands on the back L,', k='red', size=16, anchor='start'),
            text(x0 + 6 * c - 10, y0 + 0.4 * c + 98, 'and the end of the foot', k='red', size=16, anchor='start'),
            text(x0 + 6 * c - 10, y0 + 0.4 * c + 120, 'is left open.', k='red', size=16, anchor='start')]
    return svg(660, 290, rough(*parts) + ''.join(lab),
               'Net A redrawn with each face named: the top-left square is attached to the foot-top square on the edge where the back L belongs, so it overlaps the back L and the end of the foot is missing')


Q.append(dict(
    n=22, orig=44, answer='A', topic='Nets & folding',
    question=f"""<p>The drawing below shows an ‘L’ shaped box.</p>
{fig(Y, 'ps_q22_box', 'A box shaped like a capital L: a tall block on the left joined to a lower block on the right', 150)}
<p class="stem">Which one of the nets below {hl('<b>cannot</b>', 'b', 1)} be folded up to form the ‘L’ shaped box? ({hl('A dotted line indicates a fold and a solid line indicates a cut', 'y', 2)}.)</p>
{fig(Y, 'ps_q22_nets', 'Five nets A to E made of squares, with dotted fold lines and solid cut lines', 540)}""",
    options={'A': 'net A', 'B': 'net B', 'C': 'net C', 'D': 'net D', 'E': 'net E'},
    notes=[(1, 'b', 'Four nets work. Hunt for the one face that ends up in the wrong place.'),
           (2, 'y', 'A solid line <b>inside</b> a net means those squares are not joined. Dotted lines show which edges hold faces together.')],
    steps=[
        f"""<p>First list the faces of the box. There are two L-shaped ends (3 squares each) and a band of six faces going round the edge of the L:</p>
{_l_face()}
<p>Every net has 14 squares, so counting won’t help. Check <b>which edge</b> each face is joined to.</p>""",
        f"""<p>Name the faces in net A. The two L shapes are the ends. The 1 × 2 strip between them is the tall side, the strip below the right L is the bottom,
the square on the right L’s inner corner is the step, with the top of the tall part above it. On the left L, the square sitting on the foot is the top of the foot.
Then there is one square left over:</p>{_net_a()}
{calc(f'one face lands on the back L, and the end of the foot is missing {ar()} {boxed("A")}')}
{note('Fast check for each net: find the two L’s, then make sure each small square is attached to an edge it really touches on the box. The square for the end of the foot must be attached to the end of a foot (or to the bottom strip or the top of the foot, at the right edge).', 'tip')}""",
    ],
    answer_text='Net A: its top-left square folds onto the back L, so the end of the foot is never covered.',
    why={'B': 'B: the two L’s are joined by the tall side; the top of the foot, step, top of the tall part, end of the foot and bottom are all on the right edges.',
         'C': 'C: the two 1 × 2 strips meet end to end at the corner (tall side and bottom), and each small square sits on a correct edge.',
         'D': 'D: the row of four squares wraps round the L in order: end of foot, top of foot, step, top of the tall part. It folds up.',
         'E': 'E: every face is joined along an edge it really touches, so it folds into the box.'},
    fast='Name the faces of net A: two L’s, tall side, bottom, step, top, foot top… and the last square is stuck to the far edge of the foot top, where the back L goes. A can’t fold.',
))


# ---------------------------------------------------------------- 23 (Q48)
def _tiles():
    words = ['TEAR', 'RITE', 'TREE', 'RAT']
    col = {'T': 'o', 'R': 'o', 'E': 'b', 'A': 'g', 'I': 'v'}
    parts, lab = [], []
    for i, wd in enumerate(words):
        y = 30 + i * 56
        for j, ch in enumerate(wd):
            x = 40 + j * 52
            parts.append(rect(x, y, 44, 44, k='ink', fill=col[ch], sw=1.8, rx=5))
            lab.append(text(x + 22, y + 30, ch, k='ink', size=24, font='print', weight='700'))
    lab += [text(290, 60, 'Every word has one T and one R.', k='orange', size=19, anchor='start'),
            text(290, 88, 'They always travel as a pair,', k='orange', size=19, anchor='start'),
            text(290, 116, 'so only T + R can be found.', k='orange', size=19, anchor='start'),
            text(290, 164, 'E, A and I come and go between', k='pen', size=19, anchor='start'),
            text(290, 192, 'words, so subtracting picks them out ✓', k='pen', size=19, anchor='start')]
    return svg(640, 254, rough(*parts) + ''.join(lab),
               'Letter tiles for TEAR, RITE, TREE and RAT; T and R are coloured the same because they always appear together; E, A and I can be found')


Q.append(dict(
    n=23, orig=48, answer='D', topic='Logic with unknowns',
    question=f"""<p>Each word in a word game is scored by {hl('adding up the values of its letters', 'y', 1)}. Each letter has the
same value whenever it appears but different letters have different values. I know the word
values for {hl('TEAR, RITE, TREE and RAT', 'g', 2)}, but none of the letter values.</p>
<p class="stem">{hl('<b>How many</b> of the letter values', 'b', 3)} can I now calculate?</p>""",
    options={'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4'},
    notes=[(1, 'y', 'Word value = sum of its letters. E appears twice in TREE, so it counts twice there.'),
           (2, 'g', 'Four words, five different letters: T, E, A, R, I.'),
           (3, 'b', 'Count the letters you can pin down exactly.')],
    steps=[
        f"""<p>Write each word as a sum:</p>
{calc('TEAR = T + E + A + R', 'RITE = R + I + T + E', 'TREE = T + R + E + E', 'RAT = R + A + T')}""",
        f"""<p>Subtract words that share letters:</p>
{calc(f'TEAR − RAT = E {tick()}', f'TREE − 2E = T + R (only the pair)',
      f'RAT − (T + R) = A {tick()}', f'RITE − (T + R) − E = I {tick()}')}
{_tiles()}""",
        f"""<p>T and R appear together in <b>every</b> word, so you only ever learn T + R, never T or R alone.</p>
{calc(f'E, A and I {ar()} {boxed("3")} letter values')}""",
    ],
    answer_text='3 letters (E, A and I). T and R only ever appear as a pair.',
    why={'A': '0 is too few: TEAR − RAT gives E straight away.',
         'B': '1 stops after finding E. Once you know T + R, A and I follow too.',
         'C': '2 misses one of A or I. Both come out once you know T + R.',
         'E': '4 would need T or R on its own, but every word contains both T and R, so they can’t be separated.'},
    fast='TEAR − RAT = E. TREE gives T + R, then RAT gives A and RITE gives I. T and R never split: 3.',
))


# ---------------------------------------------------------------- 24 (Q49)
def _clocks():
    X = lambda h: 110 + h * 21.5
    rows = [('Nathan', 'London', [(8, 20)], 'pen', 'b', '08–20'),
            ('Mark', 'San Diego', [(16, 24), (0, 4)], 'orange', 'o', '08–20 local'),
            ('Ben', 'Barcelona', [(7, 19)], 'green', 'g', '08–20 local'),
            ('Isabel', 'Nairobi', [(6, 18)], 'violet', 'v', '08–20 local')]
    parts, lab = [], []
    parts.append(rect(X(8), 34, X(19) - X(8), 4 * 40 + 8, k='red', fill='p', sw=1.6))
    for i, (name, city, spans, k, f, loc) in enumerate(rows):
        y = 40 + i * 40
        lab.append(text(X(0) - 8, y + 21, name, k=k, size=17, anchor='end'))
        for a, b in spans:
            parts.append(rect(X(a), y + 4, X(b) - X(a), 26, k=k, fill=f, sw=2))
        a, b = spans[0]
        lab.append(text((X(a) + X(b)) / 2, y + 22, f'{a:02d}–{b % 24:02d}' if name != 'Mark' else '16–04 (next day)',
                        k='ink', size=14))
    for h in range(0, 25, 2):
        parts.append(line(X(h), 210, X(h), 218, k='ink', w=1.4))
        lab.append(text(X(h), 236, f'{h:02d}', k='muted', size=14))
    parts.append(line(X(0), 210, X(24), 210, k='ink', w=1.6))
    counts = [(0, 4, 1), (4, 6, 0), (6, 7, 1), (7, 8, 2), (8, 16, 3), (16, 18, 4), (18, 19, 3), (19, 20, 2), (20, 24, 1)]
    for a, b, n in counts:
        lab.append(text((X(a) + X(b)) / 2, 262, n, k='red' if n >= 3 else 'muted', size=18 if n >= 3 else 15,
                        weight='700' if n >= 3 else None))
    lab += [text(X(0) - 8, 262, 'online:', k='ink', size=15, anchor='end'),
            text(X(13.5), 28, '08:00–19:00 London time = 11 hours', k='red', size=19, font='scrawl'),
            text(X(12), 290, 'all times in London time', k='muted', size=14)]
    return svg(660, 300, rough(*parts) + ''.join(lab),
               'Timeline in London time: Nathan 08 to 20, Mark 16 to 04, Ben 07 to 19, Isabel 06 to 18; at least three are online from 08:00 to 19:00, 11 hours')


Q.append(dict(
    n=24, orig=49, answer='D', topic='Time zones & overlaps',
    question=f"""<p>Nathan lives in London. His older brother Mark lives in San Diego, his younger brother Ben
lives in Barcelona and his sister Isabel lives in Nairobi. Nathan is trying to arrange an online call
between all four siblings. Each of the siblings has agreed to be available {hl('between 08:00 and 20:00 local time', 'g', 1)}.</p>
<p>{hl('San Diego is 8 hours behind London time.', 'y', 2)}</p>
<p>{hl('Barcelona is 1 hour ahead of London time.', 'y', 3)}</p>
<p>{hl('Nairobi is 2 hours ahead of London time.', 'y', 4)}</p>
<p class="stem">For how many hours during a 24-hour period are {hl('<b>at least three</b> of the four', 'b', 5)} siblings able to be
online at the same time?</p>""",
    options={'A': '8', 'B': '9', 'C': '10', 'D': '11', 'E': '12'},
    notes=[(1, 'g', 'Everyone: a 12-hour window in their <b>own</b> time. Put them all on London time.'),
           (2, 'y', 'Behind: when it’s 08:00 in San Diego it’s 16:00 in London. Add 8.'),
           (3, 'y', 'Ahead: 08:00 in Barcelona is 07:00 in London. Take 1 off.'),
           (4, 'y', 'Ahead: 08:00 in Nairobi is 06:00 in London. Take 2 off.'),
           (5, 'b', '3 or 4 people online. Not the time when all four are on.')],
    steps=[
        f"""<p>Change each window (08:00–20:00 local) into London time:</p>
{calc('Nathan: 08:00–20:00', 'Mark: 16:00–04:00 (into the next morning)', 'Ben: 07:00–19:00', 'Isabel: 06:00–18:00')}
{note('“Ahead” means their clock shows a later time, so London is earlier: subtract. “Behind” means add.', 'trap')}""",
        f"""<p>Draw the four windows on one London clock and count who is online:</p>{_clocks()}""",
        f"""{calc('08:00–16:00: Nathan, Ben, Isabel = 3 (8 hours)', '16:00–18:00: all four (2 hours)',
                  '18:00–19:00: Nathan, Ben, Mark = 3 (1 hour)', f'total = 8 + 2 + 1 = {boxed("11 hours")}')}""",
    ],
    answer_text='11 hours: from 08:00 to 19:00 London time.',
    why={'A': '8 stops at 16:00, when Mark joins. But at least three stay online until 19:00.',
         'B': '9 is too few: 08:00 to 19:00 is 11 hours with three or more online.',
         'C': '10 counts 08:00–18:00 (Nathan, Ben and Isabel) but forgets 18:00–19:00, when Mark has joined Nathan and Ben.',
         'E': '12 is the length of one person’s window. There’s no 12-hour stretch with three people: at 07:00 only Ben and Isabel are on, at 19:00 only Nathan and Mark.'},
    fast='London times: N 8–20, M 16–4, B 7–19, I 6–18. Three or more from 08 (N joins) to 19 (B leaves) = 11 hours.',
))


# ---------------------------------------------------------------- 25 (Q50)
_L = [(0, 0), (0, 1), (0, 2), (1, 2)]


def _turns():
    c = 22
    parts, lab = [], []
    shapes = [(_L, 'as bought'), ([(0, 0), (1, 0), (2, 0), (0, 1)], 'quarter turn'),
              ([(0, 0), (1, 0), (1, 1), (1, 2)], 'half turn'), ([(2, 0), (0, 1), (1, 1), (2, 1)], 'three-quarter turn')]
    x = 30
    for cells, t in shapes:
        parts += _cells(cells, x, 50, c, 'b', k='muted') + _outline(cells, x, 50, c, k='pen', w=2.6)
        w = max(cx for cx, _ in cells) + 1
        lab.append(text(x + w * c / 2, 140, t, k='ink', size=14))
        lab.append(text(x + w * c / 2, 162, '✓', k='green', size=18))
        x += w * c + 46
    mirror = [(1, 0), (1, 1), (1, 2), (0, 2)]
    parts += _cells(mirror, x + 20, 50, c, 'p', k='muted') + _outline(mirror, x + 20, 50, c, k='red', w=2.6)
    parts += [line(x + 8, 44, x + 84, 124, k='red', w=3), line(x + 84, 44, x + 8, 124, k='red', w=3)]
    lab += [text(x + 46, 140, 'flipped over', k='red', size=14), text(x + 46, 160, 'legs in the air!', k='red', size=14),
            text(330, 26, 'a table can spin round on the floor, but can’t turn over', k='ink', size=16)]
    return svg(640, 176, rough(*parts) + ''.join(lab),
               'The L table in its four turned positions, all allowed, and its mirror image crossed out because the table would have to be upside down')


def _arrangements():
    c = 30
    splits = {
        'A': ([(0, 0), (1, 0), (2, 0), (0, 1)], [(3, 0), (1, 1), (2, 1), (3, 1)], True),
        'B': ([(0, 1), (1, 1), (2, 1), (2, 0)], [(3, 0), (4, 0), (5, 0), (3, 1)], True),
        'C': ([(0, 0), (1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2), (3, 2)], True),
        'D': ([(0, 1), (1, 1), (2, 1), (2, 0)], [(3, 0), (3, 1), (4, 1), (5, 1)], False),
        'E': ([(0, 0), (1, 0), (2, 0), (0, 1)], [(0, 2), (0, 3), (0, 4), (1, 4)], True),
    }
    pos = {'A': (40, 50), 'B': (230, 50), 'C': (470, 50), 'D': (40, 230), 'E': (330, 200)}
    parts, lab = [], []
    for k, (t1, t2, ok) in splits.items():
        x0, y0 = pos[k]
        parts += _cells(t1, x0, y0, c, 'b') + _cells(t2, x0, y0, c, 'o' if ok else 'p')
        parts += _outline(t1, x0, y0, c, k='pen', w=3) + _outline(t2, x0, y0, c, k='orange' if ok else 'red', w=3)
        lab.append(text(x0 - 14, y0 + 18, k, k='ink', size=20, weight='700'))
        h = max(r for _, r in t1 + t2) + 1
        w = max(cx for cx, _ in t1 + t2) + 1
        if ok:
            lab.append(text(x0 + w * c / 2, y0 + h * c + 24, 'two L’s ✓', k='green', size=17))
    lab += [text(40 + 3 * c, 230 + 2 * c + 24, 'left L + right J: mirror images ✗', k='red', size=17),
            text(40 + 3 * c, 230 + 2 * c + 46, 'one table would be upside down', k='red', size=15)]
    return svg(660, 390, rough(*parts) + ''.join(lab),
               'Each arrangement split into two tables: A, B, C and E are two copies of the same L turned round; D needs an L and its mirror image')


Q.append(dict(
    n=25, orig=50, answer='D', topic='Shapes & rotation',
    question=f"""<p>Marina purchased {hl('a pair of L-shaped tables', 'y', 1)} thinking that they would add an unusual touch to
her conference room.</p>
{fig(Y, 'ps_q25_tables', 'Two identical L-shaped tables side by side, each a tall bar with a foot sticking out to the right at the bottom', 190)}
<p class="stem">Which one of the following arrangements {hl('could <b>not</b>', 'b', 2)} be made using the two {hl('L-shaped tables', 'p', 3)}?</p>
{fig(Y, 'ps_q25_options', 'Five outline shapes A to E, each made of eight squares', 520)}""",
    options={'A': 'arrangement A', 'B': 'arrangement B', 'C': 'arrangement C', 'D': 'arrangement D', 'E': 'arrangement E'},
    notes=[(1, 'y', 'Two identical tables, both the same “L” (a bar of 3 with a foot).'),
           (2, 'b', 'Four arrangements can be made; find the impossible one.'),
           (3, 'p', 'The hidden rule: they’re <b>tables</b>. You can turn a table round, but you can’t turn it upside down. So a mirror-image “J” isn’t allowed.')],
    steps=[
        f"""<p>Each table covers 4 squares: a bar of 3 with one square sticking out at the end. Here are all the ways one table can sit:</p>{_turns()}""",
        f"""<p>Split each arrangement (8 squares) into two tables:</p>{_arrangements()}
<ul><li>A, B, C and E each split into two L’s, just turned round. {tick()}</li>
<li>D: the end square on the left can only belong to “bar of 3 with a square on top of its <b>right</b> end”. That leaves “bar of 3 with a square on top of its <b>left</b> end”, which is the mirror image. {cross()}</li></ul>
{calc(f'impossible arrangement = {boxed("D")}')}
{note('In D, both tables would need their feet pointing towards each other. That only happens if one table is flipped over.', 'check')}""",
    ],
    answer_text='Arrangement D: it needs one table to be the mirror image of the other, which means turning a table upside down.',
    why={'A': 'A is one L plus the other L turned half way round: a 2 × 4 rectangle.',
         'B': 'B is two L’s each turned a quarter turn, stepped like stairs.',
         'C': 'C is one L as bought, plus one turned half way round.',
         'E': 'E is one L as bought (bottom) and one turned a quarter turn (top).'},
    fast='Tables can’t be flipped. Split each shape into two 4-square L’s: only D forces an L and a mirror-image J.',
))
