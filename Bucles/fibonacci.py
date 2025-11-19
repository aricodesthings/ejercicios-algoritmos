N = int(input("Ingrese un número entero positivo N: "))

fibonacci = []
a, b = 0, 1

while a <= N:
    fibonacci.append(a)
    a, b = b, a + b

print("Serie de Fibonacci hasta", N, ":")
print(fibonacci)