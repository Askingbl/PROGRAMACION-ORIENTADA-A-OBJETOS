class ShoppingList:
    """
    Clase que gestiona una lista de compras para objetos de cocina.
    Utiliza un constructor (__init__) para inicializar la lista
    y un destructor (__del__) para realizar una limpieza final (si es necesario).
    """

    def __init__(self):
        """
        Constructor de la clase ShoppingList.
        Inicializa una lista vacía para los objetos de cocina.
        """
        self.items = []
        print("Lista de compras creada.")

    def add_item(self, item):
        """
        Agrega un objeto de cocina a la lista de compras.

        :param item: Nombre del objeto de cocina a agregar.
        """
        self.items.append(item)
        print(f"'{item}' agregado a la lista de compras.")

    def remove_item(self, item):
        """
        Elimina un objeto de cocina de la lista de compras si existe.

        :param item: Nombre del objeto de cocina a eliminar.
        """
        if item in self.items:
            self.items.remove(item)
            print(f"'{item}' eliminado de la lista de compras.")
        else:
            print(f"'{item}' no se encuentra en la lista de compras.")

    def show_items(self):
        """
        Muestra todos los objetos en la lista de compras.
        """
        if self.items:
            print("Lista de compras:")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")
        else:
            print("La lista de compras está vacía.")

    def sort_items(self):
        """
        Ordena los objetos de la lista de compras alfabéticamente.
        """
        self.items.sort()
        print("Lista de compras ordenada alfabéticamente.")

    def __del__(self):
        """
        Destructor de la clase ShoppingList.
        Indica que la lista de compras ya no está en uso.
        """
        print("La lista de compras ya no está en uso.")


# Demostración del uso de la clase
if __name__ == "__main__":
    # Crear una instancia de ShoppingList
    my_list = ShoppingList()

    while True:
        print("\nOpciones:")
        print("1. Agregar objeto")
        print("2. Eliminar objeto")
        print("3. Mostrar lista")
        print("4. Ordenar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            item = input("Ingrese el objeto de cocina a agregar: ")
            my_list.add_item(item)
        elif opcion == "2":
            item = input("Ingrese el objeto de cocina a eliminar: ")
            my_list.remove_item(item)
        elif opcion == "3":
            my_list.show_items()
        elif opcion == "4":
            my_list.sort_items()
        elif opcion == "5":
            print("Saliendo del programa...")
            del my_list
            break
        else:
            print("Opción no válida. Intente nuevamente.")

