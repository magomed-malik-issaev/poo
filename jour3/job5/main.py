import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 20)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
    
    def estEnVie(self):
        return self.vie > 0


class Jeu:
    def choisirNiveau(self):
        niveaux = {
            1: {'joueur': 100, 'ennemi': 100},
            2: {'joueur': 150, 'ennemi': 150},
            3: {'joueur': 200, 'ennemi': 200}
        }
        while True:
            niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))
            if niveau in niveaux:
                self.niveau = niveau
                self.points_vie_joueur = niveaux[niveau]['joueur']
                self.points_vie_ennemi = niveaux[niveau]['ennemi']
                break
            else:
                print("Niveau invalide. Veuillez choisir parmi les niveaux disponibles.")
    
    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Joueur", self.points_vie_joueur)
        ennemi = Personnage("Ennemi", self.points_vie_ennemi)
        
        while joueur.estEnVie() and ennemi.estEnVie():
            joueur.attaquer(ennemi)
            if not ennemi.estEnVie():
                break
            ennemi.attaquer(joueur)
        
        if joueur.estEnVie():
            print("Vous avez vaincu l'ennemi ! Félicitations !")
        else:
            print("Vous avez été vaincu par l'ennemi. Essayez encore !")


# Création de l'instance du jeu et lancement du jeu
jeu = Jeu()
jeu.lancerJeu()