from wslib import *

Y = 2023
Q = []

# Country borders of the five blank maps in Q38, traced from the paper (local units, frame top-left = 0, 0).
_MAPS = {
    'A': ('M66.8 0.0 C66.7 8.5 68.5 9.1 64.3 17.5 C62.2 21.7 50.6 20.9 50.6 27.6 C50.6 33.4 59.4 37.4 51.9 39.4'
         ' C47.5 40.6 45.8 48.2 44.8 52.1 C44.3 53.7 49.0 72.0 42.7 64.2 C39.8 60.8 33.6 68.2 33.6 71.7'
         ' C33.6 76.3 22.0 73.9 18.9 77.4 C15.3 81.5 21.9 89.5 23.7 93.1 M50.8 26.4 C46.1 23.5 41.8 20.3 37.3 17.3'
         ' C33.2 14.7 28.8 15.7 24.8 12.6 C20.3 9.1 19.3 15.8 15.8 15.8 C10.5 15.8 5.2 15.4 0.0 15.5 M19.5 76.9'
         ' C12.9 70.6 10.0 66.3 0.0 67.2 M67.1 8.2 C69.0 11.9 78.2 12.3 81.1 12.9 C83.5 13.4 84.9 7.6 88.4 12.9'
         ' C92.6 19.0 91.8 13.2 96.9 13.4 C106.4 13.7 110.3 15.9 113.5 25.1 C115.4 30.6 117.0 37.0 123.8 38.3'),
    'B': ('M57.2 0.0 C56.4 4.3 61.8 3.0 63.3 5.8 C64.2 7.6 68.2 13.0 70.7 11.6 C71.8 11.0 72.0 2.8 77.1 7.3'
         ' C79.1 9.1 82.5 13.1 85.5 12.7 C88.7 12.3 89.6 7.3 92.9 7.3 C96.6 7.3 98.7 10.6 102.5 8.8'
         ' C109.8 5.4 116.9 5.9 123.9 10.1 M64.4 7.9 C62.6 8.4 56.1 9.8 56.1 10.8 C56.1 13.0 53.1 18.3 51.6 19.8'
         ' C48.3 23.0 33.8 22.9 33.8 27.6 C33.8 33.4 34.0 42.0 41.9 42.0 C44.6 42.0 46.3 45.7 50.1 45.7'
         ' C53.5 45.7 55.5 47.2 59.2 47.2 C63.4 47.2 64.6 47.0 67.2 43.7 C69.9 40.3 71.0 38.9 75.6 37.8'
         ' C78.7 37.1 80.0 34.0 83.3 33.7 C85.0 33.6 86.7 35.5 88.7 35.0 C90.1 34.7 91.5 32.7 92.7 32.0'
         ' C95.2 30.4 96.2 27.0 98.7 25.7 C101.4 24.4 105.2 26.3 107.8 26.1 C111.2 26.0 112.8 25.2 116.3 26.2'
         ' C119.4 27.0 121.2 28.6 123.9 25.5 M0.0 22.7 C6.1 21.6 11.0 27.5 16.4 27.5 C19.7 27.5 22.3 25.1 25.5 25.1'
         ' C29.4 25.1 30.3 26.3 33.8 27.6 M37.6 40.8 C37.9 43.6 38.2 47.9 34.3 47.9 C30.6 47.9 28.6 47.1 28.0 51.3'
         ' C30.5 51.6 28.4 61.4 26.4 63.4 C22.0 67.9 27.7 73.5 31.6 76.4 C34.3 78.5 36.7 79.7 39.9 81.0'
         ' C41.9 81.8 43.8 84.7 46.5 85.8 C52.8 88.4 59.6 89.3 66.1 87.3 C71.3 85.7 78.1 82.6 82.6 79.7'
         ' C89.0 75.6 94.4 77.2 101.5 76.5 C104.3 76.3 106.4 73.8 108.7 73.8 C112.1 73.8 113.6 73.4 115.4 70.3'
         ' C116.5 68.5 119.7 65.6 119.7 63.6 C119.7 60.0 121.8 57.0 123.9 54.1 M24.8 65.5'
         ' C22.9 66.1 20.9 67.0 19.7 68.6 C17.7 71.0 16.4 70.4 13.8 71.4 C9.6 73.1 4.6 73.3 0.0 73.3 M28.0 73.3'
         ' C25.6 79.6 17.8 78.1 13.9 82.1 C11.4 84.7 13.7 86.0 12.4 88.4'
         ' C11.3 90.3 7.4 92.5 5.8 94.3 M74.3 84.1 L75.2 86.1 L75.8 88.4 L75.8 94.3 M99.0 76.7'
         ' C101.1 81.0 106.2 80.9 108.9 84.1 C110.4 85.9 110.2 88.1 110.2 90.2 C110.2 90.4 113.6 92.9 114.1 94.3'),
    'C': ('M83.3 0.0 C86.7 7.7 104.9 16.5 93.8 25.1 C89.0 28.7 86.3 31.2 89.9 37.5 C92.5 42.1 86.9 47.0 90.2 51.5'
         ' C94.0 56.7 100.7 57.1 103.1 63.7 C105.1 69.2 104.6 75.5 102.1 80.5 C99.7 85.2 95.2 89.0 89.6 89.0'
         ' C82.3 89.0 80.9 89.3 78.1 96.5 M102.1 80.5 C106.4 78.8 110.4 78.3 114.3 76.5'
         ' C118.9 74.3 123.3 71.6 127.9 69.3 M89.1 48.3 C85.8 48.3 83.7 48.6 80.6 49.5 C78.5 50.2 75.4 50.7 73.3 51.6'
         ' C72.0 52.1 70.8 52.7 69.7 53.4 C68.2 54.2 66.9 55.1 65.5 56.3 C62.6 58.7 58.8 56.5 55.8 58.6'
         ' C53.4 60.3 53.3 63.7 51.1 65.7 C48.2 68.2 46.2 61.1 46.2 59.1 C46.2 57.1 41.0 55.9 39.9 55.0'
         ' C37.3 53.0 33.6 49.4 33.4 45.9 C33.2 42.3 35.4 41.0 37.8 38.5 C38.9 37.3 39.1 35.5 40.2 34.1'
         ' C41.5 32.6 43.6 34.4 44.8 32.7 C48.0 28.1 45.6 18.8 55.5 21.9 C59.6 23.2 59.1 26.1 61.3 29.0'
         ' C63.3 31.8 66.4 32.6 68.7 34.4 C75.5 39.7 69.1 47.2 69.7 53.4 M13.4 0.0 C14.2 2.9 20.7 8.6 17.2 11.6'
         ' C12.8 15.3 11.5 17.3 17.9 20.4 C21.9 22.3 25.1 25.9 28.9 28.0 C32.5 30.1 37.3 31.3 39.7 34.8 M13.7 15.3'
         ' C12.0 17.8 9.2 23.6 6.9 25.4 C5.6 26.5 4.1 23.2 2.7 26.3 C1.8 28.2 0.9 30.1 0.0 32.0 M48.7 65.7'
         ' C48.7 69.1 50.1 77.1 47.9 79.6 C45.4 82.5 49.0 92.8 49.4 96.5 M34.0 48.3 C30.1 51.9 26.2 49.2 22.6 53.5'
         ' C19.7 57.0 18.9 62.6 18.9 67.0 C18.9 77.4 30.8 87.1 18.9 95.6 M21.1 75.9 C14.3 69.0 8.6 61.5 0.0 56.8'),
    'D': ('M0.0 16.0 C4.5 15.7 13.1 19.5 16.9 15.4 C21.4 10.5 28.7 12.1 34.8 12.1 C40.4 12.1 46.1 18.0 51.4 13.8'
         ' C52.4 12.9 53.0 11.1 54.1 10.4 C55.4 9.7 57.3 9.9 58.6 9.1 C61.8 7.4 64.6 7.8 67.8 6.8'
         ' C74.2 4.6 76.9 9.1 82.0 11.5 C87.5 14.0 93.8 12.5 99.7 13.9 C104.8 15.0 110.2 21.5 114.8 15.3'
         ' C116.5 13.1 117.1 10.0 118.3 7.5 C119.6 4.9 121.0 2.9 121.9 0.0 M0.0 25.6 C11.9 31.3 25.8 39.3 25.8 54.6'
         ' C25.8 66.4 11.7 83.2 0.0 85.9 M25.3 58.6 C27.8 58.6 29.2 56.6 31.7 55.8 C32.7 55.4 34.0 55.9 35.0 55.5'
         ' C37.4 54.8 36.6 54.0 38.3 52.9 C42.6 50.1 45.0 50.0 50.6 51.1 C56.1 52.3 60.3 54.1 62.6 59.4'
         ' C64.4 63.6 64.2 72.4 68.8 74.7 C74.0 77.4 80.0 71.5 85.4 73.7 C90.6 75.9 94.5 81.1 99.8 83.7'
         ' C114.1 90.7 117.8 77.8 125.2 68.1 M86.6 74.3 C86.5 75.6 87.3 76.7 85.7 76.7 C84.1 76.7 85.0 78.5 84.0 79.7'
         ' C80.9 83.0 86.3 81.8 86.6 84.2 C87.1 87.7 82.8 86.8 82.3 87.7 C80.8 90.3 82.4 92.2 84.1 94.3 M90.6 13.1'
         ' C90.6 15.9 90.0 19.6 92.9 21.0 C95.5 22.3 98.3 23.2 99.9 25.8 C104.8 33.9 88.8 30.4 86.1 30.6'
         ' C77.8 31.2 78.3 38.3 72.6 42.2 C67.3 45.7 61.6 48.3 57.6 53.6 M76.5 38.0 C77.8 40.0 79.0 38.6 80.4 39.6'
         ' C81.4 40.3 81.8 42.5 82.6 43.0 C85.0 44.2 88.4 43.1 90.5 46.1 C92.1 48.5 90.1 50.9 93.3 53.2'
         ' C96.0 55.1 98.1 53.0 99.5 57.1 C100.3 59.4 98.9 62.0 100.8 64.0 C101.6 64.9 107.6 65.2 109.0 65.6'
         ' C115.6 67.5 115.0 71.9 119.5 76.6'),
    'E': ('M0.0 5.2 C4.3 8.7 7.4 13.7 13.0 15.4 C19.1 17.2 21.4 20.8 21.4 26.8 C21.4 29.2 18.6 31.2 20.6 33.5'
         ' C22.4 35.4 24.9 36.4 26.6 38.3 C30.0 42.1 34.6 48.7 30.5 53.1 C26.5 57.4 21.1 56.1 19.0 61.7'
         ' C17.9 64.8 15.7 64.5 14.4 66.4 C12.6 69.1 13.4 73.3 14.0 76.2 C14.6 79.0 16.2 80.5 18.7 81.4'
         ' C20.6 82.1 26.4 80.0 27.8 81.4 C31.8 85.4 34.3 90.5 38.2 94.3 M25.9 56.1 C25.8 58.2 24.5 61.1 25.5 62.9'
         ' C26.6 64.8 29.5 67.4 31.0 69.3 C35.7 75.0 31.7 76.8 28.2 81.8 M31.9 0.0 C31.8 6.5 34.9 11.6 32.1 18.6'
         ' C30.8 21.9 29.8 24.0 29.1 27.4 C28.3 31.3 26.8 33.2 25.1 36.9 M15.0 78.8 C12.2 79.6 9.7 80.4 6.7 80.4'
         ' C3.4 80.4 3.2 75.0 0.0 73.9'),
}
_FRAMES = {'A': (123.8, 93.1), 'B': (125.2, 94.3), 'C': (127.9, 96.5), 'D': (125.2, 94.3), 'E': (125.2, 94.3)}
# A spot inside each country (local units), the colour used (1-4) and how much room there is for a dot.
_COUNTRIES = {
    'A': [(49.7, 13.6, 1, 11.5), (112.6, 10.9, 2, 8.9), (83.5, 52.2, 3, 30), (26.3, 38.5, 2, 20), (10.1, 77.5, 1, 8.0)],
    'B': [(14.8, 14.4, 1, 12), (84.3, 7.1, 2, 5.0), (63.5, 27.3, 3, 18), (17.6, 43.5, 2, 15), (98.6, 51.6, 1, 24),
          (114.7, 80.7, 2, 8.4), (8.6, 79.8, 3, 6.5), (28.4, 83.3, 2, 8.8), (97.8, 84.7, 3, 7.5)],
    'C': [(9.8, 9.8, 1, 7.8), (76.5, 21.4, 2, 19), (107.3, 31.7, 1, 18), (19.2, 38.8, 3, 17), (53.6, 42.3, 1, 17),
          (76.7, 72.7, 3, 21), (33.8, 67.3, 2, 14), (12.6, 83.0, 1, 10.5), (116.6, 85.1, 2, 9.1)],
    'D': [(109.0, 9.7, 1, 7.6), (105.6, 42.8, 2, 17), (57.1, 31.4, 3, 21), (13.6, 52.1, 1, 11.5), (78.3, 56.5, 1, 16.8),
          (44.0, 71.6, 2, 20), (93.1, 86.0, 3, 6.1)],
    'E': [(22.8, 11.9, 3, 9.9), (77.5, 47.1, 1, 40), (16.7, 47.3, 2, 14.6), (22.8, 71.6, 4, 9.0), (14.7, 85.8, 3, 6.4)],
}


# ---------------------------------------------------------------- 17 (Q36)
def _toys():
    x0, s = 40, 1.0
    X = lambda m: x0 + s * m
    parts, lab = [], []
    parts.append(line(X(0), 110, X(560), 110, k='ink', w=1.8))
    for h in range(9, 18):
        m = (h - 8.5) * 60
        parts.append(line(X(m), 104, X(m), 116, k='ink', w=1.4))
        if h > 9:
            lab.append(text(X(m), 134, f'{h:02d}:00', k='muted', size=13))
    parts.append(line(X(540), 40, X(540), 120, k='red', w=2.4))
    lab += [text(X(0), 134, '08:30', k='ink', size=13), text(X(540) + 4, 34, '17:30', k='red', size=16, anchor='end')]
    t = 0
    for i in range(1, 25):
        parts.append(rect(X(t), 60, 16 * s, 36, k='ink', fill='b', sw=1.2))
        if i in (1, 12, 13, 24):
            lab.append(text(X(t) + 8, 54, i, k='pen', size=14))
        t += 16
        if i == 12:
            parts.append(rect(X(t), 60, 40 * s, 36, k='ink', fill='g', sw=1.4))
            lab.append(text(X(t) + 20, 84, 'lunch', k='green', size=13))
            t += 40
        elif i < 24:
            t += 5
    end = t
    parts.append(rect(X(end + 5), 60, 16 * s, 36, k='red', sw=1.6, fill='p'))
    lab += [text(X(end) - 2, 160, 'toy 24 done at 17:24', k='pen', size=16, anchor='end'),
            text(X(end + 13), 186, 'a 25th toy would end at 17:45', k='red', size=16, anchor='end'),
            text(X(0), 24, 'blue = 16-minute toy, gaps = 5-minute breaks', k='muted', size=14, anchor='start')]
    return svg(640, 200, rough(*parts) + ''.join(lab),
               'Timeline from 08:30 to 17:30 with 24 toy blocks, short gaps and a 40-minute lunch; toy 24 finishes at 17:24 and a 25th would finish after 17:30')


Q.append(dict(
    n=17, orig=36, answer='B', topic='Time & schedules',
    question=f"""<p>Becky works from home making soft toys which she sells online. Each one takes her {hl('exactly 16 minutes', 'g', 1)} to make and she takes a {hl('5-minute break between finishing one item and starting the next', 'p', 2)}. She always takes a {hl('40-minute break for her lunch', 'g', 3)}. Today she is starting on a new
batch of toys and is planning to work {hl('from 08:30 until 17:30', 'g', 4)}.</p>
<p class="stem">How many soft toys will she have {hl('<b>completed</b>', 'b', 5)} by 17:30?</p>""",
    options={'A': '23', 'B': '24', 'C': '25', 'D': '26', 'E': '27'},
    notes=[(1, 'g', '16 minutes of making for each toy.'),
           (2, 'p', 'Breaks only go <b>between</b> toys: one fewer break than toys. No break needed after the last one.'),
           (3, 'g', 'Lunch: 40 minutes of no making.'),
           (4, 'g', '9 hours = 540 minutes.'),
           (5, 'b', 'Only finished toys count.')],
    steps=[
        f"""<p>Time available: 08:30 to 17:30 = 9 hours = <b>540 minutes</b>.</p>""",
        f"""<p>Each toy plus the break after it is 16 + 5 = 21 minutes. Lunch is one of the gaps between toys. Try 24 toys:</p>
{calc('making: 24 × 16 = 384 min', 'gaps: 23 gaps = 22 short breaks + lunch = 22 × 5 + 40 = 150 min',
      f'384 + 150 = 534 min ≤ 540 {tick()} finishes at 17:24')}
{calc(f'25 toys: 534 + 5 + 16 = 555 min > 540 {cross()}')}
{_toys()}
{calc(f'completed = {boxed("24")}')}
{note('Even if she takes lunch as well as a 5-minute break, 24 toys take 539 minutes and still fit. 25 never fits.', 'check')}""",
    ],
    answer_text='24 toys: they take 534 minutes (or 539), and a 25th would run past 17:30.',
    why={'A': '23 comes from 500 ÷ 21 = 23.8, giving every toy a break afterwards, even the last one. Her last toy needs no break, which frees the time for a 24th.',
         'C': '25 forgets the 40-minute lunch: without lunch, 25 toys take 25 × 16 + 24 × 5 = 520 minutes.',
         'D': '26 forgets lunch <b>and</b> rounds up: 26 toys need 541 minutes even with no lunch at all.',
         'E': '27 is “3 toys an hour for 9 hours”, treating 16 + 5 as 20 minutes and forgetting lunch.'},
    fast='540 − 40 lunch = 500. n toys need 21n − 5 minutes: 21 × 24 − 5 = 499 fits, 21 × 25 − 5 = 520 doesn’t. 24.',
))


# ---------------------------------------------------------------- 18 (Q37)
def _cyclists():
    x0, L = 170, 380
    parts, lab = [], []
    rows = [('men (first 100)', 42, 'pen'), ('men (second 100)', 42, 'pen'), ('women (100)', 54, 'orange')]
    for i, (name, pc, k) in enumerate(rows):
        y = 40 + 50 * i
        parts.append(rect(x0, y, L, 34, k='ink', fill='paper', sw=1.6))
        parts.append(rect(x0, y, L * pc / 100, 34, k='ink', fill='b' if k == 'pen' else 'o', sw=1.6))
        lab.append(text(x0 - 10, y + 23, name, k=k, size=17, anchor='end'))
        lab.append(text(x0 + 10, y + 23, f'{pc}%', k='ink', size=17, anchor='start'))
    avg = x0 + L * 0.46
    parts.append(line(avg, 28, avg, 196, k='red', w=2.4, dash=True))
    lab += [text(avg, 220, '(42 + 42 + 54) ÷ 3 = 138 ÷ 3 = 46%', k='red', size=20, font='scrawl'),
            text(x0 + L + 8, 64, 'shaded =', k='muted', size=14, anchor='start'),
            text(x0 + L + 8, 82, 'over 4 hours', k='muted', size=14, anchor='start'),
            text(x0, 22, 'twice as many men: imagine 200 men and 100 women', k='ink', size=16, anchor='start')]
    return svg(640, 236, rough(*parts) + ''.join(lab),
               'Three bars of 100 people: two bars of men with 42 percent shaded and one bar of women with 54 percent shaded; the average shading is 46 percent')


Q.append(dict(
    n=18, orig=37, answer='A', topic='Weighted averages',
    question=f"""<p>Last Saturday a large number of men and women competed in a long-distance cycling event.
The time that each competitor took to complete the course was recorded. The following table
shows the range of times taken and the percentages of men and women who achieved these
times.</p>
{table([['0–120', '5', '1'], ['121–150', '5', '5'], ['151–180', '6', '4'], ['181–210', '12', '21'],
        [hl('211–240', 'p', 1), '30', '15'], [hl('241–300', 'g', 2), hl('26', 'g'), hl('36', 'g')],
        [hl('301–420', 'g'), hl('16', 'g'), hl('12', 'g')], [hl('421 or more', 'g'), hl('0', 'g'), hl('6', 'g')]],
       head=['time in minutes', 'percentage of men', 'percentage of women'])}
<p>{hl('There were twice as many men as women', 'y', 3)} in the event.</p>
<p class="stem">What percentage of {hl('all the competitors', 'b', 4)} took {hl('more than four hours', 'p', 5)} to complete the event?</p>""",
    options={'A': '46%', 'B': '48%', 'C': '54%', 'D': '69%', 'E': '71%'},
    notes=[(1, 'p', 'This band ends at 240 minutes, which is exactly 4 hours, not <b>more</b> than 4 hours. Leave it out.'),
           (2, 'g', 'More than 240 minutes: this row and the two below it.'),
           (3, 'y', 'Men count double, so you can’t just average the two percentages.'),
           (4, 'b', 'Men and women together.'),
           (5, 'p', '4 hours = 4 × 60 = 240 minutes.')],
    steps=[
        f"""<p>More than four hours = more than 240 minutes = the last three rows:</p>
{calc('men: 26 + 16 + 0 = 42%', 'women: 36 + 12 + 6 = 54%')}""",
        f"""<p>Twice as many men, so picture 200 men and 100 women (300 people):</p>
{calc('men: 42% of 200 = 84', 'women: 54% of 100 = 54', f'84 + 54 = 138 out of 300 = 46 out of 100 = {boxed("46%")}')}
{_cyclists()}
{note('Weighted average shortcut: men count twice, so (42 + 42 + 54) ÷ 3 = 46. The answer must be closer to the men’s 42 than to the women’s 54.', 'tip')}""",
    ],
    answer_text='46%: (2 × 42 + 54) ÷ 3.',
    why={'B': '48% is the plain average of 42 and 54. It forgets there are twice as many men.',
         'C': '54% is the women only.',
         'D': '69% is the women including the 211–240 row (15 + 36 + 12 + 6). But 240 minutes is exactly four hours, not more.',
         'E': '71% includes the 211–240 row for everyone: men 72%, women 69%, (72 + 72 + 69) ÷ 3 = 71.'},
    fast='Over 240 min: men 42%, women 54%. Men count double: (42 + 42 + 54) ÷ 3 = 46%.',
))


# ---------------------------------------------------------------- 19 (Q38)
_FILL = {1: 'b', 2: 'y', 3: 'g', 4: 'p'}


def _map(key, ox, oy, s, big=False):
    w, h = _FRAMES[key]
    lines = (f'<g transform="translate({ox} {oy}) scale({s})">'
             + path(_MAPS[key], k='ink', sw=2.0 / s) + '</g>')
    frame = rect(ox, oy, w * s, h * s, k='muted', sw=1.6)
    dots, lab = [], []
    for x, y, c, room in _COUNTRIES[key]:
        r = max(6, min(room * s * 0.8, 15 if big else 11))
        cx, cy = ox + x * s, oy + y * s
        dots.append(circle(cx, cy, r, k='red' if c == 4 else 'ink', fill=_FILL[c], sw=2.4 if c == 4 else 1.4))
        lab.append(text(cx, cy + r * 0.42, c, k='ink', size=round(r * 1.25), font='print'))
    return frame, lines, dots, lab


def _maps():
    parts, mapl, lab = [], [], []
    spots = {'A': (14, 34, 1.45), 'B': (226, 34, 1.45), 'C': (438, 34, 1.45), 'D': (14, 232, 1.45), 'E': (222, 232, 1.95)}
    verdict = {'A': '3 colours', 'B': '3 colours', 'C': '3 colours', 'D': '3 colours', 'E': 'needs 4!'}
    for key, (ox, oy, s) in spots.items():
        if key == 'E':
            pts = {c: (ox + x * s, oy + y * s) for x, y, c, _ in _COUNTRIES['E'] if c != 3 or y > 50}
            for a, b in ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)):
                parts.append(line(*pts[a], *pts[b], k='red', w=1.6, dash=True))
        f, ln, d, l = _map(key, ox, oy, s, big=key == 'E')
        parts.append(f)
        mapl.append(ln)
        parts += d
        lab += l
        k = 'red' if key == 'E' else 'green'
        lab.append(text(ox, oy - 10, key, k='ink', size=19, anchor='start', font='print', weight='bold'))
        lab.append(text(ox + _FRAMES[key][0] * s, oy - 10, verdict[key], k=k, size=18, anchor='end', font='scrawl'))
    lab += [text(476, 262, 'In E, countries', k='ink', size=16, anchor='start'),
            text(476, 284, '1, 2, 3 and 4 all', k='ink', size=16, anchor='start'),
            text(476, 306, 'touch each other', k='ink', size=16, anchor='start'),
            text(476, 328, '(red dashes).', k='ink', size=16, anchor='start'),
            text(476, 362, 'Four neighbours', k='red', size=18, anchor='start', font='scrawl'),
            text(476, 384, 'in a group = 4', k='red', size=18, anchor='start', font='scrawl'),
            text(476, 406, 'colours needed.', k='red', size=18, anchor='start', font='scrawl')]
    return svg(640, 422, rough(*parts) + ''.join(mapl) + ''.join(lab),
               'The five maps painted: A, B, C and D need only colours 1, 2 and 3; in E four countries all touch each other, so a fourth colour is needed')


Q.append(dict(
    n=19, orig=38, answer='E', topic='Maps & colouring',
    question=f"""<p>The following pictures are blank maps. The continuous lines indicate country borders, the dotted
lines show the borders of the maps. These maps need to be painted so that each country is
filled with one colour and that {hl('no two neighbouring countries (countries with a common border) have the same colour', 'y', 1)}. {hl('The fewest number of colours should be used', 'y', 2)} on a given map.</p>
<p class="stem">Which one of the following blank maps will {hl('require 4 different colours', 'b', 3)} to be painted?</p>
{fig(Y, 'ps_q19_maps', 'Five blank maps A to E with wiggly country borders inside dotted frames', 560)}""",
    options={'A': 'map A', 'B': 'map B', 'C': 'map C', 'D': 'map D', 'E': 'map E'},
    notes=[(1, 'y', 'Countries that share a stretch of border must be different colours. Edges of the dotted frame don’t count.'),
           (2, 'y', 'So for each map, find the smallest number of colours that works.'),
           (3, 'b', '“Requires 4” = three colours are <b>not</b> enough. Look for four countries that all touch each other.')],
    steps=[
        f"""<p>Plan: try to paint each map with just 3 colours. Start with the biggest country, then go round its neighbours.
If you get stuck, that map needs a 4th colour.</p>
{note('Trick for the neighbours of one country: if they form a ring and each touches the next, an <b>even</b> number of them can swap between 2 colours. An <b>odd</b> ring (like 3) forces a 4th colour.', 'tip')}""",
        f"""<p>Here are the maps painted (the numbers are the colours):</p>
{_maps()}""",
        f"""<p>Why A–D manage with 3:</p>
{calc('A: the big country (3) has neighbours in a chain 2, 1, 2, 1: they just alternate',
      'B: the big middle country (1) has 6 neighbours in a chain, not a closed ring: alternate 2 and 3',
      'C: the round middle country (1) is ringed by 4 countries: an even ring, so 2, 3, 2, 3',
      'D: the enclosed middle country (1) is ringed by 4 countries: even again')}
<p>But in E the small enclosed country (4) is ringed by just <b>3</b> countries (the big right one, the long left one and the bottom-left corner), and those 3 all touch each other:</p>
{calc(f'4 countries all touching each other {ar()} 4 colours {ar()} {boxed("E")}')}""",
    ],
    answer_text='Map E: four of its countries all border each other, so 3 colours can’t work.',
    why={'A': 'A can be done with 3 colours: the big country’s neighbours alternate in a chain.',
         'B': 'B looks busy, but 3 colours work: the big middle country’s neighbours form a chain that alternates 2, 3, 2, 3…',
         'C': 'C’s round middle country has 4 neighbours in a ring (even), so 3 colours are enough.',
         'D': 'D’s enclosed middle country has 4 neighbours in a ring (even), so 3 colours are enough.'},
    fast='Look for a small enclosed country with an odd number (3) of neighbours that all touch: only E has one.',
))


# ---------------------------------------------------------------- 20 (Q42)
def _scales():
    X = lambda kg: 70 + 46 * (kg - 89)
    parts, lab = [], []
    parts.append(rect(X(94), 30, X(95) - X(94), 156, k='green', fill='g', sw=1.6))
    rows = [(95, 'reads 95', 'pen', 'b'), (93, 'reads 93', 'orange', 'o'), (96, 'reads 96', 'violet', 'v')]
    for i, (v, name, k, f) in enumerate(rows):
        y = 50 + 46 * i
        parts.append(line(X(v - 2), y, X(v + 2), y, k=k, w=9))
        parts.append(circle(X(v), y, 6, k='ink', fill='paper', sw=2))
        lab.append(text(X(v + 2) + 10, y + 6, f'{name}: {v - 2} to {v + 2}', k=k, size=16, anchor='start'))
    parts.append(line(X(89), 196, X(100), 196, k='ink', w=2))
    for kg in range(89, 101):
        parts.append(line(X(kg), 190, X(kg), 202, k='ink', w=1.4))
        lab.append(text(X(kg), 222, kg, k='muted', size=15))
    lab.append(text(X(94.5), 252, 'inside all three: 94 to 95 kg', k='green', size=20, font='scrawl'))
    return svg(640, 264, rough(*parts) + ''.join(lab),
               'Three ranges on a number line: 93 to 97, 91 to 95 and 94 to 98; they all overlap only from 94 to 95')


Q.append(dict(
    n=20, orig=42, answer='D', topic='Ranges & accuracy',
    question=f"""<p>Isaac has been on a diet to lose weight. He wants to be certain how much weight he has lost,
so he checks himself on three different weighing scales consecutively. One reads {hl('95 kg', 'g', 1)}, one
reads {hl('93 kg', 'g')}, and one reads {hl('96 kg', 'g')}. {hl('Each weighing scale is accurate to within 2 kg above or below the value they actually read', 'y', 2)}.</p>
<p class="stem">What is the {hl('<b>minimum</b> range in which Isaac’s true weight <b>must</b> lie', 'b', 3)}?</p>""",
    options={'A': '91–94 kg', 'B': '91–98 kg', 'C': '93–96 kg', 'D': '94–95 kg', 'E': '95–98 kg'},
    notes=[(1, 'g', 'Three readings of the same person at the same time.'),
           (2, 'y', 'Each reading gives a window: reading − 2 up to reading + 2. His true weight is inside it.'),
           (3, 'b', 'He must be inside <b>every</b> window at once, so find where all three overlap.')],
    steps=[
        f"""<p>Write each scale’s window:</p>
{calc('95 ± 2 = 93 to 97', '93 ± 2 = 91 to 95', '96 ± 2 = 94 to 98')}""",
        f"""<p>Where do all three overlap?</p>
{_scales()}
{calc(f'lowest he can be: the biggest bottom = 94', f'highest he can be: the smallest top = 95', f'{boxed("94–95 kg")}')}""",
    ],
    answer_text='94–95 kg: the only weights that fit all three scales.',
    why={'A': '91–94 kg starts from the 93 scale’s lowest value. But the 96 scale says he is at least 94 kg.',
         'B': '91–98 kg is everywhere <b>any</b> scale allows (all three windows joined together), not the part they share.',
         'C': '93–96 kg just runs from the lowest reading to the highest reading.',
         'E': '95–98 kg ignores the 93 scale, which says he is at most 95 kg.'},
    fast='Overlap = (biggest of 93, 91, 94) to (smallest of 97, 95, 98) = 94 to 95 kg.',
))


# ---------------------------------------------------------------- 21 (Q43)
def _socks():
    bw, x0 = 64, 130
    parts, lab = [], []
    lab.append(text(x0 - 12, 56, 'white', k='ink', size=18, anchor='end'))
    parts.append(rect(x0, 34, bw, 36, k='ink', fill='paper', sw=1.8))
    lab.append(text(x0 + bw / 2, 58, '16', k='ink', size=17))
    lab.append(text(x0 - 12, 126, 'blue', k='ink', size=18, anchor='end'))
    for i in range(4):
        parts.append(rect(x0 + bw * i, 104, bw, 36, k='ink', fill='b', sw=1.8))
        lab.append(text(x0 + bw * i + bw / 2, 128, '16', k='ink', size=17))
    parts.append(brace(x0 + bw + 2, x0 + 4 * bw - 2, 146, '', k='red'))
    lab += [text(x0 + 2.5 * bw, 186, '3 blocks = 24 + 24 = 48, so 1 block = 16', k='red', size=17),
            text(x0 + 4 * bw + 18, 56, 'white: 40 − 24 = 16', k='muted', size=16, anchor='start'),
            text(x0 + 4 * bw + 18, 128, 'blue: 40 + 24 = 64', k='muted', size=16, anchor='start'),
            text(x0 - 100, 226, 'start: 16 + 24 = 40 of each  →  red now 2 × 40 = 80', k='green', size=20, anchor='start', font='scrawl')]
    return svg(640, 242, rough(*parts) + ''.join(lab),
               'Bar model: white is 1 block, blue is 4 blocks; the 3 extra blocks are 48 socks, so a block is 16 and each colour started at 40')


Q.append(dict(
    n=21, orig=43, answer='E', topic='Ratio & bar models',
    question=f"""<p>A box contains {hl('equal numbers of each colour', 'y', 1)} of red socks, white socks and blue socks.
Additional red socks are put into the box which {hl('doubles the number of red socks', 'g', 2)} in the box.
{hl('24 of the white socks are removed from the box and replaced with 24 blue socks', 'g', 3)}.</p>
<p class="stem">If there are now {hl('four times as many blue socks as white socks', 'y', 4)} in the box, how many {hl('<b>red</b> socks', 'b', 5)}
are there in the box?</p>""",
    options={'A': '40', 'B': '60', 'C': '64', 'D': '72', 'E': '80'},
    notes=[(1, 'y', 'Same starting number for each colour. Call it n.'),
           (2, 'g', 'Red ends up as 2n.'),
           (3, 'g', 'White loses 24, blue gains 24. So blue is now 48 more than white.'),
           (4, 'y', 'Blue = 4 × white.'),
           (5, 'b', 'Red, after doubling: don’t stop at the starting number!')],
    steps=[
        f"""<p>After the swap: white = n − 24 and blue = n + 24, so blue is <b>48 more</b> than white.</p>""",
        f"""<p>Blue is also 4 times white. Draw white as 1 block and blue as 4 blocks: the extra 3 blocks are the 48.</p>
{_socks()}
{calc('3 blocks = 48 → 1 block = 16', 'white = 16, blue = 64', 'start: n = 16 + 24 = 40 (check: 64 − 24 = 40 too)',
      f'red now = 2 × 40 = {boxed("80")}')}
{note('With algebra: n + 24 = 4(n − 24) → n + 24 = 4n − 96 → 120 = 3n → n = 40.', 'check')}""",
    ],
    answer_text='80 red socks: each colour started at 40 and red doubled.',
    why={'A': '40 is the starting number of each colour. The red socks were doubled.',
         'B': '60 would mean 30 of each at the start: white 6 and blue 54, which is 9 times as many, not 4.',
         'C': '64 is the number of <b>blue</b> socks now, not red.',
         'D': '72 would mean 36 of each at the start: white 12 and blue 60, which is 5 times as many, not 4.'},
    fast='Blue − white = 48 = 3 × white, so white 16, blue 64, start 40. Red = 2 × 40 = 80.',
))


# ---------------------------------------------------------------- 22 (Q44)
def _machine():
    parts, lab = [], []

    def row(y, a, op1, b, op2, c, ok, k):
        for i, v in enumerate((a, b, c)):
            x = [40, 250, 460][i]
            parts.append(rect(x, y, 80, 46, k=k, fill='paper', sw=2, rx=8))
            lab.append(text(x + 40, y + 31, v, k='ink', size=22, font='print'))
        for i, op in enumerate((op1, op2)):
            cx = [185, 395][i]
            parts.append(circle(cx, y + 23, 28, k=k, fill='y', sw=1.8))
            lab.append(text(cx, y + 31, op, k='ink', size=19, font='print'))
            parts.append(arrow([122, 332][i], y + 23, cx - 32, y + 23, k=k, w=2))
            parts.append(arrow(cx + 32, y + 23, [248, 458][i], y + 23, k=k, w=2))
        lab.append(text(560, y + 31, ok, k='green' if '✓' in ok else 'red', size=22, anchor='start', font='scrawl'))

    row(40, '18', '÷ 3', '6', '+ 4', '10', '✓', 'pen')
    lab.append(text(40, 26, 'the original: third ÷ first, then + second', k='pen', size=16, anchor='start'))
    row(150, '12', '÷ 2', '6', '+ 5', '11', '✓ A', 'green')
    lab.append(text(40, 136, 'option A: 2, 5 and 12 to give 11', k='green', size=16, anchor='start'))
    return svg(640, 214, rough(*parts) + ''.join(lab),
               'Number machine: 18 divided by 3 is 6, add 4 gives 10; for option A, 12 divided by 2 is 6, add 5 gives 11')


Q.append(dict(
    n=22, orig=44, answer='A', topic='Number operations',
    question=f"""<p>Three numbers are combined in a particular way, using addition, subtraction, multiplication
and/or division.</p>
<p>The numbers {hl('3, 4 and 18 (used once each)', 'g', 1)} are combined to give the number {hl('10', 'g')}.</p>
<p class="stem">Which one of the following sets of numbers combines the first three numbers, {hl('in the same way', 'y', 2)}
to produce the final number?</p>""",
    options={'A': '2, 5 and 12 to give 11', 'B': '4, 6 and 12 to give 8', 'C': '5, 12 and 20 to give 18',
             'D': '6, 8 and 12 to give 14', 'E': '8, 16 and 24 to give 32'},
    notes=[(1, 'g', 'First find the one recipe that turns 3, 4 and 18 into 10.'),
           (2, 'y', 'Same operations on the same positions (first, second, third). Test that recipe on every option.')],
    steps=[
        f"""<p>Find the recipe. 10 is much smaller than 18, so 18 must shrink. Try a few:</p>
{calc(f'18 − 4 − 3 = 11 {cross()}', f'18 − 3 × 4 = 6 {cross()}', f'18 ÷ 3 + 4 = 6 + 4 = 10 {tick()}')}
<p>Recipe: <b>third ÷ first, then add the second</b>.</p>
{_machine()}""",
        f"""<p>Test it on each option:</p>
{calc(f'A: 12 ÷ 2 + 5 = 11 {tick()}', f'B: 12 ÷ 4 + 6 = 9, not 8 {cross()}', f'C: 20 ÷ 5 + 12 = 16, not 18 {cross()}',
      f'D: 12 ÷ 6 + 8 = 10, not 14 {cross()}', f'E: 24 ÷ 8 + 16 = 19, not 32 {cross()}')}
{calc(f'{boxed("A")}')}
{note('18 ÷ 3 + 4 is the only way to make 10 from 3, 4 and 18, so this is the only recipe to test.', 'check')}""",
    ],
    answer_text='A: 12 ÷ 2 + 5 = 11, just like 18 ÷ 3 + 4 = 10.',
    why={'B': 'B uses × and ÷ (4 × 12 ÷ 6 = 8). Our recipe gives 12 ÷ 4 + 6 = 9.',
         'C': 'Our recipe gives 20 ÷ 5 + 12 = 16, not 18.',
         'D': 'D uses + and − (8 + 12 − 6 = 14). On 3, 4, 18 that would give 4 + 18 − 3 = 19, not 10.',
         'E': 'E uses + and − (16 + 24 − 8 = 32), which gives 19 for 3, 4, 18. Our recipe gives 24 ÷ 8 + 16 = 19.'},
    fast='18 ÷ 3 + 4 = 10. Only A works the same: 12 ÷ 2 + 5 = 11.',
))


# ---------------------------------------------------------------- 23 (Q46)
def _laps():
    x0, L = 60, 500
    X = lambda f: x0 + L * f
    parts, lab = [], []
    parts.append(rect(X(0), 70, L, 30, k='ink', fill='paper', sw=1.8))
    for k in range(1, 9):
        parts.append(rect(X(0.12 * (k - 1)), 70, L * 0.12, 30, k='ink', fill='o', sw=1.2))
        lab.append(text(X(0.12 * k) - 2, 62, k, k='orange', size=14, anchor='end'))
    parts.append(rect(X(0.96), 70, L * 0.04, 30, k='red', fill='p', sw=1.2))
    parts.append(line(X(1), 40, X(1), 130, k='red', w=2.6))
    lab += [text(X(0), 34, 'grey’s lead, after each white lap (+12% of a lap each time)', k='ink', size=16, anchor='start'),
            text(X(0), 124, '0', k='muted', size=15), text(X(1), 150, '1 whole lap ahead = passes white', k='red', size=17, anchor='end'),
            text(X(0.48), 124, 'after 8 white laps the lead is 96%', k='orange', size=16),
            text(X(0), 186, 'white needs 100 ÷ 12 = 8⅓ laps to give away a whole lap', k='pen', size=17, anchor='start'),
            text(X(0), 214, 'grey has then done 8⅓ + 1 = 9⅓ laps: 9 completed', k='red', size=20, anchor='start', font='scrawl')]
    return svg(640, 228, rough(*parts) + ''.join(lab),
               'A bar for one lap of lead filling up 12 percent per white lap: 96 percent after 8 white laps, full at 8 and a third, when grey has done 9 and a third laps')


Q.append(dict(
    n=23, orig=46, answer='B', topic='Relative speed',
    question=f"""<p>The drawing shows a slot car track.</p>
<p>A grey car and a white car {hl('start together at the same point and travel in the same direction', 'y', 1)}.
Because of the figure-of-eight arrangement of the track, {hl('each car travels exactly the same distance to complete one lap', 'y', 2)} of the track. The grey car is {hl('12% faster', 'g', 3)} than the white car.</p>
{fig(Y, 'ps_q23_track', 'A figure-of-eight slot car track with two lanes; the grey and white cars sit side by side at the start/finish line', 260)}
<p class="stem">How many laps will the grey car have {hl('<b>completed</b>', 'b', 4)} before it {hl('passes the white car for the first time', 'p', 5)}?</p>""",
    options={'A': '8', 'B': '9', 'C': '10', 'D': '11', 'E': '12'},
    notes=[(1, 'y', 'Same start, same direction: a chase.'),
           (2, 'y', 'So the two lanes don’t matter. A lap is a lap.'),
           (3, 'g', 'Every time white does 1 lap, grey does 1.12 laps: grey gains 0.12 of a lap.'),
           (4, 'b', 'Whole laps finished by grey.'),
           (5, 'p', 'They start side by side, so to pass (overtake) white again, grey must get a <b>whole lap</b> ahead.')],
    steps=[
        f"""<p>Grey gains 12% of a lap for every lap white does. It passes white when it is a whole lap ahead:</p>
{_laps()}""",
        f"""{calc('lead needed: 1 lap = 100%', 'gain per white lap: 12%', f'100 ÷ 12 = 8⅓ white laps', f'grey: 8⅓ + 1 = 9⅓ laps {ar()} completed {boxed("9")}')}
{note('Check with 1.12: after 8 white laps grey has done 8.96 laps (not yet past). After 9 white laps grey has done 10.08 (already past). So the pass happens partway through grey’s 10th lap, with 9 laps completed.', 'check')}""",
    ],
    answer_text='9 laps: grey passes white after 9⅓ of its own laps.',
    why={'A': '8 is how many laps the <b>white</b> car has completed (8⅓) when it is passed.',
         'C': '10 rounds 9⅓ up. Grey is still in the middle of its 10th lap when it passes.',
         'D': 'After 11 grey laps, white has done only about 9.8, so grey is already more than a lap ahead: it passed earlier.',
         'E': '12 takes the 12 from “12%” as a number of laps.'},
    fast='Gain 0.12 lap per white lap; need 1 lap: 100 ÷ 12 = 8⅓ white laps = 9⅓ grey laps. 9 completed.',
))


# ---------------------------------------------------------------- 24 (Q48)
def _tokens():
    parts, lab = [], []
    seq = ['y'] * 8 + ['b'] * 20 + ['g'] * 4
    people = [('Mike', 7), ('Helen', 7), ('Amy', 7), ('Ben', 7), ('Pearl', 4)]
    n = 0
    for i, (name, cnt) in enumerate(people):
        y = 76 + 38 * i
        lab.append(text(100, y + 6, name, k='red' if name == 'Amy' else 'ink', size=18, anchor='end'))
        for j in range(cnt):
            parts.append(circle(122 + 30 * j, y, 11, k={'y': 'orange', 'b': 'pen', 'g': 'green'}[seq[n]], fill=seq[n], sw=2.4))
            n += 1
        lab.append(text(122 + 30 * 7 + 12, y + 6, f'{cnt} rides', k='red' if name == 'Amy' else 'muted', size=16, anchor='start'))
    for j, (f, t) in enumerate((('y', '8 from the family ticket'), ('b', '20 from 2 super rides'), ('g', '4 singles'))):
        parts.append(circle(30 + 214 * j, 24, 9, k={'y': 'orange', 'b': 'pen', 'g': 'green'}[f], fill=f, sw=2.4))
        lab.append(text(44 + 214 * j, 30, t, k='ink', size=16, anchor='start'))
    lab += [text(400, 110, '32 tokens', k='pen', size=22, anchor='start', font='scrawl'),
            text(400, 140, '= 4 × 7 + 4', k='pen', size=20, anchor='start'),
            text(400, 186, '8 each would leave', k='red', size=16, anchor='start'),
            text(400, 208, 'Pearl with 0 rides', k='red', size=16, anchor='start')]
    return svg(640, 260, rough(*parts) + ''.join(lab),
               'Thirty-two tokens shared out: Mike, Helen, Amy and Ben get 7 each and Pearl gets 4')


Q.append(dict(
    n=24, orig=48, answer='D', topic='Best value & sharing',
    question=f"""<p>The charges at the Puffins adventure park are shown in the following table.</p>
{table([['adult entry', '30'], ['child entry', '25'],
        [f'family ticket (entry for 2 adults and 2 children, {hl("includes 8 single-ride tokens", "g", 1)})', '120'],
        ['single-ride token', '5'], [hl('super ride (10 single-ride tokens)', 'g', 2), '40']], head=['', 'price ($)'])}
<p>A single-ride token allows one person one ride on any of the adventure rides.</p>
<p>Mike and Helen are visiting Puffins with their two children, Amy and Ben, {hl("and Helen’s mother, Pearl", 'p', 3)}. They {hl('pay $250', 'g', 4)} and want to have as many rides as possible. {hl('Mike, Helen, Amy and Ben will each have the same number of rides', 'y', 5)}. {hl('Pearl will have at least two rides', 'y', 6)}.</p>
<p class="stem">What is the {hl('<b>maximum</b>', 'b', 7)} number of rides that Amy will have?</p>""",
    options={'A': '4', 'B': '5', 'C': '6', 'D': '7', 'E': '8'},
    notes=[(1, 'g', 'Free tokens! Don’t forget to count them.'),
           (2, 'g', '10 tokens for $40 = $4 a ride, cheaper than $5 singles.'),
           (3, 'p', 'A 5th person: an adult who needs her own entry.'),
           (4, 'g', 'Spend all $250: entry first, then as many tokens as possible.'),
           (5, 'y', 'Four equal shares.'),
           (6, 'y', 'Pearl must get 2 or more, so the four can’t take every token.'),
           (7, 'b', 'Amy’s share, as big as possible.')],
    steps=[
        f"""<p>Entry: the family ticket covers Mike, Helen, Amy and Ben <b>and</b> gives 8 tokens. Pearl pays adult entry.</p>
{calc('family ticket $120 + Pearl $30 = $150', '$250 − $150 = $100 left for tokens')}""",
        f"""<p>Spend the $100 on tokens, cheapest first:</p>
{calc(f'2 super rides = $80 {ar()} 20 tokens', f'$20 left {ar()} 4 single tokens', 'total = 8 + 20 + 4 = <b>32 tokens</b>')}
{note('Without the family ticket, entry is 30 + 30 + 25 + 25 + 30 = $140, leaving $110 for 26 tokens. The family ticket wins.', 'check')}""",
        f"""<p>Share them: 4 equal shares, with at least 2 left for Pearl.</p>
{calc(f'8 each = 32 {ar()} Pearl gets 0 {cross()}', f'7 each = 28 {ar()} Pearl gets 4 {tick()}')}
{_tokens()}
{calc(f'Amy = {boxed("7")}')}""",
    ],
    answer_text='7 rides: 32 tokens = 4 × 7 + 4 for Pearl.',
    why={'A': '4 forgets both the family ticket’s 8 tokens and the spare $20 (20 tokens = 4 each + 4).',
         'B': '5 forgets the 8 tokens that come with the family ticket (24 tokens = 4 × 5 + 4).',
         'C': '6 leaves $20 unspent (28 tokens), or pays separate entry fees instead of the family ticket (26 tokens).',
         'E': '8 each uses all 32 tokens, leaving Pearl with none. She must have at least 2.'},
    fast='Family $120 + Pearl $30 = $150. $100 → 2 super rides + 4 singles = 24 tokens, plus 8 free = 32. 32 − 2 = 30 → 7 each (Pearl 4).',
))


# ---------------------------------------------------------------- 25 (Q50)
def _ratios():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    vals = [2, 2.5, 3, 2.4, 2, 10 / 6]
    shows = ['10 ÷ 5 = 2', '10 ÷ 4 = 2.5', '12 ÷ 4 = 3', '12 ÷ 5 = 2.4', '14 ÷ 7 = 2', '10 ÷ 6 ≈ 1.7']
    X = lambda i: 70 + 100 * i
    Yv = lambda r: 270 - (r - 1.4) * 120
    parts, lab = [], []
    parts.append(line(40, 290, 620, 290, k='ink', w=1.6))
    parts.append(poly([(X(i), Yv(v)) for i, v in enumerate(vals)], k='pen', sw=2.6, closed=False))
    for i, (d, v, s) in enumerate(zip(days, vals, shows)):
        parts.append(circle(X(i), Yv(v), 6, k='pen', fill='b', sw=2))
        lab.append(text(X(i), 314, d, k='ink', size=16))
        dx, dy, an = [(0, 26, 'middle'), (12, 22, 'start'), (0, -14, 'middle'), (10, -12, 'start'), (10, -12, 'start'), (0, 26, 'middle')][i]
        lab.append(text(X(i) + dx, Yv(v) + dy, s, k='ink', size=14, anchor=an))
    lab += [text(X(0.5) - 8, Yv(2.25) - 22, '+25%', k='red', size=22, font='scrawl', anchor='end'),
            text(X(1.5) - 6, Yv(2.75) - 20, '+20%', k='orange', size=20, font='scrawl', anchor='end'),
            text(X(3.5), Yv(2.4) - 50, 'then it only falls', k='muted', size=15),
            text(X(0), 24, 'ratio = production ÷ resources', k='muted', size=15, anchor='start')]
    return svg(640, 326, rough(*parts) + ''.join(lab),
               'Line of the daily ratio: 2, 2.5, 3, 2.4, 2, 1.7; the rise from Monday to Tuesday is 25 percent, from Tuesday to Wednesday 20 percent, then it falls')


Q.append(dict(
    n=25, orig=50, answer='A', topic='Ratios & percentage change',
    question=f"""<p>At a factory, the senior management are monitoring the {hl('ratio of production to resources used', 'y', 1)}
each day. For example, if on one day the production is $200&nbsp;000 and the resources used is
$40&nbsp;000, then the ratio is 5.</p>
<p>Last week, the production and resources used each day (both in tens of thousands of dollars)
were as shown in the graph below.</p>
{fig(Y, 'ps_q25_graph', 'Bar chart Monday to Saturday: resources used 5, 4, 4, 5, 7, 6 and production 10, 10, 12, 12, 14, 10 (tens of thousands of dollars)', 440)}
<p class="stem">Between which two days did the ratio of production to resources used {hl('increase by the greatest <b>percentage</b>', 'b', 2)}?</p>""",
    options={'A': 'Monday to Tuesday', 'B': 'Tuesday to Wednesday', 'C': 'Wednesday to Thursday',
             'D': 'Thursday to Friday', 'E': 'Friday to Saturday'},
    notes=[(1, 'y', 'Ratio = production ÷ resources = grey bar ÷ black bar. The “tens of thousands” cancel out.'),
           (2, 'b', 'Only rises count, and compare them as a percentage of the starting ratio.')],
    steps=[
        f"""<p>Read the bars and work out each day’s ratio (grey ÷ black):</p>
{calc('Mon 10 ÷ 5 = 2', 'Tue 10 ÷ 4 = 2.5', 'Wed 12 ÷ 4 = 3', 'Thu 12 ÷ 5 = 2.4', 'Fri 14 ÷ 7 = 2', 'Sat 10 ÷ 6 ≈ 1.67')}""",
        f"""<p>Only two changes go up:</p>
{_ratios()}
{calc(f'Mon → Tue: 2 → 2.5, up 0.5 out of 2 = {frac(1, 4)} = 25%', f'Tue → Wed: 2.5 → 3, up 0.5 out of 2.5 = {frac(1, 5)} = 20%',
      f'biggest % rise = Monday to Tuesday {ar()} {boxed("A")}')}
{note('Both rises are +0.5, but the same jump is a bigger percentage when you start from a smaller number.', 'trap')}""",
    ],
    answer_text='Monday to Tuesday: the ratio rises from 2 to 2.5, a 25% increase.',
    why={'B': 'Tuesday to Wednesday also rises by 0.5, but from 2.5, so only 20%.',
         'C': 'Wednesday to Thursday the ratio falls (3 → 2.4).',
         'D': 'Thursday to Friday the ratio falls (2.4 → 2), even though production jumps to its highest. Watch the ratio, not the bars.',
         'E': 'Friday to Saturday the ratio falls (2 → 1.67).'},
    fast='Ratios: 2, 2.5, 3, 2.4, 2, 1.67. Rises: +25% (Mon–Tue) and +20% (Tue–Wed). A.',
))
