def invertir_diccionario():
    diccionario = {'a': 1, 'b': 2, 'c': 3}
    invertido = {valor: clave for clave, valor in diccionario.items()}
    print(invertido)