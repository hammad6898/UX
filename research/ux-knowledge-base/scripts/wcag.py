from common import *
base = SRC + '/wcag'
idx = BeautifulSoup(open(base + '/guidelines/index.html').read(), 'lxml')
LIC = 'W3C Document License (copy with attribution)'
# rough automation mapping (axe-core / Lighthouse coverage)
AUTO = {'1.1.1','1.3.1','1.3.5','1.4.3','1.4.4','1.4.6','1.4.11','1.4.12','2.1.1','2.2.1','2.4.1','2.4.2','2.4.4','2.4.7','2.4.11','2.5.3','2.5.8','3.1.1','3.1.2','3.3.2','4.1.2','4.1.3','1.4.10','2.4.6','2.5.5'}
FLOW = {'2.1.2','2.2.2','2.4.3','3.2.1','3.2.2','3.2.3','3.2.4','3.2.6','3.3.1','3.3.3','3.3.4','3.3.7','3.3.8','3.3.9','3.3.6','2.2.5','2.2.6','2.4.5','2.4.8','3.2.5'}
CAT = {'text-alternatives':'Accessibility / Content alternatives','time-based-media':'Accessibility / Media',
 'adaptable':'Accessibility / Structure & semantics','distinguishable':'Accessibility / Visual presentation',
 'keyboard-accessible':'Accessibility / Keyboard','enough-time':'Accessibility / Timing',
 'seizures-and-physical-reactions':'Accessibility / Motion & seizures','navigable':'Accessibility / Navigation & focus',
 'input-modalities':'Accessibility / Pointer & touch input','readable':'Accessibility / Language & readability',
 'predictable':'Accessibility / Predictability','input-assistance':'Accessibility / Forms & errors','compatible':'Accessibility / Robust markup'}
rows=[]; terms_used=set()
for p in idx.select('section.principle'):
    pname = soup_text(p.find('h2'))
    for g in p.select('section.guideline'):
        gid = g.get('id'); gname = soup_text(g.find('h3'))
        gnum = None
        for inc in g.select('section[data-include]'):
            path = inc['data-include']  # sc/20/x.html
            ver = path.split('/')[1]; slug = path.split('/')[-1][:-5]
            sc = BeautifulSoup(open(base + '/guidelines/' + path).read(), 'lxml')
            sec = sc.find('section')
            title = soup_text(sec.find('h4'))
            lvl = soup_text(sec.find(class_='conformance-level'))
            for x in sec.find_all(['h4']): x.decompose()
            for x in sec.find_all(class_=['conformance-level','change']): x.decompose()
            notes = [soup_text(n) for n in sec.find_all(class_='note')]
            for n in sec.find_all(class_='note'): n.decompose()
            text = soup_text(sec)
            rows.append(dict(slug=slug, ver=ver, title=title, level=lvl, text=text, notes=notes, principle=pname, guideline=gname, gid=gid))
# number them
pn=0; out=[]
cur_p=cur_g=None; gn=0; sn=0
for r in rows:
    if r['principle']!=cur_p: pn+=1; cur_p=r['principle']; gn=0; cur_g=None
    if r['guideline']!=cur_g: gn+=1; cur_g=r['guideline']; sn=0
    sn+=1
    num=f'{pn}.{gn}.{sn}'
    r['num']=num
# understanding
for r in rows:
    up = f"{base}/understanding/{r['ver']}/{r['slug']}.html"
    brief=intent=benefits=''
    if os.path.exists(up):
        u = BeautifulSoup(open(up).read(), 'lxml')
        b = u.find('section', id='brief')
        if b:
            dd = [soup_text(d) for d in b.find_all('dd')]
            dt = [soup_text(d) for d in b.find_all('dt')]
            brief = ' | '.join(f'{a}: {c}' for a,c in zip(dt,dd))
        it = u.find('section', id='intent')
        if it:
            ps = [soup_text(pp) for pp in it.find_all('p', recursive=False)][:3]
            intent = ' '.join(ps)
        be = u.find('section', id='benefits')
        if be:
            benefits = ' '.join(soup_text(li) for li in be.find_all('li'))[:1500]
    yr = {'20':'2008','21':'2018','22':'2023'}[r['ver']]
    removed = r['slug']=='parsing'
    lvl = r['level'] or ('Obsolete' if removed else '')
    out.append(row(id='wcag22.'+r['num'], source_set='WCAG 2.2', source_org='W3C', author='W3C Accessibility Guidelines Working Group',
        year=yr, category=CAT.get(r['gid'],'Accessibility'), subcategory=f"{r['principle']} > {r['guideline']}",
        title=f"{r['num']} {r['title']}", statement=r['text'] + (' NOTES: ' + ' / '.join(r['notes']) if r['notes'] else ''),
        rationale=(brief + ' || ' if brief else '') + intent + (' || Benefits: ' + benefits if benefits else ''),
        audit_check=f"Does the interface meet WCAG {r['num']} {r['title']} (Level {lvl})?",
        detection_layer=('deterministic (partial) + screen' if r['num'] in AUTO else ('flow' if r['num'] in FLOW else 'screen / manual')),
        applies_to='web, mobile web, native apps (via WCAG2ICT), documents', level=lvl,
        severity_default={'A':'critical','AA':'major','AAA':'minor'}.get(lvl,'n/a'),
        citation=f"W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2, SC {r['num']}. First introduced in WCAG {r['ver'][0]}.{r['ver'][1]} ({yr}).",
        url=f"https://www.w3.org/WAI/WCAG22/Understanding/{r['slug']}", text_origin='verbatim (normative SC text) + verbatim excerpts (Understanding doc)', license=LIC))
write('wcag22_sc', out)
# failures
fr=[]
for fn in sorted(os.listdir(base+'/techniques/failures'), key=lambda x:int(re.sub(r'\D','',x) or 0)):
    if not fn.endswith('.html'): continue
    s = BeautifulSoup(open(base+'/techniques/failures/'+fn).read(),'lxml')
    t = soup_text(s.find('h1')); fid=fn[:-5]
    d = s.find('section', id='description'); desc = ' '.join(soup_text(p) for p in d.find_all('p'))[:1200] if d else ''
    scs = ', '.join(re.findall(r'\d\.\d\.\d+', t))
    fr.append(row(id='wcag.failure.'+fid, source_set='WCAG Techniques: Common Failures', source_org='W3C', author='W3C AG WG', year='2008-2024',
        category='Accessibility / Known failure', subcategory='SC '+scs, title=f'{fid}: {t}', statement=desc, audit_check=f'Check that the page does not exhibit failure {fid}.',
        detection_layer='screen / deterministic (varies)', applies_to='web', level='', severity_default='major',
        citation=f'W3C. Techniques for WCAG 2.2, Failure {fid}.', url=f'https://www.w3.org/WAI/WCAG22/Techniques/failures/{fid}', text_origin='verbatim', license=LIC))
write('wcag_failures', fr)
# all techniques index (non-failure) titles
tr=[]
for tech in ['general','html','aria','css','client-side-script','server-side-script','text','pdf']:
    d=base+'/techniques/'+tech
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.html'): continue
        s = BeautifulSoup(open(d+'/'+fn).read(),'lxml'); t=soup_text(s.find('h1')); tid=fn[:-5]
        de = s.find('section', id='description'); desc=' '.join(soup_text(p) for p in de.find_all('p'))[:800] if de else ''
        tr.append(row(id='wcag.technique.'+tid, source_set='WCAG Techniques: Sufficient/Advisory', source_org='W3C', author='W3C AG WG', year='2008-2024',
          category='Accessibility / Technique', subcategory=tech, title=f'{tid}: {t}', statement=desc, detection_layer='reference', applies_to='web',
          citation=f'W3C. Techniques for WCAG 2.2, {tid}.', url=f'https://www.w3.org/WAI/WCAG22/Techniques/{tech}/{tid}', text_origin='verbatim', license=LIC))
write('wcag_techniques', tr)
