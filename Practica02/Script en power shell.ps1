# Definición de variable
$nombre = "Juan"

# Función con parámetro
function Saludar($nombre) {
  Write-Host "Hola, $nombre!"
}

# If
if ($nombre -eq "Juan") {
  # Ciclo
  for ($i = 1; $i -le 5; $i++) {
    Saludar $nombre
  }
}
elseif ($nombre -eq "Pedro") {
  Write-Host "Hola, Pedro!"
}
else {
  Write-Host "El nombre no es Juan ni Pedro."
}
