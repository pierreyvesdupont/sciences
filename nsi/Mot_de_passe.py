while True:
    try:
        mot_de_passe=int(input("mot de passe: "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

if mot_de_passe == 64741:
    print("Bon festin !")
else:
    print("Allez-vous en !")
