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
    c==b==a
    paaris=0 # Убрала лишний =
    paaritu= 0 # Убрала лишний =
    while b > 0: # Заменила ; на :
            if b % 2==0: # Добавила еще одно равно
                paaris =+ 1 # Убрала лишний таб
            else:
                paaritu =+ 1 # Убрала лишний таб
                b = b // 10