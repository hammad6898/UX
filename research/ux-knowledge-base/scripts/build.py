"""Assemble all extracted/curated JSONL files into the knowledge-base deliverables."""
from common import *
import csv, glob, collections, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

DEST = os.environ.get('KB_DEST', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
os.makedirs(DEST + '/data', exist_ok=True)

def load(name):
    p = os.path.join(OUT, name + '.jsonl')
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

CODEY = re.compile(r'(=>|className=|\bimport\s+\{|useState|useEffect|\bfunction\s*\(|\bconst\s+\w+\s*=|\bprops\.)')
META = re.compile(r'(component lifecycle|contribut|release notes|migrat|deprecat|changelog|versioning|figma kit|storybook|status of component|token names)', re.I)
FILTERED = {'govuk_design_system','nhs_service_manual','uswds','carbon','polaris','primer','18f_content_guide','18f_ux_guide','18f_accessibility','plain_language','digitalgov_guides'}
def keep(r, name=''):
    st = r.get('statement', '')
    if r.get('text_origin', '').startswith('paraphrased'): return True
    if name not in FILTERED: return len(st) > 0 or len(r.get('title','')) > 0
    if len(st) < 30: return False
    if META.search(r.get('subcategory','')) or META.search(r.get('title','')): return False
    if CODEY.search(st) or st.count('{') > 2: return False
    return True

# source groups -> (sheet, layer label, repo/source url)
GROUPS = [
 ('curated_rules', 'Audit_Rules', 'Curated knowledge', 'Written for this KB from cited research'),
 ('curated_heuristics', 'Heuristics', 'Curated knowledge', 'Written for this KB from cited sources'),
 ('curated_laws', 'Laws_Principles', 'Curated knowledge', 'Written for this KB from cited sources'),
 ('curated_biases', 'Biases_Behavior', 'Curated knowledge', 'Written for this KB from cited sources'),
 ('curated_dark_patterns', 'Deceptive_Patterns', 'Curated knowledge', 'Written for this KB from cited sources'),
 ('curated_metrics_methods', 'Metrics_Methods', 'Curated knowledge', 'Written for this KB from cited sources'),
 ('wcag22_sc', 'WCAG22_SC', 'Standard (normative)', 'https://github.com/w3c/wcag'),
 ('wcag_failures', 'WCAG_Failures', 'Standard (informative)', 'https://github.com/w3c/wcag'),
 ('wcag_techniques', 'WCAG_Techniques', 'Standard (informative)', 'https://github.com/w3c/wcag'),
 ('wcag3_draft', 'WCAG3_Draft', 'Standard (draft)', 'https://github.com/w3c/wcag3'),
 ('act_rules', 'ACT_Rules', 'Automated/semi-automated test rules', 'https://github.com/act-rules/act-rules.github.io'),
 ('aria_apg_patterns', 'ARIA_Patterns', 'Standard (informative)', 'https://github.com/w3c/aria-practices'),
 ('coga_patterns', 'COGA_Patterns', 'Standard (informative)', 'https://github.com/w3c/coga'),
 ('axe_rules', 'Axe_Rules', 'Automated checks', 'https://github.com/dequelabs/axe-core'),
 ('lighthouse_audits', 'Lighthouse', 'Automated checks', 'https://github.com/GoogleChrome/lighthouse'),
 ('a11yproject_checklist', 'Checklists', 'Practitioner checklist', 'https://github.com/a11yproject/a11yproject.com'),
 ('frontend_checklist', 'Checklists', 'Practitioner checklist', 'https://github.com/thedaviddias/Front-End-Checklist'),
 ('govuk_design_system', 'DesignSystems', 'Design system guidance', 'https://github.com/alphagov/govuk-design-system'),
 ('nhs_service_manual', 'DesignSystems', 'Design system guidance', 'https://github.com/nhsuk/nhsuk-service-manual'),
 ('uswds', 'DesignSystems', 'Design system guidance', 'https://github.com/uswds/uswds-site'),
 ('carbon', 'DesignSystems', 'Design system guidance', 'https://github.com/carbon-design-system/carbon-website'),
 ('polaris', 'DesignSystems', 'Design system guidance', 'https://github.com/Shopify/polaris'),
 ('primer', 'DesignSystems', 'Design system guidance', 'https://github.com/primer/design'),
 ('18f_content_guide', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/18F/content-guide'),
 ('18f_ux_guide', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/18F/ux-guide'),
 ('18f_accessibility', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/18F/accessibility'),
 ('plain_language', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/GSA/plainlanguage.gov'),
 ('digitalgov_guides', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/GSA/digitalgov.gov'),
 ('usds_playbook', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/usds/playbook'),
 ('18f_methods', 'Gov_Content_Service', 'Government content & service guidance', 'https://github.com/18F/methods'),
]
FIELDS2 = ['kb_layer'] + FIELDS
sheets = collections.OrderedDict(); master = []; src_stats = []
for name, sheet, layer, origin in GROUPS:
    rows = [r for r in load(name) if keep(r, name)]
    seen = set(); clean_rows = []
    for r in rows:
        k = (r['title'], r['statement'][:200])
        if k in seen: continue
        seen.add(k); r = {**{f: '' for f in FIELDS}, **r}; r['kb_layer'] = layer; clean_rows.append(r)
    # split thresholds out of metrics sheet
    if name == 'curated_metrics_methods':
        th = [r for r in clean_rows if r['source_set'] == 'Curated: numeric thresholds']
        clean_rows = [r for r in clean_rows if r['source_set'] != 'Curated: numeric thresholds']
        sheets.setdefault('Thresholds', []).extend(th); master.extend(th)
        src_stats.append(('Curated: numeric thresholds', 'Curated knowledge', len(th), CUR_LIC, origin))
    sheets.setdefault(sheet, []).extend(clean_rows); master.extend(clean_rows)
    by_set = collections.Counter(r['source_set'] for r in clean_rows)
    for s, n in by_set.items():
        lic = next(r['license'] for r in clean_rows if r['source_set'] == s)
        src_stats.append((s, layer, n, lic, origin))
    with open(f'{DEST}/data/{name}.jsonl', 'w') as f:
        for r in clean_rows + (th if name == 'curated_metrics_methods' else []):
            f.write(json.dumps({k: r[k] for k in FIELDS2}, ensure_ascii=False) + '\n')

# extra tables
sets_index = load('heuristic_sets_index'); bib = load('bibliography'); dpi = load('dark_pattern_instances')
for nm, data in [('heuristic_sets_index', sets_index), ('bibliography', bib), ('dark_pattern_instances', dpi)]:
    with open(f'{DEST}/data/{nm}.jsonl', 'w') as f:
        for r in data: f.write(json.dumps(r, ensure_ascii=False) + '\n')

# master files
with open(f'{DEST}/data/ALL_RULES.jsonl', 'w') as f:
    for r in master: f.write(json.dumps({k: r[k] for k in FIELDS2}, ensure_ascii=False) + '\n')
with open(f'{DEST}/ALL_RULES.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS2); w.writeheader()
    for r in master: w.writerow({k: r[k] for k in FIELDS2})

# timeline by decade from bibliography + curated years
dec = collections.defaultdict(list)
for b in bib: dec[b['decade']].append(f"{b['year']} {b['authors'].split(',')[0]}: {b['title']}")
timeline = [{'decade': d, 'works_in_bibliography': len(v), 'highlights': ' | '.join(v[:12])} for d, v in sorted(dec.items())]

# ---------------- workbook ----------------
wb = Workbook(); ws0 = wb.active; ws0.title = 'README'
HDR = Font(bold=True, color='FFFFFF'); FILL = PatternFill('solid', fgColor='1F3A5F')
WIDTH = {'id': 24, 'kb_layer': 18, 'source_set': 28, 'source_org': 18, 'author': 22, 'year': 10, 'category': 22, 'subcategory': 28, 'title': 44,
         'statement': 80, 'rationale': 60, 'audit_check': 60, 'detection_layer': 22, 'threshold': 26, 'applies_to': 18, 'level': 10,
         'severity_default': 12, 'citation': 60, 'url': 40, 'text_origin': 18, 'license': 24, 'confidence': 11}
def sanitize(v):
    if v is None: return ''
    if isinstance(v, (int, float)): return v
    return ILLEGAL_CHARACTERS_RE.sub('', str(v))[:32000]
def add_sheet(title, rows, cols, wrap=False):
    ws = wb.create_sheet(title)
    ws.append(cols)
    for c in ws[1]: c.font = HDR; c.fill = FILL; c.alignment = Alignment(vertical='top', wrap_text=True)
    for r in rows: ws.append([sanitize(r.get(c, '')) for c in cols])
    for i, c in enumerate(cols, 1): ws.column_dimensions[get_column_letter(i)].width = WIDTH.get(c, 22)
    ws.freeze_panes = 'C2' if len(cols) > 3 else 'A2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(cols))}{len(rows)+1}'
    if wrap:
        for row in ws.iter_rows(min_row=2):
            for c in row: c.alignment = Alignment(vertical='top', wrap_text=True)
    return ws
ORDER = ['Audit_Rules', 'Heuristics', 'Laws_Principles', 'Biases_Behavior', 'Deceptive_Patterns', 'Metrics_Methods', 'Thresholds',
         'WCAG22_SC', 'WCAG_Failures', 'WCAG_Techniques', 'WCAG3_Draft', 'ACT_Rules', 'ARIA_Patterns', 'COGA_Patterns', 'Axe_Rules', 'Lighthouse',
         'Checklists', 'DesignSystems', 'Gov_Content_Service']
for s in ORDER:
    rows = sheets.get(s, [])
    add_sheet(s, rows, FIELDS2, wrap=s in ('Audit_Rules', 'Heuristics', 'Laws_Principles', 'Biases_Behavior', 'Deceptive_Patterns', 'Metrics_Methods', 'Thresholds'))
    if s == 'Heuristics':
        add_sheet('Heuristic_Sets', sets_index, ['set_id', 'name', 'author', 'year', 'items', 'domain', 'citation', 'url', 'confidence', 'note'], wrap=True)
    if s == 'Deceptive_Patterns':
        add_sheet('DP_Instances', dpi, ['id', 'dataset', 'pattern_category', 'pattern_type', 'text', 'where', 'deceptive', 'comment', 'page_url', 'label', 'license'])
add_sheet('Bibliography', sorted(bib, key=lambda b: (b['year'], b['authors'])), ['id', 'year', 'decade', 'authors', 'title', 'venue', 'type', 'topic', 'key_contribution', 'citation', 'find_url', 'confidence'], wrap=True)
add_sheet('Timeline', timeline, ['decade', 'works_in_bibliography', 'highlights'], wrap=True)
srcrows = [{'source_set': s, 'kb_layer': l, 'rows': n, 'license': lic, 'obtained_from': o} for s, l, n, lic, o in src_stats]
srcrows += [{'source_set': 'Heuristic set index', 'kb_layer': 'Curated knowledge', 'rows': len(sets_index), 'license': CUR_LIC, 'obtained_from': 'Curated'},
            {'source_set': 'Bibliography 1908–2025', 'kb_layer': 'Curated knowledge', 'rows': len(bib), 'license': 'Citations (facts)', 'obtained_from': 'Curated'},
            {'source_set': 'Dark pattern instances (Mathur et al. 2019; Yada et al. 2022)', 'kb_layer': 'Research dataset', 'rows': len(dpi), 'license': 'GPL-3.0 (Mathur) / Apache-2.0 (Yada repo)', 'obtained_from': 'https://github.com/aruneshmathur/dark-patterns ; https://github.com/yamanalab/ec-darkpattern'}]
add_sheet('Sources_Licenses', srcrows, ['source_set', 'kb_layer', 'rows', 'license', 'obtained_from'], wrap=True)

# README sheet
total = len(master)
lines = [
 ['UX Knowledge Base for auditing (research compiled ' + datetime.date.today().isoformat() + ')'], [''],
 ['What this is', 'A structured, cited knowledge base of UX heuristics, laws, standards, guidelines, biases, deceptive patterns, metrics, thresholds, methods and seminal literature (1908–2025), built to train and ground a UX audit product.'],
 ['Rows (rules/guidelines)', total], ['Heuristic sets', len(sets_index)], ['Bibliography entries', len(bib)], ['Dark-pattern instances', len(dpi)], [''],
 ['How to use', 'Start with Audit_Rules (product-ready rules with checks, layer and severity). Use Heuristics/Laws/Biases/Deceptive_Patterns for reasoning and citations; WCAG/ACT/axe/Lighthouse for deterministic checks; DesignSystems/Gov_Content_Service for component-level guidance; Thresholds for numeric limits.'],
 ['Columns', 'kb_layer, id, source_set, source_org, author, year, category, subcategory, title, statement, rationale, audit_check, detection_layer (deterministic / screen / flow / organizational), threshold, applies_to, level, severity_default, citation, url, text_origin (verbatim vs paraphrased), license, confidence'],
 ['detection_layer', 'Matches docs/ARCHITECTURE.md: deterministic = DOM/axe/Lighthouse rules; screen = vision + accessibility tree on one screen; flow = reasoning over a multi-step journey; organizational/research = process advice, not detectable on screen.'],
 ['severity_default', 'Suggested starting severity (critical / major / minor / n/a). Calibrate against your eval set.'],
 ['text_origin & license', 'Verbatim text comes only from openly licensed or public-domain sources (W3C, US Gov CC0, UK OGL, MIT/Apache/MPL repos). Everything else is paraphrased with citations. Check the license column before redistributing; dark-pattern instances from Mathur et al. are GPL-3.0.'],
 ['confidence', 'high = well-established and/or checked; medium = from memory of the source or secondary confirmation; verify before quoting exactly.'],
 ['Files', 'ALL_RULES.csv and data/*.jsonl contain the same rows as this workbook for programmatic use. See README.md for sources, gaps and how to regenerate.'],
]
for l in lines: ws0.append(l)
ws0['A1'].font = Font(bold=True, size=14); ws0.column_dimensions['A'].width = 26; ws0.column_dimensions['B'].width = 140
for row in ws0.iter_rows(min_row=3):
    row[0].font = Font(bold=True)
    for c in row: c.alignment = Alignment(wrap_text=True, vertical='top')
wb.save(f'{DEST}/UX_Knowledge_Base.xlsx')
print('master rows', total)
for s in ORDER: print(f'  {s}: {len(sheets.get(s, []))}')
json.dump({'generated': datetime.date.today().isoformat(), 'rows': total, 'sheets': {s: len(sheets.get(s, [])) for s in ORDER},
           'sources': srcrows}, open(f'{DEST}/data/manifest.json', 'w'), indent=1, ensure_ascii=False)
