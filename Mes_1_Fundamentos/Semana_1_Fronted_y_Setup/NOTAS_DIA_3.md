# --- DÍA 3: HTML Semántico y Formularios ---

## 1. ¿Qué es el HTML Semántico?
* Mi definición: Es usar etiquetas de HTML que describen el **significado** del contenido que envuelven, no solo su apariencia. Un `<h1>` dice "esto es el título principal", no solo "texto grande".
* **¿Por qué es importante?** Ayuda a los motores de búsqueda (SEO) y a las tecnologías de asistencia (accesibilidad para personas con discapacidad) a entender la estructura de nuestra página.

## 2. Nuevas Etiquetas Semánticas
* `<header>`: Representa el encabezado de una página o sección. Suele contener el logo y el menú de navegación.
* `<nav>`: Para la sección de navegación principal (menús).
* `<main>`: Define el contenido principal y único del documento. Solo debe haber uno por página.
* `<section>`: Agrupa contenido relacionado temáticamente.
* `<footer>`: Representa el pie de página. Suele tener información de copyright, contacto, etc.

## 3. Formularios HTML
* Mi definición: Son la forma en que los usuarios pueden enviarnos información (un login, un formulario de contacto, una búsqueda).
* `<form>`: La etiqueta que envuelve todo el formulario. El atributo `action` define a dónde se enviarán los datos y `method` cómo (ej. "GET" o "POST").
* `<label>`: Etiqueta de texto para describir un campo del formulario. Es importante por accesibilidad.
* `<input>`: El campo donde el usuario introduce datos. El atributo `type` es muy importante (ej. `type="text"`, `type="email"`, `type="submit"`).
* `<textarea>`: Para campos de texto de múltiples líneas.
* `<button>`: Un botón.