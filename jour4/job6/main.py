class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)


# Instanciation de la classe Voiture
voiture = Voiture("Toyota", "Corolla", 2022, 25000)
voiture.informationsVehicule()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)


# Instanciation de la classe Moto
moto = Moto("Honda", "CBR500R", 2023, 8000)
moto.informationsVehicule()

class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)
    
    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)
    
    def demarrer(self):
        print("La voiture démarre. Vroum vroum !")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)
    
    def demarrer(self):
        print("La moto démarre. Vroum !")


# Instanciation de la classe Voiture et appel de la méthode demarrer()
voiture = Voiture("Toyota", "Corolla", 2022, 25000)
voiture.demarrer()

# Instanciation de la classe Moto et appel de la méthode demarrer()
moto = Moto("Honda", "CBR500R", 2023, 8000)
moto.demarrer()