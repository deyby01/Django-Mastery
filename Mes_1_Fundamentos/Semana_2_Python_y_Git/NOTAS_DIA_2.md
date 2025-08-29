# --- DÍA 2: Fundamentos de Python (Parte 1) ---

## 1. Variables
* **Mi definición:** Son contenedores con un nombre donde guardamos datos para usarlos más tarde.
* **Analogía:** Como una caja con una etiqueta. La etiqueta es el nombre de la variable y lo que hay dentro es el valor. `nombre = "Juan"`

## 2. Tipos de Datos
* **String (str):** Cadenas de texto. Siempre van entre comillas simples `' '` o dobles `" "`. Ej: `"Hola Mundo"`.
* **Integer (int):** Números enteros, sin decimales. Ej: `25`, `-10`.
* **Float:** Números de punto flotante, con decimales. Ej: `3.14`, `9.99`.
* **Boolean (bool):** Representan un valor de verdad. Solo pueden ser `True` o `False`.

## 3. Operadores
* **Aritméticos:** Para hacer matemáticas (`+` suma, `-` resta, `*` multiplicación, `/` división).
* **De asignación:** El más común es `=` para asignar un valor a una variable.
* **De comparación:** Para comparar valores. Devuelven un booleano (`True` o `False`). Ej: `==` (igual a), `!=` (no es igual a), `>` (mayor que), `<` (menor que).

## 4. Entrada y Salida
* **`print()`:** Una función para mostrar información en la terminal.
* **`input()`:** Una función que muestra un mensaje y espera a que el usuario escriba algo y presione Enter. **¡Importante!** `input()` siempre devuelve los datos como un **string**. Si necesitas un número, debes convertirlo.