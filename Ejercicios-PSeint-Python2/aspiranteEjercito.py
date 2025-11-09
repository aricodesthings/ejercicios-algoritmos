est= input("¿Estas solter@. Si (s), No (n): ")
se=input("Ingrese su sexo. Mujer (m), Hombre (h): ")
alt=float(input("Ingrese su altura: "))
edad=int(input("Ingrese su edad: "))
if est in ('S', 's') and se in ('m', 'M') and (alt>=160) and (20<=edad<=24):
    print("eres apt@ para ser parte del ejercito")
else:
    print("No apt@ para ser parte del ejercito")