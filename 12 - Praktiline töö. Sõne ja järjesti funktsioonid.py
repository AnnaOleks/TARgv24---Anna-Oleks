tasks=[]
while True:
    print("1-Добавить задачу")
    print("2-Удалить задачу")
    print("3-Показать задачи")
    print("4-Сортировать задачи")
    print("5-Добавить задачу в конкретное место в списке")
    print("6-Удалить весь список")
    print("7-Выйти из программы")
    print()
    while True:
        try:
            valik=int(input("Твой выбор: "))
            break
        except:
            print("Выбери значение 1-8")
            print()
    if valik==1:
        while True:
            vastus=input("Задача: ")
            tasks.append(vastus)
            print(f"Ваша задача -{vastus.capitalize()}- добавлена в список")
            print()
            while True:
                soov=input("Еще? (да/нет) ").strip().lower()
                if soov=="нет":
                    print()
                    break
                elif soov=="да":
                    print()
                    break
                else: 
                    print("Да или нет")
                    print()
            if soov=="нет": 
                break
    elif valik==2:
        vastus=input("Удалить: ")
        n=tasks.count(vastus)
        print()
        if n>0:
            for i in range(n):
                tasks.remove(vastus)
        print(f"Ваша задача {vastus.capitalize()} удалена из списка")
        print()
    elif valik==3:
        print(f"В твоем списке задач: {tasks}")
        print()
    elif valik==4:
        tasks.sort()
        print(f"Твой отсортированный список задач: {tasks}")
        print()
    elif valik==5:
        soov=input("Задача: ")
        koht=int(input("Позиция: "))
        tasks.insert(koht-1, soov)
        print(f"Задача -{soov}- добавлена на {koht} позицию")
        print()
    elif valik==6:
        tasks.clear()
        print(f"Ваш список задач удалён {tasks}")
        print()
    elif valik==7:
        print("До свилания!")
        break
