from murcielago import Murcielago
from ornitorrinco import Ornitorrinco

def main():
  dracula = Murcielago(nombre="Drácula", especie="Vampiro", edad=500)
  dracula.comer()
  dracula.hacer_sonido()
  dracula.amamantar()
  dracula.dormir()
  dracula.volar()

  perry = Ornitorrinco(nombre="Perry", edad=7)
  print(f'{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos')
  perry.poner_huevo()
  perry.poner_huevo()
  perry.poner_huevo()
  print(f'{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos')
  print(f'{perry.especie}')



if __name__ == "__main__":
  main()