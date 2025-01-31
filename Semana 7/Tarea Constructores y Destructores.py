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

    # Agregar objetos a la lista de compras
    my_list.add_item("Sartén")
    my_list.add_item("Cuchillo")
    my_list.add_item("Tabla de cortar")

    # Mostrar los objetos de la lista de compras
    my_list.show_items()

    # Eliminar un objeto de la lista de compras
    my_list.remove_item("Cuchillo")

    # Mostrar la lista de compras actualizada
    my_list.show_items()

    # Eliminar la instancia explícitamente (esto activará el destructor)
    del my_list


