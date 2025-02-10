# Ülesanne 4
# Kontrollida N inimese sisestatud isikukoodi õigsust.  Määrake isiku sugu. Mitu inimest N-st on mees ja mitu naissoost, 
# ütle kasutajale.

N=int(input("Mitu isikukoodi soovid kontrollida? "))
km=0
kn=0
for i in range(N):
    ik=input(f"Sisesta isikukood {i+1}: ")
    while True:
        if len(ik)==11 and ik.isdigit(): #len - эта функция считает символы
            break
        else:
            print("Isikukoodis peab olema 11 arvu")
            print()
    if ik[0]=="1" or ik[0]=="3" or ik[0]=="5":
        sugu="mees"
        km+=1
        print(f"See on {sugu}")
        print()
    elif ik[0]=="2" or ik[0]=="4" or ik[0]=="6":
        sugu="naine"
        kn+=1
        print(f"See on {sugu}")
        print()
print(f"Kokku:\nMeest on {km}\nNaist on {kn}")
    