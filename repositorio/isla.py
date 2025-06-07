import random
from objetos import Cocodrilo
from objetos import Llave
from objetos import Fruta
from objetos import Roca
from objetos import SerpientesEscorpiones

class Isla:
    def __init__(self):
        objetos = [Roca()] * 3 + [Fruta()] * 3
        objetos += [SerpientesEscorpiones("🐍")] * 2 + [SerpientesEscorpiones("🦂")] * 2
        objetos += [Cocodrilo()] + [Llave()]
        objetos += random.choices([Roca(), Fruta(), SerpientesEscorpiones("🐍"), SerpientesEscorpiones("🦂")], k=14)
        random.shuffle(objetos)

        self.mapa = [[None for _ in range(6)] for _ in range(6)]
        posiciones = [(i, j) for i in range(6) for j in range(6)]
        random.shuffle(posiciones)

        for pos, obj in zip(posiciones, objetos):
            x, y = pos
            self.mapa[x][y] = obj

        self.explorado = [[False] * 6 for _ in range(6)]


    def mostrar(self):
        print("\nMapa:")
        for i in range(6):
            print(" ".join(self.mapa[i][j].simbolo if self.explorado[i][j] else "■" for j in range(6)))
        print()


    def explorar(self, x, y, jugador):
        if not (0 <= x < 6 and 0 <= y < 6):
            return "fuera de rango pipip"
        
        if self.explorado[x][y]:
            return "ya pasaste por estos lares"

        self.explorado[x][y] = True
        return self.mapa[x][y].interactuar(jugador)
