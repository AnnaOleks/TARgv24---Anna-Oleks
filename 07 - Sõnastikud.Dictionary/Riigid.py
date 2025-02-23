from multiprocessing.managers import RemoteError
from random import *
from os import system
from gtts import *
import os

riik_pealinn={} #sõnastik {"Riik":"Pealinn"}
pealinn_riik={} #sõnastik {"Pealinn":"Riik"}
riigid=[] #järjend, kus talletakse riigide nimetused
pealinnad=[]  #järjend, kus talletakse pealinnade nimetused

def failist_to_dict(f:str):
    file=open(f,'r',encoding="utf-8")
    for line in file:
        k,v=line.strip().split('-',1) #k-võti, v-väärtus
        riik_pealinn[k]=v #täidame riik_pealinn
        pealinn_riik[v]=k #täidame pealinn_riik
        riigid.append(k)
        pealinnad.append(v)
    file.close()
    return riik_pealinn,pealinn_riik,riigid,pealinnad

def sonasik():
    for k, v in riik_pealinn.items():
        print(k+"-"+v)
    return True

def andmkuv():
    while True:
        print("1-Kuvada riigi\n2-Kuvada paelinna\n3-Välju")
        raagimine("1-Kuvada riigi\n2-Kuvada paelinna\n3-Välju","et")
        vastus=int(input("Sinu valik: "))
        raagimine("Sinu valik","et")
        print()
        print()
        if vastus==1:
            pealinn=input("Pealinn (väljumiseks vajuta X): ")
            raagimine("Pealinn (väljumiseks vajuta X): ","et")
            print()
            if pealinn.upper()=="X":
                break
            elif pealinn not in pealinnad:
                print("Sellist pealinna sõnastikus ei ole")
                raagimine("Sellist pealinna sõnastikus ei ole","et")
                print()
            else:
                print(f"Riik: {pealinn_riik[pealinn]}\nPealinn: {pealinn}")
                raagimine(f"Riik: {pealinn_riik[pealinn]}\nPealinn: {pealinn}","et")
                print()
        elif vastus==2:
            riik=input("Riik (väljumiseks vajuta X): ")
            raagimine(f"Riik (väljumiseks vajuta X)","et")
            print()
            if riik.upper()=="X":
                break
            elif riik not in riigid:
                print("Sellist riiki ei ole")
                raagimine(f"Sellist riiki ei ole","et")
                print()
            else:
                print(f"Riik: {riik}\nPealinn: {riik_pealinn[riik]}")
                raagimine(f"Riik: {riik}\nPealinn: {riik_pealinn[riik]}","et")
                print()
        elif vastus==3:
            break
        else:
            print("Vali 1,2,3!")
            raagimine("Vali 1,2,3!","et")
    return True

def lisamine(f:str):
    while True:
        try:
            riik=input("Sisesta riik (väljumiseks vajuta X): ")
            if riik.upper()=="X":
                break
            pealinn=input("sisesta pealinn: ")
            if riik in riigid or pealinn in pealinnad:
                print("Sellised andmed sõnastikus on juba olemas!")
            else:
                with open(f,'a',encoding="utf-8") as file:
                    file.write(f"{riik}-{pealinn}\n")
                riik_pealinn[riik] = pealinn
                pealinn_riik[pealinn] = riik
                riigid.append(riik)
                pealinnad.append(pealinn)
                print("Andmed on lisatud")
                print()
        except:
            print("Midagi läks valesti")
            print()

def uuendamine(f:str):
    print("Millised andmed soovid uuendada?\n1-Riik\n2-Pealinn")
    try:
        valik=int(input("Sinu valik: "))
        print()
    except:
        print("Vali 1,2,3!")
    if valik==1:
        while True:
            vanariik=input("Sisesta endine riigi nimetus: ")
            if vanariik not in riigid:
                print("Sellist riiki ei ole")
                print()
            else:
                break
        while True:
            uusriik=input("Sisesta uus riigi nimetus: ")
            if uusriik in riigid:
                print("Selline riik on juba olemas")
                print()
            else:
                break
        pealinn = riik_pealinn.pop(vanariik)
        riik_pealinn[uusriik] = pealinn
        pealinn_riik[pealinn] = uusriik
        riigid.remove(vanariik)
        riigid.append(uusriik)
        print("Riik on muudetud")
        print()
    elif valik==2:
        vanapealinn=input("Sisesta endine pealinna nimetus: ")
        if vanapealinn not in pealinnad:
            print("Sellist pealinna ei ole")
            print()
        uuspealinn=input("Sisesta uus pealinna nimetus: ")
        if uuspealinn in pealinnad:
            print("Selline pealinn on juba olemas")
            print()
        riik = pealinn_riik.pop(vanapealinn)
        pealinnad.remove(vanapealinn)
        pealinnad.append(uuspealinn)
        riik_pealinn[riik] = uuspealinn
        pealinn_riik[uuspealinn] = riik
        print("Pealinn on muudetud")
        print()
    elif valik==3:
        return
    else:
        print("Vali 1,2,3!")
    with open(f, 'w', encoding="utf-8") as file:
        for riik, pealinn in riik_pealinn.items():
            file.write(f"{riik}-{pealinn}\n")

def kontrolltest():
    count=0
    kusimusi=0
    print("Alustame testi (väljumiseks vajuta X): ")
    while True:
        kusimusevariant=choice(["riik","pealinn"])
        if kusimusevariant=="riik":
            riik=choice(riigid)
            vastus=input(f"{riik}: pealinn on ")
            oigevastus=riik_pealinn[riik]
            if oigevastus==vastus:
                count+=1
                print("Õige vastus! Tubli!")
                print()
            elif vastus.upper()=="X":
                break
            else:
                print(f"Kahjuks sa eksisid!\nÕige vastus on:\nRiik: {riik}\nPealinn: {oigevastus}")
                print()
        else:
            pealinn=choice(pealinnad)
            vastus=input(f"{pealinn}: riik on ")
            oigevastus=pealinn_riik[pealinn]
            if oigevastus==vastus:
                count+=1
                print("Õige vastus! Tubli!")
                print()
            elif vastus.upper()=="X":
                break
            else:
                print(f"Kahjuks sa eksisid!\nÕige vastus on:\nRiik: {oigevastus}\nPealinn: {pealinn}")
                print()
        kusimusi+=1
    if kusimusi>0:
        tulemus=count*100/kusimusi
        print(f"Sul on {count} õiget vastust. Test on sooritud {tulemus} protsendiks")
        print()

def raagimine(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")
    
 