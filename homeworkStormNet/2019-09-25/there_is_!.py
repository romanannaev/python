# function that definits '!' in string
def main():
    any_string = input('Enter anystring: ')
    if '!' in any_string:
        print('"!" there is in this string')
    else:
        print('"!" there isn\'t in this string')

if __name__ == "__main__":
    main()