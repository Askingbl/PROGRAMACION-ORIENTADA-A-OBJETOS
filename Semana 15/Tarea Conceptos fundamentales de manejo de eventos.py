import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind("<Double-1>", self.complete_task)

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_index)

            # Verificar si ya está completada
            if task_text.startswith("✔️ "):
                messagebox.showinfo("Ya completada", "Esta tarea ya está marcada como completada.")
            else:
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"✔️ {task_text}")
        except IndexError:
            messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
