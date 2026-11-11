def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No es posible dividir entre cero.")
    return a / b

def potencia(base, exponente):
    """Potencia usando multiplicación internamente para exponentes enteros."""
    if exponente == 0:
        return 1
    resultado = 1
    for _ in range(abs(exponente)):
        resultado = multiplicacion(resultado, base)
    return resultado if exponente > 0 else division(1, resultado)

def raiz_cuadrada(x):
    """Aproximación de raíz cuadrada usando algoritmo de Newton basado en multiplicación."""
    if x < 0:
        raise ValueError("No existe raíz real para números negativos.")
    if x == 0:
        return 0.0
    estimacion = x / 2.0
    for _ in range(20):
        estimacion = 0.5 * (estimacion + division(x, estimacion))
    return estimacion

def factorial(n):
    """Calcula el factorial de n usando la función multiplicación."""
    if n < 0:
        raise ValueError("Factorial no definido para negativos.")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado = multiplicacion(resultado, i)
    return resultado

def inversa(x):
    """Retorna 1/x (Útil para admitancias Y = 1/Z)."""
    return division(1, x)

# Pruebas
print("--- PRUEBAS CALCULADORA MODULAR ---")
print("Suma 5 + 3:", suma(5, 3))
print("Potencia 2^4:", potencia(2, 4))
print("Raíz cuadrada de 25:", raiz_cuadrada(25))
print("Factorial de 5:", factorial(5))
print("Admitancia Y para Z=50 ohms (Inversa):", inversa(50), "Siemens")