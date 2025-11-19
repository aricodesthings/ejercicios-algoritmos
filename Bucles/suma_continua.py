suma_total = 0

print("Ingrese números para sumar (solo se sumarán los positivos)")
print("Ingrese 0 para terminar")

while True:
    numero = int(input("Ingrese un número: "))
    
    if numero == 0:
        break
    
    if numero < 0:
        continue
    
    suma_total += numero

print(f"La suma total de los números positivos es: {suma_total}")