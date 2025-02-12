from MyModule import *
while True:
    kas=loe_failist('05 - Kasutajate funktsioonid/17 - Registreerimine ja autoriseerimine/Kasutajad.txt')
    sala=loe_failist('05 - Kasutajate funktsioonid/17 - Registreerimine ja autoriseerimine/Salasonad.txt')
    teh=int(input("Tere tulemast! Vali tehing:\n1-Registreerimine\n2-Autoriseerimine\n3-Nime või parooli muutmine\n4-Unustatud parooli taastamine\n5-Lõpetamine.\n\nSinu valik: "))
    print()
    if teh==1:
        reg()
    elif teh==2:
        nim=autorizlog()
        autorizparool(nim)
    elif teh==3:
        chandmed()
    elif teh==4:
        parooltaast()
    elif teh==5:
        print("Head aega!")
        break
    else:
        print("Midagi läks valesti")
        print()
    print(login)
    print(paroolid)
