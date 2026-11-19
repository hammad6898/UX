from common import *
import glob, yaml
def md_rows(files, set_name, org, year, lic, url_fn, prefix, applies='web, apps', min_len=60, title_fn=None):
    rows=[]
    for f in files:
        raw=open(f, errors='ignore').read()
        fm=re.match(r'^---\n(.*?)\n---\n', raw, re.S); meta={}
        if fm:
            try: meta=yaml.safe_load(fm.group(1)) or {}
            except Exception: meta={}
        doc=(meta.get('title') if isinstance(meta,dict) else None) or (title_fn(f) if title_fn else os.path.basename(f).rsplit('.',1)[0])
        doc=md_to_text(str(doc))
        for h2,h3,text in split_md_sections(raw):
            if SKIP_H.search(h2 or '') or SKIP_H.search(h3 or ''): continue
            bb=bold_bullets(text)
            if len(bb)>=2:
                for rule,expl in bb:
                    st=(rule+' '+expl).strip()
                    if len(st)<25: continue
                    rows.append((doc,h2,h3,rule,st,f))
            else:
                t=md_to_text(text)
                if len(t)<min_len: continue
                rows.append((doc,h2,h3,h3 or h2 or doc,t,f))
    out=[]; seen=set()
    for i,(doc,h2,h3,title,st,f) in enumerate(rows):
        key=(doc,title,st[:80])
        if key in seen: continue
        seen.add(key)
        sub=' > '.join(x for x in [doc,h2,h3] if x)
        out.append(row(id=f'{prefix}.{len(out)+1:04d}', source_set=set_name, source_org=org, author=org, year=year,
            category=categorize(doc,h2,h3,title), subcategory=sub, title=f'{doc}: {title}' if title!=doc else doc, statement=st[:2500],
            audit_check='', detection_layer='screen / flow (guideline)', applies_to=applies, severity_default='minor',
            citation=f'{org}. {set_name}: "{doc}" ({h2}{" > "+h3 if h3 else ""}).', url=url_fn(f), text_origin='verbatim (section text)', license=lic))
    return out
S=SRC
# GOV.UK Design System
g=S+'/alphagov_govuk-design-system/src'
files=sorted(glob.glob(g+'/components/*/index.md')+glob.glob(g+'/patterns/*/index.md')+glob.glob(g+'/styles/*/index.md')+glob.glob(g+'/accessibility/*.md')+glob.glob(g+'/accessibility/*/index.md'))
rel=lambda f: 'https://design-system.service.gov.uk/'+f.split('/src/')[1].replace('index.md','')
write('govuk_design_system', md_rows(files,'GOV.UK Design System','Government Digital Service (UK)','2018-2026','MIT (code) / Open Government Licence v3.0 (content)',rel,'govuk'))
# USWDS
u=S+'/uswds_uswds-site'
files=sorted(glob.glob(u+'/_components/*/guidance/*.md')+glob.glob(u+'/_patterns/**/*.md',recursive=True)+glob.glob(u+'/pages/design-principles/*.md'))
def uswds_title(f):
    parts=f.split('/'); 
    if 'guidance' in parts: return parts[parts.index('guidance')-1].replace('-',' ').title()+' — '+parts[-1][:-3].replace('-',' ')
    return parts[-1][:-3].replace('-',' ').title()
rows=[]
for f in files:
    raw=open(f).read(); bb=bold_bullets(raw); t=uswds_title(f)
    if bb:
        for rule,expl in bb: rows.append((t,rule,(rule+' '+expl).strip(),f))
    else:
        for h2,h3,text in split_md_sections(raw):
            tx=md_to_text(text)
            if len(tx)>60 and not SKIP_H.search(h2+h3): rows.append((t,h3 or h2 or t,tx,f))
out=[]
for t,rule,st,f in rows:
    out.append(row(id=f'uswds.{len(out)+1:04d}', source_set='U.S. Web Design System (USWDS)', source_org='GSA / USWDS', author='U.S. General Services Administration', year='2015-2026',
      category=categorize(t,rule,st), subcategory=t, title=f'{t}: {rule}', statement=st[:2500], detection_layer='screen / flow (guideline)', applies_to='web', severity_default='minor',
      citation=f'USWDS. {t}.', url='https://designsystem.digital.gov/'+('components/'+f.split('/_components/')[1].split('/')[0]+'/' if '_components' in f else ''), text_origin='verbatim', license='Public domain (US Gov) / CC0'))
write('uswds', out)
# Carbon
c=S+'/carbon-design-system_carbon-website/src/pages'
files=sorted(glob.glob(c+'/guidelines/**/*.mdx',recursive=True)+glob.glob(c+'/patterns/**/*.mdx',recursive=True)+glob.glob(c+'/components/*/usage.mdx')+glob.glob(c+'/components/*/accessibility.mdx')+glob.glob(c+'/elements/**/*.mdx',recursive=True)+glob.glob(c+'/data-visualization/**/*.mdx',recursive=True))
ct=lambda f: f.split('/src/pages/')[1].rsplit('.',1)[0].replace('/usage','').replace('/index','')
write('carbon', md_rows(files,'IBM Carbon Design System','IBM','2016-2026','Apache-2.0',lambda f:'https://carbondesignsystem.com/'+ct(f)+'/','carbon',title_fn=ct))
# Polaris
p=S+'/Shopify_polaris/polaris.shopify.com/content'
files=sorted(f for f in glob.glob(p+'/**/*.md*',recursive=True) if '/previous-releases/' not in f and '/version-guides/' not in f and '/tokens/' not in f and '/icons' not in f and '/tools/' not in f and '/contributing/' not in f)
write('polaris', md_rows(files,'Shopify Polaris','Shopify','2017-2026','MIT',lambda f:'https://polaris.shopify.com/'+f.split('/content/')[1].rsplit('.',1)[0].replace('/index',''),'polaris'))
# Primer
pr=S+'/primer_design/content'
files=sorted(glob.glob(pr+'/ui-patterns/**/*.mdx',recursive=True)+glob.glob(pr+'/foundations/**/*.mdx',recursive=True)+glob.glob(pr+'/guides/**/*.mdx',recursive=True)+glob.glob(pr+'/components/*.mdx'))
write('primer', md_rows(files,'GitHub Primer Design System','GitHub','2017-2026','MIT',lambda f:'https://primer.style/'+f.split('/content/')[1].rsplit('.',1)[0],'primer'))
# 18F content guide + ux guide + accessibility guide
files=sorted(glob.glob(S+'/18F_content-guide/_pages/**/*.md',recursive=True))
write('18f_content_guide', md_rows(files,'18F Content Guide','18F (GSA)','2016-2024','Public domain (US Gov) / CC0',lambda f:'https://content-guide.18f.gov/','18f-content'))
files=sorted(glob.glob(S+'/18F_ux-guide/_pages/**/*.md',recursive=True))
write('18f_ux_guide', md_rows(files,'18F UX Guide','18F (GSA)','2018-2024','Public domain (US Gov) / CC0',lambda f:'https://ux-guide.18f.gov/','18f-ux'))
files=sorted(glob.glob(S+'/18F_accessibility/pages/**/*.md',recursive=True))
write('18f_accessibility', md_rows(files,'18F Accessibility Guide','18F (GSA)','2015-2024','Public domain (US Gov) / CC0',lambda f:'https://accessibility.18f.gov/','18f-a11y'))
# plain language
files=sorted(glob.glob(S+'/GSA_plainlanguage.gov/_pages/guidelines/**/*.md',recursive=True))
write('plain_language', md_rows(files,'Federal Plain Language Guidelines (plainlanguage.gov)','PLAIN / GSA','2011 (rev. 2023)','Public domain (US Gov) / CC0',lambda f:'https://www.plainlanguage.gov/guidelines/','plain'))
# digital.gov guides
files=sorted(glob.glob(S+'/GSA_digitalgov.gov/content/guides/hcd/**/*.md',recursive=True)+glob.glob(S+'/GSA_digitalgov.gov/content/guides/mobile-principles/**/*.md',recursive=True)+glob.glob(S+'/GSA_digitalgov.gov/content/guides/accessibility-for-teams/**/*.md',recursive=True))
write('digitalgov_guides', md_rows(files,'Digital.gov guides (HCD, Mobile principles, Accessibility for teams)','GSA Digital.gov','2018-2025','Public domain (US Gov) / CC0',lambda f:'https://digital.gov/guides/','digitalgov'))
