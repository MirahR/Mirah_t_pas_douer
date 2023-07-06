from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self, nom, prenom, couleur, genre, deplacement):
        self.nom = nom
        self.prenom = prenom
        self.couleur = couleur
        self.genre = genre
        self.deplacement = deplacement

    @abstractmethod
    def display(self):
        return "L'animal est un " + self.nom\
                + " qui s'appelle " + self.prenom\
                + "\nIl est de couleur " + self.couleur\
                + "\nC'est un animal " + self.genre
    
    @abstractmethod
    def manger(self):
        return "Je mange un peu de tout ! =d"
    
    @abstractmethod
    def deplacer(self):
        return "Pour me déplacer, je " + self.deplacement + "\n"


class Carnivore (Animal):
    def __init__(self, nom, prenom, couleur, genre, deplacement):
        super().__init__(nom, prenom, couleur, genre, deplacement)


    def manger(self):
        return "Je mange de la viande (>u<)"

class CarniSauvage (Carnivore):
    """classe d'animaux sauvages qui sont aussi carnivores"""
    def __init__(self, nom, prenom, couleur, genre, deplacement):
        super().__init__(nom, prenom, couleur, genre, deplacement)


"""définit les attributs des classes et sous-classes"""
animal = Animal("chat", "Mimi o(^.^)O", "noir", "domestique",\
                "marche à quatre pattes")
carnivore = Carnivore("lion", "Moufassa", "blanc", "domestique",\
                      "marche à quatre pattes")
carnisauvage = CarniSauvage("tigre", "Shere Khan",\
                            "orange avec des rayures noires", "sauvage",\
                            "marche sur mes grosses patounes")


"""Méthodes sur animal"""
print(animal.display())
print(animal.manger())
print(animal.deplacer())

"""Méthodes sur carnivore"""
print(carnivore.display())
print(carnivore.manger())
print(carnivore.deplacer())

"""Méthodes sur carnisauvage"""
print(carnisauvage.display())
print(carnisauvage.manger())
print(carnisauvage.deplacer())
print(CarniSauvage.__doc__)
