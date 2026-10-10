# Precios base y adicionales
PRECIO_BASE = 1.90

toppings = {
    "1": ("Sin topping", 0.00),
    "2": ("Frutas", 0.50),
    "3": ("Granola", 1.50),
    "4": ("Oreo", 1.00),
    "5": ("Brownie", 0.75)
}

total_a_pagar = 0.0
pedidos_realizados = 0

print("🍦 ¡Bienvenido a la Heladería Gourmet! 🍦")

while True:
    print("\n--- MENÚ DE TOPPINGS ---")
    print("1. Sin topping -------- $0.00")
    print("2. Topping de Frutas -- $0.50")
    print("3. Topping de Granola - $1.50")
    print("4. Topping de Oreo ---- $1.00")
    print("5. Topping de Brownie - $0.75")
    
    opcion = input("\nSeleccione el número del topping que desea para su helado (1-5): ").strip()

    if opcion in toppings:
        nombre_topping, precio_topping = toppings[opcion]
        precio_helado = PRECIO_BASE + precio_topping
        total_a_pagar += precio_helado
        pedidos_realizados += 1
        
        if opcion == "1":
            print(f"✨ ¡Un clásico! Tu helado sin topping cuesta ${precio_helado:.2f}")
        else:
            print(f"🎉 ¡Excelente elección! Tu helado con topping de {nombre_topping} cuesta ${precio_helado:.2f}")
    else:
        print("❌ Lo sentimos, no disponemos del topping solicitado en nuestro menú.")

    # Preguntar si desea otro pedido
    continuar = input("\n¿Desea ordenar otro helado? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Resumen final
print("\n" + "="*40)
if pedidos_realizados > 0:
    print(f"🛍️ Gracias por tu compra. Has pedido {pedidos_realizados} helado(s).")
    print(f"💳 El valor total a pagar es: ${total_a_pagar:.2f}")
    print("🍦 ¡Que disfrutes tu helado y vuelvas pronto!")
else:
    print("¡Esperamos verte pronto de nuevo!")
print("="*40)