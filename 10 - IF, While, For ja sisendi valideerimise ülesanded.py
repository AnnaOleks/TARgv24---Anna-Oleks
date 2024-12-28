from random import *
from math import *

# Ülesanne 1. Определить и вывести максимальное из N вводимых пользователем чисел.

N=int(input("Mitu arvu soovid sisestada? "))
for i in range(N):
    arv=float(input(f"Sisesta arv {i+1}: "))
    if arv>0:
        maxnum=arv
print(f"Maksimaalne arv on {float(maxnum)}")
print()
print()


# Ülesanne 2. Написать программу, которая бы запрашивала целые числа и распечатывала любые значение, кроме13. 
# Если заданное число равно13, вместо него печатается число 77.

for i in range(100):
    try:
        arv=int(input("Sisesta arv: "))
        if arv==13:
            print(77)
        else:
            print(abs(arv))
    except:
        print("Sisesta täisarv")
print()
print()


# Ülesanne 3. Начав тренировки, спортсмен в первый день пробежал 10 км. 
# Каждый день он увеличивал дневную норму на 10% нормы предыдущего дня. 
# Какой суммарный путь пробежит спортсмен за 7 дней?

alg=10
kokku=0
for i in range(7):
    kokku+=alg
    alg*=1.1
    print(f"{i+1} päeval läbis sportlane {round(kokku,2)} km")
print()
print(f"Kokku 7 päeva jooksul sportlane läbis {round(kokku,2)} km")
print()
print()


# Ülesanne 4. Имеется кусок ткани длиной М метров. От него последовательно отрезаются куски разной длины. 
# Все данные по использованию ткани заносятся в компьютер. Компьютер должен выдать сообщение о том, 
# что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется и предложить выкупить остаток. 
# Если пользователь согласен, то продается последний кусок и программа заканчивает работу, если нет, 
# то переходим к следующиму покупателю.

M=abs(randint(1,100))
sumcut=0
while True:
    print("Tere tulemast!")
    klient=input("Mis on teie nimi? ")
    print()
    print(f"Tere {klient}!")
    jaak=M-sumcut
    if jaak <=0:
        print("Kahjuks kangas on otsas")
        break
    while True:
        try:
            cut=float(input("Mitu kanga meetrit soovite: "))
            jaak=M-sumcut
            if cut>jaak:
                while True:
                    vastus=input(f"On jäänud {jaak} m. Kas soovite osta? ")
                    if vastus.lower()=="jah":
                        sumcut+=jaak
                        print("Täname Teid ostu eest!")
                        print()
                        break
                    elif vastus.lower()=="ei":
                        print("Head aega!")
                        print()
                        break
                    else:
                        print("Kas jah või ei?")
                break
            elif cut<=jaak:
                sumcut+=cut
                jaak=M-sumcut
                if jaak <= 0:
                    print("Kahjuks kangas on otsas.")
                    break
                while True:
                    vast=input("Kas soovite veel? ")
                    if vast.lower()=="ei":
                        print("Täname Teid ostu eest!")
                        print()
                        break
                    elif vast=="jah":
                        break
                    else:
                        print("Kas jah või ei?")
                if vast=="ei":
                    break
        except:
            print("Sisesta korrektne arv")
print()
print()


# Ülesanne 5. Составьте программу для вычисления площади трапеций до тех пор пока пользователь не откажется вычислать.

nr=0
print("Tere!\nTrapetsite pindala arvutamiseks on kolm võimalust\n1) Kahe aluse ja kõrguse kaudu\n2) Kesklõigu ja kõrguse kaudu\n3) Diagonaalide ja nendevahelise nurga kaudu")
print()
while True:
    try:
        vastus=input(f"Kas soovid ülesannet {nr+1} lahendada? ")
        nr+=1
        if vastus.lower()=="jah":
            while True:
                try:
                    met=int(input("Millist meetodid valid (1,2,3)? "))
                    if met==1:
                        a=float(input("Sisesta trapetsi aluse pikkus a: "))
                        b=float(input("Sisesta trapetsi aluse pikkus b: "))
                        h=float(input("Sisesta trapetsi kõrgus h: "))
                        S=(a+b)/2*h
                        print(f"Trapetsi pindala on {round(S,2)}")
                        print()
                        break
                    elif met==2:
                        m=float(input("Sisesta trapetsi Kesklõigu pikkus m: "))
                        h=float(input("Sisesta trapetsi kõrgus h: "))
                        S=m*h
                        print(f"Trapetsi pindala on {round(S,2)}")
                        print()
                        break
                    elif met==3:
                        x=float(input("Sisesta trapetsi diagonaali pikkus x: "))
                        y=float(input("Sisesta trapetsi diagonaali pikkus y: "))
                        a=float(input("Sisesta trapetsi diagonaalide vahelise nurk a: "))
                        S=x*y/2*sin(radians(a))
                        print(f"Trapetsi pindala on {round(S,2)}")
                        print()
                        break
                    else:
                        print("Pead valima kas 1, 2 või 3.")
                except:
                    print("Pead valima kas 1, 2 või 3.")
        elif vastus.lower()=="ei":
            print("Täname Teid! Head aega!")
            break
    except:
        print("Pead vastama kas jah või ei")
print()
print()


# Ülesanne 6. Составьте программу, проверяющую, верно ли утверждение, 
# что введенное вами целое число делится без остатка на 3.

while True:
    try:
        vast=input("Kas soovid kontrollida, kas arv on jagatav 3-ga? ")
        if vast.lower()=="jah":
            while True:
                try:
                    arv=int(input("Sisesta arv: "))
                    if arv%3==0:
                        print("Sisestatud arv on jagatav 3-ga")
                        print()
                    else:
                        print("Sisestatud arv ei ole jagatav 3-ga")
                        print()
                    break
                except:
                    print("Peab olema täisarv")
                    print()
        elif vast.lower()=="ei":
            print("\nHead aega!")
            break
    except:
        print("Vastus peab olema jah või ei")
        print()
