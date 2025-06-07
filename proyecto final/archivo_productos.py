import json
from producto import Producto

class ArchivoProductos:
    RUTA = "productos.json"

    @staticmethod
    def cargar():
        try:
            with open(ArchivoProductos.RUTA, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Producto(**item) for item in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def guardar(productos):
        with open(ArchivoProductos.RUTA, "w", encoding="utf-8") as f:
            data = [vars(p) for p in productos]
            json.dump(data, f, indent=4)
