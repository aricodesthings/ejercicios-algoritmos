def promedio_calificaciones():
    calificaciones = {}
    
    while True:
        entrada = input("Ingrese 'nombre: nota' o 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            break
        
        if ':' in entrada:
            nombre, nota = entrada.split(':')
            calificaciones[nombre.strip()] = float(nota.strip())
    
    if calificaciones:
        promedio = sum(calificaciones.values()) / len(calificaciones)
        print(f"Promedio general: {promedio}")
    else:
        print("No se ingresaron calificaciones")