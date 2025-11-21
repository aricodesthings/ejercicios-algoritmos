n = int(input("Ingrese el valor de n: "))

print("Columna 1\tColumna 2\tColumna 3")
for i in range(1, n + 1):
    columna2 = i * i
    columna3 = i * (i + 1)
    print(i, "\t\t", columna2, "\t\t", columna3)