from cx_Freeze import setup, Executable
import sys
import os

# Define la ruta al icono personalizado
icon_path = "ruta/a/tu/icono.ico"

# Define la ruta al archivo ejecutable de tu aplicación
executable_path = "to_do_list.py"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Define el ejecutable
exe = Executable(
    script=executable_path,
    base=base,
    icon=icon_path
)

setup(
    name="ToDoList",
    version="1.0",
    description="Una lista de hacer cosas",
    executables=[exe]
)

