class Person:
    pass



class Man(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def drink(self):
        print('drink beer')
    
class Girl(Man):
    def klevat_brain(self):
        print('where is money?')

gena = Man("Gena", 40)
print (gena.name, 'is', gena.age)
gena.drink()

zina = Girl("zina", 31)
print(zina.name, zina.age)
zina.klevat_brain()


class Chaild(Girl, Man):
    pass

egor = Chaild('Egor', 21)

print(egor.name, egor.age)







