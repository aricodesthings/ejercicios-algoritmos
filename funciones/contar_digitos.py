def contar_digitos(n):
    if n == 0:
        return 1
    
    n = abs(n)
    
    contador = 0
    while n > 0:
        contador += 1
        n //= 10
    
    return contador


print(contar_digitos(12345))
print(contar_digitos(-987))