class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("L'âge de la personne est :", self.age)
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")


# Création d'une instance de la classe Personne
personne = Personne()
personne.afficherAge()

# Création d'une instance de la classe Eleve
eleve = Eleve()
eleve.afficherAge()


# Création d'une instance de la classe Personne
personne = Personne()
personne.afficherAge()

# Création d'une instance de la classe Eleve
eleve = Eleve()
eleve.afficherAge()

# Création d'une instance de la classe Eleve
eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()

# Redéfinition de l'âge de l'élève à 15 ans
eleve.modifierAge(15)

# Création d'une instance de la classe Professeur
professeur = Professeur(age=40)
professeur.bonjour()
professeur.enseigner()