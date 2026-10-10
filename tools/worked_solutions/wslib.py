"""Helpers for writing worked-solution content.

Content files (content/y<YEAR>_ps.py and content/y<YEAR>_ct.py) import from here.
Everything returns HTML strings. See SCHEMA.md for how a question is described.
"""

import base64
import html as _html
from pathlib import Path

HERE = Path(__file__).resolve().parent


# ------------------------------------------------------------------ text bits

def esc(s):
    return _html.escape(str(s), quote=False)


def hl(text, colour='y', n=None):
    """Highlighter mark on the question. colour: y rule/key fact, p trap, g numbers, b what's asked.
    n links it to an annotation note with the same number."""
    pin = f'<sup class="pin">{n}</sup>' if n is not None else ''
    return f'<mark class="hl hl-{colour}">{text}{pin}</mark>'


def frac(top, bottom):
    """A stacked fraction that renders without any maths library."""
    return f'<span class="frac"><span>{top}</span><span>{bottom}</span></span>'


def calc(*lines):
    """A block of hand-written working, one line per argument."""
    return '<div class="calc">' + ''.join(f'<div>{l}</div>' for l in lines) + '</div>'


def ar(colour='red'):
    """A small hand-drawn arrow to use inside text."""
    return (f'<svg class="ar k-{colour}" viewBox="0 0 34 16" aria-hidden="true">'
            '<path d="M2 9 C 10 3, 20 13, 30 8" fill="none"/>'
            '<path d="M24 3 L31 8 L24 13" fill="none"/></svg>')


def tick():
    return '<span class="tickmark">✓</span>'


def cross():
    return '<span class="crossmark">✗</span>'


def boxed(text, colour='red'):
    """Hand-circled answer or value."""
    return f'<span class="ringed k-{colour}">{text}</span>'


def note(text, kind='tip'):
    """A sticky note inside the working. kind: tip, trap, check."""
    label = {'tip': 'Tip', 'trap': 'Trap!', 'check': 'Check'}[kind]
    return f'<div class="sticky sticky-{kind}"><span class="sticky-label">{label}</span> {text}</div>'


def table(rows, head=None, cls=''):
    """Simple printed table. rows: list of lists of HTML cells."""
    h = ''
    if head:
        h = '<thead><tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr></thead>'
    b = '<tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody>'
    return f'<div class="tbl-wrap"><table class="ptable {cls}">{h}{b}</table></div>'


def options(opts):
    """The A-E option list as printed on the paper."""
    return '<ol class="opts">' + ''.join(
        f'<li><b>{k}</b><span>{v}</span></li>' for k, v in opts.items()) + '</ol>'


_FIG_CACHE = {}


def fig(year, name, alt, width=None):
    """Embed a crop of the original paper (figures/<year>/<name>.png) as a data URI."""
    path = HERE / 'figures' / str(year) / f'{name}.png'
    if path not in _FIG_CACHE:
        _FIG_CACHE[path] = base64.b64encode(path.read_bytes()).decode()
    style = f' style="width:{width}px;max-width:100%"' if width else ''
    return (f'<img class="paperfig" alt="{esc(alt)}"{style} '
            f'src="data:image/png;base64,{_FIG_CACHE[path]}">')


# ------------------------------------------------------------------ sketches
# Sketches are inline SVG. Shapes inside rough() get a hand-drawn wobble.
# Colours come from classes so they follow the page theme:
#   stroke: k-pen k-red k-green k-ink k-muted k-orange k-violet
#   fill:   f-y f-p f-g f-b f-o f-v f-paper f-ink f-none, and f-black for things that are black in real life

def svg(w, h, body, label, maxw=None):
    mw = maxw or w
    return (f'<div class="sketch-wrap"><svg class="sketch" viewBox="0 0 {w} {h}" '
            f'style="max-width:{mw}px" role="img" aria-label="{esc(label)}">{body}</svg></div>')


def rough(*parts):
    return '<g class="rough">' + ''.join(parts) + '</g>'


def line(x1, y1, x2, y2, k='pen', w=2.2, dash=False, head=False, tail=False):
    d = ' stroke-dasharray="6 5"' if dash else ''
    m = (f' marker-end="url(#ah-{k})"' if head else '') + (f' marker-start="url(#ah-{k})"' if tail else '')
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="k-{k}" stroke-width="{w}"{d}{m}/>'


def arrow(x1, y1, x2, y2, k='red', bend=0, w=2.2):
    """Curved hand-drawn arrow from (x1,y1) to (x2,y2). bend bows it sideways."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    cx, cy = mx - dy * bend, my + dx * bend
    return (f'<path d="M{x1} {y1} Q{cx:.1f} {cy:.1f} {x2} {y2}" class="k-{k}" stroke-width="{w}" '
            f'fill="none" marker-end="url(#ah-{k})"/>')


def rect(x, y, w, h, k='pen', fill='none', sw=2.2, rx=0):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="k-{k} f-{fill}" '
            f'stroke-width="{sw}"/>')


def circle(cx, cy, r, k='pen', fill='none', sw=2.2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" class="k-{k} f-{fill}" stroke-width="{sw}"/>'


def poly(points, k='pen', fill='none', sw=2.2, closed=True):
    pts = ' '.join(f'{x},{y}' for x, y in points)
    tag = 'polygon' if closed else 'polyline'
    return f'<{tag} points="{pts}" class="k-{k} f-{fill}" stroke-width="{sw}"/>'


def path(d, k='pen', fill='none', sw=2.2):
    return f'<path d="{d}" class="k-{k} f-{fill}" stroke-width="{sw}"/>'


def text(x, y, s, k='ink', size=18, anchor='middle', font='hand', weight=None, rotate=None):
    """font: hand (Patrick Hand), scrawl (Caveat), print (exam-style sans)."""
    wt = f' font-weight="{weight}"' if weight else ''
    rt = f' transform="rotate({rotate} {x} {y})"' if rotate else ''
    return (f'<text x="{x}" y="{y}" class="t-{font} c-{k}" font-size="{size}" '
            f'text-anchor="{anchor}"{wt}{rt}>{s}</text>')


def eye(x, y, k='ink', facing='right'):
    """A little eye doodle, used for 'look from here' in view questions."""
    flip = {'right': 0, 'left': 180, 'down': 90, 'up': 270}[facing]
    return (f'<g transform="translate({x} {y}) rotate({flip})">'
            f'<path d="M-14 0 Q0 -11 14 0 Q0 11 -14 0Z" class="k-{k} f-paper" stroke-width="2"/>'
            f'<circle cx="2" cy="0" r="4" class="k-{k} f-ink" stroke-width="1"/></g>')


def stick_person(x, y, k='pen', s=1.0):
    """Tiny stick figure standing at (x, y) = feet position."""
    return (f'<g transform="translate({x} {y}) scale({s})" class="k-{k}" fill="none" stroke-width="2">'
            f'<circle cx="0" cy="-34" r="6"/><line x1="0" y1="-28" x2="0" y2="-12"/>'
            f'<line x1="0" y1="-24" x2="-8" y2="-17"/><line x1="0" y1="-24" x2="8" y2="-17"/>'
            f'<line x1="0" y1="-12" x2="-7" y2="0"/><line x1="0" y1="-12" x2="7" y2="0"/></g>')


def brace(x1, x2, y, label, k='red', size=17, down=True):
    """Curly bracket under (or over) a horizontal span with a label."""
    h = 9 if down else -9
    mid = (x1 + x2) / 2
    d = (f'M{x1} {y} q0 {h} 8 {h} L{mid - 8} {y + h} q8 0 8 {h} q0 {-h} 8 {-h} '
         f'L{x2 - 8} {y + h} q8 0 8 {-h}')
    ty = y + h * 2 + (size if down else -6)
    return path(d, k=k, sw=2) + text(mid, ty, label, k=k, size=size)
