from wslib import *

Y = 2021
Q = []


# ---------------------------------------------------------------- 1 (Q2)
def _flashes():
    X = lambda t: 110 + t * 4.2
    rows = [('blue every 5 s', 5, 'pen', 62), ('green every 8 s', 8, 'green', 112), ('silver every 12 s', 12, 'violet', 162)]
    parts, lab = [], []
    for name, gap, col, y in rows:
        parts.append(line(X(0), y, X(120), y, k='muted', w=1.2))
        for t in range(0, 121, gap):
            parts.append(circle(X(t), y, 5.5, k=col, fill='paper' if t not in (0, 120) else 'y', sw=2.2))
        lab.append(text(96, y + 6, name, k=col, size=16, anchor='end'))
    parts.append(line(X(0), 202, X(124), 202, k='ink', head=True, w=1.8))
    for t in range(0, 121, 20):
        parts.append(line(X(t), 196, X(t), 208, k='ink', w=1.4))
        lab.append(text(X(t), 228, t, k='muted', size=14))
    lab.append(text(X(124) + 4, 228, 's', k='muted', size=14, anchor='start'))
    for t in (0, 120):
        parts.append(line(X(t), 36, X(t), 190, k='red', w=2.4, dash=True))
    lab += [text(X(0) + 6, 28, 'all flash', k='red', size=17, font='scrawl', anchor='start'),
            text(X(120) - 4, 28, 'all flash again!', k='red', size=17, font='scrawl', anchor='end'),
            text(X(60), 28, '60 s: no green', k='orange', size=16, font='scrawl'),
            text(X(60), 258, 'together every 120 s = 2 minutes', k='red', size=20, font='scrawl')]
    parts.append(line(X(60), 36, X(60), 172, k='orange', w=1.6, dash=True))
    return svg(650, 272, rough(*parts) + ''.join(lab),
               'Flash timeline from 0 to 120 seconds: blue every 5, green every 8, silver every 12; all three line up only at 0 and 120 seconds')

Q.append(dict(
    n=1, orig=2, answer='B', topic='LCM & repeating cycles',
    question=f"""<p>The fairy lights on a Christmas tree are in three colours, blue, green and silver. The blue lights
flash {hl('every 5 seconds', 'g', 1)}, the green lights flash {hl('every 8 seconds', 'g', 1)} and the silver lights flash every
{hl('12 seconds', 'g', 1)}. {hl('The lights have all just flashed at the same time', 'p', 2)}.</p>
<p class="stem">How many times will they {hl('all flash at the same time', 'y', 3)} {hl('in the next 45 minutes', 'b', 4)}?</p>""",
    options={'A': '5', 'B': '22', 'C': '45', 'D': '108', 'E': '112'},
    notes=[(1, 'g', 'Three different gaps: 5, 8 and 12 seconds.'),
           (2, 'p', 'That flash has already happened, so it is <b>not</b> one of the ones you count.'),
           (3, 'y', 'All three together = a time that 5, 8 and 12 all divide into: a <b>common multiple</b>.'),
           (4, 'b', '45 minutes. Work in minutes or seconds, but don’t mix them.')],
    steps=[
        f"""<p>All three flash together again after the <b>lowest common multiple</b> (LCM) of 5, 8 and 12.</p>
{calc('go up in 12s: 12, 24, 36, 48, 60, 72, 84, 96, 108, <b>120</b>',
      f'120 ÷ 8 = 15 {tick()} and 120 ÷ 5 = 24 {tick()}',
      f'so they all flash together every <b>120 s = 2 minutes</b>')}
{note('LCM trick: count up in the biggest number (12) and stop at the first one that the others divide. It must end in 0 because of the 5.', 'tip')}""",
        f"""<p>Picture the first 2 minutes. Lots of near misses, but all three only line up at 0 and 120 s:</p>{_flashes()}""",
        f"""<p>Now count the together-flashes in the next 45 minutes:</p>
{calc(f'one every 2 minutes {ar()} at 2, 4, 6, …, 44 minutes',
      f'45 ÷ 2 = 22.5 {ar()} only <b>22</b> whole ones fit',
      f'answer = {boxed("22")}')}
{note('The flash at 0 minutes has already happened, so don’t count it. The next one after 44 minutes is at 46 minutes, too late.', 'trap')}""",
    ],
    answer_text='22 times: they line up every 2 minutes, at 2, 4, … 44 minutes.',
    why={'A': '5 uses 5 × 8 × 12 = 480 s (8 minutes) as the gap: 45 ÷ 8 ≈ 5.6. That is <b>a</b> common multiple, but not the lowest one.',
         'C': '45 uses a gap of 60 s (5 × 12). But 60 is not a multiple of 8, so the green lights are not flashing then.',
         'D': '108 adds the gaps: 5 + 8 + 12 = 25 s, and 2700 ÷ 25 = 108. Adding gaps has nothing to do with when they line up.',
         'E': '112 uses 24 s, the LCM of 8 and 12 only, and forgets the blue lights: 2700 ÷ 24 = 112.5.'},
    fast='LCM of 5, 8, 12 = 120 s = 2 min. 45 ÷ 2 = 22.5, so 22 times.',
))


# ---------------------------------------------------------------- 2 (Q6)
def _alphabet():
    w, x0 = 23, 31
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    parts, lab = [], []
    for i, ch in enumerate(abc):
        x = x0 + i * w
        f = 'g' if ch == 'X' else 'y' if ch == 'S' else 'paper'
        parts.append(rect(x, 52, w, 30, k='ink', fill=f, sw=1.3))
        parts.append(rect(x, 132, w, 30, k='ink', fill=f, sw=1.3))
        lab.append(text(x + w / 2, 73, ch, k='ink', size=16, font='print'))
        lab.append(text(x + w / 2, 153, abc[(i + 12) % 26], k='pen', size=16, font='print'))
        lab.append(text(x + w / 2, 46, i + 1, k='muted', size=10))
    xi, si = abc.index('X'), abc.index('S')
    parts.append(arrow(x0 + xi * w + w / 2, 84, x0 + xi * w + w / 2, 128, k='green', bend=0))
    parts.append(arrow(x0 + si * w + w / 2, 128, x0 + si * w + w / 2, 86, k='red', bend=0))
    lab += [text(x0, 24, 'real message (plain)', k='ink', size=17, anchor='start'),
            text(x0, 190, 'coded letter (shift 12)', k='pen', size=17, anchor='start'),
            text(x0 + xi * w + w / 2, 216, 'X → J', k='green', size=18, font='scrawl'),
            text(x0 + si * w + w / 2, 216, 'E → back to S', k='red', size=18, font='scrawl')]
    return svg(660, 228, rough(*parts) + ''.join(lab),
               'Alphabet strip: each plain letter on top, its coded letter 12 places on underneath; X codes to J, and coded E comes from S')

Q.append(dict(
    n=2, orig=6, answer='D', topic='Codes & ciphers',
    question=f"""<p>I have received the following message that is encrypted with a Caesar cipher:</p>
<p><b>JYMDWEFTQEBAF</b></p>
<p>This Caesar cipher replaces each letter of the plaintext (the message to be encrypted) with a
letter that is {hl('a certain fixed number of positions along', 'y', 1)} the 26-letter English alphabet. Knowing
this fixed number of positions (the shift parameter) is the key to decrypt the message. For
example, if the letter in the plaintext is A (the 1st letter of the alphabet) and the shift parameter
is 4, then the encrypted letter is E (the 5th letter of the alphabet). Similarly, with a shift
parameter of 7, Y (the 25th letter of the alphabet) is encrypted as F, which is the 32nd letter if
{hl('the alphabet is repeated immediately after Z', 'p', 2)}.</p>
<p>I would like to decrypt the message that I have received but I do not know the shift parameter. I
only know that {hl('the first letter of the plaintext is X', 'g', 3)}.</p>
<p class="stem">What is the {hl('sixth letter', 'b', 4)} of the decrypted message?</p>""",
    options={'A': 'P', 'B': 'Q', 'C': 'R', 'D': 'S', 'E': 'T'},
    notes=[(1, 'y', 'Every letter moves forward by the same amount. Find that amount once and use it for every letter.'),
           (2, 'p', 'Wrap-around! After Z you go back to A. So counting can go past 26.'),
           (3, 'g', 'The coded message starts with J, so plain X became J. That gives the shift.'),
           (4, 'b', 'Count carefully: J Y M D W <b>E</b>. The 6th coded letter is E.')],
    steps=[
        f"""<p>Find the shift: X turned into J.</p>
{calc('X is letter 24, J is letter 10',
      f'X → Y → Z is 2 steps, then A … J is 10 more {ar()} shift = <b>12</b>',
      f'check: 24 + 12 = 36, and 36 − 26 = 10 = J {tick()}')}""",
        f"""<p>To decrypt, go <b>back</b> 12. The 6th coded letter is E (letter 5):</p>
{calc(f'5 − 12 = −7 {ar()} wrap round: −7 + 26 = 19', f'letter 19 = {boxed("S")}')}
{note('Going back 12 is the same as going forward 14 (because 12 + 14 = 26). Use whichever you find easier.', 'tip')}""",
        f"""<p>See it on a strip: top row is the real letter, bottom row is what it turns into.</p>{_alphabet()}""",
        f"""<p>Check by decoding the whole message:</p>
{table([['J', 'Y', 'M', 'D', 'W', hl('E', 'y'), 'F', 'T', 'Q', 'E', 'B', 'A', 'F'],
        ['X', 'M', 'A', 'R', 'K', hl('<b>S</b>', 'y'), 'T', 'H', 'E', 'S', 'P', 'O', 'T']],
       head=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])}
<p>X MARKS THE SPOT. It makes sense, so the shift is right.</p>""",
    ],
    answer_text='S: the shift is 12, and E goes back 12 places to S (“X MARKS THE SPOT”).',
    why={'A': 'P needs a shift of 15. That only comes from miscounting the X to J gap by 3. (P is also the 11th letter, not the 6th.)',
         'B': 'Q moves E 12 places <b>forward</b>, which codes it again instead of decoding it.',
         'C': 'R uses a shift of 13: an off-by-one when counting from X round to J. (R is also the 4th letter of the message.)',
         'E': 'T uses a shift of 11 (off by one the other way). It is also what you get by decoding the 7th letter, F, by mistake.'},
    fast='X → J is +12. Sixth coded letter E (5): 5 − 12 + 26 = 19 = S.',
))


# ---------------------------------------------------------------- 3 (Q7)
def _masks():
    needs = ['size: children', 'size: adult', 'dust and pollen', 'hypoallergenic', 'urban', 'rural']
    masks = ['Air-1', 'GXi', 'Optiair', 'Speed', 'Breathe']
    grid = ['YNYNY', 'YYYYY', 'YNYYY', 'YYNYY', 'NYYNY', 'YNYYY']
    x0, y0, cw, rh = 214, 58, 86, 32
    parts, lab = [], []
    for j, m in enumerate(masks):
        ok = all(grid[i][j] == 'Y' for i in range(len(needs)))
        lab.append(text(x0 + j * cw + cw / 2, 46, m, k='green' if ok else 'ink', size=17, weight='700' if ok else None))
        if ok:
            parts.append(rect(x0 + j * cw + 3, 26, cw - 6, rh * len(needs) + 40, k='green', fill='g', sw=2.6, rx=8))
    for i, nd in enumerate(needs):
        y = y0 + i * rh
        lab.append(text(x0 - 12, y + 22, nd, k='ink', size=16, anchor='end'))
        first_fail = {}
        for j in range(len(masks)):
            v = grid[i][j]
            if v == 'N':
                parts.append(rect(x0 + j * cw + 14, y + 3, cw - 28, rh - 6, k='red', fill='p', sw=1.6, rx=4))
            lab.append(text(x0 + j * cw + cw / 2, y + 23, '✓' if v == 'Y' else '✗', k='green' if v == 'Y' else 'red', size=20, font='print'))
    yb = y0 + rh * len(needs) + 28
    verdicts = [('not for', 'town'), ('no child', 'size'), ('not hypo-', 'allergenic'), ('no child', 'size'), ('fits', 'all!')]
    for j, (v1, v2) in enumerate(verdicts):
        lab.append(text(x0 + j * cw + cw / 2, yb, v1, k='green' if j == 4 else 'red', size=17, font='scrawl'))
        lab.append(text(x0 + j * cw + cw / 2, yb + 20, v2, k='green' if j == 4 else 'red', size=17, font='scrawl'))
    lab.append(text(x0 - 12, 46, 'what the family needs', k='muted', size=15, anchor='end'))
    return svg(660, yb + 34, rough(*parts) + ''.join(lab),
               'Checklist of the six needs against the five masks: every mask except Breathe has a cross in a needed row')

Q.append(dict(
    n=3, orig=7, answer='E', topic='Tables & matching',
    question=f"""<p>Gordon’s family are keen cyclists and regularly cycle {hl('around town (urban) and a nearby forest (rural)', 'y', 1)}. He has become concerned recently that the air they are breathing whilst cycling is
causing his family respiratory problems. He has decided to buy his whole family anti-pollution
cycling masks, by buying {hl('two adult and two child masks', 'g', 2)}. Jo, his wife, has {hl('asthma which is caused by pollen', 'y', 3)} and his son has {hl('allergies to clothing', 'y', 4)}.</p>
<p>Information about five cycling masks is shown below in the table.</p>
{table([['exhaust fume filtration', 'x', '✓', '✓', 'x', '✓'],
        ['replaceable filter system', '✓', '✓', 'x', '✓', 'x'],
        [hl('size: children', 'g'), '✓', 'x', '✓', 'x', '✓'],
        [hl('size: adult', 'g'), '✓', '✓', '✓', '✓', '✓'],
        [hl('dust and pollen filtration', 'y'), '✓', 'x', '✓', '✓', '✓'],
        [hl('hypoallergenic (kind to allergy sufferers)', 'y'), '✓', '✓', 'x', '✓', '✓'],
        [hl('urban environment', 'y'), 'x', '✓', '✓', 'x', '✓'],
        [hl('rural environment', 'y'), '✓', 'x', '✓', '✓', '✓'],
        [hl('cold environment', 'p', 5), '✓', 'x', 'x', '✓', 'x']],
       head=['', '<i>Air-1</i>', '<i>GXi</i>', '<i>Optiair</i>', '<i>Speed</i>', '<i>Breathe</i>'])}
<p>Gordon wants to buy the brand of cycling mask which {hl("fits the whole family's requirements", 'b', 6)}.</p>
<p class="stem">Which cycling mask should he buy?</p>""",
    options={'A': 'Air-1', 'B': 'GXi', 'C': 'Optiair', 'D': 'Speed', 'E': 'Breathe'},
    notes=[(1, 'y', 'Town <b>and</b> forest: the mask needs ✓ for urban and rural.'),
           (2, 'g', 'One brand for everyone, so it must come in children’s <b>and</b> adult sizes.'),
           (3, 'y', 'Pollen → needs dust and pollen filtration.'),
           (4, 'y', 'Allergies → needs hypoallergenic.'),
           (5, 'p', 'Nobody mentions cold weather or replacing filters. Ignore those rows.'),
           (6, 'b', 'One brand, every need ticked.')],
    steps=[
        f"""<p>Turn the story into a checklist before looking at the table:</p>
<ul><li>two children {ar()} <b>children’s size</b> (and adult size)</li>
<li>Jo’s pollen asthma {ar()} <b>dust and pollen</b> filtration</li>
<li>son’s allergies {ar()} <b>hypoallergenic</b></li>
<li>town and forest {ar()} <b>urban</b> and <b>rural</b></li></ul>""",
        f"""<p>Run each mask down the needed rows. One ✗ and it’s out:</p>{_masks()}""",
        f"""<p>Only Breathe has a tick in every row the family needs {ar()} {boxed('Breathe')}</p>
{note('Breathe has crosses for “replaceable filter” and “cold environment”, but nobody asked for those. A cross only matters in a row you need.', 'trap')}""",
    ],
    answer_text='Breathe: the only mask ticked for children, adults, pollen, allergies, town and forest.',
    why={'A': 'Air-1 is not for the urban environment, but they cycle around town.',
         'B': 'GXi has no children’s size (and no dust and pollen filter for Jo).',
         'C': 'Optiair is not hypoallergenic, and the son has allergies.',
         'D': 'Speed has no children’s size and isn’t for urban use.'},
    fast='Children’s size knocks out GXi and Speed; urban knocks out Air-1; hypoallergenic knocks out Optiair. Breathe.',
))


# ---------------------------------------------------------------- 4 (Q8)
T1 = '01100010111001010011000100'
T2 = '10101001111011100101000101'


def _bits():
    w = 20
    x1, x2 = 110, 110 - 4 * w
    parts, lab = [], []
    for row, (bits, x0, start, y) in enumerate(((T1, x1, 6, 54), (T2, x2, 10, 140))):
        for i, b in enumerate(bits):
            inside = start <= i < start + 12
            parts.append(rect(x0 + i * w, y, w, 30, k='ink', fill='y' if inside else 'paper', sw=1.2))
            lab.append(text(x0 + i * w + w / 2, y + 21, b, k='ink' if inside else 'muted', size=15, font='print'))
    mx = x1 + 6 * w
    parts.append(rect(mx - 4, 46, 12 * w + 8, 132, k='red', sw=2.6, rx=6))
    lab += [text(x1, 38, '1st transmission', k='ink', size=16, anchor='start'),
            text(x2, 196, '2nd transmission, slid 4 places left', k='ink', size=16, anchor='start'),
            text(mx + 6 * w, 224, 'same 12 bits in both = 101110010100', k='red', size=20, font='scrawl')]
    return svg(650, 238, rough(*parts) + ''.join(lab),
               'The two 26-bit transmissions lined up so the shared 12 bits 101110010100 sit in one box')

Q.append(dict(
    n=4, orig=8, answer='D', topic='Codes & patterns',
    question=f"""<p>A signal transmitter transmits a message in binary form. (In other words, the message is coded
in ‘bits’. Each bit is represented either by the digit ‘1’ or by the digit ‘0’.)</p>
<p>To add an element of security, the signal is {hl('embedded within other random bits', 'p', 1)} (so that there
are other 1s and 0s before and after the message), creating a 26-bit transmission.</p>
<p>A particular {hl('12-bit message', 'g', 2)} is transmitted as follows:</p>
<p><b>01100010111001010011000100</b></p>
<p>{hl('The same message is transmitted again', 'y', 3)}, as follows:</p>
<p><b>10101001111011100101000101</b></p>
<p class="stem">What is the 12-bit message {hl('contained within these two transmissions', 'b', 4)}?</p>""",
    options={'A': '001010011000', 'B': '001111011100', 'C': '010011000100', 'D': '101110010100', 'E': '111101110010'},
    notes=[(1, 'p', 'The random padding can be a different length each time, so the message can sit in a different place.'),
           (2, 'g', 'Look for a block of exactly 12 bits in a row.'),
           (3, 'y', 'Key fact: the real message appears in <b>both</b> strings.'),
           (4, 'b', 'Just test each option: is it in string 1? Is it in string 2?')],
    steps=[
        f"""<p>The real message must appear, unbroken, in <b>both</b> transmissions. Random padding can make a
fake match in one string, but not in both.</p>""",
        f"""<p>Test the options in the 1st transmission (count the bit where each one starts):</p>
{calc(f'A: 01100010111<b>001010011000</b>100, found at bit 12 {tick()}', 'B: not there ' + cross(),
      f'C: found at bit 15 {tick()}', f'D: found at bit 7 {tick()}', 'E: not there ' + cross())}""",
        f"""<p>Only A, C and D survive. Now the 2nd transmission:</p>
{calc('A: not there ' + cross(), 'C: not there ' + cross(), f'D: found at bit 11 {tick()} {ar()} {boxed("D")}')}
{_bits()}""",
        f"""{note('Fake matches happen! B and E really are in the 2nd string, and A and C really are in the 1st. That’s why you must check both.', 'trap')}""",
    ],
    answer_text='101110010100: the only option inside both transmissions (bits 7–18 of the first, 11–22 of the second).',
    why={'A': 'A is in the 1st transmission (bits 12–23) but nowhere in the 2nd.',
         'B': 'B is in the 2nd transmission (bits 6–17) but not in the 1st.',
         'C': 'C is in the 1st transmission (bits 15–26) but not in the 2nd.',
         'E': 'E is in the 2nd transmission (bits 8–19) but not in the 1st.'},
    fast='Check each option in string 1 (A, C, D are there), then string 2: only D is in both.',
))


# ---------------------------------------------------------------- 5 (Q12)
def _meal_bars():
    s = 0.42
    x0 = 160
    parts = [rect(x0, 40, 1140 * s, 40, k='ink', fill='p', sw=1.8),
             rect(x0, 120, 400 * s, 40, k='ink', fill='g', sw=1.8),
             rect(x0 + 400 * s, 120, 90 * s, 40, k='ink', fill='o', sw=1.8),
             line(x0 + 490 * s, 100, x0 + 490 * s, 178, k='red', w=2, dash=True),
             line(x0 + 1140 * s, 100, x0 + 1140 * s, 178, k='red', w=2, dash=True)]
    lab = [text(x0 - 10, 66, 'pay each visit', k='ink', size=17, anchor='end'),
           text(x0 - 10, 146, 'meal ticket', k='ink', size=17, anchor='end'),
           text(x0 + 570 * s, 66, '30 visits × $38 = $1140', k='ink', size=17),
           text(x0 + 200 * s, 146, '$400 ticket', k='ink', size=16),
           text(x0 + 445 * s + 2, 112, '+$90', k='orange', size=16),
           text(x0 + 815 * s, 150, 'saves $650', k='red', size=24, font='scrawl')]
    parts.append(line(x0 + 490 * s + 6, 172, x0 + 1140 * s - 6, 172, k='red', head=True, tail=True, w=2))
    lab.append(text(x0 + 490 * s, 200, '$490', k='green', size=17))
    return svg(660, 212, rough(*parts) + ''.join(lab),
               'Two bars: paying per visit costs 1140 dollars; the ticket plus the extra child costs 490 dollars; the gap is 650 dollars')

Q.append(dict(
    n=5, orig=12, answer='D', topic='Money & best deal',
    question=f"""<p>Help Yourself! is a restaurant in which customers can help themselves to as much food as they
wish from a buffet for a fixed price of {hl('$10 for adults and $6 for children', 'g', 1)}.</p>
<p>A Family Meal Ticket is available for $400 that allows unlimited visits to the restaurant for {hl('2 adults and 2 children', 'y', 2)} for one year. {hl("Any families with more than 2 children are charged half the children's price for every additional child, every time they eat", 'p', 3)}.</p>
<p>Mr and Mrs Monroe and their {hl('3 children', 'g', 4)} made good use of their Family Meal Ticket last year,
eating at Help Yourself! {hl('30 times', 'g', 4)}.</p>
<p class="stem">How much did the Family Meal Ticket {hl('save', 'b', 5)} the Monroe family last year compared to if they had
just paid per visit?</p>""",
    options={'A': '$470', 'B': '$560', 'C': '$590', 'D': '$650', 'E': '$740'},
    notes=[(1, 'g', 'Normal prices for each visit.'),
           (2, 'y', 'The $400 only covers four people.'),
           (3, 'p', 'The 3rd child is <b>not</b> free: half of $6 = $3, on <b>every</b> visit.'),
           (4, 'g', '5 people, 30 visits.'),
           (5, 'b', 'Saving = (cost paying each time) − (cost with the ticket).')],
    steps=[
        f"""<p>Without the ticket, the whole family pays every visit:</p>
{calc('2 × $10 + 3 × $6 = $20 + $18 = $38 a visit', '30 × $38 = <b>$1140</b>')}
{note('30 × 38: do 30 × 40 = 1200, then take off 30 × 2 = 60. That leaves 1140.', 'tip')}""",
        f"""<p>With the ticket, they pay $400 plus the 3rd child at half price each time:</p>
{calc('half of $6 = $3 a visit', '30 × $3 = $90', '$400 + $90 = <b>$490</b>')}""",
        f"""{_meal_bars()}{calc(f'$1140 − $490 = {boxed("$650")}')}""",
    ],
    answer_text='$650: $1140 paying per visit against $490 with the ticket.',
    why={'A': '$470 forgets the 3rd child in the pay-per-visit cost (30 × $32 = $960), then takes off $490.',
         'B': '$560 charges the 3rd child the full $6 each visit (400 + 180 = 580).',
         'C': '$590 charges the 3rd child half the <b>adult</b> price, $5 (400 + 150 = 550).',
         'E': '$740 forgets the 3rd child’s $3 a visit: 1140 − 400.'},
    fast='Pay per visit 30 × 38 = 1140. Ticket 400 + 30 × 3 = 490. Saving 650.',
))


# ---------------------------------------------------------------- 6 (Q13)
def _breakfast():
    parts, lab = [], []
    groups = [(30, ['bacon', 'sausage'], 'pick ONE', 'red'), (250, ['egg', 'beans'], 'pick ONE', 'red'),
              (470, ['toast', 'tomatoes'], 'need BOTH', 'green')]
    for x, items, tag, col in groups:
        parts.append(rect(x, 40, 170, 44, k=col, fill='paper', sw=2.2, rx=10))
        lab.append(text(x + 44, 68, items[0], k='ink', size=17))
        lab.append(text(x + 126, 68, items[1], k='ink', size=17))
        lab.append(text(x + 85, 30, tag, k=col, size=17, font='scrawl'))
        if col == 'red':
            parts.append(path(f'M{x + 76} 50 l8 8 l-8 8 l8 8', k='red', sw=2.4))
    lab.append(text(330, 116, '1 + 1 + 2 = 4 items, so there is no spare slot', k='ink', size=17))
    plates = [('bacon', 'egg'), ('bacon', 'beans'), ('sausage', 'egg'), ('sausage', 'beans')]
    for i, (a, b) in enumerate(plates):
        cx = 95 + i * 157
        parts.append(circle(cx, 210, 62, k='ink', fill='y', sw=2))
        parts.append(circle(cx, 210, 50, k='muted', sw=1.2))
        for j, item in enumerate((a, b, 'toast', 'tomatoes')):
            lab.append(text(cx, 184 + j * 19, item, k='ink', size=15))
        lab.append(text(cx, 296, f'meal {i + 1}', k='pen', size=17, font='scrawl'))
    return svg(660, 308, rough(*parts) + ''.join(lab),
               'Bacon or sausage, egg or beans, plus toast and tomatoes; four plates show the four allowed meals')

Q.append(dict(
    n=6, orig=13, answer='C', topic='Counting combinations',
    question=f"""<p>Jason’s workplace offers a special deal on {hl('any four breakfast items', 'g', 1)}. He can choose from
bacon, sausage, eggs, toast, tomatoes and beans.</p>
<p>Jason {hl('will not have bacon and sausage together', 'p', 2)}, {hl('nor will he have egg with beans', 'p', 2)}.</p>
<p class="stem">{hl('How many different combinations', 'b', 3)} of the six items will be acceptable to Jason?</p>""",
    options={'A': '2', 'B': '3', 'C': '4', 'D': '5', 'E': '6'},
    notes=[(1, 'g', 'Exactly 4 different items out of 6.'),
           (2, 'p', 'Two clashing pairs: at most one from each pair.'),
           (3, 'b', 'Combinations: order on the plate doesn’t matter.')],
    steps=[
        f"""<p>Group the six items:</p>
<ul><li>{{bacon, sausage}}: at most <b>one</b></li><li>{{egg, beans}}: at most <b>one</b></li><li>toast and tomatoes: no rules</li></ul>""",
        f"""<p>Most he can take is 1 + 1 + 2 = 4, and he needs exactly 4. So no slack at all:
<b>one</b> from each pair <b>and</b> both toast and tomatoes.</p>{_breakfast()}""",
        f"""{calc(f'2 choices × 2 choices = {boxed("4")}')}
{note('Long way: 15 ways to choose 4 from 6. Bacon + sausage are together in 6 of them, egg + beans in 6, and both clashes in 1. So 15 − 6 − 6 + 1 = 4.', 'check')}""",
    ],
    answer_text='4 meals: bacon or sausage, egg or beans, plus toast and tomatoes.',
    why={'A': '2 only lets one pair change (e.g. always egg), forgetting that egg/beans is a choice too.',
         'B': '3 is 15 − 6 − 6 = 3: it takes away the meal with both clashes twice.',
         'D': '5 needs a 5th meal, but any meal missing toast or tomatoes must use both items from a clashing pair.',
         'E': '6 is the number of meals with bacon and sausage together: banned, not allowed.'},
    fast='One from each clashing pair plus toast and tomatoes: 2 × 2 = 4.',
))


# ---------------------------------------------------------------- 7 (Q14)
def _age_bar():
    X = lambda p: 60 + p * 5.4
    segs = [(0, 15, 'b', '≤ 10'), (15, 50, 'paper', '11–18'), (50, 80, 'paper', '19–40'), (80, 90, 'o', '41–60'), (90, 100, 'o', '61–85')]
    parts, lab = [], []
    for a, b, f, name in segs:
        parts.append(rect(X(a), 70, X(b) - X(a), 44, k='ink', fill=f, sw=1.8))
        lab.append(text((X(a) + X(b)) / 2, 98, f'{b - a}%', k='ink', size=16))
        lab.append(text((X(a) + X(b)) / 2, 60, name, k='muted', size=14))
    for p in (0, 15, 50, 80, 90, 100):
        lab.append(text(X(p), 136, f'{p}%', k='pen', size=14))
    lab += [text(X(7.5), 166, '270 people', k='pen', size=17, font='scrawl'),
            text(X(7.5), 186, '1% = 18', k='pen', size=16),
            text(X(90), 30, 'above 40 = 20%', k='red', size=18, font='scrawl')]
    lab.append(text(X(90), 170, '20 × 18 = 360', k='red', size=20, font='scrawl'))
    lab.append(text(X(50), 22, 'age (years)', k='muted', size=14))
    return svg(620, 200, rough(*parts) + ''.join(lab),
               'A 100 per cent bar split 15, 35, 30, 10 and 10 per cent; the 15 per cent is 270 people, so the 20 per cent above 40 is 360')

Q.append(dict(
    n=7, orig=14, answer='D', topic='Percentages',
    question=f"""<p>Cyclists in a small town were surveyed about their age. A table was produced to show the
percentages and numbers of cyclists in five categories of their age. Some of the survey data
was added to the table.</p>
{table([['up to 10 years', hl('15%', 'g', 2), hl('270', 'g', 2)], ['up to 18 years', '50%', ''], [hl('up to 40 years', 'y'), hl('80%', 'y'), ''],
        ['up to 60 years', '90%', ''], ['up to 85 years', '100%', '']],
       head=['age categories', hl('cumulative percentages', 'y', 1) + ' of cyclists', 'numbers of cyclists'])}
<p class="stem">How many cyclists in the survey were {hl('above 40 years of age', 'b', 3)}?</p>""",
    options={'A': '180', 'B': '200', 'C': '270', 'D': '360', 'E': '540'},
    notes=[(1, 'y', 'Cumulative = running total. “Up to 40 years: 80%” means 80% are aged 40 or under.'),
           (2, 'g', '15% of everyone is 270 people. That’s your conversion rate.'),
           (3, 'b', 'Above 40 = everyone not in the “up to 40” 80%.')],
    steps=[
        f"""<p>Above 40 is everything after the 80%:</p>{calc(f'100% − 80% = <b>20%</b> are above 40')}""",
        f"""<p>Use the 270 to turn percentages into people:</p>
{calc('15% = 270', '1% = 270 ÷ 15 = <b>18</b>', f'20% = 20 × 18 = {boxed("360")}')}
{_age_bar()}
{note('No need to find the total. But if you want it: 100 × 18 = 1800 cyclists, and 20% of 1800 = 360.', 'check')}""",
    ],
    answer_text='360 cyclists: 20% of the survey, and 1% is 18 people.',
    why={'A': '180 is 10%, just the 41–60 group (90% − 80%). It forgets the over-60s.',
         'B': '200 isn’t a whole percentage here (1% = 18). It is 20% of a guessed total of 1000.',
         'C': '270 is the “up to 10 years” number copied from the table.',
         'E': '540 is 30%, the 19–40 group (80% − 50%). Wrong end of the table.'},
    fast='Above 40 = 100 − 80 = 20%. 15% is 270, so 5% is 90 and 20% is 360.',
))


# ---------------------------------------------------------------- 8 (Q18)
def _zones():
    X = lambda h: 70 + (h - 7) * 56
    parts, lab = [], []
    parts.append(line(X(7), 236, X(17.3), 236, k='ink', head=True, w=1.8))
    for h in range(7, 18):
        parts.append(line(X(h), 230, X(h), 242, k='ink', w=1.3))
        lab.append(text(X(h), 262, f'{(h - 1) % 12 + 1}', k='muted', size=15))
    lab.append(text(X(12), 284, 'Oklahoma (Central) time, am → pm', k='muted', size=15))
    # Jerry
    parts += [rect(X(8), 64, X(10) - X(8), 40, k='ink', fill='b', sw=1.8), rect(X(10), 64, X(16) - X(10), 40, k='ink', fill='o', sw=1.8)]
    lab += [text(X(9), 90, 'train 2 h', k='ink', size=15), text(X(13), 90, 'bus 6 h', k='ink', size=16),
            text(X(9), 122, '6–8 am Pacific', k='pen', size=14), text(X(13), 122, '9 am–3 pm Mountain', k='orange', size=14),
            text(42, 90, 'Jerry', k='ink', size=18, font='scrawl')]
    # Tim
    parts.append(rect(X(11), 150, X(15) - X(11), 40, k='ink', fill='g', sw=1.8))
    lab += [text(X(13), 176, 'flight 4 h', k='ink', size=16), text(X(13), 208, '12–4 pm Eastern', k='green', size=14),
            text(42, 176, 'Tim', k='ink', size=18, font='scrawl')]
    for h, who, y in ((15, 'Tim lands 3 pm', 34), (16, 'Jerry 4 pm', 34)):
        parts.append(line(X(h), y + 8, X(h), 228, k='red', w=2.2, dash=True))
    lab += [text(X(15) - 6, 34, 'Tim lands 3 pm', k='red', size=17, anchor='end', font='scrawl'),
            text(X(16) + 6, 34, 'Jerry 4 pm', k='red', size=17, anchor='start', font='scrawl')]
    parts.append(line(X(15) + 4, 140, X(16) - 4, 140, k='red', head=True, tail=True, w=2))
    lab.append(text(X(15.5), 160, '1 h', k='red', size=16))
    return svg(660, 296, rough(*parts) + ''.join(lab),
               'Both journeys on one Central-time line: Jerry 8 am train then bus to 4 pm; Tim flies 11 am to 3 pm, an hour earlier')

Q.append(dict(
    n=8, orig=18, answer='D', topic='Time zones',
    question=f"""<p>Tim and Jerry are business partners. Tim lives in New York (Eastern Time Zone) and Jerry
lives in San Francisco (Pacific Time Zone). They both agree to meet in {hl('Oklahoma (Central Time Zone)', 'b', 1)}.</p>
<div class="tbl-wrap"><table class="ptable"><thead><tr><th colspan="3"><i>time zones relative to Pacific Time Zone</i></th></tr>
<tr><th>Mountain</th><th>Central</th><th>Eastern</th></tr></thead>
<tbody><tr><td>+1 hour</td><td>{hl('+2 hours', 'y', 2)}</td><td>{hl('+3 hours', 'y', 2)}</td></tr></tbody></table></div>
<p>Tim {hl('set off at 10 am local time', 'p', 3)} but shortly afterwards he realised he had left his ticket at home.
As a result he missed his {hl('4 hour flight', 'g', 4)} to Oklahoma, so had to get the {hl('12 pm (midday) flight', 'g', 4)}
instead.</p>
<p>Jerry travelled by train for {hl('2 hours', 'g', 5)} to Salt Lake City (Mountain Time Zone), leaving
San Francisco at {hl('6 am local time', 'g', 5)}. He then immediately boarded a bus from Salt Lake City to
Oklahoma, where he arrived {hl('6 hours later', 'g', 5)}.</p>
<p class="stem">Which one of the following is true?</p>""",
    options={'A': 'Jerry arrived in Oklahoma 3 hours before Tim.', 'B': 'Jerry arrived in Oklahoma 1 hour before Tim.',
             'C': 'Jerry and Tim both arrived in Oklahoma at the same time.', 'D': 'Tim arrived in Oklahoma 1 hour before Jerry.',
             'E': 'Tim arrived in Oklahoma 3 hours before Jerry.'},
    notes=[(1, 'b', 'Compare arrivals on <b>one</b> clock: Oklahoma (Central) time.'),
           (2, 'y', 'Central = Pacific + 2. Eastern = Pacific + 3, so Central = Eastern − 1.'),
           (3, 'p', 'Red herring: he missed that flight. Only the 12 pm flight matters.'),
           (4, 'g', 'Leaves 12 pm New York time, takes 4 hours.'),
           (5, 'g', 'Jerry: 2 + 6 = 8 hours of travel from 6 am Pacific.')],
    steps=[
        f"""<p>Work everything out in <b>Central time</b> (the Oklahoma clocks).</p>""",
        f"""<p><b>Tim</b> (Eastern clocks, 1 hour ahead of Central):</p>
{calc('12 pm + 4 h = 4 pm Eastern', f'4 pm Eastern − 1 h = <b>3 pm Central</b>')}""",
        f"""<p><b>Jerry</b> (Pacific clocks, 2 hours behind Central):</p>
{calc('6 am + 2 h train + 6 h bus = 2 pm Pacific', f'2 pm Pacific + 2 h = <b>4 pm Central</b>')}
{note('You never need the Mountain zone. Jerry just travels for 8 hours in a row.', 'tip')}""",
        f"""<p>Put both on one Oklahoma-time line:</p>{_zones()}
{calc(f'Tim 3 pm, Jerry 4 pm {ar()} Tim arrives 1 hour first {ar()} {boxed("D")}')}""",
    ],
    answer_text='Tim arrived 1 hour before Jerry: Tim at 3 pm Central, Jerry at 4 pm Central.',
    why={'A': 'Needs Tim to land at 7 pm Central. That happens if you add Eastern’s +3 to Tim’s 4 pm instead of taking 1 hour off.',
         'B': 'Leaves Jerry’s arrival in Pacific time (2 pm) and compares it with Tim’s 3 pm Central.',
         'C': 'Compares Tim’s 4 pm <b>Eastern</b> with Jerry’s 4 pm <b>Central</b>: two different clocks.',
         'E': 'Uses Tim’s original 10 am start as his flight time (landing 2 pm Eastern = 1 pm Central). He missed that flight.'},
    fast='Tim: 12 + 4 = 4 pm Eastern = 3 pm Central. Jerry: 6 + 8 = 2 pm Pacific = 4 pm Central. Tim 1 hour first.',
))
