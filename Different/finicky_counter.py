#Привередливая считалка
#демонстрирует работу команд break и continue

count = 0
while True :
    count += 1

# завершить цикл если переменная count принимает значение > 10

    if count > 10:
        break
    # пропустить число 5
    if count == 5:
        continue
    print (count)

input ("\n\n\t press key  enter to exit")
