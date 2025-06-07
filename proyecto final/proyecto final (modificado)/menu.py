from colores import AZUL, CYAN, AMARILLO, NEGRITA, RESET, ROJO, VERDE



def menu_principal():
    print(f"{AZUL}" + "=" * 50)
    print(f"{NEGRITA}=========== TIENDITA EL MORRÓN PIMPÓN ==========={RESET}")
    print(f"{AZUL}" + "=" * 50 + f"{RESET}")
    print(f"{VERDE}1.{RESET} Ingresar como Administrador")
    print(f"{VERDE}2.{RESET} Ingresar como Cliente")
    print(f"{VERDE}3.{RESET} Salir")
    return input(f"{NEGRITA}Selecciona una opción:{RESET} ")


