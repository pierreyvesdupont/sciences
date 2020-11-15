while True:
    try:
        nbMembres=int(input("nbMembres : "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

poids_e = [0, 0]

for index in range(2 * nbMembres):
    while True:
        try:
            poids=int(input("poids: "))
            break
        except ValueError:
            print("Oops! That was no valid number.  Try again...")

    poids_e[index % 2] += poids

print("L'équipe {} a un avantage".format(("1", "2")[poids_e[0] <poids_e[1]]))
print("Poids total pour l'équipe 1 : {}".format(poids_e[0]))
print("Poids total pour l'équipe 2 : {}".format(poids_e[1]))