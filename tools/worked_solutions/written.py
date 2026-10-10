"""Written methods for the arithmetic in the worked solutions, and a clearer division sign.

add_methods(step_html) finds sums in a working step, such as "903 − 689 = 214" or "12 000 ÷ 25 = 480 ml",
checks that the stated answer is right, and draws the written method underneath:
    + : column addition (carries under the line)
    − : column subtraction (exchanges shown above the top number)
    × : short multiplication (one-digit multiplier) or long multiplication (a row for each digit)
    ÷ : bus stop (short) division for divisors up to 12, long division otherwise
Decimals are lined up on the point. Only sums whose stated answer checks out are drawn, and basic facts
(times tables, 5 + 10, 100 − 30 ...) are left as they are.

clear_division(html) swaps every ÷ for a drawn sign with bold dots (the handwriting font's ÷ is too faint).
"""

import html as _html
import re
from decimal import Decimal, getcontext

getcontext().prec = 50

TERM = r'(?:[£$€]\s?)?(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d{1,3}(?: \d{3})+(?![\d.])|\d+(?:\.\d+)?)%?'
LABEL = r'(?:\s?[A-Za-z²³]{1,12}(?:/[A-Za-z]{1,4})?)?'
OP = r'[+−\-×÷]'
CHAIN = re.compile(rf'(?<![\w.:/(^]){TERM}{LABEL}(?:\s*{OP}\s*{TERM}{LABEL})+\s*[=≈]\s*{TERM}(?![\d:/])')
START = re.compile(r'(?<![\w.:/(^])(?:[£$€]\s?)?\d')
PART = re.compile(rf'(?P<term>{TERM})|(?P<op>{OP})|(?P<eq>[=≈])')
MAX_DP = 4


# ---------------------------------------------------------------- finding sums

def to_text(fragment):
    """Plain text of an HTML fragment, without sketches, stacked fractions or superscripts."""
    s = re.sub(r'<svg\b.*?</svg>', ' ', fragment, flags=re.S)
    s = re.sub(r'<span class="frac">.*?</span></span>', ' ¦ ', s, flags=re.S)
    s = re.sub(r'<sup\b.*?</sup>', '^', s, flags=re.S)
    s = re.sub(r'<br\s*/?>|</div>|</p>|</li>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    return _html.unescape(s)


def num(term):
    t = term.lstrip('£$€').strip().replace(',', '').replace(' ', '')
    return Decimal(t.rstrip('%'))


def dp(d):
    e = d.as_tuple().exponent
    return max(0, -e)


def find_sums(text):
    """Each checked sum as (shown text, terms, ops, stated answer, approximate?)."""
    out, pos = [], 0
    while True:
        m = START.search(text, pos)
        if not m:
            return out
        c = CHAIN.match(text, m.start())
        if not c:
            pos = m.start() + 1
            continue
        parts = [(p.lastgroup, p.group()) for p in PART.finditer(c.group())]
        terms, ops, stated, approx, seen_eq = [], [], None, False, False
        for kind, val in parts:
            if kind == 'term' and not seen_eq:
                terms.append(val)
            elif kind == 'op' and not seen_eq:
                ops.append('-' if val in '−-' else val)
            elif kind == 'eq':
                seen_eq, approx = True, val == '≈'
            elif kind == 'term' and seen_eq and stated is None:
                stated = val
        ok = (len(terms) == len(ops) + 1 and stated is not None and not any('%' in t for t in terms + [stated]))
        if ok:
            vals = [num(t) for t in terms]
            value = evaluate(vals, ops)
            s = num(stated)
            if value is not None and value >= 0 and matches(value, s, approx):
                shown = re.sub(r'\s+', ' ', c.group()).strip()
                out.append((shown, vals, ops, s, approx))
                pos = c.end()
                continue
        pos = m.start() + 1


def evaluate(vals, ops):
    if set(ops) <= {'+', '-'} or set(ops) <= {'×', '÷'}:
        v = vals[0]
        for o, x in zip(ops, vals[1:]):
            if o == '+':
                v += x
            elif o == '-':
                v -= x
            elif o == '×':
                v *= x
            else:
                if x == 0:
                    return None
                v /= x
        return v
    return None


def matches(value, stated, approx):
    if value == stated:
        return True
    if approx:
        q = Decimal(1).scaleb(-dp(stated))
        return abs(value - stated) <= q / 2 + Decimal('1e-30') or value.quantize(q) == stated
    return False


# ---------------------------------------------------------------- deciding what to draw

def core(d):
    """Digits without the point and without trailing zeros, e.g. 0.40 -> 4, 1200 -> 12."""
    s = format(d.normalize(), 'f').replace('.', '').lstrip('0') or '0'
    return int(s.rstrip('0') or '0')


def strip_common_zeros(a, b):
    if a != a.to_integral_value() or b != b.to_integral_value():
        return a, b
    while a and b and a % 10 == 0 and b % 10 == 0:
        a, b = a / 10, b / 10
    return a, b


def worth_adding(terms):
    if any(dp(t) for t in terms):
        return True
    cores = sorted((core(t) for t in terms), reverse=True)
    return cores[0] >= 100 or (len(cores) > 1 and cores[1] >= 10 and sum(cores) >= 20)


def worth_subtracting(a, b):
    if dp(a) or dp(b):
        return True
    a, b = strip_common_zeros(a, b)
    return a >= 100 or (a >= 20 and b >= 10)


def worth_multiplying(a, b):
    if core(a) == 1 or core(b) == 1:      # x 10, x 100, x 0.1 ...
        return False
    return not (core(a) <= 12 and core(b) <= 12)


def worth_dividing(a, b, q):
    a, b = strip_common_zeros(a, b)
    if b != b.to_integral_value():
        return True
    return not (b <= 12 and q == q.to_integral_value() and core(q) <= 12 and dp(a) == 0)


def methods_for(vals, ops, stated, approx):
    """The written methods for one sum, as HTML strings."""
    out = []
    if set(ops) <= {'+', '-'}:
        acc, i = vals[0], 0
        while i < len(ops):
            if ops[i] == '+':
                group = [acc]
                while i < len(ops) and ops[i] == '+':
                    group.append(vals[i + 1])
                    i += 1
                total = sum(group, Decimal(0))
                if worth_adding(group):
                    out.append(col_add(group, total))
                acc = total
            else:
                b = vals[i + 1]
                if worth_subtracting(acc, b) and acc >= b:
                    out.append(col_sub(acc, b))
                acc -= b
                i += 1
        return out
    acc = vals[0]
    for o, x in zip(ops, vals[1:]):
        if o == '×':
            r = acc * x
            if worth_multiplying(acc, x):
                out.append(multiply(acc, x, r))
            acc = r
        else:
            r = acc / x
            last = o is ops[-1] and x is vals[-1]
            places = dp(stated) + (1 if approx else 0) if last else MAX_DP
            if worth_dividing(acc, x, r):
                m = divide(acc, x, places, stated if last else None, approx and last)
                if m:
                    out.append(m)
            acc = r
    return out


# ---------------------------------------------------------------- drawing
# Each method is a small table: one column per place value (plus a narrow column for the point).
# A cell is None (empty) or (html, classes).

def fmt(d):
    s = format(d, 'f')
    return s.rstrip('0').rstrip('.') if '.' in s else s


def int_len(d):
    return len(format(d, 'f').partition('.')[0].lstrip('0')) or 1


def by_place(d, L, F):
    """Digit values (or None for empty places on the left) from the 10^(L-1) column down to the 10^-F column."""
    ip, _, fp = format(d, 'f').partition('.')
    ip = ip.lstrip('0') or '0'
    return [None] * (L - len(ip)) + [int(c) for c in ip] + [int(c) for c in fp] + ['pad'] * (F - len(fp))


def cells(values, L, F, cls='', faint_pad=True):
    """Turn place values into cells, putting the point between the units and tenths columns."""
    out = []
    for i, v in enumerate(values):
        if i == L and F:
            out.append(('.', ('pt ' + cls).strip()))
        if v is None:
            out.append(('', cls) if cls else None)
        elif v == 'pad':
            out.append(('0', ('fz ' + cls).strip() if faint_pad else cls))
        else:
            out.append((str(v), cls))
    return out


def table(rows, cap, note='', cls=''):
    body = ''
    for cls, row in rows:
        tds = ''.join('<td></td>' if c is None else (f'<td class="{c[1]}">{c[0]}</td>' if c[1] else f'<td>{c[0]}</td>')
                      for c in row)
        body += f'<tr class="{cls}">{tds}</tr>' if cls else f'<tr>{tds}</tr>'
    n = f'<div class="wm-note">{note}</div>' if note else ''
    t = f'<table class="{cls}">' if cls else '<table>'
    return f'<div class="wm"><div class="wm-cap">{cap}</div>{t}{body}</table>{n}</div>'


def carry_row(carry_in, L, F):
    """Small carry digits, each in the column it was carried into."""
    vals = [(c if c else None) for c in carry_in]
    row = []
    for i, v in enumerate(vals):
        if i == L and F:
            row.append(None)
        row.append((str(v), 'cy') if v else None)
    return row


def col_add(terms, total):
    F = max(dp(t) for t in terms + [total])
    L = max(int_len(t) for t in terms + [total])
    n = L + F
    digs = [[0 if v in (None, 'pad') else v for v in by_place(t, L, F)] for t in terms]
    carry_in = [0] * n
    for c in range(n - 1, 0, -1):
        carry_in[c - 1] = (sum(d[c] for d in digs) + carry_in[c]) // 10
    rows = [('', [('+', 'op') if i == len(terms) - 1 else None] + cells(by_place(t, L, F), L, F))
            for i, t in enumerate(terms)]
    rows.append(('res', [None] + cells(by_place(total, L, F), L, F, 'sum', faint_pad=False)))
    cy = carry_row(carry_in, L, F)
    if any(cy):
        rows.append(('cyrow', [None] + cy))
    return table(rows, ' + '.join(fmt(t) for t in terms) + ' · column addition')


def col_sub(a, b):
    F = max(dp(a), dp(b))
    L = max(int_len(a), int_len(b))
    n = L + F
    top = [0 if v in (None, 'pad') else v for v in by_place(a, L, F)]
    bot = [0 if v in (None, 'pad') else v for v in by_place(b, L, F)]
    work, changed = top[:], [False] * n
    for c in range(n - 1, -1, -1):
        if work[c] < bot[c]:
            j = c - 1
            while work[j] == 0:
                j -= 1
            work[j] -= 1
            changed[j] = True
            for k in range(j + 1, c):
                work[k] += 9
                changed[k] = True
            work[c] += 10
            changed[c] = True
    shown = []
    for i, v in enumerate(by_place(a, L, F)):
        if i == L and F:
            shown.append(('.', 'pt'))
        if v is None:
            shown.append(None)
        elif changed[i]:
            d = '0' if v == 'pad' else str(v)
            shown.append((f'<span class="x">{d}</span><span class="nv">{work[i]}</span>', 'ex'))
        else:
            shown.append(('0', 'fz') if v == 'pad' else (str(v), ''))
    rows = [('ex-row', [None] + shown), ('', [('−', 'op')] + cells(by_place(b, L, F), L, F)),
            ('res', [None] + cells(by_place(a - b, L, F), L, F, 'sum', faint_pad=False))]
    return table(rows, f'{fmt(a)} − {fmt(b)} · column subtraction')


def as_whole(d):
    """d as a whole number of its digits, and how many decimal places that removed (0.45 -> 45, 2)."""
    d = d.normalize()
    places = max(0, -d.as_tuple().exponent)
    return int(d.scaleb(places)), places


def multiply(a, b, r):
    big, small = (a, b) if core(a) >= core(b) else (b, a)
    si, sp = as_whole(small)
    tz = 0
    while si and si % 10 == 0:
        si, tz = si // 10, tz + 1
    if si < 10 and sp == 0 and tz == 0:
        # short multiplication with the point kept in place
        F, L = dp(big), max(int_len(big), int_len(r))
        n = L + F
        top = [0 if v in (None, 'pad') else v for v in by_place(big, L, F)]
        carry_in = [0] * n
        for c in range(n - 1, 0, -1):
            carry_in[c - 1] = (top[c] * si + carry_in[c]) // 10
        mult = [None] * (L + F - 1) + [si]
        mrow = [None if v is None else (str(v), '') for v in mult]
        if F:
            mrow.insert(L, None)
        rows = [('', [None] + cells(by_place(big, L, F), L, F)), ('', [('×', 'op')] + mrow),
                ('res', [None] + cells(by_place(r, L, F), L, F, 'sum', faint_pad=False))]
        cy = carry_row(carry_in, L, F)
        if any(cy):
            rows.append(('cyrow', [None] + cy))
        return table(rows, f'{fmt(a)} × {fmt(b)} · short multiplication')
    bi, bp = as_whole(big)
    prod = bi * si
    W = max(len(str(prod)), len(str(bi)), len(str(si)))

    def line(s, cls='', faint_tail=0):
        s = s.rjust(W)
        return [None if ch == ' ' else (ch, (('fz ' if j >= W - faint_tail else '') + cls).strip())
                for j, ch in enumerate(s)]

    if si < 10:
        kind = 'short multiplication'
        top = [int(c) for c in str(bi).rjust(W, '0')]
        carry_in = [0] * W
        for c in range(W - 1, 0, -1):
            carry_in[c - 1] = (top[c] * si + carry_in[c]) // 10
        rows = [('', [None] + line(str(bi))), ('', [('×', 'op')] + line(str(si))),
                ('res', [None] + [c if c else ('', 'sum') for c in line(str(prod), 'sum')])]
        cy = [(str(c), 'cy') if c else None for c in carry_in]
        if any(cy):
            rows.append(('cyrow', [None] + cy))
    else:
        kind = 'long multiplication'
        partials = [(bi * int(ch) * 10 ** i, i, int(ch) * 10 ** i) for i, ch in enumerate(reversed(str(si))) if ch != '0']
        rows = [('', [None] + line(str(bi)) + [None]), ('', [('×', 'op')] + line(str(si)) + [None])]
        for k, (p, i, m) in enumerate(partials):
            rows.append(('first' if k == 0 else '', [None] + line(str(p), faint_tail=i) + [(f'× {m}', 'lab')]))
        rows.append(('res', [('+', 'op')] + [c if c else ('', 'sum') for c in line(str(prod), 'sum')] + [None]))
    note = ''
    if bp + sp or tz:
        note = (f'Leave out the point{"s" if bp + sp > 1 else ""} and zeros: {bi} × {si} = {prod}. '
                f'Then put the size back: {fmt(a)} × {fmt(b)} = <b>{fmt(r)}</b>')
    return table(rows, f'{fmt(a)} × {fmt(b)} · {kind}', note)


def divide(a, b, places, stated, approx):
    a0, b0 = a, b
    note = []
    scale = 0
    while b != b.to_integral_value():
        a, b, scale = a * 10, b * 10, scale + 1
    if scale:
        note.append(f'× {10 ** scale} first to make the divisor whole: {fmt(a0)} ÷ {fmt(b0)} = {fmt(a)} ÷ {fmt(b)}')
    b = int(b)
    ip, _, fp = format(a.normalize(), 'f').partition('.')
    ip = ip.lstrip('0') or '0'
    digits = [int(c) for c in ip + fp]
    Li = len(ip)
    rem = 0
    for d in digits:
        rem = (rem * 10 + d) % b
    extra = 0
    want = min(places, MAX_DP)
    while rem and (len(fp) + extra < want or (not approx and len(fp) + extra < MAX_DP)):
        rem = rem * 10 % b
        extra += 1
    if rem and not approx:
        return None
    digits += [0] * extra
    nf = len(fp) + extra

    def col(i):
        return i + (1 if nf and i >= Li else 0)

    width = len(digits) + (1 if nf else 0)
    qd, steps, cur = [], [], 0
    for i, d in enumerate(digits):
        cur = cur * 10 + d
        q = cur // b
        qd.append(q)
        if q:
            steps.append((i, cur, q * b))
            cur -= q * b
    final = cur
    if not steps:
        return None
    qrow = [None] * width
    on = False
    for i, q in enumerate(qd):
        on = on or q > 0 or i >= Li - 1
        if on:
            qrow[col(i)] = (str(q), 'qt')
    if nf:
        qrow[Li] = ('.', 'pt qt')
    faint_from = len(digits) - extra
    if b <= 12:
        kind = 'bus stop division'
        drow, r = [], 0
        for i, d in enumerate(digits):
            carry = f'<span class="ci">{r}</span>' if r else ''
            drow.append((f'{carry}{d}', ('fz ' if i >= faint_from else '') + 'roof' + (' wall' if i == 0 else '')))
            r = (r * 10 + d) % b
        if nf:
            drow.insert(Li, ('.', 'pt roof'))
        rows = [('', [None] + qrow), ('', [(str(b), 'dv')] + drow)]
        tcls = 'bus'
    else:
        tcls = ''
        kind = 'long division'
        drow = [(str(d), ('fz ' if i >= faint_from else '') + 'roof' + (' wall' if i == 0 else '')) for i, d in enumerate(digits)]
        if nf:
            drow.insert(Li, ('.', 'pt roof'))
        rows = [('', [None, None] + qrow), ('', [(str(b), 'dv'), None] + drow)]

        def put(row, number, end, cls=''):
            i = end
            for ch in reversed(str(number)):
                row[2 + col(i)] = (ch, cls)
                i -= 1
            return 2 + col(i + 1)

        for k, (i, _cur, prod) in enumerate(steps):
            prow = [None] * (width + 2)
            start = put(prow, prod, i)
            prow[start - 1] = ('−', 'op')
            rows.append(('', prow))
            end = steps[k + 1][0] if k + 1 < len(steps) else len(digits) - 1
            value = steps[k + 1][1] if k + 1 < len(steps) else final
            rrow = [None] * (width + 2)
            put(rrow, value, end)
            for c in range(start, 2 + col(end) + 1):
                rrow[c] = (rrow[c][0], (rrow[c][1] + ' sum').strip()) if rrow[c] else ('', 'sum')
            rows.append(('', rrow))
    if approx and stated is not None:
        note.append(f'≈ {fmt(stated)} after rounding')
    elif final:
        note.append(f'remainder {final}')
    return table(rows, f'{fmt(a0)} ÷ {fmt(b0)} · {kind}', ' · '.join(note), tcls)


# ---------------------------------------------------------------- putting them in the page

def _balanced_div(s, start):
    """Index just after the </div> that closes the <div ...> starting at `start`."""
    depth, i = 0, start
    tag = re.compile(r'<(/?)div\b[^>]*>')
    for m in tag.finditer(s, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    return len(s)


def _render(sums, done):
    out = []
    for shown, vals, ops, stated, approx in sums:
        if shown in done:
            continue
        done.add(shown)
        try:
            out += methods_for(vals, ops, stated, approx)
        except (ArithmeticError, ValueError, IndexError):
            continue
    return f'<div class="wms">{"".join(out)}</div>' if out else ''


def add_methods(step_html, done=None):
    """step_html with the written methods for its sums added after each calc block (and at the end for the rest)."""
    done = set() if done is None else done
    out, pos = [], 0
    for m in re.finditer(r'<div class="calc">', step_html):
        if m.start() < pos:
            continue
        end = _balanced_div(step_html, m.start())
        block = step_html[m.start():end]
        out.append(step_html[pos:end])
        out.append(_render(find_sums(to_text(block)), done))
        pos = end
    out.append(step_html[pos:])
    joined = ''.join(out)
    rest = re.sub(r'<div class="calc">.*?</div></div>', ' ', step_html, flags=re.S)
    rest = re.sub(r'<div class="sticky.*?</div>', ' ', rest, flags=re.S)
    return joined + _render(find_sums(to_text(rest)), done)


DIV_SVG = ('<svg class="dvs" viewBox="0 0 12 12" role="img" aria-label="divided by"><path d="M1.6 6h8.8"/>'
           '<circle cx="6" cy="2.3" r="1.35"/><circle cx="6" cy="9.7" r="1.35"/></svg>')


def clear_division(page):
    """Replace ÷ in text with a drawn sign (in sketches, with a bold sans-serif ÷)."""
    out, depth = [], 0
    for part in re.split(r'(<[^>]+>)', page):
        if part.startswith('<'):
            if re.match(r'<svg\b', part):
                depth += 1
            elif part.startswith('</svg'):
                depth -= 1
            out.append(part)
        elif '÷' in part:
            out.append(part.replace('÷', '<tspan class="dvt">÷</tspan>' if depth else DIV_SVG))
        else:
            out.append(part)
    return ''.join(out)
