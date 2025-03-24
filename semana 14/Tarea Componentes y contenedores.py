import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# ======== FRAMES ========
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# ======== TREEVIEW DE EVENTOS ========
columns = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(top_frame, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)
tree.pack()

# ======== ENTRADAS Y ETIQUETAS ========
tk.Label(middle_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(middle_frame, width=15, date_pattern='yyyy-mm-dd')
date_entry.grid(row=0, column=1, padx=5)

tk.Label(middle_frame, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
hour_entry = tk.Entry(middle_frame, width=10)
hour_entry.grid(row=0, column=3, padx=5)

tk.Label(middle_frame, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
desc_entry = tk.Entry(middle_frame, width=40)
desc_entry.grid(row=1, column=1, columnspan=3, padx=5)

# ======== FUNCIONES ========
def agregar_evento():
    fecha = date_entry.get()
    hora = hour_entry.get()
    descripcion = desc_entry.get()

    if not hora or not descripcion:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    tree.insert("", "end", values=(fecha, hora, descripcion))
    hour_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

def eliminar_evento():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showinfo("Eliminar", "Selecciona un evento para eliminar.")
        return
    confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento?")
    if confirm:
        tree.delete(seleccionado)

# ======== BOTONES ========
btn_agregar = tk.Button(bottom_frame, text="Agregar Evento", command=agregar_evento, width=20)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(bottom_frame, text="Eliminar Evento Seleccionado", command=eliminar_evento, width=25)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(bottom_frame, text="Salir", command=root.destroy, width=10)
btn_salir.grid(row=0, column=2, padx=10)

# ======== INICIAR APLICACIÓN ========
root.mainloop()
