# Writing worked solutions

Each paper's solutions live in one Python file in `content/`:

- `content/y<YEAR>_ps.py`: Problem Solving (25 questions)
- `content/y<YEAR>_ct.py`: Critical Thinking (25 questions)

Each file defines `QUESTIONS`, a list of 25 dicts in set order (1–25). A big file may be split into
parts (`content/_<YEAR>_ps_1.py` defining `Q = [...]`, and so on) with `y<YEAR>_ps.py` doing
`from _<YEAR>_ps_1 import Q as A` … `QUESTIONS = A + B + C`.

Start every file with `from wslib import *`, which brings in the helpers below.
`tools/worked_solutions/keys.json` gives, for every year and set, `[set number, original number, answer]`.
`n`, `orig` and `answer` must match it exactly. The build refuses to run otherwise.

Reference examples (copy their style and depth): `content/_2014_ps_1.py` (Problem Solving) and
`content/y2014_ct.py` (Critical Thinking).

## Problem Solving question

```python
dict(
    n=2, orig=6, answer='D',
    topic='Speed, time & timetables',          # short tag shown in the nav
    question=f"""<p>…full question text, exactly as printed, with highlights…</p>
<p class="stem">What is the {hl('<b>longest</b>', 'b', 4)} journey time…?</p>""",
    options={'A': '6 minutes', 'B': '7 minutes', 'C': '8 minutes', 'D': '9 minutes', 'E': '10 minutes'},
    notes=[(1, 'p', 'What highlight 1 means / why it matters'), ...],   # one per numbered highlight
    steps=[ 'HTML for step 1', 'HTML for step 2', ... ],                # the working, in order
    answer_text='9 minutes: 6 riding + 2 waiting + 1 waiting.',
    why={'A': 'why A is wrong', 'B': ..., 'C': ..., 'E': ...},          # every option except the answer
    fast='The 30-second route to the answer.',
)
```

- **Question in full.** Copy the wording exactly from the paper (fix decoding slips such as `¢` → `£`).
  Rebuild tables with `table(rows, head=[...])` so cells can be highlighted. For diagrams, graphs and
  picture options, crop the original with `extract_year.py crop` and embed with
  `fig(YEAR, 'name', 'alt text', width)`. If the options are pictures, still fill `options` with short
  labels such as `'graph A'`.
- **Annotations.** Wrap key phrases with `hl(text, colour, n)`. Colours: `y` key rule or fact,
  `p` trap, `g` numbers you need, `b` what they are asking. Give each numbered highlight a note in
  `notes`, in handwritten tone ("2 people! Double anything per person.").
- **Working.** Several short steps. Use quick bullet points, `calc(...)` lines for the maths, `ar()`
  arrows between ideas, `frac(a, b)` for fractions and `boxed(x)` to ring the answer. GCSE methods
  only (arithmetic, fractions, percentages, ratio, speed = distance ÷ time, simple counting); always
  the quickest clear route. Include mental-maths tips where they save time, using `note(text, 'tip' | 'trap' | 'check')`.
- **Sketches.** Draw something whenever it helps you see the question or the working, and
  **always** for questions that ask you to imagine a situation (a frame round a picture, people
  walking towards each other, a calendar, a family tree, folding a net, a lift display, a journey).
  Use `svg(w, h, body, label)` with shapes from `wslib` (`rect`, `line`, `arrow`, `circle`, `poly`,
  `path`, `text`, `brace`, `eye`, `stick_person`). Put shapes inside `rough(...)` for the
  hand-drawn wobble; keep `text(...)` outside `rough`. Use colour classes (`k='pen'|'red'|'green'|'orange'|'ink'|'muted'|'violet'`,
  `fill='y'|'p'|'g'|'b'|'o'|'v'|'paper'|'none'`, or `'black'` for something that is black in real life), never literal colours. Keep sketches about
  400–660 units wide with text size 14–24 so they stay readable on a phone. Every sketch needs a
  meaningful `label` (it is the accessible description).
- **Why not the others.** One line per wrong option saying exactly what mistake leads there
  ("forgets the 2-second gaps", "rounds 80 g down"). If an option is simply never reachable, say what it would need.
- **Fast route.** One or two lines: the quickest way a strong candidate would do it in the exam.

## Critical Thinking question

```python
dict(
    n=1, orig=1, answer='C', type='Main conclusion',      # or Flaw, Assumption, Weaken, Strengthen,
                                                          # Draw a conclusion, Parallel reasoning, Principle
    passage=[('evid', 'sentence(s)…'), ('conc', '…'), ...],  # the passage in order, split by role
    stem='Which one of the following best expresses …?',
    options={'A': '…', ...},
    right='Brief reason the answer is right.',
    why={'A': 'Brief reason it is wrong', ...},              # every option except the answer
    gap='Optional one-line tip on what to look for.',
    working='Required for Parallel reasoning and Principle questions (see 2014 Q12, Q13, Q24, Q25).',
    working_title='Working: strip it to a skeleton',
)
```

Roles: `ctx` context, `prem` reason, `evid` evidence or example, `analogy` comparison,
`counter` opposing view, `ic` intermediate conclusion, `conc` main conclusion. The passage text
must be the exact wording of the paper, split into consecutive pieces, nothing left out.
Keep the explanations brief: one line each. For parallel reasoning, write the original as a
skeleton (A, B, "need A to get B" …) and map every option onto it.

## Python gotchas (the machine runs Python 3.11)

- Inside an f-string's `{...}` you cannot use a backslash or the same quote character as the f-string,
  and a quoted string inside `{...}` cannot run over two lines. Write `hl("Lucy's watch", 'b', 1)` (double quotes when the
  text has an apostrophe) and keep each `hl('...')` argument on one line.
- Use `&lt;` and `&amp;` for literal `<` and `&` in text.

## Style

- British English. Plain, friendly, direct sentences. No em dashes.
- Ground everything in the question's own numbers and words.
- Do not add an `attempt` field (that only exists for 2014).

## Checking your work

1. Solve every question yourself before looking at `keys.json`. If you disagree with the key, the
   key is right: find your mistake and fix the working. Never change `answer`.
2. Build only your file into a scratch folder:
   `python3 tools/worked_solutions/build.py <YEAR> --out <scratch>/ws_check/<YEAR>_<ps|ct>`
   (the build checks numbering, answers and that every wrong option has a reason).
3. Look at your sketches: `node <scratch>/work/shot.js <html file> <png> 1200 light full`, then view
   the PNG (split tall pages into parts). Fix overlaps, clipped text and anything unclear.

## Written methods and the division sign

`written.py` adds these automatically when a page is built, so content files do not draw them:

- Any sum in a step written as `a + b = c`, `a − b = c`, `a × b = c` or `a ÷ b = c` (chains such as
  `a + b + c = d` are fine, and `≈` works for rounded answers) gets its written method drawn under the
  `calc` block, or at the end of the step for sums in the text. Money signs, thousands separators and a
  one-word label after a number (`6 pairs × £1.50 = £9.00`) are understood.
- The stated answer is checked; a sum that does not work out is left alone, and so are basic facts such as
  times tables, `5 + 10` or `× 10`.
- Write the sum on one line with the operator between the numbers. Percentages, fractions made with
  `frac()` and times such as `16:00` are not drawn.
- Every `÷` is replaced by a drawn sign with bold dots, because the handwriting font's `÷` is faint.

