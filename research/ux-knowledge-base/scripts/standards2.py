from common import *
import glob, yaml
# ---- axe-core
rows=[]
for f in sorted(glob.glob(SRC+'/dequelabs_axe-core/lib/rules/*.json')):
    j=json.load(open(f)); tags=j.get('tags',[])
    wc=[t for t in tags if re.match(r'wcag\d{3,4}$',t)]
    scs=', '.join(f"{t[4]}.{t[5]}.{t[6:]}" for t in wc)
    lv=[t for t in tags if re.match(r'wcag2(a|aa|aaa|1a|1aa|2aa|1aaa)$',t)]
    cat=[t[4:] for t in tags if t.startswith('cat.')]
    rows.append(row(id='axe.'+j['id'], source_set='axe-core rules (Deque)', source_org='Deque Systems', author='Deque Systems', year='2015-2026',
        category='Accessibility / Automated check', subcategory=', '.join(cat), title=j['metadata']['help'], statement=j['metadata']['description'],
        rationale='WCAG SC: '+scs if scs else 'Best practice (not a WCAG requirement)' if 'best-practice' in tags else '',
        audit_check="Check: "+j["metadata"]["description"], detection_layer='deterministic (axe-core)',
        applies_to='web', level=' '.join(lv), severity_default={'critical':'critical','serious':'major','moderate':'minor','minor':'minor'}.get(j.get('impact',''),'major'),
        threshold='enabled by default' if j.get('enabled',True) else 'disabled by default (experimental/opt-in)',
        citation=f"Deque Systems. axe-core rule '{j['id']}'. Tags: {', '.join(tags)}", url=f"https://dequeuniversity.com/rules/axe/4.10/{j['id']}",
        text_origin='verbatim (rule metadata)', license='MPL-2.0'))
write('axe_rules', rows)
# ---- Lighthouse
d=json.load(open(SRC+'/GoogleChrome_lighthouse/shared/localization/locales/en-US.json'))
rows=[]
for k in d:
    if not (k.startswith('core/audits/') and k.endswith('| title')): continue
    mod=k.split(' | ')[0]
    if '/accessibility/' in mod: continue
    t=d[k]['message']; desc=d.get(mod+' | description',{}).get('message',''); ft=d.get(mod+' | failureTitle',{}).get('message','')
    aid=mod.split('/')[-1][:-3]; grp=mod.split('/')[2] if mod.count('/')>2 else 'misc'
    cat={'seo':'Findability / SEO','metrics':'Performance','byte-efficiency':'Performance','insights':'Performance','dobetterweb':'Best practices / Trust','agentic':'Agent readiness'}.get(grp,'Performance / Best practices')
    rows.append(row(id='lighthouse.'+aid, source_set='Lighthouse audits (Google)', source_org='Google', author='Google Chrome team', year='2016-2026',
        category=cat, subcategory=grp, title=t, statement=re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', desc), audit_check=(ft or t), detection_layer='deterministic (Lighthouse)',
        applies_to='web', severity_default='major' if grp in ('metrics',) else 'minor', citation=f'Google. Lighthouse audit {aid}.',
        url='https://developer.chrome.com/docs/lighthouse/', text_origin='verbatim (UI strings)', license='Apache-2.0'))
# metric thresholds
for aid,name,good,poor,unit in [('largest-contentful-paint','Largest Contentful Paint (Core Web Vital)',2.5,4.0,'s'),('interaction-to-next-paint','Interaction to Next Paint (Core Web Vital)',200,500,'ms'),('cumulative-layout-shift','Cumulative Layout Shift (Core Web Vital)',0.1,0.25,'score'),('first-contentful-paint','First Contentful Paint',1.8,3.0,'s'),('time-to-first-byte','Time to First Byte',0.8,1.8,'s')]:
    rows.append(row(id='cwv.'+aid, source_set='Core Web Vitals / web.dev thresholds', source_org='Google', author='Google (web.dev)', year='2020-2024',
        category='Performance', subcategory='Core Web Vitals', title=name+' thresholds', statement=f'Good: <= {good}{unit}; Needs improvement: {good}-{poor}{unit}; Poor: > {poor}{unit}, measured at the 75th percentile of page loads (mobile and desktop separately).',
        audit_check=f'Is {name} within the good threshold ({good}{unit}) at p75?', detection_layer='deterministic (field data/CrUX or lab)', threshold=f'good<={good}{unit}; poor>{poor}{unit}',
        applies_to='web', severity_default='major', citation='Google web.dev, "Web Vitals" (2020; INP replaced FID in March 2024).', url='https://web.dev/articles/vitals', text_origin='paraphrased', license='facts (not copyrightable)'))
write('lighthouse_audits', rows)
# ---- ACT rules
rows=[]
for f in sorted(glob.glob(SRC+'/act-rules_act-rules.github.io/_rules/*.md')):
    s=open(f).read(); m=re.match(r'---\n(.*?)\n---\n(.*)',s,re.S)
    if not m: continue
    fm=yaml.safe_load(m.group(1)); body=m.group(2)
    ar=fm.get('accessibility_requirements') or {}
    scs=', '.join(k.split(':')[1] for k in ar if k.startswith('wcag'))
    def sec(name):
        mm=re.search(r'## '+name+r'\n(.*?)(\n## |\Z)',body,re.S); return md_to_text(mm.group(1))[:1200] if mm else ''
    rows.append(row(id='act.'+str(fm['id']), source_set='W3C ACT Rules (Accessibility Conformance Testing)', source_org='W3C / ACT Rules Community Group', author=', '.join((fm.get('acknowledgments') or {}).get('authors',[]) or []), year='2017-2026',
        category='Accessibility / Test rule', subcategory=fm.get('rule_type',''), title=fm['name'], statement=md_to_text(fm.get('description','')),
        rationale=sec('Background')[:800], audit_check='Applicability: '+sec('Applicability')+' Expectation: '+sec('Expectation'),
        detection_layer='deterministic' if 'DOM Tree' in str(fm.get('input_aspects')) and fm.get('rule_type')=='atomic' else 'semi-automated / manual',
        applies_to='web', level='', severity_default='major', rationale_extra='' if False else None, citation=f"ACT Rules CG. Rule {fm['id']}: {fm['name']}. Maps to WCAG {scs}.",
        url=f"https://www.w3.org/WAI/standards-guidelines/act/rules/{fm['id']}/", text_origin='verbatim', license='W3C Document License / CLA') if False else row(id='act.'+str(fm['id']), source_set='W3C ACT Rules (Accessibility Conformance Testing)', source_org='W3C / ACT Rules Community Group', author=', '.join((fm.get('acknowledgments') or {}).get('authors',[]) or []), year='2017-2026',
        category='Accessibility / Test rule', subcategory=fm.get('rule_type',''), title=fm['name'], statement=md_to_text(fm.get('description','')),
        rationale=sec('Background')[:800], audit_check='Applicability: '+sec('Applicability')+' Expectation: '+sec('Expectation'),
        detection_layer='deterministic' if fm.get('rule_type')=='atomic' else 'semi-automated / manual', applies_to='web', severity_default='major',
        citation=f"ACT Rules CG. Rule {fm['id']}: {fm['name']}. Maps to WCAG {scs}.", url=f"https://www.w3.org/WAI/standards-guidelines/act/rules/{fm['id']}/", text_origin='verbatim', license='W3C Document License'))
write('act_rules', rows)
# ---- ARIA APG patterns
rows=[]
for d_ in sorted(glob.glob(SRC+'/w3c_aria-practices/content/patterns/*/')):
    name=os.path.basename(d_.rstrip('/')); f=glob.glob(d_+'*-pattern.html')
    if not f: continue
    s=BeautifulSoup(open(f[0]).read(),'lxml'); title=soup_text(s.find('h1')) or name
    about=s.find('section',id='about'); ab=' '.join(soup_text(p) for p in about.find_all('p'))[:1000] if about else ''
    kb=s.find('section',id='keyboard_interaction'); kbt=' '.join(soup_text(li) for li in kb.find_all('li'))[:1500] if kb else ''
    rr=s.find('section',id='roles_states_properties'); rrt=' '.join(soup_text(li) for li in rr.find_all('li'))[:1500] if rr else ''
    rows.append(row(id='apg.'+name, source_set='WAI-ARIA Authoring Practices Guide (APG) patterns', source_org='W3C', author='W3C ARIA Authoring Practices Task Force', year='2008-2026',
        category='Components / Accessible patterns', subcategory=name, title=title, statement=ab, rationale='Roles/states/properties: '+rrt,
        audit_check='Keyboard interaction expected: '+kbt, detection_layer='flow (keyboard walkthrough) + deterministic (ARIA)', applies_to='web components',
        severity_default='major', citation=f'W3C. ARIA Authoring Practices Guide, {title}.', url=f'https://www.w3.org/WAI/ARIA/apg/patterns/{name}/', text_origin='verbatim excerpts', license='W3C Software and Document License'))
write('aria_apg_patterns', rows)
# ---- COGA patterns
rows=[]
for f in sorted(glob.glob(SRC+'/w3c_coga/design-guide/o*p*.html')):
    s=BeautifulSoup(open(f).read(),'lxml'); h=s.find('h3'); title=soup_text(h).replace('(Pattern)','').strip()
    pre=s.find('pre'); 
    if pre: pre.decompose()
    secs={soup_text(x.find('h5')):x for x in s.find_all('section') if x.find('h5')}
    def g(k): 
        x=secs.get(k); 
        if not x: return ''
        x=BeautifulSoup(str(x),'lxml'); x.find('h5').decompose(); return soup_text(x)
    base=os.path.basename(f)[:-5]; obj=base.split('p')[0]
    rows.append(row(id='coga.'+base, source_set='W3C Making Content Usable for People with Cognitive and Learning Disabilities (COGA)', source_org='W3C', author='W3C COGA Task Force', year='2021',
        category='Cognitive accessibility', subcategory='Objective '+obj[1:], title=title, statement=g('What to Do')[:1500], rationale=(g('User Need')+' || '+g('How it Helps'))[:1500],
        audit_check='User need: '+g('User Need'), detection_layer='screen / flow', applies_to='web, apps', severity_default='major',
        citation=f'W3C (2021). Making Content Usable for People with Cognitive and Learning Disabilities, pattern "{title}".', url='https://www.w3.org/TR/coga-usable/', text_origin='verbatim excerpts', license='W3C Document License'))
write('coga_patterns', rows)
# ---- WCAG 3 draft requirements
rows=[]
gp=SRC+'/w3c_wcag3/guidelines/groups'
for gj in sorted(glob.glob(gp+'/*.json')):
    group=os.path.basename(gj)[:-5]
    for gl in json.load(open(gj)).get('children',[]):
        gmd=f'{gp}/{group}/{gl}.md'
        if not os.path.exists(gmd): continue
        gs=open(gmd).read(); gtext=md_to_text(re.sub(r'^---.*?---','',gs,flags=re.S))
        for rq in sorted(glob.glob(f'{gp}/{group}/{gl}/*.md')):
            rs=open(rq).read(); fm=re.match(r'---\n(.*?)\n---',rs,re.S); fmd=yaml.safe_load(fm.group(1)) if fm else {}
            body=re.sub(r'^---.*?---','',rs,flags=re.S); body=re.sub(r':term\[([^\]]+)\]',r'\1',body); body=re.sub(r':::[a-z-]*','',body)
            rows.append(row(id='wcag3.'+group+'.'+gl+'.'+os.path.basename(rq)[:-3], source_set='WCAG 3.0 (Working Draft)', source_org='W3C', author='W3C AG WG', year='2021-2026 (draft)',
                category='Accessibility / WCAG 3 draft', subcategory=f'{group} > {gl}', title=os.path.basename(rq)[:-3].replace('-',' ').capitalize(), statement=md_to_text(body)[:1500],
                rationale='Guideline: '+gtext, audit_check='Requirement status: '+str(fmd.get('status',''))+'; type: '+str(fmd.get('type','')), detection_layer='screen / manual',
                applies_to='web, apps, documents', level=str(fmd.get('type','')), severity_default='minor (draft, non-normative)', citation='W3C. WCAG 3.0 Editor\'s Draft, '+group+'.',
                url='https://w3c.github.io/wcag3/guidelines/', text_origin='verbatim (draft)', license='W3C Document License'))
write('wcag3_draft', rows)
