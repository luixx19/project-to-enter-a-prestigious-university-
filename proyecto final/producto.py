class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} | {self.categoria} | ${self.precio:.2f} | Stock: {self.stock}"
