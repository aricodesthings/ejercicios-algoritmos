def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print("¿Es 17 primo?", es_primo(17))
print("¿Es 15 primo?", es_primo(15))
print("¿Es 2 primo?", es_primo(2))
print("¿Es 1 primo?", es_primo(1))