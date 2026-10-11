"""The mock papers: the questions chosen in tools/mock_selection.json, with their worked solutions.

Each mock question is a copy of its original question (same wording, figures and worked solution),
renumbered 1-25, with src (its year), src_n (its set number in that year's paper), mock_type and why
(why it was chosen). Answers come from the official key of each question's own paper (keys.json).
"""

import copy
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELECTION = HERE.parent / 'mock_selection.json'
KEY = {'ct': 'CT', 'ps': 'PS'}
NAME = 'Mock'
COPYRIGHT = '© UCLES 2008–2021 and © Cambridge University Press &amp; Assessment 2022–2023'


def selection():
    return json.loads(SELECTION.read_text()) if SELECTION.exists() else None


def load(kind, load_content):
    """The mock's questions for kind ('ct' or 'ps'), or None if there is no selection yet."""
    sel = selection()
    if not sel:
        return None
    papers, out = {}, []
    for i, it in enumerate(sel[KEY[kind]], 1):
        year = str(it['year'])
        if year not in papers:
            papers[year] = load_content(year, kind)
        q = next(x for x in papers[year] if x['orig'] == it['orig'])
        m = copy.deepcopy(q)
        m.pop('attempt', None)
        m.update(n=i, src=year, src_n=q['n'], mock_type=it['type'], mock_rank=it.get('rank', 1),
                 why_here=it.get('why', ''))
        out.append(m)
    return out


def keys(real_keys):
    """{'Mock': {'CT': [[n, orig, answer], ...], 'PS': [...]}} with answers from each paper's official key."""
    sel = selection()
    if not sel:
        return {}
    out = {}
    for kind, k in KEY.items():
        rows = []
        for i, it in enumerate(sel[k], 1):
            row = next(r for r in real_keys[str(it['year'])][k] if r[1] == it['orig'])
            rows.append([i, it['orig'], row[2]])
        out[k] = rows
    return {NAME: out}
