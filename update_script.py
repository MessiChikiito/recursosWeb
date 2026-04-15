import re

file_path = 'c:/Users/uestudiantes/Documents/GitHub/recursosWeb/apliables-pensum.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(
    r'<div class=\"pd-semesters\" id=\"semestresContainer\">.*?</div>',
    '''<div class=\"pd-semesters\" id=\"semestresContainer\">
            <button class=\"pd-semester-btn active\" data-semestre=\"1\">Eje Temático 1</button>
            <button class=\"pd-semester-btn\" data-semestre=\"2\">Eje Temático 2</button>
        </div>''',
    text, flags=re.DOTALL
)

text = re.sub(
    r'<div class=\"pd-total-carrera-label\">.*?</div>\s*<div class=\"pd-total-carrera-value\" id=\"creditosCarrera\">.*?</div>\s*<div class=\"pd-total-carrera-unit\">.*?</div>',
    '''<div class=\"pd-total-carrera-label\">Total</div>
                        <div class=\"pd-total-carrera-value\" id=\"creditosCarrera\">48</div>
                        <div class=\"pd-total-carrera-unit\">horas en total</div>''',
    text, flags=re.DOTALL
)

# remove the extra 'cr.' from materia head
text = re.sub(r'<div class=\"pd-materia-credit\">.*?</div>', '', text, flags=re.DOTALL)

text = re.sub(
    r'const semestreData = \{.*?\};',
    '''const semestreData = {
            1: [
                { nombre: "Marco Mercantil, Registro y Estructuras Empresariales: 'Emprende Legalmente: Comercio, Sociedades y Tributos sin Complicaciones'", tipo: "nucleo", temas: "Fundamentos de derecho mercantil<br>Organizaciones y sociedades<br>Títulos valores<br>Fundamentos de derecho tributario" }
            ],
            2: [
                { nombre: "Fundamentos y Aplicación Práctica de la Tributación Colombiana: 'Cumple y gana: guía práctica del sistema tributario colombiano'", tipo: "nucleo", temas: "El impuesto de renta y complementarios<br>Impuesto al Valor Agregado (IVA).<br>Régimen Simple de Tributación (RST)<br>Otros impuestos nacionales.<br>Aspectos generales de procedimiento tributario." }
            ]
        };''',
    text, flags=re.DOTALL
)

text = re.sub(r'document\.getElementById\(\'creditosCarrera\'\)\.textContent = totalCreditos;', '', text)
text = re.sub(r'const totalCreditos = .*?;', '', text)
text = re.sub(r'<div class=\"pd-credits-label\">Total créditos cuatrimestre.*?</div>', '', text, flags=re.DOTALL)
text = text.replace('let totalCreditos = 0;', '')
text = text.replace('totalCreditos += parseInt(materia.creditos || 0);', '')
text = text.replace('let creditosCuatrimestre = 0;', '')
text = text.replace('+ materia.creditos +', '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Done')
