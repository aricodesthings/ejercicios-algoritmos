print("=== CALCULADORA BÁSICA ===")

while True:
    print("\nOpciones disponibles:")
    print("1. Sumar")
    print("2. Restar") 
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        print("\n--- SUMA ---")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    
    elif opcion == "2":
        print("\n--- RESTA ---")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    
    elif opcion == "3":
        print("¡Gracias por usar la calculadora!")
        break
    
    else:
        print("Opción inválida. Por favor seleccione 1, 2 o 3.")