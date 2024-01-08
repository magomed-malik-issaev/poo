class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur
    
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Création d'un rectangle avec une longueur de 10 et une largeur de 5
rectangle = Rectangle(10, 5)

# Affichage des attributs initialisés
print("Longueur :", rectangle.getLongueur())
print("Largeur :", rectangle.getLargeur())

# Modification de la longueur et de la largeur
rectangle.setLongueur(15)
rectangle.setLargeur(8)

# Affichage des attributs modifiés
print("Nouvelle longueur :", rectangle.getLongueur())
print("Nouvelle largeur :", rectangle.getLargeur())