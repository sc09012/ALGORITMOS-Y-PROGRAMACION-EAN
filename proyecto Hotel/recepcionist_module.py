# receptionist_module.py

def login():
password = input("Ingresa la contraseña del recepcionista: ")
if password == "1234":
print("¡Bienvenido, Recepcionista!")
menu_recepcionista()
else:
print("Contraseña incorrecta. Intenta de nuevo.")

def menu_recepcionista():
while True:
print("\n--- Menú de Recepcionista ---")
print("1. Registrar huésped")
print("2. Crear reserva")
print("3. Consultar disponibilidad")
print("4. Eliminar reserva")
print("5. Salir al menú principal")
opcion = input("Selecciona una opción: ")

if opcion == '1':
registrar_huesped()
elif opcion == '2':
crear_reserva()
elif opcion == '3':
consultar_disponibilidad()
elif opcion == '4':
eliminar_reserva()
elif opcion == '5':
print("Cerrando sesión de recepcionista.")
break
else:
print("Opción no válida.")

def registrar_huesped():
print("--- Proceso de Registro de Huésped ---")
huesped_id = input("Ingresa la identificación (ID) del huésped: ")
nombre = input("Ingresa el nombre del huésped: ")
print(f"Huésped {nombre} con ID {huesped_id} registrado exitosamente.")

def crear_reserva():
print("--- Proceso de Creación de Reserva ---")
huesped_info = input("Ingresa la información del huésped: ")
fecha = input("Ingresa la fecha de la reserva (dd/mm/aaaa): ")
print(f"Verificando disponibilidad para el huésped {huesped_info} en la fecha {fecha}.")
# Aquí iría la lógica para verificar disponibilidad
print("Reserva creada y guardada.")

def consultar_disponibilidad():
print("--- Proceso de Consulta de Disponibilidad ---")
fecha = input("Ingresa la fecha para consultar (dd/mm/aaaa): ")
# Aquí iría la lógica para mostrar las habitaciones disponibles
print("Mostrando habitaciones disponibles para la fecha especificada.")

def eliminar_reserva():
print("--- Proceso de Eliminación de Reserva ---")
reserva_id = input("Ingresa el ID de la reserva a eliminar: ")
confirmacion = input(f"¿Estás seguro de que quieres eliminar la reserva {reserva_id}? (s/n): ").lower()
if confirmacion == 's':
print(f"Reserva {reserva_id} eliminada exitosamente.")
else:
print("Eliminación de reserva cancelada.")
