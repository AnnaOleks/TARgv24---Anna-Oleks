
from random import *
def summa3(arv1:int,arv2:int,arv3:int)->int:
    """Tagastab kolme taisarvu summa

    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int

    """
    summa=arv1+arv2+arv3
    return summa



def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator:
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float b: arv2
    :param str t: arithmeetiline tehing
    :rtype: var Määramata tüüp (float or str)
    """

    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"
    return vastus



def is_year_leap(y:int)->bool:
    """Liigaasta leidmine:
    Tagastab True, kui liigaasta janFalse kui on tavaline aasta
    :param int y: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus
    """

    if y%4==0:
        v=True
    else:
        v=False
    return v



def square(a:float)->float:
    """
    :
    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    return S,P,d



def season(kuu:int)->str:
    """Aastaaja leidmine:
    :param int kuu: kuu number
    :rtype: str Kirjutab mis aastaajale kuu kulub
    """
    talv=[12,1,2]
    kevad=[3,4,5]
    suvi=[6,7,8]
    sugis=[9,10,11]
    if kuu in talv:
        aa="talv"
    elif kuu in kevad:
        aa="kevad"
    elif kuu in suvi:
        aa="suvi"
    else:
        aa="sugis"
    return aa



def bank(a:float,years:int)->any:
    """Protsendi arvestamine:
    :param float a: Sisestatud summa
    :param int years: Mitu aastat 
    :rtype: var Määramata tüüp
    """
    for i in range(years):
        prots=a*0.1
        a=a+prots
    return a



def is_prime(a=randint(0,100))->bool:
    """
    """
    print(a)
    v=True
    for i in range(2,a):
        if a%i==0:
            v=False
    return v



