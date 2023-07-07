from TP3 import Joueur
from TP3_erreurs import Erreur, ErreurMinAge, ErreurMaxAge, ErreurSexe


nom_joueur = input("Nom du joueur : ")

age_min = 18
age_max = 35
while True:
    try:
        age_joueur = int(input("Age du joueur : "))
        if age_joueur < age_min :
            raise ErreurMinAge
        elif age_joueur > age_max :
            raise ErreurMaxAge
        break
    except ErreurMinAge:
        print(ErreurMinAge.__doc__)
    except ErreurMaxAge:
        print(ErreurMaxAge.__doc__)

while True:
    try:
        sexe_joueur = input("Sexe du Joueur : ")
        if sexe_joueur != "F" or sexe_joueur != "f":
            raise ErreurSexe
        break
    except ErreurSexe:
        print(ErreurSexe.__doc__)


