def main():
    print('\tЗагадайте число от 1 до 1000')
    print('\nЯ угадаю его максимум с 12 попытки')
    print('\nесли предложенное мной число меньше вашего, ответьте "-", если больше то "+", если я угадал ответьте "да", поехали!')

    x = 500 #задаем пока жестко середину заданного интервала
    attempt = 1 #
    total = [500, ] #сразу делаем как непустой список для цикла, я так захотел 
    y = [] #список введеных ответов

    while total:

        print('\nВаше число', x, '?')
        answer = input('\nВведите "-", "+", "да": ')
        y.append(answer) #сразу добавляем ответ чтоб непустой был список,я использовал для условий
        print(total) #делаем принты для себя
        print(y)
        if answer in ("-", "+", "да"): # тип минимальная проверка на кореектность


            if answer == "-": #в зависимости от ответа использую для условия че будет делать


                if "+" in y and len(total) <= 8: # 8 это тут по моим наблюдениям с такой примерно длины начинается
                # детальная разбивка интервалов значений ,чтоб уменьшить количество попыток 
                # + это для того чтоб не выкидывало ошибку на условие total[-2], так как нет еще индекса

                    
                    if total[-2] > total[-1]:  #типа побыстрее делит интервалы пока список меньше 8 
                        x = total[-1] - (total[-2] - total[-1]) // 2 
                        total.append(x)
                    else:
                        x = total[-1] - (total[-1] - total[-2]) // 2  
                        total.append(x)



                elif "+" in y and len(total) > 8:


                    if total[-2] > total[-1]: # это подетальнее режет интервалы, когда уже практически у цели
                        x = total[-1] - (total[-2] - total[-1])
                        total.append(x)
                    else:
                        x = total[-1] - (total[-1] - total[-2]) // 2  
                        total.append(x)
                
                    
                else: # если число к примеру 1 то будет польвателю надо будет вводить раз за разом '-'

                    x = x - x // 2
                    total.append(x)

           



            elif answer == "+":     # тут тоже самое как вверху ток логика на добавление 

                if "-" in y and len(y) <= 8:
                    
                    if total[-2] > total[-1]:

                        x = (total[-2] - total[-1]) // 2 + total[-1]
                        total.append(x)

                    else:
                        x = (total[-1] - total[-2]) // 2 + total[-1]
                        total.append(x)

                elif "-" in y and len(y) > 8:

                    if total[-2] > total[-1]:

                        x = (total[-2] - total[-1]) // 2 + total[-1] 
                        total.append(x)

                    else:
                        x = (total[-1] - total[-2]) + total[-1] 
                        total.append(x)

                else:
                    x += 250
                    total.append(x)

            

            elif answer == "да":
                print('\nя угадал ваше число с ', attempt, 'попытки!')
                break
            attempt += 1

        else:
            print('\nвы че то не то ввели')

if __name__ == "__main__":
    main()
