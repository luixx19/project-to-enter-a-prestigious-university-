from isla import Isla

class Jugador:
    def __init__(self):
        self.vidas = 5
        self.tiene_llave = False

class Menu:
    @staticmethod
    def iniciar():
        while True:
            opcion = input("\n1. Jugar\n2. Salir\nElige: ")
            if opcion == "1":
                Menu.jugar()
            elif opcion == "2":
                print("baiii")
                break
            else:
                print("no se puede")


    @staticmethod
    def jugar():
        jugador = Jugador()
        isla = Isla()

        while jugador.vidas > 0 and not jugador.tiene_llave:
            isla.mostrar()
            print(f"Vidas: {jugador.vidas} | ¿Tienes la llave?: {'Sí' if jugador.tiene_llave else 'No'}")

            try:
                x, y = map(int, input("Ingresa X e Y (0-5) separados por espacio: ").split())
                if not (0 <= x < 6 and 0 <= y < 6):
                    raise ValueError
            except ValueError:
                print("intenta otra vez aaaa")
                continue

            mensaje = isla.explorar(x, y, jugador)
            print(mensaje)

        isla.mostrar()
        print(f"Juego terminado. Vidas finales: {jugador.vidas}")


Menu.iniciar()