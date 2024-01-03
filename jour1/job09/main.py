class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def calculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC
    
    def afficher(self):
        print("Informations sur le produit :")
        print("Nom :", self.nom)
        print("Prix HT :", self.prixHT)
        print("TVA :", self.TVA)
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    def getNom(self):
        return self.nom
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Téléphone", 500, 10)
produit3 = Produit("Clavier", 50, 5)

# Calcul de la TVA pour chaque produit
tva_produit1 = produit1.calculerPrixTTC() - produit1.prixHT
tva_produit2 = produit2.calculerPrixTTC() - produit2.prixHT
tva_produit3 = produit3.calculerPrixTTC() - produit3.prixHT

# Affichage des informations de chaque produit
produit1.afficher()
print("TVA :", tva_produit1)
print()
produit2.afficher()
print("TVA :", tva_produit2)
print()
produit3.afficher()
print("TVA :", tva_produit3)
print()

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Laptop")
produit1.modifierPrix(1200)

produit2.modifierNom("Smartphone")
produit2.modifierPrix(550)

produit3.modifierNom("Souris")
produit3.modifierPrix(60)

# Affichage des nouveaux prix des produits
print("Nouveau prix du produit", produit1.getNom(), ":", produit1.getPrixHT())
print("Nouveau prix du produit", produit2.getNom(), ":", produit2.getPrixHT())
print("Nouveau prix du produit", produit3.getNom(), ":", produit3.getPrixHT())