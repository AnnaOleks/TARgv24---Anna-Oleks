# #Ülesanne 1
# # Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное), 
# # если число положительное, то проверяет его на  четность и нечетность.

# arv=float(input("Sisesta arv: "))
# if arv <0:
#     print(f"Arv {arv} on negatiivne")
# else:
#     if arv%2==0:
#         print(f"Arv {arv} on positiivne ja paariline")
#     else:
#         print(f"Arv {arv} on positiivne ja paaritu")



# #Ülesanne 2
# # Спросить у пользователя 3 числа, если они окажуться положительными, 
# # то проверить могут ли они быть углами одного треугольника(сумма углов 180) и 
# # уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).

# a=float(input("Sisesta arv: "))
# b=float(input("Sisesta arv: "))
# c=float(input("Sisesta arv: "))
# if a<0 or b<0 or c<0:
#     print("See ei ole kolmnurk")
# else:
#     if a+b+c==180:
#         if a==b==c:
#             print("See on võrdkülgne kolmnurk")
#         elif a==b or b==c or c==a:
#             print("See on võrdhaarne kolmnurk")
#         else:
#             print("See on isekülgne kolmnurk")



# #Ülesanne 3
# # Выяснить у пользователя желание расшифровать порядковый номер дня недели в название. 
# # Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), 
# # спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.

# vastus=input("Kas soovid dešifreerida nädalapäeva numbrit nimes? ")
# if vastus.isalpha() or vastus.isupper():
#     if vastus=="jah":
#         arv=int(input("Sisesta arv 1-7: "))
#         if arv == 1:
#             print("1 on esmaspäev")
#         elif arv == 2:
#             print("2 on teisipäev")
#         elif arv == 3:
#             print("3 on kolmapäev")
#         elif arv == 4:
#             print("4 on neljapäev")
#         elif arv == 5:
#             print("5 on reede")
#         elif arv == 6:
#             print("6 on laupäev")
#         elif arv == 7:
#             print("7 on pühapäev")
#         else:
#             print("Sellist päeva ei ole olemas")
#     else:
#         print("Ei, siis ei")



# #Ülesanne 4
# # Определить по дню и месяцу рождения пользователя кто он по гороскопу. 
# # Проверять введенные данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение!

# d=int(input("Sisesta sünnipäeva kuupäev (1-31): "))
# m=int(input("Sisesta sünnipäeva kuu (1-12): "))
# if (21<= d <=31 and m==3) or (1<= d<=20 and m==4):
#     print("Sina oled Jäär")
# elif (21<= d <=31 and m==4) or (1<= d<=20 and m==5):
#     print("Sina oled Sõnn")
# elif (21<= d <=31 and m==5) or (1<= d<=21 and m==5):
#     print("Sina oled Kaksikud")
# elif (22<= d <=31 and m==6) or (1<= d<=22 and m==7):
#     print("Sina oled Vähk")
# elif (23<= d <=31 and m==7) or (1<= d<=23 and m==8):
#     print("Sina oled Lõvi")
# elif (24<= d <=31 and m==8) or (1<= d<=23 and m==9):
#     print("Sina oled Neitsi")
# elif (24<= d <=31 and m==9) or (1<= d<=23 and m==10):
#     print("Sina oled Kaalud")
# elif (24<= d <=31 and m==10) or (1<= d<=22 and m==11):
#     print("Sina oled Skorpion")
# elif (23<= d <=31 and m==11) or (1<= d<=21 and m==12):
#     print("Sina oled Ambur")
# elif (22<= d <=31 and m==11) or (1<= d<=20 and m==1):
#     print("Sina oled Kaljukits")
# elif (21<= d <=31 and m==1) or (1<= d<=20 and m==2):
#     print("Sina oled Veevalaja")
# elif (21<= d <=31 and m==2) or (1<= d<=20 and m==3):
#     print("Sina oled Kala")
# else:
#     print("Sisesta õiged andmed")