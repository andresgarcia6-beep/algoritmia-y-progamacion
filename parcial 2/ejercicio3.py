def agregar_componente(diccionario, nombre, cantidad, precio):
    """Agrega o actualiza un componente en el inventario."""
    diccionario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Componente '{nombre}' agregado/actualizado con éxito.")

def eliminar_componente(diccionario, nombre):
    """Elimina un componente del inventario si existe."""
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"Componente '{nombre}' eliminado con éxito.")
    else:
        print(f"El componente '{nombre}' no se encuentra en el inventario.")

def calcular_valor_total(diccionario):
    """Calcula el valor monetario total almacenado en el laboratorio."""
    total = sum(item["cantidad"] * item["precio"] for item in diccionario.values())
    return total

def mostrar_inventario(diccionario):
    """Muestra de forma organizada el inventario actual."""
    print("\n--- INVENTARIO DEL LABORATORIO ---")
    if not diccionario:
        print("El inventario está vacío.")
        return
    for nombre, datos in diccionario.items():
        print(f"- {nombre}: {datos['cantidad']} unidades | ${datos['precio']:.2f} c/u")
    print("---------------------------------")

# Programa interactivo/secuencial
inventario = {}
agregar_componente(inventario, "Resistencia 10k", 50, 0.15)
agregar_componente(inventario, "Capacitor 100uF", 30, 0.50)
agregar_componente(inventario, "Inductor 1mH", 20, 1.20)

mostrar_inventario(inventario)
print(f"Valor total del laboratorio: ${calcular_valor_total(inventario):.2f}\n")

eliminar_componente(inventario, "Capacitor 100uF")
mostrar_inventario(inventario)
print(f"Nuevo valor total del laboratorio: ${calcular_valor_total(inventario):.2f}")