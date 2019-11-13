class Employeer:
    count = 0
    raise_amount = 1
    def __init__(self, name, profession=None, pay=0):
        self.name = name
        self.profession = profession
        self.pay = pay
        Employeer.count += 1
    
    def add_preme(self,raise_amount):
        self.pay = int(self.pay*raise_amount)

    @classmethod
    def raise_add_amount(cls, amount):
        cls.raise_amount = amount
    
    @staticmethod
    def amount_instance_class():
        print('Created instances of class Employeer: ', Employeer.count)
    

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.profession, self.pay)

class Manager(Employeer):
    def __init__(self, name):
        super(Manager, self).__init__(name, 'manager', pay = 1500)
        
    

class Engeneer(Employeer):
    def __init__(self, name):
        Employeer.__init__(self, name, 'engeneer', 2000)



alex = Manager("Alex Annaev" )
print(alex)
Manager.raise_add_amount(1.1)
print(Employeer.raise_amount)
print()
print(Manager.raise_amount)
alex.add_preme(Manager.raise_amount)
print(alex)









