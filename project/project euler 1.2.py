#первая задача эйлера другим методом
#через цикл while и условие if 

number =0
number2 = 0
total1 =0
total2 = 0
total3 = 0
print("\nВот числа кратные 3:")

while number <=1000:
    number+=1
    if (number % 3)!=0:
        continue
    total1+=number
    print (number, end=" ")
    
print ("\n\nтеперь числа до 1000 кратные 5:")

while number2 < 1000:
    
    if (number2 % 5 ) !=0:
        continue
    
    total2+=number2
    print(number2 , end=" ")
    number2 +=5
    print("\n", total2)
    

total3 = total1 + total2
print("\n\n", total3)
input("\nНажмите  enter ,чтобы выйти")


    



