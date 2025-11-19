def transponer_matriz():
    matriz = [[1, 2, 3], [4, 5, 6]]
    
    transpuesta = []
    for j in range(len(matriz[0])):
        fila = []
        for i in range(len(matriz)):
            fila.append(matriz[i][j])
        transpuesta.append(fila)
    
    print(transpuesta)