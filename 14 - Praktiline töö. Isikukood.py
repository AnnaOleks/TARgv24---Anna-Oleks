# Проверка личного кода
# Безконечно запрашиваем личные коды.
# Проверяем их:
# - если 11 символов/чисел, то продолжаем проверку, если нет, то сообщить, что кол-во цифт не верное и запрашивает новый личный код,
# Первый символ только:1,2,3,4,5,6, если числа другие, то прерываем проверку и запрашиваем новый личный код,
# Второй-седьмой символы- должны сообветствовать цифрам дат рождения, если нет, то новый личный код,
# Найти контрольный номер (смотри ниже пояснение)
# * Если личный код правильный, то добавить его в список ikoodid, а на экран вывести фразу:
# Это {пол}, его/ее день рождения {дата рождения}  и место рождения {название города и больницы}
# * Если код не верный, то он добавляется в список arvud

# После прерывания бесконечного цикла проверки, надо вывести на экран оба списка (ikoodid, arvud).
# Список arvud упорядочи по-возростанию, список ikoodid отобрази таким образом, что сначала личные коды женщин, потом мужчин.
# Способ остановки цикла придумай сам.

# Например: Если личный код 47610112243, то будет след. фраза: Это женцина, его/ее день рождения 11.10.1976  и место рождения Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi).

# Пол 1,3,5 -муж, 2,4,6-жен

# Kontrollnumber
# I astme kaal: 1 2 3 4 5 6 7 8 9 1
# II astme kaal: 3 4 5 6 7 8 9 1 2 3
# See tähendab, et isikukoodi kümme esimest numbrit korrutatakse igaüks
# omaette I astme kaaluga, korrutised liidetakse.
# Saadud summa jagatakse 11ga.
# Kui jagatise jääk ei võrdu 10ga, on jääk kontrollnumbriks.
# Kui jääk võrdub 10ga, siis korrutatakse koodi kümme esimest numbrit igaüks omaette II astme kaaluga. Korrutised liidetakse. Saadud summa jagatakse 11ga. 
# Kui jääk ei võrdu 10ga, on saadud jääk kontrollnumbriks. Kui jääk võrdub 10ga, siis on kontrollnumber 0.
# Näide: isikukoodi 37605030299 kontroll:
# Summa = 1×3 + 2×7 + 3×6 + 4×0 + 5×5 + 6×0 + 7×3 + 8×0 + 9×2 + 1×9 = 108.
# 108 jääk jagamisel 11-ga on 9. (108/11 ~ 9,8. Täisosa on seega 9.
# Siit 9*11 = 99. Lahutades 108 – 99 = 9, mis ongi jääk).
# Nii peabki isikukoodi 37605030299 viimane number olema 9.

# Haiglatele eraldatud järjekorranumbri vahemikud arvatakse olevat üldjoontes järgmised:

# 001...010 = Kuressaare Haigla

# 011...019 = Tartu Ülikooli Naistekliinik, Tartumaa, Tartu
# 021...220 = Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla
# 221...270 = Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)
# 271...370 = Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla
# 371...420 = Narva Haigla
# 421...470 = Pärnu Haigla
# 471...490 = Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla
# 491...520 = Järvamaa Haigla (Paide)
# 521...570 = Rakvere, Tapa haigla
# 571...600 = Valga Haigla
# 601...650 = Viljandi Haigla
# 651...700? = Lõuna-Eesti Haigla (Võru), Põlva Haigla

from datetime import *
ikoodid=[]
arvud=[]
esarv=['1','2','3','4','5','6']
today=datetime.now().date()
year=today.year-2000
month=today.month
day=today.day
esastme=[1,2,3,4,5,6,7,8,9,1]
tteineastme=[3,2,3,4,5,6,7,8,9,1,2,3]
while True:
    ik=str(input("Sisesta isikukood (süsteemi peatumiseks sisesta X): "))
    if ik.upper()=="X":
        break
    else:
        if len(ik)==11 and ik.isdigit():
            print("OK")
            if ik[0] in esarv:
                print("OK")
                if ik[0] in ['1','2','3','4'] or (ik[0] in ['5','6'] and int(ik[1:3])<=year):
                    print("OK")
                    if 0<int(ik[3:5])<=12 or (ik[0] in ['5','6'] and int(ik[3:5])<=month):
                        print("OK")
                        if 0<int(ik[5:7])<=31 or (ik[0] in ['5','6'] and int(ik[5:7])<=day):
                            for ik in range(ik[0:11]):
                        else:
                            print("Sellist kuupäeva ei ole")
                    else:
                        print("Sellist kuud ei ole")
                else:
                    print("selline isikukood võib olla ainult tulevikus")
            else:
                print("Esimene sümbol ei ole õige")
                print()
        else:
            print("Isikukoodis peab olema 11 märgi")
            print()
    