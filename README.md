# TSA Critical Thinking and Problem Solving sets

Every TSA Oxford Section 1 paper from 2008 to 2023 (16 years) split into a
**Critical Thinking** set and a **Problem Solving** set, each with its own
time limit and mark scheme.

## Folders

| Folder | Contents |
| --- | --- |
| `TSA_Papers/` | `TSA_<year>_Critical_Thinking.pdf` and `TSA_<year>_Problem_Solving.pdf` |
| `TSA_Answers/` | `TSA_<year>_Critical_Thinking_Mark_Scheme.pdf` and `TSA_<year>_Problem_Solving_Mark_Scheme.pdf` |
| `TSA_Worked_Solutions/` | `TSA_<year>_Problem_Solving_Worked_Solutions.html` and `TSA_<year>_Critical_Thinking_Worked_Solutions.html` |
| `TSA_Website/` | One website with everything above: open `TSA_Website/index.html` |

Each year therefore has four documents: two papers and their two mark schemes.

The **mock papers** sit alongside them: Mock 1 (`TSA_Mock_Critical_Thinking.pdf` and `TSA_Mock_Problem_Solving.pdf`)
and Mock 2 (`TSA_Mock2_Problem_Solving.pdf`), with their mark schemes and worked solutions under the same names.

## The papers

- The cover page gives the title (for example *TSA 2015 Critical Thinking*),
  the number of questions, the total marks and the time limit.
- Questions are renumbered 1, 2, 3 … within each set. The original question
  number from the TSA paper follows in brackets, e.g. **1 (Q3)**.
- Each question is reproduced exactly as printed in the original paper,
  including all diagrams, tables and graphs.

Every set has 25 questions, so each paper is worth **25 marks** (one mark per
question, with no penalty for incorrect answers).

## Worked solutions

The pages in `TSA_Worked_Solutions/` open in any web browser and work offline (fonts and pictures are
built in).

- **Problem Solving:** every question in full with the key words highlighted and explained, then
  step-by-step working using GCSE methods only, hand-drawn sketches, the answer, why each other
  option is wrong, and a quick exam route.
- **Critical Thinking:** each passage colour-coded by the job each sentence does (reason, evidence,
  conclusion…), the answer highlighted with a short reason, a short note on every wrong option, and
  full working for parallel reasoning and principle questions.
- **Written methods** (column subtraction and addition, long multiplication, long division) are set out in
  full only where they are really needed: where the answer options are too close to estimate and there is
  no quicker trick. Everywhere else the working estimates or uses a shortcut, because that saves time.
- **Practice mode** hides the working until you press *Show working* on a question.

They are built from `tools/worked_solutions/` (see `SCHEMA.md` there).

## Website

Open `TSA_Website/index.html` in a web browser (it works offline). It holds everything: the answers, the
worked solutions and the question papers for every year.

- The home page shows every year as a card, and the **mock papers** above them. Pick one to see its pages: for each set (Critical Thinking and
  Problem Solving) the **answers**, the **worked solutions** and the **question paper**.
- To check a paper, open its *Answers* and tap any question to jump straight to its worked solution. Each
  worked solution also shows the answer at the top.
- The side menu (the *Menu* button on a phone) reaches every page of the year in one tap, and every other
  year. The arrows in the top bar step to the same page in the previous or next year.

Rebuild it with `python tools/worked_solutions/build_site.py` (it needs `pymupdf` and `pillow` to draw the
question papers).

## Mock papers

### Mock 1

Two extra 25-question papers, one Critical Thinking and one Problem Solving, each 45 minutes. Every question
is a real past TSA question. Each paper has the **hardest question of every question type** across all 16
papers, and the remaining places go to the **next-hardest questions overall** (at most 4 of any one type, so
the paper stays balanced):

- **Critical Thinking** covers all 10 question types (main conclusion, drawing a conclusion, assumption, flaw,
  strengthen, weaken, parallel reasoning, identifying a principle, applying a principle, filling the gap).
- **Problem Solving** covers all 19 question types. The six extra places went to the next-hardest questions:
  two more 3D views, two more nets, one more counting and one more 2D shapes question.
- Wherever a paper has more than one question of a type, they are the hardest ones of that type, in order.
- Each question shows where it came from, e.g. **12 (2014 Q6)**. Its worked solution says why it was chosen.
  Questions from the 2014 paper are marked as ones you have met before.

How they were chosen. There are no official statistics on how often each TSA question is answered correctly,
so the choice rests on careful judgement, made in rounds:

1. Every one of the 800 past questions was rated for difficulty and sorted into a type.
2. The leading candidates of each type (about 330 questions, with each rater's scores adjusted for how harshly
   they marked) were solved and re-ranked side by side by a judge who saw the whole type at once.
3. The top candidates of each type were then solved and ranked again, blind, by two more independent judges,
   who also estimated the share of strong candidates who would get each one wrong. The consensus order is the
   average of the three rankings.
4. Each type's first question goes in. The other places go to the hardest remaining questions; for Problem
   Solving the closest contenders were scored once more on a single common scale by two further judges.

Questions whose official answer is debatable, or that repeat another year's question, were left out, so every
mock answer is the official one. The order is shuffled so that no two neighbouring questions share a type.

The choice is in `tools/mock_selection.json`. Rebuild the papers with
`python tools/build_mock.py --papers <folder of question papers> --answers <folder of answer keys>`, and the
worked solutions with `python tools/worked_solutions/build.py Mock`.

### Mock 2 (Problem Solving only)

One more 25-question Problem Solving paper, 45 minutes: the 25 questions judged **hardest of all those not
already in Mock 1**, from any question type. Unlike Mock 1, it also includes questions whose official answer is
debatable (7 of them). Each of those has a *Debatable* note in its worked solution explaining the rival reading;
the mark scheme uses the official answers.

How they were chosen: 41 candidates were shortlisted, the strongest from the Mock 1 judging plus the questions
left out of Mock 1 as debatable. Each was given an estimate of the share of strong candidates who miss the
official answer: the Mock 1 judges' estimates, with each judge's scores shifted to match how the later judges
marked, and fresh judgements of the questions that had not been scored on that scale. The 25 highest go in;
a tie for the last place was broken by the first-round ratings. The order is shuffled so that no two
neighbouring questions share a type. Spatial questions (nets, 3D views, 2D shapes) dominate, because they are
the ones strong candidates get wrong most often.

The choice is in `tools/mock2_selection.json`. Rebuild with `python tools/build_mock.py --mock Mock2 ...` and
`python tools/worked_solutions/build.py Mock2`.

## Time limits

The time limits are based on the TARA (Test of Academic Reasoning for
Admissions) modules: Critical Thinking is 22 questions in 40 minutes, and
Problem Solving is 22 questions in 40 minutes. Each limit is scaled to the
number of questions in the set and rounded to the nearest minute:

| Set | Questions | Calculation | Time limit |
| --- | --- | --- | --- |
| Critical Thinking | 25 | 25 × 40 ÷ 22 = 45.45 | **45 minutes** |
| Problem Solving | 25 | 25 × 40 ÷ 22 = 45.45 | **45 minutes** |

## Mark schemes

Each mark scheme lists the set's question numbers (1–25, matching the
renumbered paper) and the correct option. Original TSA question numbers are
deliberately left out. Answers come from the official Section 1 answer keys.

## How questions were classified

TSA Section 1 always contains 25 Critical Thinking and 25 Problem Solving
questions, placed in fixed positions:

| Years | Critical Thinking (original question numbers) | Problem Solving |
| --- | --- | --- |
| 2008–2019 | 1, 3–5, 9–11, 15–17, 21–23, 27–29, 33–35, 39–41, 45–47 | all others |
| 2020–2023 | 1, 3–5, 9–11, 15–17, 21–23, 27–29, 33–35, 39–41, 45, 47, 49 | all others |

Every question was also checked individually by its question type. Critical
Thinking questions ask about arguments: main conclusions, assumptions, flaws,
strengthening or weakening, principles and parallel reasoning. Problem Solving
questions are numerical, spatial and data questions. The full list is in
`tools/classification.json`.

## Rebuilding

`tools/build_tsa_sets.py` regenerates everything from the original question
papers and answer keys:

```
pip install pymupdf reportlab
python tools/build_tsa_sets.py --papers <folder of question papers> --answers <folder of answer keys>
```

To change the timing basis, edit the `TARA` settings at the top of the script.

## Copyright

The questions are © UCLES (2008–2021) and © Cambridge University Press &
Assessment (2022–2023), reproduced from the TSA Oxford Section 1 papers for
practice purposes.
