spisok=[] #пустои список
numbers=[1,2,3,4,5,6]
abc=['a', 'b', 'c']
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-Добавить букву в список")
    print("2-Соединить списки")
    print("3-Добавить букву на i-позицию")
    print("4-Удалить элемент из списка")
    valik=int(input())
    if valik==1:
        a=input("Введи букву: ")
        slovo_list.append(a)
        print(f"Добавили {a} в список.", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву: ")
        i=int(input("Введи номер позиции буквы в списке, куда добавить букву: "))
        slovo_list.insert(i-1, a) #0,1,2,...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, кторую хочешь удалить: ")
        n=slovo_list.count(a)
        if n>0:
            for i in range(n):
                slovo_list.remove(a)
        print(slovo_list)
    else:
        print("Искомой буквы нет")