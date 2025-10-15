Algoritmo salud_pension
	Definir salud, pension, salario, neto Como Real
	Escribir "Ingresa el salario base: "
	Leer salario
	salud = 0.04
	pension = 0.04
	salud = salario*salud
	pension = salario*pension
	neto = (salario-salud)-pension
	Escribir "El salario neto del empleado es: ", neto
	
FinAlgoritmo
