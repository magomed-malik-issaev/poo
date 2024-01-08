class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants
    
    def getNom(self):
        return self.__nom
    
    def getHabitants(self):
        return self.__habitants
    
    def augmenterPopulation(self):
        self.__habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def ajouterPopulation(self):
        self.__ville.augmenterPopulation()


# Création de la ville de Paris avec 1 000 000 d'habitants
paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants à {paris.getNom()} : {paris.getHabitants()}")

# Création de la ville de Marseille avec 861 635 habitants
marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants à {marseille.getNom()} : {marseille.getHabitants()}")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de population
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Nombre d'habitants à {paris.getNom()} après l'arrivée de John et Myrtille : {paris.getHabitants()}")
print(f"Nombre d'habitants à {marseille.getNom()} après l'arrivée de Chloé : {marseille.getHabitants()}")