# Lista original
lista_original = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

print("📌 Lista original:", lista_original)

# ==========================================
# PARTE 1: Ordenamiento manual con CICLOS
# ==========================================
# Hacemos una copia para no alterar la lista original
lista_ciclos = lista_original.copy()
n = len(lista_ciclos)

# Algoritmo de Burbuja (Bubble Sort) con ciclos anidados
for i in range(n):
    for j in range(0, n - i - 1):
        if lista_ciclos[j] > lista_ciclos[j + 1]:
            # Intercambiamos los elementos de posición
            lista_ciclos[j], lista_ciclos[j + 1] = lista_ciclos[j + 1], lista_ciclos[j]

print("\n🔄 Lista ordenada con CICLOS (Bubble Sort):")
print(lista_ciclos)

# ==========================================
# PARTE 2: Verificación con FUNCIÓN PREDETERMINADA
# ==========================================
# Usamos la función predeterminada sorted() de Python
lista_verificada = sorted(lista_original)

print("\n✅ Lista ordenada con FUNCIÓN PREDETERMINADA (sorted):")
print(lista_verificada)

# ==========================================
# PARTE 3: Comprobación de funcionamiento
# ==========================================
print("\n" + "="*45)
if lista_ciclos == lista_verificada:
    print("🎉 ¡VERIFICACIÓN EXITOSA!")
    print("El algoritmo implementado con ciclos funciona correctamente.")
else:
    print("❌ Hubo un error en el ordenamiento.")
print("="*45)