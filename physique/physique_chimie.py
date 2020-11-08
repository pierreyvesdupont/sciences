print("taper 1 pour resoudre une quantitée de matière")
print("taper 2 pour resoudre une masse volumique")
print("taper 3 pour resoudre une consentration massique")
print("taper 4 pour resoudre une dilution")
resolution=input('que voulez-vous résoudre') 


####la quantitée de matière n = N / Na(6,02*10^23) 
if resolution == 1:
    N=input("quel est le nombre de matière")
    Na=6.02*10^23
    n=N/Na
    print("la quantitée de matière est de "+n+)

####la masse volumique ρ = m(solution) / V(solution)
elif resolution == 2:
    m=input('quel est la masse de la solution')
    V=input('quel est le volume de la solution')
    ρ=m/V
    print("la masse volumique est de "+ρ+)

####la consentration massique Cm = m(soluté) / V(solution)
elif resolution == 3:
    m=input('quel est la masse du soluté')
    V=input('quel est le volume de la solution')
    Cm=m/V
    print("la consentration massique est de "+Cm+)

####la dilution V(mère) * Cm(mère) = V(fille) * Cm(fille)
elif resolution == 4:
    m=input('quel est la masse du soluté')
    V=input('quel est le volume de la solution')
    Cm=m/V
    print("la consentration massique est de "+Cm+)