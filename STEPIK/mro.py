# class A:
#    def foo(self):
#       print("A")

# class B(A):
#    pass

# class C(A):
#    def foo(self):
#       print("C")

# class D:
#    def foo(self):
#       print("D")

# class E(B, C, D):
#    pass

# E().foo()
# class A:
#     pass

# class B(A):
#     pass

# class C:
#     pass

# class D(C):
#     pass

# class E(B, C, D):
#     pass

# print(E.mro())
class ExtendedStack(list):
    def sum(self):
        
        self.append(self.pop(-1) + self.pop(-1))
        # операция сложения

    def sub(self):
        
        self.append(self.pop(-1) - self.pop(-1))
        # операция вычитания

    def mul(self):
        
        self.append(self.pop(-1) * self.pop(-1))
        # операция вычитания
        # операция умножения

    def div(self):
        
        self.append(self.pop(-1) // self.pop(-1))
        # операция целочисленного деления

x = ExtendedStack([1, 2])
print(x)
x.mul()
print(x)
x.sum()
print(x)