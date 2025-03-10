class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (autor, titulo)  # Tupla para autor y título (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.detalles[1]} por {self.detalles[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.usuario_id})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios
        self.historial_prestamos = {}  # Diccionario para gestionar préstamos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.usuario_id)
            self.historial_prestamos[usuario.usuario_id] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            if not self.historial_prestamos[usuario_id]:  # Verificar que no tenga libros prestados
                self.usuarios_registrados.remove(usuario_id)
                del self.historial_prestamos[usuario_id]
                print(f"Usuario con ID {usuario_id} eliminado.")
            else:
                print("No se puede eliminar el usuario, tiene libros prestados.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.historial_prestamos[usuario_id].append(libro)
            print(f"Libro prestado: {libro} a usuario {usuario_id}")
        else:
            print("No se puede realizar el préstamo.")

    def devolver_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios_registrados:
            for libro in self.historial_prestamos[usuario_id]:
                if libro.isbn == isbn:
                    self.historial_prestamos[usuario_id].remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
        print("El usuario no tiene este libro prestado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            libros = self.historial_prestamos[usuario_id]
            if libros:
                print(f"Libros prestados al usuario {usuario_id}:")
                for libro in libros:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("El usuario no está registrado.")


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nMenú de Biblioteca")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))
        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(user_id)
        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(user_id, isbn)
        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(user_id, isbn)
        elif opcion == "7":
            criterio = input("Buscar por (titulo, autor, categoria): ")
            valor = input(f"Ingrese el valor de {criterio}: ")
            biblioteca.buscar_libro(criterio, valor)
        elif opcion == "8":
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(user_id)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
