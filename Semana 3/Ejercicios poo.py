class ClimaDiario:
    """Clase que representa la información diaria del clima."""
    def __init__(self, temperatura=0.0):
        self.__temperatura = temperatura  # Encapsulación de temperatura

    def set_temperatura(self, temperatura):
        """Método para establecer la temperatura diaria."""
        self.__temperatura = temperatura

    def get_temperatura(self):
        """Método para obtener la temperatura diaria."""
        return self.__temperatura

class ClimaSemanal:
    """Clase para gestionar el clima de una semana."""
    def __init__(self):
        self.dias = [ClimaDiario() for _ in range(7)]  # Lista de objetos ClimaDiario

    def ingresar_temperaturas(self):
        """Método para ingresar temperaturas diarias."""
        for i, dia in enumerate(self.dias):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            dia.set_temperatura(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)

def main():
    print("Programa para calcular el promedio semanal del clima (POO).")
    clima_semanal = ClimaSemanal()
    clima_semanal.ingresar_temperaturas()
    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
