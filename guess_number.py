#угадай число
#демонстирует работу цикла и не только

print("\n привет и прочая хрень из приветствия")
print("я игра угадай число")
print("правила таковы,угадать число от 1 до 100")
print("я буду подсказывать, но у тебя ограниченное количество попыток")
print ("а именно '10' ")

import random

number = random.randint(1,100)
tries = 0
guess = 0

while guess != number and tries <= 10 :
    guess = int(input("введите число:"))

    if guess > number :
        print("меньше")

    elif guess < number :
        print("больше")
    
    tries += 1

if guess == number:
    print ("ты выиграл! с ", tries , "попытки!)")
elif tries > 10 :
    print (" попытки закончились ,ты проиграл(")


input ("\n\t введите enter чтобы выйти")





    
     

    
