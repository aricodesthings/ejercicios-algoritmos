print("Reloj Digital - 24 horas")

for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            hora_str = str(horas)
            minuto_str = str(minutos)
            segundo_str = str(segundos)
            
            if horas < 10:
                hora_str = "0" + hora_str
            if minutos < 10:
                minuto_str = "0" + minuto_str
            if segundos < 10:
                segundo_str = "0" + segundo_str
            
            print(hora_str + ":" + minuto_str + ":" + segundo_str)