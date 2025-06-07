from tipoelectrico import TipoElectrico

class Pikachu(TipoElectrico):
    def __init__(self, nombre, defensa=50, ataque=55, tipo="N/A"):
        super().__init__("Pikachu", defensa, ataque, tipo)