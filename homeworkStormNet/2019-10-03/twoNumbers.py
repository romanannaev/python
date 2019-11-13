"""function wich calculate even numbers"""
def twoNumbers(a, c):
    evenNumbers = []
    for i in range(a, c):
        if i % 2 == 0 :
            evenNumbers.append(i)
        else:
            continue
    return evenNumbers

def main():
    print('Введите два числа из диапазона от 1 до 100, чтобы первое было меньше второго')
    print('Например: 25 и 99')
    b = []
    one = 1
    while len(b) != 2:
        print('Number', one)
        try:
            x = int(input())
            b.append(x)
            one += 1

        except:
            print('Введите число!')
    if b:
        a,c = b
        if a < c :
            print(twoNumbers(a, c))
        else:
            print('Read to condition one more time!')
            b.clear()
            main()

if __name__ == "__main__":
    main()