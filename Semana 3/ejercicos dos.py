class Vehículo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_información(self):
        return f"{self.año} {self.marca} {self.modelo}"

    def encender(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

    def apagar(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")