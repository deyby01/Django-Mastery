# IMPORTANTE: Este archivo corresponde al dia 1.

# 1. Definimos la Clase (el plano)
class Coche:
    # 2. El método constructor __init__
    # Se ejecuta al crear un nuevo objeto Coche
    def __init__(self, marca_coche, modelo_coche, color_coche):
        # 3. Atributos de instancia
        # Usamos 'self' para guardar los datos específicos de este objeto
        self.marca = marca_coche
        self.modelo = modelo_coche
        self.color = color_coche
        self.encendido = False # Por defecto, el coche empieza apagado
        print(f"¡Se ha creado un {self.marca} {self.modelo} de color {self.color}!")

    # 4. Métodos (acciones que el objeto puede hacer)
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("¡Oye! El coche ya estaba encendido.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"Estado del {self.marca} {self.modelo}: está {estado}.")


# --- Programa Principal ---

# 5. Creamos Objetos (instancias) a partir de la clase Coche
print("Creando mi primer coche...")
mi_coche = Coche("Toyota", "Corolla", "Rojo")

print("\nCreando el coche de un amigo...")
coche_amigo = Coche("Ford", "Mustang", "Negro")

# 6. Interactuamos con los objetos llamando a sus métodos
print("\n--- Interactuando con mi coche ---")
mi_coche.mostrar_estado()  # Debería estar apagado
mi_coche.encender()        # Lo encendemos
mi_coche.mostrar_estado()  # Ahora debería estar encendido
mi_coche.encender()        # Intentamos encenderlo de nuevo

print("\n--- Interactuando con el coche de mi amigo ---")
coche_amigo.mostrar_estado() # Sigue apagado, no le afecta lo que le pasa a mi_coche