import tkinter as tk
from tkinter import ttk


class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Datos")

        # Etiqueta y campo de entrada
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Botón para agregar datos
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Tabla para mostrar los datos
        self.tree = ttk.Treeview(root, columns=("Dato"), show='headings')
        self.tree.heading("Dato", text="Dato Ingresado")
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botón para limpiar datos
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.grid(row=2, column=1, pady=10)

    def add_data(self):
        data = self.entry.get()
        if data:
            self.tree.insert("", "end", values=(data,))
            self.entry.delete(0, tk.END)

    def clear_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
