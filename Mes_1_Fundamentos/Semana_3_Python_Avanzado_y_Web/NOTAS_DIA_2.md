# --- DÍA 2: Herencia en POO ---

## 1. ¿Qué es la Herencia?
* **Mi definición:** Es un mecanismo que permite a una nueva clase (llamada **subclase** o **clase hija**) adquirir los atributos y métodos de una clase existente (llamada **superclase** o **clase padre**).
* **Principal Ventaja:** Reutilización de código. No tienes que escribir lo mismo una y otra vez. Es la base del principio DRY (Don't Repeat Yourself).

## 2. Sintaxis de la Herencia
* Para indicar que una clase hereda de otra, se pone el nombre de la clase padre entre paréntesis en la definición de la clase hija.
* `class CocheElectrico(Coche):` significa: "La clase `CocheElectrico` es un tipo de `Coche` y hereda todo de él".

## 3. La Función `super()`
* **`super()`** es una función especial que te da acceso a los métodos de la clase padre.
* El uso más común es en el `__init__` de la clase hija para llamar al `__init__` de la clase padre. Esto asegura que todos los atributos del padre se inicialicen correctamente antes de añadir los nuevos atributos de la hija.
* `super().__init__(marca, modelo, color)`