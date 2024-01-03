class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y -= 1
    
    def bas(self):
        self.y += 1
    
    def position(self):
        return (self.x, self.y)
    
    # Création d'un objet Personnage avec une position initiale (2, 3)
personnage = Personnage(2, 3)

# Affichage de la position initiale du personnage
print("Position initiale :", personnage.position())

# Déplacement du personnage vers la gauche
personnage.gauche()

# Déplacement du personnage vers le haut
personnage.haut()

# Affichage de la position après les déplacements
print("Nouvelle position :", personnage.position())