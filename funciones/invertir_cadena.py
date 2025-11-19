def invertir(cadena):
    if len(cadena) == 0:
        return ""
    elif len(cadena) == 1:
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1])

print(invertir("hola"))