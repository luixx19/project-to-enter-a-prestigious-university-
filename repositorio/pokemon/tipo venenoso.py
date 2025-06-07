from pokemon import Pokemon

class TipoVenenoso(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo="Venenoso"):
        super().__init__(nombre, defensa, ataque, tipo)