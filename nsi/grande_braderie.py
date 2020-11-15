#Il y a trois entiers à lire : 
# la position de départ position "depart",
# la largeur d'un emplacement "largeurEmplacement"
# et le nombre de vendeurs "nbVendeurs".
while True:
    try:
        depart=int(input("la position de départ position: "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")
    
while True:
    try:
        largeurEmplacement=int(input("la largeur d'un emplacement: "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

while True:
    try:
        nbVendeurs=int(input("le nombre de vendeurs: "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

print("depart: {} largeurEmplacement: {} nbVendeurs: {}".format(depart, largeurEmplacement, nbVendeurs))

# Vous devez afficher une suite de nombres, => print
# partant de depart et augmentant de largeurEmplacement à chaque fois. 
# u(n) = depart + largeurEmplacement * n
# Il y a au total nbVendeurs augmentations à faire.
# Vous devez afficher la valeur de chacun des nombres de la suite.
n = 0
while n <= nbVendeurs :
    u = depart + largeurEmplacement * n
    print(u)
    n += 1
