
import json
from usuario import Usuario

class ArchivoUsuarios:
    RUTA = "usuarios.json"

    @staticmethod
    def cargar():
        try:
            with open(ArchivoUsuarios.RUTA, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Usuario(**u) for u in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def guardar(usuarios):
        with open(ArchivoUsuarios.RUTA, "w", encoding="utf-8") as f:
            data = [vars(u) for u in usuarios]
            json.dump(data, f, indent=4)
