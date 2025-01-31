"""
Programa de conversión de unidades
Este programa permite al usuario convertir diferentes unidades de medida:
1. Metros a kilómetros
2. Gramos a kilogramos
3. Grados Celsius a Fahrenheit

Tipos de datos utilizados:
- Enteros (integer) para selecciones de menú.
- Flotantes (float) para valores numéricos en las conversiones.
- Cadenas de texto (string) para mensajes y entradas de usuario.
- Booleanos (boolean) para controlar el ciclo de ejecución.

Autor: [carlos]
"""

def convertir_metros_a_kilometros(metros):
    """
    Convierte una cantidad dada en metros a kilómetros.
    :param metros: Distancia en metros (float).
    :return: Distancia en kilómetros (float).
    """
    return metros / 1000


def convertir_gramos_a_kilogramos(gramos):
    """
    Convierte una cantidad dada en gramos a kilogramos.
    :param gramos: Peso en gramos (float).
    :return: Peso en kilogramos (float).
    """
    return gramos / 1000


def convertir_celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura dada en grados Celsius a Fahrenheit.
    :param celsius: Temperatura en grados Celsius (float).
    :return: Temperatura en grados Fahrenheit (float).
    """
    return (celsius * 9/5) + 32


# Variable booleana para controlar la ejecución del programa
continuar_programa = True

while continuar_programa:
    # Mostrar menú de opciones
    print("\nConversor de Unidades")
    print("1. Convertir metros a kilómetros")
    print("2. Convertir gramos a kilogramos")
    print("3. Convertir grados Celsius a Fahrenheit")
    print("4. Salir")

    # Solicitar al usuario que elija una opción
    opcion = int(input("Selecciona una opción (1-4): "))

    if opcion == 1:
        # Convertir metros a kilómetros
        metros = float(input("Introduce la distancia en metros: "))
        kilometros = convertir_metros_a_kilometros(metros)
        print(f"{metros} metros son {kilometros:.2f} kilómetros.")
    elif opcion == 2:
        # Convertir gramos a kilogramos
        gramos = float(input("Introduce el peso en gramos: "))
        kilogramos = convertir_gramos_a_kilogramos(gramos)
        print(f"{gramos} gramos son {kilogramos:.2f} kilogramos.")
    elif opcion == 3:
        # Convertir grados Celsius a Fahrenheit
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        fahrenheit = convertir_celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
    elif opcion == 4:
        # Salir del programa
        print("Gracias por usar el conversor de unidades. ¡Hasta luego!")
        continuar_programa = False
    else:
        # Manejar opciones no válidas
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

# Fin del programa

