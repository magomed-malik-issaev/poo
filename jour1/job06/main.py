class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1

# Instanciation d'un objet Animal
animal = Animal()

# Affichage de l'âge initial de l'animal
print("L'âge de l'animal", animal.age, "ans")

# Faire vieillir l'animal
animal.vieillir()

# Affichage de l'âge de l'animal après avoir vieilli
print("L'âge de l'animal après appel de la méthode vieillir", animal.age, "ans")