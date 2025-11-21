n = int(input("Ingrese la cantidad de estudiantes: "))

aprobados = 0
reprobados = 0
suma_notas = 0

for i in range(n):
    codigo = input("Ingrese código del estudiante: ")
    nota = float(input("Ingrese nota del estudiante: "))
    
    suma_notas = suma_notas + nota
    
    if nota >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

promedio = suma_notas / n

print("Resultados:")
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
print("Promedio general:", promedio)