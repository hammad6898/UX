from common import *
import glob, yaml, csv
S=SRC
# ---- NHS service manual (njk -> html sections)
def html_sections(h):
    h=re.sub(r'\{%.*?%\}','',h,flags=re.S); h=re.sub(r'\{\{.*?\}\}','',h,flags=re.S); h=re.sub(r'\{#.*?#\}','',h,flags=re.S)
    s=BeautifulSoup(h,'lxml'); out=[]; h2=h3=''; buf=[]
    for el in s.find_all(['h2','h3','p','li','td']):
        if el.name in ('h2','h3'):
            if buf: out.append((h2,h3,' '.join(buf))); buf=[]
            t=soup_text(el); t=re.sub(r'^\d+\s+','',t)
            if el.name=='h2': h2,h3=t,''
            else: h3=t
        elif el.name in ('p','td') or (el.name=='li' and not el.find('p')):
            buf.append(soup_text(el))
    if buf: out.append((h2,h3,' '.join(buf)))
    return out
n=S+'/nhsuk_nhsuk-service-manual/app/views'
files=sorted(set(glob.glob(n+'/design-system/components/*/index.njk')+glob.glob(n+'/design-system/patterns/*/index.njk')+glob.glob(n+'/design-system/patterns/*.njk')+glob.glob(n+'/design-system/styles/**/*.njk',recursive=True)+glob.glob(n+'/design-system/design-principles.njk')+glob.glob(n+'/content/**/*.njk',recursive=True)+glob.glob(n+'/accessibility/*.njk')))
rows=[]
for f in files:
    if '/_' in f or 'partials' in f: continue
    raw=open(f).read(); m=re.search(r'set pageTitle = "([^"]+)"',raw); doc=m.group(1) if m else os.path.basename(f)
    for h2,h3,t in html_sections(raw):
        if len(t)<60 or SKIP_H.search(h2+' '+h3): continue
        title=h3 or h2 or doc
        rows.append(row(id=f'nhs.{len(rows)+1:04d}', source_set='NHS digital service manual', source_org='NHS England', author='NHS England', year='2018-2026',
            category=categorize(doc,h2,h3), subcategory=' > '.join(x for x in [doc,h2,h3] if x), title=f'{doc}: {title}' if title!=doc else doc, statement=t[:2500],
            detection_layer='screen / flow (guideline)', applies_to='web, health services', severity_default='minor', citation=f'NHS England. NHS digital service manual, "{doc}".',
            url='https://service-manual.nhs.uk/'+f.split('/views/')[1].replace('/index.njk','').replace('.njk',''), text_origin='verbatim (section text)', license='Open Government Licence v3.0'))
write('nhs_service_manual', rows)
# ---- US Digital Services Playbook
rows=[]
for f in sorted(glob.glob(S+'/usds_playbook/_plays/*.md')):
    raw=open(f).read(); fm=yaml.safe_load(re.match(r'---\n(.*?)\n---',raw,re.S).group(1)); body=raw.split('---',2)[2]
    intro=md_to_text(body.split('###')[0]); n_=fm['play_number']
    rows.append(row(id=f'usds.play{n_:02d}', source_set='U.S. Digital Services Playbook (13 plays)', source_org='U.S. Digital Service', author='U.S. Digital Service', year='2014',
        category='Research & process' if n_ in (1,2,3,4) else 'Product & service delivery', subcategory='Play', title=f"Play {n_}: {fm['title']}", statement=intro,
        detection_layer='organizational / research', applies_to='digital services', severity_default='n/a', citation=f"U.S. Digital Service (2014). Digital Services Playbook, Play {n_}.", url='https://playbook.usds.gov/', text_origin='verbatim', license='Public domain (US Gov)'))
    for sec in ('Checklist','Key Questions'):
        mm=re.search(r'### '+sec+r'\n(.*?)(\n### |\Z)',body,re.S)
        if not mm: continue
        for i,item in enumerate(re.findall(r'^\s*(?:\d+\.|-)\s+(.*)$',mm.group(1),re.M)):
            rows.append(row(id=f'usds.play{n_:02d}.{sec[:3].lower()}{i+1:02d}', source_set='U.S. Digital Services Playbook (13 plays)', source_org='U.S. Digital Service', author='U.S. Digital Service', year='2014',
              category=categorize(item, default='Product & service delivery'), subcategory=f"Play {n_}: {fm['title']} > {sec}", title=md_to_text(item)[:140], statement=md_to_text(item),
              audit_check=md_to_text(item) if sec=='Key Questions' else '', detection_layer='organizational / research', applies_to='digital services', severity_default='n/a',
              citation=f"U.S. Digital Service (2014). Digital Services Playbook, Play {n_} {sec}.", url='https://playbook.usds.gov/', text_origin='verbatim', license='Public domain (US Gov)'))
write('usds_playbook', rows)
# ---- A11Y Project checklist
d=json.load(open(S+'/a11yproject_a11yproject.com/src/_data/checklists.json')); rows=[]
for sec,v in d.items():
    for t in v.get('tasks',[]):
        rows.append(row(id='a11yproject.'+t.get('checkboxId',str(len(rows))), source_set='The A11Y Project Checklist', source_org='The A11Y Project', author='The A11Y Project contributors', year='2013-2026',
          category='Accessibility', subcategory=sec, title=clean(BeautifulSoup(t['title'],'lxml').get_text()), statement=clean(BeautifulSoup(t.get('description',''),'lxml').get_text()),
          rationale='WCAG '+t.get('wcag',''), audit_check=clean(BeautifulSoup(t['title'],'lxml').get_text()), detection_layer='deterministic / screen', applies_to='web', severity_default='major',
          citation='The A11Y Project. Checklist.', url='https://www.a11yproject.com/checklist/', text_origin='verbatim', license='Apache-2.0'))
write('a11yproject_checklist', rows)
# ---- Front-End Checklist rules
rows=[]
for f in sorted(glob.glob(S+'/thedaviddias_Front-End-Checklist/packages/content/rules/en/**/*.mdx',recursive=True)):
    raw=open(f).read(); m=re.match(r'---\n(.*?)\n---',raw,re.S)
    if not m: continue
    try: fm=yaml.safe_load(m.group(1))
    except Exception: continue
    grp=f.split('/rules/en/')[1].split('/')[0]
    rows.append(row(id='fec.'+grp+'.'+os.path.basename(f)[:-4], source_set='Front-End Checklist (rules)', source_org='David Dias & contributors', author='David Dias', year='2016-2026',
        category={'accessibility':'Accessibility','performance':'Performance','seo':'Findability / SEO','security':'Authentication, security & privacy','privacy':'Authentication, security & privacy','i18n':'Internationalization','images':'Performance','css':'Visual design & layout'}.get(grp,'Technical quality'),
        subcategory=grp+' / '+str(fm.get('subcategory','')), title=fm.get('title',''), statement=(fm.get('description') or '')+' TL;DR: '+' / '.join(map(str,fm.get('tldr') or [])),
        rationale=fm.get('whyItMatters',''), audit_check=((fm.get('prompts') or {}).get('check') or ''), detection_layer='deterministic / code review', applies_to='web',
        severity_default={'high':'major','medium':'minor','low':'minor'}.get(str(fm.get('priority','')),'minor'), threshold='priority: '+str(fm.get('priority','')),
        citation='Dias, D. Front-End Checklist, rule "'+str(fm.get('title',''))+'".', url='https://frontendchecklist.io/', text_origin='verbatim', license='MIT'))
write('frontend_checklist', rows)
# ---- 18F methods (research & design methods)
rows=[]
for f in sorted(glob.glob(S+'/18F_methods/_methods/*.md')):
    raw=open(f).read(); m=re.match(r'---\n(.*?)\n---',raw,re.S)
    try: fm=yaml.safe_load(m.group(1))
    except Exception: continue
    if not fm or '[' in str(fm.get('title','[')): continue
    body=md_to_text(raw.split('---',2)[2])
    rows.append(row(id='18f.method.'+os.path.basename(f)[:-3], source_set='18F Methods', source_org='18F (GSA)', author='18F', year='2015-2024', category='Research & process',
        subcategory=str(fm.get('category','')), title=fm.get('title',''), statement='What: '+str(fm.get('what',''))+' Why: '+str(fm.get('why','')), rationale=body[:2000],
        threshold='time: '+str(fm.get('timeRequired','')), detection_layer='method', applies_to='research & design process', citation='18F. Methods: '+str(fm.get('title','')), url='https://methods.18f.gov/', text_origin='verbatim', license='Public domain (US Gov) / CC0'))
write('18f_methods', rows)
# ---- dark pattern instances
rows=[]
with open(S+'/aruneshmathur_dark-patterns/data/final-dark-patterns/dark-patterns.csv',newline='',encoding='utf-8',errors='ignore') as fh:
    for i,r in enumerate(csv.DictReader(fh)):
        rows.append({'id':f'mathur2019.{i+1:04d}','dataset':'Mathur et al. 2019 (Princeton) — 11K shopping websites crawl','pattern_category':r.get('Pattern Category',''),'pattern_type':r.get('Pattern Type',''),
          'text':clean(r.get('Pattern String','')),'where':r.get('Where in website?',''),'deceptive':r.get('Deceptive?',''),'comment':r.get('Comment',''),'page_url':r.get('Website Page',''),
          'label':'dark pattern','license':'GPL-3.0 (dataset); cite Mathur et al., CSCW 2019'})
with open(S+'/yamanalab_ec-darkpattern/dataset/dataset.tsv',newline='',encoding='utf-8',errors='ignore') as fh:
    for i,r in enumerate(csv.DictReader(fh,delimiter='\t')):
        rows.append({'id':f'yada2022.{i+1:04d}','dataset':'Yada et al. 2022 ec-darkpattern (text classification; positives from Mathur et al. + negatives)','pattern_category':r.get('Pattern Category',''),'pattern_type':'',
          'text':clean(r.get('text','')),'where':'','deceptive':'','comment':'','page_url':'','label':'dark pattern' if r.get('label')=='1' else 'not dark pattern','license':'Apache-2.0 (repo); underlying positives from Mathur et al. (GPL-3.0)'})
os.makedirs(OUT,exist_ok=True)
with open(OUT+'/dark_pattern_instances.jsonl','w') as fo:
    for r in rows: fo.write(json.dumps(r,ensure_ascii=False)+'\n')
print('dark_pattern_instances',len(rows))
