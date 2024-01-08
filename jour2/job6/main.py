class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__plats = {}
        self.__statut = "en cours"
    
    def ajouterPlat(self, nom, prix):
        if nom not in self.__plats:
            self.__plats[nom] = {"prix": prix, "statut": "en cours"}
            print(f"Le plat '{nom}' a été ajouté à la commande.")
        else:
            print(f"Le plat '{nom}' est déjà présent dans la commande.")
    
    def annulerCommande(self):
        self.__statut = "annulée"
        print("La commande a été annulée.")
    
    def __calculerTotal(self):
        total = 0
        for plat in self.__plats.values():
            if plat["statut"] == "en cours":
                total += plat["prix"]
        return total
    
    def afficherCommande(self):
        print(f"Commande #{self.__numero}")
        for nom, plat in self.__plats.items():
            if plat["statut"] == "en cours":
                print(f"- {nom} : {plat['prix']} €")
        print(f"Total à payer : {self.__calculerTotal()} €")
    
    def calculerTVA(self, taux):
        tva = self.__calculerTotal() * taux
        return tva

# Exemple d'utilisation
commande = Commande(1)

commande.ajouterPlat("Pizza Margherita", 10)
commande.ajouterPlat("Salade César", 8)
commande.ajouterPlat("Pizza Prosciutto", 12)

commande.afficherCommande()

commande.annulerCommande()

commande.afficherCommande()

tva = commande.calculerTVA(0.20)
print(f"TVA : {tva} €")