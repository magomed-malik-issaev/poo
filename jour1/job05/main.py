class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"Coordonnée x : {self.x}")
    
    def afficherY(self):
        print(f"Coordonnée y : {self.y}")
    
    def changerX(self, new_x):
        self.x = new_x
    
    def changerY(self, new_y):
        self.y = new_y

    # Instanciation d'un objet Point
point = Point(3, 5)

# Affichage des coordonnées du point
point.afficherLesPoints()

# Affichage des coordonnées x et y
point.afficherX()
point.afficherY()

# Changement des coordonnées x et y
point.changerX(10)
point.changerY(8)

# Affichage des nouvelles coordonnées x et y
point.afficherX()
point.afficherY()