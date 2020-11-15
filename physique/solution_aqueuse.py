#constante d'avogadro
Na=6.02*10E23

#masse volumique de l’eau à 4 °C est de 0,999 973 kg⋅L-1.
MVeau = 999.973

####la quantitée de matière n = N / Na(6,02*10^23) 
def calcul_nombre_mol(nombre_quantite_elementaire):
    return nombre_quantite_elementaire / Na

####la masse volumique ρ = m(solution) / V(solution)
def calcul_masse_volumique(masse_solution, volume_solution):
    return masse_solution / volume_solution

def calcul_concentration_massique(masse_solute, volume_solute): 
    return masse_solute / volume_solute

class Dilution:
    solution_fille = None # Solution
    solution_mere = None # Solution

    coefficient = None

    def __init__(self, solution1, solution2):
        return

class Solution:
  solute = None # Substance
  solvant = None # Substance

  concentration_massique = None # (g/l) masse / volume
  concentration_molaire = None # (mol/l) nombre_mol / volume

  masse_volumique = None
  densité = None # concentration_massique / MVeau

  def __init__(self, solute, solvant):
      self.solute = solute
      self.solvant = solvant

class Substance:
    etat = None # solide / liquide / gazeux
    nom = None
    masse = None # (g)
    volume = None # (l)

    masse_molaire = None # (g/mol)
    nombre_mol = None # (mol) masse_molaire / masse
    masse_volumique = None # (g/l) masse / volume

    def __init__(self):
        return
