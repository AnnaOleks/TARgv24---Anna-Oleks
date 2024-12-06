from random import * #*-kõik funktsioonid, randint as rd funktsioonide ümbernimetus
from math import * #pi kasutamiseks


#Ülesanne 1
print("Tere tulemast!") #print-вывод
nimi=input("Mis on sinu nimi? ").capitalize() #input-ввод и замещение #lower(), upper()
print("Tere tulemast! Tervitan sind",nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
vanus=int(input("Kui vana sa oled? ")) #int-целая цифра
print("Tere tulemast! Tervitan sind "+nimi+" Sa oled",vanus,"aastat vana")
print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana") #f-делает в тексте скобками {.} функцию


#Ülesanne 2
vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))


#Ülesanne 3
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")


#Ülesanne 4
print("Läbimõõdu leidmine")
#´l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")


#Ülesanne 5
N=float(input("Külg 1: "))
M=float(input("Külg 2: "))
L=sqrt(pow(N,2)+pow(M,2))
print(f"Maatüki diagonaal on {round(L,2)}")


#Ülesanne 6
aeg=float(input("Mitu tundi kulus sõiduks? "))
teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
kiirus=teepikkus/aeg
print(f"Sinu kiirus oli {round(kiirus,2)} km/h")


#Ülesanne 7
A=int(input("Arv 1: "))
B=int(input("Arv 2: "))
C=int(input("Arv 3: "))
D=int(input("Arv 4: "))
E=int(input("Arv 5: "))
F=(A+B+C+D+E)/5
print(f"Keskmine aritmeetiline: {F}")


#Ülesanne 8
print(" @..@ ")
print("(----)")
print("(\__/)")
print("^^ "" ^^")


#Ülesanne 9
a=int(input("Külg a: "))
b=int(input("Külg b: "))
c=int(input("Külg c: "))
P=a+b+c
print(f"Ümbermõõt: {P}")


#Ülesanne 10
pizza=12.90
jootraha=12.90*0.1
summa=pizza+jootraha
üks=summa/2
print(f"Pzzi maksab: {pizza}")
print(f"Jootraha: {jootraha}")
print(f"Summa: {round(summa,2)}")
print(f"Anna peab maksma: {round(üks,2)}")
print(f"P peab maksma: {round(üks,2)}")
