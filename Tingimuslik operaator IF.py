

#Ülesanne 1
#1. Juku
#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, 
#kui nimi oli kirjutatud suurtähtedega.
#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. 
#(Tee kontroll, kas sisestatud arv on täisarv)
#<6 aastad  - tasuta
#6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega




# nimi = input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#     if nimi == "JUKU":
#         print("Lähme kinno")
#         try:
#             vanus = int(input(f"Kui vana sa oled {nimi}? "))
#             if vanus < 0:
#                 print("Viga!")
#             elif vanus <= 6:
#                 print("Tasuta")
#             elif vanus < 15:
#                 print("Lastepilet")
#             elif vanus < 65: 
#                 print("Täispilet")
#             elif vanus < 100:
#                 print("Sooduspilet")
#             else:
#                 print("Nii palju!!!")
#         except:
#             print("Täesarv oli vaja sisestada")
#     else:
#         print("Ootan Juku")
# else:
#     print("Segatud sõna")



#Ülesanne 2
#2 соседа на скамейке
#Спросите имена двух человек. Если имена состоят только из букв  , 
#то сообщите пользователю, соседи они сегодня или нет.

# nimi1 = input("1. Mis su nimi on? ")
# nimi2 = input("2. Mis su nimi on? ")
# nimed=["Doris","Kiana"]
# if nimi1.isalpha() and nimi2.isalpha():
#     if nimi1 in nimed and nimi2 in nimed:
#         print("Oleme naabrid")
#     else:
#         print("Me ei ole naabrid")
# else:
#     print("Midagi läks valest")



#Ülesanne 3
# Запросите длины стен прямоугольной комнаты и вычислите площадь пола. 
# Спросите пользователя, хочет ли он сделать ремонт, если он положительный, 
# то спросите, сколько стоит квадратный метр, и узнайте цену замены пола.

# try:
#     a=float(input("Sisesta põranda pikkus: "))
#     b=float(input("Sisesta põranda laius: "))
#     S=a*b
#     print(f"Põranda pindala on {S}")
#     vastus=input("Kas teeme remonti? jah või ei: ")
#     if vastus.upper() == "JAH":
#         print("Teeme remonti")
#         hind=float(input("Kui palju maksab 1 ruutmeetri hind? "))
#         kokku=S*hind
#         print(f"Summa kokku: {kokku}")
#     elif vastus.upper() == "EI":
#         print("Jätame ära")
#     else:
#         print("Viga!")
# except:
#     print("Sul on viga sisestamisel")



#Ülesanne 4
#Найдите цену со скидкой 30%, если первоначальная цена больше 700.

# try:
#     hind=float(input("Hind:"))
#     if hind >= 700:
#         HS=hind-(hind*0.3)
#         print(f"Hind soodustusega: {round(HS,2)}")
#     else:
#         print(f"Hind on sooduseta: {hind}")
# except:
#     print("Viga")



#Ülesanne 5 
#Спросите температуру и скажите, выше ли она 18 градусов (зимой рекомендуется комнатная температура)

# try:
#     temp=float(input("Sisesta temperatuuri: "))
#     if temp >=18:
#         print("Sobiv toasoojus")
#     else:
#         print("Temperatuur on alla 18 kraadi")
# except:
#     print("Viga")



#Ülesanne 6 
#Спросите рост человека и скажите, низкий он, средний или высокий (установите пределы сами)

# try:
#     pikkus=float(input("Mis on sinu pikkus? "))
#     if pikkus <=100:
#         print("Sina oled madala kasvu")
#     elif pikkus <=170:
#         print("Sina oled keskmist kasvu")
#     elif pikkus <=300:
#         print("Sina oled pikka kasvu")
#     else:
#         print("Kas sa oled kindel?")
# except:
#     print("Viga")



#Ülesanne 7 
# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, 
# keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

try:
    sugu=input("Kas sa oled naine (N) või mees (M)?")
    if sugu.upper()=="N":
        pikkus=float(input("Kui pikk sa oled?"))
        if pikkus <=100:
            print("Sina oled madala kasvu")
        elif pikkus <=165:
            print("Sina oled keskmist kasvu")
        elif pikkus <=300:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel?")
    elif sugu.upper()=="M":
        pikkus=float(input("Kui pikk sa oled?"))
        if pikkus <=150:
            print("Sina oled madala kasvu")
        elif pikkus <=190:
            print("Sina oled keskmist kasvu")
        elif pikkus <=300:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel?")
    else:
        print("Sisesta õigesti: Kas N või M")
except:
    print("Midagi läks valesti")