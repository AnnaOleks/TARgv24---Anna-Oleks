from socket import BDADDR_ANY
from MMM import *

a=int(input("Sisesta arv1: "))
b=int(input("Sisesta arv2: "))
c=input("Sisesta arv3: ")
vastus=summa3(a,b,int(c))
print(vastus)
print()
print()


# Ülesanne 1
# Простейшие арифметические операции
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, 
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; 
# если —, то вычесть; * — умножить; / — разделить (первое на второе). 
# В остальных случаях вернуть строку "Неизвестная операция".

a=int(input("Sisesta arv1: "))
b=int(input("Sisesta arv2: "))
t=str(input("Sisesta argument: "))
vastus=arithmetic(a,b,t)
print(vastus)
print()
print()


# Ülesanne 2
# Високосный год
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

y=int(input("Sisesta aasta: "))
v=is_year_leap(y)
print(v)
print()
print()


# Ülesanne 3
# Квадрат
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: 
# периметр квадрата, площадь квадрата и диагональ квадрата.

a=int(input("Sisesta arv: "))
S,P,d=square(a)
print(S,P,d)
print()
print()


# Ülesanne 4
# Времена года
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
# которому этот месяц принадлежит (talv, kevad, suvi или sügis).

a=int(input("Sisesta kuu number: "))
v=season(a)
print(v)
print()
print()


# Ülesanne 5
# Банковский вклад
# Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, 
#  и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

a=float(input("Sisesta summa: "))
years=int(input("Sisesta mitu aastat: "))
kokku=bank(a,years)
print(kokku)
print()
print()


# Ülesanne 6
# Простые числа
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, 
# и False - иначе.


print(is_prime())
print()
print()


# Ülesanne 7
# Правильная дата
# Написать функцию date, принимающую 3 аргумента — день, месяц и год. 
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.

