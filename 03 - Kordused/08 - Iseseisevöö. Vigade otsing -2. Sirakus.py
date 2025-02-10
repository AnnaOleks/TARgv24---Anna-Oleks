# Доказать гипотезу Сиракуз на диапазоне чисел. Гипотеза Сиракуз утверждает, 
# что любое натуральное число сводится к единице в результате повторения следующих действий над самим числом и 
# результатами этих действий.
# Если число четное следует разделить его на 2.
# Если нечетное, то умножить его на 3, прибавить 1 и разделить на 2.
# Найдите и исправьте ошибки в программе:
# Переведи программу на эстонский язык и добавьте в программу комментарии, для пояснения ошибок и того, как работают функции.
# Tõlgi suhtlemise laused eesti keele ja lisa kommentaare koodi seletamiseks.
from time import *

print("*** ARVUDE MÄNG ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => "))) # убрала скобку в начале и добавила скобку в конце / было =(abs(int(input...
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga on mõttetu töö")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu on paaritu arvu")
    print()
    c=b=a # Убрала лишние =
    paaris=0 # Убрала лишний =
    paaritu= 0 # Убрала лишний =
    while b > 0: # Заменила ; на :
        if b % 2==0: # Добавила еще одно равно
            paaris += 1 # Убрала лишний таб и переставила +
        else:
            paaritu += 1 # Убрала лишний таб и переставила +
        b = b // 10
    print(f"Paaris arvude kogus: {paaris}") # Добавила f, переставила ковычки и добавила фигурные скобки / print("Чётных цифр:"paaris)
    print(f"Paaritu arvude kogus:{paaritu}") # Добавила f, переставила ковычки и добавила фигурные скобки / print("Нечётных цифр:"paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud arv")
    print()
    b=0
    while a > 0: # Добавила :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number # Переставила +
    print("*Ümberpööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Tõestame teoreemi") # Убрала лишнуу скобку впереди
    print()
    # if c % 2 == 0:
    #     print(с, " - Paaris arv. Jagame 2.")
    # else:
    #     print(с, " - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1:
        sleep(1) # 1 секунда
        if c % 2 == 0:
            print('{:>4}'.format(round(c))," - Paaris arv, jagame 2.")
            c = c / 2
        else:
            print('{:>4}'.format(round(c))," - Paaritu arv, Korrutame 3, liidame 1 ja jagame 2.")
            c = (3*c + 1) / 2
    print('{:>4}'.format(round(c))," - Teoreem on tõestatud")
    print()
    
