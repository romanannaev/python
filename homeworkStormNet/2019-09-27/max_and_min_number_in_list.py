# Пользователь вводит 3 числа. Написать функцию, возвращающую минимальное и максимальное число.
# Например, пользователь ввел: “ 5, 28 и -1”. Функция должна вернуть -1 и 28.

def main():
    lst_number = []
    num = 1
    while len(lst_number) != 3:
        try:
            x = int(input('Enter number ' + str(num) + ':'))
            lst_number.append(x)
            num += 1

        except:
            print('Enter NUMBER!')

    print('min number : ', min(lst_number))
    print('max number : ', max(lst_number))

if __name__ == "__main__":
    main()
