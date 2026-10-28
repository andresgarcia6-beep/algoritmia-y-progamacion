def pares_al_cuadrado_recursivo(lista):
    # Caso base: lista vacía
    if not lista:
        return []
    
    # Evaluar el primer elemento
    cabeza = lista[0]
    resto = pares_al_cuadrado_recursivo(lista[1:])
    
    if cabeza % 2 == 0:
        return [cabeza ** 2] + resto
    else:
        return resto

# Prueba
numeros = [1, 2, 3, 4, 5, 6]
print("Pares al cuadrado:", pares_al_cuadrado_recursivo(numeros))  # Salida: [4, 16, 36]