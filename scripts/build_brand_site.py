"""Build the public Index with the main website's actual shared stylesheet.

The research publisher may replace index.html nightly. Applying the brand at
Pages build time keeps that publisher's data and markup intact while retaining
the shared theme on every deployment.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
MAIN='https://prismaticalgos.com'
FALLBACK=MAIN+'/_next/static/chunks/3t9xluh6psjy7.css'

def shared_styles():
    try:
        with urllib.request.urlopen(MAIN+'/',timeout=20) as r:
            home=r.read().decode()
        tags=re.findall(r'<link\b[^>]*>',home)
        paths=[re.search(r'href="([^"]+)"',tag).group(1) for tag in tags if 'rel="stylesheet"' in tag]
        urls=[MAIN+p if p.startswith('/') else p for p in paths]
        assert urls and all(u.startswith(MAIN+'/') for u in urls)
        return urls
    except Exception:
        # The last verified shared stylesheet keeps research publication viable
        # when the homepage cannot be inspected during a deployment.
        return [FALLBACK]

ADAPTER='''
/* Layout adapter; colors and fonts come from PrismaticAlgos.com shared CSS. */
:root{--soft:var(--paper);--panel:var(--wash);--bright:var(--ink);--mut:var(--muted);--cyan:var(--accent);--violet:var(--muted);--magenta:var(--ink);--gold:var(--accent);--tb:var(--accent);--mr:var(--ink);--sc:var(--muted);--display:Georgia,'Times New Roman',serif;--ui:Geist,Arial,sans-serif;--mono:GeistMono,ui-monospace,Menlo,monospace}
html,body{background:var(--bg);color:var(--ink)}
body{font:16px/1.7 var(--ui)}
main{max-width:1120px;margin:0 auto;padding:12px 24px 56px}
.rays{display:none}
.brand{color:var(--accent);font-family:var(--ui);font-weight:600;letter-spacing:.14em;margin-top:32px}
.brand a,a{color:var(--accent)}
h1{font-family:var(--display);font-size:clamp(32px,4vw,62px);color:var(--ink);letter-spacing:-.035em;margin:12px 0 14px}
.tagline,.sig{color:var(--accent)}
.sub,.status,.hyp,.foot{color:var(--muted)}
.status{border:0;background:transparent;padding:0;border-radius:0;display:block}
.grid{gap:16px;margin:24px 0}
.card{background:var(--paper);border-color:var(--line);border-radius:10px;padding:22px;overflow-x:auto}
.card.fam h3{color:var(--ink)}
.big{color:var(--ink);font-family:var(--display)}
.tag{background:var(--wash);color:var(--muted);border-color:var(--line)}
td,th{border-color:var(--line)}
pre,code{background:var(--wash);color:var(--ink)}
a:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
@media(max-width:650px){main{padding:8px 16px 32px}.card{padding:18px}.grid{grid-template-columns:1fr}h1 .tag{display:table;margin:12px 0 0}.status{overflow-wrap:anywhere}}
'''

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    styles=shared_styles()
    links=''.join('<link rel="stylesheet" data-prismatic-shared-css="1" href="'+u+'">' for u in styles)
    for name in ['index.html','methodology.html']:
        source=(ROOT/name).read_text()
        # Remove the independent dark palette, leaving research structure intact.
        page=re.sub(r':root\{[^}]*\}','',source)
        page=re.sub(r'<link[^>]+(?:fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>','',page)
        page=page.replace('</head>',links+'<style id="prismatic-index-layout">'+ADAPTER+'</style></head>',1)
        page=page.replace("Chart.defaults.color='#9799a3';Chart.defaults.borderColor='rgba(255,255,255,.08)';", "Chart.defaults.color=cs.getPropertyValue('--muted').trim();Chart.defaults.borderColor=cs.getPropertyValue('--line').trim();")
        page=page.replace("grid:{color:'rgba(255,255,255,.07)'}", "grid:{color:cs.getPropertyValue('--line').trim()}")
        page=page.replace("'Geist Mono'", "'GeistMono'")
        page=page.replace('<p class="brand">Prismatic Algos <span>', '<p class="brand"><a href="https://prismaticalgos.com/">Prismatic Algos</a> <span>')
        assert 'data-prismatic-shared-css' in page
        assert '--ink:#05070d' not in page
        (OUT/name).write_text(page)
    shutil.copy2(ROOT/'methodology.md',OUT/'methodology.md')
    shutil.copytree(ROOT/'data',OUT/'data')
    for p in (ROOT/'data').rglob('*'):
        if p.is_file(): assert p.read_bytes()==(OUT/'data'/p.relative_to(ROOT/'data')).read_bytes()
    (OUT/'brand-build.json').write_text(json.dumps({'sharedStylesheets':styles,'theme':'main website','researchDataChanged':False},indent=2)+'\n')
    print(json.dumps({'output':str(OUT),'sharedStylesheets':styles,'researchDataChanged':False}))

if __name__=='__main__': build()
