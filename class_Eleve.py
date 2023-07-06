class Eleve :
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def show(self):
        print("Il s'appelle", self.nom, "il a", self.age)
    def get_nom(self):
        return self.nom

elv = Eleve("john", 150)
elv.show()


