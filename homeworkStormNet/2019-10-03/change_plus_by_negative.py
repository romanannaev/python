#function that changes plus by negative numbers
def change_plus_by_negative(user_list):
    index = 0
    for i in user_list:
        user_list.insert(index, 0 - i)
        user_list.remove(i)
        index += 1
    return user_list

def main():
    user_list = []
    total_user_list = input('Какое количество положительных чисел вы желаете записать?:')
    numeric = 1
    try:
        while len(user_list) != int(total_user_list):
        
            x = int(input('Number #' + str(numeric) + ':'))
            if x > 0:
                user_list.append(x)
                numeric += 1 
            else:
                print('Entered negative number!Try one more time!:')

        print(change_plus_by_negative(user_list))

    except:
        print("\nEnter a positive digit! \n")
        main()

if __name__ == "__main__":
    main()