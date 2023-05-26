# Consulta 1 a la API
Invoke-RestMethod -Uri "<URL_API>/endpoint1"  # Reemplaza <URL_API> con la URL real

# Consulta 2 a la API basada en la consulta previa
$respuesta1 = Invoke-RestMethod -Uri "<URL_API>/endpoint1"
$id = $respuesta1.id
Invoke-RestMethod -Uri "<URL_API>/endpoint2/$id"

# Consulta 3 a la API
Invoke-RestMethod -Uri "<URL_API>/endpoint3"

# Consulta 4 a la API basada en la consulta previa
$respuesta3 = Invoke-RestMethod -Uri "<URL_API>/endpoint3"
$parametro = $respuesta3.parametro
Invoke-RestMethod -Uri "<URL_API>/endpoint4/$parametro"

# Consulta 5 a la API
Invoke-RestMethod -Uri "<URL_API>/endpoint5"
