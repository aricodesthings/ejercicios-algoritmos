n = int(input("Ingrese el último término: "))

print("La serie es:")
for i in range(1, n + 1, 2):
    if i == n or i == n - 1:
        print(i)
    else:
        print(i, end=", ")