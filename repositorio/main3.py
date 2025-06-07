from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago
from ornitorrinco import Ornitorrinco


def main():
    # leon = Animal("Leon", 5)
    # leon.hacer_sonido()

    perro = Perro("Churro", 3, "Salchicha")
    perro.hacer_sonido()
    print(perro.es_cachorro())

    gato = Gato("Michi", 2, 2)
    gato.hacer_sonido()
    print("Vida(s) restante(s):", gato.vidas)
    print("Atropellado 😿" if not gato.sobrevive() else "Vive 😺")
    print("Vida(s) restante(s):", gato.vidas)
    print("Intoxicado ☠" if not gato.sobrevive() else "Vive 😺")
    print("Vida(s) restante(s):", gato.vidas)
    print("Electrocutado ⚡" if not gato.sobrevive() else "Vive 😺")
    print("Vida(s) restante(s):", gato.vidas)

    # ave = Ave("KP", 1)
    # ave.hacer_sonido()

    # dracula = Murcielago("Drácula", 100, "Vampiro")
    # dracula.hacer_sonido()
    # dracula.soy_un()
    perry = Ornitorrinco("Perry", 5)
    perry.hacer_sonido()
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevo(s)")
    for i in range(3):
        perry.poner_huevo()
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevo(s)")


if __name__ == '__main__':
    main()