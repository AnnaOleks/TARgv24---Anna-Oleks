from math import * #muutsin järjestust / import * from math - oli / 


print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #parandasin jutumärgid, lisasin float / 'Sisesta ruudu külje pikkus => ' oli / 
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #parandasin jutumärgid / "Ruudu ümbermõõt'' - oli /
di=a*sqrt(2) #убрала math ja parandasin sqrt / di=a*math.sqr(2) /
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #parandasin jutumärgid ja sulgud / ("Ristküliku karakteristikud")) - oli /
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #lisasin float /
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #lisasin float /
S=b*c
print("Ristküliku pindala", S) #parandasin jutumärgid / (Ristküliku pindala', S) - oli /
P=2*(b+c) #lisasin * / =2(b+c) - oli
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #убрала math ja lisasin * / di=math.sqrt(b*2+c*2) - oli
print("Ristküliku diagonaal", round(di,1)) #parandasin sulgud ja round / ("Ristküliku diagonaal", round(di) /
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #parandasin jutumärgid, lisasin float / ''Sisesta ringi raadiusi pikkus => '' - oli
d=2*r #lisasin * / 2r - oli
print("Ringi läbimõõt", d) #lisasin , / ("Ringi läbimõõt" d) - oli
S=pi*r**2 #parandasin sulgud ja lisasin * / S=pi()*r*2 - oli /
print("Ringi pindala", round(S,2)) #parandasin sulgud ja round / ("Ringi pindala", round(S) + oli /
C=2*pi*r #parandasin sulgud / C=2pi()*r - oli /
print("Ringjoone pikkus", round(C,2)) #parandasin sulgud ja round / ("Ringjoone pikkus", round(C) - oli /




