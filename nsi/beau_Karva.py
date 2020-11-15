while True:
    try:
        nb_karva=int(input("nbkarva : "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

for karva in range(nb_karva):
    while True:
        try:
            poids=int(input("poids: "))
            break
        except ValueError:
            print("Oops! That was no valid number.  Try again...")
        
    while True:
        try:
            age=int(input("age: "))
            break
        except ValueError:
            print("Oops! That was no valid number.  Try again...")

    while True:
        try:
            longueur_cornes=int(input("longueur_cornes: "))
            break
        except ValueError:
            print("Oops! That was no valid number.  Try again...")
    
    while True:
        try:
            hauteur=int(input("hauteur: "))
            break
        except ValueError:
            print("Oops! That was no valid number.  Try again...")

    note=longueur_cornes * hauteur + poids
    print(note)

