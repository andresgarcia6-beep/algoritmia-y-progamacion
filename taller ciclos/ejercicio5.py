import random

# Posición inicial (x, y)
x = 0
y = 0

print(f"📌 Posición inicial: ({x}, {y})\n")
print("Recorriendo las 100 intersecciones...")

# Las 4 direcciones posibles en la cuadrícula tipo Manhattan:
# Norte (y+1), Sur (y-1), Este (x+1), Oeste (x-1)
direcciones = ["Norte", "Sur", "Este", "Oeste"]

# Ciclo para simular las 100 intersecciones
for paso in range(1, 101):
    eleccion = random.choice(direcciones)
    
    if eleccion == "Norte":
        y += 1
    elif eleccion == "Sur":
        y -= 1
    elif eleccion == "Este":
        x += 1
    elif eleccion == "Oeste":
        x -= 1

    # Imprimir el paso y la ubicación actual
    print(f"Paso {paso:3d}: Movimiento hacia el {eleccion:5s} -> Ubicación: ({x}, {y})")

print("\n" + "="*45)
print(f"📍 UBICACIÓN FINAL tras 100 pasos: ({x}, {y})")
# Distancia Manhattan desde el origen (0, 0)
distancia = abs(x) + abs(y)
print(f"📏 Desplazamiento total (Distancia Manhattan): {distancia} cuadras")
print("="*45)