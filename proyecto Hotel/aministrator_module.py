import json # Módulo para trabajar con datos en formato JSON (leer y escribir archivos).
import os # Módulo para interactuar con el sistema operativo, como chequear si un archivo existe.
DATA_FILE = "data.json"

# --- Manejo de JSON ---
def cargar_datos():
if not os.path.exists(DATA_FILE): # os.path.exists() es una función que comprueba si un archivo o directorio existe. Es muy útil para evitar errores al intentar abrir un archivo inexistente.
return {"turnos": [], "tarifas": {}, "reservas": []}
try: # El bloque try...except es fundamental para manejar errores, como el que se podría dar al intentar cargar un archivo JSON dañado.
with open(DATA_FILE, "r") as f: # Abre el archivo. 'with' asegura que se cierre automáticamente.
return json.load(f) # Carga el contenido JSON del archivo y lo convierte a un diccionario de Python.
except json.JSONDecodeError: # Captura un error si el archivo JSON está dañado o no es válido.
return {"turnos": [], "tarifas": {}, "reservas": [], "huespedes": []}

def guardar_datos(data):
with open(DATA_FILE, "w") as f:
json.dump(data, f, indent=4) # Guarda el diccionario de Python como texto JSON en el archivo.

# --- Utilidad: Pausa ---
def pausar():
input("\n🔹 Presiona ENTER para continuar...")

# --- Login ---
def login():
password = input("Ingresa la contraseña del administrador: ")
if password == "1234":
print("¡Bienvenido, Administrador!")
menu_administrador()
else:
print("Contraseña incorrecta. Intenta de nuevo.")

# --- Menú principal ---
def menu_administrador():
while True:
print("\n--- Menú de Administrador ---")
print("1. Asignar turnos y tareas")
print("2. Actualizar tarifas")
print("3. Generar reportes")
print("4. Consultar reservas")
print("5. Salir al menú principal")
opcion = input("Selecciona una opción: ").strip()

if opcion == '1':
asignar_turnos_tareas()
pausar()
elif opcion == '2':
actualizar_tarifas()
pausar()
elif opcion == '3':
generar_reportes()
pausar()
elif opcion == '4':
consultar_reservas()
pausar()
elif opcion == '5':
print("Cerrando sesión de administrador.")
break
else:
print("⚠️ Opción no válida. Intenta de nuevo.")

# --- Funciones con persistencia ---
def asignar_turnos_tareas():
data = cargar_datos()
empleado = input("Ingresa el nombre del empleado: ").strip()
if not empleado.isalpha(): # .isalpha() es un método de strings que valida si todos los caracteres son letras, útil para verificar entradas del usuario.
print("⚠️ El nombre del empleado debe contener solo letras.")
return

turno = input("Ingresa el turno (ej. 'Mañana'): ").strip()
tareas = input("Ingresa las tareas a realizar: ").strip()

data["turnos"].append({ # .append() es una función para agregar un nuevo elemento (en este caso un diccionario) a una lista.
"empleado": empleado,
"turno": turno,
"tareas": tareas
})
guardar_datos(data)

print(f"\n✅ Turno '{turno}' y tareas '{tareas}' asignadas a {empleado} (guardado en JSON).")

def actualizar_tarifas():
data = cargar_datos()
tipo_habitacion = input("Ingresa el tipo de habitación: ").strip()
try:
nueva_tarifa = float(input("Ingresa la nueva tarifa: ").strip()) # float() convierte la entrada a un número decimal, lo que puede causar un error si no se ingresa un número.
except ValueError: # Este except captura el error específico de cuando la conversión a float falla.
print("⚠️ Debes ingresar un número válido para la tarifa.")
return

data["tarifas"][tipo_habitacion] = nueva_tarifa
guardar_datos(data)

print(f"\n✅ Tarifa de '{tipo_habitacion}' actualizada a {nueva_tarifa} (guardado en JSON).")

def generar_reportes():
data = cargar_datos()
print("\n--- Proceso de Generación de Reportes ---")
print("1. Reporte de ocupación")
print("2. Reporte de tarifas")
print("3. Reporte de tareas de empleados")
opcion = input("Selecciona un reporte: ").strip()

if opcion == '1':
total_habitaciones = 20
ocupadas = len(data.get("reservas", [])) # .get() es un método de diccionario que permite obtener un valor de una clave de forma segura, devolviendo un valor por defecto si la clave no existe.
disponibles = total_habitaciones - ocupadas
porcentaje = (ocupadas / total_habitaciones) * 100

print(f"\n🏨 Reporte de Ocupación:")
print(f" - Habitaciones totales: {total_habitaciones}")
print(f" - Ocupadas: {ocupadas}")
print(f" - Disponibles: {disponibles}")
print(f" - Porcentaje de ocupación: {porcentaje:.2f}%") # {:.2f} es un f-string que formatea el número a dos decimales, útil para mostrar dinero o porcentajes.

elif opcion == '2':
print("\n💲 Reporte de tarifas:")
if data.get("tarifas"):
for tipo, tarifa in data["tarifas"].items(): # .items() es un método que devuelve una lista de pares (clave, valor) de un diccionario.
print(f" - {tipo}: {tarifa}")
else:
print("No hay tarifas registradas aún.")

elif opcion == '3':
print("\n📝 Reporte de tareas de empleados:")
if data.get("turnos"):
for turno in data["turnos"]: # Itera sobre la lista de diccionarios, lo que permite acceder a cada turno individualmente.
print(f"{turno['empleado']} - Turno: {turno['turno']} - Tareas: {turno['tareas']}")
else:
print("No hay turnos registrados aún.")
else:
print("⚠️ Opción no válida.")

def consultar_reservas():
data = cargar_datos()
print("\n--- Proceso de Consulta de Reservas ---")
reservas = data.get("reservas", [])
if not reservas:
print("No hay reservas registradas.")
else:
for r in reservas:
cliente = r.get("cliente", "N/A") # Uso de .get() para evitar errores si alguna clave no existe en un diccionario.
habitacion = r.get("habitacion", "N/A")
fecha = r.get("fecha", "N/A")
print(f"Cliente: {cliente} | Habitación: {habitacion} | Fecha: {fecha}")
