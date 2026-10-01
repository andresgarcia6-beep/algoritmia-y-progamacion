# Ejercicio 3
dia = input("Ingrese un día de la semana: ").strip().lower()

if dia == "lunes":
    print("¡Ánimo! Comenzando la semana laboral.")
elif dia == "viernes":
    print("¡Llegó el viernes! Casi es fin de semana.")
elif dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana! A descansar.")
else:
    print("Es un día común de la semana.")