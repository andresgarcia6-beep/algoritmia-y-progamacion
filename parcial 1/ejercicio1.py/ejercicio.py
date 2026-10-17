def sistema_restaurante():
    # Menú de la franquicia con opciones y precios
    menu = {
        1: {"nombre": "Hamburguesa Doble Queso", "precio": 12.0},
        2: {"nombre": "Perro Caliente Especial", "precio": 8.0},
        3: {"nombre": "Porción de Pizza", "precio": 10.0},
        4: {"nombre": "Papas Fritas Grandes", "precio": 5.0},
        5: {"nombre": "Gaseosa 500ml", "precio": 3.0}
    }
    
    total_a_pagar = 0.0
    pedidos_realizados = []
    
    print("=" * 50)
    print(" 🍔 ¡BIENVENIDO A FAST FOOD EXPRESS! 🍕")
    print("=" * 50)
    
    while True:
        print("\n--- NUESTRO MENÚ ---")
        for clave, item in menu.items():
            print(f"{clave}. {item['nombre']}: ${item['precio']:.2f}")
        
        try:
            opcion = int(input("\nPor favor, seleccione el número de su pedido: "))
            
            if opcion in menu:
                plato = menu[opcion]
                total_a_pagar += plato["precio"]
                pedidos_realizados.append(plato["nombre"])
                print(f"✅ ¡Excelente elección! Se agregó '{plato['nombre']}' (${plato['precio']:.2f}) al pedido.")
            else:
                # Mensaje de aviso cuando la opción no existe
                print("❌ ¡Epa! Ese plato no está en el menú. Ayuda a tu sobrino a elegir una opción entre el 1 y el 5 😉")
        
        except ValueError:
            print("❌ Entrada no válida. Debe ingresar el número entero de la opción.")
        
        continuar = input("\n¿Desea realizar otro pedido? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\n" + "=" * 50)
    print("🧾 RESUMEN FINAL DEL PEDIDO")
    print("=" * 50)
    if pedidos_realizados:
        for i, item in enumerate(pedidos_realizados, 1):
            print(f"{i}. {item}")
        print(f"\n💰 TOTAL A PAGAR: ${total_a_pagar:.2f}")
    else:
        print("No se realizó ningún pedido.")
    print("¡Gracias por su compra, vuelva pronto!")

# Salvaguarda de ejecución principal
if __name__ == "__main__":
    sistema_restaurante()