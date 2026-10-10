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
- **Written methods:** every sum in the Problem Solving working is also set out in full underneath:
  column addition and subtraction, short and long multiplication, and bus stop or long division (with
  decimals lined up). The *Written methods* button hides them if you want a shorter page.
- **Practice mode** hides the working until you press *Show working* on a question.

They are built from `tools/worked_solutions/` (see `SCHEMA.md` there).

## Website

Open `TSA_Website/index.html` in a web browser (it works offline). It holds everything: the answers, the
worked solutions and the question papers for every year.

- The home page shows every year as a card. Pick one to see its pages: for each set (Critical Thinking and
  Problem Solving) the **answers**, the **worked solutions** and the **question paper**.
- To check a paper, open its *Answers* and tap any question to jump straight to its worked solution. Each
  worked solution also shows the answer at the top.
- The side menu (the *Menu* button on a phone) reaches every page of the year in one tap, and every other
  year. The arrows in the top bar step to the same page in the previous or next year.

Rebuild it with `python tools/worked_solutions/build_site.py` (it needs `pymupdf` and `pillow` to draw the
question papers).

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
