# Задача 1. Создайте класс с методом класса, в котором определялась бы сумма двух целых чисел.

# class Addition:
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def return_sum_a_b(cls, *args):
#         return sum(args)
# class B(Addition): pass

# print(Addition.return_sum_a_b(1,2,3,4))
# x = Addition(1)
# print(x.name)
# print(x.return_sum_a_b(1,2,3,4))
# y = B(2)
# print(y.name)
# print(y.return_sum_a_b(1,2,3,4))

# Задача 2. Создайте класс с методом-конструктором, в котором следует определить атрибуты экземпляра класса, 
# необходимые для сложения двух целых чисел. 
# Напишите метод, в котором бы определялась сумма двух целых чисел.

# class Sum:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def method_sum(self):
#         return self.a + self.b

# x = Sum(1, 2)
# print(x.method_sum())

# Задача 3. Создайте класс с методами, формирующими вложенную последовательность. 
# Пользователю должна быть предоставлена возможность заполнить ее либо случайными числами в интервале [-10; 10], 
# либо осуществить ввод данных с клавиатуры.
from random import randrange
class MethodAdd:
    @staticmethod
    def add_follow(*args):
        if len(args) == 0:
            lst = [randrange(-10, 10) for i in range(10)]
            return lst
        else:
            lst = args
            return lst
        


x = MethodAdd()
print(MethodAdd.add_follow())



