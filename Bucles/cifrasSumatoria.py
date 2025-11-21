numero = int(input("Ingrese un número entero: "))

if numero <= 0:
    print("El número no es positivo")
else:
    if numero < 0:
        numero = -numero
    
    numero_texto = str(numero)
    cantidad_cifras = len(numero_texto)
    
    suma = 0
    for digito in numero_texto:
        suma = suma + int(digito)
    
    print("El número tiene", cantidad_cifras, "cifras")
    print("La suma de sus cifras es:", suma)