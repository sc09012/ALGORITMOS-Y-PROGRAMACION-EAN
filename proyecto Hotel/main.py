# main.py

import receptionist_module
import administrator_module

def main():
while True:
print("\n--- Sistema de Gestión de Hotel ---")
rol = input("¿Eres administrador o recepcionista? (a/r/salir): ").lower()

if rol == 'a':
administrator_module.login()
elif rol == 'r':
receptionist_module.login()
elif rol == 'salir':
print("Saliendo del programa.")
break
else:
print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
main()
