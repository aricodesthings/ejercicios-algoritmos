def mayores_que_promedio():
    numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
    promedio = sum(numeros) / len(numeros)
    mayores = [n for n in numeros if n > promedio]
    
    print(f"Promedio: {promedio}")
    print(f"Mayores que el promedio: {sorted(mayores)}")