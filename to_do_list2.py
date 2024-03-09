import tkinter as tk
from tkinter import messagebox

# Función para guardar las tareas en un archivo de texto
def guardar_tareas():
    with open("Py_escritorio/tareas.txt", "w") as archivo:
        tareas = lista_tareas.get(0, tk.END)
        for tarea in tareas:
            archivo.write(tarea + "\n")

# Función para cargar las tareas desde un archivo de texto
def cargar_tareas():
    try:
        with open("Py_escritorio/tareas.txt", "r") as archivo:
            for tarea in archivo:
                lista_tareas.insert(tk.END, tarea.strip())
    except FileNotFoundError:
        return

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
        guardar_tareas()
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
        guardar_tareas()
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

# Cargar tareas al iniciar la aplicación
cargar_tareas()

# Guardar tareas al cerrar la aplicación
def cerrar_ventana():
    guardar_tareas()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Ejecutar la ventana
ventana.mainloop()

