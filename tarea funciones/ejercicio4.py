def invertir_cadena(texto):
    # Caso base: texto vacío o de 1 carácter
    if len(texto) <= 1:
        return texto
    # Caso recursivo: último carácter + resto invertido
    return texto[-1] + invertir_cadena(texto[:-1])

# Prueba
cadena = "Algoritmia"
print("Texto invertido:", invertir_cadena(cadena))  # Salida: aimtirogla