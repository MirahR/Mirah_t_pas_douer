from personne import personne

class etudiant(personne):
    def __init__(self, nom, prenom, age, langue, matricule, note):
        super().__init__(self, nom, prenom, age, langue)
        self.matricule = matricule
        self.note = note

    def getnom(self):
        return super().getnom()
    
    def getprenom(self):
        return super().getprenom()
    
    def getage(self):
        return super().getage()
    
    def langage(self):
        return super().langage()
    
    def getmatricule(self):
        return self.matricule
    
    def getnote(self):
        return self.note

    def liste_etudiant(self):
        list_etudiant = [self.nom, self.prenom]
        return self.nom + self.prenom + "a eu " + self.note + "à l'examen !"
    





     