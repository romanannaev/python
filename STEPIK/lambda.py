# def f(x):
#   def f1(y):
#     return y+x
#   return f1

# a=f(5)
# print(a)
# print(a(2))

# В данной за

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
# def mod_checker(x, mod=0):
#     def check(y):
#         return y % x == mod
#     return check
# mod_checker = lambda x, mod=0: lambda y: y % x == mod