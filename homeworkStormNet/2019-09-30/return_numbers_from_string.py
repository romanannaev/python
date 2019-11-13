# 3. Пользователь вводит строку, состоящую из различных символов.
# Написать функцию, возвращающую список цифр введенной строки,
# между которыми нет других символов (кроме пробела).
# Например, пользователь ввел: “a 3 4uyt 6 g 5 67 zz 5,5”. Функция должна вернуть [34,6,567,5,5].



def main():

    any_string = input('enter any string:\n')
    c =[]
    for i in any_string:
        if  i != ' ':
            c.append(i)
    

    print(c)
    b = []
    index = -2
    for i in c:
        index += 1
        if i.isdigit():
            if not len(b):
                b.append(i)
                continue
            elif len(b):
                if c[index].isdigit() or c[index] in (',', '.'):
                    x = b[-1] + str(i)
                    b.insert(-1, x)
                    b.remove(b[-1])
                
                else:
                    b.append(i)
        else:
            if i in (',', '.'):
                if c[index].isdigit():
                    x = b[-1] + str(i)
                    b.insert(-1, x)
                    b.remove(b[-1])
            else:

                continue
        
    print(b)

if __name__ == "__main__":
    main()