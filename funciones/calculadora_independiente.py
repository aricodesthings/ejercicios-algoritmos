def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    print("=== CALCULADORA ===")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Seleccione una operación (1-4): ")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Por favor ingrese números válidos")
        return
    
    if opcion == "1":
        resultado = sumar(num1, num2)
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == "2":
        resultado = restar(num1, num2)
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
        print(f"Resultado: {num1} × {num2} = {resultado}")
    elif opcion == "4":
        resultado = dividir(num1, num2)
        print(f"Resultado: {num1} ÷ {num2} = {resultado}")
    else:
        print("Opción no válida")

# ESTA ES LA LÍNEA QUE FALTA PARA EJECUTAR EL PROGRAMA
calculadora()