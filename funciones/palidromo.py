def es_palindromo(cadena):

    cadena_limpia = cadena.lower().replace(" ", "")
    
    return cadena_limpia == cadena_limpia[::-1]

# PRUEBAS
print(es_palindromo("anita lava la tina")) 
print(es_palindromo("hola"))                
print(es_palindromo("reconocer"))           