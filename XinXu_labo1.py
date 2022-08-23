# Xin Xu #2194517

# import fomction ramdom pour brasser le dé
import random

class Des:
    def __init__(self, nb_faces, valeur1 = 0, valeur2 = 0) -> None:
        self.nb_faces = nb_faces
        self.de_1 = valeur1
        self.de_2 = valeur2

#on brasse les dés dont la valeur est un nombre aléatoir entre 1 et nombre de faces
    def brasser(self):
        self.de_1 = random.randint(1, self.nb_faces)
        self.de_2 = random.randint(1, self.nb_faces)

#une fonction pour calculer la valeur totale   
    def total(self):
        return self.de_1 + self.de_2


    def comparer(self, d2):
        return self.total() > d2.total()

    def __str__(self):
        return f"nombre de faces({self.nb_faces})\tdé_1({self.de_1})\tdé2({self.de_2})"

#fonction initialiser
def initial():
    condition = True
    while condition:
        nbFaces = int(input("Entrez le nombre de faces voulu(6 à 24): "))
        valeur1 = int(input(f"Entrez l'état du dé_1(1 à {nbFaces}): "))
        valeur2 = int(input(f"Entrez l'état du dé_2(1 à {nbFaces}): "))
        if 6 <= nbFaces <= 24 and 1 <= valeur1 <= nbFaces and 1 <= valeur2 <= nbFaces:
            condition = False
        else:
            print("Entrées invalides")
    return nbFaces, valeur1, valeur2

nbFaces, valeur1, valeur2 = initial()
de_utilisateur = Des(nbFaces, valeur1, valeur2)
de_sys = Des(de_utilisateur.nb_faces)

def menu(d_u, d_s):
    condition = True
    while condition:
        choix = input("1. Brasser les dés #(affiche le résultat des deux paires de dés)\n"+
        "2. Comparer les dés #(indique si la paire de l'utilisateur est supérieure ou non)\n"+
        "3. Sortir #(sort de l'exécution du programme)\n")
        if choix == "3":
            condition = False
        elif choix == "1":
            d_u.brasser()
            d_s.brasser()
            print(f"L'état des dés de l'utilisateur: {d_u}")
            print(f"L'état des dés du système: {d_s}")
        elif choix == "2":
            if d_u.comparer(d_s):
                print("La paire de l'utilisateur est supérieure que la paire du système. ")
            else:
                print("La paire de l'utilisateur n'est pas supérieure que la paire du système. ")
        else:
            print("Votre choix est invalide, veuillez choisir 1 à 3 ")


menu(de_utilisateur,de_sys)







"""
d = Des(24)
print(d.nb_faces)
print(d.de_1)
print(d.de_2)
d2 = Des(6, 3, 2)
print(d.comparer(d2))
for i in range(30):
    d.brasser()
    print(d.de_1, end = "\t")
    print(d.de_2)
"""

