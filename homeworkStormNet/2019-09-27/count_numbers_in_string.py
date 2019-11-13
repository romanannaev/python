# Пользователь вводит строку, состоящую из различных символов.
# Необходимо написать функцию, подсчитывающую количество цифр в строке.
# Например, пользователь ввел: “fdsk 33 dfsjk 44 jdkf 5”. Функция должна вернуть - 5.

def main():
    any_string = input('Enter any string: ')
    total_number_in_string = []
    for string in any_string:
        if string.isdigit():
            total_number_in_string.append(string)
    print('in string', len(total_number_in_string), 'numbers')


if __name__ == "__main__":
    main()
