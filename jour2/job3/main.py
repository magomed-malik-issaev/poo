class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True
    
    def getTitre(self):
        return self.__titre
    
    def setTitre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def getAuteur(self):
        return self.__auteur
    
    def setAuteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur
    
    def getNombrePages(self):
        return self.__nombre_pages
    
    def setNombrePages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Le nombre de pages doit être un entier positif. La valeur n'a pas été modifiée.")
    
    def vérification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.vérification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")
    
    def rendre(self):
        if not self.vérification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

# Exemple d'utilisation
livre = Livre("Les Misérables", "Victor Hugo", 1000)

print("Titre :", livre.getTitre())
print("Auteur :", livre.getAuteur())
print("Nombre de pages :", livre.getNombrePages())

livre.emprunter()
livre.rendre()
livre.emprunter()
livre.emprunter()
livre.rendre()