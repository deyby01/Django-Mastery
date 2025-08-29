# IMPORTANTE: Este archivo pertenece al dia 3.

# 1. Definimos el número secreto que el usuario debe adivinar.
numero_secreto = 7

# 2. Inicializamos una variable para guardar el intento del usuario.
#    La iniciamos en None o en un número que no sea el secreto.
intento_usuario = 0

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 10. ¡Intenta adivinarlo!")

# 3. Iniciamos un bucle que se repetirá MIENTRAS el intento no sea el correcto.
while intento_usuario != numero_secreto:

    # 4. Pedimos al usuario que introduzca un número.
    intento_texto = input("Tu adivinanza: ")
    intento_usuario = int(intento_texto)

    # 5. Usamos condicionales para dar pistas.
    if intento_usuario < numero_secreto:
        print("¡Demasiado bajo! Intenta de nuevo.")
    elif intento_usuario > numero_secreto:
        print("¡Demasiado alto! Intenta de nuevo.")
    else:
        # Si no es ni menor ni mayor, ¡es que ha acertado!
        print(f"¡Felicidades! ¡Has adivinado que el número era {numero_secreto}!")

print("¡Fin del juego!")