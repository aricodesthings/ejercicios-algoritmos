import math

cat1 = float(input("Ingrese el primer cateto: "))
cat2 = float(input("Ingrese el segundo cateto: "))

hip = math.sqrt(cat1**2 + cat2**2)

print("La hipotenusa del triángulo es:", hip)