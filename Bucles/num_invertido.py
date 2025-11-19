numero = int(input("Ingrese un número entero: "))

numero_invertido = 0
numero_original = numero

es_negativo = False
if numero < 0:
    es_negativo = True
    numero = -numero

while numero > 0:
    ultimo_digito = numero % 10
    
    numero_invertido = numero_invertido * 10 + ultimo_digito
    
    numero = numero // 10

if es_negativo:
    numero_invertido = -numero_invertido

print(f"El número {numero_original} invertido es: {numero_invertido}")