from tipoelectrico import TipoElectrico

class Raichu(TipoElectrico):
    def __init__(self, nombre, defensa=60, ataque=90, tipo="N/A"):
        super().__init__("Raichu", defensa, ataque, tipo)