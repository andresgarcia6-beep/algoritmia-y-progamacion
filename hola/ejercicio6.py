# Ejercicio 6
entrada = input("Ingrese una sola letra: ").strip()

# 1. Validar que el usuario ingrese exactamente un carácter
if len(entrada) != 1:
    print("No se puede procesar el dato")
else:
    # Convertir a minúscula para evaluar mayúsculas y minúsculas por igual
    letra = entrada.lower()
    
    # 2. Evaluar si es una vocal
    if letra in "aeiouáéíóú":
        print("Es vocal")
    else:
        print("No es vocal")