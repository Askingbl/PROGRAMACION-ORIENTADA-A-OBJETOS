import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Métodos para obtener y establecer atributos
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def a_diccionario(self):
        """Convierte el producto a un diccionario para almacenamiento."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def desde_diccionario(datos):
        """Crea un Producto desde un diccionario."""
        return Producto(datos['id_producto'], datos['nombre'], datos['cantidad'], datos['precio'])


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos, clave es el ID

    def añadir_producto(self, producto):
        if producto.obtener_id() not in self.productos:
            self.productos[producto.obtener_id()] = producto
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
                producto.establecer_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.establecer_precio(nuevo_precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.obtener_nombre().lower() == nombre.lower()]
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

    # Persistencia (archivos)
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
        except FileNotFoundError:
            print("No se encontró el archivo, iniciando con inventario vacío.")
        except json.JSONDecodeError:
            print("Error al leer el archivo, iniciando con inventario vacío.")


# Función menú interactivo
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


# Ejecución
if __name__ == "__main__":
    menu()
