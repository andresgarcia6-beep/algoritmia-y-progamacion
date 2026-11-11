# Lista de 24 lecturas de voltaje durante el día (Nodo de Subestación)
lecturas_voltaje = [
    118.5, 119.0, 118.2, 117.8, 118.0, 119.5,
    120.1, 121.5, 122.0, 121.8, 120.5, 119.8,
    118.0, 117.5, 116.8, 118.2, 119.0, 121.0,
    122.5, 123.0, 121.2, 119.5, 118.8, 118.1
]

def calcular_promedio(lista):
    """Calcula el promedio de una lista de voltajes."""
    return sum(lista) / len(lista)

def obtener_extremos(lista):
    """Retorna el voltaje mínimo y máximo de la lista."""
    voltaje_min = min(lista)
    voltaje_max = max(lista)
    return voltaje_min, voltaje_max

def contar_sobre_promedio(lista):
    """Cuenta cuántas horas estuvo el voltaje por encima del promedio diario."""
    prom = calcular_promedio(lista)
    horas = sum(1 for v in lista if v > prom)
    return horas

# Programa Principal
promedio = calcular_promedio(lecturas_voltaje)
v_min, v_max = obtener_extremos(lecturas_voltaje)
horas_sobre = contar_sobre_promedio(lecturas_voltaje)

print("--- REPORTE DE VOLTAJE DIARIO ---")
print(f"Voltaje promedio del día: {promedio:.2f} V")
print(f"Voltaje más bajo: {v_min} V | Voltaje más alto: {v_max} V")
print(f"Horas por encima del promedio: {horas_sobre} horas")