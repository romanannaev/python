# 1. Пользователь вводит строку, состоящую из различных символов.
#  Необходимо написать функцию, выводящую сколько раз каждый символ повторяется в строке.
#   Например, пользователь ввел: “a 4 b % c a 5 4”.
#  Функция должна вывести -  ‘a’ – 2, ’4’ - 2, ’b’ - 1, ’%’ – 1, ’c’ - 1, ’5’ - 1



def main():
    any_string = input('Enter any string: ')
    x = any_string.split(' ')
    y = []
    d = {}
    for i in ''.join(x):
        
        if i not in y:
            y.append(i)
            d[i] = any_string.count(i)

    print(d)
    
if __name__ == "__main__":
    main()