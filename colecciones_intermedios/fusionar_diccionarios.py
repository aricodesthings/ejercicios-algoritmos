def fusionar_diccionarios():
    A = {'x': 1, 'y': 2}
    B = {'y': 10, 'z': 3}
    
    fusionado = A.copy()
    fusionado.update(B)
    
    
    print(fusionado)