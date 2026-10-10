from wslib import *

Y = 2008
Q = []


# ---------------------------------------------------------------- 18 (Q37)
def _grid(x0, y0, cols, rows, c, fill_of):
    out = []
    for r in range(rows):
        for q in range(cols):
            f = fill_of(r, q)
            if f:
                out.append(rect(x0 + q * c, y0 + r * c, c, c, k='ink', fill=f, sw=1.6))
    return out


def _pens():
    parts = []
    parts += _grid(30, 50, 4, 4, 30, lambda r, q: 'p' if r in (1, 2) and q in (1, 2) else 'g')
    parts += _grid(210, 50, 8, 2, 30, lambda r, q: 'g')
    parts += _grid(480, 40, 5, 5, 22, lambda r, q: None if 0 < r < 4 and 0 < q < 4 else 'g')
    parts += _grid(210, 196, 16, 1, 24, lambda r, q: 'g')
    lab = [text(90, 192, '4 × 4: 40 hurdles', k='ink', size=16),
           text(90, 212, 'but 4 pens trapped ✗', k='red', size=16),
           text(330, 134, '2 × 8: 42 hurdles ✓', k='green', size=19, font='scrawl'),
           text(330, 156, 'every pen touches the outside', k='ink', size=15),
           text(535, 170, 'ring: 48 hurdles', k='ink', size=16),
           text(402, 246, 'one long line: 49 hurdles', k='ink', size=16)]
    return svg(640, 262, rough(*parts) + ''.join(lab),
               'Four layouts of 16 pens: a 4 by 4 block with 4 trapped pens (40 hurdles), 2 rows of 8 (42), a hollow ring (48) and one long line (49)')

Q.append(dict(
    n=18, orig=37, answer='B', topic='Shapes & counting',
    question=f"""<p>Peter needs to separate his sheep into {hl('16 square pens', 'g', 1)}. {hl('Each side of a pen is formed by a free-standing barrier known as a hurdle', 'y', 2)}. {hl('Each pen must be individually accessible on at least one side', 'p', 3)} so that sheep can be penned or released without a risk of the others
escaping.</p>
<p class="stem">What is the {hl('smallest', 'b', 4)} number of hurdles that Peter must take out to the fields in order to
accomplish his task?</p>""",
    options={'A': '40', 'B': '42', 'C': '48', 'D': '49', 'E': '64'},
    notes=[(1, 'g', '16 pens × 4 sides = 64 sides, but two pens side by side can <b>share</b> a hurdle.'),
           (2, 'y', 'One hurdle per side of a pen.'),
           (3, 'p', 'Every pen must have a side on the <b>outside</b>. No pen can be boxed in by other pens.'),
           (4, 'b', 'Share as many hurdles as you can.')],
    steps=[
        f"""<p>Count sides: a shared hurdle does 2 sides, an outside hurdle does 1.</p>
{calc('16 × 4 = 64 sides', f'hurdles = (64 + outside hurdles) ÷ 2 {ar()} keep the outside short')}""",
        f"""<p>Try some layouts:</p>{_pens()}""",
        f"""<p>The 4 × 4 square is cheapest (40) but its middle 4 pens can’t be reached. Two rows of 8 keeps every pen on the edge:</p>
{calc('rows of hurdles: 3 lines × 8 = 24', 'columns of hurdles: 9 lines × 2 = 18', f'total = 24 + 18 = {boxed("42")}')}
{note('Could anything beat 42? It would need an outside of 18 hurdles or less. The only shapes that small are 3 × 6 or 4 × 5 blocks with a few pens missing, and they always leave pens boxed in the middle. So 42 is the best.', 'check')}""",
    ],
    answer_text='42 hurdles: two rows of 8 pens, so every pen has an outside side.',
    why={'A': '40 is the 4 × 4 square, but the four middle pens have no outside side.',
         'C': '48 is a hollow 5 × 5 ring of pens. Every pen is reachable, but the inside of the ring wastes hurdles.',
         'D': '49 is one long line of 16 pens (32 + 17). Fewer pens share sides.',
         'E': '64 gives every pen its own 4 hurdles, sharing nothing.'},
    fast='Every pen on the edge with the most sharing: 2 rows of 8. Hurdles: 3 × 8 + 9 × 2 = 24 + 18 = 42.',
))


# ---------------------------------------------------------------- 19 (Q38)
def _ribbon():
    ys = [40, 58, 76, 94]
    parts = [line(220, y, 420, y, k='pen', w=4) for y in ys]
    parts += [path('M420 58 A9 9 0 0 1 420 76', k='pen', sw=4),
              path('M420 40 A27 27 0 0 1 420 94', k='pen', sw=4),
              path('M220 40 A9 9 0 0 0 220 58', k='pen', sw=4),
              line(320, 26, 320, 108, k='red', w=2.6, dash=True)]
    lab = [text(320, 18, 'snip', k='red', size=16),
           text(470, 22, 'the snip hits', k='red', size=15, anchor='start')]
    for y, m in zip(ys, ('5 m', '3 m', '1 m', '7 m')):
        lab.append(text(470, y + 5, m, k='red', size=15, anchor='start'))
    lab += [text(206, 85, 'free ends', k='muted', size=14, anchor='end'),
            text(206, 101, '(0 m and 8 m)', k='muted', size=14, anchor='end')]
    extra = brace(220, 420, 112, 'folded: 2 m long, 4 layers', k='ink', size=15)
    X = lambda m: 40 + m * 70
    pieces = [(0, 1, 'o'), (1, 3, 'b'), (3, 5, 'b'), (5, 7, 'b'), (7, 8, 'o')]
    for a, b, f in pieces:
        parts.append(rect(X(a), 196, X(b) - X(a), 24, k='ink', fill=f, sw=1.6))
        lab.append(text((X(a) + X(b)) / 2, 214, f'{b - a} m', k='ink', size=15))
    for m in (2, 4, 6):
        parts.append(line(X(m), 184, X(m), 194, k='muted', w=1.6))
        parts.append(line(X(m), 222, X(m), 232, k='muted', w=1.6))
        lab.append(text(X(m), 178, 'fold', k='muted', size=14))
    for m in (1, 3, 5, 7):
        parts.append(line(X(m), 184, X(m), 232, k='red', w=3))
        lab.append(text(X(m), 178, 'cut', k='red', size=14))
    for m in range(9):
        lab.append(text(X(m), 250, m, k='muted', size=14))
    lab.append(text(320, 280, '5 pieces: three of 2 m and two of 1 m', k='green', size=19, font='scrawl'))
    return svg(640, 292, rough(*parts) + ''.join(lab) + extra,
               'The ribbon folded into four 2 m layers with the snip in the middle; opened out, the cuts are at 1, 3, 5 and 7 m, giving pieces of 1, 2, 2, 2 and 1 m')

Q.append(dict(
    n=19, orig=38, answer='C', topic='Folding',
    question=f"""<p>A piece of ribbon {hl('8m long', 'g', 1)} is {hl('folded in half', 'y', 2)} so the two ends are on top of each other. This
doubled 4m length is then {hl('folded in half again', 'y', 2)}. The folded, 2m length of ribbon is then {hl('cut right through at its midway point', 'p', 3)}.</p>
<p class="stem">How many cut pieces are there and what are their lengths?</p>""",
    options={'A': '8 pieces of ribbon each 1m long.', 'B': '6 pieces of ribbon, 2 of 2m long and 4 of 1m long.',
             'C': '5 pieces of ribbon, 3 of 2m long and 2 of 1m long.', 'D': '4 pieces of ribbon each 2m long.',
             'E': '3 pieces of ribbon one 4m long and 2 of 2m long.'},
    notes=[(1, 'g', 'Mark the ribbon from 0 m to 8 m.'),
           (2, 'y', 'Two folds: 4 layers, each 2 m long. The folds are at 2, 4 and 6 m on the ribbon.'),
           (3, 'p', 'One snip goes through all 4 layers, so 4 cuts in the ribbon. But the folds keep some bits joined!')],
    steps=[
        f"""<p>Each layer of the folded stack is a 2 m stretch of ribbon (0–2, 2–4, 4–6, 6–8). The snip is halfway along each one:</p>
{calc(f'midpoints: 1 m, 3 m, 5 m, 7 m {ar()} 4 cuts')}""",
        f"""{_ribbon()}""",
        f"""{calc('pieces: 0–1, 1–3, 3–5, 5–7, 7–8', f'= 1 m, 2 m, 2 m, 2 m, 1 m {ar()} {boxed("5 pieces: 3 of 2 m, 2 of 1 m")}')}
{note('4 cuts in a line always make 5 pieces, and the lengths must add to 8 m: 1 + 2 + 2 + 2 + 1 = 8.', 'check')}""",
    ],
    answer_text='5 pieces: the cuts land at 1, 3, 5 and 7 m, giving 1, 2, 2, 2 and 1 m.',
    why={'A': '8 pieces treats the 4 layers as separate strips. The folds keep pairs of 1 m bits joined into 2 m pieces.',
         'B': '6 pieces would need 5 cuts, but one snip through 4 layers makes only 4 cuts.',
         'D': '4 pieces of 2 m comes from cutting along the folds (2, 4, 6 m), not halfway along the folded length.',
         'E': '3 pieces would need only 2 cuts. The snip makes 4.'},
    fast='Folded layers are 0–2, 2–4, 4–6, 6–8; cut each in the middle: 1, 3, 5, 7. Pieces 1, 2, 2, 2, 1.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _stamps():
    parts, lab = [], []
    specs = [(20, '24c', ['6c'] * 4, '4 × 6c'), (230, '30c', ['30c'], '1 × 30c'),
             (440, '72c', ['30c', '30c', '6c', '6c'], '2 × 30c + 2 × 6c')]
    for x, post, stamps, sub in specs:
        parts += [rect(x, 40, 180, 110, k='ink', fill='paper', sw=2),
                  line(x + 90, 40, x + 90, 150, k='muted', w=2), line(x, 95, x + 180, 95, k='muted', w=2)]
        lab.append(text(x + 90, 30, f'parcel {post}', k='ink', size=17))
        x1 = x + 90 - (len(stamps) * 42 - 8) / 2
        for i, s in enumerate(stamps):
            parts.append(rect(x1 + i * 42, 75, 34, 40, k='ink', fill='y' if s == '6c' else 'b', sw=1.8))
            lab.append(text(x1 + i * 42 + 17, 100, s, k='ink', size=14))
        lab.append(text(x + 90, 174, sub, k='pen', size=16))
    lab += [text(320, 212, '6c stamps: 4 + 0 + 2 = 6', k='orange', size=18),
            text(320, 238, '30c stamps: 0 + 1 + 2 = 3', k='pen', size=18),
            text(320, 274, '6 : 3 = 2 : 1', k='green', size=28, font='scrawl')]
    return svg(640, 290, rough(*parts) + ''.join(lab),
               'Three parcels: 24c uses four 6c stamps, 30c uses one 30c stamp, 72c uses two 30c and two 6c; totals six 6c and three 30c')

Q.append(dict(
    n=20, orig=42, answer='C', topic='Best combination',
    question=f"""<p>A small mail order company sends out three sizes of parcel {hl('in about equal numbers', 'y', 1)} which
require postages of {hl('24c, 30c and 72c', 'g', 2)}. They stock stamps in denominations of {hl('6c and 30c', 'g', 3)}
and use the {hl('minimum number of stamps', 'p', 4)} on each parcel.</p>
<p class="stem">What proportion of the two denominations of stamps should the company buy?</p>""",
    options={'A': '1 x 6c for every 4 x 30c', 'B': '1 x 6c for every 1 x 30c', 'C': '2 x 6c for every 1 x 30c',
             'D': '5 x 6c for every 1 x 30c', 'E': '11 x 6c for every 2 x 30c'},
    notes=[(1, 'y', 'Equal numbers, so just count the stamps for <b>one of each</b> parcel.'),
           (2, 'g', 'The three postages.'),
           (3, 'g', 'Only two kinds of stamp.'),
           (4, 'p', 'Use a 30c stamp whenever one fits; 6c stamps only to make up the rest.')],
    steps=[
        f"""<p>Stamp each parcel with as few stamps as possible:</p>
{calc(f'24c: a 30c is too much {ar()} 4 × 6c', '30c: 1 × 30c',
      f'72c: 2 × 30c = 60c, then 12c more = 2 × 6c {ar()} 4 stamps')}""",
        f"""{_stamps()}
{calc(f'6c : 30c = 6 : 3 = {boxed("2 : 1")}')}""",
    ],
    answer_text='2 × 6c for every 1 × 30c: one set of parcels uses six 6c and three 30c stamps.',
    why={'A': '1 : 4 has far too few 6c stamps. The 24c parcel alone needs four of them.',
         'B': '1 : 1 counts <b>parcels</b> (two parcels use 6c stamps, two use 30c), not stamps.',
         'D': '5 : 1 would be 15 × 6c for every 3 × 30c, but one set of parcels needs only six 6c stamps.',
         'E': '11 : 2 uses 6c stamps where a 30c would do, e.g. 72c as 30c + seven 6c (8 stamps, not the minimum 4).'},
    fast='24 = 4 × 6, 30 = 1 × 30, 72 = 2 × 30 + 2 × 6. Count: six 6c, three 30c, so 2 : 1.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _draw():
    parts, lab = [], []
    qs = [(30, 'QF1: Scorpions v Archers', 'o'), (80, 'QF2: Bearers v Bulls', 'o'),
          (170, 'QF3: Scales v Rams', 'paper'), (220, 'QF4: Goats v Fish', 'g')]
    for y, s, f in qs:
        parts.append(rect(20, y, 250, 36, k='ink', fill=f, sw=1.6))
        lab.append(text(145, y + 24, s, k='ink', size=16))
    sc = [(48 + 98) / 2, (188 + 238) / 2]
    for i, (y, s, f) in enumerate(qs):
        parts.append(line(270, y + 18, 320, sc[i // 2], k='muted', w=1.8))
    for i, c in enumerate(sc):
        parts.append(rect(320, c - 17, 90, 34, k='ink', fill='y', sw=1.6))
        lab.append(text(365, c + 6, f'semi {i + 1}', k='ink', size=16))
    fc = (sc[0] + sc[1]) / 2
    parts += [line(410, sc[0], 460, fc, k='muted', w=1.8), line(410, sc[1], 460, fc, k='muted', w=1.8),
              rect(460, fc - 20, 100, 40, k='ink', fill='paper', sw=2)]
    lab += [text(510, fc + 6, 'FINAL', k='ink', size=17, font='print', weight='700'),
            text(425, 32, 'one of these four reaches', k='orange', size=15, anchor='start'),
            text(425, 50, 'the final from semi 1', k='orange', size=15, anchor='start'),
            text(425, 236, 'Goats meet Scales or', k='green', size=15, anchor='start'),
            text(425, 254, 'Rams in semi 2', k='green', size=15, anchor='start')]
    return svg(640, 270, rough(*parts) + ''.join(lab),
               'Knockout tree: QF1 Scorpions v Archers and QF2 Bearers v Bulls feed semi 1; QF3 Scales v Rams and QF4 Goats v Fish feed semi 2')

Q.append(dict(
    n=21, orig=43, answer='C', topic='Knockout draws',
    question=f"""<p>Every year the 12 local teams that compete for the Tipley and District Tiddlywinks Trophy
are split into two leagues for the purpose of {hl('eliminating four of the teams', 'p', 1)}, and sorting out
the pairings for the knockout stage of the competition. The table below shows how this is
done (QF is Quarter Final).</p>
{table([['1st QF', 'Winners League A v 4th place League B'], ['2nd QF', '3rd place League A v Runners-up League B'],
        ['3rd QF', 'Winners League B v 4th place League A'], ['4th QF', hl('3rd place League B v Runners-up League A', 'g', 2)],
        ['1st Semi-final', 'Winners of 1st QF v Winners of 2nd QF'], ['2nd Semi-final', hl('Winners of 3rd QF v Winners of 4th QF', 'y', 3)]])}
<p>This year's league stage has just been completed, with the following results.</p>
{table([['1st', 'The Scorpions', 'The Scales'], ['2nd', 'The Fish', 'The Bulls'], ['3rd', 'The Bearers', hl('The Goats', 'g', 4)],
        ['4th', 'The Rams', 'The Archers'], ['5th', 'The Crabs', 'The Maidens'], ['6th', 'The Lions', 'The Twins']],
       head=['', 'League A', 'League B'])}
<p>Despite having finished 3rd in their league, the reigning champions, The Goats are still
confident of reaching the final.</p>
<p class="stem">If The Goats are successful, what are the alternatives as to their {hl('prospective opponents in the final', 'b', 5)}?</p>""",
    options={'A': 'The Scorpions or The Fish or The Bearers or The Rams.',
             'B': 'The Archers or The Bulls or The Rams or The Fish.',
             'C': 'The Scorpions or The Archers or The Bearers or The Bulls.',
             'D': 'The Scorpions or The Archers or The Scales or The Rams.',
             'E': 'The Scorpions or The Twins or The Bearers or The Bulls.'},
    notes=[(1, 'p', '12 teams, 8 quarter-finalists: 5th and 6th in each league are out.'),
           (2, 'g', 'This is The Goats’ quarter final (3rd in League B), against The Fish.'),
           (3, 'y', 'So The Goats’ semi is against the 3rd QF winner. Their final opponent must come from the <b>other</b> semi.'),
           (4, 'g', 'The Goats: 3rd in League B.'),
           (5, 'b', 'Anyone who could win the 1st semi-final.')],
    steps=[
        f"""<p>Fill in the names, then follow The Goats:</p>
{calc('1st QF: Scorpions v Archers', '2nd QF: Bearers v Bulls', '3rd QF: Scales v Rams', '4th QF: <b>Goats</b> v Fish')}""",
        f"""{_draw()}""",
        f"""{calc(f'Goats: 4th QF {ar()} 2nd semi (v Scales or Rams) {ar()} final',
               f'final opponent = winner of 1st semi {ar()} Scorpions, Archers, Bearers or Bulls')}
{calc(f'answer = {boxed("C")}')}""",
    ],
    answer_text='The Scorpions, The Archers, The Bearers or The Bulls: the four teams in the other half of the draw.',
    why={'A': 'A lists League A’s top four, but The Fish (4th QF) and The Rams (3rd QF) are in The Goats’ own half.',
         'B': 'The Rams and The Fish are in The Goats’ half, so The Goats would have to beat them before the final.',
         'D': 'The Scales and The Rams play in the 3rd QF, whose winner meets The Goats in the semi-final, not the final.',
         'E': 'The Twins finished 6th, so they were knocked out. The Archers are the 4th team in that half.'},
    fast='Goats = 3rd in B → 4th QF → 2nd semi. Final opponent comes from semi 1 = QF1 + QF2 teams: Scorpions, Archers, Bearers, Bulls.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _carpets():
    u = 22
    parts = [rect(30, 60, 4 * u, 4 * u, k='ink', fill='b', sw=1.8), rect(30 + 4 * u, 60, 6 * u, 4 * u, k='ink', fill='o', sw=1.8),
             line(30 + 9 * u, 50, 30 + 9 * u, 60 + 4 * u + 10, k='red', w=2.6, dash=True)]
    for x1, x2 in ((40, 100), (130, 210)):
        for y in (82, 126):
            parts.append(arrow(x1, y, x2, y, k='muted', w=1.8))
    lab = [text(140, 40, 'end to end: 10 m × 4 m', k='ink', size=17),
           text(74, 108, '4 m', k='ink', size=15), text(30 + 7 * u, 108, '6 m', k='ink', size=15),
           text(22, 108, '4', k='ink', size=15, anchor='end'),
           text(30 + 9.5 * u, 172, 'trim', k='red', size=14),
           text(140, 196, 'trim 1 m: 9 m × 4 m', k='green', size=18),
           text(140, 218, 'the library ✓', k='green', size=20, font='scrawl')]
    ox = 380
    parts += [rect(ox, 60, 4 * u, 4 * u, k='ink', fill='b', sw=1.8), rect(ox, 60 + 4 * u, 6 * u, 4 * u, k='ink', fill='o', sw=1.8),
              rect(ox + 4 * u, 60, u, 4 * u, k='red', fill='p', sw=1.6)]
    for (x1, x2, y) in ((ox + 10, ox + 70, 82), (ox + 10, ox + 70, 126), (ox + 10, ox + 120, 170), (ox + 10, ox + 120, 214)):
        parts.append(arrow(x1, y, x2, y, k='muted', w=1.8))
    for a, b in (((ox, 54), (ox + 5 * u, 54)), ((ox + 5 * u, 54), (ox + 5 * u, 60 + 8 * u + 6))):
        parts.append(line(*a, *b, k='red', w=2.2, dash=True))
    lab += [text(ox + 70, 40, 'side by side: 8 m across', k='ink', size=17),
            text(ox + 4.5 * u, 112, 'gap', k='red', size=15, rotate=-90),
            text(ox + 6 * u + 14, 120, 'an 8 × 5 room', k='red', size=15, anchor='start'),
            text(ox + 6 * u + 14, 140, 'needs 5 m here,', k='red', size=15, anchor='start'),
            text(ox + 6 * u + 14, 160, 'the 4 m piece', k='red', size=15, anchor='start'),
            text(ox + 6 * u + 14, 180, 'falls short ✗', k='red', size=15, anchor='start'),
            text(320, 274, 'grey arrows = the pattern: it must run the same way in both pieces', k='muted', size=15)]
    return svg(640, 288, rough(*parts) + ''.join(lab),
               'Left: the 4 m and 6 m pieces end to end make 10 m by 4 m, trimmed to 9 by 4. Right: side by side they are 8 m across but the 4 m piece leaves a gap in an 8 by 5 room')

Q.append(dict(
    n=22, orig=44, answer='E', topic='Area & shape',
    question=f"""<p>Jess buys two lengths of carpet in the sales. The carpet is {hl('4m wide', 'g', 1)} and one of the
lengths purchased is {hl('4m long while the other is 6m', 'g', 2)}. There is a very pronounced pattern
which means that the pieces can {hl('only be joined so that the pattern runs the same way', 'p', 3)}. {hl('Jess will only accept one join', 'y', 4)}.</p>
<p class="stem">In which of Jess's rooms could the carpet be fitted?</p>
{fig(Y, 'ps_q22_rooms', 'Five rooms: A snooker room 8 by 6; B breakfast room 7 by 5; C dining room 6 by 6; D living room 8 by 5; E library 9 by 4', 420)}""",
    options={'A': 'Snooker room (8 × 6)', 'B': 'Breakfast room (7 × 5)', 'C': 'Dining room (6 × 6)',
             'D': 'Living room (8 × 5)', 'E': 'Library (9 × 4)'},
    notes=[(1, 'g', 'Both pieces are 4 m across.'),
           (2, 'g', 'So the pieces are 4 × 4 and 4 × 6: 40 m² in all.'),
           (3, 'p', 'You can’t turn one piece round 90° to make it fit.'),
           (4, 'y', 'Exactly two pieces in the room, joined along one straight seam.')],
    steps=[
        f"""<p>With one join and the pattern the same way, there are only two ways to put the pieces together:</p>{_carpets()}""",
        f"""<p>End to end covers up to 10 × 4. Side by side covers 8 across, but only 4 m along (the short piece). Either way,
<b>the room must have a side of 4 m or less</b>.</p>
{calc('A 8 × 6, B 7 × 5, C 6 × 6, D 8 × 5: no side of 4 m ' + cross(), f'E 9 × 4: two pieces end to end, trim 1 m {tick()} {ar()} {boxed("E")}')}
{note('Area alone fools you: D (8 × 5) is exactly 40 m², the same as the carpet. But the shape is wrong, so it needs a second join or a turned piece.', 'trap')}""",
    ],
    answer_text='The library (9 m × 4 m): the two pieces joined end to end make 10 m × 4 m, trimmed by 1 m.',
    why={'A': '8 × 6 = 48 m², more than the 40 m² of carpet Jess has.',
         'B': '7 × 5: neither side is 4 m or less, so it would need a turned piece or a second join.',
         'C': '6 × 6: same problem, no side is 4 m or less.',
         'D': '8 × 5 = 40 m², exactly the right area, but side by side the 4 m piece is 1 m too short for the 5 m side.'},
    fast='Both pieces are 4 m wide, so the room needs a 4 m side. Only the 9 × 4 library has one (4 + 6 = 10 ≥ 9).',
))


# ---------------------------------------------------------------- 23 (Q48)
def _prize():
    kgs = [80, 85, 90, 95, 100, 105, 110]
    incs = [0, 10, 15, 20, 25, 30, 35]
    base = 288
    parts, lab = [], []
    total = 100
    for i, (kg, inc) in enumerate(zip(kgs, incs)):
        x = 40 + i * 84
        parts.append(rect(x, base - 100, 56, 100, k='ink', fill='b', sw=1.4))
        h = 100
        for j, step in enumerate(incs[1:i + 1]):
            parts.append(rect(x, base - h - step, 56, step, k='ink', fill='o' if j % 2 == 0 else 'y', sw=1.4))
            h += step
        total = 100 + sum(incs[1:i + 1])
        lab.append(text(x + 28, base - h - 8, f'${total}', k='ink', size=16))
        if inc:
            lab.append(text(x + 28, base - h - 28, f'+{inc}', k='orange', size=16))
        lab.append(text(x + 28, base + 20, f'{kg} kg', k='muted', size=15))
    return svg(640, 318, rough(*parts) + ''.join(lab),
               'Staircase of prize money: 100 dollars at 80 kg, then plus 10, 15, 20, 25, 30 and 35 for each extra 5 kg, reaching 235 dollars at 110 kg')

Q.append(dict(
    n=23, orig=48, answer='C', topic='Number patterns',
    question=f"""<p>In a prize weight-lifting competition the winner receives {hl('$100 if he lifts 80kg', 'g', 1)}. He then
receives {hl('$10 for the next 5 additional kg, $15 for the second', 'y', 2)}, and the incremental prize
money {hl('increases by a further $5 for each additional unit of 5kg', 'y', 3)} he successfully lifts.</p>
<p>The winner of the competition lifts {hl('110kg', 'g', 4)}.</p>
<p class="stem">How much prize money does he receive?</p>""",
    options={'A': '$130', 'B': '$160', 'C': '$235', 'D': '$240', 'E': '$310'},
    notes=[(1, 'g', 'Start: $100 for the first 80 kg.'),
           (2, 'y', '85 kg earns +$10, then 90 kg earns another +$15.'),
           (3, 'y', 'Each 5 kg step pays $5 more than the step before: 10, 15, 20, …'),
           (4, 'g', '110 − 80 = 30 kg = 6 steps of 5 kg.')],
    steps=[
        f"""{calc(f'110 − 80 = 30 kg {ar()} 30 ÷ 5 = <b>6 steps</b>', 'steps pay: 10, 15, 20, 25, 30, 35')}""",
        f"""{_prize()}""",
        f"""{calc('10 + 15 + 20 + 25 + 30 + 35 = 135', f'total = 100 + 135 = {boxed("$235")}')}
{note('Pair them up: 10 + 35 = 45, 15 + 30 = 45, 20 + 25 = 45. Three pairs of 45 = 135.', 'tip')}""",
    ],
    answer_text='$235: $100 plus 10 + 15 + 20 + 25 + 30 + 35 = $135.',
    why={'A': '$130 = 100 + 6 × 5: it adds only the $5 rises, not the payments themselves.',
         'B': '$160 = 100 + 6 × 10: it forgets each payment grows by $5.',
         'D': '$240 is $5 too much: the six steps add to 135, not 140. Recheck the adding.',
         'E': '$310 = 100 + 6 × 35: it pays the top rate ($35) for every 5 kg.'},
    fast='6 steps: 10 + 15 + 20 + 25 + 30 + 35 = 3 × 45 = 135. Plus 100 = $235.',
))


# ---------------------------------------------------------------- 24 (Q49)
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def _row(name, vals, total):
    cells = [''] * 12
    for m, v in vals.items():
        cells[MONTHS.index(m)] = str(v)
    return [name] + cells + [str(total)]


def _q24_table():
    every = lambda v: {m: v for m in MONTHS}
    rows = [['<i>Expenses</i>'] + [''] * 13,
            _row(hl('Gas', 'y', 1), {'Jan': 125, 'Apr': 120, 'Jul': 80, 'Oct': 70}, 395),
            _row(hl('Electricity', 'y'), {'Feb': 160, 'May': 140, 'Aug': 80, 'Nov': 110}, 490),
            _row('Telephone', {'Mar': 80, 'Jun': 95, 'Sep': 110, 'Dec': 90}, 375),
            _row('Council Tax', every(60), 720),
            _row(hl('Coal', 'y'), {'Jun': 80, 'Dec': 85}, 165),
            _row('Road Tax', {'Oct': 125}, 125),
            _row('Car Insurance', {'Oct': 250}, 250),
            _row('Car Maintenance', {'Feb': 125, 'Aug': 155, 'Nov': 285}, 565),
            _row('TV Licence', {'Sep': 85}, 85),
            _row(hl('Logs for Fire', 'y'), {'Mar': 40, 'May': 40, 'Jul': 60}, 140),
            _row('House Maintenance', {'Mar': 55, 'Jun': 225, 'Nov': 128}, 408),
            _row('Disposable Items', every(10), 120),
            _row('Food', every(200), 2400),
            _row('Mortgage', every(320), 3840),
            _row('House Insurance', {'Jan': 240}, 240),
            [hl('<i>Total Expenses</i>', 'p', 2), '955', '875', '765', '710', '770', '990', '730', '825', '785', '1035', '1113', '765', '10318']]
    # same look as table(), but tighter so all 14 columns fit the slip
    pad = 'padding:2px 5px'
    head = ''.join(f'<th style="{pad}">{c}</th>' for c in [''] + MONTHS + ['Total'])
    body = ''
    for r in rows:
        body += ('<tr>' + f'<td style="{pad};text-align:left;white-space:nowrap">{r[0]}</td>'
                 + ''.join(f'<td style="{pad};text-align:right">{c}</td>' for c in r[1:]) + '</tr>')
    return (f'<div class="tbl-wrap"><table class="ptable" style="font-size:.78em">'
            f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')


def _energy():
    data = [('Jan', [(125, 'b')]), ('Feb', [(160, 'y')]), ('Apr', [(120, 'b')]),
            ('May', [(140, 'y'), (40, 'o')]), ('Jul', [(80, 'b'), (60, 'o')])]
    base = 236
    parts, lab = [line(30, base, 520, base, k='ink', w=2)], []
    for i, (m, segs) in enumerate(data):
        x, h = 50 + i * 95, 0
        for v, f in segs:
            parts.append(rect(x, base - h - v, 60, v, k='red' if m == 'May' else 'ink', fill=f, sw=2.6 if m == 'May' else 1.5))
            lab.append(text(x + 30, base - h - v / 2 + 5, v, k='ink', size=15))
            h += v
        lab.append(text(x + 30, base - h - 10, f'£{h}', k='red' if m == 'May' else 'ink', size=17))
        lab.append(text(x + 30, base + 20, m, k='muted', size=15))
    lab.append(text(x + 30 - 95, base - 180 - 30, 'highest ✓', k='red', size=18, font='scrawl'))
    for j, (name, f) in enumerate((('gas', 'b'), ('electricity', 'y'), ('logs', 'o'))):
        parts.append(rect(540, 60 + j * 30, 18, 18, k='ink', fill=f, sw=1.4))
        lab.append(text(564, 75 + j * 30, name, k='ink', size=15, anchor='start'))
    return svg(640, 266, rough(*parts) + ''.join(lab),
               'Energy spending in the five option months: January 125, February 160, April 120, May 140 plus 40 = 180, July 80 plus 60 = 140')

Q.append(dict(
    n=24, orig=49, answer='D', topic='Tables',
    question=f"""<p>The table below shows the expenses by month for a given household.</p>
{_q24_table()}
<p class="stem">In which month were the {hl('energy costs', 'b', 3)} highest?</p>""",
    options={'A': 'January', 'B': 'February', 'C': 'April', 'D': 'May', 'E': 'July'},
    notes=[(1, 'y', 'Energy rows: gas, electricity, coal and logs for the fire. Four rows to add.'),
           (2, 'p', 'Not this row! The total includes food, mortgage, insurance and so on.'),
           (3, 'b', 'Add only the energy rows, month by month.')],
    steps=[
        f"""<p>Pick out the energy rows (gas, electricity, coal, logs) for the five months on offer:</p>
{calc('Jan: gas 125 = <b>125</b>', 'Feb: electricity 160 = <b>160</b>', 'Apr: gas 120 = <b>120</b>',
      'May: electricity 140 + logs 40 = <b>180</b>', 'Jul: gas 80 + logs 60 = <b>140</b>')}""",
        f"""{_energy()}
{calc(f'highest = {boxed("May")} (£180)')}
{note('The coal months (June 80, December 85) are lower too, so May is highest in the whole year.', 'check')}""",
    ],
    answer_text='May: electricity 140 + logs 40 = 180.',
    why={'A': 'January has only gas (125). Its big total (955) comes from house insurance, food and the mortgage.',
         'B': 'February has the biggest single bill (electricity 160), but May’s two energy bills add to more.',
         'C': 'April has just 120 of gas.',
         'E': 'July: gas 80 + logs 60 = 140. Less than May’s 180.'},
    fast='Energy = gas + electricity + coal + logs. May: 140 + 40 = 180 beats February’s 160.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _boxes():
    c, x0, y0 = 56, 80, 40
    cells = {(1, 0): ('o', '≤4'), (0, 1): ('b', '≤2'), (1, 1): ('o', '≤4'), (2, 1): ('g', '3'),
             (0, 2): ('b', '≤2'), (1, 2): ('o', '≤4')}
    parts, lab = [], []
    for (q, r), (f, s) in cells.items():
        parts.append(rect(x0 + q * c, y0 + r * c, c, c, k='ink', fill=f, sw=1.8))
        lab.append(text(x0 + q * c + c / 2, y0 + r * c + c / 2 + 7, s, k='ink', size=19))
    for r, name in enumerate(('back', 'middle', 'front')):
        lab.append(text(x0 - 8, y0 + r * c + c / 2 + 5, name, k='muted', size=15, anchor='end'))
    sx, vy = x0 + 3 * c + 34, y0 + 3 * c + 30
    lab += [eye(sx, y0 + 1.5 * c, facing='left'), eye(x0 + 1.5 * c, vy, facing='up'),
            text(sx, y0 + 1.5 * c + 30, 'Sarah', k='ink', size=16),
            text(x0 + 1.5 * c + 24, vy + 6, 'Vinod', k='ink', size=16, anchor='start'),
            text(x0 + 1.5 * c, 22, 'from above, with heights', k='ink', size=15)]
    b, bx, base = 44, 390, 250
    for i, (name, solid) in enumerate((('front', 1), ('middle', 3), ('back', 1))):
        x = bx + i * b
        for j in range(4):
            y = base - (j + 1) * b
            if j < solid:
                parts.append(rect(x, y, b, b, k='ink', fill='g' if name == 'middle' else 'paper', sw=1.8))
            else:
                for (x1, y1, x2, y2) in ((x, y, x + b, y), (x, y, x, y + b), (x + b, y, x + b, y + b)):
                    parts.append(line(x1, y1, x2, y2, k='muted', w=1.4, dash=True))
        lab.append(text(x + b / 2, base + 18, name, k='muted', size=14))
    lab += [text(bx + 1.5 * b, 50, 'Sarah’s view, her left → right', k='ink', size=15),
            text(bx + 3 * b + 14, 150, 'middle ≥ 3', k='green', size=19, font='scrawl', anchor='start'),
            text(bx + 3 * b + 14, 174, '(the 3-high pile', k='green', size=15, anchor='start'),
            text(bx + 3 * b + 14, 192, 'is in that row)', k='green', size=15, anchor='start'),
            text(bx + 3 * b + 14, 228, 'D shows 2 ✗', k='red', size=19, font='scrawl', anchor='start')]
    return svg(680, 282, rough(*parts) + ''.join(lab),
               'Top view with heights: the left column at most 2, the middle column at most 4, the single right-hand pile exactly 3. Sarah looks along the rows, so her middle column must be at least 3 tall')

Q.append(dict(
    n=25, orig=50, answer='D', topic='3D views',
    question=f"""<p>Vinod and Sarah are about to move some {hl('cube-shaped boxes', 'y', 1)} that have been left in the
middle of a store room. The appearance of the boxes {hl('from above', 'y', 2)} and the positions of
Vinod and Sarah are shown below.</p>
{fig(Y, 'ps_q25_plan', 'Top view: six squares, one at the back middle, three in the middle row, two at the front left; Sarah on the right, Vinod at the front', 180)}
<p>{hl('Vinod sees this', 'g', 3)}:</p>
{fig(Y, 'ps_q25_vinod', 'Vinod’s view: three columns of boxes, 2 high on the left, 4 high in the middle and 3 high on the right', 90)}
<p class="stem">Which of the following {hl('<b>cannot</b>', 'b', 4)} be the view that Sarah sees?</p>
{fig(Y, 'ps_q25_opts', 'Five views: A columns 2, 4, 2; B 4, 3, 1; C 4, 3, 4; D 3, 2, 4; E 4, 4, 2', 400)}""",
    options={'A': 'view A', 'B': 'view B', 'C': 'view C', 'D': 'view D', 'E': 'view E'},
    notes=[(1, 'y', 'The boxes sit in piles. From the side you see the <b>tallest</b> pile in each line.'),
           (2, 'y', 'Six piles. Vinod looks along the columns; Sarah looks along the rows.'),
           (3, 'g', 'Vinod’s view, left to right: 2, 4, 3. That is the tallest pile in each of his columns.'),
           (4, 'b', 'Four views are possible; find the impossible one.')],
    steps=[
        f"""<p>Read Vinod’s view column by column (his left = the left of the plan):</p>
{calc('left column (2 piles): tallest is 2, so both are 2 or less', 'middle column (3 piles): tallest is 4',
      f'right column: only <b>one</b> pile {ar()} it is exactly <b>3</b> high')}""",
        f"""<p>Sarah looks along the rows. Her left is the front row (Vinod’s side), then the middle row, then the back box.
The single 3-high pile is in the <b>middle row</b>, so her middle column is at least 3 tall:</p>{_boxes()}""",
        f"""{calc(f'A 2, 4, 2 {tick()}', f'B 4, 3, 1 {tick()}', f'C 4, 3, 4 {tick()}',
               f'D 3, <b>2</b>, 4 {ar()} middle only 2 {cross()}', f'E 4, 4, 2 {tick()}')}
{calc(f'answer = {boxed("D")}')}
{note('Even if you mix up Sarah’s left and right, the middle column is still the middle row. D fails either way.', 'check')}""",
    ],
    answer_text='View D: its middle column is only 2 high, but that row contains the pile that is 3 high.',
    why={'A': 'A (2, 4, 2) works: the 4-pile in the middle row, the back pile 2, the front row 2.',
         'B': 'B (4, 3, 1) works: the 4-pile at the front, the middle row topped by the 3-pile, the back pile 1.',
         'C': 'C (4, 3, 4) works: 4-piles at the front and the back, the middle row’s tallest is the 3-pile.',
         'E': 'E (4, 4, 2) works: 4-piles in the front and middle rows, the back pile 2.'},
    fast='The lone right-hand pile is 3 high (Vinod) and sits in Sarah’s middle line, so her middle column is at least 3. D shows 2.',
))
