
#симулятор пирожок с сюрпризом
#демонстирурет работу условий if , elif ,else 

print("\t\t hi my friend!\n")
print("вот тебе пирожок ,по умолчанию ты его скушал ,а в нем .....\
:)")

import random

number = random.randint(1,5)

if number == 1 :
    print("\n ты скушал маленький кусочек человеческой какахи,это зашквар :)))")

elif number == 2 :
    print("\n ты употреб ворс,который был тщательно отобран в трусах бомжика:)")

elif number == 3 :
    print("\n ты сЪел алмаз,это джекпот!")

elif number == 4 :
    print("\n ты покушал червячка,навозного ,это неудача((")

else :
    print("\n тебе выпало число 5 ,ты красаава и съел норм пирожок" ,
"с капусткой!")

input ("\n\t введете enter и молодцом! ")        
    



