class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut


class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
    
    def marquerCommeFinie(self, tache):
        if tache in self.taches:
            tache.statut = "terminée"
    
    def afficherListe(self):
        for tache in self.taches:
            print(f"Titre : {tache.titre}")
            print(f"Description : {tache.description}")
            print(f"Statut : {tache.statut}")
            print()
    
    def filterListe(self, statut):
        filtered_list = []
        for tache in self.taches:
            if tache.statut == statut:
                filtered_list.append(tache)
        return filtered_list


# Création de tâches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain", "à faire")
tache2 = Tache("Appeler le médecin", "Prendre rendez-vous", "à faire")
tache3 = Tache("Préparer la réunion", "Faire le diaporama", "terminée")

# Création de la liste de tâches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste complète des tâches
print("Liste complète des tâches :")
liste_taches.afficherListe()

# Suppression d'une tâche
liste_taches.supprimerTache(tache2)

# Affichage de la liste mise à jour des tâches
print("Liste des tâches après suppression :")
liste_taches.afficherListe()

# Changement de statut d'une tâche
liste_taches.marquerCommeFinie(tache1)

# Affichage de la liste mise à jour des tâches
print("Liste des tâches après modification de statut :")
liste_taches.afficherListe()

# Filtrage des tâches par statut
taches_a_faire = liste_taches.filterListe("à faire")
print("Liste des tâches à faire :")
for tache in taches_a_faire:
    print(f"Titre : {tache.titre}")
    print(f"Description : {tache.description}")
    print(f"Statut : {tache.statut}")
    print()