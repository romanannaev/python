# i'm lazy boy to write comments:(
menu = """
1.Enter '1' if you want to exit!

2.Enter '2' if you want to add book!

3.Enter '3' if you want to find book and information about it!

"""
import datetime
import os
if not os.path.isfile('library_db.txt'):
    with open('library_db.txt', 'w') as f:
        f.write('Library Data Base --- ' + str(datetime.datetime.now()) + '\n')

def print_something(something):
    print(something)

def add_dictionary(library, values, file='library_db.txt'):
    library[values[0]] = values

    with open(file, 'a') as f:
        f.write('Book name: ' + str(values[0]) + ' = ' + str(values) + '\n')

    library['count_books'][0] += 1 
    return library

def find_book(library, look_for):
    for key in library:
        print('everything books which you look for with: ', look_for.upper())
        if look_for in library[key]:
            print('1: ', library[key])
    print('Amount of books in library are: ', library['count_books'])

def main(menu, library):
    while True:
        print_something(menu)
        try:
            answer = int(input('Your answer: '))
        except:
            print('Read menu one more times!')
            main(menu, library)

        if answer == 1:
            print('good luck!')
            break

        elif answer == 2:
            values = (input('Enter your book\'s name, autor, genre, produce, year of produce: ')).split(' ')
            add_dictionary(library, values)

        elif answer == 3:
            look_for = input('Enter name\'s book and autor and genre and produce and year of produce to find \
that there is in a library: ')
            find_book(library, look_for)

        else:
            print('you entered some хрень!')


if __name__ == "__main__":
    library = {'count_books' : [0]}
    main(menu, library)

