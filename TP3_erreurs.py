class Erreur(Exception):
    """classe d'exception de base pour les autres classes"""
    pass

class ErreurMinAge(Erreur):
    """L'âge du joueur est inférieur à 18"""
    pass

class ErreurMaxAge(Erreur):
    """L'âge du joueur est supérieur à 18"""
    pass

class ErreurSexe(Erreur):
    """Le sexe mentionner est différent de F ou f"""
    pass

