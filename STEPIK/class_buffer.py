class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.lst = []

    def add(self, *a):
        
        self.lst.extend(a)
        while len(self.lst) >= 5:
            print(sum(self.lst[:5]))
            for i in range(5):
                self.lst.pop(0)
            
                

        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.lst
        # вернуть сохраненные в текущий момент элементы последовательности в порядке,
        # в котором они были добавлены


buf = Buffer()
buf.add(1, 2, 4, 5, 5)
print(buf.get_current_part())
buf.add(1,2)
print(buf.get_current_part())
buf.add(12, 3, 4, 5)
print(buf.get_current_part())
buf.add(12, 3, 4, 5)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part())
# class Buffer:
#     def __init__(self):
#         self.part = []

#     def add(self, *a):
#         for i in a:
#             self.part.append(i)
#             if len(self.part) == 5:
#                 print(sum(self.part))
#                 self.part.clear()

#     def get_current_part(self):
#         return self.part