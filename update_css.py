import re

html_path = 'c:/Users/emers/Documents/GitHub/recursosWeb/cursosG-cards.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make icon CSS available
icon_css = """
        .cg-icon {
            width: 18px !important;
            height: 18px !important;
            display: inline-block;
            vertical-align: middle;
            fill: none !important;
            stroke: currentColor !important;
            stroke-width: 2 !important;
            stroke-linecap: round !important;
            stroke-linejoin: round !important;
            color: #EF1218;
        }"""
if '.cg-icon' not in html:
    html = html.replace('.cg-card-meta {', icon_css + '\n        .cg-card-meta {')

html = html.replace("""        .cg-card-meta-item:not(:first-child)::before {
            content: "•";
            color: #EF1218;
            margin-right: 8px;
            font-size: 18px;
        }""", """        .cg-card-meta-item:not(:last-child)::after {
            content: "/";
            color: #cbd5e1;
            margin-left: 10px;
            font-size: 14px;
            font-weight: 400;
        }""")

html = html.replace("""        .cg-card-meta-item {
            font-size: 13px;
            color: #334155;
            font-weight: 600;
            display: flex;
            align-items: center;
        }""", """        .cg-card-meta-item {
            font-size: 13px;
            color: #334155;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }""")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
