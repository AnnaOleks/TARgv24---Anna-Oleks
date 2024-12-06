from datetime import *
from calendar import *
from time import strptime

#Ülesanne 1. Juku
#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, 
#kui nimi oli kirjutatud suurtähtedega.
#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. 
#(Tee kontroll, kas sisestatud arv on täisarv)
#<6 aastad  - tasuta
#6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega

nimi = input("Mis on sinu nimi? ")
if nimi.isalpha() and nimi.isupper():
    if nimi == "JUKU":
        print("Lähme kinno")
        try:
            vanus = int(input(f"Kui vana sa oled {nimi}? "))
            if vanus < 0:
                print("Viga!")
            elif vanus <= 6:
                print("Tasuta")
            elif vanus < 15:
                print("Lastepilet")
            elif vanus < 65: 
                print("Täispilet")
            elif vanus < 100:
                print("Sooduspilet")
            else:
                print("Nii palju!!!")
        except:
            print("Täesarv oli vaja sisestada")
    else:
        print("Ootan Juku")
else:
    print("Segatud sõna")



#Ülesanne 2 Pinginaabrid
#Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis teavita kasutajat, 
#kas nad on täna pinginaabrid või ei mitte.

nimi1 = input("1. Mis su nimi on? ")
nimi2 = input("2. Mis su nimi on? ")
nimed=["Doris","Kiana"]
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1 in nimed and nimi2 in nimed:
        print("Oleme naabrid")
    else:
        print("Me ei ole naabrid")
else:
    print("Midagi läks valest")



#Ülesanne 3 Remont
#Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. 
#Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, 
#siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind

try:
    a=float(input("Sisesta põranda pikkus: "))
    b=float(input("Sisesta põranda laius: "))
    S=a*b
    print(f"Põranda pindala on {S}")
    vastus=input("Kas teeme remonti? jah või ei: ")
    if vastus.upper() == "JAH":
        print("Teeme remonti")
        hind=float(input("Kui palju maksab 1 ruutmeetri hind? "))
        kokku=S*hind
        print(f"Summa kokku: {round(kokku,2)}")
    elif vastus.upper() == "EI":
        print("Jätame ära")
    else:
        print("Viga!")
except:
    print("Sul on viga sisestamisel")



#Ülesanne 4 Allahindus
#Leia 30% soodustusega hinna, kui alghind on suurem kui 700

try:
    hind=float(input("Hind: "))
    if hind >= 700:
        HS=hind-(hind*0.3)
        print(f"Hind soodustusega: {round(HS,2)}")
    else:
        print(f"Hind on sooduseta: {hind}")
except:
    print("Sul on viga sisestamisel")



#Ülesanne 5 Temperatuur
#Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)

try:
    temp=float(input("Sisesta temperatuuri: "))
    if temp >=18:
        print("Sobiv toasoojus")
    else:
        print("Temperatuur on alla 18 kraadi")
except:
    print("Sul on viga sisestamisel")



#Ülesanne 6 Pikkus
#Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)

try:
    pikkus=float(input("Mis on sinu pikkus? "))
    if pikkus <=100:
        print("Sina oled madala kasvu")
    elif pikkus <=170:
        print("Sina oled keskmist kasvu")
    elif pikkus <=300:
        print("Sina oled pikka kasvu")
    else:
        print("Kas sa oled kindel?")
except:
    print("Sul on viga sisestamisel")



#Ülesanne 7 Pikkus ja sugu
# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, 
# keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

try:
    sugu=input("Kas sa oled naine (N) või mees (M)?")
    if sugu.upper()=="N":
        pikkus=float(input("Kui pikk sa oled?"))
        if pikkus <=100:
            print("Sina oled madala kasvu")
        elif pikkus <=165:
            print("Sina oled keskmist kasvu")
        elif pikkus <=300:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel?")
    elif sugu.upper()=="M":
        pikkus=float(input("Kui pikk sa oled?"))
        if pikkus <=150:
            print("Sina oled madala kasvu")
        elif pikkus <=190:
            print("Sina oled keskmist kasvu")
        elif pikkus <=300:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel?")
    else:
        print("Sisesta õigesti: Kas N või M")
except:
    print("Midagi läks valesti")



#Ülesanne 8 Poes
#Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. 
#Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. 
#Teata, mis summa maksma läheb(Kuva ekraanil tšekk).



#Ülesanne 9 Ruut
#Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

a=float(input("Sisesta külg a: "))
b=float(input("Sisesta külg b: "))
if a==b:
    print("See on ruut")
else:
    print("See on ristkülik")



#Ülesanne 10 Matemaatika
#Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
#Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

a=float(input("Sisesta arv a: "))
b=float(input("Sisesta arv b: "))
vastus=input("Kas soovid + või -: ")
try:
    if vastus=="-":
        c=float(a-b)
        print(f"{a}-{b}={c}")
    elif vastus=="+":
        c=float(a+b)
        print(f"{a}+{b}={round(c,2)}")
except:
    print("Vastus peab olema + või -")


#Ülesanne 11 Juubel
#Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#Plokkskeemi pole vaja!

syn=input("Sisesta oma sünnipäeva YYYY-MM-DD: ")
synp=datetime.strptime(syn, "%Y-%m-%d")
tana=datetime.today()
vanus=tana.year-synp.year
if vanus>0 and vanus%10==0:
    print("Õnnitleme! Sellel aastal on sul juubel")
else:
    print("Juubel on varsti, aga mitte sellel aastal")

    

#Ülesanne 12 Müük
#Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
#Kuva toote lõplik hind. Plokkskeemi pole vaja!

hind=float(input("Sisesta toote hinna: "))
if hind<0:
    print("Hind peab olema rohkem kui 0")
elif 0<hind<10:
    print(f"Saate 10% soodustust. Maksmisele: {hind-(hind*0.1)}")
elif hind>10:
    print(f"Saate 20% soodustust. Maksmisele: {hind-(hind*0.2)}")
else:
    print("Midgi läks valesti")


#Ülesanne 13 Jalgpalli meeskond
#Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
#Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
#Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita

sugu=input("Kas sa oled naine (N) või mees (M)? ")
if sugu.upper()=="N":
    print("Kahjuks naised meeskonnas ei osale")
elif sugu.upper()=="M":
    vanus=int(input("Kui vana sa oled? "))
    if 16<=vanus<=18:
        print("Oled sobiv kandideerija")
    else:
        print("Kahjuks meil on vanuse piirang")
else:
    print("Kirjuta, kas M või N")



# Ülesanne 14 Busside logistika
# Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. 
# Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid, ja mitu inimest on viimases bussis 
# (eeldusel, et eelmised on kõik täiesti täis)? Kirjuta programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande

try:
    inim=int(input("Kui palju inimesi tuleb? "))
    inbuss=int(input("Mitu istekohta on bussis? "))
    if inim % inbuss==0:
        print(f"On vaja {int(inim/inbuss)} bussi")
        print(f"Viimases bussis on {inbuss} inimest")
    elif inim % inbuss!=0:
        print(f"On vaja {int(inim/inbuss)+1} bussi")
        print(f"Viimases bussis on {inim-(int(inim/inbuss))*inbuss} inimest")
    else:
        print("Sisesta õige arv")
except:
    print("Sisesta õige arv")