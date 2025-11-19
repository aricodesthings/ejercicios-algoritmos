CLAVE_CORRECTA = "admin123"
MAX_INTENTOS = 3

print("VALIDACIÓN DE CLAVE")

# Usando for para controlar intentos
for intento in range(1, MAX_INTENTOS + 1):
    clave = input(f"Intento {intento}/{MAX_INTENTOS}: Ingrese la clave: ")
    
    if clave == CLAVE_CORRECTA:
        print("¡Acceso concedido!")
        break
    else:
        intentos_restantes = MAX_INTENTOS - intento
        if intentos_restantes > 0:
            print(f"Clave incorrecta. Te quedan {intentos_restantes} intentos.")
        else:
            print("¡Acceso denegado! No hay más intentos.")