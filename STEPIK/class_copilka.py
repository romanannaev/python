class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = 0
        

    def can_add(self, v):
        if  self.value + v < self.capacity:
            return True
        else:
            return False
            
        

    def add(self, v):
        if self.can_add(v):
            self.value += v
            self.capacity -= self.value
            return self.capacity
        else:
            return False

# class MoneyBox:
#     def __init__(self, capacity):
#         self.count_coin = 0
#         self.capacity = capacity

#     def can_add(self, v):
#         return self.count_coin + v <= self.capacity

#     def add(self, v):
#         if self.can_add(v):
#             self.count_coin += v
            

x = MoneyBox(5)
print(x.capacity)
x.add(5)
print(x.capacity)

print(x.add(4))
print(x.capacity)

