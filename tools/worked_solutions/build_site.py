"""Build the TSA website in TSA_Website/.

    python tools/worked_solutions/build_site.py
    python tools/worked_solutions/build_site.py --artifact-dir DIR   # also write a body-only home page for publishing

Pages (all relative links, so the folder works offline and when hosted):
    index.html                                       every year as a card
    TSA_<year>.html                                  the six pages for that year
    TSA_<year>_<Set>_Answers.html                    the mark scheme; each answer links to its worked solution
    TSA_<year>_<Set>_Worked_Solutions.html           the worked solutions
    TSA_<year>_<Set>_Paper.html                      the question paper to read on screen
    assets/tsa.css, assets/tsa.js                    shared styles (fonts built in) and scripts

<Set> is Critical_Thinking or Problem_Solving. Paper pages are rendered from TSA_Papers/ (page images are cached
in tools/worked_solutions/.cache/). Worked solutions come from the same content files as TSA_Worked_Solutions/.
"""

import argparse
import base64
import html
import io
import json
import sys
from pathlib import Path

import pymupdf
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

REPO = build.REPO
TARA = {'questions': 22, 'minutes': 40}   # per module, as in tools/build_tsa_sets.py
SETS = [('ct', 'Critical Thinking', 'CT'), ('ps', 'Problem Solving', 'PS')]
WHAT = [('ans', 'Answers'), ('sol', 'Worked solutions'), ('paper', 'Question paper')]
WHAT_LABEL = dict(WHAT)
COVERS = 8
CACHE = HERE / '.cache' / 'papers'
CURRENT = ' aria-current="page"'

SITE_CSS = r"""
/* ---------------------------------------------------------------- site shell
   Quiet, clean chrome (system font, white cards, a side menu with every page) around the
   hand-written worked solutions. Handwriting is kept for big headings and for the working itself. */
:root{
  --ui:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --bar-h:56px; --side-w:256px;
  --surface:#ffffff; --surface-2:#ecebe3; --line:rgba(36,39,44,.13); --line-2:rgba(36,39,44,.28);
  --bar-bg:rgba(246,245,239,.94); --shadow:rgba(40,40,20,.09); --scrim:rgba(20,24,28,.45);
  --accent-soft:#e1e9f7; --on-accent:#ffffff; --ok:#1d7a42; --ok-soft:#dcf2e3; --bad:#c42f2a; --bad-soft:#fbe1de;
  --cover-1:#2f5fb3; --cover-2:#c2413b; --cover-3:#2f8a55; --cover-4:#d4a22b;
  --cover-5:#7a4fb8; --cover-6:#d6732a; --cover-7:#cc5a88; --cover-8:#23878a;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --surface:#1c2823; --surface-2:#26352f; --line:rgba(255,255,255,.11); --line-2:rgba(255,255,255,.26);
  --bar-bg:rgba(22,33,29,.94); --shadow:rgba(0,0,0,.35); --scrim:rgba(0,0,0,.6);
  --accent-soft:#1f3350; --on-accent:#0e1814; --ok:#86e0a6; --ok-soft:#1c3a29; --bad:#ff8d84; --bad-soft:#4a2421;
  --cover-1:#3b66ad; --cover-2:#b0473f; --cover-3:#358457; --cover-4:#b8902f;
  --cover-5:#7552a8; --cover-6:#b8692e; --cover-7:#b0587d; --cover-8:#2b8083;
}}
:root[data-theme="dark"]{
  --surface:#1c2823; --surface-2:#26352f; --line:rgba(255,255,255,.11); --line-2:rgba(255,255,255,.26);
  --bar-bg:rgba(22,33,29,.94); --shadow:rgba(0,0,0,.35); --scrim:rgba(0,0,0,.6);
  --accent-soft:#1f3350; --on-accent:#0e1814; --ok:#86e0a6; --ok-soft:#1c3a29; --bad:#ff8d84; --bad-soft:#4a2421;
  --cover-1:#3b66ad; --cover-2:#b0473f; --cover-3:#358457; --cover-4:#b8902f;
  --cover-5:#7552a8; --cover-6:#b8692e; --cover-7:#b0587d; --cover-8:#2b8083;
}
html{scroll-padding-top:calc(var(--bar-h) + 16px)}
.app{font-family:var(--ui);font-size:16px;line-height:1.55}
.ws{font-family:var(--hand);font-size:18px;line-height:1.5;container-type:inline-size}
@container (max-width:800px){.ws .q-grid{grid-template-columns:minmax(0,1fr)}}
.q{scroll-margin-top:calc(var(--bar-h) + 16px)}
button{font-family:inherit}

/* top bar */
.topbar{position:sticky;top:env(safe-area-inset-top,0px);z-index:30;height:var(--bar-h);background:var(--bar-bg);
  border-bottom:1px solid var(--line);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.topbar-in{height:100%;max-width:1440px;margin:0 auto;padding-inline:16px;display:flex;align-items:center;gap:10px}
.brand{display:flex;align-items:baseline;gap:.3em;text-decoration:none;color:var(--ink);font-family:var(--scrawl);font-weight:700;
  font-size:1.6rem;line-height:1;white-space:nowrap}
.brand mark{color:var(--slip-ink);padding:0 .15em;background:linear-gradient(transparent 18%,var(--hl-y) 18%,var(--hl-y) 86%,transparent 86%)}
.icon-btn,.tbtn{font:inherit;font-size:.92rem;display:inline-flex;align-items:center;justify-content:center;gap:6px;height:36px;
  padding:0 12px;border-radius:9px;border:1px solid var(--line-2);background:var(--surface);color:var(--ink);cursor:pointer;
  text-decoration:none;white-space:nowrap}
.icon-btn:hover,.tbtn:hover{background:var(--surface-2)}
.icon-btn svg,.tbtn svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;flex:none}
.tbtn.primary{background:var(--pen);border-color:var(--pen);color:var(--on-accent)}
.tbtn.primary:hover{filter:brightness(1.08)}
.menu-btn{display:none}
.yearstep{margin-left:auto;display:flex;align-items:center;gap:6px}
.yearstep .now{font-weight:700;font-variant-numeric:tabular-nums;padding:0 4px}
.yearstep .off{opacity:.35;pointer-events:none}

/* side menu: a column on wide screens, a drawer on small ones */
.shell.has-side{display:grid;grid-template-columns:var(--side-w) minmax(0,1fr);max-width:1440px;margin:0 auto}
.side{position:sticky;top:calc(env(safe-area-inset-top,0px) + var(--bar-h));align-self:start;
  max-height:calc(100dvh - var(--bar-h) - env(safe-area-inset-top,0px));overflow:auto;padding:20px 14px 32px 16px;
  border-right:1px solid var(--line);font-size:.95rem}
.side-head{display:none}
.side-all{display:inline-flex;align-items:center;gap:6px;color:var(--pen);text-decoration:none;font-size:.9rem;margin-bottom:10px}
.side-all svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.side-title{font-family:var(--scrawl);font-weight:700;font-size:2rem;line-height:1;margin:0 0 12px}
.side-title a{color:inherit;text-decoration:none}
.side-title a:hover{color:var(--pen)}
.side-set{margin:0 0 16px}
.side h3,.side h2{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 6px;font-weight:600}
.side-set a{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;color:var(--ink);text-decoration:none}
.side-set a::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--c);flex:none}
.side-set a:hover{background:var(--surface-2)}
.side-set a[aria-current="page"]{background:var(--accent-soft);color:var(--pen);font-weight:600}
.side-years{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:4px}
.side-years a{display:block;text-align:center;padding:6px 0;border-radius:7px;color:var(--ink);text-decoration:none;font-size:.88rem;
  font-variant-numeric:tabular-nums}
.side-years a:hover{background:var(--surface-2)}
.side-years a[aria-current="page"]{background:var(--pen);color:var(--on-accent);font-weight:700}
.side-hint{font-size:.8rem;color:var(--muted);margin:0 0 8px}
.scrim{position:fixed;inset:0;background:var(--scrim);z-index:45}
.scrim[hidden]{display:none}
@media (max-width:999px){
  .shell.has-side{display:block}
  .menu-btn{display:inline-flex}
  .side{position:fixed;top:0;bottom:0;left:0;z-index:50;width:min(320px,86vw);max-height:none;background:var(--paper);
    padding-top:calc(14px + env(safe-area-inset-top,0px));padding-bottom:calc(28px + env(safe-area-inset-bottom,0px));
    box-shadow:6px 0 28px var(--shadow);transform:translateX(-105%);visibility:hidden;transition:transform .22s ease,visibility 0s linear .22s}
  .menu-open .side{transform:none;visibility:visible;transition:transform .22s ease}
  .side-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
  .side-head b{font-size:1.05rem}
}
@media (max-width:520px){.brand span{display:none}.yearstep .lbl{display:none}}

/* content */
.content{min-width:0}
.pagebar{max-width:1120px;margin:0 auto;padding-inline:16px;padding-block:18px 0;display:grid;gap:12px}
.crumbs{font-size:.9rem;color:var(--muted)}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px 8px;align-items:center}
.crumbs li+li::before{content:"\203A";margin-right:8px}
.crumbs a{color:var(--pen);text-decoration:none}
.crumbs a:hover{text-decoration:underline}
.pagetabs{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.seg{display:inline-flex;gap:2px;padding:3px;border-radius:11px;background:var(--surface-2);max-width:100%;min-width:0;overflow-x:auto;scrollbar-width:none}
.seg .s{display:none}
@media (max-width:520px){.seg .l{display:none}.seg .s{display:inline}.seg a{padding:6px 11px}}
.seg::-webkit-scrollbar{display:none}
.seg a{padding:6px 13px;border-radius:8px;text-decoration:none;color:var(--ink);font-size:.92rem;white-space:nowrap}
.seg a:hover{background:var(--surface)}
.seg a[aria-current="page"]{background:var(--surface);box-shadow:0 1px 3px var(--shadow);font-weight:600}
.switch{font-size:.9rem;color:var(--pen);text-decoration:none;white-space:nowrap}
.switch:hover{text-decoration:underline}
.pagebar + .wrap,.pagebar + .ws .wrap{padding-top:20px}
.app .page-head h1{font-size:clamp(2.3rem,6vw,3.3rem)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.app .chip{font-size:.85rem;padding:2px 10px}
.foot{font-size:.88rem}

/* home */
.home-head{display:grid;gap:12px;margin-bottom:22px}
.home-head h1{font-family:var(--scrawl);font-weight:700;font-size:clamp(2.5rem,7vw,3.8rem);line-height:1;margin:0}
.home-head .lede{font-size:1.05rem}
.continue{display:flex;align-items:center;gap:14px;max-width:620px;margin:0 0 22px;padding:12px 16px;background:var(--surface);
  border:1px solid var(--line);border-radius:12px;text-decoration:none;color:var(--ink);box-shadow:0 1px 3px var(--shadow)}
.continue[hidden]{display:none}
.continue:hover{border-color:var(--pen)}
.continue small{display:block;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.continue svg{width:22px;height:22px;stroke:var(--pen);fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;margin-left:auto;flex:none}
.years{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
@media (max-width:640px){.years{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}
.ycard{position:relative;display:grid;gap:2px;height:100%;padding:14px 14px 14px 24px;background:var(--surface);border:1px solid var(--line);
  border-radius:12px;text-decoration:none;color:var(--ink);box-shadow:0 1px 3px var(--shadow);overflow:hidden;
  transition:transform .15s ease,box-shadow .15s ease,border-color .15s ease}
.ycard::before{content:"";position:absolute;left:0;top:0;bottom:0;width:9px;background:var(--cv)}
.ycard:hover,.ycard:focus-visible{transform:translateY(-2px);box-shadow:0 8px 20px var(--shadow);border-color:var(--line-2)}
.ycard-year{font-family:var(--scrawl);font-weight:700;font-size:2.5rem;line-height:1}
.ycard-sub{font-size:.85rem;color:var(--muted)}
.ycard-tag{position:absolute;top:10px;right:10px;font-size:.72rem;font-weight:600;background:var(--note-bg);color:var(--note-ink);
  padding:2px 8px;border-radius:999px}
.cv-1{--cv:var(--cover-1)}.cv-2{--cv:var(--cover-2)}.cv-3{--cv:var(--cover-3)}.cv-4{--cv:var(--cover-4)}
.cv-5{--cv:var(--cover-5)}.cv-6{--cv:var(--cover-6)}.cv-7{--cv:var(--cover-7)}.cv-8{--cv:var(--cover-8)}
.howto{margin-top:34px;display:grid;gap:10px;max-width:760px}
.howto h2{font-family:var(--scrawl);font-weight:700;font-size:2rem;margin:0;line-height:1}
.howto ol{margin:0;padding:0;list-style:none;counter-reset:h;display:grid;gap:10px}
.howto li{counter-increment:h;display:grid;grid-template-columns:2.2em minmax(0,1fr);gap:10px;align-items:start}
.howto li::before{content:counter(h);font-family:var(--scrawl);font-weight:700;font-size:1.4rem;line-height:1;color:var(--red);
  width:1.5em;height:1.5em;display:grid;place-items:center;border:2px solid currentColor;border-radius:50% 46% 52% 48%}
.facts{background:var(--note-bg);color:var(--note-ink);padding:10px 14px;border-radius:3px;box-shadow:2px 3px 0 var(--shadow);
  max-width:62ch;margin:26px 0 0;transform:rotate(-.4deg)}
.facts b{font-family:var(--scrawl);font-size:1.25rem;margin-right:.2em}

/* year page */
.year-head{display:grid;gap:8px;margin-bottom:22px}
.year-head h1{font-family:var(--scrawl);font-weight:700;font-size:clamp(3rem,9vw,4.6rem);line-height:.95;margin:0}
.year-head .facts{margin:6px 0 0}
.sets{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;align-items:start}
@media (max-width:760px){.sets{grid-template-columns:minmax(0,1fr)}}
.set{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px;display:grid;gap:10px;
  box-shadow:0 1px 3px var(--shadow);min-width:0}
.set-ct{--c:var(--hl-p)}.set-ps{--c:var(--hl-b)}
.set h2{font-family:var(--scrawl);font-weight:700;font-size:2.1rem;line-height:1.05;margin:0}
.set h2 span{padding:0 .1em;background:linear-gradient(transparent 64%,var(--c) 64%,var(--c) 92%,transparent 92%)}
.set .meta{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:center;font-size:.88rem;color:var(--muted);margin:0 0 4px}
.choice{display:grid;grid-template-columns:46px minmax(0,1fr) 20px;gap:12px;align-items:center;padding:12px;border-radius:11px;
  border:1px solid var(--line);background:var(--paper);text-decoration:none;color:var(--ink);transition:border-color .15s,background .15s}
.choice:hover,.choice:focus-visible{border-color:var(--pen);background:var(--accent-soft)}
.choice b{display:block;font-weight:600;font-size:1.05rem;line-height:1.3}
.choice .d{display:block;font-size:.88rem;color:var(--muted);line-height:1.4;margin-top:2px}
.choice svg.doodle{width:46px;height:46px}
.choice .go{width:20px;height:20px;stroke:var(--muted);fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}

/* answers page */
.sheet{background:var(--slip);color:var(--slip-ink);border:1px solid var(--slip-edge);box-shadow:0 1px 3px var(--shadow);border-radius:4px;
  padding:18px 20px 20px;max-width:920px;display:grid;gap:12px;min-width:0}
.sheet-head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;font-family:var(--print);font-size:.9rem;
  border-bottom:2px solid var(--slip-ink);padding-bottom:6px}
.sheet-head b{font-size:1rem}
.sheet-tip{margin:0;font-size:.92rem;color:#5b5f66}
.ans-grid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}
.ans{position:relative;display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--slip-ink);border:1.5px solid var(--slip-edge);
  border-radius:9px;padding:8px 10px;min-height:58px;transition:background .15s}
a.ans:hover,a.ans:focus-visible{background:var(--hl-g)}
.ans .n{font-family:var(--scrawl);font-weight:700;font-size:1.5rem;color:#c42f2a;min-width:1.3em;line-height:1}
.ans .L{font-family:var(--scrawl);font-weight:700;font-size:1.9rem;color:#1d7a42;width:1.5em;height:1.5em;display:grid;place-items:center;
  border:2.5px solid currentColor;border-radius:50% 46% 52% 48%;transform:rotate(-5deg);line-height:1}
.ans .see{font-size:.8rem;color:#5b5f66;margin-left:auto;white-space:nowrap}
.ans .you{position:absolute;top:3px;right:6px;font-size:.7rem;font-weight:700}
.ans.good .you{color:#1b6d3b}.ans.bad .you{color:#b3231d}.ans.blank .you{color:#5b5f66}
.ans.bad{border-color:#e7a29c}
@media (max-width:860px){.ans .see{display:none}}
@media (max-width:560px){
  .ans-grid{gap:5px}
  .ans{flex-direction:column;gap:2px;padding:6px 2px 7px;min-height:0}
  .ans .n{font-size:1.25rem;min-width:0}
  .ans .L{font-size:1.5rem}
  .ans .you{position:static;font-size:.62rem}
}
.score{font-family:var(--scrawl);font-weight:700;font-size:1.6rem;color:#c42f2a;margin:0}
.next{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}

/* question paper page */
.paper-tools .links{display:flex;flex-wrap:wrap;gap:8px;margin-left:auto}
.paper-tools{position:sticky;top:calc(env(safe-area-inset-top,0px) + var(--bar-h));z-index:20;display:flex;flex-wrap:wrap;align-items:center;
  gap:8px 12px;min-height:var(--tools-h);padding-block:10px;margin-bottom:16px;background:var(--bar-bg);border-bottom:1px solid var(--line);
  backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.zoom{display:inline-flex;gap:2px;padding:3px;border-radius:11px;background:var(--surface-2)}
.zoom button{font:inherit;font-size:.85rem;border:0;background:none;color:var(--ink);padding:5px 10px;border-radius:8px;cursor:pointer}
.zoom button[aria-pressed="true"]{background:var(--surface);box-shadow:0 1px 3px var(--shadow);font-weight:600}
.pages{display:grid;gap:16px;justify-items:start;overflow-x:auto;min-width:0;padding-bottom:6px}
.paper-page{display:block;width:100%;max-width:880px;scroll-margin-top:calc(var(--bar-h) + 70px);height:auto;background:#ffffff;border:1px solid var(--line);box-shadow:0 1px 4px var(--shadow)}
.pages[data-z="1.5"] .paper-page{width:150%;max-width:none}
.pages[data-z="2"] .paper-page{width:200%;max-width:none}
.to-q{position:fixed;right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:15;font-size:.95rem;font-weight:600;
  background:var(--pen);color:var(--on-accent);text-decoration:none;border-radius:999px;padding:.5em 1em;
  box-shadow:0 4px 14px var(--shadow);opacity:0;pointer-events:none;transition:opacity .2s}
.to-q.on{opacity:1;pointer-events:auto}
"""

SITE_JS = r"""
(function(){
  var app=document.getElementById('app'); if(!app)return;
  function load(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
  function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}

  /* side menu (a drawer on small screens) */
  var side=document.getElementById('side'), menuBtn=document.getElementById('menu-btn'), scrim=document.getElementById('scrim');
  function syncScrim(){if(scrim)scrim.hidden=!app.classList.contains('menu-open');}
  function menu(open){
    if(!side)return;
    app.classList.toggle('menu-open',open); syncScrim();
    if(menuBtn)menuBtn.setAttribute('aria-expanded',open?'true':'false');
    if(open){var f=side.querySelector('[aria-current="page"]')||side.querySelector('a');if(f)f.focus();}
    else if(menuBtn&&side.contains(document.activeElement))menuBtn.focus();
  }
  if(menuBtn)menuBtn.addEventListener('click',function(){menu(!app.classList.contains('menu-open'));});
  if(scrim)scrim.addEventListener('click',function(){menu(false);});
  document.querySelectorAll('[data-close-menu]').forEach(function(b){b.addEventListener('click',function(){menu(false);});});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')menu(false);});

  /* remember the last page for "Continue where you left off" */
  if(app.dataset.page!=='home'){
    save('tsa-last',{href:location.pathname.split('/').pop(),label:app.dataset.label});
  }else{
    var last=load('tsa-last'), c=document.getElementById('continue');
    if(c&&last&&last.href&&/^TSA_\w+\.html$/.test(last.href)){c.href=last.href;c.querySelector('b').textContent=last.label;c.hidden=false;}
  }

  /* question paper: zoom */
  var pages=document.getElementById('pages');
  document.querySelectorAll('.zoom button').forEach(function(b){b.addEventListener('click',function(){
    pages.dataset.z=b.dataset.z;
    document.querySelectorAll('.zoom button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
  });});

  /* worked solutions: a button back to the question list once you have scrolled down */
  var toq=document.querySelector('.to-q');
  if(toq){var onScroll=function(){toq.classList.toggle('on',window.scrollY>700);};window.addEventListener('scroll',onScroll,{passive:true});onScroll();}
})();
"""

ICON_MENU = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
ICON_L = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
ICON_R = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'
ICON_X = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
ICON_GO = '<svg class="go" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'

# hand-drawn doodles for the year page; colours come from the theme
DOODLES = {
    'paper': ('<svg class="doodle" viewBox="0 0 52 52" aria-hidden="true"><g class="rough" fill="none" stroke="currentColor" '
              'stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4">'
              '<g class="k-pen"><path d="M12 6 H32 L40 14 V46 H12 Z"/><path d="M32 6 V14 H40"/></g>'
              '<g class="k-muted"><path d="M17 20 H34"/><path d="M17 26 H34"/><path d="M17 32 H27"/></g>'
              '<g class="k-red"><circle cx="37" cy="40" r="8.5" fill="var(--paper)"/><path d="M37 35.5 V40 L40.5 42"/></g></g></svg>'),
    'ans': ('<svg class="doodle" viewBox="0 0 52 52" aria-hidden="true"><g class="rough" fill="none" stroke="currentColor" '
            'stroke-linecap="round" stroke-linejoin="round"><circle class="k-red" cx="26" cy="26" r="20" stroke-width="2.6"/>'
            '<path class="k-green" d="M15 27 L23 35 L38 16" stroke-width="4"/></g></svg>'),
    'sol': ('<svg class="doodle" viewBox="0 0 52 52" aria-hidden="true"><g class="rough" fill="none" stroke="currentColor" '
            'stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4"><g class="k-pen">'
            '<path d="M8 44 L12 33 L36 9 L43 16 L19 40 Z" fill="var(--fill-y)"/><path d="M12 33 L19 40"/><path d="M31 14 L38 21"/></g>'
            '<path class="k-red" d="M24 47 Q30 42 34 46 T44 45"/></g></svg>'),
}


def esc(s):
    return html.escape(str(s), quote=True)


def minutes(n):
    return round(n * TARA['minutes'] / TARA['questions'])


def page_name(year, kind=None, what=None):
    if kind is None:
        return f'TSA_{year}.html'
    slug = build.KINDS[kind]['slug']
    return f'TSA_{year}_{slug}_' + {'paper': 'Paper', 'ans': 'Answers', 'sol': 'Worked_Solutions'}[what] + '.html'


def paper_images(year, kind):
    """The set's question paper as page images: cropped to the printed area, 16 greys (64 colours where the page has colour)."""
    pdf = REPO / 'TSA_Papers' / f'TSA_{year}_{build.KINDS[kind]["slug"]}.pdf'
    stamp = f'{pdf.stat().st_size}-{pdf.stat().st_mtime_ns}-v1'
    cache = CACHE / pdf.stem
    meta = cache / 'meta.json'
    if meta.exists():
        m = json.loads(meta.read_text())
        if m.get('stamp') == stamp:
            return [((cache / p['file']).read_bytes(), p['w'], p['h']) for p in m['pages']]
    cache.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)
    raw = []
    for pg in doc:
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(2, 2))
        raw.append(Image.frombytes('RGB', (pix.width, pix.height), pix.samples))
    boxes = []
    for im in raw:
        ink = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 30 else 0)
        boxes.append(ink.getbbox() or (0, 0, im.width, im.height))
    pad = 40
    x0 = max(0, min(b[0] for b in boxes) - pad)
    x1 = min(raw[0].width, max(b[2] for b in boxes) + pad)
    pages = []
    for i, (im, b) in enumerate(zip(raw, boxes)):
        crop = im.crop((x0, max(0, b[1] - pad), x1, min(im.height, b[3] + pad)))
        sat = crop.resize((max(1, crop.width // 4), max(1, crop.height // 4))).convert('HSV').getchannel('S')
        colour = sum(sat.histogram()[61:]) > 20
        img = crop.quantize(64) if colour else crop.convert('L').quantize(16)
        buf = io.BytesIO()
        img.save(buf, 'PNG', optimize=True)
        name = f'p{i + 1:02d}.png'
        (cache / name).write_bytes(buf.getvalue())
        pages.append({'file': name, 'w': crop.width, 'h': crop.height})
    meta.write_text(json.dumps({'stamp': stamp, 'pages': pages}))
    return [((cache / p['file']).read_bytes(), p['w'], p['h']) for p in pages]


class Site:
    def __init__(self, keys):
        self.keys = keys
        self.years = sorted(keys)
        self.content = {}      # (year, kind) -> questions, only when they pass the checks
        self.problems = []
        for year in self.years:
            for kind, _, _ in SETS:
                qs = build.load_content(year, kind)
                if qs is None:
                    continue
                errs = build.check(year, kind, qs, keys)
                if errs:
                    self.problems.append(f'{year} {kind}: {errs[0]}' + (f' (+{len(errs) - 1} more)' if len(errs) > 1 else ''))
                    continue
                self.content[(year, kind)] = qs

    def has(self, year, kind, what):
        return what != 'sol' or (year, kind) in self.content

    def attempt(self, year, kind):
        """(right, total) for the user's own marked 2014 attempt, if the content has one."""
        qs = self.content.get((year, kind))
        if not qs or not any('attempt' in q for q in qs):
            return None
        return sum(q.get('attempt') == q['answer'] for q in qs), len(qs)

    def n_questions(self, year, kind):
        return len(self.keys[year][build.KINDS[kind]['key']])

    def same_page(self, y, kind, what):
        """The same kind of page in year y, or that year's menu when there is no such page."""
        return page_name(y, kind, what) if kind and self.has(y, kind, what) else page_name(y)

    # ---------------------------------------------------------------- chrome
    def topbar(self, year=None, kind=None, what=None, side=True):
        menu = (f'<button class="icon-btn menu-btn" id="menu-btn" type="button" aria-controls="side" aria-expanded="false">'
                f'{ICON_MENU}Menu</button>' if side else '')
        step = ''
        if year:
            i = self.years.index(year)

            def link(y, icon, word):
                if y is None:
                    return f'<span class="icon-btn off" aria-hidden="true">{icon}</span>'
                lbl = f'<span class="lbl">{y}</span>'
                inner = f'{icon}{lbl}' if word == 'Previous' else f'{lbl}{icon}'
                return f'<a class="icon-btn" href="{self.same_page(y, kind, what)}" aria-label="{word} year, {y}">{inner}</a>'
            prev_y = self.years[i - 1] if i > 0 else None
            next_y = self.years[i + 1] if i + 1 < len(self.years) else None
            step = (f'<div class="yearstep">{link(prev_y, ICON_L, "Previous")}<span class="now">{year}</span>'
                    f'{link(next_y, ICON_R, "Next")}</div>')
        return (f'<header class="topbar"><div class="topbar-in">{menu}'
                f'<a class="brand" href="index.html" title="All years"><mark>TSA</mark><span>solutions</span></a>'
                f'{step}</div></header>')

    def side(self, year, kind=None, what=None):
        sets = []
        for k, name, _ in SETS:
            links = ''.join(f'<a href="{page_name(year, k, w)}"{CURRENT if (k, w) == (kind, what) else ""}>{label}</a>'
                            for w, label in WHAT if self.has(year, k, w))
            sets.append(f'<div class="side-set set-{k}"><h3>{name}</h3>{links}</div>')
        years = ''.join(f'<li><a href="{self.same_page(y, kind, what)}"{CURRENT if y == year else ""}>{y}</a></li>'
                        for y in self.years)
        hint = (f'<p class="side-hint">Opens {build.KINDS[kind]["name"]} {WHAT_LABEL[what].lower()} for that year.</p>'
                if kind else '')
        return (f'<nav class="side" id="side" aria-label="Menu">'
                f'<div class="side-head"><b>Menu</b><button class="icon-btn" type="button" data-close-menu>{ICON_X}Close</button></div>'
                f'<a class="side-all" href="index.html">{ICON_L}All years</a>'
                f'<p class="side-title"><a href="{page_name(year)}">TSA {year}</a></p>{"".join(sets)}'
                f'<h2>Other years</h2>{hint}<ul class="side-years">{years}</ul></nav><div class="scrim" id="scrim" hidden></div>')

    def pagebar(self, year, kind=None, what=None):
        items = ['<li><a href="index.html">All years</a></li>']
        if kind is None:
            items.append(f'<li aria-current="page">TSA {year}</li>')
        else:
            items.append(f'<li><a href="{page_name(year)}">TSA {year}</a></li>')
            items.append(f'<li aria-current="page">{build.KINDS[kind]["name"]} {WHAT_LABEL[what].lower()}</li>')
        crumbs = f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
        tabs = ''
        if kind:
            short = {'ans': 'Answers', 'sol': 'Solutions', 'paper': 'Paper'}
            seg = ''.join(f'<a href="{page_name(year, kind, w)}"{CURRENT if w == what else ""}>'
                          f'<span class="l">{label}</span><span class="s">{short[w]}</span></a>'
                          for w, label in WHAT if self.has(year, kind, w))
            other = next(k for k, _, _ in SETS if k != kind)
            tabs = (f'<div class="pagetabs"><nav class="seg" aria-label="{build.KINDS[kind]["name"]} pages">{seg}</nav>'
                    f'<a class="switch" href="{self.same_page(year, other, what)}">Switch to {build.KINDS[other]["name"]} →</a></div>')
        return f'<div class="pagebar">{crumbs}{tabs}</div>'

    def frame(self, page, label, body, year=None, kind=None, what=None):
        side = year is not None
        shell = (f'<div class="shell has-side">{self.side(year, kind, what)}<main class="content">{body}</main></div>'
                 if side else f'<div class="shell"><main class="content">{body}</main></div>')
        return (f'<div class="app" id="app" data-page="{page}" data-label="{esc(label)}">'
                f'{self.topbar(year, kind, what, side)}{shell}</div>')

    @staticmethod
    def doc(title, body):
        """Full document for the repo folder and for the extra pages of a published site."""
        return ('<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                f'<title>{esc(title)}</title><link rel="stylesheet" href="assets/tsa.css"></head>'
                f'<body>{build.DEFS}{body}<script src="assets/tsa.js"></script></body></html>\n')

    @staticmethod
    def body_only(title, body):
        """The published home page: the host adds the document skeleton."""
        return (f'<title>{esc(title)}</title>\n<link rel="stylesheet" href="assets/tsa.css">\n'
                f'{build.DEFS}{body}<script src="assets/tsa.js"></script>\n')

    # ---------------------------------------------------------------- pages
    def home(self):
        cards = []
        for i, y in enumerate(self.years):
            tag = '<span class="ycard-tag">your attempt</span>' if any(self.attempt(y, k) for k, _, _ in SETS) else ''
            cards.append(f'<li><a class="ycard cv-{i % COVERS + 1}" href="{page_name(y)}">{tag}'
                         f'<span class="ycard-year">{y}</span><span class="ycard-sub">Answers &amp; solutions</span></a></li>')
        n = self.n_questions(self.years[0], 'ct')
        body = f"""<div class="wrap home">
  <header class="home-head">
    <p class="eyebrow">TSA Oxford · Section 1 · {self.years[0]}–{self.years[-1]}</p>
    <h1>Papers, answers &amp; worked solutions</h1>
    <p class="lede">Pick a year to check your answers. Each year has a Critical Thinking set and a Problem Solving set, and each
      set has its answers, full worked solutions and the question paper.</p>
  </header>
  <a class="continue" id="continue" href="index.html" hidden><span><small>Continue where you left off</small><b></b></span>{ICON_R}</a>
  <ol class="years" aria-label="Years">{''.join(cards)}</ol>
  <section class="howto" aria-labelledby="howto-h">
    <h2 id="howto-h">Checking a paper</h2>
    <ol>
      <li><span><b>Open the year,</b> then the set's <i>Answers</i>.</span></li>
      <li><span><b>Mark your sheet</b> against the answers. One mark each, no penalty for wrong answers.</span></li>
      <li><span><b>Tap any question</b> you got wrong (or guessed) to jump straight to its worked solution.</span></li>
    </ol>
  </section>
  <p class="facts"><b>Each set:</b> {n} questions · {n} marks · {minutes(n)} minutes. One mark per question and no penalty
    for a wrong answer. The time is scaled from TARA ({TARA['questions']} questions in {TARA['minutes']} minutes).</p>
  <p class="foot">Questions © UCLES {self.years[0]}–2021 and © Cambridge University Press &amp; Assessment 2022–{self.years[-1]},
    reproduced from the TSA Oxford Section 1 papers for practice. Answers come from the official answer keys.</p>
</div>"""
        return 'TSA Section 1 Solutions', self.frame('home', 'All years', body)

    def year_page(self, year):
        mine = [f'{name} {a[0]}/{a[1]}' for k, name, _ in SETS if (a := self.attempt(year, k))]
        mine_html = (f'<p class="facts"><b>Your attempt</b> is marked on these pages: {" · ".join(mine)}.</p>'
                     if mine else '')
        sets = []
        for k, name, _ in SETS:
            n = self.n_questions(year, k)
            desc = {
                'ans': f'The correct option for questions 1–{n}. Tap one to see its working.',
                'paper': 'The questions, to read on screen.',
                'sol': {'ct': 'Each argument colour-coded, the answer highlighted and every wrong option explained.',
                        'ps': 'Every question annotated and worked through with sketches, using GCSE methods only.'}[k],
            }
            rows = ''.join(f'<a class="choice" href="{page_name(year, k, w)}">{DOODLES[w]}<span><b>{label}</b>'
                           f'<span class="d">{desc[w]}</span></span>{ICON_GO}</a>'
                           for w, label in WHAT if self.has(year, k, w))
            sets.append(f'<section class="set set-{k}" aria-labelledby="h-{k}"><h2 id="h-{k}"><span>{name}</span></h2>'
                        f'<p class="meta"><span>{n} questions · {n} marks · {minutes(n)} minutes</span></p>'
                        f'{rows}</section>')
        body = f"""{self.pagebar(year)}
<div class="wrap">
  <header class="year-head">
    <p class="eyebrow">TSA Oxford · Section 1</p>
    <h1>TSA {year}</h1>
    <p class="lede">Choose a set, then open its answers or its worked solutions.</p>
    {mine_html}
  </header>
  <div class="sets">{''.join(sets)}</div>
</div>"""
        return f'TSA {year}', self.frame('year', f'TSA {year}', body, year)

    def paper_page(self, year, kind):
        meta = build.KINDS[kind]
        rows = self.keys[year][meta['key']]
        n = len(rows)
        imgs = paper_images(year, kind)
        pages = ''.join(
            f'<img class="paper-page" src="data:image/png;base64,{base64.b64encode(b).decode()}" width="{w}" height="{h}" '
            f'alt="Page {i + 1} of {len(imgs)} of the TSA {year} {meta["name"]} paper"'
            + (' loading="lazy"' if i > 1 else '') + '>'
            for i, (b, w, h) in enumerate(imgs))
        sol_btn = (f'<a class="tbtn primary" href="{page_name(year, kind, "sol")}">Worked solutions</a>'
                   if self.has(year, kind, 'sol') else '')
        body = f"""{self.pagebar(year, kind, 'paper')}
<div class="wrap">
  <header class="page-head">
    <p class="eyebrow">TSA {year} · question paper</p>
    <h1>{meta['name']}</h1>
    <div class="chips"><span class="chip">{n} questions</span><span class="chip">{n} marks</span>
      <span class="chip">{minutes(n)} minutes</span><span class="chip">no negative marking</span></div>
  </header>
  <div class="paper-tools" id="paper-tools">
    <div class="zoom" role="group" aria-label="Zoom the paper">
      <button type="button" data-z="1" aria-pressed="true">Fit</button>
      <button type="button" data-z="1.5" aria-pressed="false">1.5×</button>
      <button type="button" data-z="2" aria-pressed="false">2×</button>
    </div>
    <div class="links"><a class="tbtn" href="{page_name(year, kind, 'ans')}">Answers</a>{sol_btn}</div>
  </div>
  <div class="pages" id="pages" data-z="1">{pages}</div>
  <p class="foot">Question numbers match the answers and the worked solutions. The number in brackets on the paper is the
    question number in the original TSA {year} Section 1 paper.</p>
</div>"""
        return (f'TSA {year} {meta["name"]} Paper',
                self.frame('paper', f'TSA {year} · {meta["name"]} question paper', body, year, kind, 'paper'))

    def answers_page(self, year, kind):
        meta = build.KINDS[kind]
        rows = self.keys[year][meta['key']]
        n = len(rows)
        qs = self.content.get((year, kind))
        attempts = {q['n']: q.get('attempt') for q in qs} if qs and any('attempt' in q for q in qs) else {}
        sol = page_name(year, kind, 'sol') if self.has(year, kind, 'sol') else None
        cells = []
        for num, _orig, ans in rows:
            you, cls = '', ''
            if attempts:
                a = attempts.get(num)
                if not a:
                    you, cls = '<span class="you">you: –</span>', ' blank'
                elif a == ans:
                    you, cls = f'<span class="you">you: {a} ✓</span>', ' good'
                else:
                    you, cls = f'<span class="you">you: {a} ✗</span>', ' bad'
            inner = (f'<span class="n">{num}</span><span class="L" aria-label="answer {ans}">{ans}</span>{you}'
                     + ('<span class="see">working →</span>' if sol else ''))
            if sol:
                cells.append(f'<li><a class="ans{cls}" href="{sol}#q{num}" aria-label="Question {num}: {ans}. See the working.">'
                             f'{inner}</a></li>')
            else:
                cells.append(f'<li><span class="ans{cls}">{inner}</span></li>')
        score = f'<p class="score">Your 2014 attempt: {a[0]} / {a[1]}</p>' if (a := self.attempt(year, kind)) else ''
        tip = '<p class="sheet-tip">Tap a question to jump to its worked solution.</p>' if sol else ''
        nxt = (f'<a class="tbtn primary" href="{sol}">Open the worked solutions</a>' if sol else '') + \
              f'<a class="tbtn" href="{page_name(year, kind, "paper")}">Open the question paper</a>'
        body = f"""{self.pagebar(year, kind, 'ans')}
<div class="wrap">
  <header class="page-head">
    <p class="eyebrow">TSA {year} · mark scheme</p>
    <h1>{meta['name']} answers</h1>
    <div class="chips"><span class="chip">{n} questions</span><span class="chip">{n} marks</span>
      <span class="chip">{minutes(n)} minutes</span><span class="chip">no negative marking</span></div>
  </header>
  <section class="sheet" aria-label="Answers">
    <div class="sheet-head"><b>TSA {year} {meta['name']} · mark scheme</b><span>Question · correct option</span></div>
    {tip}
    <ol class="ans-grid">{''.join(cells)}</ol>
    {score}
  </section>
  <nav class="next" aria-label="More for this set">{nxt}</nav>
  <p class="foot">Answers come from the official TSA Section 1 answer key for {year}.</p>
</div>"""
        return (f'TSA {year} {meta["name"]} Answers',
                self.frame('answers', f'TSA {year} · {meta["name"]} answers', body, year, kind, 'ans'))

    def solutions_page(self, year, kind):
        qs = self.content[(year, kind)]
        name = build.KINDS[kind]['name']
        body = (self.pagebar(year, kind, 'sol') + f'<div class="ws">{build.render_main(year, kind, qs)}</div>'
                + '<a class="to-q" href="#questions">↑ All questions</a>')
        return (f'TSA {year} {name} Solutions',
                self.frame('solutions', f'TSA {year} · {name} worked solutions', body, year, kind, 'sol'))

    # ---------------------------------------------------------------- output
    def write(self, out, artifact_dir=None):
        (out / 'assets').mkdir(parents=True, exist_ok=True)
        fonts = (build.font_face('Patrick Hand', 'patrick-hand-latin-400-normal.woff2', 400)
                 + build.font_face('Caveat', 'caveat-latin-400-normal.woff2', 400)
                 + build.font_face('Caveat', 'caveat-latin-700-normal.woff2', 700))
        (out / 'assets' / 'tsa.css').write_text(fonts + build.CSS + SITE_CSS, encoding='utf-8')
        (out / 'assets' / 'tsa.js').write_text(build.JS + SITE_JS, encoding='utf-8')
        pages = {'index.html': self.home()}
        for y in self.years:
            pages[page_name(y)] = self.year_page(y)
            for k, _, _ in SETS:
                pages[page_name(y, k, 'paper')] = self.paper_page(y, k)
                pages[page_name(y, k, 'ans')] = self.answers_page(y, k)
                if (y, k) in self.content:
                    pages[page_name(y, k, 'sol')] = self.solutions_page(y, k)
        for old in out.iterdir():
            if old.suffix == '.html' and old.name not in pages:
                old.unlink()
        for name, (title, body) in pages.items():
            (out / name).write_text(self.doc(title, body), encoding='utf-8')
        if artifact_dir:
            artifact_dir.mkdir(parents=True, exist_ok=True)
            title, body = pages['index.html']
            (artifact_dir / 'index.html').write_text(self.body_only(title, body), encoding='utf-8')
        return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=REPO / 'TSA_Website', type=Path)
    ap.add_argument('--artifact-dir', type=Path)
    args = ap.parse_args()
    keys = json.loads((HERE / 'keys.json').read_text())
    site = Site(keys)
    pages = site.write(args.out, args.artifact_dir)
    sols = sorted(f'{y}{k}' for y, k in site.content)
    size = sum(f.stat().st_size for f in args.out.rglob('*') if f.is_file())
    print(f'{len(pages)} pages, {size / 1e6:.1f} MB. Worked solutions: {" ".join(sols)}')
    for p in site.problems:
        print('  not included:', p)


if __name__ == '__main__':
    main()
