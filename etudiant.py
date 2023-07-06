from personne import personne

class etudiant(personne):
    def __init__(self, nom, prenom, age, langue, matricule, note):
        super().__init__(self, nom, prenom, age, langue)
        self.matricule = matricule
        self.note = note

    def liste_etudiant(self):
        return self.nom + self.prenom + "a eu " + self.note + "à l'examen !"
    

list_etudiant = [self.nom, self.prenom]

     