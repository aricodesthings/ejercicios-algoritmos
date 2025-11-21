n = int(input("Ingrese el valor de n: "))

print("x\tf(x)")
for x in range(0, n + 1, 2):
    resultado = x * x * x + x * x - 5
    print(x, "\t", resultado)