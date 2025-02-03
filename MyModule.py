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
        if log in login:
            print("Selline kasutaja on juba olemas. Vali teine kasutajanimi: ")
        else:
            break
    login.append(log)
    par=parool()
    paroolid.append(par)
    print(f"Olete registreeritud!\nSinu kasutaja nimi on: {log}\nSinu parool on: {par}")
    return True

def parool()->any:
    """Uue parooli sisestamine või genereerimine.
    :rtype: any 
    """
    while True:
        try:
            valik=int(input("Millist parooli soovid?:\n1-Oma parool\n2-Genereeritud parool"))
            if valik==1:
                parool=omaparool()
                break
            elif valik==2:
                parool=genparool()
                break
            else:
                print("Palun vali ainult 1 või 2.")
        except:
            print("Vale sisend! Palun sisesta number 1 või 2.")
    return parool

def omaparool()->any:
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
    return omaparool

def genparool():
    str0=".,:;!_*-+()/#¤%&"
    str1='0123456789'
    str2='qwertyuiopasdfghjklzxcvbnm'
    str3=str2.upper()
    str4=str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    genparool=''.join([random.choice(ls) for x in range(12)])
    return genparool