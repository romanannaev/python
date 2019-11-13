#
#
#


number = int(input("введите любое число от 1 до 100:"))
if  number>100:
    print ("ты ввел число вне предложенного диапазона подонок")
elif number<=0:
    print ("ты ввел отрицательное число или ноль гавнюк")
guess = 0

tries = 0
import random
while guess != number:
    guess = random.randrange(1,101)
    tries += 1
    
print ("а я его очень быстро угадаю")
print ("\t это число\n" ,guess )
print( "\t\n угадал с  " , tries , "попытки")
input("введите enter дабы выйти")
