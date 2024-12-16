def ingresar_temperaturas():
    """Función para ingresar temperaturas diarias."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio semanal."""
    return sum(temperaturas) / len(temperaturas)

def main():
    print("Programa para calcular el promedio semanal del clima.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()

