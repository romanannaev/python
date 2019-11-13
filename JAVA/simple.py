
try:
    num = float(input("enter number : "))
    
except ValueError as e:
    print ("it is not number!interpretator sort of says us:")
    print (e)
else :
    print("you entered number ", num)