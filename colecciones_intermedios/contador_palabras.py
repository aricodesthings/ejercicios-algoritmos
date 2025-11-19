def contador_palabras():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    contador = {}
    
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    
    print(contador)