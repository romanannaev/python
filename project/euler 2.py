#сумма четных чисел ряда фибоначчи

#создадим список из чисел ряда фибоначчи 
number = [1, 2]
total = 2
x = 5
while total <= 4000000 :
    high_position = len(number) - 1
    low_position = high_position - 1
    i = number[high_position] + number[low_position]
    number.append(i)
    if len(number) == x:
        total += number[x - 1]
        x += 3
        
    else :
        total += 0
    if len(number) ==32:
        break
    
    
print(number)
print(len(number))
print(total)



    
   

    