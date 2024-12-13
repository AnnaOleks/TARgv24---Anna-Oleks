p=1
for j in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {j+1} arv: "))
            break
        except:
            print("On vaja arv")
    if arv>0: 
        p*=arv
    else:
        print("Korrutame arvud rohkem kui 0")
    print(f"{j+1}. samm korrutis= {p}")
print(f"Lõpptulemus on {p}")