N = int(input("Ingrese el número N (inicio): "))
M = int(input("Ingrese el número M (fin): "))

print(f"Buscando el primer múltiplo de 9 entre {N} y {M}...")

multiplo_encontrado = None

for numero in range(N, M + 1):
    if numero % 9 == 0:
        multiplo_encontrado = numero
        break

if multiplo_encontrado is not None:
    print(f"El primer múltiplo de 9 es: {multiplo_encontrado}")
    print(f"   ({multiplo_encontrado} ÷ 9 = {multiplo_encontrado // 9})")
else:
    print("No se encontró ningún múltiplo de 9 en el rango")