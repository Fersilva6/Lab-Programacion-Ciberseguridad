#!/bin/bash

# Función para enviar correo
enviar_correo() {
    destinatario="$1"
    asunto="$2"
    mensaje="$3"
    echo "$mensaje" | mail -s "$asunto" "$destinatario"
}

# Archivo con la lista de direcciones de correo
archivo_correos="lista_correos.txt"

# Ruta al script de Bash para la descarga de archivos
ruta_script_bash="/ruta/al/script_bash.sh"

# Ejecutar el script de Bash y verificar su resultado
bash "$ruta_script_bash"
resultado=$?

# Verificar si el último comando fue exitoso o tuvo un error
if [[ $resultado -eq 0 ]]; then
    asunto="Comando exitoso"
    mensaje="El último comando se ejecutó con éxito."
else
    asunto="Error en el comando"
    mensaje="El último comando tuvo un error."
fi

# Leer el archivo de lista de correos y enviar un correo a cada dirección
while IFS= read -r correo
do
    enviar_correo "$correo" "$asunto" "$mensaje"
done < "$archivo_correos"
