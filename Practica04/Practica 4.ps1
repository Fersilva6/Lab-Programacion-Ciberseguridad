# Ruta de las imágenes a decodificar
$imagen1 = "Ruta/imagen1.png"
$imagen2 = "Ruta/imagen2.png"

# Función para decodificar una imagen en Base64
function Decodificar-Imagen([string]$rutaImagen) {
    $bytes = [System.IO.File]::ReadAllBytes($rutaImagen)
    $imagenBase64 = [System.Convert]::ToBase64String($bytes)
    $imagenDecodificada = [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($imagenBase64))
    return $imagenDecodificada
}

# Decodificar las imágenes
$mensaje1 = Decodificar-Imagen $imagen1
$mensaje2 = Decodificar-Imagen $imagen2

# Codificar el mensaje "Hola mundo" en C#
$mensajeCSharp = @"
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hola mundo");
    }
}
"@

# Guardar el mensaje codificado en un archivo
$archivoSalida = "Ruta/hola_mundo.cs"
Set-Content -Path $archivoSalida -Value $mensajeCSharp

Write-Host "Decodificación completada."
Write-Host "Mensaje 1: $mensaje1"
Write-Host "Mensaje 2: $mensaje2"
Write-Host "Mensaje codificado en C# guardado en: $archivoSalida"
