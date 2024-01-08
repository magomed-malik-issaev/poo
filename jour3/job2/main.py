class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte : {self.__numero}")
        print(f"Titulaire : {self.__prenom} {self.__nom}")
        print(f"Solde : {self.__solde} €")
    
    def afficherSolde(self):
        print(f"Solde du compte : {self.__solde} €")
    
    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué.")
    
    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué.")
        else:
            print("Solde insuffisant. Retrait impossible.")
    
    def agios(self, taux):
        if self.__solde < 0:
            agios = self.__solde * taux
            self.__solde += agios
            print(f"Des agios de {agios} € ont été appliqués.")
    
    def virement(self, compte_dest, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_dest.getNumero()}.")
        else:
            print("Solde insuffisant. Virement impossible.")
    
    def getNumero(self):
        return self.__numero


# Création du premier compte
compte1 = CompteBancaire("001", "Doe", "John", 1000, False)
compte1.afficher()

compte1.retrait(500)
compte1.afficherSolde()

compte1.versement(200)
compte1.afficherSolde()

# Création du deuxième compte à découvert
compte2 = CompteBancaire("002", "Smith", "Alice", -500, True)
compte2.afficher()

compte2.retrait(200)
compte2.afficherSolde()

compte1.virement(compte2, 300)
compte1.afficherSolde()
compte2.afficherSolde()