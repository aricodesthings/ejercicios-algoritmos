votos_android = 0
votos_ios = 0
otros = 0

while True:
    codigo = input("Ingrese código del estudiante (o 'fin' para terminar): ")
    
    if codigo == "fin":
        break
    
    plataforma = input("Ingrese plataforma (Android/iOS): ")
    
    if plataforma == "Android" or plataforma == "android":
        votos_android = votos_android + 1
    elif plataforma == "iOS" or plataforma == "ios":
        votos_ios = votos_ios + 1
    else:
        print("Plataforma no válida")
        otros = otros + 1

print("Resultados:")
print("Android:", votos_android, "votos")
print("iOS:", votos_ios, "votos")
print("Votos no válidos:", otros)

if votos_android > votos_ios:
    print("Se elegirá Android")
elif votos_ios > votos_android:
    print("Se elegirá iOS")
else:
    print("Empate. Se usará otro método")