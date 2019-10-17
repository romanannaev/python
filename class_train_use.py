# class A:
#     pass


# a = A()

# a.__class__.name = 'Sergey'
# print(a.name)

# class MyObject:
#     par_atr = 0

#     def __init__(self):
#         self.data_attribute = 42
#         MyObject.par_atr += 1
#     def instance_method(self):
#         return self.data_attribute

#     @staticmethod
#     def static_method(self):
#         return self.par_atr


# print(MyObject.par_atr)
# a = MyObject()
# print(a.data_attribute)
# print(a.instance_method())
# print(MyObject.static_method(a))
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def __repr__(self):
            return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)
    # '''для представления для пользователя'''
    # def __str__(self):
    #    return"Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __repr__(self):
        return "Hello.. greeting!! I'm {}, it's my radius - {}".format(self.__class__.__name__, self.radius)
    @staticmethod
    def from_rectangle_cyrcle(rectangle):
        radius = (rectangle.side_a * 2 + rectangle.side_b * 2) ** 0.5 / 2
        return Circle(radius)
    # @classmethod
    # def from_rectangle_cyrcle(cls, rectangle):
    #     radius=(rectangle.side_a * 2 + rectangle.side_b * 2) ** 0.5 / 2
    #     return cls(radius)
class Cylinder(Circle):
    thick=''
    def __init__(self, radius, thick):
        super(Cylinder, self).__init__(radius) # Circle.__init__(self, radius)
        self.thick = thick
    @classmethod
    def from_rectangle_cylinder(cls, rectangle):
        radius=(rectangle.side_a * 2 + rectangle.side_b * 2) ** 0.5 / 2
        thick = 4
        return cls(radius, thick)

    def __repr__(self):
        return super().__repr__() + ', {}\'s thick is  {}'.format(self.__class__.__name__, self.thick)
def main():
    rectangle=Rectangle(3, 4)
    print(rectangle)
    second_circle = Circle.from_rectangle_cyrcle(rectangle)
    print(second_circle)
    c1 = Cylinder(3, 4)
    c2 = Cylinder.from_rectangle_cylinder(rectangle)
    print(c1)
    print(c2)

if __name__ == "__main__":
    main()
# # if __name__ =="__main__":
# #     rectangle = Rectangle(3, 4)
# #     print(rectangle)
# #
# #     first_circle = Circle(1)
# #     print(first_circle)
# #
# #     second_circle = Circle.from_rectangle(rectangle)
# #     print(second_circle)