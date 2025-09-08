# --- DÍA 4: Estructuras de Datos en Python ---

## 1. Listas (`list`)
* **Mi definición:** Son colecciones **ordenadas** y **modificables** de elementos. Se crean con corchetes `[]`.
* **Características:**
    * Los elementos tienen un orden y se accede a ellos por su índice (empezando en 0). `mi_lista[0]` es el primer elemento.
    * Puedes añadir, quitar o cambiar elementos después de crearla.
* **Analogía:** Una lista de compras. Puedes añadir cosas, tachar otras y el orden en que las apuntas se mantiene.
* **Métodos comunes:** `.append()` (añadir al final), `.pop()` (quitar del final), `len()` (saber cuántos elementos tiene).

## 2. Tuplas (`tuple`)
* **Mi definición:** Son colecciones **ordenadas** e **inmutables** de elementos. Se crean con paréntesis `()`.
* **Características:**
    * Son como las listas, pero una vez creadas, **no se pueden modificar**. Ni añadir, ni quitar, ni cambiar elementos.
    * Son más rápidas y seguras para datos que no deben cambiar.
* **Analogía:** Las coordenadas de un mapa (latitud, longitud). Una vez definidas, no deberían cambiar.

## 3. Diccionarios (`dict`)
* **Mi definición:** Son colecciones **desordenadas** (en versiones antiguas de Python) y **modificables** de pares **clave-valor**. Se crean con llaves `{}`.
* **Características:**
    * No usas un índice numérico para acceder a los datos, sino una `clave` única (que suele ser un string). `mi_dict['nombre']`.
    * Son extremadamente útiles para representar objetos del mundo real con sus propiedades.
* **Analogía:** Un diccionario de verdad o la agenda de un teléfono. Buscas por una palabra (`clave`) para encontrar su definición (`valor`).