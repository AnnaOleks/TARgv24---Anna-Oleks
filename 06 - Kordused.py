from random import *

# # Ülesanne 1.    
# # Вводят 15 чисел. Определить, сколько среди них целых.

# kogus=0
# for i in range(15):
#     while True:
#         try:
#             arv=float(input("Sisesta arv: "))
#             break
#         except:
#             print("Sisesta arv")
#     if arv==int(arv):
#         kogus+=1
# print(f"Täisrve: {kogus}")


# # Ülesanne 2.    
# # Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.

# while True:
#     try:
#         A=int(input("SIsesta A: "))
#         break
#     except:
#         print("On vaja naturaalne arv")
# summa=0
# if A>0:
#     for i in range(1,A+1,1):
#         summa+=i        #summa=summa+i
#         print(f"{i}. samm={summa}")
# print(f"vastus {summa}")


# # Ülesanne 3.    
# # Вводят 8 чисел. Найти их произведение (только положительных).

# p=1
# for j in range(8):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {j+1} arv: "))
#             break
#         except:
#             print("On vaja arv")
#     if arv>0: 
#         p*=arv
#     else:
#         print("Korrutame arvud rohkem kui 0")
#     print(f"{j+1}. samm korrutis= {p}")
# print(f"Lõpptulemus on {p}")


# # Ülesanne 4.    
# # Составьте программу, выводящую на экран квадраты чисел от 10 до 20.

# for i in range(10,21,1):
#     print(i**2, end=";")
# print()


# # Ülesanne 5.    
# # Составьте программу, которая вычисляет сумму только отрицательных из N чисел. 
# # Значение N вводится с клавиатуры.

# N=int(input("Sisesta arvude arv: "))
# summa=0
# for i in range(N):
#     arv=float(input("Sisesta arv: "))
#     if arv<0:
#         summa+=arv
#     else:
#         print("Summeeritakse ainult negatiivsed arvud")
# print(f"Kokku: {summa}")
    

# # Ülesanne 6.    
# # С клавиатуры вводятся N чисел.
# # Составьте программу, которая определяет количество отрицательных,
# # количество положительных и количество нулей среди введенных чисел.  
# # Значение N вводится с клавиатуры.

# N=int(input("Sisesta arvude arv: "))
# kogneg=0
# kogpos=0
# kogo=0
# for i in range(N):
#     arv=float(input("Sisesta arv: "))
#     if arv<0:
#         kogneg+=1
#     elif arv==0:
#         kogo+=1
#     else:
#         kogpos+=1
# print(f"Negatiivsed arvud: {kogneg}\nPositiivsed arvud: {kogpos}\n0: {kogo}")


# # Ülesanne 7.    
# # Вывести на экран числа, кратные К из промежутка [А,В].

# K=int(input("Sisesta kordne arv: "))
# A=int(input("Sisesta vahemiku algarv: "))
# B=int(input("Sisesta vahemiku lõpparv: "))
# for i in range(A,B+1):
#     if i%K==0:
#         print(f"Arved {i}")

 
# # Ülesanne 8.    
# # Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры 
# # (1 дюйм = 2,5 см) для значений длин от 1 до 20 дюймов.

# for i in range(1,21,1):
#     sm=i*2.5
#     print(f"{i}. samm={sm}")


# # Ülesanne 9.    
# # В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?

# N=randint(0,30)
# print(f"Aastat: {N}")
# pr=3
# print(f"Protsent: {pr}%")
# sis=5
# print(f"Sissemaks: {sis}€")
# if N>0:
#     for i in range(N):
#         summa=(sis+(sis*0.3))*N
# print(f"Tulemus {summa}€")


# # Ülesanne 10. 
# # Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.

# for i in range(10):
#     try:
#         arv1=float(input("Sisesta arv 1: "))
#         arv2=float(input("Sisesta arv 2: "))
#         if arv1>arv2:
#             print(f"Suurem arv: {arv1}")
#         elif arv2>arv1:
#             print(f"Suurem arv: {arv2}")
#         else:
#             print("Arvud on võrdsed")
#     except:
#         print("Sisesta arv")


# # Ülesanne 11.
# # Найти произведение двузначных нечетных чисел, кратных случайно сгенерированному числу.

# K=randint(2,10)
# print(f"Kordne arv: {K}")
# p=1
# for i in range(10,100):
#     if i%2!=0 and i%K==0:
#         p*=i
#         print(f"Kahekohalise paaritu arvude korrutis: {p}")


# # Ülesanne 12.
# # В бригаде, работающей на уборке сена, имеется N сенокосилок.
# # Первая сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем предыдущая.
# # Сколько часов проработала вся бригада?

# N=randint(1,10)
# print(f"Heinakoristusmeeskonnal on {N} heinakoristusmasinat")
# M=randint(1,8)
# print(f"Esimene heinakoristusmasin töötas {M} tundi")
# kokku=0
# for i in range(N):
#     kokku+=M+i*10/60
# print(f"Heinakoristusmeeskond töötas {kokku} tundi")


# # Ülesanne 13.
# # Найти все натуральные числа от 100 до 1000 кратные 7. И посчитать их колличество и сумму.

# kogus=0
# summa=0
# for i in range(100,1000,1):
#     if i%7==0:
#         kogus+=1
#         summa+=i
# print(f"Arvude kogus: {kogus}\nSumma: {summa}")

# # Ülesanne 14.
# # Составьте программу, которая вычисляет произведение чисел от 1 до N. 
# # Значение N создается случайным образом.

# N=randint(1,100)
# p=1
# for i in range(1,N+1,1):
#     p*=i
# print(f"Arvude korrutus vahemikus 1-{N}: {p}")


# # Ülesanne 15.Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, 
# # то есть в таком виде:
# # 0 1 2 3 4 5 6 7 8 9
# # 0 1 2 3 4 5 6 7 8 9
# # ...................
# # 0 1 2 3 4 5 6 7 8 9

# for read in range(10):
#     for rida in range(10):
#         print('{:>3}'.format(rida**2), end=" ")
#     print()
# print()


# # Ülesanne 16.
# # Напишите программу, печатающую столбик строк такого вида:
# # 1 0 0 0 0 0 0 0 0
# # 0 2 0 0 0 0 0 0 0
# # 0 0 3 0 0 0 0 0 0
# # 0 0 0 4 0 0 0 0 0
# # 0 0 0 0 5 0 0 0 0
# # 0 0 0 0 0 6 0 0 0
# # 0 0 0 0 0 0 7 0 0
# # 0 0 0 0 0 0 0 8 0
# # 0 0 0 0 0 0 0 0 9

# for j in range(10):
#     for i in range(1,10):
#         if i==j:
#             print(j, end=" ")
#         else:
#             print("0", end=" ")
#     print()


# # 17.Напишите программу, печатающую столбик таблицу умножения такого вида:
# # 2*1=2
# # 2*2=4
# # 2*3=6
# # 2*4=8
# # 2*5=10
# # 2*6=12
# # 2*7=14
# # 2*8=16
# # 2*9=18

# kor=1
# for i in range(1,10):
#     kor=2*i
#     print(f"2*{i}={kor}")


# # 18.    Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.

# for i in range(20,50):
#     if i%3==0 and i%5!=0:
#         print(f"{i}")
 

# # 19.    Даны натуральные числа от 35 до 87. Найти и напечатать те из них, которые при делении на 7 дают остаток
# # 1, 2 или 5.
 
# for i in range(35,88):
#     if i%7==1 or i%7==2 or i%7==5:
#         print(i)
 

# # 20.    Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.

# summa=0
# for i in range(1,50):
#     if i%5==0 or i%7==0:
#         summa+=i
#         print(i)
# print(f"Arvude summa: {summa}")


# # 21.    Ввести с клавиатуры 10 чисел – положительных и отрицательных. Заменить все отрицательные числа их
# # модулями и напечатать все полученные 10 чисел.
 
# for i in range(10):
#     arv=float(input("Sisesta arv: "))
#     print(f"Sisestatud arvud {abs(arv)}")


# # 22.    Найти сумму чисел от 100 до 200, кратных 17.
 
# summa=0
# for i in range(100,200):
#     if i%17==0:
#         summa+=i
#         print(i)
# print(f"Arvude summa: {summa}")

 
# # 23.    В ЭВМ вводятся координаты N точек. 
# # Определить, сколько из них попадает в круг радиусом R с центром в точке (a,b).
 
# N=int(input("Sisesta koordinaadide arv: "))
# a=float(input("Sisesta ringi tsentri koordinnat x: "))
# b=float(input("Sisesta ringi tsentri koordinnat y: "))
# R=float(input("Sisesta ringi raadius: "))
# count=0
# for i in range(N):
#     print(f"Koordinaadid {i+1}")
#     x=float(input("Sisesta koordinaat x:"))
#     y=float(input("Sisesta koordinaat y:"))
#     if (x-a)**2+(y-b)**2<=R**2:
#         count+=1
# print(f"Ringis on {count} punkti")


# # 24.    В ЭВМ вводятся по очереди данные о росте N учащихся класса. Определить средний рост учащихся класса.
 
# summa=0
# N=int(input("Sisesta õpileste arv: "))
# for i in range(N):
#     try:
#         pik=float(input("Sisesta õppija pikkus: "))
#         summa+=pik
#     except:
#         print("Sisesta ]ige pikkus")
# print(f"Keskmine pikkus {summa/N}")


# # 25.    Задано натуральное число N. Найти количество натуральных чисел, не превосходящих N и 
# # не делящихся ни на одно из чисел 2, 3, 5.

# N=randint(1,100)
# print(f"Antud naturaalne arv: {N}")
# count=0
# for i in range(N):
#     if i==int(i) and i%2!=0 and i%3!=0 and i%5!=0:
#         print(i)
#         count+=1
# print(f"Naturaalsete arvude kogus vahemikus 1-{N}: {count}")


# 26.    Два двузначных числа, записанных одно за другим, образуют четырехзначное число, которое
# делится на их произведение. Найти эти числа.
 


# 27. Даны два двузначных числа А и В. Из этих чисел составили два четырехзначных числа: первое число
# получили путем написания сначала числа A, а затем В; для получения второго
# сначала записали В, а потом А. Найти числа А и В, если известно, что первое
# четырехзначное число нацело делится на 99, а второе – на 49.

 

# 28.    Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. 
# В конце сообщив количество попыток.

 

# 29.Напишите программу, печатающую столбик строк такого вида:
# x 0 0 0 0 0 0 0 0
# x x 0 0 0 0 0 0 0
# x 0 x 0 0 0 0 0 0
# x 0 0 x 0 0 0 0 0
# x 0 0 0 x 0 0 0 0
# x 0 0 0 0 x 0 0 0
# x 0 0 0 0 0 x 0 0
# x 0 0 0 0 0 0 x 0
# x 0 0 0 0 0 0 0 x

# 30.    В программе создаются 2 случайных числа M и N. И выводятся на экран в срочку 2 последовательности 
# от N к M, и обратно  .

# 31.  Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.
# Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней.
