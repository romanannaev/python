        
class Woman:
    def my_female(self):
        print("i'm woman!")


class Negr:
    def my_rassa(self):
        print('i\'m negr!')

class Man:
    def my_female(self):
        print("i'm man!")


class Person(Woman, Negr):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "HI, i'm {} ".format(self.name)

        
    

andrey = Person("ANdrey")
print(andrey)
andrey.my_rassa()
andrey.my_female()
print(vasy.name)



    