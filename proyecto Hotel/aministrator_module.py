# administrator_module.py

def login():
    password = input("Ingresa la contraseña del administrador: ")
    if password == "1234":
        print("¡Bienvenido, Administrador!")
        menu_administrador()
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")

def menu_administrador():
    while True:
        print("\n--- Menú de Administrador ---")
        print("1. Asignar turnos y tareas")
        print("2. Actualizar tarifas")
        print("3. Generar reportes")
        print("4. Consultar reservas")
        print("5. Salir al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            asignar_turnos_tareas()
        elif opcion == '2':
            actualizar_tarifas()
        elif opcion == '3':
            generar_reportes()
        elif opcion == '4':
            consultar_reservas()
        elif opcion == '5':
            print("Cerrando sesión de administrador.")
            break
        else:
            print("Opción no válida.")

def asignar_turnos_tareas():
    print("--- Proceso de Asignación de Turnos y Tareas ---")
    empleado = input("Ingresa el nombre del empleado: ")
    turno = input("Ingresa el turno (ej. 'Mañana'): ")
    tareas = input("Ingresa las tareas a realizar: ")
    print(f"Turno '{turno}' y tareas '{tareas}' asignadas a {empleado}.")

def actualizar_tarifas():
    print("--- Proceso de Actualización de Tarifas ---")
    tipo_habitacion = input("Ingresa el tipo de habitación: ")
    nueva_tarifa = input("Ingresa la nueva tarifa: ")
    print(f"Tarifa de habitación '{tipo_habitacion}' actualizada a {nueva_tarifa}.")

def generar_reportes():
    print("--- Proceso de Generación de Reportes ---")
    reporte_tipo = input("¿Qué reporte quieres generar? (ocupación/tarifas): ").lower()
    if reporte_tipo == 'ocupación':
        print("Generando reporte de ocupación... (simulando 70% de ocupación).")
    elif reporte_tipo == 'tarifas':
        print("Generando reporte de tarifas... (simulando reporte de precios).")
    else:
        print("Tipo de reporte no válido.")

def consultar_reservas():
    print("--- Proceso de Consulta de Reservas ---")
    print("Mostrando todas las reservas existentes y su disponibilidad.")
    # Aquí iría la lógica para mostrar las reservas
