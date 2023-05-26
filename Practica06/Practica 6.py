import subprocess
import base64

# Obtener la IP local
ip_local = subprocess.check_output(['hostname', '-I']).decode().strip()

# Obtener la IP pública
ip_publica = subprocess.check_output(['curl', 'ifconfig.me']).decode().strip()

# Escanear el segmento de red privado
segmento_red_privado = '192.168.1.0/24'
resultado_segmento_privado = subprocess.check_output(['nmap', '-sn', segmento_red_privado]).decode().strip()

# Escanear una IP específica con un script
ip_escaneo = '192.168.1.1'
resultado_escaneo = subprocess.check_output(['nmap', '-sC', ip_escaneo]).decode().strip()

# Guardar los resultados codificados en Base64 en un archivo
archivo_resultados = 'resultados.txt'

with open(archivo_resultados, 'w') as archivo:
    archivo.write('IP Local: ' + ip_local + '\n')
    archivo.write('IP Pública: ' + ip_publica + '\n')
    archivo.write('Resultado Escaneo Segmento Privado:\n' + resultado_segmento_privado + '\n')
    archivo.write('Resultado Escaneo IP ' + ip_escaneo + ':\n' + resultado_escaneo + '\n')

# Codificar los resultados en Base64
with open(archivo_resultados, 'rb') as archivo:
    resultados_codificados = base64.b64encode(archivo.read()).decode()

# Guardar los resultados codificados en un archivo de texto
archivo_codificado = 'resultados_codificados.txt'

with open(archivo_codificado, 'w') as archivo:
    archivo.write(resultados_codificados)

print('Los resultados han sido guardados en el archivo', archivo_codificado)
