numero = int(input("Ingrese un número entero mayor que 1: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
if es_primo:
    print(f"El número {numero} ES primo")
else:
    print(f"El número {numero} NO es primo")