from ftplib import FTP
import os

# Información de conexión al servidor FTP
ftp_host = 'ftp.example.com'
ftp_user = 'tu_usuario'
ftp_password = 'tu_contraseña'

# Carpeta local para almacenar los archivos de texto descargados
carpeta_destino = 'TXT'

# Función para descargar un archivo desde el servidor FTP
def descargar_archivo(ftp, archivo, carpeta_destino):
    ruta_local = os.path.join(carpeta_destino, archivo)
    with open(ruta_local, 'wb') as archivo_local:
        ftp.retrbinary('RETR ' + archivo, archivo_local.write)
    print(f'Descargado: {archivo}')

# Conexión al servidor FTP
ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_password)

# Cambiar al directorio principal del servidor FTP
ftp.cwd('/')

# Crear la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Obtener la lista de archivos y carpetas en el servidor FTP
archivos_ftp = ftp.nlst()

# Buscar y descargar los archivos de texto
for archivo in archivos_ftp:
    nombre_archivo, extension = os.path.splitext(archivo)
    extension = extension.lower()
    if extension in ['.txt', '.msg', '.readme']:
        descargar_archivo(ftp, archivo, carpeta_destino)

# Cerrar la conexión FTP
ftp.quit()

print('Descarga completada.')
