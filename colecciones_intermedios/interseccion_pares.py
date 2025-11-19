def pares_comunes():
    A = [2, 4, 6, 8]
    B = [4, 5, 6, 9]
    
    pares_A = {x for x in A if x % 2 == 0}
    pares_B = {x for x in B if x % 2 == 0}
    comunes = pares_A & pares_B
    
    print(comunes)