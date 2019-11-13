# “Продвинутая” задача:
# Условие – как в предыдущей, но пользователь вводит любое количество положительных цифр в строку:
# “234 43 1 43 43 55 6 6” (пробелов между цифрами может быть несколько). Функция должна вернуть: 1 и 234.
# предусмотреть проверку корректности вводимых данных.


def main():

    any_numbers_in_string = input('Enter any amount positive numbers in string through spaces: ')
    new_
    if any_numbers_in_string.isdigit():

        if '1' in any_numbers_in_string:
            print('1')
        elif '234' in any_numbers_in_string:
            print('234')
        else:
            print('there is\'t numbers "1" and "234"')
    
    else:
        print('False')


if __name__ == "__main__":
    main()

