# IMPORTANTE: Este archivo corresponde al dia 2.

# --- CLASE PADRE (la misma de ayer) ---
class Coche:
    def __init__(self, marca_coche, modelo_coche, color_coche):
        self.marca = marca_coche
        self.modelo = modelo_coche
        self.color = color_coche
        self.encendido = False
        print(f"¡Se ha creado un coche base: {self.marca} {self.modelo}!")

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El coche ya estaba encendido.")

    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"Estado del {self.marca} {self.modelo}: está {estado}.")


# --- CLASE HIJA (¡Aquí está la herencia!) ---
# CocheElectrico hereda de Coche
class CocheElectrico(Coche):
    # El constructor ahora acepta un nuevo atributo: la capacidad de la batería
    def __init__(self, marca_coche, modelo_coche, color_coche, capacidad_bateria):
        # 1. Llamamos al constructor de la CLASE PADRE (Coche) para que
        #    inicialice marca, modelo, color, etc.
        super().__init__(marca_coche, modelo_coche, color_coche)

        # 2. Ahora añadimos el nuevo atributo que solo tienen los coches eléctricos
        self.bateria_kwh = capacidad_bateria
        print(f"¡Es un modelo eléctrico con una batería de {self.bateria_kwh} kWh!")

    # Podemos añadir métodos nuevos que solo existen en la clase hija
    def cargar_bateria(self):
        print(f"Cargando la batería de {self.bateria_kwh} kWh del {self.marca} {self.modelo}...")


# --- Programa Principal ---

print("--- Creando un coche de combustión ---")
mi_toyota = Coche("Toyota", "Camry", "Plata")
mi_toyota.encender()

print("\n--- Creando un coche eléctrico ---")
mi_tesla = CocheElectrico("Tesla", "Model 3", "Blanco", 75)

# Podemos usar métodos HEREDADOS de la clase Coche
mi_tesla.encender()
mi_tesla.mostrar_estado()

# Y también podemos usar métodos PROPIOS de la clase CocheElectrico
mi_tesla.cargar_bateria()