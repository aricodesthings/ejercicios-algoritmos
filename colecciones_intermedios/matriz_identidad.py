def matriz_identidad():
    n = int(input("n = "))
    identidad = []
    
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        identidad.append(fila)
    
    for fila in identidad:
        print(fila)