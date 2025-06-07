from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def comer(self, comida):
        # Método abstracto que obliga a las clases hijas a implementar su propia versión del método `comer`.
        pass

    def dormir(self):
        # Método concreto que define un comportamiento común para todas las clases hijas.
        print("El animal está durmiendo.")

# Clase Perro que hereda de Animal e implementa el método abstracto `comer`.


class Perro(Animal):
    def comer(self, comida):
        print(f"El perro esta comiendo {comida}")

# Clase Gato que hereda de Animal e implementa el método abstracto `comer`.


class Gato(Animal):
    def comer(self, comida):
        print(f"El gato esta comiendo {comida}")

# Clase Ave que hereda de Animal e implementa el método abstracto `comer`.


class Ave(Animal):
    def comer(self, comida):
        print(f"Al ave no le gusta comer {comida}, prefiere comer semillas")