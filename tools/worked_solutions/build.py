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
import written  # noqa: E402
import mock  # noqa: E402

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
  --wm-bg:rgba(255,255,255,.6); --wm-edge:rgba(31,78,168,.28);
  --print:Arial,"Helvetica Neue",Helvetica,sans-serif;
  --hand:"Patrick Hand","Bradley Hand","Segoe Print","Comic Sans MS",cursive;
  --scrawl:"Caveat","Bradley Hand","Segoe Print","Comic Sans MS",cursive;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --paper:#16211d; --grid:rgba(255,255,255,.045); --ink:#e7ece8; --muted:#a3aea8;
  --pen:#9cc3ff; --red:#ff8d84; --green:#86e0a6; --orange:#ffc07d; --violet:#c9b0ff;
  --fill-y:#5a5016; --fill-p:#5c2742; --fill-g:#1d4f33; --fill-b:#1b3d63; --fill-o:#653d13; --fill-v:#3d2d68;
  --chip:#23312b; --chip-ink:#dfe6e1; --wm-bg:rgba(255,255,255,.04); --wm-edge:rgba(156,195,255,.3); color-scheme:dark;
}}
:root[data-theme="dark"]{
  --paper:#16211d; --grid:rgba(255,255,255,.045); --ink:#e7ece8; --muted:#a3aea8;
  --pen:#9cc3ff; --red:#ff8d84; --green:#86e0a6; --orange:#ffc07d; --violet:#c9b0ff;
  --fill-y:#5a5016; --fill-p:#5c2742; --fill-g:#1d4f33; --fill-b:#1b3d63; --fill-o:#653d13; --fill-v:#3d2d68;
  --chip:#23312b; --chip-ink:#dfe6e1; --wm-bg:rgba(255,255,255,.04); --wm-edge:rgba(156,195,255,.3); color-scheme:dark;
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
.anschip{margin-left:auto;border-radius:999px;padding:1px 4px 1px 12px;font-size:.95rem;background:var(--fill-g);color:var(--ink);
  display:inline-flex;align-items:center;gap:8px}
.anschip b{font-family:var(--scrawl);font-size:1.4rem;line-height:1;width:1.35em;height:1.35em;display:grid;place-items:center;
  border-radius:50%;background:var(--green);color:var(--paper)}
.whyhere{margin:-2px 0 14px;padding:8px 14px;border-radius:12px 9px 13px 8px;background:var(--fill-v);color:var(--ink);
  font-size:1.02rem;max-width:84ch;border-left:5px solid var(--violet)}
.whyhere b{font-family:var(--scrawl);font-size:1.3rem;color:var(--violet);margin-right:.4em}
.whyhere .debate{display:block;margin-top:6px;padding-top:6px;border-top:1.5px dashed var(--violet)}
.whyhere .debate b{color:var(--red)}
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
.qfoot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:8px;margin-top:20px;font-size:1rem}
.qfoot a{color:var(--pen);text-decoration:none;border:1.5px solid currentColor;border-radius:10px 8px 11px 7px;padding:.05em .7em}
.qfoot a:hover{background:var(--pen);color:var(--paper)}

/* written methods (column addition and subtraction, multiplication, bus stop and long division) */
.wms{display:flex;flex-wrap:wrap;gap:10px 14px;margin:.25em 0 .8em;align-items:flex-start}
.wm{border:1.5px solid var(--wm-edge);border-radius:12px 9px 13px 8px;padding:6px 12px 8px;background:var(--wm-bg);max-width:100%;overflow-x:auto}
.wm-cap{font-family:var(--scrawl);font-weight:700;font-size:1.05rem;line-height:1.15;color:var(--red);margin-bottom:4px}
.wm table{border-collapse:collapse;font-family:var(--hand);font-size:1.35rem;line-height:1;color:var(--pen);font-variant-numeric:tabular-nums}
.wm td{min-width:.95em;height:1.45em;padding:0 .04em;text-align:center;vertical-align:middle;position:relative}
.wm td.pt{min-width:.3em;width:.3em}
.wm table.bus td:not(.dv):not(.pt){min-width:1.45em;padding-left:.5em}
.wm td.op{color:var(--ink);padding-right:.15em}
.wm td.sum{border-top:2px solid var(--ink)}
.wm tr.res td,.wm td.qt{color:var(--green)}
.wm tr.first td:not(.lab):not(:first-child){border-top:2px solid var(--ink)}
.wm .fz{opacity:.4}
.wm tr.cyrow td{height:1em;vertical-align:top}
.wm td.cy{font-size:.62em;color:var(--red)}
.wm tr.ex-row td{height:2.15em;vertical-align:bottom;padding-bottom:.12em}
.wm .x{text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:2px}
.wm .nv{position:absolute;left:50%;top:.1em;transform:translateX(-50%);font-size:.62em;color:var(--red);white-space:nowrap}
.wm .ci{position:absolute;left:.08em;top:.05em;font-size:.6em;color:var(--red)}
.wm td.roof{border-top:2px solid var(--ink)}
.wm td.wall{border-left:2px solid var(--ink);border-top-left-radius:12px}
.wm td.dv{padding-right:.35em;text-align:right;color:var(--ink)}
.wm td.lab{font-size:.62em;color:var(--muted);text-align:left;padding-left:.7em;white-space:nowrap}
.wm-note{font-family:var(--hand);font-size:.98rem;color:var(--muted);margin-top:4px;max-width:32ch}
.no-wm .wms{display:none}
@media (max-width:700px){.wms{flex-wrap:nowrap;overflow-x:auto;scroll-snap-type:x proximity;padding-bottom:6px}.wm{flex:none;scroll-snap-align:start}}
svg.dvs{display:inline-block;width:.68em;height:.68em;vertical-align:-.02em;margin:0 .1em;stroke:currentColor;stroke-width:1.9;
  stroke-linecap:round;fill:currentColor}
svg.dvs path{fill:none}svg.dvs circle{stroke:none}
.dvt{font-family:Arial,Helvetica,sans-serif;font-weight:700}

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
.sketch .f-none{fill:none}.sketch .f-paper{fill:var(--paper)}.sketch .f-ink{fill:var(--ink)}.sketch .f-black{fill:#1d1f23}
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
.practice .q:not(.shown) sup.pin,.practice .q:not(.shown) .anschip,.practice .q:not(.shown) .whyhere{display:none}
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
  if(!btn)return;
  function set(on){root.classList.toggle('practice',on);btn.setAttribute('aria-pressed',on?'true':'false');
    btn.textContent=on?'Practice mode: on (working hidden)':'Practice mode: off';try{localStorage.setItem(KEY,on?'1':'0')}catch(e){}}
  var saved=false;try{saved=localStorage.getItem(KEY)==='1'}catch(e){}
  set(saved);
  btn.addEventListener('click',function(){set(!root.classList.contains('practice'))});
  var wm=document.getElementById('wm-toggle'), WKEY='tsa-ws-methods';
  function setWm(on){root.classList.toggle('no-wm',!on);wm.setAttribute('aria-pressed',on?'true':'false');
    wm.textContent=on?'Written methods: shown':'Written methods: hidden';try{localStorage.setItem(WKEY,on?'1':'0')}catch(e){}}
  if(wm){var wsaved=true;try{wsaved=localStorage.getItem(WKEY)!=='0'}catch(e){}
    setWm(wsaved);wm.addEventListener('click',function(){setWm(root.classList.contains('no-wm'))});}
  document.querySelectorAll('.reveal').forEach(function(b){b.addEventListener('click',function(){
    var q=b.closest('.q'), on=!q.classList.contains('shown');
    q.classList.toggle('shown',on); b.textContent=on?'Hide working':'Show working';});});
})();
"""


def load_content(year, kind):
    if mock.is_mock(year):
        return mock.load(str(year), kind, load_content)
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


def orig_label(q):
    if q.get('src'):
        return f'(TSA {q["src"]}, Q{q["orig"]})'
    return f'(Q{q["orig"]} in the original paper)'


RANK_WORD = {1: 'the hardest', 2: 'the second-hardest', 3: 'the third-hardest', 4: 'the fourth-hardest'}


def fmt_minutes(m):
    """3.5 -> '3½ minutes', 4 -> '4 minutes' (rounded to the nearest half minute)."""
    half = round(m * 2) / 2
    whole = int(half)
    return f'{whole}{"½" if half != whole else ""} minutes'


def ordinal(n):
    return f'{n}{"th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")}'


def why_here(q):
    """For a mock question: why it was chosen, what makes it hard, and any doubt about the official answer."""
    if not q.get('mock_style'):
        return ''
    seen = (' You have met this one before: it was in the 2014 paper you sat.' if q.get('src') == '2014' else '')
    if q['mock_style'] == 'longest':
        r, m = q.get('mock_rank', 1), q.get('mock_minutes')
        mins = f' A strong candidate needs about {fmt_minutes(m)} on it.' if m else ''
        lead = f'judged the {"" if r == 1 else ordinal(r) + "-"}longest sustained workout of the 25.{mins} '
    elif q['mock_style'] == 'hardest':
        r = q.get('mock_rank', 1)
        lead = f'judged the {"" if r == 1 else ordinal(r) + "-"}hardest of the 25. '
    else:
        rank = RANK_WORD.get(q.get('mock_rank', 1), 'one of the hardest')
        lead = f'{rank} <i>{q["mock_type"]}</i> question in the past papers. '
    debate = (f'<span class="debate"><b>Debatable</b>{q["debate"]} This mock marks the official answer as correct.</span>'
              if q.get('debate') else '')
    return f'<p class="whyhere"><b>Why it\'s here</b>{lead}{q.get("why_here", "")}{seen}{debate}</p>'


def answer_chip(q):
    return f'<span class="anschip">Answer <b>{q["answer"]}</b></span>'


def render_ps(year, q):
    notes = ''.join(
        f'<li><span class="pinbadge hl-{c}" style="background:var(--c)">{n}</span><span>{t}</span></li>'
        for n, c, t in q.get('notes', []))
    notes_html = (f'<aside><p class="notes-title">Reading it properly</p><ul class="notes">{notes}</ul></aside>'
                  if notes else '<aside></aside>')
    done = set()
    key = f'{q.get("src", year)}-{q.get("src_n", q["n"])}'
    steps = ''.join(f'<li><div>{written.add_methods(s, done, key)}</div></li>' for s in q['steps'])
    others = ''.join(
        f'<li><span class="ol">{k}</span><span class="crossmark">✗</span><span class="why">{wslib.ar()} {q["why"][k]}</span></li>'
        for k in q['options'] if k != q['answer'])
    fast = (f'<div class="fast">{wslib.note(q["fast"], "tip")}</div>' if q.get('fast') else '')
    return f"""
<section class="q" id="q{q['n']}">
  <div class="q-head"><span class="qnum">{q['n']}</span><span class="qorig">{orig_label(q)}</span>
    <span class="chip">{q.get('topic', '')}</span>{attempt_chip(q)}{answer_chip(q)}</div>
  {why_here(q)}
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
  <div class="q-head"><span class="qnum">{q['n']}</span><span class="qorig">{orig_label(q)}</span>
    <span class="chip">{q.get('type', '')}</span>{attempt_chip(q)}{answer_chip(q)}</div>
  {why_here(q)}
  <div class="slip ct-tag-wrap">
    <div class="passage">{passage}</div>
    <p class="stem">{q['stem']}</p>
    <ol class="ct-opts">{opts}</ol>
  </div>
  {gap}
  {work}
  <button class="btn reveal" type="button">Show working</button>
</section>"""


def with_foot(section, n, total):
    """Add previous / all / next links to the end of a question."""
    prev = f'<a href="#q{n - 1}">← Question {n - 1}</a>' if n > 1 else '<span></span>'
    nxt = f'<a href="#q{n + 1}">Question {n + 1} →</a>' if n < total else '<span></span>'
    foot = f'<nav class="qfoot" aria-label="Move between questions">{prev}<a href="#questions">All questions</a>{nxt}</nav>'
    head, _, tail = section.rpartition('</section>')
    return head + foot + '</section>' + tail


def render_main(year, kind, qs):
    """The page content: header, questions and footer (no styles or scripts)."""
    meta = KINDS[kind]
    if kind == 'ps':
        legend = ''.join(f'<span><span class="sw hl-{c}" style="background:var(--c)">highlight</span> {label}</span>'
                         for c, label in PS_COLOURS)
        lede = ('Every question in full, annotated, then worked through step by step with sketches. '
                'Numbers in brackets are the question numbers in the original paper.')
        body = ''.join(with_foot(render_ps(year, q), q['n'], len(qs)) for q in qs)
        nav = ''.join(f'<a href="#q{q["n"]}"><b>{q["n"]}</b><span>{q.get("topic", "")}</span>'
                      f'<i>{nav_mark(q)}</i></a>' for q in qs)
        wm_btn = ('<button class="btn" id="wm-toggle" type="button" aria-pressed="true">Written methods: shown</button>'
                  if 'class="wms"' in body else '')
    else:
        legend = ''.join(f'<span><span class="sw seg-{r}" style="background:var(--c)">{label}</span></span>'
                         for r, label in CT_ROLES)
        lede = ('Each argument is colour-coded by the job each sentence does. The right answer is highlighted, '
                'and every wrong option gets a quick note on why it fails.')
        body = ''.join(with_foot(render_ct(year, q), q['n'], len(qs)) for q in qs)
        nav = ''.join(f'<a href="#q{q["n"]}"><b>{q["n"]}</b><span>{q.get("type", "")}</span>'
                      f'<i>{nav_mark(q)}</i></a>' for q in qs)
        wm_btn = ''
    if not str(year).isdigit():
        copy, source = mock.COPYRIGHT, 'the TSA Oxford Section 1 papers'
    else:
        copy = (f'© Cambridge University Press &amp; Assessment {year}' if int(year) >= 2022 else f'© UCLES {year}')
        source = f'the TSA Oxford {year} Section 1 paper'
    return written.clear_division(f"""<div class="wrap">
  <header class="page-head">
    <p class="eyebrow">TSA {mock.label(year)} · worked solutions</p>
    <h1>{meta['name']}</h1>
    <p class="lede">{lede}</p>
    <div class="legend">{legend}</div>
    <div class="controls"><button class="btn" id="practice" type="button" aria-pressed="false">Practice mode: off</button>{wm_btn}
      <span style="color:var(--muted)">Turn practice mode on to hide the working until you have had a go.</span></div>
    <nav class="nav" id="questions" aria-label="Questions">{nav}</nav>
  </header>
  <main>{body}</main>
  <p class="foot">Questions {copy}, reproduced from {source} for practice.
    Answers match the official answer key.</p>
</div>""")


def render_page(year, kind, qs, fonts_css):
    title = f'TSA {mock.label(year)} {KINDS[kind]["name"]} Solutions'
    return f"""<title>{title}</title>
<style>{fonts_css}{CSS}</style>
{DEFS}
{render_main(year, kind, qs)}
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
    keys.update(mock.keys(keys))
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
