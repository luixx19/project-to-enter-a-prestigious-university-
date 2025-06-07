class Zoo:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.comer()