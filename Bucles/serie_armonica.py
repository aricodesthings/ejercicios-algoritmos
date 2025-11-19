n = int(input("Ingrese un número entero positivo n: "))

if n <= 0:
    print("Error: n debe ser un número entero positivo")
else:
    suma = 0.0
    
    for i in range(1, n + 1):
        suma += 1 / i
    
    print(f"La suma de la serie armónica hasta 1/{n} es: {suma}")