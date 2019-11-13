# найти сумму натуральных чисел кратных 3 или 5 до 1000
total1=0
total2=0

print ("\n\n\tВот числа до 1000 кратные трем:\n\n")
for guess in range(0 ,1000 , 3):
    print( guess , end=" ")
    guess=int(guess)
    total1 +=guess
print("\n\n\tПеречислим теперь числа до 1000 кратные пяти:\n\n")
for number in range(0 ,1000 , 5):
    print (number , end=" ")
    number=int(number)
    total2 +=number



print (" \n\nА вот и сумма всех числе до 1000 кратных пяти или трем! :",
       total1+total2)


input("\n\n\t Нажмите enter , чтобы выйти!")
