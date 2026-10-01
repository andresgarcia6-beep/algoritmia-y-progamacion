# Ejercicio 8
print("Candidatos disponibles:")
print("A - Candidato A (Partido Rojo)")
print("B - Candidato B (Partido Verde)")
print("C - Candidato C (Partido Azul)")

opcion = input("Ingrese la letra de su candidato (A, B o C): ").strip().upper()

if opcion == "A":
    print("Usted ha votado por el partido rojo")
elif opcion == "B":
    print("Usted ha votado por el partido verde")
elif opcion == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")