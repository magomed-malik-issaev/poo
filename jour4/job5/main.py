import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, rayon):
        self.radius = rayon
    
    def aire(self):
        return math.pi * self.radius**2


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 8)
print("Aire du rectangle :", rectangle.aire())

# Instanciation de la classe Cercle
cercle = Cercle(3)
print("Aire du cercle :", cercle.aire())