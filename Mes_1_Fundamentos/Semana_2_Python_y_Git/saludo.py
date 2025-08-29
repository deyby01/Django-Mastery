# IMPORTANTE: Este archivo va vinculado con el dia 2.


# 1. Pedimos el nombre al usuario y lo guardamos en una variable.
nombre_usuario = input("Por favor, introduce tu nombre: ")

# 2. Pedimos la edad. input() la guardará como texto.
edad_texto = input("Ahora, introduce tu edad: ")

# 3. Convertimos la edad de texto a un número entero.
edad_numero = int(edad_texto)

# 4. Mostramos un saludo personalizado usando una f-string.
print(f"¡Hola, {nombre_usuario}! Es un gusto conocerte.")
print(f"Veo que tienes {edad_numero} años. ¡Excelente!")

# 5. Usamos un operador para un pequeño cálculo.
edad_futura = edad_numero + 10
print(f"En 10 años, tendrás {edad_futura} años.")