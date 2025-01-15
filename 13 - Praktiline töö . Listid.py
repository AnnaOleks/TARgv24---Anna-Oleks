# # Ülesanne 1 Sõna/Lause
# # Sisestage sõna või lause klaviatuurilt ja loendage, mitu vokaali ja mitu konsonanti selles on.
# # Kui on sisestatud lause, loendage ka kirjavahemärgid ja tühikud.

# import string
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
# konsonanti="qwrtpsdfghklzxcvbnm"
# markid=string.punctuation #Значки !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# while True:
#     v=k=m=t=0
#     tekst=input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list=list(tekst)
#         print(tekst_list)
#         for taht in tekst_list:
#             if taht in vokaali:
#                 v+=1
#             elif taht in konsonanti:
#                 k+=1
#             elif taht in markid:
#                 m+=1
#             elif taht==" ":
#                 t+=1
#     print("Vokaali:",v)
#     print("Konsonanti: ",k)
#     print("Markid: ",m)
#     print("Tühikud: ",t)


# Ülesanne 2 Loetelu
# 2.1 Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
# Lisa võimalist loendis olevaid nimesid muuta.
# 2.2 Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed. opilased = [‘Juhan’,’Kati’,’Mario’,’Mario’,’Mati’,’Mati’]
# Loo kood, mis ei väljasta kordusi.
# 2.3 Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine.

nimed=[]
for nimi in range(5):
    nimi=input(f"Sisesta nimi {nimi+1}: ")
    nimed.append(nimi)
print("Enne sorteerimist:")
print(nimed)
nimed.sort()
print("Sorteerimise pärast:")
print(nimed)
print(f"Viimasena lisatud nimi on: {nimi}") #{nimed[4]}, {nimed[-1]}
v=input("Kas muudame nimeid" ).lower()
if v=="jah":
    v=input("Nime või positsiooni järgi (N/P): ").upper()
    if v=="P":
        print("Sisesta nime asukoht")
        v=int(input())
        uus_nimi=input("Uus nimi: ")
        nimed[v-1]=uus_nimi
        print(nimed)
    else:
        print("Sisesta nimi")
        vana_nimi=input("Vana nimi: ")
        v=nimed.index(vana_nimi)
        uus_nimi=input("Uus nimi: ")
        nimed[v]=uus_nimi
    print(nimed)
# dublikatid 1
dublta=list(set(nimed))
print(dublta)
# dublikatid 2



# 3 Tärnid
# Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm. Näiteks:
# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************

# 4 Postiindex

# Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:

# 1 – Tallinn
# 2 – Narva, Narva-Jõesuu
# 3 – Kohtla-Järve
# 4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa
# 5 – Tartu linn
# 6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa
# 7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa
# 8 – Pärnumaa
# 9 – Läänemaa, Hiiumaa, Saaremaa
# Kirjuta programm, mis kontrollib sisestatud indeksit (tähemärkide arv, vastav andmetüüp jne) ja näitab, millisesse maakonda see kuulub.

# И если почтовый индекс Нарвы, Таллинна и Кохтла-Ярве, то сообщить пользователю "Оставайтесь дома!", в остальных случаях "Носите маски!".

# 5: Vahetus
# Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.

# 6: Бесполезные числа
# Николай задумался о поиске «бесполезного» числа на основании списка.
# Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка и заменяет его в списке результатом деления.
# Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции.

# 7: Sorteerimine
# Teil on vaja luua programm, mis sorteerib numbrite nimekirja kahaneva/kasvava absoluutväärtuse järgi.

# 8: Võrdsepikkusega elemendid
# На входе имеем список строк разной длины.
# ['крот', 'белка', 'выхухоль']
# ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
# ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
# Необходимо написать программу, которая вернет новый список из строк одинаковой длины. Длину итоговой строки определяем исходя из самой большой из них. Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов. Расположение элементов начального списка не менять.
# ['крот____', 'белка___', 'выхухоль']
# ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
# ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']
# 9: Nimi kontroll
# Надо спросить имя человека. Проверь чтобы в имени были только буквы.
# Отобрази приветствие, используя имя с большой буквы.
# Посчитай сколько букв в имени. Найти количество гласных и согласных букв с слове.
# Выведи на экран буквы имени в алфавитном порядке.(если буква встречается несколько раз, то повторять ее не надо)

# 10
# Antud on

# Aadu Suur;56;2500
# Malle Kapsas;42;1500
# Uudo Koba;32;700
# Tiit Kopikas;22;550
# Vahur Vana;67;870
# , kus igal real on töötaja nimi, tema vanus ja kuupalk. Kirjuta programm, mis väljastab antud andmete põhjal:
# kõige suurema palgaga töötaja nime ja palga suuruse (vihje: suurima palga otsimisel jäta meelde, milliselt positsioonilt sa selle leidsid);
# keskmise palga;
# keskmisest palgast rohkem teenijate arvu;
# keskmised vanused eraldi neile, kes teenivad keskmisest palgast vähem (või samapalju), ning neile, kes teenivad keskmisest palgast 

# 11
# Kirjutage programm, mis kuvab ingliskeelse tähestiku n tähest koosneva järjendi ['a', 'b', 'c', ...] alaregistris ja teise järjendi: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...] rohkem.

# 12
# Koostage loend 10 juhuslikust numbrist 1 kuni 100. Kirjutage programm, mis vahetab selle loendi miinimaalse ja maksimaalse elemendid

# 13
# Arva sõna ära
# Looge sõnade järjend. Programm kuvab juhuslikult järjendis oleva sõna alljoontena, olenevalt tähtede arvust.
# Kasutaja sisestab tähe, kui selline täht on olemas, siis alljoone asemel kuvatakse sõna õiges kohas täht. Kui sellist tähte pole, lisatakse see täht arvamata tähtede järjendisse ja see järjend kuvatakse ka. Kui kasutaja arvas sõna ära, peab programm kuvama ka katsete arvu.

# 14
# Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

# Väljasta linnad eraldi ridadena.
# Järjesta need tähestikulisse järjekorda.
# Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
# Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
# Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna", kus linnade arv leitakse vastava funktsiooni abil.
# 15
# Lihtsa sõnaraamatu jaoks koosta neli järjendit (arv, eesti, inglise, itaalia) sisuga: arv - 1, 2, 3, 4 eesti - üks, kaks, kolm, neli inglise - one, two, three, four itaalia - uno, due, tre, quattro

# Väljasta kõik elemendid tabelina ekraanile: 1 - üks - one - uno 2 - kaks - two - due ...

# Lisa arvude ja eesti järjendile veel kaks elementi.
# Kontrolli, kas itaalia sõnade järjendis eksiteerib element 'tre'
# Väljasta kõigi nelja järjendi elemendid tähestikulises järjekorras kasvavalt.
# 16
# Moodusta järjend järgnevate sõnedega:

# Jah, kindlasti!
# Jah!
# Võib-olla!
# Ei!
# Tee programm, kus kasutaja saab küsida jah/ei küsimuse ja programm annab vastuse ühe suvalise elemendi eelnevast järjendist.

# Juhuslike arvude genereerimist vaatame tulevikus, kuid praegu lisame programmi algusesse rea, tänu millele Python suudab juhuslikke arve genereerida:

# import random
# Seejärel võime suvalises kohas programmis kasutada juhusliku arvu saamiseks funktsiooni random.randint(x, y), mis genereerib juhusliku täisarvu x-st y-ni (mõlemad kaasaarvatud), näiteks:

# juhuarv = random.randint(1, 10)
# Lisa ka sisse- ja väljajuhatavad tekstid, et dialoog kasutajaga oleks võimalikult loomulik.

# 17
# Koosta järjend sõnadest. Seejärel koosta programm, mis küsib kasutajalt otsingusõna ja seejärel käib kõik järjendi elemendid läbi ning väljastab ekraanile järjendi elemendi, kui järjendi element sisaldab otsitavat sõna.

# Vihje: sõnest saab otsida reaga "if <otsitavsõna> in sõna".

# Näiteks:

# sona="automobiil"
# if "auto" in sona:
#     print("Jaa, sisaldab sõna")
# 18
# Mõtle ise välja ülesanne ja lahenda seda.
