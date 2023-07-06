from abc import ABC,abstractmethod
class personne(ABC):
    def __init__(self, nom, prenom, age, langue):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.langue = langue

    @abstractmethod
    def langage(self):
        return "Je parle" + self.langue