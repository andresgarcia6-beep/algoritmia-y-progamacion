productos = {
    "Papas": 2500,
    "Gaseosa": 3000,
    "Galletas": 1500,
    "Chocolatina": 2000,
    "Agua": 1200
}

def mostrar_productos(diccionario_prod):
    print("--- PRODUCTOS DISPONIBLES ---")
    for prod, precio in diccionario_prod.items():
        print(f"- {prod}: ${precio}")

def procesar_pago(precio_producto, dinero_ingresado):
    """Verifica el dinero ingresado y calcula si hay vuelto o falta dinero."""
    if dinero_ingresado < precio_producto:
        faltante = precio_producto - dinero_ingresado
        return False, faltante
    else:
        devuelta = dinero_ingresado - precio_producto
        return True, devuelta

def ejecutar_dispensadora():
    mostrar_productos(productos)
    eleccion = input("\nIngrese el nombre del producto que desea comprar: ").strip().capitalize()

    if eleccion not in productos:
        print("Error: El producto seleccionado no existe.")
        return

    precio = productos[eleccion]
    print(f"El producto '{eleccion}' cuesta ${precio}.")
    
    try:
        dinero = float(input("Ingrese el dinero para pagar: $"))
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return

    exito, cambio_o_falta = procesar_pago(precio, dinero)

    if exito:
        print(f"\n¡Compra exitosa! Se ha entregado su '{eleccion}'.")
        if cambio_o_falta > 0:
            print(f"Su devuelta es de: ${cambio_o_falta:.2f}")
        else:
            print("Pago exacto. No hay devuelta.")
    else:
        print(f"\n[ERROR] Dinero insuficiente. Le faltan ${cambio_o_falta:.2f} para completar la compra.")

# Esta es la línea que debe quedar activa para que corra:
ejecutar_dispensadora()