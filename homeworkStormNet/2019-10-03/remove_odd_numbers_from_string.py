
# function that removes odd numbers from a string
def remove_uneven_numers_from_string(string):
    new_string = ''
    for symbol in string:
        if symbol.isdigit() and int(symbol) % 2 != 0 :
            continue
        else:
            new_string += symbol
    return new_string

def main():
    any_string = input('Enter any string: ')
    if not any_string:
        main()
    else:
        print(remove_uneven_numers_from_string(any_string))

if __name__ == "__main__":
    main()