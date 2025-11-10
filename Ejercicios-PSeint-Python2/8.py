tipo = int(input("Seleccione el tipo de artículo (1-4): "))

# Pedir el precio del artículo
precio = float(input("Ingrese el precio del artículo: "))

# Calcular el descuento según el tipo
if tipo == 1:  # Textil
    descuento_porcentaje = 0
    nombre_tipo = "Textil"
elif tipo == 2:  # Electrodoméstico
    descuento_porcentaje = 3.7
    nombre_tipo = "Electrodoméstico"
elif tipo == 3:  # Elementos de cocina
    descuento_porcentaje = 4.2
    nombre_tipo = "Elementos de cocina"
elif tipo == 4:  # Video juego
    descuento_porcentaje = 7.8
    nombre_tipo = "Video juego"
else:
    print("Tipo de artículo no válido")
    descuento_porcentaje = 0
    nombre_tipo = "Desconocido"