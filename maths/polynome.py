import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def recherche_identité_remarquable(polynome):
    # (fx + g)² => f²x² + 2fgx + g² => si b = 2fg => b == 2sqrt(a*c) ==> (sqrt(a)x + sqrt(c))² ==> p(x) = 0 a une solution : -sqrt(c / a)
    # (fx - g)² => f²x² - 2fgx + g² => si b = -2fg => b == -2sqrt(a*c) ==> (sqrt(a)x - sqrt(c))² ==> p(x) = 0 a une solution : sqrt(c / a)
    # (fx + g)(fx - g) => f²x² - g² => si b == 0 et c < 0 ==> (sqrt(a)x + sqrt(c))(sqrt(a)x - sqrt(c)) ==> p(x) = 0 a deux solutions : -sqrt(c / a) et sqrt(c / a)
    A=polynome["A"]
    B=polynome["B"]
    C=polynome["C"]
    A1=(-A, A)[A > 0]
    B1=(-B, B)[A > 0]
    C1=(-C, C)[A > 0]
    if C1 > 0 and B1 == 2 * math.sqrt(abs(A1*C1)):
        print("p(x) est une identité remarquable : {}({}x + {})²".format(("-", "")[A > 0], math.sqrt(abs(A)), math.sqrt(abs(C))))
    elif C1 > 0 and B1 == -2 * math.sqrt(abs(A1*C1)):
        print("p(x) est une identité remarquable : {}({}x - {})²".format(("-", "")[A > 0], math.sqrt(abs(A)), math.sqrt(abs(C))))
    elif B1 == 0 and C1 < 0 or A1 < 0 :
        print("p(x) est une identité remarquable : {}({}x - {})({}x + {})".format(("-", "")[A > 0], math.sqrt(abs(A)), math.sqrt(abs(C)), math.sqrt(abs(A)), math.sqrt(abs(C))))
    else:
        print("p(x) n'est pas une identité remarquable")


def calcule_discriminant(polynome):
    A=polynome["A"]
    B=polynome["B"]
    C=polynome["C"]
    alpha=-B/(2*A)
    béta=(A*alpha**2)+(B*alpha)+C
    delta=(B**2)-4*A*C

    print("la forme canonique est "+str(A)+"*(x + "+str(-1*alpha)+")²+ "+str(béta))
    print("Le discriminant est: "+str(delta))
    return alpha, béta, delta 


def résoudre_px_égale_zéro(polynome):
    A=polynome["A"]
    B=polynome["B"]
    C=polynome["C"]
    delta=polynome["delta"]
    solution = []
    if delta < 0:
        print("il n'y a pas de solution pour p(x) = 0")
    elif delta > 0:
        x0 = (-B+(math.sqrt(delta)))/(2*A)
        x1 = (-B-(math.sqrt(delta)))/(2*A)
        solution.append(min(x0, x1))
        solution.append(max(x0, x1))
        print("les solutions pour p(x) = 0 sont "+str(solution[0])+" "+str(solution[1])+".")
    elif delta == 0:
        solution.append(-B/(2*A))
        print("la seul solution pour p(x) = 0 est "+str(solution[0])+".")
    return solution


def afficher_tableau_de_signe(polynome):
    A=polynome["A"]
    B=polynome["B"]
    C=polynome["C"]
    delta=polynome["delta"]
    solution=polynome["solution"]
    if delta < 0:
        print(" (x)  -----------")
        # sign de C
        print("p(x) |     {}     |".format(("-", "+")[C > 0]))
        print("      -----------")

    elif delta > 0:
        print(" (x)  ---({})---({})---".format(solution[0], solution[1]))
        # sign de p(solution[0] - 1) | signe contraire de p(solution[0] - 1) | sign de p(solution[0] - 1)
        pxo = A * (solution[0] - 1)**2 + (solution[0] - 1)*B + C
        print("p(x) | {} | {} | {} |".format(("-", "+")[pxo > 0],("+", "-")[pxo> 0],("-", "+")[pxo> 0]))
        print("      --- --- ---")

    elif delta == 0:
        print(" (x)  -----({})-----".format((solution[0])))
        # sign de p(solution[0] - 1)
        pxo = A * (solution[0] - 1)**2 + (solution[0] - 1)*B + C
        print("p(x) |  {}  |  {}  |".format(("-", "+")[pxo > 0],("-", "+")[pxo > 0]))
        print("      ----- -----")


def Dessiner_courbe(polynome):
    A=polynome["A"]
    delta=polynome["delta"]
    alpha=polynome["alpha"]
    béta=polynome["béta"]
    solution=polynome["solution"]
    x = np.arange(-2, 2,0.01)
    if delta > 0:
        x = np.arange( solution[0] - 1, solution[1] + 1, 0.01)
    elif delta == 0:
        x = np.arange(solution[0]-2, solution[0]+2, 0.01)
    fx = A *(x + (-1*alpha))**2 + béta

    fig, ax = plt.subplots()
    ax.plot(x, fx)

    ax.set(xlabel='abscisses', ylabel='ordonnées',
        title='Courbe')
    ax.grid()

    fig.savefig("test3.png")
    plt.show()
