X = 12
number1 = []
number = []
number2 = []
for x in range (2, X ):
    y = X/x
    if y == int(y):
        number.append(y)
print(number)

for x in number:
    high =int(x + 1)
    print(high)
    
    for i in range(1, high):
        z = x/i
        if z == int(z):
            number1.append(z)
            if len(number1) > 2 :
                number.remove(number[0])
                index=len(number1)-1
                while index >=0:
                        del number1[index]
                        index-=1
                
                

                break
print(number)                
print(number1)
print(number2)




    
    




