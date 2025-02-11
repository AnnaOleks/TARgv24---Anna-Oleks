from DefIK import *

ikoodid = []
arvud = []

while True:
    ik=str(input("Sisesta isikukood (süsteemi peatumiseks sisesta X): "))
    print()
    if ik.upper()=="X":
        break
    else:
        IKkontroll(ik,ikoodid,arvud)       
    print(f"Õigete isikukoodide loetelu:\n{ikoodid}")  
    print(f"Valete isikokoodide loetel:\n{arvud}")