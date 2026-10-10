from wslib import *

Y = 2015
Q = []


# ---------------------------------------------------------------- 18 (Q37)
def _mulch():
    m = 8
    parts = [rect(40, 60, 10 * m, 5 * m, k='ink', fill='o', sw=2),
             rect(250, 30, 20 * m, 15 * m, k='ink', fill='o', sw=2)]
    lab = [text(40 + 5 * m, 52, '10 m × 5 m', k='ink', size=16),
           text(40 + 5 * m, 128, '50 m² × 0.05 m', k='pen', size=16),
           text(40 + 5 * m, 150, '= 2.5 m³', k='pen', size=18),
           text(250 + 10 * m, 22, '15 m × 20 m', k='ink', size=16),
           text(250 + 10 * m, 90, '300 m² × 0.1 m', k='pen', size=16),
           text(250 + 10 * m, 114, '= 30 m³', k='pen', size=18),
           text(480, 70, '2.5 + 30 = 32.5 m³', k='ink', size=17, anchor='start'),
           text(480, 96, '× 0.65 t', k='ink', size=17, anchor='start'),
           text(480, 122, '= 21.125 t', k='red', size=19, anchor='start')]
    for i in range(22):
        r, c = divmod(i, 11)
        x, y = 40 + c * 52, 200 + r * 46
        parts.append(rect(x, y, 38, 36, k='ink', fill='paper', sw=1.6, rx=6))
        if i < 21:
            parts.append(rect(x + 3, y + 3, 32, 30, k='green', fill='g', sw=1, rx=4))
        else:
            parts.append(rect(x + 3, y + 29, 32, 4, k='green', fill='g', sw=1, rx=1))
    lab += [text(634, 300, '22nd bag: only 0.125 t,', k='red', size=15, anchor='end'),
            text(634, 318, 'but you still need it', k='red', size=15, anchor='end'),
            text(200, 316, '22 one-tonne bags', k='green', size=22, font='scrawl')]
    return svg(640, 330, rough(*parts) + ''.join(lab),
               'The two plots with their mulch volumes, 2.5 and 30 cubic metres, then 22 bags where the last is barely used')

Q.append(dict(
    n=18, orig=37, answer='D', topic='Area, volume & mass',
    question=f"""<p>A gardener has to apply mulch to two plots of land, measuring {hl('10 metres by 5 metres', 'g', 1)} and {hl('15 metres by 20 metres', 'g', 1)}. The mulch has to be applied to a depth of {hl('50 mm for the first plot and 100 mm for the second plot', 'g', 2)}. The mulch weighs {hl('0.65 tonnes per cubic metre', 'y', 3)}.</p>
<p><b>AREA COVERAGE OF MULCH IN SQUARE METRES</b></p>
{table([['1', '40', hl('20', 'g'), '13', hl('10', 'g'), '8', '7'], ['2', '80', '40', '26', '20', '16', '14'],
        ['3', '120', '60', '39', '30', '24', '21'], ['4', '160', '80', '52', '40', '32', '28'],
        ['5', '200', '100', '65', '50', '40', '35'], ['6', '240', '120', '78', '60', '48', '42'],
        ['7', '280', '140', '91', '70', '56', '49'], ['8', '320', '160', '104', '80', '64', '56'],
        ['9', '360', '180', '117', '90', '72', '63'], ['10', '400', '200', '130', '100', '80', '70']],
       head=['Quantity in cubic metres', '25 mm depth', '50 mm depth', '75 mm depth', '100 mm depth', '125 mm depth', '150 mm depth'])}
<p class="stem">How many {hl('one-tonne bags', 'b', 4)} are necessary to complete the mulching of the two plots?</p>""",
    options={'A': '2', 'B': '13', 'C': '20', 'D': '22', 'E': '33'},
    notes=[(1, 'g', 'Areas: 10 × 5 = 50 m² and 15 × 20 = 300 m².'),
           (2, 'g', 'Each plot has its own depth. Don’t swap them! 50 mm = 0.05 m, 100 mm = 0.1 m.'),
           (3, 'y', 'Turns cubic metres into tonnes: × 0.65.'),
           (4, 'b', 'Whole bags only, so round <b>up</b>.')],
    steps=[
        f"""<p>Volume = area × depth (in metres):</p>
{calc('plot 1: 50 m² × 0.05 m = <b>2.5 m³</b>', 'plot 2: 300 m² × 0.1 m = <b>30 m³</b>', 'total = <b>32.5 m³</b>')}
{note('Same from the table: at 50 mm, 1 m³ covers 20 m², so 50 m² needs 2.5 m³. At 100 mm, 1 m³ covers 10 m², so 300 m² needs 30 m³.', 'check')}""",
        f"""<p>Weight, then bags:</p>
{calc('32.5 × 0.65 = 16.25 + 4.875 = <b>21.125 tonnes</b>', f'21.125 t {ar()} 21 bags is not enough {ar()} {boxed("22 bags")}')}
{note('32.5 × 0.65: half of 32.5 is 16.25, and 0.15 × 32.5 = 3.25 + 1.625 = 4.875.', 'tip')}
{_mulch()}""",
    ],
    answer_text='22 bags: 32.5 m³ × 0.65 = 21.125 tonnes, rounded up.',
    why={'A': '2 bags only covers the small plot (2.5 m³ × 0.65 ≈ 1.6 t).',
         'B': '13 swaps the depths: 100 mm on the small plot (5 m³) and 50 mm on the big one (15 m³) gives 20 m³ × 0.65 = 13.',
         'C': '20 only does the big plot: 30 m³ × 0.65 = 19.5, so 20 bags.',
         'E': '33 counts cubic metres as tonnes (32.5 m³ rounded up). It forgets the 0.65.'},
    fast='50 × 0.05 + 300 × 0.1 = 32.5 m³; × 0.65 = 21.1 t; round up to 22.',
))


# ---------------------------------------------------------------- 19 (Q38)
SEG = {'0': 'abcdef', '1': 'bc', '2': 'abged', '3': 'abgcd', '5': 'afgcd', '8': 'abcdefg', '9': 'abcdfg'}
FLIP = {'a': 'a', 'b': 'f', 'c': 'e', 'd': 'd', 'e': 'c', 'f': 'b', 'g': 'g'}


def _digit(x, y, segs, k, w=24, h=44):
    g = 4
    pos = {'a': (x + g, y, x + w - g, y), 'b': (x + w, y + g, x + w, y + h / 2 - g),
           'c': (x + w, y + h / 2 + g, x + w, y + h - g), 'd': (x + g, y + h, x + w - g, y + h),
           'e': (x, y + h / 2 + g, x, y + h - g), 'f': (x, y + g, x, y + h / 2 - g),
           'g': (x + g, y + h / 2, x + w - g, y + h / 2)}
    return [line(*pos[sg], k=k, w=4.5) for sg in segs]


def _display(x, y, digits, k, label, lk):
    """digits: list of segment strings (4 of them)."""
    parts = [rect(x, y, 196, 70, k='ink', fill='paper', sw=2)]
    xs = [x + 14, x + 52, x + 110, x + 148]
    for dx, segs in zip(xs, digits):
        parts += _digit(dx, y + 13, segs, k)
    parts += [circle(x + 95, y + 28, 2.5, k=k, fill='ink'), circle(x + 95, y + 44, 2.5, k=k, fill='ink')]
    return parts, [text(x + 98, y - 10, label, k=lk, size=16)]


def _mirror(t):
    return [''.join(FLIP[s] for s in SEG[c]) for c in reversed(t)]


def _clocks():
    parts, lab = [], []
    rows = [(40, 'last night', '22:05', 'what I saw (and set my watch to)', 'the real clock: 20:55'),
            (190, 'this morning', None, 'what I will see = E', 'real time: 08:59')]
    for y, name, seen, l1, l2 in rows:
        if seen:
            left = [SEG[c] for c in '2205']
            right = _mirror('2205')
        else:
            right = [SEG[c] for c in '0859']
            left = _mirror('0859')
        p1, t1 = _display(30, y, left, 'pen', l1, 'pen')
        p2, t2 = _display(400, y, right, 'ink', l2, 'ink')
        parts += p1 + p2
        lab += t1 + t2
        lab.append(text(320, y - 22, name, k='red', size=20, font='scrawl'))
    parts.append(line(318, 20, 318, 300, k='violet', w=2.4, dash=True))
    parts += [arrow(238, 75, 392, 75, k='violet', bend=-0.12), arrow(392, 225, 238, 225, k='violet', bend=-0.12)]
    lab += [text(318, 318, 'mirror: reverse the order AND flip each digit (2 ↔ 5, 0 and 8 stay)', k='violet', size=15)]
    return svg(620, 330, rough(*parts) + ''.join(lab),
               'Seven-segment displays: the 22:05 seen last night mirrors back to 20:55; this morning the real 08:59 mirrors to the display in option E')


def _street():
    parts = [rect(30, 60, 150, 220, k='ink', fill='paper', sw=2.2),
             rect(110, 100, 46, 40, k='pen', fill='b', sw=1.8),
             line(180, 280, 470, 280, k='muted', w=2),
             rect(470, 40, 120, 240, k='pen', fill='b', sw=2.2),
             rect(190, 200, 54, 28, k='ink', fill='paper', sw=1.8),
             line(217, 228, 217, 280, k='ink', w=2.4)]
    for yy in range(60, 280, 30):
        parts.append(line(470, yy, 590, yy - 14, k='pen', w=1, dash=False))
    parts += [arrow(246, 212, 468, 160, k='orange', bend=0.0, w=2.4),
              arrow(468, 154, 160, 124, k='orange', bend=0.0, w=2.4)]
    lab = [eye(133, 120, k='ink', facing='right'),
           text(105, 52, 'my hotel', k='ink', size=17),
           text(530, 30, 'glass building', k='pen', size=17),
           text(530, 300, '= a mirror', k='pen', size=17, font='scrawl'),
           text(217, 248, 'clock', k='ink', size=14),
           text(325, 300, 'road', k='muted', size=16),
           text(217, 192, 'faces the road', k='ink', size=14),
           text(330, 120, 'I only see its reflection', k='orange', size=17)]
    return svg(620, 316, rough(*parts) + ''.join(lab),
               'Street scene: the clock outside my hotel faces a glass building across the road; I see its reflection from my window')

Q.append(dict(
    n=19, orig=38, answer='E', topic='Reflections & clocks',
    question=f"""<p>I stayed in a hotel last night. My room was at the front of the building. At one point I looked out of
the window and saw:</p>
{fig(Y, 'ps_q19_clock', 'A digital display reading 22:05', 180)}
<p>on an illuminated digital clock on the other side of the road. I took the opportunity to {hl('reset my watch', 'p', 1)}, which had stopped sometime earlier.</p>
<p>This morning, when I looked out, I realised that what I could see across the road was a
{hl('reflection in the building opposite of a clock outside the hotel', 'y', 2)}. According to my watch ({hl('which I now knew I had reset incorrectly last night', 'p', 3)}) the time was supposedly {hl('nine minutes past ten', 'g', 4)}.</p>
<p class="stem">{hl('What did I see', 'b', 5)} across the road when I looked out this morning?</p>
{fig(Y, 'ps_q19_opts', 'Five digital displays A to E made of seven-segment digits', 420)}""",
    options={'A': 'display A', 'B': 'display B', 'C': 'display C', 'D': 'display D', 'E': 'display E'},
    notes=[(1, 'p', 'He set his watch to 22:05, exactly what he saw. But that was a mirror image!'),
           (2, 'y', 'A reflection reverses left and right: the digit order flips and every digit is drawn back to front.'),
           (3, 'p', 'So the watch is wrong by a fixed amount. Find it from last night.'),
           (4, 'g', 'Watch says 10:09.'),
           (5, 'b', 'He still sees the reflection, so the answer is a mirror image.')],
    steps=[
        f"""<p>Picture the street:</p>{_street()}""",
        f"""<p>Last night: 22:05 was a reflection. Flip it back: reverse the order and flip each digit (in a mirror a 2 looks like a 5 and a 5 like a 2):</p>
{calc(f'seen 22:05 {ar()} real clock <b>20:55</b>', f'watch set to 22:05 {ar()} watch is <b>1 h 10 min fast</b>')}""",
        f"""<p>This morning:</p>
{calc(f'watch 10:09 − 1 h 10 min = real time <b>08:59</b>')}
<p>Now mirror 08:59: the order becomes 9, 5, 8, 0 and each digit flips (9 back to front, 5 becomes a 2-shape, 8 and 0 unchanged).</p>
{_clocks()}
{calc(f'that is display {boxed("E")}')}""",
    ],
    answer_text='Display E: the mirror image of 08:59.',
    why={'A': 'A flips the 9 but forgets to flip the 5 (in a mirror it looks like a 2). Read back, A says 08:29.',
         'B': 'Read back in a mirror, B says 09:02, not 08:59.',
         'C': 'Read back, C says 09:29: wrong hour, and the 5 is not flipped.',
         'D': 'Read back, D says 09:32.'},
    fast='Mirror 22:05 → real 20:55, so the watch is 70 min fast. 10:09 − 1:10 = 08:59. Mirror 08:59: reversed order, 5 becomes a 2-shape: E.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _combos():
    combos = ['123', '124', '125', '134', '135', '145', '234', '235', '245', '345']
    bad = {'145': '4 and 5', '245': '4 and 5', '345': 'no 1 or 2, and 4 and 5'}
    parts, lab = [], []
    for i, c in enumerate(combos):
        r, col = divmod(i, 5)
        x, y = 20 + col * 118, 30 + r * 96
        isbad = c in bad
        parts.append(rect(x, y, 100, 46, k='red' if isbad else 'green', fill='p' if isbad else 'g', sw=2))
        lab.append(text(x + 50, y + 31, ' '.join(c), k='ink', size=22, font='print'))
        if isbad:
            parts.append(line(x + 6, y + 6, x + 94, y + 40, k='red', w=2.6))
            lab.append(text(x + 50, y + 66, bad[c], k='red', size=15))
    lab.append(text(310, 240, '10 − 3 = 7 allowed', k='green', size=24, font='scrawl'))
    return svg(620, 254, rough(*parts) + ''.join(lab),
               'All ten ways to pick three of five questions; 1 4 5, 2 4 5 and 3 4 5 are crossed out, leaving seven')

Q.append(dict(
    n=20, orig=42, answer='C', topic='Counting',
    question=f"""<p>An examination contains five questions. Candidates are instructed to {hl('answer three questions only', 'g', 1)}, including {hl('at least one of the first two', 'y', 2)} and {hl('no more than one of the last two', 'p', 3)}.</p>
<p class="stem">How many different combinations of questions are available for a candidate to choose from?</p>""",
    options={'A': '4', 'B': '6', 'C': '7', 'D': '8', 'E': '10'},
    notes=[(1, 'g', 'Exactly 3 out of questions 1 to 5. Order doesn’t matter.'),
           (2, 'y', 'Must include 1 or 2 (or both).'),
           (3, 'p', 'Can’t have <b>both</b> 4 and 5. One of them, or neither, is fine.')],
    steps=[
        f"""<p>Only 10 ways to choose 3 from 5, so just list them all and cross out the rule-breakers:</p>{_combos()}""",
        f"""{calc('no 1 or 2: only 3 4 5', 'both 4 and 5: 1 4 5, 2 4 5, 3 4 5',
      f'banned: 3 different sets (3 4 5 breaks both rules but only counts once)', f'10 − 3 = {boxed("7")}')}""",
    ],
    answer_text='7: 123, 124, 125, 134, 135, 234, 235.',
    why={'A': '4 reads both rules as “exactly one”: one of Q1/Q2, Q3, and one of Q4/Q5 (2 × 2 = 4).',
         'B': '6 takes away 1 + 3 = 4 sets, counting 3 4 5 twice.',
         'D': '8 only removes 1 4 5 and 2 4 5, and misses 3 4 5.',
         'E': '10 is every way of choosing 3 questions, with no rules applied.'},
    fast='List the 10 triples. Remove any with both 4 and 5 (145, 245, 345). 3 4 5 also has no 1 or 2, so it is already gone. 7 left.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _journeys():
    X = lambda t: 122 + (t - 9) * 53
    hm = lambda s: int(s[:2]) + int(s[3:]) / 60
    plans = [('A', [('09:00', '09:30', 'b'), ('09:30', '11:30', 'y'), ('11:30', '11:50', 'b'), ('11:50', '12:15', 'o')], 'can’t do it', True),
             ('B', [('10:00', '10:28', 'b'), ('10:28', '11:30', 'y'), ('11:30', '11:50', 'b'), ('11:50', '14:00', 'o'), ('14:00', '15:00', 'b')], '5 h 00', False),
             ('C', [('11:00', '11:30', 'b'), ('11:30', '12:45', 'y'), ('12:45', '13:05', 'b'), ('13:05', '15:20', 'o'), ('15:20', '16:12', 'b')], '5 h 12', False),
             ('D', [('12:00', '12:45', 'b'), ('12:45', '13:45', 'y'), ('13:45', '14:00', 'b'), ('14:00', '16:10', 'o'), ('16:10', '16:55', 'b')], '4 h 55', False),
             ('E', [('13:30', '13:45', 'b'), ('13:45', '14:45', 'y'), ('14:45', '15:05', 'b'), ('15:05', '17:00', 'o'), ('17:00', '18:15', 'b')], '4 h 45', False)]
    parts, lab = [], []
    for h in range(9, 19):
        parts.append(line(X(h), 34, X(h), 262, k='muted', w=1))
        lab.append(text(X(h), 282, f'{h}', k='muted', size=14))
    for i, (opt, segs, total, bad) in enumerate(plans):
        y = 44 + i * 44
        for a, b, f in segs:
            parts.append(rect(X(hm(a)), y, X(hm(b)) - X(hm(a)), 26, k='ink', fill=f, sw=1.4))
        best = opt == 'E'
        lab.append(text(8, y + 20, opt, k='ink', size=19, font='print', weight='700', anchor='start'))
        lab.append(text(112, y + 20, total, k='red' if bad else ('green' if best else 'ink'), size=17, anchor='end'))
        if bad:
            parts.append(line(X(12.25) + 4, y - 2, X(12.25) + 20, y + 28, k='red', w=2.6))
            parts.append(line(X(12.25) + 20, y - 2, X(12.25) + 4, y + 28, k='red', w=2.6))
            lab.append(text(X(12.25) + 26, y + 20, 'ready only at 13:20', k='red', size=15, anchor='start'))
    lab += [text(122, 20, 'blue = on a train, yellow = Tamworth, orange = Derby', k='muted', size=15, anchor='start'),
            text(X(13.75), 300, 'hour of the day', k='muted', size=14)]
    return svg(660, 310, rough(*parts) + ''.join(lab),
               'Timelines for the five options: A cannot catch the 12:15; B 5 hours, C 5 hours 12, D 4 hours 55, E 4 hours 45')

Q.append(dict(
    n=21, orig=43, answer='E', topic='Timetables',
    question=f"""<p>Hester is going for a job interview. She needs to travel by railway between Birmingham and
Derby, but she needs to {hl('stop off in Tamworth for an hour on the way out', 'y', 1)} to see her former
teacher for some coaching. When at Derby, she needs {hl('an hour and a half', 'y', 2)} to go to the
prospective employer to take an aptitude test. She can {hl('fix her appointments for any time in the day', 'g', 3)}. Naturally, she wants to make the journey in the most efficient way so that it {hl('takes the least possible time', 'b', 4)}.</p>
<p>This is the railway timetable:</p>
<p><b>Out:</b></p>
{table([['<b>Birmingham</b>', '09:00', '10:00', '11:00', '12:00', '13:00', '13:30', '14:30', '15:30'],
        ['<b>Tamworth</b>', '09:30', '10:28', '11:30', '12:45', hl('-', 'p', 5), '13:45', '14:45', '15:50'],
        ['<b>Derby</b>', '09:50', '10:40', '11:50', '13:05', '13:35', '14:00', '15:05', '16:00']],
       head=['Station', '', '', '', '', '', '', '', ''])}
<p><b>Return:</b></p>
{table([['<b>Derby</b>', '10:40', '11:10', '12:15', '13:10', '14:00', '15:20', '16:10', '17:00'],
        ['<b>Tamworth</b>', '11:05', '-', '12:35', '13:45', '-', '15:45', '16:35', '-'],
        ['<b>Birmingham</b>', '11:50', '11:55', '13:10', '14:15', '15:00', '16:12', '16:55', '18:15']],
       head=['Station', '', '', '', '', '', '', '', ''])}
<p class="stem">Which would be the best trains to catch from Birmingham and Derby?</p>""",
    options={'A': 'Leaving Birmingham 09:00; leaving Derby 12:15', 'B': 'Leaving Birmingham 10:00; leaving Derby 14:00',
             'C': 'Leaving Birmingham 11:00; leaving Derby 15:20', 'D': 'Leaving Birmingham 12:00; leaving Derby 16:10',
             'E': 'Leaving Birmingham 13:30; leaving Derby 17:00'},
    notes=[(1, 'y', 'At least 1 hour at Tamworth, then catch the <b>next</b> train on to Derby.'),
           (2, 'y', 'At least 1½ hours at Derby before the train home.'),
           (3, 'g', 'No fixed appointment times: only the train times matter.'),
           (4, 'b', 'Shortest time from leaving Birmingham to getting back to Birmingham.'),
           (5, 'p', 'A dash means the train doesn’t stop there. The 13:00 is no use for Tamworth.')],
    steps=[
        f"""<p>Follow each option: arrive Tamworth, add 1 hour, take the next train, arrive Derby, add 1½ hours, check the Derby train, get home.</p>
{calc(f'A: Tamworth 09:30 {ar()} 10:30, missed the 10:28, wait for 11:30 {ar()} Derby 11:50 {ar()} free at 13:20, can’t catch 12:15 ' + cross(),
      f'B: Tamworth 10:28 {ar()} 11:30 train {ar()} Derby 11:50 {ar()} 14:00 train {ar()} home 15:00 = 5 h 00',
      f'C: Tamworth 11:30 {ar()} 12:45 train {ar()} Derby 13:05 {ar()} 15:20 train {ar()} home 16:12 = 5 h 12',
      f'D: Tamworth 12:45 {ar()} 13:45 train {ar()} Derby 14:00 {ar()} 16:10 train {ar()} home 16:55 = 4 h 55',
      f'E: Tamworth 13:45 {ar()} 14:45 train {ar()} Derby 15:05 {ar()} 17:00 train {ar()} home 18:15 = <b>4 h 45</b>')}""",
        f"""{_journeys()}
{calc(f'shortest = 4 h 45 {ar()} {boxed("E")}')}
{note('E fits perfectly: she gets to Tamworth at 13:45 and the next train leaves at 14:45, exactly an hour later.', 'check')}""",
    ],
    answer_text='E: 13:30 out, 17:00 back, home at 18:15 after 4 h 45.',
    why={'A': 'A is impossible: she reaches Derby at 11:50 and needs 1½ hours, so she can’t catch the 12:15.',
         'B': 'B works but takes 5 hours (10:00 to 15:00).',
         'C': 'C works but takes 5 hours 12 minutes, the longest.',
         'D': 'D works and is close (4 h 55), but E is 10 minutes quicker.'},
    fast='Work out door-to-door time for each option: A impossible, B 5:00, C 5:12, D 4:55, E 4:45. Pick E.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _cube(cx, cy, s, top, left, right, three_on, verdict, vk, corner_note):
    L, N, R, F = (cx - 0.866 * s, cy - 0.5 * s), (cx, cy), (cx + 0.866 * s, cy - 0.5 * s), (cx, cy - s)
    down = lambda p: (p[0], p[1] + s)
    parts = [poly([L, N, R, F], k='ink', fill='paper', sw=2),
             poly([L, N, down(N), down(L)], k='ink', fill='paper', sw=2),
             poly([N, R, down(R), down(N)], k='ink', fill='paper', sw=2)]
    lab = []
    centres = {'top': (cx, cy - 0.5 * s + 9), 'left': (cx - 0.433 * s, cy + 0.25 * s + 9), 'right': (cx + 0.433 * s, cy + 0.25 * s + 9)}
    for face, num in (('top', top), ('left', left), ('right', right)):
        if face != three_on:
            lab.append(text(*centres[face], num, k='pen', size=28, font='print', weight='700'))
    if three_on == 'left':
        a, b = down(L), N
    else:
        a, b = N, F
    for t in (0.25, 0.5, 0.75):
        parts.append(circle(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, 5.5, k='ink', fill='ink', sw=1))
    parts.append(line(a[0], a[1], b[0], b[1], k='red', w=2, dash=True))
    parts.append(circle(N[0], N[1], 11, k=vk, sw=2.6))
    lab += [text(cx, cy + s + 34, verdict, k=vk, size=20),
            text(cx, cy + s + 56, corner_note, k=vk, size=15)]
    return parts, lab


def _dice():
    parts, lab = [], []
    for cx, args in ((110, ('1', '3', '5', 'left', 'the given die', 'green', 'line hits the 1–5 corner')),
                     (320, ('3', '2', '6', 'top', 'B ✓', 'green', 'line hits the 2–6 corner')),
                     (530, ('5', '3', '6', 'left', 'D ✗', 'red', 'line hits a 5–6 corner'))):
        p, l = _cube(cx, 110, 80, *args)
        parts += p
        lab += l
    return svg(640, 260, rough(*parts) + ''.join(lab),
               'Three dice: the given die with the line of three spots pointing at the corner shared with 1 and 5; B with it pointing at the 2 and 6 corner; D with it pointing at a 5 and 6 corner, which is wrong')

Q.append(dict(
    n=22, orig=44, answer='D', topic='Dice & 3D',
    question=f"""<p>The die shown below is a conventional die, i.e. {hl('the total number of spots on any two opposite faces is always seven', 'y', 1)}.</p>
{fig(Y, 'ps_q22_die', 'A die showing 1 on top, 3 on the left face (spots in a diagonal line) and 5 on the right face', 130)}
<p class="stem">Which one of the following {hl('could <b>not</b>', 'b', 2)} be the appearance of the die shown above {hl('after a subsequent throw', 'g', 3)}?</p>
{fig(Y, 'ps_q22_opts', 'Five dice A to E: A shows 2, 1, 4; B shows 3, 2, 6; C shows 4, 1, 5; D shows 5, 3, 6; E shows 6, 2, 4 (top, left, right)', 360)}""",
    options={'A': 'die A', 'B': 'die B', 'C': 'die C', 'D': 'die D', 'E': 'die E'},
    notes=[(1, 'y', 'Opposite pairs: 1–6, 2–5, 3–4. You never see both of a pair at once.'),
           (2, 'b', 'Four dice are the same die turned round. Find the one that can’t be.'),
           (3, 'g', 'Same die, any way up.')],
    steps=[
        f"""<p>Read each option as top / left / right:</p>
{calc('A 2, 1, 4 · B 3, 2, 6 · C 4, 1, 5 · D 5, 3, 6 · E 6, 2, 4')}
<p>None shows an opposite pair (1–6, 2–5, 3–4), so that quick test rules nothing out. Look for a finer clue.</p>""",
        f"""<p>The 1 and 5 look the same however you turn them. The <b>3 doesn’t</b>: its spots make a diagonal line that points at two corners.
On the given die the line runs into the top corner, where 3 meets <b>1 and 5</b>. Its other end is the hidden corner where 3 meets <b>2 and 6</b>.</p>
{calc('rule: the line of 3 always joins the 1–5 corner and the 2–6 corner')}""",
        f"""<p>Only B and D show a 3. Check where the line points:</p>{_dice()}
{calc(f'B: 3 on top, line runs to the front corner where it meets 2 and 6 {tick()}',
      f'D: 3 on the left, line runs to the top corner where it meets 5 and 6 {cross()} {ar()} {boxed("D")}')}
{note('A, C and E show no 3, and each is the die tipped over. For example C: roll the die so the 1 tips onto the left face; the 4 comes up on top and the 5 stays on the right.', 'check')}""",
    ],
    answer_text='Die D: its line of three spots points at the corner shared with 5 and 6, which can’t happen on this die.',
    why={'A': 'A (2, 1, 4) is possible: it is the die tipped over twice, and with no 3 showing there is nothing to clash.',
         'B': 'B is possible: the line of 3 runs to the 2–6 corner, just like the hidden end of the line on the original.',
         'C': 'C (4, 1, 5) is the die rolled once so the 1 goes to the left face and 4 comes on top.',
         'E': 'E (6, 2, 4) is possible: no opposite pair and no 3 to check, and it is the die tipped over again.'},
    fast='Opposites don’t help. The 3’s diagonal must join the 1–5 and 2–6 corners. In D it hits the corner with 5 and 6: impossible.',
))


# ---------------------------------------------------------------- 23 (Q48)
def _stock():
    u = 30
    base = 290
    qs = [('Jan–Mar', 2, 5, 6), ('Apr–Jun', 1, 6, 7), ('Jul–Sep', 0, 5, 5), ('Oct–Dec', 0, 6, 6)]
    parts, lab = [], []
    parts.append(line(30, base - 6 * u, 620, base - 6 * u, k='red', w=1.8, dash=True))
    lab.append(text(618, base - 6 * u - 8, 'max 6,000', k='red', size=15, anchor='end'))
    for i, (name, carry, deliv, use) in enumerate(qs):
        x = 40 + i * 130
        if carry:
            parts.append(rect(x, base - carry * u, 50, carry * u, k='ink', fill='paper', sw=1.6))
            lab.append(text(x + 25, base - carry * u / 2 + 6, f'{carry}k', k='muted', size=15))
        parts.append(rect(x, base - (carry + deliv) * u, 50, deliv * u, k='ink', fill='g', sw=1.6))
        lab.append(text(x + 25, base - carry * u - deliv * u / 2 + 6, f'+{deliv}k', k='green', size=17))
        parts.append(rect(x + 60, base - use * u, 30, use * u, k='ink', fill='o', sw=1.6))
        lab.append(text(x + 75, base - use * u - 8, f'{use}k', k='orange', size=16))
        lab.append(text(x + 45, base + 22, name, k='ink', size=16))
        left_ = carry + deliv - use
        lab.append(text(x + 45, base + 44, f'left {left_}k', k='pen', size=15))
    parts.append(line(30, base, 620, base, k='ink', w=2))
    lab.append(text(320, 24, 'green = delivered, white = carried over, orange = used', k='muted', size=15))
    return svg(640, 344, rough(*parts) + ''.join(lab),
               'Quarter by quarter: 2k carried plus 5k delivered covers 6k used with 1k left; then 1k plus 6k covers 7k; then 5k and 6k; nothing left at the end')

Q.append(dict(
    n=23, orig=48, answer='A', topic='Stock planning',
    question=f"""<p>Deliveries of containers for a fast-food takeaway are made {hl('only four times per year, at the beginning of January, April, July and October', 'y', 1)}. Last year the takeaway over-ordered containers
and {hl('currently has 2,000 left', 'g', 2)}. The number of containers used per month varies, but is no more
than 3,000 and no fewer than 1,000. {hl('The maximum number that can be delivered at one time is 6,000', 'p', 3)}. The usage for last year is illustrated below.</p>
{fig(Y, 'ps_q23_chart', 'Bar chart of containers used each month in thousands: J 2, F 3, M 1, A 3, M 2, J 2, J 1, A 1, S 3, O 1, N 2, D 3', 440)}
<p class="stem">{hl('Assuming the same usage this year', 'y', 4)}, how many containers need to be delivered each quarter
(in January, April, July and October) in order for {hl('over-ordering to be minimised', 'b', 5)}?</p>""",
    options={'A': '5,000 in January, 6,000 in April, 5,000 in July, 6,000 in October',
             'B': '6,000 in January, 7,000 in April, 5,000 in July, 6,000 in October',
             'C': '4,000 in January, 7,000 in April, 5,000 in July, 6,000 in October',
             'D': '6,000 in January, 6,000 in April, 6,000 in July, 6,000 in October',
             'E': '4,000 in January, 6,000 in April, 6,000 in July, 6,000 in October'},
    notes=[(1, 'y', 'Each delivery must last for the next 3 months.'),
           (2, 'g', 'Already 2,000 in stock at the start of January.'),
           (3, 'p', 'No delivery can be bigger than 6,000. Any option with 7,000 is out.'),
           (4, 'y', 'Use last year’s bars month by month.'),
           (5, 'b', 'Never run out, but finish with as few spare as possible.')],
    steps=[
        f"""<p>Add up each quarter (in thousands):</p>
{calc('Jan–Mar: 2 + 3 + 1 = 6', 'Apr–Jun: 3 + 2 + 2 = <b>7</b>', 'Jul–Sep: 1 + 1 + 3 = 5', 'Oct–Dec: 1 + 2 + 3 = 6',
      'year: 24 needed, 2 already in stock, so 22 to deliver')}""",
        f"""<p>The catch: April–June needs 7,000 but a delivery can only be 6,000. So 1,000 must be <b>left over</b> from January.</p>
{calc(f'January: need 6 + 1 spare = 7, have 2 {ar()} deliver <b>5,000</b>',
      f'April: 1 left + 6 = 7 {ar()} deliver <b>6,000</b>',
      f'July: deliver <b>5,000</b> · October: deliver <b>6,000</b>',
      'total 22,000, nothing left at the end ' + tick())}
{_stock()}
{calc(f'answer = {boxed("A")}')}""",
    ],
    answer_text='A: 5,000, 6,000, 5,000, 6,000, with 1,000 carried from the first quarter into the second.',
    why={'B': 'B needs a 7,000 delivery in April, over the 6,000 maximum, and over-orders by 2,000.',
         'C': 'C delivers exactly what each quarter needs (4, 7, 5, 6), but 7,000 in April breaks the 6,000 limit.',
         'D': 'D never runs out but delivers 24,000 on top of the 2,000 in stock: 2,000 over-ordered.',
         'E': 'E runs out in June: January leaves nothing spare, and 6,000 can’t cover April–June’s 7,000.'},
    fast='Quarters need 6, 7, 5, 6 (thousand). Max 6 per delivery, so carry 1 from Q1: deliver 5, 6, 5, 6. Only A.',
))


# ---------------------------------------------------------------- 24 (Q49)
def _stamp_line():
    made = {56: '56', 57: '56+1', 58: '56+2', 59: '50+9', 60: '50+10', 61: '61', 62: '62', 63: '62+1',
            64: '62+2', 65: '56+9', 66: '56+10', 67: '62+5', 68: '?'}
    X = lambda v: 40 + (v - 56) * 46
    parts = [line(X(56) - 16, 100, X(68) + 20, 100, k='ink', w=2)]
    lab = []
    for v, how in made.items():
        parts.append(line(X(v), 94, X(v), 106, k='ink', w=1.6))
        bad = v == 68
        lab.append(text(X(v), 128, v, k='red' if bad else 'ink', size=16 if not bad else 20, weight='700' if bad else None))
        if not bad:
            yy = 76 if v % 2 == 0 else 54
            lab.append(text(X(v), yy, how, k='green', size=15))
    parts.append(circle(X(68), 122, 18, k='red', sw=2.6))
    lab += [text(X(68), 64, 'no pair', k='red', size=16),
            text(X(68), 84, 'works!', k='red', size=16),
            text(X(62), 170, 'green = made with 1 or 2 stamps', k='green', size=16),
            text(X(62), 196, '68 needs three, e.g. 56 + 10 + 2', k='red', size=19, font='scrawl')]
    return svg(640, 210, rough(*parts) + ''.join(lab),
               'Number line 56 to 68: every value up to 67 can be made with one or two stamps; 68 cannot')

Q.append(dict(
    n=24, orig=49, answer='C', topic='Making amounts',
    question=f"""<p>The table below shows the available denominations of British stamps in 2009:</p>
{table([['1p', '1p', 'Make up value'], ['2p', '2p', 'Make up value'], ['5p', '5p', 'Make up value'], ['9p', '9p', 'Make up value'],
        ['10p', '10p', 'Make up value'], ['17p', '17p', 'Make up value'], ['20p', '20p', 'Make up value'], ['22p', '22p', 'Make up value'],
        ['2nd', hl('30p', 'g'), '2nd Class (UK) standard letter rate'], ['1st', hl('39p', 'g'), '1st Class (UK) standard letter rate'],
        ['Large 2nd', hl('47p', 'g'), '2nd Class (UK) standard letter rate'], ['50p', '50p', 'Make up value'],
        ['54p', '54p', 'Worldwide basic (20 g) surface rate'], ['56p', '56p', 'European basic (20 g)'],
        ['Large 1st', hl('61p', 'g'), '1st Class (UK) standard letter rate'], ['Postcard', hl('62p', 'g'), 'World postcard rate'],
        ['62p', '62p', 'Airmail']],
       head=['Stamp', 'Value', hl('Usual Purpose', 'p', 3)])}
<p class="stem">What is the {hl('lowest amount above 55p', 'b', 1)} which {hl('must be made up with at least three stamps', 'y', 2)}?</p>""",
    options={'A': '58p', 'B': '65p', 'C': '68p', 'D': '75p', 'E': '79p'},
    notes=[(1, 'b', 'Start at 56p and go up. The first one that fits wins.'),
           (2, 'y', '“Must” = it is impossible with one or two stamps.'),
           (3, 'p', 'Ignore the purpose column. A “2nd” stamp is just a 30p stamp, “Large 1st” a 61p, and so on.')],
    steps=[
        f"""<p>The values available: 1, 2, 5, 9, 10, 17, 20, 22, 30, 39, 47, 50, 54, 56, 61, 62.</p>
<p>Fastest: test the options from the smallest. Can it be made with two stamps?</p>
{calc(f'58 = 56 + 2 {ar()} two stamps ' + cross(), f'65 = 56 + 9 {ar()} two stamps ' + cross())}""",
        f"""<p>68: try taking off each big stamp and see if the rest is one stamp:</p>
{calc('68 − 62 = 6 · 68 − 61 = 7 · 68 − 56 = 12 · 68 − 54 = 14', '68 − 50 = 18 · 68 − 47 = 21 · 68 − 39 = 29 · 68 − 30 = 38',
      f'none of these is a stamp {ar()} 68 needs <b>three</b> stamps {tick()}')}
{note('Pairs of two small stamps can’t reach 68 (the biggest small pair is 22 + 22 = 44), so checking the big stamps covers everything.', 'check')}""",
        f"""<p>And every amount from 56 to 67 does work with one or two stamps:</p>{_stamp_line()}
{calc(f'lowest = {boxed("68p")}')}""",
    ],
    answer_text='68p: no two stamps make 68p, and every amount from 56p to 67p can be made with one or two.',
    why={'A': '58p = 56p + 2p: only two stamps needed.',
         'B': '65p = 56p + 9p: two stamps.',
         'D': '75p does need three stamps, but 68p is lower.',
         'E': '79p = 62p + 17p: two stamps.'},
    fast='Test options upward: 58 = 56 + 2, 65 = 56 + 9, 68 − each big stamp gives 6, 7, 12, 14, 18, 21, 29, 38, none a stamp. 68.',
))


# ---------------------------------------------------------------- 25 (Q50)
def _fields():
    T = {1: (250, 150), 2: (370, 150), 3: (370, 30), 4: (250, 30)}
    parts = [rect(235, 15, 150, 150, k='ink', fill='paper', sw=2),
             rect(90, 165, 440, 175, k='ink', fill='g', sw=2)]
    parts += [line(250, 150, 250, 340, k='red', w=2, dash=True), line(370, 150, 370, 340, k='red', w=2, dash=True),
              line(250, 150, 90, 310, k='violet', w=2, dash=True), line(370, 150, 530, 310, k='violet', w=2, dash=True),
              line(370, 30, 250, 150, k='violet', w=1.4, dash=True), line(250, 30, 370, 150, k='violet', w=1.4, dash=True)]
    lab = []
    for n, (x, y) in T.items():
        parts.append(circle(x, y, 9, k='ink', fill='y', sw=2))
        lab.append(text(x, y + 5, n, k='ink', size=13, font='print', weight='700'))
    lab += [text(310, 130, 'field X', k='muted', size=16), text(100, 334, 'field Y', k='green', size=16, anchor='start'),
            text(310, 262, '1 4 3 2', k='ink', size=20, font='print'),
            text(160, 196, '4 3 1 2', k='ink', size=19, font='print'),
            text(170, 300, '4 1 3 2', k='ink', size=19, font='print'),
            text(460, 196, '1 2 4 3', k='ink', size=19, font='print'),
            text(450, 300, '1 4 2 3', k='ink', size=19, font='print'),
            text(310, 362, 'red: lines through two side trees; violet: diagonals carried on into Y', k='muted', size=14)]
    return svg(620, 372, rough(*parts) + ''.join(lab),
               'Plan of field X above field Y; the side lines and the two diagonals cut field Y into five regions, each with its own left-to-right order')

Q.append(dict(
    n=25, orig=50, answer='E', topic='Spatial reasoning',
    question=f"""<p>Four trees stand at the {hl('corners of square field X', 'y', 1)}. They are photographed {hl('from field Y', 'y', 2)}, from
{hl('every possible direction, close up and from a distance', 'g', 3)}, but {hl('never so that one tree stands in front of another', 'p', 4)}.</p>
{fig(Y, 'ps_q25_fields', 'Square field X with trees 4 and 3 at the top corners and trees 1 and 2 at the bottom corners, sitting on top of a wide field Y', 300)}
<p class="stem">In how many {hl('different orders, left to right', 'b', 5)}, can the trees appear in the photographs?</p>""",
    options={'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'},
    notes=[(1, 'y', 'Trees 1 and 2 are nearest field Y; 4 and 3 are behind them.'),
           (2, 'y', 'The photographer is always somewhere in field Y, below the square.'),
           (3, 'g', 'Moving sideways <b>and</b> moving nearer or further can both change the order.'),
           (4, 'p', 'The order only changes at the exact moment two trees line up. Those lines are the borders between different orders.'),
           (5, 'b', 'Count the regions of field Y with different orders.')],
    steps=[
        f"""<p>Key idea: as you walk around, two trees swap places in the photo only when you cross the straight line through them.
So draw every line through two trees and see which ones run into field Y.</p>
<ul><li>1–2 (front row) and 4–3 (back row): run sideways, never enter Y.</li>
<li>1–4 and 2–3 (the sides): run straight down into Y.</li>
<li>3–1 and 4–2 (the diagonals): carry on down into Y, out to the left and right.</li></ul>""",
        f"""<p>Those four lines cut field Y into 5 regions. Each region gives its own order:</p>{_fields()}
{calc('straight in front: 1 4 3 2', 'left, close: 4 3 1 2 · left, further back: 4 1 3 2',
      'right, close: 1 2 4 3 · right, further back: 1 4 2 3', f'number of orders = {boxed("5")}')}
{note('Check the middle: stand in front, between the two side lines. Tree 1 is on your far left, 2 on your far right, and the back trees 4 and 3 appear in between.', 'check')}""",
    ],
    answer_text='5 orders: one straight in front, two on the left and two on the right.',
    why={'A': '1 assumes you always see 1 4 3 2, as from straight in front. Walking to the side changes it.',
         'B': '2 would be just “left side” and “right side”, missing the view from the front and the diagonal swaps.',
         'C': '3 only uses the side lines (left, middle, right) and forgets the diagonals, which matter “from a distance”.',
         'D': '4 misses one region, usually the middle view or one of the diagonal swaps.'},
    fast='Order changes only when you cross a line through two trees. Side lines (2) and diagonals (2) enter field Y, cutting it into 5 regions: 5 orders.',
))
