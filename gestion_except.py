class Erreur(Exception):
    """class de base pour les autres erreurs"""
    pass

class ValueTropPetiteErreur(Erreur):
    """survient quand la valeur entre est petite"""
    pass

class ValueTropLargeErreur(Erreur):
    """survient quand la valeur entre est grande"""
    pass

number = 10
while True:
    try:
        i_num = int(input("Entrez un nombre : "))
        if i_num < number :
            raise ValueTropPetiteErreur
        elif i_num > number :
            raise ValueTropLargeErreur
        break
    except ValueTropPetiteErreur:
        print("cette valeur est petite, essaye encore")
    except ValueTropLargeErreur:
        print("cette valeur est trop grande, essaye encore")