#!/usr/bin/env python3
"""Génère references/widgets/*.md + widgets-index.md depuis widgets-dump.json.

Usage :
  wp eval-file extract-widgets.php   # produit widgets-dump.json (adapter le chemin de sortie)
  python3 generate-widget-refs.py <widgets-dump.json> <dossier-sortie> [<version-elementor>]
"""
import json, collections, re, os, sys

dump, outdir = sys.argv[1], sys.argv[2]
version = sys.argv[3] if len(sys.argv) > 3 else '?'
data = json.load(open(dump))
skip_names = {'common', 'common-base', 'common-optimized', 'global', 'inner-section', 'template'}

def bucket(w):
    n = w['name']
    if n in skip_names or n.startswith(('jet-', 'wp-widget-')):
        return None
    return 'pro' if w['pro'] else 'core'

ws = [w for w in data if bucket(w)]
freq = collections.Counter(c['id'] for w in ws for c in w['controls'])
common = {cid for cid, n in freq.items() if n >= 0.9 * len(ws)}

RESP = re.compile(r'_(tablet|mobile|widescreen|laptop|tablet_extra|mobile_extra)$')
NOISE = re.compile(r'(_slideshow_|_video_link|_video_start|_video_end|_play_once|_play_on_mobile|_privacy_mode|_ken_burns)')
GROUPS = [
    ('_typography', 'GROUPE typo', ['_font_family', '_font_size', '_font_weight', '_text_transform', '_font_style', '_text_decoration', '_line_height', '_letter_spacing', '_word_spacing']),
    ('_border', 'GROUPE bordure', ['_width', '_color']),
    ('_box_shadow_type', 'GROUPE box_shadow', ['_box_shadow', '_box_shadow_position']),
    ('_text_shadow_type', 'GROUPE text_shadow', ['_text_shadow']),
    ('_text_stroke_type', 'GROUPE text_stroke', ['_text_stroke', '_stroke_color']),
    ('_background', 'GROUPE background', ['_color', '_color_stop', '_color_b', '_color_b_stop', '_gradient_angle', '_gradient_type', '_gradient_position', '_image', '_position', '_xpos', '_ypos', '_attachment', '_repeat', '_size', '_bg_width', '_video_fallback', '_transition']),
]
TYPE_HINT = {'slider': 'slider{unit,size}', 'dimensions': 'dim{t,r,b,l,unit,isLinked}',
             'media': 'media{id,url}', 'icons': 'icons{value,library}', 'url': 'url{url,is_external}',
             'color': 'color', 'repeater': 'repeater[]', 'gallery': 'gallery[{id,url}]', 'wysiwyg': 'html',
             'code': 'code', 'switcher': "'yes'", 'textarea': 'txt', 'text': 'txt', 'number': 'nb',
             'date_time': 'datetime', 'box_shadow': 'box_shadow', 'text_shadow': 'text_shadow'}

def fmt(c):
    s = '`' + c['id'] + '`'
    if c['options']:
        opts = [str(o) for o in c['options']]
        s += '(' + '|'.join(opts[:10]) + ('|…' if len(opts) > 10 else '') + ')'
    elif c['type'] in TYPE_HINT:
        s += ':' + TYPE_HINT[c['type']]
    d = c.get('default')
    if d not in (None, '', [], {}) and isinstance(d, (str, int, float)) and len(str(d)) <= 16:
        s += f'[={d}]'
    return s

def compress(ctrls):
    ids = {c['id'] for c in ctrls}
    absorbed, found = set(), []
    for c in ctrls:
        for suf, label, subs in GROUPS:
            if c['id'].endswith(suf):
                stem = c['id'][:-len(suf)]
                members = [c['id']] + [stem + s for s in subs if stem + s in ids]
                if len(members) >= 3:
                    absorbed.update(members)
                    found.append((c['id'], label))
                break
    out = [f'`{gid}`+{label}' for gid, label in found]
    out += [fmt(c) for c in ctrls if c['id'] not in absorbed]
    return out

def keep(c):
    return c['id'] not in common and not RESP.search(c['id']) and not NOISE.search(c['id'])

def variant_root(n):
    m = re.match(r'(.+)-var-\d+$', n)
    return m.group(1) if m else n

os.makedirs(f'{outdir}/widgets', exist_ok=True)
index_lines, roots = {'core': [], 'pro': []}, {}
for w in sorted(ws, key=lambda x: x['name']):
    root = variant_root(w['name'])
    if root != w['name']:
        roots.setdefault(root, []).append(w['name'])
        continue
    specific = [c for c in w['controls'] if keep(c)]
    by_tab = collections.OrderedDict()
    for c in specific:
        by_tab.setdefault(c['tab'] or '?', collections.OrderedDict()).setdefault(c['section'] or '?', []).append(c)
    lines = [f"# `{w['name']}` — {w['title']} ({'Pro' if w['pro'] else 'core'})", '',
             '`x`+GROUPE = groupe de contrôles (sous-clés dans common-controls.md). Suffixes responsive `_tablet`/`_mobile` dispo sur les contrôles responsive.', '']
    for tab, sections in by_tab.items():
        lines.append(f'## onglet {tab}')
        for sec, ctrls in sections.items():
            lines.append(f'- {sec} : ' + ', '.join(compress(ctrls)))
        lines.append('')
    open(f"{outdir}/widgets/{w['name']}.md", 'w').write('\n'.join(lines))
    index_lines[bucket(w)].append(w['name'])

with open(f'{outdir}/widgets-index.md', 'w') as f:
    f.write(f"""# Index des widgets Elementor / Elementor Pro (généré depuis Elementor {version})

Détail des contrôles d'un widget : `references/widgets/<nom>.md`. Charger UNIQUEMENT les
fichiers des widgets qu'on s'apprête à utiliser. Formats de valeurs et contrôles communs
(onglet Avancé `_*`, responsive, groupes background/typo/border) : `references/common-controls.md`.

""")
    for b, label in (('core', 'Elementor (gratuit)'), ('pro', 'Elementor Pro')):
        f.write(f'## {label} ({len(index_lines[b])})\n`' + '`, `'.join(index_lines[b]) + '`\n\n')
    for root, variants in sorted(roots.items()):
        f.write(f"Variantes de `{root}` (mêmes contrôles, layout différent) : `{'`, `'.join(variants)}`\n")
print('OK:', len(index_lines['core']), 'core +', len(index_lines['pro']), 'pro widgets ->', outdir)
