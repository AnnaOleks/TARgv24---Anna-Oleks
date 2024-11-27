from datetime import *
from calendar import *
from random import *
from math import *
from zlib import decompressobj


#Ülesanne 1
#Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime kasutades ja date.today() funktsiooni abil.
#from datetime import *
#tana=date.today()
#print(f"Täna on {tana}")
#Kasuta erinevate formaatide kuvamiseks ekraanile järgmised funktsioonid:
# 27/12/2022
#tana = tana.strftime("%d/%m/%Y")
# December 27, 2022
#tana = tana.strftime("%B %d, %Y")
# 12/27/22
#tana = tana.strftime("%m/%d/%y")
# Dec-27-2022
#tana = tana.strftime("%b-%d-%Y")
#Funktsioonid day(), month(), year() kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
#Arvuta mitu päeva on jäänud kuu lõppuni, aasta lõppuni.

tana=date.today() #название() - функция (требует скобки)
tanaf=date.today().strftime("%B %d,%Y")

print(f"Tere! Täna on {tanaf}")
d=tana.day #название - свойство (без скобок)
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

novP=monthrange(2024,11)[1] #день недели первого дня месяца и количество дней в этом месяце
jaaknov=novP-d

detsP=monthrange(2024,12)[1]
jaakdets=novP+detsP-d

print(f"Kuu lõppuni on {jaaknov} päeva")
print(f"Aasta lõppuni on {jaakdets} päeva")
print("\n ")


#Ülesanne 2
#Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
#+Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
#+Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

vastus1=3 + 8 / (4 - 2) * 4
vastus2=3 + 8 / 4 - 2 * 4
vastus3=(3 + 8) / (4 - 2) * 4
print(vastus1,"\n",vastus2,"\n",vastus3)
print("\n ")


#Ülesanne 3
#Ruudu sees asub ring. Ringi raadius on R.
#Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.

try: #помещается код, который может вызвать ошибку
    R=float(input("sisesta R: "))
    Sk=pi*R**2 #** - степень
    Lk=2*pi*R
    Skv=R*2**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
except: #действия, которые будут выполнены в случае возникновения ошибки
    print("On vaja number")
print("\n ")

R=int(random()*100) #генерирует значения от 0.0...1.0
print(f"R={R}")
Sk=pi*R**2 #** - степень
Lk=2*pi*R
Skv=R*2**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
print("\n ")


#Ülesanne 4
#Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.
#Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
#Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
#Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?

maa=6378
d=2.575
maa*=100000 #maa=maa*100000
Lmaa=2*pi*maa
kogus=int(Lmaa/d)
print(f"On vaja {kogus} mündi.\nMeil on vaja {kogus*2} eur")
print("\n ")


#Ülesanne 5
#Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
#kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll kill-koll
#Saab kasutada muutujaid. Kuva iga sõna suure tähega.

k1="kill-koll ".capitalize()
k2="killadi-koll ".capitalize()
print(f"{k1*2}{k2}{k1*2}{k2}{k1*4}")
print("\n ")


#Ülesanne 6
#Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:

a="""
rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
aga seal rongi peal,
kas sa tead, kes olid seal?

rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
""".upper()
print(f"{a}")
print("\n ")


#Ülesanne 7
#Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.

a=float(input("Sisesta ristküliku lähiskülje pikkus a: "))
b=float(input("Sisesta ristküliku lähiskülje pikkus b: "))
P=2*(a+b)
S=a*b
print(f"Ristküliku ümbermõõt: {P}")
print(f"Ristküliku pindala: {S}")
print("\n ")


#Ülesanne 8
#Kütusekulu arvutamine
#Kasutaja sisestab tangitud kütuse liitrid
#Kasutaja sisestab läbitud kilomeetrid
#Programm leiab kütusekulu 100km kohta keskmiselt

TL=float(input("Sisesta tangitud kütuse liitrid: "))
LK=float(input("Sisesta läbitud kilomeetrid: "))
KK=TL*100/LK
print(f"Kütusekulu 100km kohta keskmiselt: {round(KK,2)}")
print("\n ")


#Ülesanne 9
#Rulluisutajad
#Rulluisutaja keskmine kiirus on 29,9km/h
#Kui kaugele jõuab M minutiga
M=int(random()*1000)
M/=60
KK=29.9
KM=M*KK
print(f"Rulluisutaja keskmine kiirus: {KK}")
print(f"Aeg: {M}")
print(f"Läbitud kaugus: {KM}")
print("\n ")


#Ülesanne 10
#Ajateisendus
#Kasutaja sisestab aja minutites
#Sinu valem leiab ja väljastab tunnid ja minutid
#Näiteks: sisestus 72, vastus 1:12

MIN=int(input("Sisesta aja minutites: "))
H=MIN//60
M=int((MIN/60-H)*60)
print(f"{H} tundi ja {M} minutit")
