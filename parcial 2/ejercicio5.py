import random

def elegir_dificultad():
    print("Seleccione el nivel de dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (6 intentos)")
    print("3. Difícil (3 intentos)")
    opcion = input("Ingrese 1, 2 o 3: ")
    if opcion == "1":
        return 10
    elif opcion == "2":
        return 6
    elif opcion == "3":
        return 3
    else:
        print("Opción inválida. Se seleccionará modo Medio por defecto.")
        return 6

def generar_numero():
    return random.randint(1, 100)

def guardar_historial(resultado, intentos_usados):
    with open("historial_juego.txt", "a") as archivo:
        archivo.write(f"Resultado: {resultado} | Intentos utilizados: {intentos_usados}\n")

def jugar(intentos):
    frecuencia_secreta = generar_numero()
    intentos_restantes = intentos
    intentos_usados = 0

    print(f"\n¡Bienvenido! Debes adivinar la frecuencia de resonancia (1 a 100 Hz).")

    while intentos_restantes > 0:
        print(f"\nIntentos restantes: {intentos_restantes}")
        try:
            intento_usuario = int(input("Ingrese su frecuencia estimada (Hz): "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        intentos_usados += 1
        intentos_restantes -= 1

        if intento_usuario == frecuencia_secreta:
            print(f"¡Felicidades! Has sintonizado la frecuencia exacta: {frecuencia_secreta} Hz.")
            guardar_historial("Victoria", intentos_usados)
            return
        elif intento_usuario < frecuencia_secreta:
            print("PISTA: La frecuencia sintonizada es MAYOR a la ingresada.")
        else:
            print("PISTA: La frecuencia sintonizada es MENOR a la ingresada.")

    print(f"\n¡Se agotaron los intentos! La frecuencia secreta era {frecuencia_secreta} Hz.")
    guardar_historial("Derrota", intentos_usados)

# Descomentamos esta línea para iniciar el juego:
jugar(elegir_dificultad())