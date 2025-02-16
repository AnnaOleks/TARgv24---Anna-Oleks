from random import *

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
        vastus=int(input("Sinu valik: "))
        print()
        if vastus==1:
            pealinn=input("Pealinn: ")
            print()
            if pealinn not in pealinnad:
                print("Sellist pealinna sõnastikus ei ole")
                print()
            else:
                print(f"Riik: {pealinn_riik[pealinn]}\nPealinn: {pealinn}")
                print()
        elif vastus==2:
            riik=input("Riik (väljumiseks vajuta X): ")
            print()
            if riik.upper()=="X":
                break
            elif riik not in riigid:
                print("sellist riiki ei ole")
            else:
                print(f"Riik: {riik}\nPealinn: {riik_pealinn[riik]}")
                print()
        elif vastus==3:
            break
        else:
            print("Vali 1,2,3!")
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