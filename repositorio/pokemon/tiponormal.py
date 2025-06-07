from pokemon import Pokemon

class TipoNormal(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo="Normal"):
        super().__init__(nombre, defensa, ataque, tipo)
    
    def __str__(self):
        return "⬜"