# рандомный порядок слов ,ни разу не повторяющихся 




import random
WORDS = ["КИЕВ", "МИНСК", "ЛОНДОН", "ПАРИЖ", "МОСКВА", "НЬЮ-ЙОРК", "ПЕКИН"]
print(WORDS)
words = []
while len(words) != len(WORDS):
    word = random.choice(WORDS)
    if  word not in words:
        print(word)
        words.append(word)
print(words)
input("\n\tВедите Enter ,чтобы выйти.")
