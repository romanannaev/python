#просто зверюшка 
#демонстрирует простейший класс и объект
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "Имя: " + self.name + "\n"
        return rep
    def talk(self):
        print("Привет ,меня зовут ", self.name ,"\n")
#основная часть
crit1 = Critter('Бобрик')
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вывод  crit1 на экра:")
print(crit1)
print("Непосредственный доступ к атрубуту crit1.name:")
print(crit1.name)
input("\n\nНажмите Enter, чтобы выйти.")