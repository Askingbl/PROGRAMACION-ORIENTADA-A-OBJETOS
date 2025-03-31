import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        self.task_list = []

        # Entrada de nueva tarea
        self.entry = tk.Entry(root, font=('Arial', 14))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="Añadir tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, font=('Arial', 14), selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        # Enlaces de teclado
        self.entry.bind("<Return>", lambda event: self.add_task())
        root.bind("<c>", lambda event: self.complete_task())
        root.bind("<C>", lambda event: self.complete_task())
        root.bind("<d>", lambda event: self.delete_task())
        root.bind("<D>", lambda event: self.delete_task())
        root.bind("<Delete>", lambda event: self.delete_task())
        root.bind("<Escape>", lambda event: root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingresa una tarea.")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task_text = self.listbox.get(index)

            # Verificamos si ya está marcada como completada
            if not task_text.startswith("✔ "):
                self.listbox.delete(index)
                self.listbox.insert(index, f"✔ {task_text}")
                self.listbox.itemconfig(index, fg="gray")
        except IndexError:
            messagebox.showinfo("Selección requerida", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showinfo("Selección requerida", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
