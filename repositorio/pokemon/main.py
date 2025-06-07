from pikachu import Pikachu
from raichu import Raichu
from bulbasaur import Bulbasaur
from charmander import Charmander

from fuego import TipoFuego

def main():
    pika = Pikachu()
    print(pika)

    rai = Raichu()
    print(rai)

    bul = Bulbasaur()
    print(bul)

    char = Charmander
    print(char)

    fuego= TipoFuego("Charmelion", 80, 90)
    print(fuego)

if __name__ == "__main__":
    main()