resultat = 1
# afficher le bon resultat
# utiliser une boucle
nb_cube_par_ligne=17
while nb_cube_par_ligne > 1 :
   resultat += nb_cube_par_ligne**3
   nb_cube_par_ligne -= 2
print(resultat)