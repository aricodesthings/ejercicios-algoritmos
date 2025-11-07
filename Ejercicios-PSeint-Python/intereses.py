cantidad = float(input("Ingrese la cantidad de dinero que invirtió en el CDT: "))
porc_int = float(input("Ingrese el porcentaje de intereses: "))
period = float(input("Ingrese el periodo en el que el CDT estará activo en días: "))

# Calcular valores
porc_int = porc_int / 100
descuen = 0.07
valor_int = (cantidad * porc_int * period) / 360
descuen = valor_int * descuen
ganan = (cantidad + valor_int) - descuen

# Mostrar resultados
print("El valor de los intereses es:", valor_int,
      ", el descuento por los impuestos es:", descuen,
      "y la ganancia total es:", ganan)