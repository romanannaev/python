# class A:
#     pass


# a = A()

# a.__class__.name = 'Sergey'
# print(a.name)

# class MyObject:
#     par_atr = 0

#     def __init__(self):
#         self.data_attribute = 42
#         par_atr += 1
#     def instance_method(self):
#         return self.data_attribute

#     @staticmethod
#     def static_method():
#         return par_atr
        
    

# a = MyObject()
# print(a.data_attribute)
# print(a.instance_method())
# print(MyObject.par_atr)
# print(MyObject.par_atr)

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    # def __repr__(self):
    #         return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)

    # '''для представления для пользователя'''
    # def __str__(self):
    #    return"Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # def __repr__(self):
    #     return "Circle(%.1f)" % self.radius

    @staticmethod
    def from_rectangle(rectangle):
        radius = (rectangle.side_a * 2 + rectangle.side_b * 2) ** 0.5 / 2
        return Circle(radius)

    # @classmethod
    # def from_rectangle(cls, rectangle):
    #     radius = (rectangle.side_a * 2 + rectangle.side_b * 2) ** 0.5 / 2
    #     return cls(radius)

class Cylinder(Circle):

    pass
    # def __init__(self, radius, thick):
    #     self.radius = radius
    #     self.thick = thick
        

def main():
    rectangle = Rectangle(3, 4)
    

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)
    
    c1 = Cylinder(10)
    c2 = Cylinder.from_rectangle(rectangle)
    
    print(c2)

if __name__ == "__main__":
    main()


# if __name__ =="__main__":
#     rectangle = Rectangle(3, 4)
#     print(rectangle)
#
#     first_circle = Circle(1)
#     print(first_circle)
#
#     second_circle = Circle.from_rectangle(rectangle)
#     print(second_circle)


