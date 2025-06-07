
from colores import AZUL, AMARILLO, NEGRITA, VERDE, RESET 

class Administrador:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_menu(self):
        print(f"\n{NEGRITA}{AZUL}Menú del Administrador:{RESET}")
        print(f"{VERDE}1.{RESET} Agregar producto")
        print(f"{VERDE}2.{RESET} Ver productos")
        print(f"{VERDE}3.{RESET} Buscar producto")
        print(f"{VERDE}4.{RESET} Reabastecer stock")
        print(f"{VERDE}5.{RESET} Editar producto")
        print(f"{VERDE}6.{RESET} Eliminar producto")
        print(f"{VERDE}7.{RESET} Volver al menú principal")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_menu(self):
        print(f"\n{NEGRITA}{AZUL}Menú del Cliente:{RESET}")
        print(f"{AMARILLO}1.{RESET} Ver productos")
        print(f"{AMARILLO}2.{RESET} Ver carrito")
        print(f"{AMARILLO}3.{RESET} Buscar producto")
        print(f"{AMARILLO}4.{RESET} Finalizar compra")
        print(f"{AMARILLO}5.{RESET} Volver al menú principal")

