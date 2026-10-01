# Ejercicio 4
numero = int(input("Ingrese un número entero: "))

# Si el número es negativo, se multiplica por -1 para volverlo positivo
if numero < 0:
    valor_absoluto = numero * -1
else:
    valor_absoluto = numero

print(f"El valor absoluto de {numero} es: {valor_absoluto}")