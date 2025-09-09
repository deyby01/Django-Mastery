# --- DÍA 1: Programación Orientada a Objetos (POO) ---

## 1. ¿Qué es la POO?
* **Mi definición:** Es un estilo de programación que se basa en el concepto de "objetos". Nos permite modelar entidades del mundo real (como un Coche, un Usuario, un Producto) con sus características y comportamientos.

## 2. Clases y Objetos
* **Clase:** Es el **plano** o la **plantilla** para crear objetos. Define qué atributos (datos) y métodos (funciones) tendrán los objetos de ese tipo.
    * *Analogía:* El plano de una casa.
* **Objeto (o Instancia):** Es una **copia** creada a partir de una clase. Es la entidad real y tangible con la que trabajas en tu programa.
    * *Analogía:* La casa construida a partir del plano. Puedes construir muchas casas (objetos) desde un solo plano (clase).

## 3. Atributos y Métodos
* **Atributos:** Son las **características** o datos de un objeto. Son como las variables que pertenecen a una clase. (Ej: para una clase `Coche`, los atributos podrían ser `color`, `marca`, `velocidad`).
* **Métodos:** Son las **acciones** o comportamientos que un objeto puede realizar. Son como las funciones que pertenecen a una clase. (Ej: para un `Coche`, los métodos podrían ser `acelerar()`, `frenar()`).

## 4. `__init__` y `self`
* **`__init__(self, ...)`:** Es un método especial llamado **constructor**. Se ejecuta automáticamente **una sola vez** cuando creas un nuevo objeto a partir de la clase. Su trabajo principal es inicializar los atributos del objeto.
* **`self`:** Es una variable especial que representa la **instancia del objeto mismo**. Se usa dentro de la clase para acceder a sus propios atributos y métodos (ej: `self.marca`, `self.acelerar()`). Siempre es el primer parámetro de cualquier método de una clase.