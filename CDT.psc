Algoritmo CDT
	Definir valor_int, cantidad, porc_int, period, descuen, ganan Como Real
	Escribir "Ingrese la cantidad de dinero que invirtió en el CDT: "
	Leer cantidad
	Escribir "Ingrese el porcentaje de intereses: "
	Leer porc_int
	Escribir "Ingrese el periodo en el que el CDT estará activo en días: "
	Leer period
	porc_int = porc_int/100
	descuen = 0.07
	valor_int = (cantidad*porc_int*period)/360
	descuen = valor_int*descuen
	ganan = (cantidad+valor_int)-descuen
	Escribir "El valor de los intereses es: ", valor_int, ", el descuento por los impuestos es: ", descuen, " y la ganancia total es: ", ganan
	
	
	
	
	
	
FinAlgoritmo
