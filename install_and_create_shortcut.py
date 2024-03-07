import os
import shutil
import subprocess

# Ejecuta el script de configuración setup.py para compilar la aplicación
subprocess.call(["python", "setup.py", "build"])

# Ruta al archivo ejecutable de tu aplicación
executable_path = "build/exe.win32-3.9/to_do_list.exe"

# Ruta al directorio del escritorio
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Ruta al icono personalizado
icon_path = "ruta/a/tu/icono.ico"

# Crear el acceso directo en el escritorio
shortcut_path = os.path.join(desktop_path, "ToDoList.lnk")
with open(shortcut_path, "w") as shortcut_file:
    shortcut_file.write(
        "[InternetShortcut]\n"
        "URL=file:///" + executable_path.replace("\\", "/") + "\n"
        "IconIndex=0\n"
        "IconFile=" + icon_path.replace("\\", "/")
    )

