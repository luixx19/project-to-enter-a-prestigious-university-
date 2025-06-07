from mamifero import Mamifero
from oviparo import Oviparo
from venenoso import Venenoso

class Ornitorrinco(Mamifero, Oviparo, Venenoso):
  def __init__(self, nombre, edad, especie="Mamifero"):
    super().__init__(nombre, edad, especie)
    self.NUMERO_HUEVOS = 0