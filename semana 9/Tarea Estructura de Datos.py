class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto
        :param id_producto: ID único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad en stock
        :param precio: Precio del producto
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        """Inicializa el inventario con una lista vacía de productos de limpieza."""
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un nuevo producto de limpieza al inventario, asegurando que el ID sea único."""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto de limpieza agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto de limpieza por su ID."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto de limpieza eliminado exitosamente.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto de limpieza por su ID."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.actualizar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.actualizar_precio(nuevo_precio)
                print("Producto de limpieza actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos de limpieza por nombre."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos de limpieza con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos de limpieza en el inventario."""
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario de productos de limpieza está vacío.")


def menu():
    """Interfaz de usuario en la consola."""
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios de Productos de Limpieza")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto de limpieza: ")
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
            nombre = input("Ingrese el nombre del producto de limpieza a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventarios de productos de limpieza.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()

