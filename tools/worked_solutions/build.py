"""Build the worked-solution pages in TSA_Worked_Solutions/.

    python tools/worked_solutions/build.py            # every year that has content
    python tools/worked_solutions/build.py 2014 2017  # just these years

Each paper becomes one self-contained HTML page (fonts and figures embedded).
A body-only copy for publishing is written to --artifact-dir when given.
"""

import argparse
import base64
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / 'content'))
import wslib  # noqa: E402

KINDS = {
    'ps': dict(name='Problem Solving', slug='Problem_Solving', key='PS'),
    'ct': dict(name='Critical Thinking', slug='Critical_Thinking', key='CT'),
}

PS_COLOURS = [('y', 'Key rule or fact'), ('p', 'Trap'), ('g', 'Numbers you need'), ('b', 'What they are asking')]
CT_ROLES = [
    ('ctx', 'Context'), ('prem', 'Reason'), ('evid', 'Evidence / example'), ('analogy', 'Comparison'),
    ('counter', 'Opposing view'), ('ic', 'Intermediate conclusion'), ('conc', 'Main conclusion'),
]
ROLE_LABEL = dict(CT_ROLES)


def font_face(family, file, weight):
    data = base64.b64encode((HERE / 'fonts' / file).read_bytes()).decode()
    return (f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};font-display:swap;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")


CSS = r"""
/* Layout: an exercise book. Printed question slips sit on squared paper; all working is in pen.
   Dark mode is a chalkboard with the same slips pinned to it. */
:root{
  --paper:#f6f5ef; --grid:rgba(60,100,160,.10); --ink:#24272c; --muted:#6b6f77;
  --pen:#1f4ea8; --red:#c42f2a; --green:#1d7a42; --orange:#b8640f; --violet:#6b3fb5;
  --slip:#ffffff; --slip-ink:#1d1f23; --slip-edge:#dad7cc;
  --hl-y:#fde46a; --hl-p:#ffb0cf; --hl-g:#aeeec1; --hl-b:#b6d8ff; --hl-o:#ffcf98; --hl-v:#dccbff; --hl-k:#e2e2dc; --hl-t:#a6ece4;
  --fill-y:#fff0a8; --fill-p:#ffd3e4; --fill-g:#cdf5d8; --fill-b:#d5e8ff; --fill-o:#ffe2bf; --fill-v:#e9ddff;
  --note-bg:#fff3a3; --note-ink:#2b2710; --chip:#e9e7df; --chip-ink:#34373c;
  --print:Arial,"Helvetica Neue",Helvetica,sans-serif;
  --hand:"Patrick Hand","Bradley Hand","Segoe Print","Comic Sans MS",cursive;
  --scrawl:"Caveat","Bradley Hand","Segoe Print","Comic Sans MS",cursive;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --paper:#16211d; --grid:rgba(255,255,255,.045); --ink:#e7ece8; --muted:#a3aea8;
  --pen:#9cc3ff; --red:#ff8d84; --green:#86e0a6; --orange:#ffc07d; --violet:#c9b0ff;
  --fill-y:#5a5016; --fill-p:#5c2742; --fill-g:#1d4f33; --fill-b:#1b3d63; --fill-o:#653d13; --fill-v:#3d2d68;
  --chip:#23312b; --chip-ink:#dfe6e1; color-scheme:dark;
}}
:root[data-theme="dark"]{
  --paper:#16211d; --grid:rgba(255,255,255,.045); --ink:#e7ece8; --muted:#a3aea8;
  --pen:#9cc3ff; --red:#ff8d84; --green:#86e0a6; --orange:#ffc07d; --violet:#c9b0ff;
  --fill-y:#5a5016; --fill-p:#5c2742; --fill-g:#1d4f33; --fill-b:#1b3d63; --fill-o:#653d13; --fill-v:#3d2d68;
  --chip:#23312b; --chip-ink:#dfe6e1; color-scheme:dark;
}
*{box-sizing:border-box}
body{margin:0;background-color:var(--paper);color:var(--ink);
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:26px 26px;font-family:var(--hand);font-size:18px;line-height:1.5}
.wrap{max-width:1120px;margin:0 auto;padding-inline:16px;padding-block:24px 64px}
a{color:var(--pen)}
:focus-visible{outline:3px solid var(--orange);outline-offset:2px}
h1,h2,h3{text-wrap:balance}

/* page header */
.page-head{display:grid;gap:14px;margin-bottom:28px}
.eyebrow{font-family:var(--scrawl);font-size:1.5rem;color:var(--red);margin:0;transform:rotate(-1.5deg);transform-origin:left}
.page-head h1{font-family:var(--scrawl);font-weight:700;font-size:clamp(2.4rem,6vw,3.6rem);line-height:1;margin:0}
.lede{margin:0;max-width:62ch;color:var(--muted)}
.legend{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;font-size:.95rem}
.legend span.sw{display:inline-block;padding:0 .45em;border-radius:3px;color:var(--slip-ink);font-family:var(--print);font-size:.82rem}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.btn{font:inherit;font-size:1.02rem;border:2px solid var(--pen);color:var(--pen);background:transparent;border-radius:12px 9px 13px 8px;
  padding:.2em .8em;cursor:pointer}
.btn[aria-pressed="true"]{background:var(--pen);color:var(--paper)}
.nav{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:6px}
.nav a{display:flex;gap:8px;align-items:baseline;text-decoration:none;color:var(--chip-ink);background:var(--chip);
  border-radius:8px;padding:5px 9px;font-size:.95rem;min-width:0}
.nav a b{font-family:var(--scrawl);font-size:1.25rem;color:var(--red)}
.nav a span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nav a i{margin-left:auto;font-style:normal}

/* one question */
.q{padding-top:26px;margin-top:26px;border-top:2px dashed var(--muted)}
.q-head{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:baseline;margin-bottom:12px}
.qnum{font-family:var(--scrawl);font-weight:700;font-size:2.6rem;line-height:1;color:var(--red)}
.qorig{color:var(--muted);font-size:1.05rem}
.chip{background:var(--chip);color:var(--chip-ink);border-radius:999px;padding:1px 10px;font-size:.92rem}
.attempt{border-radius:999px;padding:1px 10px;font-size:.92rem;border:2px solid currentColor}
.attempt.good{color:var(--green)}.attempt.bad{color:var(--red)}.attempt.blank{color:var(--muted)}
.q-grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:18px;align-items:start}
@media (max-width:860px){.q-grid{grid-template-columns:minmax(0,1fr)}}

.slip{background:var(--slip);color:var(--slip-ink);font-family:var(--print);font-size:15.5px;line-height:1.55;
  border:1px solid var(--slip-edge);padding:18px 20px;box-shadow:3px 4px 0 rgba(0,0,0,.07);min-width:0}
.slip p,.slip .passage{margin:0 0 .75em}
.slip .stem{font-weight:600}
.slip .paperfig{display:block;margin:.4em 0 .9em;height:auto;max-width:100%}
.opts{list-style:none;margin:.6em 0 0;padding:0;display:grid;gap:.35em}
.opts li{display:grid;grid-template-columns:2em minmax(0,1fr);gap:.4em}
.tbl-wrap{overflow-x:auto;margin:.4em 0 .9em}
.ptable{border-collapse:collapse;font-size:.92em;font-variant-numeric:tabular-nums}
.ptable th,.ptable td{border:1px solid #333;padding:3px 8px;text-align:center}
.ptable th{background:#f0efe9}
mark.hl{color:var(--slip-ink);padding:0 .12em;border-radius:3px;box-decoration-break:clone;-webkit-box-decoration-break:clone;
  background:linear-gradient(transparent 10%,var(--c) 10%,var(--c) 90%,transparent 90%)}
.hl-y{--c:var(--hl-y)}.hl-p{--c:var(--hl-p)}.hl-g{--c:var(--hl-g)}.hl-b{--c:var(--hl-b)}.hl-o{--c:var(--hl-o)}.hl-v{--c:var(--hl-v)}
sup.pin{font-family:var(--scrawl);font-weight:700;color:var(--red);font-size:.95em;margin-left:.08em}

.notes{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:1.06rem}
.notes li{display:grid;grid-template-columns:auto minmax(0,1fr);gap:8px;align-items:start}
.notes .pinbadge{font-family:var(--scrawl);font-weight:700;font-size:1.25rem;line-height:1;color:var(--slip-ink);
  width:1.6em;height:1.6em;display:grid;place-items:center;border-radius:50%;background:var(--c)}
.notes-title{font-family:var(--scrawl);font-size:1.6rem;color:var(--red);margin:0 0 6px;transform:rotate(-1.5deg)}

/* working */
.solution{margin-top:18px}
.solution h3{font-family:var(--scrawl);font-size:1.9rem;font-weight:700;margin:.2em 0 .3em;color:var(--pen)}
.steps{list-style:none;counter-reset:st;margin:0;padding:0;display:grid;gap:14px}
.steps>li{counter-increment:st;display:grid;grid-template-columns:4.2em minmax(0,1fr);gap:6px;align-items:start}
.steps>li::before{content:"Step " counter(st);font-family:var(--scrawl);font-weight:700;font-size:1.3rem;color:var(--red);line-height:1.4}
.steps p{margin:0 0 .4em}
.steps ul{margin:.2em 0 .4em;padding-left:1.2em}
.calc{font-size:1.2rem;line-height:1.75;color:var(--pen);padding:.2em 0 .2em .8em;border-left:3px solid var(--pen);margin:.35em 0 .5em}
.frac{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 .15em;line-height:1.15;font-size:.95em}
.frac>span:first-child{border-bottom:2px solid currentColor;padding:0 .25em}
.frac>span:last-child{padding:0 .25em}
svg.ar{width:1.7em;height:.85em;vertical-align:middle;stroke:currentColor;stroke-width:2.3;stroke-linecap:round;stroke-linejoin:round}
.ringed{display:inline-block;border:2.4px solid currentColor;border-radius:52% 48% 55% 45%/50% 55% 45% 50%;padding:0 .45em;transform:rotate(-3deg)}
.tickmark{color:var(--green);font-weight:700}.crossmark{color:var(--red);font-weight:700}
.k-red{color:var(--red)}.k-pen{color:var(--pen)}.k-green{color:var(--green)}.k-ink{color:var(--ink)}.k-orange{color:var(--orange)}.k-muted{color:var(--muted)}.k-violet{color:var(--violet)}
.sticky{background:var(--note-bg);color:var(--note-ink);padding:10px 14px;border-radius:2px;box-shadow:2px 3px 0 rgba(0,0,0,.12);
  transform:rotate(-.5deg);margin:.5em 0;max-width:62ch}
.sticky-label{font-family:var(--scrawl);font-weight:700;font-size:1.3rem;margin-right:.3em}
.sticky-trap .sticky-label{color:#b3231d}.sticky-tip .sticky-label{color:#1d4e9e}.sticky-check .sticky-label{color:#1b6d3b}

.answer{display:flex;gap:14px;align-items:center;margin:18px 0 8px}
.ans-letter{font-family:var(--scrawl);font-weight:700;font-size:2.6rem;color:var(--green);width:1.7em;height:1.7em;display:grid;
  place-items:center;border:3px solid var(--green);border-radius:50% 46% 52% 48%;transform:rotate(-6deg);flex:none}
.ans-text{font-size:1.15rem}
.others{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:8px}
.others li{display:grid;grid-template-columns:auto auto minmax(0,1fr);gap:8px;align-items:start}
.others .ol{font-family:var(--print);font-weight:700;font-size:.9rem;border:1.5px solid var(--ink);border-radius:3px;
  padding:0 .35em;line-height:1.5}
.others .why{min-width:0}
.fast{margin-top:16px}

/* critical thinking passage */
.seg{border-radius:3px;padding:.05em .1em;box-decoration-break:clone;-webkit-box-decoration-break:clone;color:var(--slip-ink);
  background:linear-gradient(transparent 8%,var(--c) 8%,var(--c) 92%,transparent 92%)}
.seg-ctx{--c:var(--hl-k)}.seg-prem{--c:var(--hl-b)}.seg-evid{--c:var(--hl-g)}.seg-analogy{--c:var(--hl-t)}
.seg-counter{--c:var(--hl-v)}.seg-ic{--c:var(--hl-o)}.seg-conc{--c:var(--hl-p)}
.seg-tag{font-family:var(--scrawl);font-weight:700;font-size:1.05rem;color:var(--red);margin:0 .25em 0 .1em;white-space:nowrap}
.ct-opts{list-style:none;margin:.6em 0 0;padding:0;display:grid;gap:.55em}
.ct-opts li{display:grid;grid-template-columns:2em minmax(0,1fr);gap:.4em;align-items:start}
.ct-opts li.right{background:var(--hl-g);outline:2px solid #2b8a4e;border-radius:4px;padding:.15em .3em;margin:0 -.3em}
.ct-why{font-family:var(--hand);font-size:1.06rem;color:#b3231d;display:block;margin-top:.1em}
.ct-opts li.right .ct-why{color:#17633a}
.ct-why svg.ar{color:#b3231d}
.ct-opts li.right .ct-why svg.ar{color:#17633a}
.work-box{border:2px solid var(--pen);border-radius:14px 10px 16px 9px;padding:12px 16px;margin-top:14px;max-width:72ch}
.work-box h4{font-family:var(--scrawl);font-size:1.5rem;margin:0 0 .3em;color:var(--pen)}
.skel{font-size:1.12rem;color:var(--pen)}
.map{display:grid;gap:8px;margin-top:.5em}
.map div{display:grid;grid-template-columns:2em minmax(0,1fr);gap:8px}

/* sketches */
.sketch-wrap{overflow-x:auto;margin:.5em 0 .7em}
svg.sketch{display:block;width:100%;min-width:320px;height:auto}
.rough{filter:url(#rough)}
.sketch line,.sketch path,.sketch rect,.sketch circle,.sketch polygon,.sketch polyline,.sketch ellipse{stroke-linecap:round;stroke-linejoin:round}
.sketch .k-pen{stroke:var(--pen)}.sketch .k-red{stroke:var(--red)}.sketch .k-green{stroke:var(--green)}.sketch .k-ink{stroke:var(--ink)}
.sketch .k-muted{stroke:var(--muted)}.sketch .k-orange{stroke:var(--orange)}.sketch .k-violet{stroke:var(--violet)}
.sketch .f-none{fill:none}.sketch .f-paper{fill:var(--paper)}.sketch .f-ink{fill:var(--ink)}
.sketch .f-y{fill:var(--fill-y)}.sketch .f-p{fill:var(--fill-p)}.sketch .f-g{fill:var(--fill-g)}.sketch .f-b{fill:var(--fill-b)}
.sketch .f-o{fill:var(--fill-o)}.sketch .f-v{fill:var(--fill-v)}
.sketch text{stroke:none}
.t-hand{font-family:var(--hand)}.t-scrawl{font-family:var(--scrawl);font-weight:700}.t-print{font-family:var(--print)}
.c-ink{fill:var(--ink)}.c-red{fill:var(--red)}.c-pen{fill:var(--pen)}.c-green{fill:var(--green)}.c-muted{fill:var(--muted)}
.c-orange{fill:var(--orange)}.c-violet{fill:var(--violet)}
.marker-pen{stroke:var(--pen)}.marker-red{stroke:var(--red)}.marker-green{stroke:var(--green)}.marker-ink{stroke:var(--ink)}
.marker-orange{stroke:var(--orange)}.marker-muted{stroke:var(--muted)}.marker-violet{stroke:var(--violet)}

/* practice mode hides the working, highlights and notes until "Show working" is pressed */
.reveal{display:none;margin-top:14px}
.practice .reveal{display:inline-block}
.practice .q:not(.shown) .solution,.practice .q:not(.shown) aside,.practice .q:not(.shown) .ct-why,
.practice .q:not(.shown) .gapnote,.practice .q:not(.shown) .work-box,.practice .q:not(.shown) .seg-tag,
.practice .q:not(.shown) sup.pin{display:none}
.practice .q:not(.shown) mark.hl,.practice .q:not(.shown) .seg{background:none}
.practice .q:not(.shown) .ct-opts li.right{background:none;outline:none}
.practice .q:not(.shown) .q-grid{grid-template-columns:minmax(0,1fr)}

.foot{margin-top:48px;color:var(--muted);font-size:.95rem;max-width:70ch}
@media (prefers-reduced-motion: reduce){*{transition:none!important}}
"""

DEFS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<filter id="rough" x="-3%" y="-3%" width="106%" height="106%"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="11" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="2.6" xChannelSelector="R" yChannelSelector="G"/></filter>
""" + ''.join(
    f'<marker id="ah-{c}" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
    f'<path d="M2 2 L10 6 L2 10" fill="none" class="marker-{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></marker>'
    for c in ('pen', 'red', 'green', 'ink', 'orange', 'muted', 'violet')) + '</defs></svg>'

JS = r"""
(function(){
  var KEY='tsa-ws-practice', root=document.documentElement, btn=document.getElementById('practice');
  function set(on){root.classList.toggle('practice',on);btn.setAttribute('aria-pressed',on?'true':'false');
    btn.textContent=on?'Practice mode: on (working hidden)':'Practice mode: off';try{localStorage.setItem(KEY,on?'1':'0')}catch(e){}}
  var saved=false;try{saved=localStorage.getItem(KEY)==='1'}catch(e){}
  set(saved);
  btn.addEventListener('click',function(){set(!root.classList.contains('practice'))});
  document.querySelectorAll('.reveal').forEach(function(b){b.addEventListener('click',function(){
    var q=b.closest('.q'), on=!q.classList.contains('shown');
    q.classList.toggle('shown',on); b.textContent=on?'Hide working':'Show working';});});
})();
"""


def load_content(year, kind):
    path = HERE / 'content' / f'y{year}_{kind}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f'y{year}_{kind}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.QUESTIONS


def check(year, kind, qs, keys):
    errs = []
    expected = keys[str(year)][KINDS[kind]['key']]
    if len(qs) != len(expected):
        errs.append(f'{len(qs)} questions, expected {len(expected)}')
    for q, (n, orig, ans) in zip(qs, expected):
        tag = f'{year} {kind} Q{q.get("n")}'
        if q.get('n') != n or q.get('orig') != orig:
            errs.append(f'{tag}: numbering n={q.get("n")} orig={q.get("orig")}, expected n={n} orig={orig}')
        if q.get('answer') != ans:
            errs.append(f'{tag}: answer {q.get("answer")} but the official key says {ans}')
        opts = q.get('options', {})
        if not opts or q.get('answer') not in opts:
            errs.append(f'{tag}: options missing or answer not among them')
        why = q.get('why', {})
        missing = [k for k in opts if k != q.get('answer') and k not in why]
        if missing:
            errs.append(f'{tag}: no "why" for wrong options {missing}')
        if kind == 'ps' and not q.get('steps'):
            errs.append(f'{tag}: no working steps')
        if kind == 'ct' and not q.get('passage'):
            errs.append(f'{tag}: no passage')
    return errs


def attempt_chip(q):
    a = q.get('attempt')
    if a is None:
        return ''
    if a == '':
        return '<span class="attempt blank">Your attempt: not reached</span>'
    ok = a == q['answer']
    return f'<span class="attempt {"good" if ok else "bad"}">Your attempt: {a} {"✓" if ok else "✗"}</span>'


def render_ps(year, q):
    notes = ''.join(
        f'<li><span class="pinbadge hl-{c}" style="background:var(--c)">{n}</span><span>{t}</span></li>'
        for n, c, t in q.get('notes', []))
    notes_html = (f'<aside><p class="notes-title">Reading it properly</p><ul class="notes">{notes}</ul></aside>'
                  if notes else '<aside></aside>')
    steps = ''.join(f'<li><div>{s}</div></li>' for s in q['steps'])
    others = ''.join(
        f'<li><span class="ol">{k}</span><span class="crossmark">✗</span><span class="why">{wslib.ar()} {q["why"][k]}</span></li>'
        for k in q['options'] if k != q['answer'])
    fast = (f'<div class="fast">{wslib.note(q["fast"], "tip")}</div>' if q.get('fast') else '')
    return f"""
<section class="q" id="q{q['n']}">
  <div class="q-head"><span class="qnum">{q['n']}</span><span class="qorig">(Q{q['orig']} in the original paper)</span>
    <span class="chip">{q.get('topic', '')}</span>{attempt_chip(q)}</div>
  <div class="q-grid">
    <div class="slip">{q['question']}{wslib.options(q['options'])}</div>
    {notes_html}
  </div>
  <button class="btn reveal" type="button">Show working</button>
  <div class="solution">
    <h3>Working it out</h3>
    <ol class="steps">{steps}</ol>
    <div class="answer"><span class="ans-letter">{q['answer']}</span><span class="ans-text">{q.get('answer_text', '')}</span></div>
    <h3>Why not the others?</h3>
    <ul class="others">{others}</ul>
    {fast}
  </div>
</section>"""


def render_ct(year, q):
    segs = q['passage']
    passage = ''
    for i, (role, text) in enumerate(segs):
        last_of_run = i + 1 == len(segs) or segs[i + 1][0] != role
        tag = f'<span class="seg-tag">{ROLE_LABEL[role]}</span>' if last_of_run else ''
        passage += f'<span class="seg seg-{role}">{text}</span>{tag} '
    opts = ''
    for k, v in q['options'].items():
        right = k == q['answer']
        reason = q.get('right', '') if right else q['why'][k]
        mark = wslib.tick() if right else wslib.cross()
        opts += (f'<li class="{"right" if right else ""}"><b>{k}</b><span>{v}'
                 f'<span class="ct-why">{mark} {wslib.ar("green" if right else "red")} {reason}</span></span></li>')
    gap = f'<div class="gapnote">{wslib.note(q["gap"], "tip")}</div>' if q.get('gap') else ''
    work = f'<div class="work-box"><h4>{q.get("working_title", "Working")}</h4>{q["working"]}</div>' if q.get('working') else ''
    return f"""
<section class="q" id="q{q['n']}">
  <div class="q-head"><span class="qnum">{q['n']}</span><span class="qorig">(Q{q['orig']} in the original paper)</span>
    <span class="chip">{q.get('type', '')}</span>{attempt_chip(q)}</div>
  <div class="slip ct-tag-wrap">
    <div class="passage">{passage}</div>
    <p class="stem">{q['stem']}</p>
    <ol class="ct-opts">{opts}</ol>
  </div>
  {gap}
  {work}
  <button class="btn reveal" type="button">Show working</button>
</section>"""


def render_page(year, kind, qs, fonts_css):
    meta = KINDS[kind]
    title = f'TSA {year} {meta["name"]} Solutions'
    if kind == 'ps':
        legend = ''.join(f'<span><span class="sw hl-{c}" style="background:var(--c)">highlight</span> {label}</span>'
                         for c, label in PS_COLOURS)
        lede = ('Every question in full, annotated, then worked through step by step with sketches. '
                'Numbers in brackets are the question numbers in the original paper.')
        body = ''.join(render_ps(year, q) for q in qs)
        nav = ''.join(f'<a href="#q{q["n"]}"><b>{q["n"]}</b><span>{q.get("topic", "")}</span>'
                      f'<i>{nav_mark(q)}</i></a>' for q in qs)
    else:
        legend = ''.join(f'<span><span class="sw seg-{r}" style="background:var(--c)">{label}</span></span>'
                         for r, label in CT_ROLES)
        lede = ('Each argument is colour-coded by the job each sentence does. The right answer is highlighted, '
                'and every wrong option gets a quick note on why it fails.')
        body = ''.join(render_ct(year, q) for q in qs)
        nav = ''.join(f'<a href="#q{q["n"]}"><b>{q["n"]}</b><span>{q.get("type", "")}</span>'
                      f'<i>{nav_mark(q)}</i></a>' for q in qs)
    copy = (f'© Cambridge University Press &amp; Assessment {year}' if int(year) >= 2022 else f'© UCLES {year}')
    return f"""<title>{title}</title>
<style>{fonts_css}{CSS}</style>
{DEFS}
<div class="wrap">
  <header class="page-head">
    <p class="eyebrow">TSA {year} · worked solutions</p>
    <h1>{meta['name']}</h1>
    <p class="lede">{lede}</p>
    <div class="legend">{legend}</div>
    <div class="controls"><button class="btn" id="practice" type="button" aria-pressed="false">Practice mode: off</button>
      <span style="color:var(--muted)">Turn practice mode on to hide the working until you have had a go.</span></div>
    <nav class="nav" aria-label="Questions">{nav}</nav>
  </header>
  <main>{body}</main>
  <p class="foot">Questions {copy}, reproduced from the TSA Oxford {year} Section 1 paper for practice.
    Answers match the official answer key.</p>
</div>
<script>{JS}</script>
"""


def nav_mark(q):
    a = q.get('attempt')
    if a is None:
        return ''
    if a == '':
        return '–'
    return '✓' if a == q['answer'] else '✗'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('years', nargs='*')
    ap.add_argument('--out', default=REPO / 'TSA_Worked_Solutions', type=Path)
    ap.add_argument('--artifact-dir', type=Path)
    ap.add_argument('--kind', choices=list(KINDS), help='build only this set')
    args = ap.parse_args()
    keys = json.loads((HERE / 'keys.json').read_text())
    fonts_css = (font_face('Patrick Hand', 'patrick-hand-latin-400-normal.woff2', 400)
                 + font_face('Caveat', 'caveat-latin-400-normal.woff2', 400)
                 + font_face('Caveat', 'caveat-latin-700-normal.woff2', 700))
    years = args.years or sorted(keys)
    args.out.mkdir(parents=True, exist_ok=True)
    problems = []
    for year in years:
        for kind, meta in KINDS.items():
            if args.kind and kind != args.kind:
                continue
            qs = load_content(year, kind)
            if qs is None:
                continue
            errs = check(year, kind, qs, keys)
            if errs:
                problems += errs
                continue
            page = render_page(year, kind, qs, fonts_css)
            name = f'TSA_{year}_{meta["slug"]}_Worked_Solutions.html'
            full = ('<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8">'
                    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                    f'</head><body>{page}</body></html>\n')
            (args.out / name).write_text(full, encoding='utf-8')
            if args.artifact_dir:
                args.artifact_dir.mkdir(parents=True, exist_ok=True)
                (args.artifact_dir / name).write_text(page, encoding='utf-8')
            print(f'{name}: {len(qs)} questions, {len(full) // 1024} KB')
    if problems:
        print('\nNOT BUILT because of these problems:')
        for p in problems:
            print('  -', p)
        sys.exit(1)


if __name__ == '__main__':
    main()
