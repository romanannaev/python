class Cat:
    def __init__(self, name, female):
        self.__name = name
        self.female = female
    def __get_mur(self):
        print('mur-mur-mur')


mursik = Cat('mursik', 'kot')
# print(mursik.__name)
print(mursik.female)
# mursik.__get_mur()
mursik._Cat__get_mur()

