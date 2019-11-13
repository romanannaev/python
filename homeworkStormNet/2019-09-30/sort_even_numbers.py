# 2. Пользователь вводит через input любое кол-во положительных цифр в список 
# (ввод данных прекращается, например, по введению пустого значения или 0 – не принципиально). 
# Написать функцию, возвращающую список четных чисел введенного списка, отсортированный по возрастанию.
#  Например, пользователь ввел: [4,12,7,9,1,4].
#  Функция должна вернуть – [4,4,12]. Предусмотреть проверку корректности вводимых данных.

def even_number(total_list):
    print(total_list)
    new_list = []
    for i in total_list:
        if i % 2 == 0:
            new_list.append(i)
        
    print(sorted(new_list))



def main():

    print('to exit enter "0" ')
    total_list = []
    while True:
        
        try:
            any_numbers = int(input('enter any amount positive numbers: '))
            if  any_numbers == 0:
                break
            else:
                total_list.append(any_numbers)
        except:
            print('enter positive number or "0" for exit!')
    even_number(total_list)



        







if __name__ == "__main__":
    main()