import os
import subprocess

# Ruta al archivo de registro de usuario de Windows
ruta_registro = "ruta_al_registro.reg"

# Directorio donde se encuentra RegRipper
directorio_regripper = "ruta_al_directorio_regripper"

# Plugins de RegRipper a utilizar
plugins = ["userassist", "runmru"]

# Crear el comando de RegRipper
comando_regripper = f"perl {os.path.join(directorio_regripper, 'rip.pl')} -r {ruta_registro} -p {','.join(plugins)}"

# Ejecutar RegRipper
resultado = subprocess.run(comando_regripper, shell=True, capture_output=True, text=True)

# Verificar si RegRipper se ejecutó correctamente
if resultado.returncode == 0:
    print("Análisis del registro completado.")
    # Acceder a los resultados generados por RegRipper
    for plugin in plugins:
        archivo_resultado = f"{ruta_registro}_{plugin}.txt"
        if os.path.exists(archivo_resultado):
            with open(archivo_resultado, "r") as archivo:
                print(f"Resultados del plugin {plugin}:")
                print(archivo.read())
        else:
            print(f"No se encontraron resultados para el plugin {plugin}.")
else:
    print("Se produjo un error al ejecutar RegRipper.")
    print("Error:", resultado.stderr)
