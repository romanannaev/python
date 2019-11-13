# function that deletes spaces and calculate long
def main():
    any_string = input('Enter any string: ').split(' ')
    new_string = ''.join(any_string)
    
    if len(new_string) > 5:
        print('string more than 5 symbols')
    elif len(new_string) < 5:
        print('String less than 5 symbols')
    else:
        print('String equil 5')

if __name__ == "__main__":
    main()