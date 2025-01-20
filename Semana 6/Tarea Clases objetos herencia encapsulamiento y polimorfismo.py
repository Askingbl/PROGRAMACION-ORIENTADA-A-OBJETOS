# Clase base: Medicina
class Medicina:
    def __init__(self, nombre, precio, fabricante):
        self.nombre = nombre  # Atributo público
        self.__precio = precio  # Atributo privado (encapsulación)
        self.fabricante = fabricante

    # Método para obtener el precio (getter)
    def obtener_precio(self):
        return self.__precio

    # Método para establecer el precio (setter)
    def establecer_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a cero.")

    # Método público
    def descripcion(self):
        return f"{self.nombre}, fabricado por {self.fabricante}, cuesta ${self.__precio:.2f}."

# Clase derivada: Antibiotico (herencia)
class Antibiotico(Medicina):
    def __init__(self, nombre, precio, fabricante, espectro):
        super().__init__(nombre, precio, fabricante)  # Llamada al constructor de la clase base
        self.espectro = espectro

    # Método sobrescrito (polimorfismo)
    def descripcion(self):
        return f"{self.nombre} es un antibiótico de espectro {self.espectro}, fabricado por {self.fabricante}."

# Clase derivada: Analgesico (herencia)
class Analgesico(Medicina):
    def __init__(self, nombre, precio, fabricante, tipo):
        super().__init__(nombre, precio, fabricante)
        self.tipo = tipo

    # Método sobrescrito (polimorfismo)
    def descripcion(self):
        return f"{self.nombre} es un analgésico de tipo {self.tipo}, fabricado por {self.fabricante}."

# Código principal para demostrar funcionalidad
if __name__ == "__main__":
    # Crear instancia de Medicina (clase base)
    medicina_base = Medicina("Paracetamol", 5.50, "PharmaCorp")
    print(medicina_base.descripcion())

    # Encapsulación: cambiar el precio usando el setter
    medicina_base.establecer_precio(6.00)
    print("Nuevo precio:", medicina_base.obtener_precio())

    # Crear instancia de Antibiotico (clase derivada)
    antibiotico = Antibiotico("Amoxicilina", 12.00, "BioLab", "amplio")
    print(antibiotico.descripcion())

    # Crear instancia de Analgesico (clase derivada)
    analgesico = Analgesico("Ibuprofeno", 8.50, "HealthCare Inc.", "antiinflamatorio")
    print(analgesico.descripcion())

    # Polimorfismo: llamar al método descripcion de diferentes clases
    lista_medicinas = [medicina_base, antibiotico, analgesico]
    print("\nDemostración de polimorfismo:")
    for medicina in lista_medicinas:
        print(medicina.descripcion())
