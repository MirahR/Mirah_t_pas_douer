class Homme :
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def show(self):
        print("Mon nom est", self.nom,", j'ai", self.age, "ans")

homme = Homme("Ali", 14)
homme.show()