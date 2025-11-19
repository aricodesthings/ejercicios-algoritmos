
def coordenadas_en_rango():
    coordenada = (4, 6)
    rango_min, rango_max = 0, 10
    
    x, y = coordenada
    if rango_min <= x <= rango_max and rango_min <= y <= rango_max:
        print("Dentro del rango")
    else:
        print("Fuera del rango")