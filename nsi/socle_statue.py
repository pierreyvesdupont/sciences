while True:
    try:
        longueur_base=int(input("la longueur_base: "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")
    
while True:
    try:
        longueur_sommet=int(input("la longueur_sommet: "))
        break
    except ValueError:
        print("Oops! That was no valid number.  Try again...")

u=0
n = longueur_base
while n >= longueur_sommet:
    u += n**2
    n -= 1
print(u)