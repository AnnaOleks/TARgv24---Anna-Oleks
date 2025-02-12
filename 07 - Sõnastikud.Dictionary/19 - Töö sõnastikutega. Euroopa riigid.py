from random import *
def failist_to_dict(f:str):
    riik_pealinn={} #sõnastik {"Riik":"Pealinn"}
    pealinn_riik={} #sõnastik {"Pealinn":"Riik"}
    riigid=[] #järjend, kus talletakse riigide nimetused
    file=open(f,'r',encoding="utf-8")
    for line in file:
        k,v=line.strip().split('-') #k-võti, v-väärtus
        riik_pealinn[k]=v #täidame riik_pealinn
        pealinn_riik[v]=k #täidame pealinn_riik
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid

#käivitame loodud funktsiooni
riik_pealinn,pealeinn_riik,riigid=failist_to_dict('riigid_pealinnad.txt')
riigid=list(riik_pealinn.keys())

#list riigid
print(riigid)
print(riik_pealinn.keys())
#list pealinnad
pealinnad=list(riik_pealinn.values())
print(pealinnad)
