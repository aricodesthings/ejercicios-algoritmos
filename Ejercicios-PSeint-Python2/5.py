a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4*a*c

if a == 0:
    print("No es una ecuación cuadrática (a no puede ser 0).")
elif discriminante < 0:
    print("La ecuación no tiene solución real.")
else:
    print("La ecuación tiene solución real.")
