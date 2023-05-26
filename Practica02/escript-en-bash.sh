#!/bin/bash

# Definición de variable
nombre="Juan"

# Función con parámetro
saludar() {
  echo "Hola, $1!"
}

# If
if [ "$nombre" == "Juan" ]; then
  # Ciclo
  for i in {1..5}; do
    saludar $nombre
  done
else
  echo "El nombre no es Juan."
fi
