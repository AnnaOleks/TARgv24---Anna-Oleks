#Registreerimine
import random

login=[]
paroolid=[]

def reg()->bool:
    """Uue kasutaja registreerimine. Kasutajanimi ja parooli sisestamine.
    :rtype: bool Väljastab True, kui inimene on registreeritud
    """
    while True:
        log=input("Sisesta kasutajanimi: ")
        print()
        if log in login:
            print("Selline kasutaja on juba olemas. Vali teine kasutajanimi: ")
            print()
        else:
            break
    login.append(log)
    par=parool()
    paroolid.append(par)
    print(f"Olete registreeritud!\nSinu kasutaja nimi on: {log}\nSinu parool on: {par}")
    print()
    return True

def parool()->str:
    """Uue parooli sisestamine või genereerimine.
    :rtype: str 
    """
    while True:
        try:
            valik=int(input("Millist parooli soovid?:\n1-Oma parool\n2-Genereeritud parool\n\nSinu valik: "))
            print()
            if valik==1:
                parool=omaparool()
                break
            elif valik==2:
                parool=genparool()
                break
            else:
                print("Palun vali ainult 1 või 2.")
                print()
        except:
            print("Vale sisend! Palun sisesta number 1 või 2.")
            print()
    return parool

def omaparool()->str:
    """Oma parooli sisestamine.
    :rtype: any Oma parooli sisestamine
    """
    import string
    markid=string.punctuation
    while True:
        omaparool=input("Sisesta parool (paroolis peavad olema numdrid, väiksed tähed, suured tähed, ja sümbolid): ")
        if (any (mark.isdigit() for mark in omaparool) and any (mark.isupper() for mark in omaparool) and any (mark.islower() for mark in omaparool) and any (mark in markid for mark in omaparool)):
            break
        else:
            print("Parool ei vasta nõuetele! Proovi uuesti.")
            print()
    return omaparool

def genparool()->str:
    str0=".,:;!_*-+()/#¤%&"
    str1='0123456789'
    str2='qwertyuiopasdfghjklzxcvbnm'
    str3=str2.upper()
    str4=str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    genparool=''.join([random.choice(ls) for x in range(12)])
    return genparool

def autorizlog()->str:
    """Sisselogimine. Kasutajanime sisestamine
    :rtype: bool Valjastab True, kui kasutajanimi on listis
    """
    while True:
        try:
            nim=str(input("Sisesta kasutaja nimi: "))
            if nim in login:
                break
            else:
                print("Sellist kasutajat ei ole. Proovi uuesti!")
                valju=str(input("Kas soovid proovida uuesti (U) või soovid väljuda? (X)"))
                if valju.upper()=="U":
                    continue
                elif valju.upper()=="X":
                    break
                else:
                    print("Midagi läks valesti")
        except:
            print("Sellist kasutajat ei ole")
    return nim

def autorizparool(nim:str)->bool:
    """Kasutaja parooli sisestamine.
    param: str nim: Sisestatud kasutajanimi
    :rtype: bool Valjastab True, kui kasutaparool on listis ja on kasutaja parool
    """
    index_nim = login.index(nim)
    while True:
        try:
            sala=input("Sisesta parool: ")
            if sala == paroolid[index_nim]:
                print("Oled autoriseeritud")
                print()
                break
            else: 
                print("Vale parool. Proovi uuesti!")
                print()
                valju=input("Kas soovid proovida uuesti (U) või soovid väljuda (X)? ")
                print()
                if valju=="U":
                    continue
                elif valju=="X":
                    break
                else:
                    print("Midagi läks valesti")
        except:
            print("Sellist kasutajat ei ole")
    return True

def chname()->bool:
    """Kasutaja nime muutmine
    :rtype: bool Tagastab True, kui nimi on muudetud
    """
    oldname=str(input("Sisesta kasutaja nimi: "))
    index_oldname=login.index(nim)