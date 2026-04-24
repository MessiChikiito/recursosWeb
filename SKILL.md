# Componentes UI (Educación Continua)

## Propósito
Reglas base al generar o modificar código HTML y CSS para landing pages, pregrados y cursos.

## Flujo de Trabajo
1. **Análisis de la Estructura Base:** Si se da un archivo de referencia (ej. pregradosP-hero.html), calcar estrictamente su maquetación de grid o flexbox sin heredar estilos de diseño no deseados.
2. **Generación del Marcado:** Crear un HTML semántico.
3. **Aplicación de Estilos:** Escribir el CSS necesario en el mismo bloque usando selectores propios (scope modular).

## Restricciones y Directrices de Diseño
- **No uses variables de colores globales:** Emplea valores hexadecimales directamente para cada color, sin depender de clases genéricas.
- **Sin Sombras (Shadow boxes):** Totalmente prohibido el uso de ox-shadow en los contenedores.
- **Sin Transformaciones (Transforms):** No utilices 	ransform: scale(...) ni similares en estados como :hover.
- **Sin Degradados (Gradients):** Especialmente en botones e imágenes. Utiliza colores planos (flat colors).
- **Textos de Marketing:** Crea copys con peso persuasivo, enfocados en el valor a aportar (ventas, inscríbete).
- **Énfasis Textual:** Usa pesos tipográficos elevados (ej. ont-weight: 800 o 900) para títulos o mensajes clave.

## Limpieza de Código (CRÍTICO)
- **Sin Comentarios Innecesarios:** Omite o elimina toda clase de comentarios descriptivos (<!-- formulario -->, /* estilos del botón */, etc.) para entregar un archivo 100% magro.
