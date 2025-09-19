import json # Módulo para trabajar con datos JSON (guardar/cargar).
import os # Módulo para interactuar con el sistema operativo (ej. chequear si un archivo existe).

def pausar():
input("\nPresiona ENTER para continuar...")
DATA_FILE = "data.json"



DATA_FILE = "data.json"
# 🚩 Define todas las claves que el programa necesita
REQUIRED_KEYS = ["turnos", "tarifas", "reservas", "huespedes"]

def cargar_datos():
data = {} # Inicializa un diccionario vacío por defecto
if os.path.exists(DATA_FILE):
try:
with open(DATA_FILE, "r") as f:
data = json.load(f)
except json.JSONDecodeError:
print("⚠️ Archivo de datos dañado. Reiniciando datos...")

# 🛠️ Verifica que todas las claves requeridas existan
for key in REQUIRED_KEYS:
if key not in data:
# Añade la clave faltante con un valor por defecto (lista o diccionario vacío)
if key == "tarifas":
data[key] = {}
else:
data[key] = []

return data

def guardar_datos(data):
with open(DATA_FILE, "w") as f:
json.dump(data, f, indent=4) # Guarda el diccionario de Python como texto JSON en el archivo.

# --- Login ---
def login():
password = input("Ingresa la contraseña del recepcionista: ").strip() # .strip() quita los espacios en blanco del inicio y final.
if password == "1234":
print("¡Bienvenido, Recepcionista!")
menu_recepcionista()
else:
print("Contraseña incorrecta. Intenta de nuevo.")

# --- Menú ---
def menu_recepcionista():
while True:
print("\n--- Menú de Recepcionista ---")
print("1. Registrar huésped")
print("2. Crear reserva")
print("3. Consultar disponibilidad")
print("4. Eliminar reserva")
print("5. Salir al menú principal")
opcion = input("Selecciona una opción: ").strip()

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
print("⚠️ Opción no válida. Intenta de nuevo.")

# --- Funciones con persistencia ---
def registrar_huesped():
data = cargar_datos()
print("\n--- Proceso de Registro de Huésped ---")
huesped_id = input("Ingresa la identificación (ID numérico) del huésped: ").strip()

if not huesped_id.isdigit(): # .isdigit() verifica si una cadena contiene solo dígitos.
print("⚠️ El ID debe ser numérico.")
return

nombre = input("Ingresa el nombre del huésped: ").strip()
if not nombre.replace(" ", "").isalpha(): # Permite nombres con espacios, verificando que el resto sean letras.
print("⚠️ El nombre debe contener solo letras.")
return

# Evitar duplicados
for h in data["huespedes"]:
if h["id"] == huesped_id:
print("⚠️ Ya existe un huésped con ese ID.")
return

data["huespedes"].append({ # .append() añade un nuevo diccionario (el huésped) a la lista de huéspedes.
"id": huesped_id,
"nombre": nombre
})
guardar_datos(data)

print(f"✅ Huésped {nombre} con ID {huesped_id} registrado exitosamente.")

def crear_reserva():
data = cargar_datos()
print("\n--- Proceso de Creación de Reserva ---")
huesped_info = input("Ingresa el nombre o ID del huésped: ").strip()
fecha = input("Ingresa la fecha de la reserva (dd/mm/aaaa): ").strip()
habitacion = input("Ingresa el tipo de habitación: ").strip()

if not fecha or not habitacion:
print("⚠️ Debes ingresar todos los datos de la reserva.")
return

reserva = {
"cliente": huesped_info,
"fecha": fecha,
"habitacion": habitacion
}
data["reservas"].append(reserva)
guardar_datos(data)

print(f"✅ Reserva creada para {huesped_info} en {habitacion} el {fecha}.")

def consultar_disponibilidad():
data = cargar_datos()
print("\n--- Proceso de Consulta de Disponibilidad ---")
fecha = input("Ingresa la fecha para consultar (dd/mm/aaaa): ").strip()

reservas_fecha = [r for r in data["reservas"] if r["fecha"] == fecha] # Comprensión de listas: forma corta de filtrar elementos.
if reservas_fecha:
print(f"📅 Ya hay {len(reservas_fecha)} reservas en {fecha}.") # len() cuenta los elementos de la lista.
else:
print(f"✅ Todas las habitaciones están disponibles en {fecha}.")

def eliminar_reserva():
data = cargar_datos()
print("\n--- Proceso de Eliminación de Reserva ---")
reserva_id = input("Ingresa el nombre o ID del huésped de la reserva a eliminar: ").strip()

nuevas_reservas = [r for r in data["reservas"] if r["cliente"] != reserva_id] # Comprensión de listas para crear una nueva lista sin la reserva a eliminar.

if len(nuevas_reservas) < len(data["reservas"]): # Compara si se encontró y eliminó una reserva. len() cuenta los elementos de la lista.
data["reservas"] = nuevas_reservas
guardar_datos(data)
print(f"✅ Reserva de {reserva_id} eliminada exitosamente.")
else:
print("⚠️ No se encontró ninguna reserva con ese dato.")
