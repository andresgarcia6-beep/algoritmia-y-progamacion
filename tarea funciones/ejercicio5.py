def maximo_recursivo(lista):
    # Caso base: un solo elemento
    if len(lista) == 1:
        return lista[0]
    
    # Obtener el máximo del resto de la lista
    max_resto = maximo_recursivo(lista[1:])
    
    # Comparar el primer elemento con el máximo del resto
    if lista[0] > max_resto:
        return lista[0]
    else:
        return max_resto

# Prueba
datos = [15, 42, 8, 99, 23]
print("Número máximo:", maximo_recursivo(datos))  # Salida: 99