class Vehículo:
    def __init__(self, marca, modelo, año):
        # Atributos básicos
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # Método para mostrar la información del vehículo
    def mostrar_información(self):
        return f"{self.año} {self.marca} {self.modelo}"


# Código principal para probar la clase
if __name__ == "__main__":
    # Crear un objeto Vehículo
    mi_auto = Vehículo("Toyota", "Corolla", 2023)

    # Mostrar la información del vehículo
    print("Información del vehículo:")
    print(mi_auto.mostrar_información())

    # Modificar los atributos directamente (sin getters ni setters)
    print("\nActualizando información del vehículo...")
    mi_auto.marca = "Honda"
    mi_auto.modelo = "Civic"
    mi_auto.año = 2022

    # Mostrar la información actualizada
    print("Información actualizada del vehículo:")
    print(mi_auto.mostrar_información())

