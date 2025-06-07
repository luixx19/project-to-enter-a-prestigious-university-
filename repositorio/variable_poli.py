from animal import Animal  # Importa la clase base Animal
from gato import Gato  # Importa la clase Gato que hereda de Animal
from perro import Perro  # Importa la clase Perro que hereda de Animal
from zoo import Zoo  # Importa la clase Zoo para manejar un grupo de animales
from ave import Ave  # Importa la clase Ave que hereda de Animal
# Importa la clase Murciélago que hereda de Animal
from murcielago import Murcielago
# Importa la clase Ornitorrinco que hereda de Animal
from ornitorrinco import Ornitorrinco


def main():
    # Crear un objeto de la clase Animal
    mascota = Animal("Pelu", 5)
    # print(type(mascota))  # Imprime el tipo de objeto
    # Llamar al método comer de la clase Animal
    mascota.comer()

    # Cambiar la referencia de mascota a un objeto de la clase Perro
    mascota = Perro("Pelu", 5, "Chihuahua")
    # print(type(mascota))  # Imprime el tipo de objeto
    # Llamar al método comer de la clase Perro
    mascota.comer()

    # Cambiar la referencia de mascota a un objeto de la clase Gato
    mascota = Gato("Pelu", 5, 9)
    # print(type(mascota))  # Imprime el tipo de objeto
    # Llamar al método comer de la clase Gato
    mascota.comer()

    # Crear un objeto de la clase Zoo para manejar un grupo de animales
    zoo = Zoo()

    # Crear varios objetos de diferentes clases de animales
    leon = Animal("Simba", 3)  # Animal genérico
    tigre = Animal("Tigger", 4)  # Otro animal genérico
    gato = Gato("Miau", 2, 9)  # Gato con 9 vidas
    perro = Perro("Rex", 1, "Labrador")  # Perro de raza Labrador
    ave = Ave("Pajaro", 1)  # Ave genérica
    murcielago = Murcielago("Murci", 2)  # Murciélago
    ornitorrinco = Ornitorrinco("Orni", 3)  # Ornitorrinco


    zoo.agregar_animal(leon)
    zoo.agregar_animal(tigre)
    zoo.agregar_animal(gato)
    zoo.agregar_animal(perro)
    zoo.agregar_animal(ave)
    zoo.agregar_animal(murcielago)
    zoo.agregar_animal(ornitorrinco)


    zoo.alimentar_animales()


if __name__ == "__main__":
    main()