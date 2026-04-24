import bs4
from bs4 import BeautifulSoup
import re

html_path = 'c:/Users/emers/Documents/GitHub/recursosWeb/cursosG-cards.html'
apilables_path = 'c:/Users/emers/Documents/GitHub/recursosWeb/apilablesG-cardsProgramas.html'

with open(html_path, 'r', encoding='utf-8') as f:
    soup_tgt = BeautifulSoup(f, 'html.parser')

with open(apilables_path, 'r', encoding='utf-8') as f:
    soup_src = BeautifulSoup(f, 'html.parser')

# Remove all badges
for badge in soup_tgt.select('.cg-card-badge'):
    badge.decompose()

# Update all existing card meta items in tab1 and tab3
icon_time = '<svg xmlns="http://www.w3.org/2000/svg" class="cg-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
icon_mod = '<svg xmlns="http://www.w3.org/2000/svg" class="cg-icon" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'

# Reformat meta items to include icons if they are just spans
for meta in soup_tgt.select('.cg-card-meta'):
    items = meta.select('.cg-card-meta-item')
    for idx, item in enumerate(items):
        if item.name == 'span':
            # Convert to div
            new_item = soup_tgt.new_tag('div', attrs={'class': 'cg-card-meta-item'})
            
            # Add icon based on type (simple heuristic: if it has "horas", use time icon, else use mod icon)
            text_content = item.text.strip()
            if 'hora' in text_content.lower():
                new_item.append(BeautifulSoup(icon_time, 'html.parser'))
            else:
                new_item.append(BeautifulSoup(icon_mod, 'html.parser'))
            
            new_item.append(" " + text_content)
            item.replace_with(new_item)

# Get all the articles from the source
src_articles = soup_src.select('.ue-card-program')

# Remove all articles from tab2
tab2 = soup_tgt.find('div', id='tab2')
if tab2:
    for art in tab2.select('.cg-card'):
        art.decompose()

# Iterate and convert the src articles to target style format properly
if tab2:
    for src_art in src_articles:
        new_art = soup_tgt.new_tag('article', attrs={'class': 'cg-card homologables-tab'})

        # Header
        header_div = soup_tgt.new_tag('div', attrs={'class': 'cg-card-header'})
        title_h3 = soup_tgt.new_tag('h3', attrs={'class': 'cg-card-title'})
        title_h3.string = src_art.select_one('.ue-card-program-title').text.strip()
        header_div.append(title_h3)
        new_art.append(header_div)

        # Meta
        meta_div = soup_tgt.new_tag('div', attrs={'class': 'cg-card-meta'})
        metas = src_art.select('.ue-card-program-meta-item')
        if len(metas) >= 2:
            meta1 = soup_tgt.new_tag('div', attrs={'class': 'cg-card-meta-item'})
            meta1.append(BeautifulSoup(icon_time, 'html.parser'))
            meta1.append(" " + metas[0].text.strip())
            meta_div.append(meta1)

            meta2 = soup_tgt.new_tag('div', attrs={'class': 'cg-card-meta-item'})
            meta2.append(BeautifulSoup(icon_mod, 'html.parser'))
            meta2.append(" " + metas[1].text.strip())
            meta_div.append(meta2)
        new_art.append(meta_div)

        # Bullets
        bullets_ul = soup_tgt.new_tag('ul', attrs={'class': 'cg-card-bullets'})
        for li in src_art.select('.ue-card-program-bullets li'):
            new_li = soup_tgt.new_tag('li')
            new_li.string = li.text.strip()
            bullets_ul.append(new_li)
        new_art.append(bullets_ul)

        # Actions
        actions_div = soup_tgt.new_tag('div', attrs={'class': 'cg-card-actions'})
        link_a = soup_tgt.new_tag('a', attrs={'href': '#', 'class': 'cg-card-link'})
        link_a.append("Ver detalles ")
        span = soup_tgt.new_tag('span')
        span.string = "→"
        link_a.append(span)
        actions_div.append(link_a)
        
        new_art.append(actions_div)
        tab2.append(new_art)

# Format the HTML to keep it pretty
html_output = str(soup_tgt)

# Fix some formatting issues created by BeautifulSoup
html_output = html_output.replace('></circle>', '/>')
html_output = html_output.replace('></polyline>', '/>')
html_output = html_output.replace('></rect>', '/>')
html_output = html_output.replace('></line>', '/>')
html_output = html_output.replace('></path>', '/>')
html_output = html_output.replace('></animate>', '/>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_output)

