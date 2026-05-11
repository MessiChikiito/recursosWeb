import re

# Leer archivo
with open(r"c:\Users\aprendizmercadeo4\Documents\GitHub\recursosWeb\cursosG-cards.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Patrón simple: buscar <picture>...</picture> y extraer la URL
pattern = r'<picture>.*?<img src="([^"]*\?w=1200[^"]*)" alt="([^"]*)".*?</picture>'

matches = re.findall(pattern, content, re.DOTALL)

print(f"Encontrados {len(matches)} picture elements:")
for i, (url, alt) in enumerate(matches, 1):
    url_base = url.split('?')[0]
    print(f"{i}. {url_base}")
    print(f"   Alt: {alt}\n")
