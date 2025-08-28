# --- DÍA 5: Modelo de Caja y Flexbox ---

## 1. El Modelo de Caja (Box Model)
* **Mi definición:** Es la idea de que cada elemento en HTML es una caja rectangular. Esta caja está compuesta por cuatro capas, de adentro hacia afuera:
    1.  **Contenido (Content):** El texto, la imagen, etc.
    2.  **Relleno (Padding):** Un espacio transparente alrededor del contenido, dentro del borde.
    3.  **Borde (Border):** La línea que puede rodear al padding y al contenido.
    4.  **Margen (Margin):** Un espacio transparente por fuera del borde, que separa esta caja de otras cajas.
* **Analogía:** Imagina un cuadro. El **contenido** es la foto, el **padding** es el paspartú o cartón blanco entre la foto y el marco, el **borde** es el marco de madera, y el **margen** es la distancia entre ese cuadro y otro cuadro en la pared.

## 2. Flexbox
* **Mi definición:** Es un modelo de diseño en CSS que nos permite alinear y distribuir el espacio entre los elementos de un contenedor de forma fácil y "flexible".
* **Conceptos clave:**
    * **Contenedor Flex (Flex Container):** Es el elemento padre al que le aplicamos `display: flex;`.
    * **Ítems Flex (Flex Items):** Son los hijos directos del contenedor, que ahora se pueden alinear.

## 3. Propiedades de Flexbox (para el contenedor)
* `display: flex;`: ¡Activa la magia de Flexbox!
* `justify-content:`: Alinea los ítems horizontalmente (ej. `center`, `space-between`, `flex-end`).
* `align-items:`: Alinea los ítems verticalmente (ej. `center`).
* `flex-direction:`: Define la dirección de los ítems (`row` es por defecto, `column` los apila).