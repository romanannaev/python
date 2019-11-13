class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count

    def say_gaw(self):
        
        if self.angry:
            print('GAW-' * self.count)
        else:
            print('gaw-' * self.count)
    #def ping(self):
    #    self.angry = True
    
    #def feed(self, food_count):
     #   if food_count > 10:
      #      self.angry = False
my_dog = Dog(True, 4)
Dog.say_gaw(my_dog)