import json

# Clase Producto (única, con atributos completos y métodos de ejemplo incluidos)
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def a_diccionario(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def desde_diccionario(datos):
        return Producto(datos['id_producto'], datos['nombre'], datos['cantidad'], datos['precio'])

# Clase Inventario (única, con los métodos de ejemplo + los necesarios para el menú)
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: clave es el ID, valor es el Producto

    def añadir_producto(self, producto):
        if producto.id_producto not in self.productos:
            self.productos[producto.id_producto] = producto
            print("Producto añadido.")
        else:
            print("El producto con ese ID ya existe.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # Métodos adicionales (adaptados del ejemplo que me diste)
    def agregar_producto(self, producto):
        """Alias de añadir_producto para compatibilidad con tu ejemplo."""
        self.añadir_producto(producto)

    def mostrar_inventario(self):
        """Alias de mostrar_todos_los_productos para compatibilidad con tu ejemplo."""
        self.mostrar_todos_los_productos()

    # Persistencia
    def guardar_en_archivo(self, nombre_archivo="inventario_productos.json"):
        with open(nombre_archivo, "w") as archivo:
            json.dump([p.a_diccionario() for p in self.productos.values()], archivo, indent=4)
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo="inventario_productos.json"):
        try:
            with open(nombre_archivo, "r") as archivo:
                productos_cargados = json.load(archivo)
                self.productos = {p['id_producto']: Producto.desde_diccionario(p) for p in productos_cargados}
            print("Inventario cargado correctamente.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Iniciando inventario vacío.")

# Menú interactivo
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n--- Gestión de Inventario - Productos de Limpieza ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no modificar): ")
            precio = input("Nuevo precio (deje vacío para no modificar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opción no válida, intente nuevamente.")

# Ejemplo de uso (cargando el ejemplo que diste al inicio)
def ejemplo_inicial():
    inventario = Inventario()
    inventario.agregar_producto(Producto("1", "Teclado", 0, 19.99))
    inventario.agregar_producto(Producto("2", "Mouse", 0, 9.99))

    print("\n--- Inventario de Ejemplo (pre-cargado) ---")
    inventario.mostrar_inventario()

# Ejecución
if __name__ == "__main__":
    ejemplo_inicial()  # Puedes quitarlo si no quieres que se muestre al arrancar
    menu()
