# генератор очков
# на 4 навыка имеется 30 пунктов
# задача игрока ,самому распределить/убавить/добавить очки по навыкам

# создадим словарь навыки/значение
skill = {"мудрость" : 0, "сила" : 0, "ловкость" : 0, "здоровье" : 0}
points = 30
choice = None
print("\t\tДобро пожаловать в программу 'Генератор очков'.")
print("\nУ тебя имеется всегда в сумме 30 очков .\n")
print("Ты можешь распределить их между навыками и в последующем изменять.")
print ("\nИз навыков у тебя имеется: мудрость ,сила ,ловкость ,здоровье.")

# цикл с условиями

while choice != "0" :
    print(
"""
    0 - Выйти
    1 - Узнать расстановку очков
    2 - Добавить очки
    3 - Удалить очки
""")
    choice = input ("\nВаш выбор: ")
    if choice == "0":
        print("\nДосвидос.")
        input("\n\nНажмите Enter, чтобы выйти.")
    elif choice == "1":
        print(skill)
    elif choice == "2": # блок добавления очков
        if points > 0:
            term = input ("\nВ какой навык добавим очки? ")
            if term in skill :
                definition = int(input ("\nСколько очков добавляем?\n"))
                if definition <= 30 and definition >=0 :
                    skill[term] += definition
                    points -= definition
                    print("\nНавыку'",term,"'начисленно", definition, "очков." )
                    print("\nУ вас осталось", points, "очков.")
                else :
                    print("\nВведено некорректное количество очков.")
                
            else :
                print ("\nУвы ,такого навыка у вас не имеется.")
        else:
            print('\nУ вас недостаточно очков.')
            
    elif choice == "3":   # блок удаления очков
        term = input ("\nКакой навык подрежем?\n")
        if term in skill:
            if skill[term] != 0:
                definition = int(input("\nНа сколько будем подрезать?\n"))
                if definition >=0 and definition <=30:
                    skill[term] -= definition
                    if skill[term] >= 0:
                            
                        points += definition
                        print("\nНавыку'",term,"'подрезано", definition, "очков." )

                        print("\nУ вас осталось", points, "очков.")

                    else:
                        print("\nНавык не может быть меньше нуля.")
                else :
                    print("\nВведено некорректное количество очков.")
            else:
                print ("\nУвы, но подрезать нечего,навык '",term,"'равен 0.")
       
        else :
                print ("\nУвы ,такого навыка у вас не имеется.")

    
            
