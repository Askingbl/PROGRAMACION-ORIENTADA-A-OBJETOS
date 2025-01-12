class Producto:
    """
    Lista que representa un producto en una tienda de repuestos de carros.
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio por unidad del producto

    def __str__(self):
        """Representación en texto del producto."""
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

class Tienda:
    """
    Lista que representa una tienda con un inventario de productos de repuestos de carros.
    """
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tienda
        self.inventario = []  # Lista de productos disponibles en la tienda

    def agregar_producto(self, producto):
        """Agrega un producto al inventario."""
        self.inventario.append(producto)

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        print(f"Inventario de {self.nombre}:")
        for producto in self.inventario:
            print(producto)

    def calcular_total_inventario(self):
        """Calcula el precio total de todos los productos en el inventario."""
        return sum(producto.precio for producto in self.inventario)

# Lista de productos predefinidos por la empresa
productos_disponibles = [
    {"nombre": "Filtro de aceite", "precio": 10.0},
    {"nombre": "Bujía", "precio": 5.0},
    {"nombre": "Pastillas de freno", "precio": 25.0},
    {"nombre": "Amortiguador", "precio": 60.0},
    {"nombre": "Filtro de aire", "precio": 15.0},
]

# Ejemplo:
if __name__ == "__main__":
    # Crear una tienda de repuestos
    tienda = Tienda("Repuestos Automotrices")

    # Mostrar lista de productos para seleccionar
    print("Lista de productos disponibles para agregar al inventario:")
    for i, producto in enumerate(productos_disponibles, start=1):
        print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']:.2f}")

    # Seleccionar productos para agregar al inventario mediante entrada del usuario
    while True:
        seleccion = input("Ingresa el número del producto que deseas agregar (o 'total' para terminar): ")
        if seleccion.lower() == 'total':
            break
        try:
            indice = int(seleccion) - 1
            if 0 <= indice < len(productos_disponibles):
                producto_seleccionado = productos_disponibles[indice]
                producto = Producto(producto_seleccionado['nombre'], producto_seleccionado['precio'])
                tienda.agregar_producto(producto)
                print(f"{producto_seleccionado['nombre']} agregado al inventario.")
            else:
                print("Número de producto no válido. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

    # Mostrar inventario final
    tienda.mostrar_inventario()

    # Calcular y mostrar el precio total del inventario
    total = tienda.calcular_total_inventario()
    print(f"El precio total de los productos en el inventario es: ${total:.2f}")

