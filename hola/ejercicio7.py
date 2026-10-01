# Ejercicio 7
numero = int(input("Ingrese un número entero: "))

# 1. Múltiplo de ambos (3 y 5)
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
# 2. Múltiplo solo de 3
elif numero % 3 == 0:
    print("Fizz")
# 3. Múltiplo solo de 5
elif numero % 5 == 0:
    print("Buzz")
# 4. No es múltiplo de ninguno
else:
    print(numero)