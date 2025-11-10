numero = int(input("Ingrese un número entre 0 y 20: "))

primos = [2, 3, 5, 7, 11, 13, 17, 19]

if numero in primos:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} NO es primo.")