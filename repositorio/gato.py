from animal import Animal

class Gato(Animal):
  def __init__(self, nombre, edad, vidas):
    super().__init__(nombre, edad)
    self.vidas = vidas

  def hacer_sonido(self):
    print(f"{self.nombre} esta maullando")
    print("Miau 😽😽😽")

  def sobrevive(self):
    if self.edad > 15 or self.vidas > 1:
      self.vidas -= 1
      return self.vidas