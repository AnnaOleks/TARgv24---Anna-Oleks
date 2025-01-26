from datetime import *

def pikkus (ik:str)->bool:
    """Kontrollime isikukoodi arvude kogust
    :param str ik: isikukood
    :rtype: bool
    """
    return len(ik)==11 and ik.isdigit()
    
def esnum (ik:str)->bool:
    """Kontrollime esimest arvu. Esimene arv peab olema vahemikkus 1-6.
    :param str ik: isikukood
    :param int esarv: Esimene arv
    :rtype: bool
    """
    esarv=['1','2','3','4','5','6']
    return ik[0] in esarv

def aasta(ik:str)->int:
    """Aasta leidmine
    :param str ik: isikukood
    :rtype: int Aasta
    """
    if ik[0] in ['1','2']:
        sunaasta=1800+int(ik[1:3])
    elif ik[0] in ['3','4']:
        sunaasta=1900+int(ik[1:3])
    elif ik[0] in ['5','6']:
        sunaasta=2000+int(ik[1:3])
    else:
        sunaasta=False
    return sunaasta

def kuu(ik:str)->int:
    """Kuu leidmine. 
    :param str ik: isikukood
    :rtype: int Kuu
    """
    sunkuu=int(ik[3:5])
    return sunkuu

def paev(ik:str)->int:
    """Paeva leidmine. 
    :param str ik: isikukood
    :rtype: int Paev
    """
    sunpaev=int(ik[5:7])
    return sunpaev

def sunnipaev(ik:str)->date:
    """Sunnipaeva kontroll. 
    :param str ik: isikukood
    :rtype: date
    """
    try:
        sunyear=aasta(ik)
        sunmonth=kuu(ik)
        sunday=paev(ik)
        sunn=date(sunyear,sunmonth,sunday)
        if sunn>date.today():
            return None
        return sunn
    except:
        return None

def haigla(ik:str)->str:
    """Haigla leidmine
    :param str ik: isikukood
    :rtype: str
    """
    if 0<int(ik[7:10])<=10:
        haigla="Kuressaare Haigla"
    elif 11<=int(ik[7:10])<=19:
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=int(ik[7:10])<=220:
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<=int(ik[7:10])<=270:
        haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271<=int(ik[7:10])<=370:
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<=int(ik[7:10])<=420:
        haigla="Narva Haigla"
    elif 421<=int(ik[7:10])<=470:
        haigla="Pärnu Haigla"
    elif 471<=int(ik[7:10])<=490:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<=int(ik[7:10])<=520:
        haigla="Järvamaa Haigla (Paide)"
    elif 521<=int(ik[7:10])<=570:
        haigla="Rakvere, Tapa haigla"
    elif 571<=int(ik[7:10])<=600:
        haigla="Valga Haigla"
    elif 601<=int(ik[7:10])<=650:
        haigla="Viljandi Haigla"
    elif 651<=int(ik[7:10])<=700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla=False
    return haigla

def kontrollnumber(ik):
    esastme=[1,2,3,4,5,6,7,8,9,1]
    teineastme=[3,2,3,4,5,6,7,8,9,1,2,3]
    esastmesumm=0
    for i in range(10):
        summ=int(ik[i])*esastme[i]
        esastmesumm+=summ
        esjaak=esastmesumm%11
        if esjaak !=10:
            kontroll=esjaak
        elif kontroll==10:
            teineastmesumm=0
            for i in range(10):
                summ=int(ik[i])*teineastme[i]
                teineastmesumm+=summ
                teinejaak=teineastmesumm%11
                if teinejaak !=10:
                    kontroll=teinejaak
                elif teinejaak==10:
                    kontroll=0
    return kontroll

def sugu(ik:str)->str:
    """Leiame sugu
    :param str ik: isikukood
    :rtype: str
    """
    if ik[0] in ['2','4','6']:
        return "naine"
    elif ik[0] in ['1','3','5']:
        return "mees"
    else:
        return False
    
def IKkontroll(ik:str, ikoodid:list, arvud:list):
    if pikkus(ik):
        if esnum(ik):
            if sunnipaev(ik):
                if kontrollnumber(ik)==int(ik[-1]):
                    if haigla(ik):
                        if sugu(ik):
                            print(f"See on {sugu(ik)}. Ta on sündinud {sunnipaev(ik)} ja sünnikoht on {haigla(ik)}")
                            ikoodid.append(ik)
                            print()
                    else:
                        print("Sellist haiglat ei ole!")
                        arvud.append(ik)
                        print()
                else:
                    print("Kontrollnumber ei ole õige!")
                    arvud.append(ik)
                    print()
            else:
                print("Sünnipäev ei ole õige!")
                arvud.append(ik)
                print()
        else:
            print("Esimene sümbol ei ole õige")
            arvud.append(ik)
            print()
    else:
        print("Isikukoodis peab olema 11 märgi")
        arvud.append(ik)
        print()   
