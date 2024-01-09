class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    
    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
    
    def surface(self):
        return self._longueur * self._largeur
    
    # Accesseurs pour la longueur et la largeur
    def get_longueur(self):
        return self._longueur
    
    def get_largeur(self):
        return self._largeur
    
    # Mutateurs pour la longueur et la largeur
    def set_longueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur
    
    def set_largeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
    
    def volume(self):
        return self._longueur * self._largeur * self._hauteur
    
    # Accesseur pour la hauteur
    def get_hauteur(self):
        return self._hauteur
    
    # Mutateur pour la hauteur
    def set_hauteur(self, nouvelle_hauteur):
        self._hauteur = nouvelle_hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 8)
print("Perimètre du rectangle :", rectangle.perimetre())
print("Surface du rectangle :", rectangle.surface())

# Utilisation des accesseurs/mutateurs pour modifier les attributs du rectangle
rectangle.set_longueur(10)
rectangle.set_largeur(6)
print("Nouvelle longueur du rectangle :", rectangle.get_longueur())
print("Nouvelle largeur du rectangle :", rectangle.get_largeur())

# Instanciation de la classe Parallelepipede
parallelepiped = Parallelepipede(4, 6, 3)
print("Perimètre du parallélépipède :", parallelepiped.perimetre())
print("Surface du parallélépipède :", parallelepiped.surface())
print("Volume du parallélépipède :", parallelepiped.volume())

# Utilisation des accesseurs/mutateurs pour modifier les attributs du parallélépipède
parallelepiped.set_longueur(8)
parallelepiped.set_largeur(10)
parallelepiped.set_hauteur(5)
print("Nouvelle longueur du parallélépipède :", parallelepiped.get_longueur())
print("Nouvelle largeur du parallélépipède :", parallelepiped.get_largeur())
print("Nouvelle hauteur du parallélépipède :", parallelepiped.get_hauteur())