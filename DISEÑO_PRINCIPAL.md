# Diseño Principal del Sitio Web — Uniempresarial

> **Propósito:** Documentar la arquitectura visual y los patrones de diseño de las páginas principales del sitio web de Uniempresarial, abarcando Posgrados, Pregrados, Tecnologías, Internacionalización, Admisiones, Apilables y Convenios.

---

## Índice

1. [Estructura General de una Página](#1-estructura-general-de-una-página)
2. [Posgrados](#2-posgrados)
3. [Pregrados](#3-pregrados)
4. [Tecnologías](#4-tecnologías)
5. [Internacionalización](#5-internacionalización)
6. [Admisiones](#6-admisiones)
7. [Apilables](#7-apilables)
8. [Convenios](#8-convenios)
9. [Estudiantes](#9-estudiantes)
10. [Componentes Compartidos](#10-componentes-compartidos)
11. [Patrones de Diseño Comunes](#11-patrones-de-diseño-comunes)

---

## 1. Estructura General de una Página

Cada sección del sitio sigue una arquitectura modular de componentes, donde cada archivo HTML representa un **bloque funcional independiente**. La estructura típica de una página es:

```
Hero (cabecera principal)
  ├── Título principal (h1)
  ├── Subtítulo / descripción
  ├── Chips / etiquetas
  ├── Metadatos (duración, modalidad, precio)
  └── Botones CTA (inscríbete, ver pensum, WhatsApp)

Cards de Programas
  ├── Grid de tarjetas (2 o 3 columnas)
  ├── Cada tarjeta con: imagen, título, metadatos, bullets, botones
  └── Modal emergente con información detallada

Sección "¿Por qué elegirnos?" (Why Us)
  ├── Grid de 4 tarjetas (2×2)
  ├── Icono + título + descripción breve
  └── Variante: integrada con tabla de inversión (split-section)

Preguntas Frecuentes (FAQ)
  └── Acordeón con pregunta/respuesta

Stats / Inversión (opcional)
  └── Grid de estadísticas o tabla de precios
```

---

## 2. Posgrados

**Archivos:** `posgrados/`

| Componente | Archivo | Descripción |
|---|---|---|
| Hero | `posgrados-hero.html` | Hero partido 50/50 con imagen de fondo |
| Cards | `posgrados-cardsProgramas.html` | Grid de 2 columnas con modal |
| Why Us | `posgrados-whyUs.html` | Grid 2×2 con iconos y descripciones |
| FAQ | `posgrados-preguntasFrecuentes.html` | Acordeón con acento naranja |

### Hero (Posgrados)
- **Layout:** Grid de 2 columnas (`grid-template-columns: 1fr 1fr`)
- **Lado izquierdo:** Fondo degradado naranja (`#FF6B35 → #FFA500`) con contenido textual
- **Lado derecho:** Imagen de fondo a través de `::after` pseudo-elemento
- **Responsive:** En ≤980px se apila verticalmente, la imagen pasa a `::before` como orden 1
- **Paleta:** Naranja corporativo (#FF6B35), textos blancos, badges rojos
- **Botones:** Verde WhatsApp (`#57D100`) y outline blanco para pensum
- **Metadatos:** Tarjetas (hp-card) con label/value: duración, créditos, precio, SNIES

### Cards de Programas (Posgrados)
- **Grid:** 2 columnas, gap 50px
- **Targeta (.pp-program-card):** Borde redondeado 12px, sombra suave, borde 1px #cbd5e1
- **Imagen:** Se desborda del contenedor (full-width + margen negativo) — `calc(100% + 56px)`
- **Badge "NUEVO":** Posición absoluta top-right, degradado rojo, sombra pulsante
- **Metadatos:** Barra horizontal con 3 items (duración, créditos, modalidad) separados por bordes
- **Bullets:** Lista con viñetas naranjas
- **Botones:** "Más información" (outline naranja) + secondary gray
- **Modal:** Overlay con animación de entrada (scale + translateY), fondo semitransparente
- **Variables de color:** Acento naranja #FF6B35, texto oscuro #1f2937, meta #334155

---

## 3. Pregrados

**Archivos:** `pregrados/`

| Componente | Archivo | Descripción |
|---|---|---|
| Hero + Cards + Why Us + FAQ | `pregrados-borrador.html` | Todo en un solo archivo |

### Características únicas (vs. Posgrados)
- **Variables CSS** con `:root` — paleta estructurada con naming semántico
- **Hero:** Fondo degradado azul (`#2A449C → #3a5bc7`) con estampado SVG de fondo
- **Barra de búsqueda** con icono de lupa y sombra al focus
- **Chips:** Estilo translucent (rgba white + backdrop-filter blur)
- **Botón CTA:** Rojo (#EF1218)
- **Grid de tarjetas:** 3 columnas en desktop, 2 en tablet, 1 en mobile
- **Animación fadeInUp** secuencial con `nth-child` delays
- **Badges:** Presencial (rojo), Virtual (verde #0BD926), Híbrida (púrpura #7C3AED)
- **Imagen de tarjeta:** `background-image` + `background-size: cover` en lugar de etiqueta `<img>`

---

## 4. Tecnologías

**Archivos:** `tecnologias/`

| Componente | Archivo | Descripción |
|---|---|---|
| Hero | `tecnologias-hero.html` | Similar a posgrados |
| Cards | `tecnologias-cardsProgramas.html` | Grid de 2 columnas tipo posgrados |
| Stats | `tecnologias-stats.html` | Grid de 4 columnas con indicadores |
| Why Us | `tecnologias-whyUs.html` | Grid 2×2 con iconos |
| FAQ | `tecnologias-preguntasFrecuentes.html` | Acordeón |

### Hero (Tecnologías)
- Mismo patrón que posgrados — hero partido con imagen
- **Prefijo de clases:** `pp-` (compartido con posgrados)
- Misma estructura de botones, badges y metadatos

### Stats (Tecnologías)
- **Grid:** 4 columnas con proporción `2.2fr 0.9fr 0.9fr 0.9fr`
- **Primera tarjeta:** Destinada a becas (borde superior amarillo #F59E0B)
- **Tarjetas de estadísticas:** Borde superior azul (#0048ff), iconos grandes (2rem)
- **Tarjeta de descuento:** Borde superior azul, sin badge de descuento visible (`display: none`)

### Why Us (Tecnologías)
- **Grid:** 2 columnas, gap 20px
- **Targeta:** Fondo gris claro (#eeefef), border-radius 16px
- **Icono:** Cuadrado azul (#0132AF) con SVG blanco, 50×50px
- **Título:** 17px, color #0a1f44
- **Párrafo:** 14px, color #64748b

---

## 5. Internacionalización

Se divide en 3 submódulos:

### 5.1 Internacionalización Inicio

**Archivos:** `internacionalizacionInicio/`

| Componente | Archivo | Descripción |
|---|---|---|
| Hero | `internacionalizacionInicio-hero.html` | Globo 3D interactivo + texto |
| Convenios | `internacionalizacionInicio-convenios.html` | Grid de socios internacionales |
| Documentos | `internacionalizacionInicio-documentos.html` | Lista de requisitos |
| Estudiantes | `internacionalizacionInicio-estudiantes.html` | Info para estudiantes |
| Visados | `internacionalizacionIncio-visados.html` | Info de visados |
| Requisitos | `internacionalizacionInicio-requisitos.html` | Requisitos detallados |

#### Hero (Internacionalización Inicio)
- **Layout:** Flex horizontal con gap 80px
- **Lado izquierdo:** Título grande (3rem, azul #0132AF), eyebrow rojo (#EF1218) con borde inferior, botón redondo (border-radius 40px)
- **Lado derecho:** Globo 3D interactivo (canvas + Three.js) con banderas de países posicionadas absolutamente
- **Banderas:** Círculos de 30×30px con `flag-icons` CSS, labels de texto, hover scale
- **Responsive:** En ≤850px se apila verticalmente

#### Convenios (Internacionalización)
- **Grid de partners:** 6 columnas, gap 14px
- **Targeta:** Borde sutil, border-radius 16px, hover con elevación (translateY -6px + scale 1.02)
- **Efecto hover:** Barra superior degradada (scaleX), brillo diagonal deslizante (pseudo-element `::after`)
- **Logo:** 68×68px círculo, imagen de 50×50px dentro
- **Sidebar derecha:** 210px fija con selector de países

### 5.2 Internacionalización Integral

**Archivos:** `internacionalizacionIntegral/`
- Hero, cultura, "en casa"

### 5.3 Internacionalización Visitante

**Archivos:** `internacionalizacionVisitante/`
- Hero, noticias, requisitos, testimonios

---

## 6. Admisiones

**Archivos:** `admisiones/`

| Componente | Archivo | Descripción |
|---|---|---|
| Hero | `admisiones-hero.html` | Split con video incrustado |
| Cards | `admisiones-cards.html` | Proceso de admisión + CTA |
| FAQ | `admisiones-preguntasFrecuentes.html` | Acordeón azul |

### Hero (Admisiones)
- **Layout:** Grid de 2 columnas, gap 50px, padding 80px
- **Lado izquierdo:** Eyebrow line animada ("Nuevo Proceso 2026" en rojo), título azul (#0132AF) 3rem, párrafo descriptivo
- **Lado derecho:** Video YouTube incrustado en iframe con sombra y border-radius
- **Animación:** Línea decorativa que se "estira" con keyframes
- **Responsive:** Apilamiento vertical en ≤768px

### Cards (Admisiones)
- **Grid:** 2 columnas, gap 24px
- **Targeta:** Borde izquierdo de 4px como acento (verde #57D100 y rojo #EA0A2A alternados)
- **Icono:** 56×56px con fondo de color según tarjeta (verde/rojo)
- **Botones:** Fondo sólido según el acento de la tarjeta
- **CTA grid:** 2 botones de ancho completo al final con fondo azul (#0132AF)
- **Modal:** Para formulario de inscripción

### FAQ (Admisiones)
- **Estilo:** Acordeón limpio con borde 1px #e5e7eb
- **Título:** Azul #0132AF, 2rem, weight 900
- **Hover:** Color azul en pregunta activa
- **Transición:** max-height suave + rotación de chevron

---

## 7. Apilables

**Archivos:** `apilables/` (programas apilables/cursos)
**Variantes:** `apilablesG/` (general), `apilablesP/` (específico)

| Componente | Archivo | Descripción |
|---|---|---|
| Hero | `apilables-hero.html` | Hero informativo con metadatos |
| Cards | `apilables-cardsProgramas-color-opciones.html` | Grid de programas |
| Why Us | `apilables-whyUs.html` | Split con inversión |
| Inversión | `apilables-inversion.html` | Tabla de precios |
| Pensum | `apilables-pensum.html` | Plan de estudios |
| FAQ | `apilables-PreguntasFrecuentes.html` | Acordeón |
| En qué puedes trabajar | `apilables-enQuePuedesTrabajar.html` | Salidas profesionales |

### Hero (Apilables)
- **Layout:** Flexible con información compacta
- **Título:** 35px, azul #0132AF
- **Meta grid:** 2×2 con items de datos (duración, horario, precio, SNIES)
- **Precio:** Destacado (18px, weight 900)
- **Botones:** WhatsApp verde, outline azul, formulario gris
- **Variantes:** Múltiples opciones de color y layout en `apilables-hero-opt10.html` y `apilables-hero-mobile-options.html`

### Cards (Apilables)
- **Opciones de color:** Múltiples variantes exploradas
- **Estructura base:** Border-left acento, meta grid interno, bullets, badges, botón full-width
- **Badges:** Etiquetas de categoría con borde

### Why Us + Inversión (Apilables)
- **Split-section:** Grid de 2 columnas (Why Us | Precios)
- **Why Us:** Grid 2×2 con iconos rojos (#EF1218), mismas cards que otras secciones
- **Inversión:** Tarjeta azul (#0132AF) con precio grande (60px) y detalles de financiación
- **Badge de descuento:** Rojo, posicionado absolutamente

---

## 8. Convenios

**Archivos:** `convenios/`

| Componente | Archivo | Descripción |
|---|---|---|
| Hero | `convenios-hero.html` | Hero editorial con imagen |
| Cards | `convenios-cards.html` | Grid de convenios con diseño geométrico |

### Hero (Convenios)
- **Layout:** Flex horizontal con altura fija (600px)
- **Texto:** Ancho fijo de 620px, título con borde izquierdo rojo de 4px (vía `::after`)
- **Imagen:** Ocupa el resto del espacio, con gradiente de desvanecimiento a blanco hacia la izquierda
- **Botón:** Azul #0132AF con hover translateX(4px) y flecha animada
- **Tipografía:** Inter, weight 800, letter-spacing -0.035em
- **Responsive:** En ≤1000px se apila verticalmente, altura automática

### Cards (Convenios)
- **Diseño geométrico único:** Tarjetas en forma de paralelogramo con `clip-path: polygon(10% 0, 100% 0, 90% 100%, 0 100%)`
- **Grid:** 3 columnas, gap 40px
- **Líneas decorativas:** Bordes superior e inferior con `clip-path`, líneas laterales con gradientes
- **Logo:** Centrado, tamaños variables según el socio (max-width 90-240px)
- **Hover:** Transformación con cubic-bezier bouncy
- **Color de borde:** Variable CSS `--border-color` para personalizar por tarjeta

---

## 9. Estudiantes

**Archivos:** `estudiantes/`

| Componente | Archivo | Descripción |
|---|---|---|
| Servicios | `estudiantes-servicios.html` | Grid 60/40 con cards de servicio + video sticky |

### Servicios (Estudiantes)
- **Layout:** Grid de 2 columnas con proporción `1.2fr 0.8fr` (60% izquierda, 40% derecha)
- **Columna izquierda:** 5 tarjetas horizontales con icono circular, texto y botón CTA
- **Icono:** Círculo 48×48px con borde azul #0132AF (1.5px), fondo blanco, border-radius 12px
- **SVG:** 22×22px, stroke #0132AF, stroke-width 2, stroke-linecap/stroke-linejoin round
- **Separador entre cards:** Borde inferior 1px #e5e7eb (no en la última)
- **Sin hover en cards** — solo el botón tiene efecto hover
- **Botón:** Outline azul #0132AF, ancho fijo 172px, hover relleno azul con texto blanco
- **Columna derecha:** Video sticky (top: 32px), tarjeta gris claro #f8fafc con sombra
- **Video:** YouTube iframe con aspect-ratio 16/9, border-radius 12px, src con ?rel=0
- **Header:** Eyebrow "Servicios" rojo #EF1218 con borde inferior 2px, título azul #0132AF 1.8rem
- **Animación:** fadeInUp con delays secuenciales (nth-child)
- **Tipografía:** Inter, títulos 800-900, textos descriptivos 0.8rem
- **Responsive:** ≤768px stack vertical, ≤480px cards con wrap

---

## 10. Componentes Compartidos

### Botón CTA Global (`.btn-cta`)
```css
.btn-cta {
    background: #0074FF;        /* o #EF1218 según sección */
    color: #ffffff;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
}
```
Cada sección redefine el color de fondo según su paleta.

### Sección "¿Por qué elegirnos?" (Why Us)
- **Layout:** Grid 2×2, max-width 680-1200px
- **Targeta:** Fondo #eeefef, border-radius 12-16px, padding 24-30px
- **Icono:** Cuadrado 46-50px con SVG blanco y fondo de color corporativo
- **Título:** 16-17px, color oscuro
- **Párrafo:** 14px, color gris (#64748b o #718096)

Los colores de acento varían por sección:
| Sección | Color Acento |
|---|---|
| Posgrados | Naranja #FF6B35 |
| Pregrados | Rojo #EF1218 |
| Tecnologías | Azul #0132AF |
| Apilables | Rojo #EF1218 |

### Preguntas Frecuentes (FAQ)
- **Patrón:** Acordeón con HTML + CSS puro (sin JavaScript)
- **Mecanismo:** Estado `open` mediante clase CSS en `.faq-item`
- **Animación:** `max-height` con transición suave + rotación de chevron (▾)
- **Estructura:**
  - Wrapper `.faq-wrap` con padding
  - Header con título + intro
  - `.faq-section` con border-radius y sombra
  - Items con `.faq-question` (button) + `.faq-answer` (div oculto)
- **Variantes por sección:**
  - **Posgrados:** Acento naranja (#FF6B35), borde azul en hover
  - **Admisiones:** Acento azul (#0132AF), borde 1px #e5e7eb
  - **Pregrados:** Integrado en borrador

---

## 10. Patrones de Diseño Comunes

### 10.1 Hero Split (mitad texto / mitad imagen)
Usado en: Posgrados, Tecnologías, Admisiones, Convenios

```
Desktop: [Texto | Imagen] en grid 1fr 1fr
Mobile:  [Imagen] → [Texto] apilado (flex-direction: column)
```

### 10.2 Grid de Tarjetas
| Sección | Columnas Desktop | Columnas Tablet | Columnas Mobile |
|---|---|---|---|
| Posgrados | 2 | 2 | 1 |
| Pregrados | 3 | 2 | 1 |
| Tecnologías | 2 | 2 | 1 |
| Convenios | 3 | 2 | 1 |

### 10.3 Paleta de Colores Corporativos

| Color | Hex | Uso |
|---|---|---|
| Azul primario | `#0132AF` | Títulos, fondos de botones, iconos |
| Rojo acento | `#EF1218` | Badges, CTAs, eyebrows |
| Naranja acento | `#FF6B35` | Posgrados, bullets, detalles |
| Verde éxito | `#57D100` / `#0BD926` | Botón WhatsApp, badge virtual |
| Fondo gris | `#eeefef` | Cards Why Us, fondos secundarios |
| Texto oscuro | `#1f2937` / `#0f172a` | Títulos de tarjetas |
| Texto gris | `#64748b` / `#4a5568` | Descripciones, metadatos |

### 10.4 Breakpoints Responsive
- **Desktop:** > 1024px
- **Tablet:** ≤ 768px (o 980px para heroes split)
- **Mobile:** ≤ 480px (o 375px para ajustes finos)

### 10.5 Animaciones Recurrentes
- `fadeInUp`: Entrada de tarjetas con delays secuenciales
- `pulse-badge`: Pulsación suave en badges "NUEVO"
- `breathing-badge`: Variante de pulsación para hero
- `estirar-linea`: Animación de línea decorativa en admisiones
- `slideUp`: Modal emergente con efecto elástico

### 10.6 Sistema de Modales
- Overlay fijo con `opacity` + `visibility` toggle
- Modal centrado con `translateY` y `scale` en entrada
- Transiciones: `cubic-bezier(0.34, 1.56, 0.64, 1)` para efecto elástico
- Botón cerrar circular con hover suave

---

## Resumen de Archivos por Sección

```
recursosWeb/
├── posgrados/
│   ├── posgrados-hero.html               # Hero split naranja
│   ├── posgrados-cardsProgramas.html     # Grid 2 cols + modal
│   ├── posgrados-whyUs.html              # Why Us naranja
│   └── posgrados-preguntasFrecuentes.html # FAQ naranja
├── pregrado/
│   └── pregrado-borrador.html            # Todo en uno (azul)
├── tecnologias/
│   ├── tecnologias-hero.html             # Hero split (pp-)
│   ├── tecnologias-cardsProgramas.html   # Grid 2 cols (pp-)
│   ├── tecnologias-stats.html            # Grid estadísticas
│   ├── tecnologias-whyUs.html            # Why Us azul
│   └── tecnologias-preguntasFrecuentes.html
├── internacionalizacionInicio/
│   ├── internacionalizacionInicio-hero.html      # Globo 3D
│   ├── internacionalizacionInicio-convenios.html # Partners grid
│   ├── internacionalizacionInicio-documentos.html
│   ├── internacionalizacionInicio-estudiantes.html
│   ├── internacionalizacionIncio-visados.html
│   └── internacionalizacionInicio-requisitos.html
├── internacionalizacionIntegral/
│   ├── internacionalizacionIntegral-hero.html
│   ├── internacionalizacionIntegral-cultura.html
│   └── internacionalizacionIntegral-enCasa.html
├── internacionalizacionVisitante/
│   ├── internacionalizacionVisitante-hero.html
│   ├── internacionalizacionVisitante-noticias.html
│   ├── internacionalizacionVisitante-requisitos.html
│   └── internacionalizacionVisitante-testimonios.html
├── admisiones/
│   ├── admisiones-hero.html              # Hero video
│   ├── admisiones-cards.html             # Proceso + CTA
│   └── admisiones-preguntasFrecuentes.html # FAQ azul
├── apilables/
│   ├── apilables-hero.html               # Hero info compacto
│   ├── apilables-cardsProgramas-color-opciones.html
│   ├── apilables-whyUs.html              # Split + inversión
│   ├── apilables-inversion.html          # Tabla precios
│   ├── apilables-pensum.html
│   ├── apilables-enQuePuedesTrabajar.html
│   └── apilables-PreguntasFrecuentes.html
├── apilablesG/                           # Variante general
│   ├── apilablesG-hero.html
│   ├── apilablesG-cardsProgramas.html
│   ├── apilablesG-whyUs.html
│   └── apilablesG-PreguntasFrecuentes.html
├── apilablesP/                           # Variante específica
│   ├── apilablesP-hero.html
│   ├── apilablesP-pensum.html
│   ├── apilablesP-whyUs.html
│   └── apilablesP-enQuePuedesTrabajar.html
└── convenios/
    ├── convenios-hero.html               # Hero editorial
    └── convenios-cards.html              # Cards geométricas
```
