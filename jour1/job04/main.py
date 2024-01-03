class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes avec des valeurs de construction de choix
personne1 = Personne("X", "Malcolm")
personne2 = Personne("Marie", "Jane")


# Appel de la méthode SePresenter pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())
