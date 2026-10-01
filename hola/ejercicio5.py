# Ejercicio 5
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} ES bisiesto.")
else:
    print(f"El año {anio} NO es bisiesto.")