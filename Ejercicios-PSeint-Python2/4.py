nota1 = float(input("Ingrese la nota 1 del estudiante: "))
nota2 = float(input("Ingrese la nota 2 del estudiante: "))
nota3 = float(input("Ingrese la nota 3 del estudiante: "))
nota4 = float(input("Ingrese la nota 4 del estudiante: "))
nota5 = float(input("Ingrese la nota 5 del estudiante: "))

promedio = nota1 + nota2 + nota3+ nota4+ nota5 / 5

if promedio > 3.5:
    print(f"Ganó el curso con una nota de {promedio:.2f}.")
else:
    print(f"Perdió el curso con una nota de {promedio:.2f}.")