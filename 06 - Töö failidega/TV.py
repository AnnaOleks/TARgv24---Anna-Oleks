import random
import os

def faili_laadimine(fail):
    """Загружаем вопрос-ответ в словарь из файла
    """
    kus_vas={}
    with open(fail,'r', encoding="utf-8-sig") as f:
        for line in f:
            kusimus,vastus=line.strip().split(':')
            kus_vas[kusimus]=vastus
    return kus_vas

def intervue(nimi,kus_vas):
    """Проводим интервью с кандидатом и считаем результаты
    """
    print(f"Tere, {nimi}! Vastage 5 küsimusele.")
    kuslist=list(kus_vas.keys())
    kus_rand=random.sample(kuslist,5)
    points=0
    for kusimus in kus_rand:
        print(f"{nimi}, {kusimus} ")
        vastus=input("Teie vastus: ")
        if vastus.strip().lower()==kus_vas[kusimus].strip().lower():
            points+=1
    return points

def tulemus(fail,kandidaadid):
    """Сохраняем результаты
    """
    with open(fail,'a', encoding="utf-8-sig") as f:
        for nimi,points in kandidaadid:
            f.write(f"{nimi}:{points}\n")

