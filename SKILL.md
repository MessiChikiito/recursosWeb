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
```

**Importante:**
- No incluir atributos de estilo en el SVG mismo.
- El `viewBox` es el único atributo necesario en el tag `<svg>`.
- Usar CSS para definir tamaño, stroke, fill y atributos de línea.
- Esto permite que los estilos se hereden correctamente del contenedor padre.

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