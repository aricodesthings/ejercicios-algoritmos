pares = 0
impares = 0

print("CONTADOR DE PARES E IMPARES")
print("Ingrese números enteros (ingrese 0 para terminar)")

while True:
    entrada = input("Ingrese un número: ")
    
    if entrada == "0":
        break
    
    try:
        numero = int(entrada)
        
        if numero % 2 == 0:
            pares += 1
            print(f"{numero} es PAR")
        else:
            impares += 1
            print(f"{numero} es IMPAR")
            
    except ValueError:
        print("Error: Por favor ingrese un número entero válido")

print("\n" + "=" * 40)
print("RESULTADOS FINALES:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Total de números ingresados: {pares + impares}")