# function that changes register and joines understring
def main():
    any_string = input('Enter any string: ').split(' ')
    print(''.join(any_string).lower())


if __name__ == "__main__":
    main()