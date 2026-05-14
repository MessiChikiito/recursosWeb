# CATALOG.md - Catálogo Completo de Componentes HTML

**Índice de todos los archivos HTML en recursosWeb, organizados temáticamente.**

Cada entrada sigue este template:
```
**[archivo.html]** — [Propósito]
- Componentes: [elementos visuales]
- Uso: [contexto/página]
- Deps: [archivos relacionados o referencias]
```

---

## Admisiones

**admisiones-hero.html** — Sección hero con diseño llamativo para página de admisiones
- Componentes: hero, encabezado, CTA principal
- Uso: Landing page de admisiones con propuesta de valor
- Deps: general-opcionesColoresHero.html (referencia de estilos)

**admisiones-cards.html** — Tarjetas informativas de pasos o requisitos en admisiones
- Componentes: cards flexibles con iconos y texto
- Uso: Mostrar proceso de admisión, documentos requeridos
- Deps: general-opcionesCardsPrograma.html (patrón de cards)

**admisiones-colores-opciones.html** — Variaciones de esquemas de color para sección de admisiones
- Componentes: cards y banners con múltiples paletas
- Uso: Pruebas de diseño y selección de tema visual
- Deps: admisiones-cards.html, admisiones-hero.html

**admisiones-preguntasFrecuentes.html** — Sección de preguntas frecuentes para admisiones
- Componentes: acordeones, FAQ items
- Uso: Sección FAQ en página de admisiones
- Deps: general-opcionesAcordeon.html (patrón de acordeón)

---

## Apilables (Variaciones de Secciones Apilables)

**apilables-hero.html** — Hero básico para tema apilables
- Componentes: hero, gradient background, CTA
- Uso: Sección superior de página de apilables
- Deps: general-opcionesfondoHero.html (estilos de fondo)

**apilables-hero-mobile-options.html** — Variaciones responsive del hero para dispositivos móviles
- Componentes: hero con layouts alternativos móvil
- Uso: Testeo de responsive design en tema apilables
- Deps: apilables-hero.html

**apilables-hero-opt10.html** — Décima opción/variación del hero (diseño experimental)
- Componentes: hero con layout alternativo
- Uso: Prueba de diseño experimental
- Deps: apilables-hero.html

**apilables-cards-opciones.html** — Múltiples estilos de cards para apilables
- Componentes: cards con diferentes layouts, iconos, metadata
- Uso: Mostrar opciones de diseño para cards en apilables
- Deps: general-opcionesCardsPrograma.html

**apilables-cardsProgramas-color-opciones.html** — Cards de programas con variaciones de color
- Componentes: cards de programas con paletas alternativas
- Uso: Comparación visual de temas de color para programas
- Deps: apilables-cards-opciones.html

**apilables-badge-opciones.html** — Variaciones de badges/etiquetas para resaltar información
- Componentes: badges con estilos múltiples
- Uso: Acompañar cards o títulos en apilables
- Deps: general-opcionesBadge.html

**apilables-whyUs.html** — Sección "Por qué elegir apilables" con puntos diferenciales
- Componentes: feature list, diferenciadores, iconografía
- Uso: Sección de ventajas/beneficios en página de apilables
- Deps: general-diferenciadoresEnListasOCards.html

**apilables-whyUs-opciones-mismo-formato.html** — Variaciones de "why us" manteniendo formato
- Componentes: listas de beneficios con estilos alternativos
- Uso: Pruebas de diseño de sección "por qué"
- Deps: apilables-whyUs.html

**apilables-whyUs-inversion.html** — Sección "por qué" con énfasis en retorno de inversión
- Componentes: cards de beneficios, estadísticas, ROI indicators
- Uso: Página de apilables enfocada en aspecto financiero
- Deps: apilables-whyUs.html, posgrados-bannerFinanciacion.html

**apilables-whyUs-inversion-15opciones.html** — 15 variaciones del layout de inversión/ROI
- Componentes: múltiples diseños de sección why-us con ROI
- Uso: Selección de diseño para énfasis financiero
- Deps: apilables-whyUs-inversion.html

**apilables-inversion.html** — Información y detalles sobre inversión/financiación
- Componentes: tabla de precios, planes, opciones de pago
- Uso: Sección de costos y financiación en apilables
- Deps: general-opcionesCardsFinanciacion.html

**apilables-enQuePuedesTrabajar.html** — Sección de oportunidades laborales post-apilables
- Componentes: grid de profesiones, salarios, salidas laborales
- Uso: Mostrar proyección profesional para egresados
- Deps: programas-enQuePuedesTrabajar.html (patrón base)

**apilables-enQuePuedesTrabajar-opciones.html** — Múltiples variaciones de "en qué puedes trabajar"
- Componentes: diferentes layouts de grid de profesiones
- Uso: Pruebas de diseño para sección de oportunidades
- Deps: apilables-enQuePuedesTrabajar.html

**apilables-PreguntasFrecuentes.html** — FAQ para programa de apilables
- Componentes: acordeones, preguntas expandibles
- Uso: Sección de preguntas frecuentes en página apilables
- Deps: general-opcionesAcordeon.html

---

## ApilablesG (Variante General/Extendida)

**apilablesG-hero.html** — Hero versión general extendida para apilables
- Componentes: hero con opciones adicionales
- Uso: Alternativa a hero estándar con más flexibilidad
- Deps: apilables-hero.html

**apilablesG-cardsProgramas.html** — Cards de programas versión general
- Componentes: cards con estructura flexible
- Uso: Mostrar programas en versión general
- Deps: apilables-cardsProgramas-color-opciones.html

**apilablesG-whyUs.html** — Sección why-us versión general
- Componentes: diferenciadores con layout flexible
- Uso: Beneficios con estructura extendida
- Deps: apilables-whyUs.html

**apilablesG-PreguntasFrecuentes.html** — FAQ versión general extendida
- Componentes: acordeones con opciones adicionales
- Uso: FAQ con mayor flexibilidad de diseño
- Deps: apilables-PreguntasFrecuentes.html

---

## Blog

**blog-hero.html** — Sección hero para página principal de blog
- Componentes: hero con fondo, título, buscador
- Uso: Encabezado de blog o página de posts
- Deps: blog-principal.html

**blog-principal.html** — Página principal de blog con lista de posts
- Componentes: grid de posts, categorías, filtros
- Uso: Landing page de blog
- Deps: blog-hero.html, blog-post-template.html

**blog-post-template.html** — Plantilla base para páginas individuales de posts
- Componentes: header, contenido, sidebar, footer
- Uso: Plantilla para todos los posts individuales
- Deps: blog-post-hero-split.html

**blog-post-hero-split.html** — Hero con split layout (imagen + texto) para posts
- Componentes: hero split, imagen destacada, metadata
- Uso: Encabezado atractivo en posts individuales
- Deps: blog-post-template.html

**blog-post-content-split.html** — Contenido con split layout para posts
- Componentes: texto + imagen lateral alternando
- Uso: Contenido body de posts con visuales intercalados
- Deps: blog-post-template.html

**blog-post-content-split-dummy.html** — Versión dummy/prueba de content-split
- Componentes: layout split con placeholder text
- Uso: Testeo y prototipado de contenido
- Deps: blog-post-content-split.html

**blog-post-formulario-banner-split.html** — Banner con formulario en split layout
- Componentes: formulario + imagen, CTA secundario
- Uso: Sección de conversión en medio del post
- Deps: general-formularioDeAsesoria.html

**webinars-beneficios.html** — Beneficios de webinars (reutilizado en blog)
- Componentes: feature list, iconografía
- Uso: Beneficios o puntos destacados
- Deps: general-10opcionesBullets.html

---

## Cursos

**cursosG-hero.html** — Hero para página de cursos
- Componentes: hero, encabezado, CTA
- Uso: Sección superior de página de cursos
- Deps: general-opcionesColoresHero.html

**cursosG-cards.html** — Cards para listar cursos disponibles
- Componentes: cards de cursos, duración, nivel, CTA
- Uso: Mostrar catálogo de cursos
- Deps: general-opcionesCardsPrograma.html

**cursosG-newsletter.html** — Sección de suscripción a newsletter para cursos
- Componentes: formulario de correo, beneficio visual
- Uso: Captura de leads en página de cursos
- Deps: general-formularioDeAsesoria.html

**cursosG-preguntasFrecuentes.html** — FAQ para cursos
- Componentes: acordeones, preguntas expandibles
- Uso: Sección FAQ en página de cursos
- Deps: general-opcionesAcordeon.html

---

## General (Componentes Reutilizables)

**general-hero.html** — Hero básico y reutilizable
- Componentes: hero con fondo, encabezado, CTA
- Uso: Sección superior de cualquier página
- Deps: Ninguna (componente base)

**general-10opcionesHero.html** — Diez variaciones de hero
- Componentes: múltiples layouts y estilos de hero
- Uso: Seleccionar variante adecuada para proyecto
- Deps: general-hero.html

**general-opcionesColoresHero.html** — Variaciones de color en sección hero
- Componentes: hero con múltiples paletas
- Uso: Testeo de temas de color
- Deps: general-hero.html

**general-headerSitioWeb.html** — Header/navbar reutilizable para sitios
- Componentes: navigation bar, logo, menú
- Uso: Encabezado en todas las páginas
- Deps: Ninguna

**general-borradorHeaderSitioWeb.html** — Versión borrador/experimental de header
- Componentes: navbar con diseño alternativo
- Uso: Pruebas de navegación
- Deps: general-headerSitioWeb.html

**general-diferenciadoresEnListasOCards.html** — Componente para resaltar diferenciales
- Componentes: listas, cards, badges destacadores
- Uso: Mostrar ventajas competitivas
- Deps: general-opcionesBadge.html

**general-opcionesCardsPrograma.html** — Diseño estándar para cards de programas
- Componentes: card con título, descripción, CTA, metadata
- Uso: Listar programas académicos
- Deps: Ninguna (componente base)

**general-10opcionesCardsFinanciacion.html** — Diez opciones de cards para financiación
- Componentes: cards con planes, precios, features
- Uso: Mostrar planes de pago disponibles
- Deps: general-opcionesCardsPrograma.html

**general-10opcionesCardsFinanciacionHorizontal.html** — Diez cards de financiación en layout horizontal
- Componentes: cards apaisadas con planes
- Uso: Mostrar planes lado a lado
- Deps: general-10opcionesCardsFinanciacion.html

**general-20opcionesCardsFinanciacionHorizontalV2.html** — 20 variaciones de cards horizontales
- Componentes: cards horizontales (imagen + contenido lado a lado)
- Uso: Testeo extenso de layouts de financiación
- Deps: general-opcionesCardsFinanciacion.html

**general-opcionesCardsJornadas.html** — Cards para mostrar jornadas (diurna, nocturna, etc.)
- Componentes: cards específicas para jornadas
- Uso: Diferenciar programas por jornada
- Deps: general-opcionesCardsPrograma.html

**general-opcionesCardsConMetadata.html** — Cards genéricas con metadata (fecha, autor, etc.)
- Componentes: cards con información adicional
- Uso: Posts de blog, eventos, noticias
- Deps: general-opcionesCardsPrograma.html

**general-opcionesColoresCardsConBoton.html** — Cards con colores alternativos y botón
- Componentes: cards con multiple color schemes
- Uso: Variantes visuales de cards
- Deps: general-opcionesCardsPrograma.html

**general-opcionesCardDescuento.html** — Card de descuentos especiales
- Componentes: card con badge de descuento, precio tachado
- Uso: Promociones, ofertas limitadas
- Deps: general-opcionesBadgeDescuento.html

**general-opcionesBadge.html** — Variaciones básicas de badges/etiquetas
- Componentes: múltiples estilos de badges
- Uso: Etiquetar información (nuevo, popular, etc.)
- Deps: Ninguna (componente base)

**general-opcionesBadge2.html** — Segunda variación de badges con estilos adicionales
- Componentes: badges alternativos
- Uso: Alternativas a badges estándar
- Deps: general-opcionesBadge.html

**general-opcionesBadgeDescuento.html** — Badges específicos para descuentos
- Componentes: badge con porcentaje, "en venta", etc.
- Uso: Indicar promociones
- Deps: general-opcionesBadge.html

**general-botonesGod.html** — Variaciones del botón "god" (principal, versátil)
- Componentes: botones con múltiples estados y tamaños
- Uso: Botones CTA principales en el sitio
- Deps: Ninguna (componente base)

**general-botonesGod2.html** — Segunda versión de botones god con estilos adicionales
- Componentes: variaciones de botones
- Uso: Alternativas de botones principales
- Deps: general-botonesGod.html

**general-botonesGod3.html** — Tercera versión con variaciones extremas
- Componentes: botones experimentales
- Uso: Pruebas de diseño avanzadas
- Deps: general-botonesGod.html

**general-10divisoresDeSecciones.html** — 10 estilos de divisores visuales
- Componentes: líneas, formas, espacios entre secciones
- Uso: Separar secciones de forma visual
- Deps: Ninguna

**general-opcionesAcordeon.html** — Acordeones expandibles básicos
- Componentes: items expandibles, toggle
- Uso: FAQ, detalles ocultables
- Deps: Ninguna (componente base)

**general-formularioDeAsesoria.html** — Formulario de contacto/asesoría reutilizable
- Componentes: inputs, selects, área de texto, CTA
- Uso: Captura de leads, contacto
- Deps: Ninguna

**general-opcionesFormularios.html** — Variaciones de estilos de formularios
- Componentes: múltiples diseños de forms
- Uso: Seleccionar estilo de formulario
- Deps: general-formularioDeAsesoria.html

**general-10opcionesBotonesLinkedin.html** — Diez variaciones de botones estilo LinkedIn
- Componentes: botones con iconografía LinkedIn
- Uso: CTAs conectadas a LinkedIn
- Deps: general-botonesGod.html

**general-opcionesDeBotonesDesplegables.html** — Dropdowns y botones con menú
- Componentes: botones con submenú
- Uso: Navegación secundaria, opciones
- Deps: general-botonesGod.html

**general-10opcionesBullets.html** — 10 estilos de listas de puntos
- Componentes: viñetas, listas con iconografía
- Uso: Listar beneficios, features, requisitos
- Deps: Ninguna

**general-carruselDeImagenesPulido.html** — Carrusel de imágenes (pulido)
- Componentes: carousel, navegación, indicators
- Uso: Galería de fotos, testimonios visuales
- Deps: Ninguna

**general-opcionesDeCarruselDeImagenes.html** — Múltiples variaciones de carruseles
- Componentes: diferentes layouts de carousels
- Uso: Pruebas de diseño de galerías
- Deps: general-carruselDeImagenesPulido.html

**general-opcionesDiseñoHeaders.html** — Múltiples diseños para headers/encabezados
- Componentes: headers alternativos
- Uso: Variantes de encabezados
- Deps: general-headerSitioWeb.html

**general-opcionesfondoHero.html** — Variaciones de fondos para heroes
- Componentes: gradients, imágenes, patrones
- Uso: Estilos de fondo para heros
- Deps: general-hero.html

**general-opcionesColoresVerdes.html** — Paleta de colores verdes para componentes
- Componentes: componentes con tema verde
- Uso: Testeo de tema verde
- Deps: Ninguna

**general-ColoresRojos.html** — Paleta de colores rojos para componentes
- Componentes: componentes con tema rojo
- Uso: Testeo de tema rojo
- Deps: Ninguna

**general-opcionesGradientBackground.html** — Variaciones de gradientes de fondo
- Componentes: gradients CSS
- Uso: Fondos llamativos para secciones
- Deps: Ninguna

**general-opcionesHeroConCards.html** — Hero combinado con cards debajo
- Componentes: hero + grid de cards
- Uso: Sección hero + presentación de opciones
- Deps: general-hero.html, general-opcionesCardsPrograma.html

**general-opcionesParaMostrarPersonas.html** — Cards para perfiles de personas/equipo
- Componentes: cards de personas, avatar, nombre, rol
- Uso: Mostrar equipo docente o staff
- Deps: general-opcionesCardsPrograma.html

**general-pruebaImagenesEnCardsPequeñas.html** — Testeo de imágenes en cards compactas
- Componentes: cards pequeñas con imágenes
- Uso: Pruebas de responsive en cards
- Deps: general-opcionesCardsPrograma.html

**general-tituloRojoParaFormulario.html** — Título rojo destacado para secciones de forms
- Componentes: título estilizado, formulario
- Uso: Sección de conversión con énfasis visual
- Deps: general-formularioDeAsesoria.html

**general-popUpConUrl.html** — Modal/popup con URL embedida
- Componentes: modal dialog, iframe
- Uso: Modales con contenido externo
- Deps: Ninguna

**general-opcionesDeDescuentoEnPrecios.html** — Variaciones de cómo mostrar descuentos
- Componentes: badges de descuento, precios tachados
- Uso: Indicar promociones visualmente
- Deps: general-opcionesBadgeDescuento.html

**general-20opcionesCelularSimple.html** — 20 variaciones simples para móvil
- Componentes: layouts optimizados para celular
- Uso: Testeo de responsive design
- Deps: Ninguna

**general-opcionesBannerBeneficiosDescuentos.html** — Banner promocional de beneficios
- Componentes: banner con beneficios listados
- Uso: Sección promotional sticky o destacada
- Deps: general-opcionesBadge.html

**general-opcionesBannerDescuentos.html** — Banner simple de descuentos
- Componentes: banner con CTA de descuento
- Uso: Promoción destacada
- Deps: general-opcionesBannerBeneficiosDescuentos.html

**general-40opcionesCardsOferta.html** — 40 variaciones de cards de oferta
- Componentes: cards con múltiples opciones de diseño
- Uso: Seleccionar variante de card
- Deps: general-opcionesCardsPrograma.html

**general-badgesParaCards.html** — Badges optimizados para ir sobre cards
- Componentes: badges con posicionamiento
- Uso: Etiquetar cards sin interferir contenido
- Deps: general-opcionesBadge.html

**general-20opcionesAccesosRapidos.html** — 20 variaciones de accesos rápidos
- Componentes: más variantes de shortcuts
- Uso: Pruebas de diseño de navegación rápida
- Deps: general-botonesGod.html

**general-opcionesCardsFinanciacionHorizontal.html** — Cards de financiación en layout horizontal
- Componentes: cards apaisadas (landscape)
- Uso: Mostrar planes lado a lado
- Deps: general-opcionesCardsFinanciacion.html

---

## Opciones Misceláneas

**opciones-reduccionNaranja.html** — Opciones de reducción/descuento con tema naranja
- Componentes: badges o etiquetas de descuento
- Uso: Indicar reducciones de precio
- Deps: general-opcionesBadgeDescuento.html

## Homologación

**homologacion-opciones.html** — Variaciones de componentes para página de homologación
- Componentes: cards, listados, formularios
- Uso: Página de programas de homologación
- Deps: general-opcionesCardsPrograma.html

---

## Inicio (Home)

**inicio-accesosRapidos.html** — Sección de accesos rápidos para home
- Componentes: grid de atajos a secciones clave
- Uso: Navegación rápida en página principal
- Deps: general-10opcionesAccesosRapidos.html

**inicio-accesosRapidos2.html** — Segunda versión de accesos rápidos
- Componentes: layout alternativo de shortcuts
- Uso: Variante de navegación rápida
- Deps: inicio-accesosRapidos.html

**inicio-bannerDescuentoPregradosPosgrados.html** — Banner promocional pregrados vs posgrados
- Componentes: banner comparativo, CTA dual
- Uso: Destacar ofertas en home
- Deps: general-opcionesBannerDescuentos.html

**inicio-bannerDescuentosProgramas.html** — Banner de descuentos en programas generales
- Componentes: banner promocional
- Uso: Sección de ofertas en home
- Deps: general-opcionesBannerDescuentos.html

**inicio-bannerProgramasVirtual.html** — Banner destacando programas virtuales
- Componentes: banner con propuesta de valor virtual
- Uso: Promocionar modalidad virtual
- Deps: general-opcionesBannerDescuentos.html

**inicio-bannerCalendarioYGestion.html** — Banner con calendario y gestión (eventos próximos)
- Componentes: banner con calendario integrado, eventos
- Uso: Mostrar próximas fechas/admisiones
- Deps: general-opcionesBannerBeneficiosDescuentos.html

**inicio-slider-nuevo.html** — Slider/carousel nuevo para home
- Componentes: carousel con múltiples slides
- Uso: Rotación de ofertas principales
- Deps: general-carruselDeImagenesPulido.html

**inicio-slider.html** — Slider estándar para home
- Componentes: carousel principal
- Uso: Galería/rotación en sección hero
- Deps: general-carruselDeImagenesPulido.html

**inicio-proyectoAlprode.html** — Sección proyecto Alprode (institucional)
- Componentes: descripción, imagen, CTA
- Uso: Destacar proyecto/iniciativa especial
- Deps: general-opcionesBadge.html

**inicio-alprode.html** — Versión base de sección Alprode
- Componentes: contenido Alprode
- Uso: Información del proyecto
- Deps: inicio-proyectoAlprode.html

**inicio-alprode-option-geometric.html** — Alprode con diseño geométrico
- Componentes: layout geométrico/moderno
- Uso: Variante visual del proyecto
- Deps: inicio-alprode.html

**inicio-opcionesBannerDescuento.html** — Múltiples opciones de banner descuentos
- Componentes: banners alternativos
- Uso: Pruebas de promoción
- Deps: general-opcionesBannerDescuentos.html

**inicio-beneficioOld.html** — Versión antigua/legacy de sección beneficios
- Componentes: beneficios en layout anterior
- Uso: Referencia histórica
- Deps: Ninguna

---

## Internacionalización

**internacionalizacion-movilidad.html** — Sección de movilidad estudiantil internacional
- Componentes: cards de destinos, testimonios, requerimientos
- Uso: Página de programas de intercambio/movilidad
- Deps: general-opcionesCardsPrograma.html

**internacionalizacion-encasa.html** — Programas internacionales sin salir (en casa)
- Componentes: cards de opciones virtuales/remotas
- Uso: Estudios virtuales con acreditación internacional
- Deps: general-opcionesCardsPrograma.html

**internacionalizacion-inicio.html** — Sección de internacionalización para home
- Componentes: overview de oportunidades internacionales
- Uso: Destaque en página principal
- Deps: internacionalizacion-movilidad.html, internacionalizacion-encasa.html

---

## Posgrados

**posgrados-hero.html** — Hero para página de posgrados
- Componentes: hero, encabezado, CTA
- Uso: Sección superior de page posgrados
- Deps: general-opcionesColoresHero.html

**posgrados-cardsProgramas.html** — Cards de programas de posgrado
- Componentes: cards con modalidad, duración, precio
- Uso: Catálogo de posgrados
- Deps: general-opcionesCardsPrograma.html

**posgrados-bannerFinanciacion.html** — Banner de opciones de financiación
- Componentes: banner con planes de pago
- Uso: Mostrar facilidades de pago
- Deps: general-opcionesCardsFinanciacion.html

**posgrados-pensum.html** — Sección de pensum/plan de estudios
- Componentes: listado de materias, semestres
- Uso: Mostrar currículum detallado
- Deps: general-opcionesPensum.html

**posgrados-internacionalizacion.html** — Sección de oportunidades internacionales en posgrados
- Componentes: cards de intercambio, convenios
- Uso: Destaque de dimensión internacional
- Deps: internacionalizacion-movilidad.html

**posgrados-internacionalizacion-v2.html** — Segunda versión de internacionalización
- Componentes: layout mejorado
- Uso: Variante visual de oportunidades
- Deps: posgrados-internacionalizacion.html

**posgrados-enQuePuedesTrabajar.html** — Sección de salidas laborales para egresados
- Componentes: grid de profesiones, salarios
- Uso: Proyección profesional
- Deps: programas-enQuePuedesTrabajar.html

**posgrados-preguntasFrecuentes.html** — FAQ para posgrados
- Componentes: acordeones
- Uso: Responder dudas comunes
- Deps: general-opcionesAcordeon.html

**posgrados-whyUs.html** — Sección de diferenciales de posgrados
- Componentes: feature list, benefits
- Uso: Mostrar ventajas de estudiar aquí
- Deps: general-diferenciadoresEnListasOCards.html

---

## Pregrados

**pregradosP-hero.html** — Hero para pregrados presenciales
- Componentes: hero, encabezado, CTA
- Uso: Sección superior de page pregrados presenciales
- Deps: general-opcionesColoresHero.html

**pregradosP-cardsProgramas.html** — Cards de programas pregrado presencial
- Componentes: cards con jornadas, facultades
- Uso: Catálogo de pregrados presenciales
- Deps: general-opcionesCardsPrograma.html

**pregradosP-preguntasFrecuentes.html** — FAQ para pregrados presenciales
- Componentes: acordeones
- Uso: Preguntas frecuentes pregrados presenciales
- Deps: general-opcionesAcordeon.html

**pregradosP-stats.html** — Estadísticas/números para pregrados presenciales
- Componentes: tarjetas de estadísticas, números destacados
- Uso: Mostrar cifras de acreditación, egresados, etc.
- Deps: general-opcionesBadge.html

**pregradosV-hero.html** — Hero para pregrados virtuales
- Componentes: hero, encabezado, CTA
- Uso: Sección superior de page pregrados virtuales
- Deps: general-opcionesColoresHero.html

**pregradosV-cardsProgramas.html** — Cards de programas pregrado virtual
- Componentes: cards con indicadores de modalidad virtual
- Uso: Catálogo de pregrados virtuales
- Deps: general-opcionesCardsPrograma.html

**pregradosV-preguntasFrecuentes.html** — FAQ para pregrados virtuales
- Componentes: acordeones con preguntas específicas virtuales
- Uso: FAQ pregrados virtuales
- Deps: general-opcionesAcordeon.html

**pregradosV-stats.html** — Estadísticas para pregrados virtuales
- Componentes: tarjetas de estadísticas
- Uso: Cifras de impacto en modalidad virtual
- Deps: general-opcionesBadge.html

**pregrados-borrador.html** — Versión borrador/experimental de página pregrados
- Componentes: Layout experimental
- Uso: Testeo de diseño
- Deps: pregradosP-hero.html, pregradosV-hero.html

**pregrados-whyUsbajo.html** — Sección "por qué" en versión baja/footer
- Componentes: diferenciales en footer
- Uso: Beneficios antes de cierre
- Deps: general-diferenciadoresEnListasOCards.html

**pregradosV-borradorPagPrograma.html** — Borrador de página de programa virtual
- Componentes: layout completo experimental
- Uso: Testeo de página de programa
- Deps: pregradosV-hero.html

---

## Programas

**programas-hero.html** — Hero genérico para página de programa
- Componentes: hero base
- Uso: Encabezado de programa (flexible)
- Deps: general-opcionesColoresHero.html

**programas-opcionesHero.html** — Múltiples opciones de hero para programas
- Componentes: variaciones de hero
- Uso: Seleccionar estilo
- Deps: programas-hero.html

**programas-cardsProgramas.html** — Cards base para programas
- Componentes: cards de programa
- Uso: Listar programas
- Deps: general-opcionesCardsPrograma.html

**programas-pensum.html** — Sección de pensum/plan de estudios
- Componentes: tabla de materias por semestre
- Uso: Mostrar currículum
- Deps: Ninguna

**programas-pensumBorrador.html** — Borrador de pensum
- Componentes: layout experimental de pensum
- Uso: Testeo
- Deps: programas-pensum.html

**programas-opcionesPensum.html** — Múltiples variaciones de pensum
- Componentes: diferentes layouts de currículum
- Uso: Seleccionar diseño
- Deps: programas-pensum.html

**programas-opcionesPensumEnCel.html** — Pensum optimizado para móvil
- Componentes: pensum responsive
- Uso: Currículum en celular
- Deps: programas-opcionesPensum.html

**programas-pensumConJornadas.html** — Pensum desglosado por jornadas
- Componentes: tabs o segmentos por jornada
- Uso: Mostrar pensum separado por jornada
- Deps: programas-opcionesPensum.html

**programas-pensumVerde.html** — Pensum con tema de color verde
- Componentes: pensum estilizado en verde
- Uso: Variante visual
- Deps: programas-pensum.html

**programas-enQuePuedesTrabajar.html** — Sección de oportunidades laborales
- Componentes: grid de profesiones, salarios
- Uso: Proyección profesional para egresados
- Deps: general-opcionesCardsPrograma.html

**programas-equipoDocentes.html** — Sección de equipo docente
- Componentes: cards de profesores, expertise
- Uso: Mostrar equipo académico
- Deps: general-opcionesParaMostrarPersonas.html

**programas-opcionesCardsJornadas.html** — Cards diferenciadas por jornada
- Componentes: cards con indicador de jornada
- Uso: Mostrar programas por jornada
- Deps: general-opcionesCardsJornadas.html

**programas-opcionesCardsJornadaDiurna.html** — Cards específicas para jornada diurna
- Componentes: cards etiquetadas como diurnas
- Uso: Mostrar solo programas diurnos
- Deps: general-opcionesCardsJornadas.html

**programas-preguntasFrecuentes.html** — FAQ para programas
- Componentes: acordeones
- Uso: Preguntas frecuentes
- Deps: general-opcionesAcordeon.html

**programas-whyUs.html** — Diferenciales del programa
- Componentes: feature list, ventajas
- Uso: Mostrar por qué elegir
- Deps: general-diferenciadoresEnListasOCards.html

---

## Programas A (Alternativa A)

**programasA-hero.html** — Hero alternativo variante A
- Componentes: hero con diseño experimental
- Uso: Prueba de diseño alternativo
- Deps: programas-hero.html

## Programas D (Variante D - Diseño Alterno)

**programasD-hero.html** — Hero variante D
- Componentes: hero con diseño alterno
- Uso: Alternativa visual a hero estándar
- Deps: programas-hero.html

**programasD-bannerFinanciacion.html** — Banner de financiación variante D
- Componentes: banner con planes de pago
- Uso: Opciones de pago
- Deps: posgrados-bannerFinanciacion.html

**programasD-enQuePuedesTrabajar.html** — Salidas laborales variante D
- Componentes: grid de profesiones (diseño alterno)
- Uso: Oportunidades laborales
- Deps: programas-enQuePuedesTrabajar.html

**programasD-pensum.html** — Pensum variante D
- Componentes: currículum con diseño alterno
- Uso: Plan de estudios
- Deps: programas-pensum.html

**programasD-preguntasFrecuentes.html** — FAQ variante D
- Componentes: acordeones (diseño alterno)
- Uso: Preguntas frecuentes
- Deps: programas-preguntasFrecuentes.html

**programasD-whyUs.html** — Diferenciales variante D
- Componentes: ventajas (diseño alterno)
- Uso: Puntos fuertes del programa
- Deps: programas-whyUs.html

---

## Programas P (Presencial)

**programasP-hero.html** — Hero para programas presenciales
- Componentes: hero con énfasis presencial
- Uso: Encabezado de programa presencial
- Deps: programas-hero.html

**programasP-bannerFinanciacionPresencial.html** — Banner de financiación presencial
- Componentes: banner con opciones presencial
- Uso: Pago para modalidad presencial
- Deps: posgrados-bannerFinanciacion.html

**programasP-bannerFinanciacionVirtual.html** — Banner de financiación virtual (en presencial)
- Componentes: banner con opciones virtuales
- Uso: Pago para opción virtual
- Deps: posgrados-bannerFinanciacion.html

**programasP-preguntasFrecuentes.html** — FAQ presencial
- Componentes: acordeones
- Uso: Preguntas presencial
- Deps: programas-preguntasFrecuentes.html

---

## Programas V (Virtual)

**programasV-hero.html** — Hero para programas virtuales
- Componentes: hero con énfasis virtual
- Uso: Encabezado de programa virtual
- Deps: programas-hero.html

---

## Webinars

**webinars-hero.html** — Hero para página de webinars
- Componentes: hero con foco en evento
- Uso: Encabezado de webinars
- Deps: general-opcionesColoresHero.html

**webinars-paginaPrincipal.html** — Página principal de webinars (versión actual)
- Componentes: grid de webinars, filtros
- Uso: Catálogo de webinars
- Deps: webinars-hero.html

**webinars-paginaPrincipalBorrador.html** — Borrador de página principal webinars
- Componentes: layout experimental
- Uso: Testeo de diseño
- Deps: webinars-paginaPrincipal.html

**webinars-formulario.html** — Formulario de registro para webinars
- Componentes: form con campos de webinar
- Uso: Captura de asistentes
- Deps: general-formularioDeAsesoria.html

**webinars-faq.html** — FAQ para webinars
- Componentes: acordeones
- Uso: Preguntas frecuentes sobre webinars
- Deps: general-opcionesAcordeon.html

**webinars-beneficios.html** — Sección de beneficios de webinars
- Componentes: feature list
- Uso: Por qué asistir
- Deps: general-10opcionesBullets.html

**webinars-testimonios.html** — Testimonios de asistentes
- Componentes: cards de testimonios
- Uso: Social proof
- Deps: general-opcionesCardsConMetadata.html

**webinars-sliderTestimonios.html** — Carousel de testimonios
- Componentes: slider de opiniones
- Uso: Rotación de reviews
- Deps: general-carruselDeImagenesPulido.html

---

## Otros

**apliables-pensum.html** — Pensum para programa apliables (similar a apilables)
- Componentes: currículum
- Uso: Plan de estudios apliables
- Deps: programas-pensum.html

**disclaimer-modal.html** — Modal de disclaimer/legal
- Componentes: modal dialog
- Uso: Avisos legales o de privacidad
- Deps: general-popUpConUrl.html

**biblioteca-buscador.html** — Buscador para biblioteca/catálogo
- Componentes: buscador, filtros, resultados
- Uso: Página de búsqueda de recursos
- Deps: general-formularioDeAsesoria.html

**biblioteca-secciones.json** — Configuración JSON de secciones de biblioteca
- Componentes: data structure para secciones
- Uso: Alimentar estructura de biblioteca
- Deps: Ninguna

**pagina.html** — Página genérica/template base
- Componentes: estructura HTML base
- Uso: Plantilla para nuevas páginas
- Deps: general-headerSitioWeb.html

**whatsapp-sticky.html** — Widget flotante de WhatsApp
- Componentes: botón flotante, integración WhatsApp
- Uso: Chat button en esquina
- Deps: Ninguna

**whatsapp-animaciones-entrada.html** — Animaciones de entrada para WhatsApp widget
- Componentes: animaciones CSS
- Uso: Efectos de aparición
- Deps: whatsapp-sticky.html

**whatsapp-animaciones-opciones.html** — Múltiples opciones de animaciones WhatsApp
- Componentes: variaciones de animaciones
- Uso: Seleccionar efecto
- Deps: whatsapp-animaciones-entrada.html

**datosUnis.txt** — Archivo de datos de universidades (texto)
- Componentes: listado de datos
- Uso: Referencia de información
- Deps: Ninguna

---

## Notas Finales

- **Total de archivos**: ~170 HTML + 1 JSON + 1 TXT
- **Temas principales**: 14 (general, programas, pregrados, posgrados, blog, webinars, etc.)
- **Patrón de nombrado**: `[tema]-[tipo]-[opciones].html` (ej: `apilables-hero-opt10.html`)
- **Template de 3-5 líneas**: Propósito + Componentes + Uso + Deps

**Actualización**: 13 de mayo de 2026

Para más información, consulta [README.md](README.md) y [SKILL.md](SKILL.md).
