import os
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio,
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos], archivo)
            print("Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            print("No se encontró un archivo de inventario. Se creará uno nuevo al guardar.")
            return
        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                datos = json.load(archivo)
                self.productos = [Producto.from_dict(p) for p in datos]
            print("Inventario cargado exitosamente desde el archivo.")
        except FileNotFoundError:
            print("El archivo de inventario no existe, se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("Error: El archivo de inventario está corrupto y no se pudo cargar.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado exitosamente y guardado en el archivo.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado exitosamente y cambios guardados en el archivo.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.actualizar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.actualizar_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado exitosamente y cambios guardados en el archivo.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                int(nueva_cantidad) if nueva_cantidad else None,
                float(nuevo_precio) if nuevo_precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventarios.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()