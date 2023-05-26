import requests
from bs4 import BeautifulSoup

# URL del sitio web que deseas hacer scraping
url = "https://www.ejemplo.com"

# Realizar la solicitud HTTP GET a la página web
response = requests.get(url)

# Crear un objeto BeautifulSoup con el contenido HTML de la página web
soup = BeautifulSoup(response.content, "html.parser")

# Extraer la información deseada del sitio web
# Aquí se muestra un ejemplo para extraer los títulos de los elementos <h1> en la página
titulos = soup.find_all("h1")

# Crear un archivo para guardar la información extraída
nombre_archivo = "datos_extraidos.txt"

with open(nombre_archivo, "w") as archivo:
    # Escribir los títulos en el archivo
    for titulo in titulos:
        archivo.write(titulo.text + "\n")

print("Los datos han sido extraídos y guardados en el archivo:", nombre_archivo)
