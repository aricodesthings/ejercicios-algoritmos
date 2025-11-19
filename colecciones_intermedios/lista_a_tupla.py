def lista_a_tupla_sin_duplicados():
    elementos = input("Ingrese elementos separados por espacios: ").split()
    tupla_sin_duplicados = tuple(set(elementos))
    print(tupla_sin_duplicados)