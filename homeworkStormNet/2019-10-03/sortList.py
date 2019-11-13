"""Функция сортирует список по возрастанию, заданный пользователем"""

def sortlist(unsortlist):
    sortlist = []
    while unsortlist:
        a = sortlist.append(min(unsortlist))
        unsortlist.remove(min(unsortlist))
    return sortlist

def main():

    print('Enter ten numbers and we\'ll sort its : ')
    unsortlist = []
    one = 1
    while len(unsortlist) != 10:
        print('number', one, ':')
                
        try:
            num = int(input())
            unsortlist.append(num)
            one += 1

        except:
            print('you enter not integer!you must enter integer!')
        
    print('Upgrade list!')
    print(sortlist(unsortlist))

if __name__ == "__main__":
    main()
