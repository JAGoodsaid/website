"""Run once before upload: python3 configure-seo.py https://your-own-domain/"""
import sys, json, re, html
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET
root=Path(__file__).resolve().parent
preview=sys.argv[1:]==['--local-preview']
if not preview and len(sys.argv)!=2: sys.exit(__doc__)
base='' if preview else sys.argv[1].rstrip('/')+'/'
u=urlsplit(base)
if not preview and (u.scheme!='https' or not u.hostname or u.username or u.password or u.query or u.fragment or any(c.isspace() for c in base)): sys.exit('Supply the final public HTTPS address, optionally with a subfolder.')
name='Jasmine Goodsaid'
pages=['index.html','client-onboarding.html','google-reporting-automation.html']
titles=['Jasmine Goodsaid | Product Operations & Applied Ai for B2B SaaS','B2B Client Onboarding With Claude and HubSpot | Jasmine Goodsaid','Google Apps Script Automation for Ad Reporting | Jasmine Goodsaid']
descriptions=['Explore Jasmine Goodsaid’s B2B SaaS portfolio: AI-powered client onboarding, Google Apps Script reporting automation, and go-to-market work at Dealers United.', 'See how Jasmine Goodsaid built a shared B2B onboarding task list from CRM data using Claude Artifacts and HubSpot at Dealers United.', 'Explore Jasmine Goodsaid’s Google Apps Script integrations for syncing advertising, streaming, and email reporting data into Google Sheets.']
def tag(key,val,prop=False): return '<meta '+('property' if prop else 'name')+'="'+key+'" content="'+html.escape(val,quote=True)+'">'
person={'@type':'Person','@id':(base or './')+'#jasmine','name':name,'alternateName':'Jasmine A. Goodsaid','description':'Jasmine Goodsaid is a marketing engineer and B2B SaaS product operations leader specializing in applied AI and automation. At Dealers United, she builds client onboarding and reporting tools and supports the go-to-market launch of software products.','jobTitle':'Reporting & Operations Manager','worksFor':{'@type':'Organization','name':'Dealers United'},'sameAs':['https://www.linkedin.com/in/jasminegoodsaid/'],'knowsAbout':['Marketing engineering','B2B SaaS product marketing','Go-to-market strategy','Google Apps Script automation','Marketing analytics','AI workflow integration']}
site={'@type':'WebSite','@id':(base or './')+'#site','name':'Jasmine Goodsaid','url':base or './'}
urls=[]
for i,f in enumerate(pages):
 target=root/f; source=target.read_text()
 url=base+('' if i==0 else f) or './'; urls.append(url)
 title,desc=titles[i],descriptions[i]
 graph=[site,person,{'@type':'ProfilePage' if not i else 'WebPage','@id':url+'#page','url':url,'name':title,'description':desc,'isPartOf':{'@id':site['@id']},'mainEntity':{'@id':person['@id'] if not i else url+'#study'}}]
 if i: graph.append({'@type':'CreativeWork','@id':url+'#study','name':title.split(' | ')[0],'description':desc,'author':{'@id':person['@id']},'url':url})
 lines=['<title>'+html.escape(title)+'</title>',tag('description',desc),tag('author',name),tag('robots','index,follow,max-image-preview:large'),tag('apple-mobile-web-app-title','JAG'),tag('theme-color','#1B8F74'),'<link rel="icon" href="assets/JG.svg" type="image/svg+xml">','<link rel="icon" href="assets/favicon-96.png" sizes="96x96" type="image/png">','<link rel="apple-touch-icon" href="assets/Logo.png">']
 if base: lines+=['<link rel="canonical" href="'+html.escape(url,quote=True)+'">',tag('og:url',url,True)]
 image=base+'assets/portfolio-preview.png'; alt='Jasmine Goodsaid | Product Operations & Applied Ai for B2B SaaS'
 for k,v in [('type','website' if not i else 'article'),('locale','en_US'),('site_name','Jasmine Goodsaid'),('title',title),('description',desc),('image',image),('image:type','image/png'),('image:width','1200'),('image:height','630'),('image:alt',alt)]:lines.append(tag('og:'+k,v,True))
 for k,v in [('card','summary_large_image'),('title',title),('description',desc),('image',image),('image:alt',alt)]:lines.append(tag('twitter:'+k,v))
 lines+=['<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},indent=2,ensure_ascii=False)+'</script>']
 head='<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'+'\n'.join(lines)+'\n<link rel="stylesheet" href="css/styles.css">\n'+('<script src="js/main.js" defer></script>\n' if not i else '')+'</head>'
 target.write_text(re.sub(r'<head>.*?</head>',lambda m:head,source,count=1,flags=re.S))
robots='User-agent: *\nAllow: /\n'
if base:
 tree=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
 for address in urls: ET.SubElement(ET.SubElement(tree,'url'),'loc').text=address
 ET.indent(tree); ET.ElementTree(tree).write(root/'sitemap.xml',encoding='utf-8',xml_declaration=True)
 robots+='\nSitemap: '+base+'sitemap.xml\n'
else: (root/'sitemap.xml').unlink(missing_ok=True)
(root/'robots.txt').write_text(robots)
print('Local preview ready.' if preview else 'Configured canonical URLs, social images, schema, robots.txt and sitemap.xml for '+base)
