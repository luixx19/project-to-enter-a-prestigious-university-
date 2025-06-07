from pokemon import Pokemon

class TipoElectrico(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo="N/A"):
        super().__init__(nombre, defensa, ataque, "Electrico")