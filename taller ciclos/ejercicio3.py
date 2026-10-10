# Pedir al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ").strip()

print(f"\nSubcadenas de '{palabra}' ordenadas por longitud:\n")

n = len(palabra)

# El ciclo exterior determina la longitud de la subcadena (de 1 a n)
for longitud in range(1, n + 1):
    # El ciclo interior recorre la palabra generando las subcadenas de dicha longitud
    for inicio in range(n - longitud + 1):
        subcadena = palabra[inicio : inicio + longitud]
        print(subcadena)