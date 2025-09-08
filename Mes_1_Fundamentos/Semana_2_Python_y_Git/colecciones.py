# IMPORTANTE: Este archivo corresponde a las notas del dia 5

# Usamos un DICCIONARIO para representar al usuario y sus propiedades.
perfil_usuario = {
    "nombre": "Alex",
    "edad": 30,
    "desarrollador": True,
    "ciudad": "Ciudad Código"
}

# Usamos una LISTA para guardar sus hobbies, ya que pueden cambiar.
hobbies = ["Programar en Django", "Leer sobre tecnología", "Hacer café"]

# Añadimos la lista de hobbies al diccionario del perfil.
perfil_usuario["hobbies"] = hobbies

# Usamos una TUPLA para guardar las redes sociales, asumiendo que no cambiarán.
redes_sociales = ("@alex_dev", "/in/alexdev")
perfil_usuario["redes_sociales"] = redes_sociales

# --- Ahora vamos a mostrar la información de forma ordenada ---

print("--- Perfil del Usuario ---")

# Accedemos a los valores del diccionario usando sus claves.
print(f"Nombre: {perfil_usuario['nombre']}")
print(f"Edad: {perfil_usuario['edad']}")

# Mostramos los hobbies iterando sobre la lista con un bucle FOR.
print("Hobbies:")
for hobby in perfil_usuario['hobbies']:
    # El print con indentación pertenece al bucle for
    print(f"- {hobby}")

print("-------------------------")