def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)

# Prueba
print("Factorial de 5:", factorial(5))  # Salida: 120