from pokemon import Pokemon

class TipoHierba(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo="Hierba"):
        super().__init__(nombre, defensa, ataque, tipo)