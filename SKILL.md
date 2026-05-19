## Propósito
Definir reglas estrictas para generar o modificar componentes HTML y CSS con estructura limpia, semántica correcta y estilos modularizados.

---

## Flujo de Trabajo

1. Analizar la estructura base proporcionada.
   - Si existe un archivo de referencia (ej. `pregradosP-hero.html`), replicar estrictamente la lógica estructural de grid o flexbox.
   - No heredar estilos visuales, efectos o decisiones gráficas no solicitadas.

2. Generar HTML semántico.
   - Utilizar etiquetas correctas según el contenido y la jerarquía.
   - Evitar el abuso de `div`.

3. Aplicar estilos del componente.
   - Escribir únicamente el CSS necesario.
   - Mantener estilos scopeados al componente.
   - Evitar dependencias globales.

---

## Reglas de Estructura y Semántica

- Utilizar etiquetas semánticas reales cuando correspondan:
  `header`, `main`, `section`, `article`, `nav`, `aside`, `footer`, `figure`, `picture`, `button`, `a`, `form`, `ul`, `li`, etc.

- Mantener jerarquía correcta de encabezados (`h1` → `h6`).

- No convertir toda la estructura en contenedores genéricos.

- Cada bloque debe tener una responsabilidad clara y una estructura fácil de leer.

- Evitar anidaciones innecesarias.

---

## Restricciones de Diseño

### Color
- No utilizar variables globales de color.
- Utilizar valores hexadecimales directos o variables estrictamente locales al componente.

### Transformaciones
- Prohibido usar `transform` en botones a menos de que se pida explícitamente o se pidan opciones de diseño, incluyendo:
  - `scale`
  - `translate`
  - `rotate`

### Sombras
- Prohibido usar `box-shadow` a menos de que se solicite o se pidan opciones de diseño.

### Degradados
- Prohibido usar `gradient` en botones, fondos o imágenes salvo que se solicite explícitamente o se pidan opciones de diseño.

### Estados Interactivos
Todo botón o elemento interactivo debe incluir:
- Estado default claramente identificable.
- Estado `:hover` con cambio visual evidente.
- Estado `:active` con feedback visual claro.
- Transiciones con `!important` para compatibilidad con WordPress.

---

## Tipografía y Contenido

- Priorizar títulos con peso visual fuerte (`700`, `800`, `900`) cuando el diseño lo requiera.

- Mantener buena legibilidad y contraste.

- Cuando el contenido sea promocional o comercial:
  - usar copy persuasivo,
  - enfocado en conversión,
  - beneficios claros,
  - y llamados a la acción directos.

## Font Weight en Móvil (WordPress + Elementor)

**Problema:** En WordPress + Elementor, los `font-weight` no se aplican correctamente en celulares aunque se vean bien en desktop.

**Solución:**
1. **NO usar `font-family: inherit`** - siempre especificar la familia completa
2. **ESPECIFICAR `font-weight` en media queries** - aunque sea el mismo valor que en desktop, es necesario re-declararlo en móvil para que se aplique
3. **Font stack completo cuando se pierden fuentes:**

```css
.elemento {
  font-weight: 900 !important;
  font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
  text-rendering: optimizeLegibility;
}

@media (max-width: 768px) {
  .elemento {
    font-weight: 900 !important;
  }
}
```

**Por qué funciona:** Elementor inyecta CSS que sobrescribe estilos. Al re-declarar el peso en el media query, aseguramos que se aplique en móvil.

---

## Convenciones de CSS

- Usar clases semánticas, descriptivas y scopeadas al componente.

## SVG en WordPress

Los SVGs para WordPress deben estar controlados por CSS para garantizar compatibilidad:

**HTML:**
```html
<svg viewBox="0 0 24 24">
  <path d="..."/>
  <line x1="..." y1="..." x2="..." y2="..."/>
</svg>
```

**CSS:**
```css
svg {
  width: 24px;
  height: 24px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

/* Para SVGs que usan relleno sólido y no líneas (ej. FontAwesome, Ionicons solid) */
svg.icon-filled {
  fill: currentColor !important;
  stroke: none !important;
}
```

**Importante:**
- OBLIGATORIO usar `!important` en las propiedades de `fill`, `stroke` y `stroke-width` en los svgs importados para que WordPress/Elementor no sobrescriba nuestros colores en los íconos integrados.
- No incluir atributos de estilo en el SVG mismo (evita `style="..."`).
- El `viewBox` es el único atributo necesario en el tag `<svg>`.
- Usar CSS para definir tamaño, stroke, fill y atributos de línea.
- Esto permite que los estilos se hereden correctamente del contenedor padre.

## Imágenes en WordPress + Elementor

Elementor filtra agresivamente los `<img>` tags generados dinámicamente por JavaScript, pero respeta las propiedades CSS. Para imágenes dinámicas o responsive:

**Usar background-image en lugar de img tags:**

**HTML:**
```html
<div class="image-container" 
     style="background-image: url('url-desktop');" 
     data-mobile="url-mobile">
  <div class="overlay-content"><!-- Si necesitas contenido sobre la imagen --></div>
</div>
```

**CSS:**
```css
.image-container {
  width: 100%;
  height: 200px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
```

**JavaScript (para responsive):**
```javascript
function updateBackgroundImages() {
  const isMobile = window.innerWidth <= 767;
  const containers = document.querySelectorAll('.image-container');
  
  containers.forEach(container => {
    if (isMobile && container.dataset.mobile) {
      container.style.backgroundImage = `url('${container.dataset.mobile}')`;
    } else if (!isMobile && container.dataset.desktop) {
      container.style.backgroundImage = `url('${container.dataset.desktop}')`;
    }
  });
}

window.addEventListener('resize', updateBackgroundImages);
document.addEventListener('DOMContentLoaded', updateBackgroundImages);
```

**Cuándo usar:**
- Imágenes generadas dinámicamente en JavaScript
- Componentes con switching responsive (desktop/mobile diferentes)
- Cuando Elementor u otro CMS filtra img tags
- Cards, héroes, galerías dinámicas

**Ventajas:**
- Evita filtrado de Elementor
- Controla responsive sin depender de display:none/block
- Mejor integración con CMS restrictivos

## Botones en Mobile

Para evitar que los botones muestren color azul cuando se presionan (estado `:active`) o se enfocan (`:focus`):

**CSS:**
```css
.button {
  outline: none;  /* Elimina outline */
  -webkit-tap-highlight-color: transparent;  /* Elimina highlight en iOS */
}

.button:focus {
  outline: none !important;
}

.button:focus-visible {
  outline: none !important;
}

.button:active:not(.active) {
  /* Define el estilo cuando se presiona un botón que NO está activo */
  background-color: /* color original */;
  color: /* color texto original */;
  border-color: /* color border original */;
}
```

**Por qué funciona:**
- `outline: none` elimina el outline por defecto
- `-webkit-tap-highlight-color: transparent` elimina el highlight en iOS Safari
- `:focus` y `:focus-visible` se anidan para máxima compatibilidad
- `:active:not(.active)` evita cambios de color al presionar botones inactivos
- Sin restricciones de `box-shadow`, puedes agregar sombras en cualquier estado sin conflictos

**Agregar sombra en estados específicos:**
```css
.button:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.button.active {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}
```

## Arrays de Datos con IDs por Categoría

Cuando trabajas con arrays dinámicos de elementos categorizados (tabs, secciones, etc.), usa IDs locales por categoría en lugar de IDs globales. Esto facilita mantenimiento y permite agregar elementos sin romper la numeración.

**Estructura recomendada:**
```javascript
const data = [
  // TAB 1 (6 items) | id: 1-6
  { id: 1, tab: 1, nombre: "Item 1" },
  { id: 2, tab: 1, nombre: "Item 2" },
  ...
  { id: 6, tab: 1, nombre: "Item 6" },
  
  // TAB 2 (4 items) | id: 1-4
  { id: 1, tab: 2, nombre: "Item 1" },
  { id: 2, tab: 2, nombre: "Item 2" },
  ...
  { id: 4, tab: 2, nombre: "Item 4" },
  
  // TAB 3 (3 items) | id: 1-3
  { id: 1, tab: 3, nombre: "Item 1" },
  { id: 2, tab: 3, nombre: "Item 2" },
  { id: 3, tab: 3, nombre: "Item 3" },
];
```

**Ventajas:**
- IDs locales reseteados por categoría
- Fácil de mantener (cada tab es independiente)
- Al agregar un elemento, solo numerase dentro de su tab
- Visualmente claro en el código
- Escalable sin conflictos

**Cómo agregar un elemento:**
```javascript
// Agregar a TAB 1 (de 6 items a 7 items)
{ id: 7, tab: 1, nombre: "Item 7" },

// Agregar a TAB 2 (de 4 items a 5 items)
{ id: 5, tab: 2, nombre: "Item 5" },
```

Sin necesidad de renumerar todos los IDs anteriores.

## Limpieza de Código (CRÍTICO)
- **Sin Comentarios Innecesarios:** Omite o elimina toda clase de comentarios descriptivos (<!-- formulario -->, /* estilos del botón */, etc.) para entregar un archivo 100% magro.

### Correcto
```css
.continuing-education-hero__content
.course-benefits-card
.registration-form__submit-button
```

### Incorrecto
```css
.container
.box
.red-text
.button2
```