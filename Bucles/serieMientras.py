n = int(input("Ingrese la cantidad de términos: "))

print("La serie es:")
for i in range(n):
    numero = 2 * i + 1
    if i == n - 1:
        print(numero)
    else:
        print(numero, end=", ")