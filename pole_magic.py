#
#
#
#
WORDS = ("пичуга", "кольчуга", "роман", "африка", "румыния")
import random
word = random.choice(WORDS)
print("\nЯ загадал одно словечко,угадай ,если смогешь.")
print("\nВ слове ", len(word), "букв.")
print("\nТы можешь пять раз спросить у меня наличие букв в этом слове.")
print("\nЯ в свою очередь буду отвечать тебе Yes/No.")
i = 0
while i <= 4 :
    tries = input ("\nВведите возможную букву: ")
    if tries in word :
        print ("\nYes.")
    else:
        print("\nNo.")
    i += 1
print("\nИтак ,попытки закончились,попытайся угадать слово целиком!")
finish = input("\nВведите образец:")
tries1 = 1
while finish != word and finish != "":
    print("\nНеудача!Попробуйте снова!")
    finish = input ("\nВведите ваш вариант:")
    tries1 += 1
if finish == word :
    print ("\nМои поздравления!Ты выиграл с ", tries1 , "попытки." )
print ("\nСпасибо за игру!")
input ("\nВведите Enter , чтобы выйти.")
