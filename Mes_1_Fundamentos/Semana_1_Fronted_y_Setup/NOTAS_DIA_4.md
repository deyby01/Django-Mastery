# --- DÍA 4: Introducción a CSS ---

## 1. ¿Qué es CSS?
* Mi definición: Es el lenguaje de diseño que le da estilo a nuestro HTML. Se encarga de "cómo se ven" las cosas (colores, fuentes, tamaños, espaciado). HTML es el esqueleto, CSS es la ropa.

## 2. ¿Cómo se conecta CSS con HTML?
* Se usa la etiqueta `<link>` dentro del `<head>` del archivo HTML.
* Ejemplo: `<link rel="stylesheet" href="estilos.css">`
    * `rel="stylesheet"`: Le dice al navegador que es una hoja de estilos.
    * `href="estilos.css"`: Es la ruta al archivo CSS que queremos usar.

## 3. La Regla Básica de CSS: Selector y Declaración
* **Selector:** Apunta al elemento HTML al que quieres darle estilo (ej. `h1`, `p`, `.una-clase`).
* **Declaración:** Contiene la propiedad y el valor del estilo a aplicar (ej. `color: blue;`). Va entre llaves `{}`.
* Ejemplo Completo: `h1 { color: blue; font-size: 24px; }`

## 4. Tipos de Selectores (los básicos)
* **Por Etiqueta:** Selecciona todas las etiquetas de un tipo. Ejemplo: `p { ... }`
* **Por Clase:** Selecciona todos los elementos que tengan el atributo `class="nombre-clase"`. Se usa un punto `.` en CSS. Ejemplo: `.destacado { ... }`
* **Por ID:** Selecciona el ÚNICO elemento que tenga el atributo `id="nombre-id"`. Se usa una almohadilla `#` en CSS. Ejemplo: `#titulo-principal { ... }`

## 5. Propiedades Comunes que Aprendí Hoy
* `color`: Color del texto.
* `background-color`: Color del fondo de un elemento.
* `font-size`: Tamaño del texto.
* `font-family`: Tipo de letra (ej. Arial, Helvetica, sans-serif).
* `margin`: Espacio POR FUERA del borde de un elemento.
* `padding`: Espacio POR DENTRO del borde de un elemento.
* `border`: Define un borde para el elemento (ej. `1px solid black`).