# Ejercicio 1
numero = int(input("Ingrese un número entre 10 y 50: "))

if numero < 10 or numero > 50:
    print("El número ingresado no está entre 10 y 50.")
elif numero == 30:
    print("Ganaste un premio")
else:
    print("Perdiste")