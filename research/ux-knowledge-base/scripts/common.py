import json, re, os, html
from bs4 import BeautifulSoup
SRC = os.environ.get('KB_SRC', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sources'))
OUT = os.environ.get('KB_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'build'))
FIELDS = ['id','source_set','source_org','author','year','category','subcategory','title','statement',
          'rationale','audit_check','detection_layer','threshold','applies_to','level','severity_default',
          'citation','url','text_origin','license','confidence']
def clean(t):
    if t is None: return ''
    t = html.unescape(t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t
def soup_text(el):
    if el is None: return ''
    return clean(el.get_text(' '))
def md_to_text(md):
    md = re.sub(r'\{%.*?%\}', '', md, flags=re.S)
    md = re.sub(r'\{\{.*?\}\}', '', md, flags=re.S)
    md = re.sub(r'<[^>]+>', ' ', md)
    md = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
    md = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', md)
    md = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', md)
    md = re.sub(r'\|\s*:?-{3,}:?\s*', ' ', md)
    md = re.sub(r'\s\|\s', '; ', md)
    md = re.sub(r'[*_`#>|]+', '', md)
    return clean(md)
def row(**kw):
    r = {f: '' for f in FIELDS}
    for k, v in kw.items():
        if k not in r: raise KeyError(k)
        r[k] = clean(str(v)) if v is not None else ''
    return r
def write(name, rows):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name + '.jsonl'), 'w') as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(name, len(rows))

CATS = [
 ('Errors & recovery', r'\b(errors?|mistakes?|undo|recover\w*|destructive|error messages?|validation)\b'),
 ('Forms & input', r'\b(forms?|fields?|inputs?|labels?|checkbox(es)?|radios?|selects?|dropdowns?|textareas?|date pickers?|date inputs?|autocomplete|placeholders?|fieldsets?|question pages?|text fields?|combo ?box(es)?|sliders?|toggles?|switch(es)?|file uploads?)\b'),
 ('Authentication, security & privacy', r'\b(passwords?|sign[- ]?in|log ?in|login|authenticat\w*|security|privacy|cookies?|consent|personal (data|information)|usernames?|two-factor|2fa)\b'),
 ('Search & filtering', r'\b(search\w*|filter\w*|sort\w*|facets?)\b'),
 ('Navigation & IA', r'\b(navigation|nav|menus?|breadcrumbs?|side ?nav|headers?|footers?|tabs|pagination|links?|information architecture|wayfinding|back links?|step-by-step|site map|hierarchy)\b'),
 ('Feedback & system status', r'\b(feedback|notifications?|alerts?|banners?|toasts?|status\w*|progress\w*|loading|spinners?|skeletons?|success messages?|saving|badges?|tags?)\b'),
 ('Actions & buttons', r'\b(buttons?|calls? to action|cta|primary actions?|secondary actions?|disabled|actions?)\b'),
 ('Data display & tables', r'\b(tables?|data visuali[sz]ations?|charts?|graphs?|summary lists?|data grids?|lists?|dashboards?)\b'),
 ('Onboarding & first use', r'\b(onboarding|start pages?|first[- ]time|empty states?|getting started|interruption|tours?|walkthroughs?)\b'),
 ('Content & microcopy', r'\b(plain language|content|copy|writing|write|words?|sentences?|tone|voice|headings?|jargon|readab\w*|microcopy|terminology|capitali[sz]\w*|grammar|punctuation|abbreviations?|numbers|dates|style guide)\b'),
 ('Accessibility', r'\b(accessib\w*|screen readers?|keyboard|focus|aria|wcag|assistive|disabilit\w*)\b'),
 ('Visual design & layout', r'\b(layout|spacing|grid|typograph\w*|fonts?|colou?rs?|contrast|icons?|visual hierarchy|alignment|white ?space|density|elevation|shadows?|themes?|illustrations?|images?)\b'),
 ('Mobile & touch', r'\b(mobile|touch|tap|gestures?|responsive|small screens?)\b'),
 ('Motion & animation', r'\b(motion|animations?|animate|transitions?)\b'),
 ('Trust & credibility', r'\b(trust\w*|credib\w*|reassur\w*)\b'),
 ('AI & automation', r'\b(ai|artificial intelligence|machine learning|generative|agents?|llm)\b'),
 ('Research & process', r'\b(research\w*|interviews?|usability test\w*|prototyp\w*|user needs?|personas?|journey|surveys?|methods?|workshops?|stakeholders?|synthesis)\b'),
]
def categorize(*texts, default='General UX'):
    t = ' '.join(texts).lower()
    for name, rx in CATS:
        if re.search(rx, t): return name
    return default

def split_md_sections(md):
    """yield (h2, h3, text) for markdown; frontmatter removed"""
    md = re.sub(r'^---\n.*?\n---\n', '', md, flags=re.S)
    md = re.sub(r'```.*?```', '', md, flags=re.S)
    md = re.sub(r'<(Code|Example|Canvas|Story|ImageFixture|DoDontRow|Row|Column|Tabs?|Video|Image|Grid|AnchorLinks?)[^>]*/>', '', md)
    md = re.sub(r'^import .*$', '', md, flags=re.M)
    h2 = h3 = ''; buf = []
    out = []
    for line in md.split('\n'):
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            if buf: out.append((h2, h3, '\n'.join(buf))); buf = []
            lvl = len(m.group(1)); t = md_to_text(m.group(2))
            if lvl <= 2: h2, h3 = t, ''
            else: h3 = t
        else:
            buf.append(line)
    if buf: out.append((h2, h3, '\n'.join(buf)))
    return out

def bold_bullets(text):
    """'- **Rule.** explanation' -> [(rule, expl)]"""
    res = []
    for m in re.finditer(r'^\s*[-*]\s+\*\*(.+?)\*\*\s*(.*)$', text, flags=re.M):
        res.append((md_to_text(m.group(1)), md_to_text(m.group(2))))
    return res

SKIP_H = re.compile(r'(nunjucks|html|code|example|research on this|next steps|help improve|known issues|changelog|related|resources|further reading|props|api|implementation|installation|contribut|discussion|feedback on|options|how to use the|references?|acknowledg|tokens|figma|react|sketch|storybook|live demo)', re.I)

CUR_LIC = 'Original summary written for this knowledge base (free to use); cite the original source'
def C(id, title, author, year, statement, implication='', check='', layer='screen', threshold='', cite='', cat='', sub='', applies='all digital products', sev='major', conf='high', url='', source_set='Curated: laws & principles', level=''):
    return row(id=id, source_set=source_set, source_org=author, author=author, year=str(year), category=cat, subcategory=sub, title=title,
               statement=statement, rationale=implication, audit_check=check, detection_layer=layer, threshold=threshold, applies_to=applies,
               level=level, severity_default=sev, citation=cite, url=url, text_origin='paraphrased (curated)', license=CUR_LIC, confidence=conf)
