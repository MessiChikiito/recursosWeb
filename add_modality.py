from bs4 import BeautifulSoup

html_path = 'c:/Users/emers/Documents/GitHub/recursosWeb/cursosG-cards.html'

with open(html_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

icon_mod = '<svg xmlns="http://www.w3.org/2000/svg" class="cg-icon" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'

# Define modalities for each course
course_modalities = {
    'Gestión de Proyectos': 'Virtual / Presencial',
    'Innovación y Transformación Digital': 'Virtual',
    'Planeación Estratégica y Toma de Decisiones': 'Virtual',
    'Servicio al Cliente y Experiencia del Usuario': 'Presencial',
    'Marketing Digital y Community Management': 'Virtual / Presencial',
    'Pensamiento Computacional y Programación Eficiente': 'Virtual / Presencial',
    'Programación y Estructuras de Datos: Java y Python': 'Virtual / Presencial',
    'Ecosistemas Digitales y Ciberseguridad Empresarial': 'Virtual',
    'Frontend Master: Diseño e Interactividad Web Profesional': 'Virtual / Presencial',
}

# Add modality to all courses in tab1 and tab3
for tab_id in ['tab1', 'tab3']:
    tab = soup.find('div', id=tab_id)
    if tab:
        for card in tab.select('.cg-card'):
            title_elem = card.select_one('.cg-card-title')
            if title_elem:
                title = title_elem.text.strip()
                # Get modality from dict or use a default
                modality = course_modalities.get(title, 'Virtual / Presencial')
                
                # Find the meta div
                meta_div = card.select_one('.cg-card-meta')
                if meta_div:
                    # Check if modality already exists
                    modality_items = meta_div.select('.cg-card-meta-item')
                    if len(modality_items) == 1:
                        # Add modality meta item
                        new_meta_item = soup.new_tag('div', attrs={'class': 'cg-card-meta-item'})
                        new_meta_item.append(BeautifulSoup(icon_mod, 'html.parser'))
                        new_meta_item.append(f" Modalidad: {modality}")
                        meta_div.append(new_meta_item)

# Write back
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(str(soup.prettify()))
