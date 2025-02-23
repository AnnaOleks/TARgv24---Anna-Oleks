from Riigid import *

riik_pealinn,pealeinn_riik,riigid,pealinnad=failist_to_dict('07 - Sõnastikud.Dictionary/riigid_pealinnad.txt')
riigid=list(riik_pealinn.keys())



while True:
    print("Riikide sõnastik! Mida soovid teha? \n1-Sõnastiku kuvamine\n2-Riigi või pealinna kuvamine\n3-Sõnastikku andmete lisamine\n4-Vigade parandamine\n5-Teadmiste kontroll\n6-Välju")
    raagimine("Riikide sõnastik! Mida soovid teha? \n1-Sõnastiku kuvamine\n2-Riigi või pealinna kuvamine\n3-Sõnastikku andmete lisamine\n4-Vigade parandamine\n5-Teadmiste kontroll\n6-Välju", "et")
    vastus=int(input("Sinu valik: "))
    if vastus==1:
        print()
        print(sonasik())
        print()
    elif vastus==2:
        andmkuv()
    elif vastus==3:
        lisamine('07 - Sõnastikud.Dictionary/riigid_pealinnad.txt')
    elif vastus==4:
        uuendamine('07 - Sõnastikud.Dictionary/riigid_pealinnad.txt')
    elif vastus==5:
        kontrolltest()
    elif vastus==6:
        break


    