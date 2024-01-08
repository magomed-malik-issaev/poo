class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50
    
    def getMarque(self):
        return self.__marque
    
    def setMarque(self, nouvelle_marque):
        self.__marque = nouvelle_marque
    
    def getModele(self):
        return self.__modele
    
    def setModele(self, nouveau_modele):
        self.__modele = nouveau_modele
    
    def getAnnee(self):
        return self.__annee
    
    def setAnnee(self, nouvelle_annee):
        self.__annee = nouvelle_annee
    
    def getKilometrage(self):
        return self.__kilometrage
    
    def setKilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage
    
    def getEnMarche(self):
        return self.__en_marche
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide. Impossible de démarrer.")
    
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")
    
    def __verifier_plein(self):
        return self.__reservoir
    
# Exemple d'utilisation
voiture = Voiture("Renault", "Clio", 2020, 50000)

print("Marque :", voiture.getMarque())
print("Modèle :", voiture.getModele())
print("Année :", voiture.getAnnee())
print("Kilométrage :", voiture.getKilometrage())
print("En marche :", voiture.getEnMarche())

voiture.demarrer()
voiture.arreter()

voiture.setKilometrage(55000)
voiture.demarrer()

voiture.setReservoir(10)
voiture.demarrer()