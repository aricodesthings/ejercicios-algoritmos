numero = int(input("Ingrese un número entero para la cuenta regresiva: "))

print("Iniciando cuenta regresiva...")

for i in range(numero, -1, -1):
    if i % 7 == 0 and i != 0:
        print(f"{i} ¡ALERTA! Es múltiplo de 7")
    else:
        print(i)

print("¡Cuenta regresiva finalizada!")