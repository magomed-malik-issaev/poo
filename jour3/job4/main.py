class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts_marques += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        print(f"Statistiques du joueur {self.nom} ({self.position}, numéro {self.numero}):")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes : {self.cartons_jaunes}")
        print(f"Cartons rouges : {self.cartons_rouges}")
        print()


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts_marques=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts_marques += buts_marques
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges
                break


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 10, "Attaquant")
joueur4 = Joueur("Mbappé", 7, "Attaquant")

# Création des équipes
equipe1 = Equipe("FC Barcelone")
equipe2 = Equipe("Paris Saint-Germain")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques initiales des joueurs
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
print("Simulation du match...")
joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur2.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()
joueur4.recevoirUnCartonRouge()

# Mise à jour des statistiques des joueurs dans les équipes
equipe1.mettreAJourStatistiquesJoueur("Messi", buts_marques=2)
equipe1.mettreAJourStatistiquesJoueur("Ronaldo", buts_marques=1, passes_decisives=1)
equipe2.mettreAJourStatistiquesJoueur("Neymar", cartons_jaunes=1)
equipe2.mettreAJourStatistiquesJoueur("Mbappé", cartons_rouges=1)

# Affichage des statistiques mises à jour des joueurs
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()