# def func(val):
#     array = []
#     dopVal = 1
#     while (val > 0):
#         array.append((val%10)*dopVal)
#         val = val//10
#         dopVal*= 10
#     array.reverse()
#     return array



# x = int(input ('введите число: '))
# print(func(x))
import random
b = []
for i in range(3):  
    x = random.randint(1, 8)
    b.append(x)
print(b)
print(random.choice(b))
