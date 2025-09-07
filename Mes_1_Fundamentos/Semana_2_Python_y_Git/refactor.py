# IMPORTANTE: Este archivo corresponde a las notas del dia 4

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