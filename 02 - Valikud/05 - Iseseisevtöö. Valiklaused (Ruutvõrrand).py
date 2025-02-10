#Ülesanne 1
# Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное), 
# если число положительное, то проверяет его на  четность и нечетность.

arv=float(input("Sisesta arv: "))
if arv <0:
    print(f"Arv {arv} on negatiivne")
else:
    if arv%2==0:
        print(f"Arv {arv} on positiivne ja paariline")
    else:
        print(f"Arv {arv} on positiivne ja paaritu")



#Ülesanne 2
# Спросить у пользователя 3 числа, если они окажуться положительными, 
# то проверить могут ли они быть углами одного треугольника(сумма углов 180) и 
# уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).

a=float(input("Sisesta arv: "))
b=float(input("Sisesta arv: "))
c=float(input("Sisesta arv: "))
if a<0 or b<0 or c<0:
    print("See ei ole kolmnurk")
else:
    if a+b+c==180:
        if a==b==c:
            print("See on võrdkülgne kolmnurk")
        elif a==b or b==c or c==a:
            print("See on võrdhaarne kolmnurk")
        else:
            print("See on isekülgne kolmnurk")



#Ülesanne 3
# Выяснить у пользователя желание расшифровать порядковый номер дня недели в название. 
# Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), 
# спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.

vastus=input("Kas soovid dešifreerida nädalapäeva numbrit nimes? ")
if vastus.isalpha() or vastus.isupper():
    if vastus=="jah":
        arv=int(input("Sisesta arv 1-7: "))
        if arv == 1:
            print("1 on esmaspäev")
        elif arv == 2:
            print("2 on teisipäev")
        elif arv == 3:
            print("3 on kolmapäev")
        elif arv == 4:
            print("4 on neljapäev")
        elif arv == 5:
            print("5 on reede")
        elif arv == 6:
            print("6 on laupäev")
        elif arv == 7:
            print("7 on pühapäev")
        else:
            print("Sellist päeva ei ole olemas")
    else:
        print("Ei, siis ei")



#Ülesanne 4
# Определить по дню и месяцу рождения пользователя кто он по гороскопу. 
# Проверять введенные данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение!

d=int(input("Sisesta sünnipäeva kuupäev (1-31): "))
m=int(input("Sisesta sünnipäeva kuu (1-12): "))
if (21<= d <=31 and m==3) or (1<= d<=20 and m==4):
    print("Sina oled Jäär")
elif (21<= d <=31 and m==4) or (1<= d<=20 and m==5):
    print("Sina oled Sõnn")
elif (21<= d <=31 and m==5) or (1<= d<=21 and m==5):
    print("Sina oled Kaksikud")
elif (22<= d <=31 and m==6) or (1<= d<=22 and m==7):
    print("Sina oled Vähk")
elif (23<= d <=31 and m==7) or (1<= d<=23 and m==8):
    print("Sina oled Lõvi")
elif (24<= d <=31 and m==8) or (1<= d<=23 and m==9):
    print("Sina oled Neitsi")
elif (24<= d <=31 and m==9) or (1<= d<=23 and m==10):
    print("Sina oled Kaalud")
elif (24<= d <=31 and m==10) or (1<= d<=22 and m==11):
    print("Sina oled Skorpion")
elif (23<= d <=31 and m==11) or (1<= d<=21 and m==12):
    print("Sina oled Ambur")
elif (22<= d <=31 and m==11) or (1<= d<=20 and m==1):
    print("Sina oled Kaljukits")
elif (21<= d <=31 and m==1) or (1<= d<=20 and m==2):
    print("Sina oled Veevalaja")
elif (21<= d <=31 and m==2) or (1<= d<=20 and m==3):
    print("Sina oled Kala")
else:
    print("Sisesta õiged andmed")



#Ülesanne 5
# Проверить введенное пользователем число, отпределить его тип и если число целое, то найти от него 50%, 
# если число дробное, то найти от него 70%, если это текст, то вывести его на экран. Для решения можно использовать: 
# is_integer(), isalpha(), isdigit(), int(), float(), //, %.



#Ülesanne 6
# Написать программу для решения квадратного уравнения a*x**2+b*x+c=0.
# Сначала спрашивается желание решить уравнение и только после утвердительного ответа спросить надо 3 значания: a, b, c.
# Если нет желания решать уравнение, то попрощаться с пользователем.
# Найти D: D=b**2-4ac.
# Если D>0, то 2 решения,
# если D=0, то 1 решение,
# если D<0, то решений нет.
# Ответы огруглить до 2 знаков после запятой.

vast=input("Kas sooovite lahendada võrrandit? jah/ei: ")
if vast =="jah":
    a=float(input("Sisesta arv 1: "))
    b=float(input("Sisesta arv 2: "))
    c=float(input("Sisesta arv 3: "))
    D=b**2-4*a*c
    if D>0:
        x1=print(f"x1={(-b+(D**2))/2*a}")
        x2=print(f"x2={(-b-(D**2))/2*a}")
        print(f"Võrrand: {a}*{x1}**2+{b}*{x2}+{c}=0")
    elif D==0:
        x=print(f"x={-b/2*a}")
        print(f"Võrrand: {a}*{x}**2+{b}*{x}+{c}=0")
    else:
        print("Kahjuks sellisel võrrandil lahendust ei ole")
else:
    print("Head aega")