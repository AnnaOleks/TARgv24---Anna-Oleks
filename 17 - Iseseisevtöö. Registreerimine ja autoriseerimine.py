from MyModule import *
while True:
    teh=int(input("Tere tulemast! Vali tehing:\n1-Registreerimine\n2-Autoriseerimine\n3-Nime või parooli muutmine\n4-Unustanud parooli taastamine\n5-Lõpetamine."))
    if teh==1:
        reg()
    else:
        print("Registreerimine ebaonnestunud")