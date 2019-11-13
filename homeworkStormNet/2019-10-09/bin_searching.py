# Мой бинарный поиск поиск :)

def main():
    print('\tЗагадайте число от 1 до 1000')
    print('\nЯ угадаю его максимум с 9 попытки')
    print('\nесли предложенное мной число меньше вашего, ответьте "-", если больше то "+", если я угадал ответьте "да", поехали!')
    global x
    x = 500
    attempt = 1
    total = [500, ]
    
    while not total:

        print('\nВаше число', x, '?')
        y = input('\nВведите "-", "+", "да": ')
        if y in ("-", "+", "да"):
            if y == "-":
                x = x - x // 2
                total.append(x)

            elif y == "+":
                x = x + x // 2
                total.append(x)
            elif y == "да":
                print('\nя угадал ваше число с ', attempt, 'попытки!')
                break
            attempt += 1

        else:
            print('\nвы че то не то ввели')

    def plus():
        global x
        if total[-2] > total[-1]:
            if len(total) <= 7 :
                x = (total[-2] - total[-1]) // 2  + total[-1]
                total.append(x)
            else:
                x = (total[-3] - total[-1]) // 2 + total[-1]
        else:
            if len(total) <= 7 :
                x = (total[-1] - total[-2]) // 2  + total[-1]
                total.append(x)
            else:
                x = (total[-3] - total[-1]) // 2 + total[-1] + 1

        

    def minus():
        global x
        if total[-2] > total[-1]:
            x = total[-1] - (total[-2] - total[-1]) // 2 
            total.append(x)
        else:
            x = total[-1] - (total[-1] - total[-2]) // 2
            total.append(x)


    while True:

        print('\nВаше число', x, '?')
        y = input('\nВведите "-", "+", "да": ')
        if y in ("-", "+", "да"):
            
            if y == "+":
                if x == 999:
                    print('\nВаше число 1000\n', 'я угадал его с ', attempt, 'попытки!')
                    break
                elif len(total) >= 2:
                    plus()
                else:
                    x += total[-1] // 2 
                    total.append(x)

            elif y == "-":
                if x == 2:
                    print('\nВаше число 2\n', 'я угадал его с ', attempt, 'попытки!')
                    break
                elif len(total) >= 2:
                    minus()
                else:
                    x -= total[-1] // 2 
                    total.append(x)

            elif y == "да":
                print('\nя угадал ваше число с ', attempt, 'попытки!')
                break
            attempt += 1
            print(total)
        else:
            print('\n\nвы че то не то ввели\n\n')

        
if __name__ == "__main__":
    main()
