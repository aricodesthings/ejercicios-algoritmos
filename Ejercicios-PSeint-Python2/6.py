min_val = int(input("Ingrese el valor mínimo: "))
max_val = int(input("Ingrese el valor máximo: "))
x = int(input("Ingrese el número a evaluar: "))

if min_val <= x <= max_val:
    print(f"El número {x} está DENTRO del intervalo [{min_val}, {max_val}].")
else:
    print(f"El número {x} está FUERA del intervalo [{min_val}, {max_val}].")