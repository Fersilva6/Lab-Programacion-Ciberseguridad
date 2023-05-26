#!/bin/bash

# Información de conexión al servidor FTP
ftp_host="ftp.example.com"
ftp_user="tu_usuario"
ftp_password="tu_contraseña"

# Carpeta local para almacenar los archivos de texto descargados
carpeta_destino="TXT"

# Función para descargar un archivo desde el servidor FTP
descargar_archivo() {
    archivo="$1"
    ruta_local="$carpeta_destino/$archivo"
    ftp -n "$ftp_host" <<END_SCRIPT
    quote USER "$ftp_user"
    quote PASS "$ftp_password"
    binary
    get "$archivo" "$ruta_local"
    quit
END_SCRIPT
    echo "Descargado: $archivo"
}

# Conexión al servidor FTP y descarga de archivos
ftp -n "$ftp_host" <<END_SCRIPT
quote USER "$ftp_user"
quote PASS "$ftp_password"
cd /
archivos_ftp=$(ls)
for archivo in $archivos_ftp
do
    nombre_archivo=$(basename "$archivo")
    extension="${nombre_archivo##*.}"
    extension=$(echo "$extension" | tr '[:upper:]' '[:lower:]')
    if [[ "$extension" == "txt" || "$extension" == "msg" || "$extension" == "readme" ]]; then
        descargar_archivo "$archivo"
    fi
done
quit
END_SCRIPT

echo "Descarga completada."

