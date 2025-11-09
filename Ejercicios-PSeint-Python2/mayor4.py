num1= float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))
num3= float(input("Ingrese el tercer número: "))
num4= float(input("Ingrese el cuarto número: "))
if (num3==num1 and num3==num2 and num3==num4):
	print("Todos los números son iguales")
elif (num1>num2 and num1>num3 and num1>num4):
	print(num1, " es el número mayor")
elif (num2>num1 and num2>num3 and num2>num4):
	print(num2, " es el número mayor")
elif (num3>num1 and num3>num2 and num3>num4):
	print(num3, " es el número mayor")
else:
	print(num4, " es el número mayor")

