#import polynome_fonctions
from polynome_fonctions import *
from random import *
#### 0. Définition des fonctions


# Mode : génération aléatoire de polynome + les résoudre
print("quel mode de génération")
print("tapez 1 pour aléatoire")
print("tapez 2 pour manuel")
mode_de_génération=int(input("quel est le mode de génération: "))
if mode_de_génération == 1:
    a=int(randint(-9, 9))
    c=int(randint(-9, 9))
    f=int(randint(-9, 9))
    g=int(randint(-9, 9))

    #### 1. Récupération des données
    print("Soit p(x) = Ax² + Bx + C")
    b=f*a
    d=g*c
    A=a*c
    B=a*d+b*c
    C=b*d
    print("=> p(x) = "+str(A)+"x² + "+str(B)+"x + "+str(C))

    polynome = {"A": A, "B": B, "C": C}
    print("=> p(x) = "+str(A)+"x² + "+str(B)+"x + "+str(C))

    #### 0,1. Est ce une identité remarquable ?
    recherche_identité_remarquable(polynome)

    #### 0,2. Calcul discriminant et forme canonique
    polynome["alpha"], polynome["béta"], polynome["delta"] = calcule_discriminant(polynome)

    #### 0,3. Résolution p(x) = 0
    polynome["solution"] = résoudre_px_égale_zéro(polynome)

    #### 0,4. Tableau de signe
    afficher_tableau_de_signe(polynome)

    #### 0,5. Dessiner la courbe
    Dessiner_courbe(polynome)

elif mode_de_génération == 2:
    A=int(input("quel est la valeur de a: "))
    B=int(input("quel est la valeur de c: "))
    C=int(input("quel est la valeur de f: "))

    polynome = {"A": A, "B": B, "C": C}
    print("=> p(x) = "+str(A)+"x² + "+str(B)+"x + "+str(C))

    #### 0,1. Est ce une identité remarquable ?
    recherche_identité_remarquable(polynome)

    #### 0,2. Calcul discriminant et forme canonique
    polynome["alpha"], polynome["béta"], polynome["delta"] = calcule_discriminant(polynome)

    #### 0,3. Résolution p(x) = 0
    polynome["solution"] = résoudre_px_égale_zéro(polynome)

    #### 0,4. Tableau de signe
    afficher_tableau_de_signe(polynome)

    #### 0,5. Dessiner la courbe
    Dessiner_courbe(polynome)

else:
    print("ce chifre n'est pas corect reesayez")



