class Person:
    def __init__(self, name, age)
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, 'is', self.age)
    
alex = Person("Alex", 36)
ira = Person("Ira", 21)



Person.print_info(alex)
Person.print_info(ira)

""" метод обертка"""
alex.print_info()
ira.print_info()

print(Person.print_info)
# связанный метод, здесь alex.print_info() просто вызывает Person.print_info(alex)
print(alex.print_info)



