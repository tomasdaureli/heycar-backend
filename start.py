import os
import sys
import platform
import subprocess


def setup():
    # Crear el entorno virtual
    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", "env"])

    # Detectar sistema operativo
    os_type = platform.system()

    # Comando para activar el entorno virtual
    if os_type == "Windows":
        activate_command = ".\\env\\Scripts\\activate"
    else:
        activate_command = "source env/bin/activate"

    # Mostrar instrucciones para activar el entorno
    print(f"Para activar el entorno virtual, usa el siguiente comando:")
    print(f"{activate_command}")

    # Instalar las dependencias
    print("Instalando dependencias...")
    subprocess.run(
        [
            os.path.join("env", "Scripts" if os_type == "Windows" else "bin", "pip"),
            "install",
            "-r",
            "app/requirements.txt",
        ]
    )


def start():
    # Cambia al directorio app y ejecuta uvicorn
    os.chdir("app")
    subprocess.run(["uvicorn", "main:app", "--reload"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python start.py [command]")
        print("Commands:")
        print("  setup    - Configura el entorno virtual")
        print("  start    - Inicia la aplicación con Uvicorn")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "setup":
        setup()
    elif command == "start":
        start()
    else:
        print(f"Unknown command: {command}")
