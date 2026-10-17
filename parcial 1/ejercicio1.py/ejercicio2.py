def calcular_precio(edad):
    """Calcula el precio de la entrada según el rango de edad."""
    if edad < 5:
        return 0
    elif 5 <= edad <= 18:
        return 5
    else:
        return 10

def sala_de_juegos():
    print("=" * 45)
    print(" 🎮 BIENVENIDO A LA SALA DE JUEGOS 🎯")
    print("=" * 45)
    
    total_grupo = 0
    
    while True:
        try:
            edad = int(input("\nIngrese la edad del cliente (o -1 para finalizar): "))
            
            if edad == -1:
                break
                
            if edad < 0:
                print("❌ La edad no puede ser un valor negativo.")
                continue
                
            precio = calcular_precio(edad)
            total_grupo += precio
            
            if precio == 0:
                print(f"👶 Cliente de {edad} años: ¡Entrada GRATIS ($0)!")
            else:
                print(f"🎟️ Cliente de {edad} años: Precio de entrada = ${precio}")
                
        except ValueError:
            print("❌ Error: Ingrese una edad válida en números enteros.")

    print("\n" + "=" * 45)
    print(f"💰 TOTAL A PAGAR POR EL GRUPO: ${total_grupo}")
    print("=" * 45)

# Salvaguarda de ejecución principal
if __name__ == "__main__":
    sala_de_juegos()