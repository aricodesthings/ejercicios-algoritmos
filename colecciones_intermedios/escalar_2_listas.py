def producto_escalar():
    lista_a = list(map(int, input("Lista A: ").split()))
    lista_b = list(map(int, input("Lista B: ").split()))
    
    if len(lista_a) != len(lista_b):
        print("Las listas deben tener el mismo tamaño")
        return
    
    producto = sum(a * b for a, b in zip(lista_a, lista_b))
    print(f"Producto escalar = {producto}")