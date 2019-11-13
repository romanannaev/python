class MyObject:
    int_field = 0
    str_field = "8"


    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
    def __str__(self):
        return '{}, {}'.format(self.name, self.lastname)

print(MyObject.int_field)
object1 = MyObject('roma', 'annaev')
object2 = MyObject('вася', 'петушков')

MyObject.int_field = 10
print(MyObject.int_field)
object1.str_field = 'ksjdhf'
print(object1.str_field)
print(object1)

# class Person:
#     def print_info(self):
#         print(self.name, "is", self.age)



# alex = Person()
# alex.name = 'Alex'
# alex.age = 36

# ira = Person()
# ira.name = 'Alex'
# ira.age = 36

# Person.print_info(alex)
# Person.print_info(ira)

# """ метод обертка"""
# alex.print_info()
# ira.print_info()

# print(Person.print_info)
# # связанный метод, здесь alex.print_info() просто вызывает Person.print_info(alex)
# print(alex.print_info)















