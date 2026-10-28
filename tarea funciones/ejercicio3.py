def suma_recursiva(lista):
    # Caso base: lista vacía
    if not lista:
        return 0
    # Caso recursivo: primer elemento + suma del resto
    return lista[0] + suma_recursiva(lista[1:])

# Prueba
valores = [10, 20, 30, 40]
print("Suma total:", suma_recursiva(valores))  # Salida: 100