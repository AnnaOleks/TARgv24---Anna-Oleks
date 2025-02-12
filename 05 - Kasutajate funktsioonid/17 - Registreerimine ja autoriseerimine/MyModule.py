#R#Registreerimine
import random
import smtplib, ssl
from email.message import EmailMessage

login=[]
paroolid=[]

def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend

def kirjuta_faili(fail:str,andmed:list):
    """
    """
    with open(fail, 'w', encoding="utf-8") as f:
        for element in andmed:
            f.write(element + "\n")

def reg()->bool:
    """Uue kasutaja registreerimine. Kasutajanimi ja parooli sisestamine.
    :rtype: bool Väljastab True, kui inimene on registreeritud
    """
    kasutaja=loe_failist('Kasutajad.txt')
    salasonad=loe_failist('Salasonad.txt')
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
    saada_kiri()
    kirjuta_faili('Kasuatajad.txt',login)
    kirjuta_faili('Salasonad.txt',paroolid)
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
    :rtype: str Oma parooli sisestamine
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
                print()
                valju=str(input("Kas soovid proovida uuesti (U) või soovid väljuda (X)? "))
                print()
                if valju.upper()=="U":
                    continue
                elif valju.upper()=="X":
                    break
                else:
                    print("Midagi läks valesti")
                    print()
        except:
            print("Sellist kasutajat ei ole")
            print()
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
            print()
            if sala == paroolid[index_nim]:
                print("Oled autoriseeritud")
                print()
                print()
                break
            else: 
                print("Vale parool. Proovi uuesti!")
                print()
                print()
                while True:
                    try:
                        valju=input("Kas soovid proovida uuesti (U) või soovid väljuda (X)? ")
                        print()
                        print()
                        if valju.upper()=="U":
                            continue
                        elif valju.upper()=="X":
                            break
                        else:
                            print("Midagi läks valesti")
                            print()
                    except:
                        print("Midagi läks valesti")
                        print()
        except:
            print("Sellist kasutajat ei ole")
            print()
    return True

def chname()->bool:
    """Kasutaja nime muutmine
    :rtype: bool Tagastab True, kui nimi on muudetud
    """
    oldname=str(input("Sisesta endine kasutajanimi: "))
    if oldname in login:
        index_oldname=login.index(oldname)
        login.pop(index_oldname)
        while True:
            uusname=str(input("Sisesta uus kasutajanimi: "))
            print()
            if uusname in login:
                print("Kahjuks selline kasutajanimi on juba olemas. Vali teine kasutajanimi!")
                print()
            else: 
                login.insert(index_oldname, uusname)
                print("Kasutajanimi on muudetud")
                print()
                break
    else:
        print("Kahjuks sellist kasutajat ei ole!")
        print()
    return True

def chparool()->bool:
    """Kasutaja parooli muutmine
    :rtype: bool Tagastab True, kui parool on muudetud
    """
    nim=input("Sisesta kasutajanimi: ")
    if nim in login:
        index_nim=login.index(nim)
        while True:
            oldparool=input("Sisesta endine parool: ")
            print()
            if oldparool==paroolid[index_nim]:
                uusparool=parool()
                paroolid.pop(index_nim)
                paroolid.insert(index_nim,uusparool)
                print("Parool on muudetud!")
                print()
                return True
    else:
        print("Kahjuks sellist kasutajat ei ole!")
        print()
    return False

def chandmed()->bool:
    """Kasutaja andmete muutmine
    :rtype: bool Tagastab True
    """
    while True:
        try:
            muutus=int(input("Millised andmed soovid muutuda?\n1-Nimi\n2-Parool\n3-Tagasi\nSinu valik: "))
            print()
            if muutus==1:
                vahetus=chname()
                break
            elif muutus==2:
                vahetus=chparool()
                break
            elif muutus==3:
                return False
                break
            else:
                print("Vale sisend! Vali 1,2 või 3!")
                print()
        except:
            print("Vale sisend! Sisesta number.")
            print()
    return True

def parooltaast()->str:
    """Kasutaja parooli taastamine
    :rtype: str Näitab ekraanil kasutaja parooli
    """
    while True:
        try:
            nim=input("Sisesta kasutajanimi: ")
            print()
            index_nim=login.index(nim)
            par=paroolid[index_nim]
            print(f"Sinu kasutaja nimi on: {nim}\nSinu parool on: {par}")
            print()
            break
        except:
            print("Sellist kasutajat ei ole")
            print()
    return par

def saada_kiri(nimi:str, parool:str):
    kellele=input("Kellele: ")
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="annaoleks88@gmail.com"
    password="xsiw uicd bpgw djpf"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg['Subject']="E-kiri saatmine"
    msg['From']="Anna Oleks"
    msg['To']=kellele
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        print("Informatsioon","Kiri oli saadetud")
    except Exception as e:
        print("Tekkis viga!",e)
    finally:
        server.quit()
    kiri="Sa oled registreeritud. Sinu kasutajanimi on"+nimi+", sinu salasona on "+parool
