notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Draco": [4.5, 4.2, 5.0],
    "Neville": [2.5, 3.0, 3.2]
}

def calcular_promedio_simple(notas_estudiante):
    return sum(notas_estudiante) / len(notas_estudiante)

def calcular_promedio_ponderado(notas_estudiante):
    # Ponderaciones: 30%, 30%, 40%
    return (notas_estudiante[0] * 0.30) + (notas_estudiante[1] * 0.30) + (notas_estudiante[2] * 0.40)

def mayor_promedio_final(diccionario_notas):
    mejor_estudiante = None
    mejor_promedio = -1.0
    for est, lista_notas in diccionario_notas.items():
        prom = calcular_promedio_ponderado(lista_notas)
        if prom > mejor_promedio:
            mejor_promedio = prom
            mejor_estudiante = est
    return mejor_estudiante, mejor_promedio

def mostrar_aprobados(diccionario_notas):
    print("--- ESTUDIANTES APROBADOS (>= 3.0) ---")
    for est, lista_notas in diccionario_notas.items():
        prom = calcular_promedio_ponderado(lista_notas)
        if prom >= 3.0:
            print(f"- {est}: {prom:.2f}")

def reporte_profesora_mcgonagall(diccionario_notas):
    print("\n--- REPORTE CLASE DE LA PROFESORA MCGONAGALL ---")
    for est, lista_notas in diccionario_notas.items():
        prom = calcular_promedio_ponderado(lista_notas)
        estado = "APROBÓ" if prom >= 3.0 else "REPROBÓ"
        print(f"El estudiante {est} {estado} la clase con un promedio de {prom:.2f}.")

# Ejecución
print("1. Promedios Simples:")
for est, n in notas.items():
    print(f" - {est}: {calcular_promedio_simple(n):.2f}")

mejor_est, mejor_prom = mayor_promedio_final(notas)
print(f"\n2. El estudiante con mayor promedio final es {mejor_est} con {mejor_prom:.2f}.\n")

mostrar_aprobados(notas)
reporte_profesora_mcgonagall(notas)