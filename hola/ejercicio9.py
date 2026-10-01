# Ejercicio 9
# Precondición: formato <[alfanumérico], [numérico]/[numérico]> (ej. "Lunes, 05/03")
fecha_input = input("Ingrese la fecha (formato 'día, DD/MM'): ").strip()

try:
    # 1. Extracción de partes usando split
    partes = fecha_input.split(",")
    dia_semana = partes[0].strip().lower()
    
    fecha_partes = partes[1].strip().split("/")
    dia_num = int(fecha_partes[0])
    mes_num = int(fecha_partes[1])

    dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]

    # 2. Validación de día, número de día y mes
    if dia_semana not in dias_validos or dia_num > 31 or mes_num > 12 or dia_num < 1 or mes_num < 1:
        print("Se produjo un error")
    else:
        # Nivel Inicial, Intermedio o Avanzado
        if dia_semana in ["lunes", "martes", "miércoles", "miercoles"]:
            examen = input("¿Se tomaron exámenes ese día? (si/no): ").strip().lower()
            if examen == "si":
                aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
                reprobados = int(input("Ingrese cantidad de alumnos reprobados: "))
                total_alumnos = aprobados + reprobados
                
                if total_alumnos > 0:
                    porcentaje = (aprobados / total_alumnos) * 100
                    print(f"Porcentaje de aprobados: {porcentaje:.2f}%")
                else:
                    print("No se registraron alumnos.")

        # Práctica Hablada
        elif dia_semana == "jueves":
            asistencia = float(input("Ingrese el porcentaje de asistencia (0-100): "))
            if asistencia > 50:
                print("Asistió la mayoría")
            else:
                print("No asistió la mayoría")

        # Inglés para Viajeros
        elif dia_semana == "viernes":
            if dia_num == 1 and (mes_num == 1 or mes_num == 7):
                print("Comienzo de nuevo ciclo")
                cant_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
                ingreso_total = cant_alumnos * arancel
                print(f"Ingreso total: ${ingreso_total:,.2f}")

except Exception:
    print("Se produjo un error")