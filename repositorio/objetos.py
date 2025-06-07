class ObjetoIsla:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def interactuar(self, jugador):
        return "chaoooo"

class Roca(ObjetoIsla):
    def __init__(self):
        self.simbolo = "🪨🪨"


class Fruta(ObjetoIsla):
    def __init__(self):
        self.simbolo = "🍍🍍🍍🥥"

    def interactuar(self, jugador):
        jugador.vidas += 1
        return "ganaste una vida🤰"


class SerpientesEscorpiones(ObjetoIsla):
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def interactuar(self, jugador):
        jugador.vidas -= 1
        return f"¡Cuidado! {self.simbolo} te ha hecho daño."


class Cocodrilo(ObjetoIsla):
    def __init__(self):
        self.simbolo = "🐊"

    def interactuar(self, jugador):
        jugador.vidas = 0
        return "moristeee"


class Llave(ObjetoIsla):
    def __init__(self):
        self.simbolo = "🗝"

    def interactuar(self, jugador):
        jugador.tiene_llave = True
        return "ganasteee"