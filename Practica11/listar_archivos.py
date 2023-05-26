import os

def listar_archivos_directorio(directorio):
    archivos = []
    for ruta, _, archivos_en_ruta in os.walk(directorio):
        for archivo in archivos_en_ruta:
            ruta_completa = os.path.join(ruta, archivo)
            archivos.append(ruta_completa)
    return archivos

if __name__ == "__main__":
    directorio = input("Ingrese la ruta del directorio a analizar: ")
    archivos = listar_archivos_directorio(directorio)
    
    print("Archivos encontrados:")
    for archivo in archivos:
        print(archivo)
