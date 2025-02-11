from TV import *

kus_vas=faili_laadimine('06 - Töö failidega/kusimused_vastused.txt')
vastuvoetud=[]
eisobi=[]

while len(vastuvoetud)<5:
    nimi=input("Sisestage nimi: ")
    points=intervue(nimi,kus_vas)
    if points>=3:
        vastuvoetud.append((nimi,points))
        vastuvoetud.sort(key=lambda x: x[1], reverse=True)
        tulemus('vastuvoetud.txt',vastuvoetud)
    else:
        eisobi.append((nimi,points))
        eisobi.sort()
        tulemus('eisobi.txt',eisobi)
print("\nVastuvõetud kandidaadid:\n")
for nimi, points in vastuvoetud:
    print(f"{nimi} - {points} õiget vastust")
print("\nKandidaadid, kes ei sobi:\n")
for nimi,points in eisobi:
    print(f"{nimi} - {points} õiget vastust")
