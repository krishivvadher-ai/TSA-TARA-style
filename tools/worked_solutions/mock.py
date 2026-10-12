"""The mock papers: the questions chosen in tools/mock_selection.json (Mock 1) and tools/mock2_selection.json (Mock 2),
with their worked solutions.

Each mock question is a copy of its original question (same wording, figures and worked solution),
renumbered 1-25, with src (its year), src_n (its set number in that year's paper), and why it was chosen.
Answers come from the official key of each question's own paper (keys.json).

Mock 1 ("types"): the hardest question of every question type, plus the next-hardest questions.
Mock 2 ("hardest", Problem Solving only): the hardest questions not in Mock 1, whatever their type. A question may
carry a "debate" note; the worked solution then shows it.
Mock 3 ("longest", Problem Solving only): the questions that keep a strong candidate thinking hard for longest, none
of them in Mock 1 or Mock 2.
"""

import copy
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEY = {'ct': 'CT', 'ps': 'PS'}
MOCKS = {
    'Mock': {'file': 'mock_selection.json', 'label': 'Mock 1', 'style': 'types'},
    'Mock2': {'file': 'mock2_selection.json', 'label': 'Mock 2', 'style': 'hardest'},
    'Mock3': {'file': 'mock3_selection.json', 'label': 'Mock 3', 'style': 'longest'},
}
NAME = 'Mock'
COPYRIGHT = '© UCLES 2008–2021 and © Cambridge University Press &amp; Assessment 2022–2023'


def is_mock(year):
    return str(year) in MOCKS


def label(year):
    """'Mock 1' or 'Mock 2' for a mock, the year itself otherwise."""
    return MOCKS[str(year)]['label'] if is_mock(year) else str(year)


def selection(name=NAME):
    path = HERE.parent / MOCKS[name]['file']
    return json.loads(path.read_text()) if path.exists() else None


def load(name, kind, load_content):
    """The mock's questions for kind ('ct' or 'ps'), or None if there is no selection yet."""
    sel = selection(name)
    if not sel:
        return None
    if KEY[kind] not in sel:
        return None
    papers, out = {}, []
    for i, it in enumerate(sel[KEY[kind]], 1):
        year = str(it['year'])
        if year not in papers:
            papers[year] = load_content(year, kind)
        q = next(x for x in papers[year] if x['orig'] == it['orig'])
        m = copy.deepcopy(q)
        m.pop('attempt', None)
        m.update(n=i, src=year, src_n=q['n'], mock_style=MOCKS[name]['style'], mock_type=it.get('type', ''),
                 mock_rank=it.get('rank', 1), why_here=it.get('why', ''), debate=it.get('debate'),
                 mock_minutes=it.get('minutes'))
        out.append(m)
    return out


def keys(real_keys):
    """{'Mock': {'CT': [[n, orig, answer], ...], 'PS': [...]}, 'Mock2': {...}} from each paper's official key."""
    out = {}
    for name in MOCKS:
        sel = selection(name)
        if not sel:
            continue
        out[name] = {}
        for kind, k in KEY.items():
            if k not in sel:
                continue
            rows = []
            for i, it in enumerate(sel[k], 1):
                row = next(r for r in real_keys[str(it['year'])][k] if r[1] == it['orig'])
                rows.append([i, it['orig'], row[2]])
            out[name][k] = rows
    return out
