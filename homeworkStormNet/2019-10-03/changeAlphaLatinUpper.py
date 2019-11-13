# function wich changes registr latin letters in any string
def change_alpha_registr(string):
    LATINOS = 'A, B, C, D, E, F, G, H, I, K, L, M, N, O, P, Q, R, S, T, V, X, Y, Z, J, U, W'
    new_string = ''
    for symbol in string:
        if symbol.isalpha() and symbol.upper() in LATINOS:
            new_string += symbol.swapcase()
        else:
            new_string += symbol

    return new_string

def main():
        any_string = input('Enter any string: ')
        if not any_string:
            main()
        else:
            print(change_alpha_registr(any_string))

if __name__ == "__main__":
    main()