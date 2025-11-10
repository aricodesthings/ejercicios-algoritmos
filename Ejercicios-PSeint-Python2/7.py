min1 = int(input("Mínimo primer intervalo: "))
max1 = int(input("Máximo primer intervalo: "))

min2 = int(input("Mínimo segundo intervalo: "))
max2 = int(input("Máximo segundo intervalo: "))

min3 = int(input("Mínimo tercer intervalo: "))
max3 = int(input("Máximo tercer intervalo: "))

x = int(input("Número a verificar: "))

if (min1 < x < max1) or (min2 < x < max2) or (min3 < x < max3):
    print(f"El número {x} está DENTRO de algún intervalo")
else:
    print(f"El número {x} está FUERA de todos los intervalos")