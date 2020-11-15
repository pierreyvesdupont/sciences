Na = 6.02E-23
masse_volumique_eau = 1000

# j'ouvre le fichier input dans le repertoire courant
# j'affiche chacune des lignes du fichier
# Using readlines() 
file1 = open('mesures.txt', 'r') 
Lines = file1.readlines() 

# Strips the newline character 
mesures={}
print('mesures:[{}]'.format(mesures))
for line in Lines:
    # line masse=10 => dictionnaire { "masse" : 10 }
    x = line.strip().split("=")
    mesures[x[0]] = int(x[1])


file1.close()

nombre_mesures = 0
while len(mesures) - nombre_mesures:
    print('mesures avant :[{}]'.format(mesures))
    nombre_mesures = len(mesures)
    print("nombre_mesures avant: {}".format(nombre_mesures))
    # masse
    # m = masse_volumique * volume
    # m = concentration_massique * volume
    # m = masse_molaire * mol
    if not "masse" in mesures:
        if "masse_volumique" in mesures and "volume" in mesures:
            mesures["masse"] = mesures["masse_volumique"] * mesures["volume"]
        elif "concentration_massique" in mesures and "volume" in mesures:
            mesures["masse"] = mesures["concentration_massique"] * mesures["volume"]
        elif "masse_molaire" in mesures and "mole" in mesures:
            mesures["masse"] = mesures["masse_molaire"] / mesures["mole"]

    # volume
    if not "volume" in mesures:
        if "masse_volumique" in mesures and "masse" in mesures:
            mesures["volume"] = mesures["masse_volumique"] * mesures["masse"]
        elif "concentration_massique" in mesures and "masse" in mesures:
            mesures["volume"] = mesures["concentration_massique"] * mesures["masse"]
        elif "concentration_molaire" in mesures and "masse" in mesures:
            mesures["volume"] = mesures["concentration_molaire"] * mesures["masse"]

    # masse_volumique
    if not "masse_volumique" in mesures:
        if "volume" in mesures and "masse" in mesures:
            mesures["masse_volumique"] = mesures["volume"] * mesures["masse"]
        elif "densité" in mesures:
            mesures["masse_volumique"] = masse_volumique_eau / mesures["densité"]

    # concentration_massique
    if not "concentration_massique" in mesures:
        if "volume" in mesures and "masse" in mesures:
            mesures["concentration_massique"] = mesures["volume"] / mesures["masse"]

    # masse_molaire
    if not "masse_molaire" in mesures:
        if "mole" in mesures and "masse" in mesures:
            mesures["masse_molaire"] = mesures["volume"] * mesures["masse"]

    # densité 
    if not "densité" in mesures:
        if "masse_molaire" in mesures and "masse" in mesures:
            mesures["densité"] = mesures["masse_molaire"] * mesures["masse"]


    # concentration_molaire 
    if not "concentration_molaire" in mesures:
        if "mole" in mesures and "volume" in mesures:
            mesures["concentration_molaire"] = mesures["mole"] / mesures["volume"]

    # densité
    if not "densité" in mesures:
        if "mole" in mesures:
            mesures["concentration_molaire"] = mesures["mole"] / masse_volumique_eau

    # quantité_de_matière
    if not "quantité_de_matière" in mesures:
        if "mole" in mesures:
            mesures["quantité_de_matière"] = mesures["mole"] / Na

    print("nombre_mesures apres: {}. J'ai {} nouvelles mesures".format(len(mesures), len(mesures) - nombre_mesures))

print('mesures après :[{}]'.format(mesures))

#sauvegardes de mesures dans un fichier resultats.txt
# pour chaque ligne du fichier on a :
# masse=20