def potencia(base, exponente):
    if not isinstance(exponente, int):
        return "Error: El exponente debe ser un número entero"
    
    if exponente == 0:
        return 1
    elif exponente > 0:
        resultado = 1
        for _ in range(exponente):
            resultado *= base
        return resultado
    else:
        resultado = 1
        for _ in range(-exponente):
            resultado *= base
        return 1 / resultado


print(potencia(2, 3))
print(potencia(5, -2))