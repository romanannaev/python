    #game in craps
    #демострирует
 #случайные числа из диапазона 1-9
import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1+die2


print("При вашем броске выпало", die1, "и" ,
          die2 ,"в сумме", total)

input('\n\n\n нажми')
    
