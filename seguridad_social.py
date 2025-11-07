salario = float(input("Ingresa el salario base: "))

salud = 0.04 * salario
pension = 0.04 * salario
neto = salario - salud - pension

print("El salario neto del empleado es:", neto)