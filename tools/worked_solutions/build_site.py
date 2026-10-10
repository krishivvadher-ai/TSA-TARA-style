"""Build the TSA website in TSA_Website/.

    python tools/worked_solutions/build_site.py
    python tools/worked_solutions/build_site.py --artifact-dir DIR   # also write a body-only index for publishing

Pages (all relative links, so the folder works offline and when hosted):
    index.html                                          every year as an exercise book
    TSA_<year>.html                                     the four choices for that year
    TSA_<year>_<Critical_Thinking|Problem_Solving>_Answers.html
    TSA_<year>_<Critical_Thinking|Problem_Solving>_Worked_Solutions.html
    assets/tsa.css, assets/tsa.js                       shared styles (fonts built in) and scripts

The worked-solution pages come from the same content files as TSA_Worked_Solutions/.
"""

import argparse
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

REPO = build.REPO
TARA = {'questions': 22, 'minutes': 40}   # per module, as in tools/build_tsa_sets.py
SETS = [('ct', 'Critical Thinking', 'CT'), ('ps', 'Problem Solving', 'PS')]
COVERS = 8                                # exercise-book cover colours, cycled
TILTS = ['-1.2deg', '.8deg', '-.4deg', '1.1deg', '-.9deg', '.5deg', '-1.4deg', '.9deg']

SITE_CSS = r"""
/* ---------------------------------------------------------------- site chrome
   The site is a pile of exercise books: one per year on the home page, then the
   printed mark schemes and worked solutions inside. */
:root{
  --bar-h:58px; --bar-bg:rgba(246,245,239,.94); --rule:rgba(60,100,160,.30); --shadow:rgba(0,0,0,.10);
  --slip-muted:#5b5f66; --label:#fbfaf4; --label-ink:#22252a; --label-pen:#1f4ea8; --label-line:#9fb6d8;
  --cover-1:#2f5fb3; --cover-2:#c2413b; --cover-3:#2f8a55; --cover-4:#d4a22b;
  --cover-5:#7a4fb8; --cover-6:#d6732a; --cover-7:#cc5a88; --cover-8:#23878a;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bar-bg:rgba(22,33,29,.94); --rule:rgba(255,255,255,.16); --shadow:rgba(0,0,0,.35);
  --label:#e9e6da; --label-line:#8ea3c2;
  --cover-1:#2b528f; --cover-2:#9c3934; --cover-3:#2a7149; --cover-4:#a8862c;
  --cover-5:#5f418f; --cover-6:#a65c27; --cover-7:#9d4a6d; --cover-8:#246e70;
}}
:root[data-theme="dark"]{
  --bar-bg:rgba(22,33,29,.94); --rule:rgba(255,255,255,.16); --shadow:rgba(0,0,0,.35);
  --label:#e9e6da; --label-line:#8ea3c2;
  --cover-1:#2b528f; --cover-2:#9c3934; --cover-3:#2a7149; --cover-4:#a8862c;
  --cover-5:#5f418f; --cover-6:#a65c27; --cover-7:#9d4a6d; --cover-8:#246e70;
}
html{scroll-padding-top:calc(var(--bar-h) + 14px)}
.q{scroll-margin-top:calc(var(--bar-h) + 14px)}

.sitebar{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--bar-bg);
  border-bottom:2px solid var(--rule);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);transition:transform .25s ease}
.sitebar.away{transform:translateY(calc(-100% - env(safe-area-inset-top,0px) - 4px))}
.sitebar-in{max-width:1120px;margin:0 auto;padding-inline:16px;padding-block:8px;display:flex;flex-wrap:wrap;
  align-items:center;gap:8px 18px;min-height:var(--bar-h)}
.brand{display:flex;align-items:baseline;gap:.35em;text-decoration:none;color:var(--ink);font-family:var(--scrawl);
  font-weight:700;font-size:1.55rem;line-height:1;white-space:nowrap}
.brand mark{color:var(--slip-ink);padding:0 .15em;background:linear-gradient(transparent 18%,var(--hl-y) 18%,var(--hl-y) 86%,transparent 86%)}
.yearnav{position:relative;display:flex;align-items:center;gap:2px}
.yr-step{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;text-decoration:none;color:var(--pen)}
.yr-step svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.yr-step:hover{background:var(--chip)}
.yr-step[aria-disabled="true"]{color:var(--muted);opacity:.35;pointer-events:none}
.yearpick summary{list-style:none;cursor:pointer;font-family:var(--scrawl);font-weight:700;font-size:1.45rem;line-height:1.25;
  padding:0 .45em 0 .55em;border:2px solid var(--pen);color:var(--pen);border-radius:12px 9px 13px 8px;display:flex;align-items:center;gap:.25em;white-space:nowrap}
.yearpick summary::-webkit-details-marker{display:none}
.yearpick summary svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.4;stroke-linecap:round;transition:transform .2s}
.yearpick[open] summary svg{transform:rotate(180deg)}
.yearmenu{position:absolute;left:0;top:calc(100% + 8px);width:min(300px,calc(100vw - 32px));background:var(--slip);color:var(--slip-ink);
  border:1px solid var(--slip-edge);box-shadow:3px 4px 0 var(--shadow);padding:10px 12px 12px;display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));gap:4px;z-index:30}
.yearmenu p{grid-column:1/-1;margin:0 0 4px;font-size:.92rem;color:var(--slip-muted)}
.yearmenu a{font-family:var(--scrawl);font-weight:700;font-size:1.35rem;text-align:center;text-decoration:none;color:var(--slip-ink);
  border-radius:6px;padding:1px 0}
.yearmenu a:hover{background:var(--hl-b)}
.yearmenu a[aria-current="page"]{background:var(--hl-y)}
.tabs{display:flex;flex-wrap:wrap;align-items:center;gap:4px 16px;margin-left:auto}
.tabgroup{display:flex;align-items:center;gap:2px}
.tabgroup>span{font-family:var(--scrawl);font-weight:700;font-size:1.2rem;color:var(--muted);margin-right:4px;white-space:nowrap}
.tab{text-decoration:none;color:var(--ink);padding:3px 9px;border-radius:999px;font-size:1rem;white-space:nowrap}
.tab:hover{background:var(--chip)}
.tab[aria-current="page"]{color:var(--slip-ink);border-radius:3px;
  background:linear-gradient(transparent 10%,var(--hl-y) 10%,var(--hl-y) 90%,transparent 90%)}
.tab[aria-disabled="true"]{color:var(--muted);opacity:.5}
.short,.ws{display:none}
@media (max-width:760px){.ws{display:inline}}
@media (max-width:1000px){.long{display:none}.short{display:inline}}
@media (max-width:760px){
  :root{--bar-h:96px}
  .yearnav{margin-left:auto}
  .yearmenu{left:auto;right:0}
  .tabs{order:3;width:100%;margin-left:0;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;gap:4px 12px}
  .tabs::-webkit-scrollbar{display:none}
  .tab{font-size:.95rem;padding:3px 6px}
  .tabgroup>span{margin-right:2px}
  .wl{display:none}
}

.crumbs{max-width:1120px;margin:0 auto;padding-inline:16px;padding-block:16px 0;font-size:1rem;color:var(--muted)}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:2px 8px;align-items:center}
.crumbs li+li::before{content:"\203A";margin-right:8px;color:var(--muted)}
.crumbs a{color:var(--pen)}
.crumbs + .wrap{padding-top:14px}

.to-q{position:fixed;right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:15;font-family:var(--hand);font-size:1.05rem;
  background:var(--pen);color:var(--paper);text-decoration:none;border-radius:14px 10px 16px 9px;padding:.3em .9em;
  box-shadow:2px 3px 0 var(--shadow);opacity:0;pointer-events:none;transition:opacity .2s}
.to-q.on{opacity:1;pointer-events:auto}

/* home: a shelf of exercise books */
.home-head{display:grid;gap:12px;margin-bottom:26px}
.home-head h1{font-family:var(--scrawl);font-weight:700;font-size:clamp(2.6rem,7vw,4rem);line-height:1;margin:0}
.facts{background:var(--note-bg);color:var(--note-ink);padding:10px 14px;border-radius:2px;box-shadow:2px 3px 0 var(--shadow);
  transform:rotate(-.6deg);max-width:62ch;margin:4px 0 0}
.facts b{font-family:var(--scrawl);font-size:1.3rem;margin-right:.2em}
.shelf{list-style:none;margin:8px 0 0;padding:0;display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:26px 18px}
@media (max-width:1000px){.shelf{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:480px){
  .shelf{grid-template-columns:repeat(4,minmax(0,1fr));gap:18px 12px}
  .book{padding:24% 9% 10% 15%}
  .label{padding:4px 4px 5px}
  .label small,.label .subj,.label .todo{display:none}
  .label .yr{font-size:1.35rem;text-align:center;border:0}
  .book .tab-note{font-size:.74rem;padding:1px 4px;left:6%;bottom:6%}
}
.book{position:relative;display:flex;flex-direction:column;aspect-ratio:3/4;max-width:100%;background:var(--cv);
  border-radius:3px 10px 10px 3px;text-decoration:none;color:var(--label-ink);padding:22% 10% 10% 17%;
  box-shadow:inset 8px 0 0 rgba(0,0,0,.18),inset 10px 0 0 rgba(255,255,255,.10),3px 5px 0 var(--shadow);
  transform:rotate(var(--tilt,0deg));transition:transform .18s ease}
.book:hover,.book:focus-visible{transform:translateY(-5px) rotate(0deg)}
.label{background:var(--label);border-radius:3px;padding:6px 8px 8px;display:grid;gap:1px;box-shadow:0 1px 0 rgba(0,0,0,.18)}
.label small{font-family:var(--print);font-size:.6rem;letter-spacing:.09em;text-transform:uppercase;color:var(--slip-muted)}
.label .subj{font-family:var(--hand);color:var(--label-pen);font-size:.95rem;line-height:1.2;border-bottom:1px solid var(--label-line);padding-bottom:2px;margin-bottom:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.label .yr{font-family:var(--scrawl);font-weight:700;color:var(--label-pen);font-size:clamp(1.7rem,3vw,2.3rem);line-height:.95;border-bottom:1px solid var(--label-line)}
.label .todo{font-family:var(--print);font-size:.64rem;color:#a2322c;margin-top:4px}
.book .tab-note{position:absolute;z-index:2;left:14%;bottom:7%;background:var(--note-bg);color:var(--note-ink);font-family:var(--scrawl);
  font-weight:700;font-size:1.05rem;line-height:1.1;padding:3px 8px;transform:rotate(-3deg);box-shadow:1px 2px 0 var(--shadow);white-space:nowrap}
.cv-1{--cv:var(--cover-1)}.cv-2{--cv:var(--cover-2)}.cv-3{--cv:var(--cover-3)}.cv-4{--cv:var(--cover-4)}
.cv-5{--cv:var(--cover-5)}.cv-6{--cv:var(--cover-6)}.cv-7{--cv:var(--cover-7)}.cv-8{--cv:var(--cover-8)}

/* year page */
.year-head{display:grid;gap:10px;margin-bottom:24px}
.year-title{display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px}
.year-title h1{font-family:var(--scrawl);font-weight:700;font-size:clamp(3.4rem,10vw,5.2rem);line-height:.9;margin:0}
.steps-yr{display:flex;gap:10px;font-size:1.05rem}
.steps-yr a{color:var(--pen);text-decoration:none;border-bottom:2px solid currentColor}
.sets{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;align-items:start}
@media (max-width:760px){.sets{grid-template-columns:minmax(0,1fr)}}
.set{background:var(--slip);color:var(--slip-ink);border:1px solid var(--slip-edge);box-shadow:3px 4px 0 var(--shadow);
  padding:18px 20px 20px;display:grid;gap:12px;min-width:0}
.set h2{font-family:var(--scrawl);font-weight:700;font-size:2.3rem;line-height:1;margin:0}
.set h2 span{padding:0 .12em;background:linear-gradient(transparent 55%,var(--c) 55%,var(--c) 92%,transparent 92%)}
.set-ct{--c:var(--hl-p)}.set-ps{--c:var(--hl-b)}
.set .meta{font-family:var(--print);font-size:.85rem;color:var(--slip-muted);margin:0;font-variant-numeric:tabular-nums}
.choice{display:grid;grid-template-columns:52px minmax(0,1fr) auto;gap:12px;align-items:center;text-decoration:none;color:var(--slip-ink);
  border:2px solid var(--slip-ink);border-radius:14px 10px 16px 9px;padding:12px 14px;transition:transform .15s,box-shadow .15s}
.choice:hover,.choice:focus-visible{transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--c)}
.choice svg.doodle{width:52px;height:52px}
.choice b{display:block;font-family:var(--scrawl);font-weight:700;font-size:1.7rem;line-height:1.05}
.choice .d{display:block;font-size:1rem;color:var(--slip-muted);line-height:1.35}
.choice .go{font-family:var(--scrawl);font-weight:700;font-size:1.8rem;color:#c42f2a}
.choice.off{border-style:dashed;color:var(--slip-muted);pointer-events:none}
.mine{margin:0;max-width:62ch}

/* answers page */
.chips{display:flex;flex-wrap:wrap;gap:6px}
.sheet{background:var(--slip);color:var(--slip-ink);border:1px solid var(--slip-edge);box-shadow:3px 4px 0 var(--shadow);
  padding:18px 20px 20px;max-width:920px;display:grid;gap:12px;min-width:0}
.sheet-head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;font-family:var(--print);font-size:.9rem;
  border-bottom:2px solid var(--slip-ink);padding-bottom:6px}
.sheet-head b{font-size:1rem}
.sheet-tip{margin:0;font-size:1rem;color:var(--slip-muted)}
.ans-grid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}
.ans{position:relative;display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--slip-ink);border:1.5px solid var(--slip-edge);
  border-radius:8px;padding:8px 10px;min-height:58px;transition:background .15s}
.ans:hover,.ans:focus-visible{background:var(--hl-g)}
.ans .n{font-family:var(--scrawl);font-weight:700;font-size:1.5rem;color:#c42f2a;min-width:1.3em;line-height:1}
.ans .L{font-family:var(--scrawl);font-weight:700;font-size:1.9rem;color:#1d7a42;width:1.5em;height:1.5em;display:grid;place-items:center;
  border:2.5px solid currentColor;border-radius:50% 46% 52% 48%;transform:rotate(-5deg);line-height:1}
.ans .see{font-size:.9rem;color:var(--slip-muted);margin-left:auto;white-space:nowrap}
.ans .you{position:absolute;top:3px;right:6px;font-family:var(--print);font-size:.7rem;font-weight:700}
.ans.good .you{color:#1b6d3b}.ans.bad .you{color:#b3231d}.ans.blank .you{color:var(--slip-muted)}
.ans.bad{border-color:#e7a29c}
@media (max-width:860px){.ans .see{display:none}}
@media (max-width:560px){
  .ans-grid{gap:5px}
  .ans{flex-direction:column;gap:2px;padding:6px 2px 7px;min-height:0}
  .ans .n{font-size:1.25rem;min-width:0}
  .ans .L{font-size:1.5rem}
  .ans .you{position:static;font-size:.62rem}
}
.score{font-family:var(--scrawl);font-weight:700;font-size:1.6rem;color:var(--red);margin:0}
.next{display:flex;flex-wrap:wrap;gap:10px 14px;margin-top:20px}
.next a{font-family:var(--hand);font-size:1.08rem;text-decoration:none;border:2px solid var(--pen);color:var(--pen);
  border-radius:12px 9px 13px 8px;padding:.25em .9em}
.next a:hover{background:var(--pen);color:var(--paper)}
"""

SITE_JS = r"""
(function(){
  var picks=document.querySelectorAll('details.yearpick');
  document.addEventListener('click',function(e){picks.forEach(function(d){if(d.open&&!d.contains(e.target))d.open=false;});});
  document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;
    picks.forEach(function(d){if(d.open){d.open=false;d.querySelector('summary').focus();}});});
  /* the bar slides away while you read down the page and comes back as soon as you scroll up */
  var bar=document.getElementById('sitebar'), toq=document.querySelector('.to-q'), last=window.scrollY;
  function onScroll(){
    var y=window.scrollY, d=y-last;
    if(bar){
      if(y<90||d<-6)bar.classList.remove('away');
      else if(d>6&&!bar.contains(document.activeElement)&&!bar.querySelector('details[open]'))bar.classList.add('away');
    }
    if(toq)toq.classList.toggle('on',y>700);
    last=y;
  }
  window.addEventListener('scroll',onScroll,{passive:true});
  if(bar)bar.addEventListener('focusin',function(){bar.classList.remove('away');});
  /* on a phone the page tabs scroll sideways: start with the current one in view */
  var tabs=document.querySelector('.tabs'), cur=tabs&&tabs.querySelector('[aria-current="page"]');
  if(tabs&&cur&&tabs.scrollWidth>tabs.clientWidth)tabs.scrollLeft=cur.offsetLeft-tabs.offsetLeft-tabs.clientWidth/2+cur.offsetWidth/2;
})();
"""

CHEVRON_L = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M12.5 4 L6.5 10 L12.5 16"/></svg>'
CHEVRON_R = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M7.5 4 L13.5 10 L7.5 16"/></svg>'
CHEVRON_D = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 6 L8 10.5 L12.5 6"/></svg>'

# hand-drawn doodles for the year page: a teacher's tick for answers, a pencil for worked solutions
DOODLE_ANS = ('<svg class="doodle" viewBox="0 0 52 52" aria-hidden="true"><g class="rough" fill="none" stroke-linecap="round" '
              'stroke-linejoin="round"><circle cx="26" cy="26" r="21" stroke="#c42f2a" stroke-width="2.6"/>'
              '<path d="M15 27 L23 35 L38 16" stroke="#1d7a42" stroke-width="4"/></g></svg>')
DOODLE_SOL = ('<svg class="doodle" viewBox="0 0 52 52" aria-hidden="true"><g class="rough" fill="none" stroke-linecap="round" '
              'stroke-linejoin="round" stroke-width="2.4"><path d="M8 44 L12 33 L36 9 L43 16 L19 40 Z" stroke="#1f4ea8" fill="#fde46a"/>'
              '<path d="M12 33 L19 40" stroke="#1f4ea8"/><path d="M31 14 L38 21" stroke="#1f4ea8"/>'
              '<path d="M8 44 L13 42" stroke="#1d1f23" stroke-width="3"/>'
              '<path d="M24 47 Q30 42 34 46 T44 45" stroke="#c42f2a"/></g></svg>')


def esc(s):
    return html.escape(str(s), quote=True)


def minutes(n):
    return round(n * TARA['minutes'] / TARA['questions'])


def page_name(year, kind=None, what=None):
    if kind is None:
        return f'TSA_{year}.html'
    slug = build.KINDS[kind]['slug']
    return f'TSA_{year}_{slug}_{"Answers" if what == "ans" else "Worked_Solutions"}.html'


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
        return what == 'ans' or (year, kind) in self.content

    def attempt(self, year, kind):
        """(right, answered-or-not total) for the user's own marked attempt, if the content has one."""
        qs = self.content.get((year, kind))
        if not qs or not any('attempt' in q for q in qs):
            return None
        return sum(q.get('attempt') == q['answer'] for q in qs), len(qs)

    # ---------------------------------------------------------------- chrome
    def bar(self, year=None, kind=None, what=None):
        """The sticky bar on every page: home, year picker (keeps you on the same page type) and the four pages."""
        def target(y):
            if kind and self.has(y, kind, what):
                return page_name(y, kind, what)
            return page_name(y)

        current = ' aria-current="page"'
        links = ''.join(f'<a href="{target(y)}"{current if y == year else ""}>{y}</a>' for y in self.years)
        hint = 'Same page, another year:' if kind else 'Choose a year:'
        pick = (f'<details class="yearpick"><summary aria-label="Choose a year">{year or "Years"}{CHEVRON_D}</summary>'
                f'<div class="yearmenu"><p>{hint}</p>{links}</div></details>')
        if year:
            i = self.years.index(year)
            prev_y = self.years[i - 1] if i > 0 else None
            next_y = self.years[i + 1] if i + 1 < len(self.years) else None

            def step(y, svg, word):
                if y is None:
                    return f'<span class="yr-step" aria-disabled="true">{svg}</span>'
                return f'<a class="yr-step" href="{target(y)}" aria-label="{word} year, {y}">{svg}</a>'
            yearnav = f'<div class="yearnav">{step(prev_y, CHEVRON_L, "Previous")}{pick}{step(next_y, CHEVRON_R, "Next")}</div>'
            groups = []
            for k, name, short in SETS:
                tabs = []
                for w, label in (('ans', 'Answers'), ('sol', '<span class="wl">Worked solutions</span><span class="ws">Solutions</span>')):
                    cur = ' aria-current="page"' if (k, w) == (kind, what) else ''
                    if self.has(year, k, w):
                        tabs.append(f'<a class="tab" href="{page_name(year, k, w)}"{cur}>{label}</a>')
                    else:
                        tabs.append(f'<span class="tab" aria-disabled="true">{label}</span>')
                groups.append(f'<div class="tabgroup"><span><span class="long">{name}</span>'
                              f'<span class="short">{short}</span></span>{"".join(tabs)}</div>')
            tabs = f'<nav class="tabs" aria-label="Pages for {year}">{"".join(groups)}</nav>'
        else:
            yearnav = f'<div class="yearnav">{pick}</div>'
            tabs = ''
        return (f'<header class="sitebar" id="sitebar"><div class="sitebar-in">'
                f'<a class="brand" href="index.html" title="All years"><mark>TSA</mark> solutions</a>'
                f'{yearnav}{tabs}</div></header>')

    def crumbs(self, year, kind=None, what=None):
        items = ['<li><a href="index.html">All years</a></li>']
        if kind is None:
            items.append(f'<li aria-current="page">{year}</li>')
        else:
            items.append(f'<li><a href="{page_name(year)}">{year}</a></li>')
            label = f'{build.KINDS[kind]["name"]} {"answers" if what == "ans" else "worked solutions"}'
            items.append(f'<li aria-current="page">{label}</li>')
        return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'

    @staticmethod
    def doc(title, body, extra=''):
        """Full document for the repo folder and for the extra pages of a published site."""
        return ('<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                f'<title>{esc(title)}</title><link rel="stylesheet" href="assets/tsa.css"></head>'
                f'<body>{build.DEFS}{body}{extra}<script src="assets/tsa.js"></script></body></html>\n')

    @staticmethod
    def body_only(title, body):
        """The published home page: the host adds the document skeleton."""
        return (f'<title>{esc(title)}</title>\n<link rel="stylesheet" href="assets/tsa.css">\n'
                f'{build.DEFS}{body}<script src="assets/tsa.js"></script>\n')

    # ---------------------------------------------------------------- pages
    def home(self):
        books = []
        for i, y in enumerate(self.years):
            missing = [f'{short} solutions' for k, _, short in SETS if (y, k) not in self.content]
            todo = f'<span class="todo">Coming soon: {" &amp; ".join(missing)}</span>' if missing else ''
            mine = ''
            if any(self.attempt(y, k) for k, _, _ in SETS):
                mine = '<span class="tab-note">your attempt</span>'
            books.append(
                f'<li><a class="book cv-{i % COVERS + 1}" style="--tilt:{TILTS[i % len(TILTS)]}" href="{page_name(y)}" '
                f'aria-label="TSA {y}"><span class="label"><small>Subject</small><span class="subj">TSA</span>'
                f'<small>Year</small><span class="yr">{y}</span>{todo}</span>{mine}</a></li>')
        n = len(self.keys[self.years[0]]['CT'])
        body = f"""<div class="wrap">
  <header class="home-head">
    <p class="eyebrow">TSA Oxford · Section 1 · {self.years[0]}–{self.years[-1]}</p>
    <h1>Answers &amp; worked solutions</h1>
    <p class="lede">Pick a year. Each year has four pages: the answers and the worked solutions for its Critical Thinking set
      and for its Problem Solving set.</p>
    <p class="facts"><b>Each set:</b> {n} questions · {n} marks · {minutes(n)} minutes. One mark per question and no penalty
      for a wrong answer. The time is scaled from TARA ({TARA['questions']} questions in {TARA['minutes']} minutes).</p>
  </header>
  <main><ol class="shelf" aria-label="Years">{''.join(books)}</ol></main>
  <p class="foot">Questions © UCLES {self.years[0]}–2021 and © Cambridge University Press &amp; Assessment 2022–{self.years[-1]},
    reproduced from the TSA Oxford Section 1 papers for practice. Answers come from the official answer keys.</p>
</div>"""
        return 'TSA Section 1 Solutions', self.bar() + body

    def year_page(self, year):
        i = self.years.index(year)
        steps = []
        if i > 0:
            steps.append(f'<a href="{page_name(self.years[i - 1])}">← {self.years[i - 1]}</a>')
        if i + 1 < len(self.years):
            steps.append(f'<a href="{page_name(self.years[i + 1])}">{self.years[i + 1]} →</a>')
        mine = [f'{name} {a[0]}/{a[1]}' for k, name, _ in SETS if (a := self.attempt(year, k))]
        mine_html = (f'<p class="facts mine"><b>Your attempt</b> is marked on these pages: {" · ".join(mine)}.</p>'
                     if mine else '')
        desc_sol = {
            'ct': 'Each argument colour-coded, the answer highlighted and every wrong option explained.',
            'ps': 'Every question annotated and worked through with sketches, using GCSE methods only.',
        }
        sets = []
        for k, name, _ in SETS:
            n = len(self.keys[year][build.KINDS[k]['key']])
            ans = (f'<a class="choice" href="{page_name(year, k, "ans")}">{DOODLE_ANS}<span><b>Answers</b>'
                   f'<span class="d">The mark scheme: the correct option for questions 1–{n}.</span></span>'
                   f'<span class="go" aria-hidden="true">→</span></a>')
            if self.has(year, k, 'sol'):
                sol = (f'<a class="choice" href="{page_name(year, k, "sol")}">{DOODLE_SOL}<span><b>Worked solutions</b>'
                       f'<span class="d">{desc_sol[k]}</span></span><span class="go" aria-hidden="true">→</span></a>')
            else:
                sol = (f'<span class="choice off">{DOODLE_SOL}<span><b>Worked solutions</b>'
                       f'<span class="d">Being written. Check back soon.</span></span><span></span></span>')
            sets.append(f'<section class="set set-{k}" aria-labelledby="h-{k}"><h2 id="h-{k}"><span>{name}</span></h2>'
                        f'<p class="meta">{n} questions · {n} marks · {minutes(n)} minutes</p>{ans}{sol}</section>')
        body = f"""{self.crumbs(year)}
<div class="wrap">
  <header class="year-head">
    <p class="eyebrow">TSA Oxford · Section 1</p>
    <div class="year-title"><h1>{year}</h1><div class="steps-yr">{''.join(steps)}</div></div>
    <p class="lede">Choose a set, then open its answers or its worked solutions.</p>
    {mine_html}
  </header>
  <main class="sets">{''.join(sets)}</main>
</div>"""
        return f'TSA {year}', self.bar(year) + body

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
        score = ''
        a = self.attempt(year, kind)
        if a:
            score = f'<p class="score">Your attempt: {a[0]} / {a[1]}</p>'
        tip = ('Tap a question to jump to its worked solution.' if sol
               else 'The worked solutions for this set are being written.')
        other = next(k for k, _, _ in SETS if k != kind)
        nxt = []
        if sol:
            nxt.append(f'<a href="{sol}">{meta["name"]} worked solutions →</a>')
        nxt.append(f'<a href="{page_name(year, other, "ans")}">{build.KINDS[other]["name"]} answers →</a>')
        nxt.append(f'<a href="{page_name(year)}">All four {year} pages</a>')
        body = f"""{self.crumbs(year, kind, 'ans')}
<div class="wrap">
  <header class="page-head">
    <p class="eyebrow">TSA {year} · mark scheme</p>
    <h1>{meta['name']} answers</h1>
    <div class="chips"><span class="chip">{n} questions</span><span class="chip">{n} marks</span>
      <span class="chip">{minutes(n)} minutes</span><span class="chip">no negative marking</span></div>
  </header>
  <main>
    <section class="sheet" aria-label="Answers">
      <div class="sheet-head"><b>TSA {year} {meta['name']} · mark scheme</b><span>Question · correct option</span></div>
      <p class="sheet-tip">Question numbers match the {year} {meta['name']} paper in TSA_Papers. {tip}</p>
      <ol class="ans-grid">{''.join(cells)}</ol>
      {score}
    </section>
    <nav class="next" aria-label="Next">{''.join(nxt)}</nav>
  </main>
  <p class="foot">Answers come from the official TSA Section 1 answer key for {year}.</p>
</div>"""
        return f'TSA {year} {meta["name"]} Answers', self.bar(year, kind, 'ans') + body

    def solutions_page(self, year, kind):
        qs = self.content[(year, kind)]
        body = (self.crumbs(year, kind, 'sol') + build.render_main(year, kind, qs)
                + '<a class="to-q" href="#questions">↑ Questions</a>')
        return f'TSA {year} {build.KINDS[kind]["name"]} Solutions', self.bar(year, kind, 'sol') + body

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
                pages[page_name(y, k, 'ans')] = self.answers_page(y, k)
                if (y, k) in self.content:
                    pages[page_name(y, k, 'sol')] = self.solutions_page(y, k)
        keep = set(pages) | {'assets'}
        for old in out.iterdir():
            if old.name not in keep and old.suffix == '.html':
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
