# Votre programme doit d'abord lire un entier décrivant votre position actuelle sur la route
# sous la forme d'un nombre de kilomètres par rapport au début de la route
while True:
    try:
        position_actuelle=int(input("position_actuelle : "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

#Ensuite, il doit lire un entier donnant le nombre de villages
while True:
    try:
        nbvillage=int(input("nbvillage : "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

# Pour chaque village, il doit lire un entier décrivant
# la position de ce village le long de cette même route
nbvillage_dans_les_50km=0
for index in range(nbvillage):
    while True:
        try:
            nbkilomètre=int(input("nbkilomètre: "))
            break
        except ValueError:
            print("Oops! That was no valid number.  Try again...")

    if nbkilomètre >= position_actuelle - 50 and nbkilomètre <= position_actuelle + 50 :
        nbvillage_dans_les_50km += 1

# Votre programme doit alors afficher le nombre de villages qui se trouvent
# à une distance inférieure ou égale à 50 km de votre position actuelle

# for valeur_courante_de_nbkilomètre_list in nbkilomètre_list:
#    if valeur_courante_de_nbkilomètre_list >= position_actuelle - 50 and valeur_courante_de_nbkilomètre_list <= position_actuelle + 50 :
#        nbvillage_dans_les_50km += 1

# Equivalent boucle while
#index_de_nbkilomètre_list =0
#while index_de_nbkilomètre_list < len(nbkilomètre_list)
#    valeur_courante_de_nbkilomètre_list = nbkilomètre_list[index_de_nbkilomètre_list]
#    index_de_nbkilomètre_list += 1
#    if valeur_courante_de_nbkilomètre_list >= position_actuelle - 50 and valeur_courante_de_nbkilomètre_list <= position_actuelle + 50 :
#        nbvillage_dans_les_50km += 1

print(nbvillage_dans_les_50km)