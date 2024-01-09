import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def afficher(self):
        print(f"{self.valeur} de {self.couleur}")


class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Pique', 'Trèfle']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        
        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self):
        main = []
        for _ in range(2):
            carte = self.paquet.pop()
            main.append(carte)
        return main

    def ajouter_carte(self, main):
        carte = self.paquet.pop()
        main.append(carte)

    def calculer_total(self, main):
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                valeur = 10
            elif carte.valeur == 'As':
                valeur = 11
                as_count += 1
            else:
                valeur = int(carte.valeur)
            
            total += valeur

        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1
        
        return total


# Initialisation du jeu
jeu = Jeu()

# Mélange du paquet de cartes
jeu.melanger_paquet()

# Distribution des cartes au joueur et au croupier
main_joueur = jeu.distribuer_cartes()
main_croupier = jeu.distribuer_cartes()

print("Main du joueur :")
for carte in main_joueur:
    carte.afficher()

print("Main du croupier :")
for carte in main_croupier:
    carte.afficher()

# Tour du joueur
while True:
    choix = input("Voulez-vous prendre une carte supplémentaire ? (oui/non) ")

    if choix.lower() == 'oui':
        jeu.ajouter_carte(main_joueur)
        print("Votre main :")
        for carte in main_joueur:
            carte.afficher()

        total = jeu.calculer_total(main_joueur)
        print("Total de points :", total)

        if total > 21:
            print("Vous avez dépassé 21 points. Vous avez perdu.")
            break

    elif choix.lower() == 'non':
        break

# Tour du croupier
total_croupier = jeu.calculer_total(main_croupier)

while total_croupier < 17:
    jeu.ajouter_carte(main_croupier)
    total_croupier = jeu.calculer_total(main_croupier)

print("Main du croupier :")
for carte in main_croupier:
    carte.afficher()

print("Total de points du croupier :", total_croupier)

# Comparaison des scores
total_joueur = jeu.calculer_total(main_joueur)

if total_joueur > 21:
    print("Vous avez dépassé 21 points. Vous avez perdu.")
elif total_croupier > 21:
    print("Le croupier a dépassé 21 points. Vous avez gagné.")
elif total_joueur > total_croupier:
    print("Vous avez un meilleur score que le croupier. Vous avez gagné.")
elif total_joueur < total_croupier:
    print("Le croupier a un meilleur score que vous. Vous avez perdu.")
else:
    print("Égalité. Personne ne gagne.")