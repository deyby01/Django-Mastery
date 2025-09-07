# --- DÍA 5: Funciones en Python ---

## 1. ¿Qué es una Función?
* **Mi definición:** Es un bloque de código organizado y reutilizable que realiza una tarea específica. Se le da un nombre y se le puede "llamar" cuando se necesite.
* **Analogía:** Es como una receta de cocina. La defines una vez (`def receta_pastel(...)`), y cada vez que quieres un pastel, simplemente sigues la receta (`receta_pastel()`) en lugar de reescribir todos los pasos.

## 2. Partes de una Función
* **Definición (`def`):** Se usa la palabra clave `def` para decirle a Python que estamos creando una función.
* **Nombre:** Un nombre descriptivo que indica lo que hace la función (ej. `saludar`, `calcular_total`).
* **Parámetros (o Argumentos):** Son las "entradas" o la información que le pasas a la función para que trabaje. Van entre paréntesis `()`. Son opcionales.
* **Cuerpo:** El bloque de código indentado que contiene las instrucciones que la función ejecuta.
* **Retorno (`return`):** La palabra clave `return` se usa para que la función "devuelva" un resultado. Es la "salida" de la función. También es opcional.

## 3. Ejemplo
```python
# Definición de la función con dos parámetros
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado # Devuelve el resultado

# Llamada a la función y guardado del valor de retorno
total = sumar(5, 10)
print(total) # Imprimirá 15
```

---

**Meta Práctica de Hoy**

Tu misión es **refactorizar**. Esto significa tomar código que ya funciona y mejorarlo, en este caso, organizándolo en funciones. Vamos a tomar la lógica de tus scripts anteriores y la encapsularemos.

1.  **Edita el archivo `refactor.py`:**
    Abre el archivo y escribe el siguiente código. Crearemos una función para el saludo y otra para el juego de adivinar el número.

    ```python
    # --- Función para el Saludo (Día 2) ---
    def ejecutar_saludo():
        """
        Esta función pide el nombre y la edad al usuario y muestra un saludo.
        """
        print("--- Iniciando Módulo de Saludo ---")
        nombre_usuario = input("Por favor, introduce tu nombre: ")
        edad_texto = input("Ahora, introduce tu edad: ")
        
        # Validamos que la entrada sea un número antes de convertir
        if edad_texto.isdigit():
            edad_numero = int(edad_texto)
            print(f"¡Hola, {nombre_usuario}! Tienes {edad_numero} años.")
        else:
            print("Entrada de edad no válida. Por favor, introduce un número.")
        print("--- Fin Módulo de Saludo ---\n")


    # --- Función para el Juego (Día 3) ---
    def jugar_adivina_el_numero():
        """
        Esta función ejecuta el juego de adivinar el número.
        """
        print("--- Iniciando Juego: Adivina el Número ---")
        numero_secreto = 7
        intento_usuario = 0

        while intento_usuario != numero_secreto:
            intento_texto = input("Adivina el número (entre 1 y 10): ")
            
            if not intento_texto.isdigit():
                print("Por favor, introduce un número válido.")
                continue # Vuelve al inicio del bucle

            intento_usuario = int(intento_texto)

            if intento_usuario < numero_secreto:
                print("¡Demasiado bajo!")
            elif intento_usuario > numero_secreto:
                print("¡Demasiado alto!")
            else:
                print(f"¡Felicidades! ¡Has adivinado que el número era {numero_secreto}!")
        
        print("--- Fin del Juego ---\n")


    # --- Programa Principal ---
    # Ahora, simplemente llamamos a las funciones para ejecutar el código.
    # Esto hace que el flujo del programa sea mucho más fácil de leer.

    ejecutar_saludo()
    jugar_adivina_el_numero()

    print("¡Programa finalizado con éxito!")
    ```

2.  **Ejecuta tu Script:**
    Guarda el archivo y ejecútalo desde la terminal.

    ```bash
    python refactor.py
    ```

Observa cómo el código principal al final del archivo es ahora muy corto y legible. Simplemente "llama" a las herramientas que has creado. Esta es la base del código limpio y mantenible. ¡Gran trabajo!