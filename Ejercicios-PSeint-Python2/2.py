litros = float(input("Ingrese la cantidad de litros en el tanque: "))

if litros < 250:
    print("La llave debe estar ABIERTA (nivel bajo).")
elif litros > 450:
    print("La llave debe estar CERRADA (nivel alto).")
else:
    print("El nivel es adecuado, no se necesita acción.")