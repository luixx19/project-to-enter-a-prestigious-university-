'''
mi diario de habitos.

Este programa permite llevar un registro de los hábitos 
diarios. Una app por consola donde puedes agregar hábitos
(como “Estudiar inglés”),marcar si los cumpliste cada
día, y guardar el historial en un archivo .json.

Aprenderás:

Entrada/salida de datos

Manejo de archivos JSON

Diccionarios, listas, funciones básicas

Estructura tipo CRUD (crear, leer, actualizar, eliminar)

Ideas para expandirlo después:

Mostrar porcentaje de cumplimiento

Graficar el progreso

Interfaz gráfica con Tkinter
'''

import json


def cargar_habitos():
    try:
        with open('habitos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

def guardar_habitos(habitos):
    with open('habitos.json', 'w') as file:
        json.dump(habitos, file, indent=4)


def agregar_habito(habitos):
    nombre = input("Nombre del hábito: ")
    if nombre in habitos:
        print("El hábito ya existe.")
    else:
        habitos[nombre] = []
        print(f"Hábito '{nombre}' agregado.")



def marcar_habito(habitos): 
    nombre = input("Nombre del hábito: ")
    if nombre in habitos:
        dia = input("Día (DD/MM): ")
        habitos[nombre].append(dia)
        print(f"Hábito '{nombre}' marcado para el día {dia}.")
    else:
        print("El hábito no existe.")



def mostrar_habitos(habitos):
    if not habitos:
        print("No hay hábitos registrados.")
    else:
        for nombre, dias in habitos.items():
            print(f"{nombre}: {', '.join(dias) if dias else 'No marcado'}")


def eliminar_habito(habitos):       
    nombre = input("Nombre del hábito a eliminar: ")
    if nombre in habitos:
        del habitos[nombre]
        print(f"Hábito '{nombre}' eliminado.")
    else:
        print("El hábito no existe.")


def menu():
    print("\n--- Mi Diario de Hábitos ---")
    print("1. Agregar hábito")
    print("2. Marcar hábito")
    print("3. Mostrar hábitos")
    print("4. Eliminar hábito")
    print("5. Salir")
    return input("Seleccione una opción: ")


def main():
    habitos = cargar_habitos()
    while True:
        opcion = menu()
        if opcion == '1':
            agregar_habito(habitos)
        elif opcion == '2':
            marcar_habito(habitos)
        elif opcion == '3':
            mostrar_habitos(habitos)
        elif opcion == '4':
            eliminar_habito(habitos)
        elif opcion == '5':
            guardar_habitos(habitos)
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
if __name__ == "__main__":
    main()