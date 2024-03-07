#to_do_list 
import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea")

# Crear la ventana
ventana = tk.Tk()
ventana.title("To Do List")

# Crear la lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Crear la entrada de texto para agregar tareas
entrada_tarea = tk.Entry(ventana, width=50)
entrada_tarea.pack(pady=5)

# Crear botones para agregar y eliminar tareas
btn_agregar = tk.Button(ventana, text="Agregar tarea", width=40, command=agregar_tarea)
btn_agregar.pack(pady=5)
btn_eliminar = tk.Button(ventana, text="Eliminar tarea", width=40, command=eliminar_tarea)
btn_eliminar.pack()

# Ejecutar la ventana
ventana.mainloop()
