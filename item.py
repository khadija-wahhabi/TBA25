# Description: Item class

class Item:
    """
    Classe représentant un objet que le joueur peut trouver dans le jeu.

    Attributs:
        name (str): Le nom de l'objet.
        description (str): La description détaillée de l'objet.

    Méthodes:
        __str__(): Retourne une représentation textuelle de l'objet.
    """

    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
