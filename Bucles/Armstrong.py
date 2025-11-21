numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("El número debe ser positivo")
else:
    numero_texto = str(numero)
    cantidad_digitos = len(numero_texto)
    
    suma = 0
    for digito_char in numero_texto:
        digito = int(digito_char)
        potencia = 1
        for i in range(cantidad_digitos):
            potencia = potencia * digito
        suma = suma + potencia
    
    if suma == numero:
        print(numero, "es un número de Armstrong")
    else:
        print(numero, "NO es un número de Armstrong")