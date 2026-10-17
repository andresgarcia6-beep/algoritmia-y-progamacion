def maquina_arroz(ciclos_a_ejecutar=6):
    """
    Simula la máquina empacadora de arroz continua.
    Usa una LISTA en Python para representar el empaque dentro de la caja.
    """
    caja_distribucion = []  # Estructura de almacenamiento de datos para la caja
    CAPACIDAD_CAJA = 3       # Número de bolsas por caja
    bolsas_procesadas = 0
    
    print("=" * 50)
    print(" 🌾 MÁQUINA EMPACADORA DE ARROZ AUTOMÁTICA")
    print("=" * 50)
    
    while bolsas_procesadas < ciclos_a_ejecutar:
        print(f"\n--- Procesando Bolsa #{bolsas_procesadas + 1} ---")
        
        # 1. Verificar si hay bolsa mediante el sensor
        hay_bolsa = True
        
        if hay_bolsa:
            print("1. 🔍 Sensor: Bolsa detectada en la posición.")
            print("2. ⏳ Vaciando arroz en la bolsa...")
            print("3. 🔥 Sellando bolsa herméticamente...")
            
            bolsas_procesadas += 1
            nombre_bolsa = f"Bolsa_Arroz_#{bolsas_procesadas}"
            caja_distribucion.append(nombre_bolsa)
            print(f"4. 📦 '{nombre_bolsa}' empacada en la caja de distribución.")
            
            # Verificar si la caja llegó a su límite para despacharla
            if len(caja_distribucion) == CAPACIDAD_CAJA:
                print("\n🚨 ¡CAJA LLENA! 🚨")
                print(f"📦 Contenido enviado: {caja_distribucion}")
                print("🚚 Despachando caja al área de distribución...")
                caja_distribucion.clear()  # Se vacía la caja para la siguiente ronda
        else:
            print("⚠️ Alerta: No hay bolsa en el sensor. Esperando...")

    print("\n" + "=" * 50)
    print("PROCESO DE EMPAQUE COMPLETADO EXITOSAMENTE.")
    print("=" * 50)

# Salvaguarda de ejecución principal
if __name__ == "__main__":
    maquina_arroz()