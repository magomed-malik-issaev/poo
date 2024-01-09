class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 8)
print("Aire du rectangle :", rectangle.aire())