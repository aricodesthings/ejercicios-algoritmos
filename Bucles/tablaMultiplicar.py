tabla = int(input("¿Qué tabla desea repasar? (1-20): "))

if tabla < 1 or tabla > 20:
    print("Tabla no válida")
else:
    aciertos = 0
    
    print("Tabla del", tabla)
    for i in range(1, 11):
        respuesta = int(input(str(tabla) + " x " + str(i) + " = "))
        resultado_correcto = tabla * i
        
        if respuesta == resultado_correcto:
            print("¡Correcto! ¡Felicitaciones!")
            aciertos = aciertos + 1
        else:
            print("Incorrecto. El resultado es:", resultado_correcto)
    
    print("Aciertos:", aciertos, "de 10")
    
    if aciertos <= 5:
        print("Valoración: Insuficiente")
    elif aciertos == 6 or aciertos == 7:
        print("Valoración: Aceptable")
    elif aciertos == 8 or aciertos == 9:
        print("Valoración: Sobresaliente")
    else:
        print("Valoración: Excelente")