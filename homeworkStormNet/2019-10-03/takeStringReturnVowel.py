""" Function takes a string and returnes vowel from her"""
def takeStringReturnVowel(string):
    VOWEL = ('A', 'E', 'I', 'O', 'U', 'Y')
    string = list(string)
    sortList = []
    for i in string:
        if i.upper() in VOWEL:
            sortList.append(i)
        else:
            continue
    return ','.join(sortList)

def main():
    print('Enter any expression consist from any simbol')
    string = input()
    print(takeStringReturnVowel(string))

if __name__ == "__main__":
    main()