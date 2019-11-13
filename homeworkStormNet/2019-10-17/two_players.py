class Player:
    def __init__(self, name, damage, health, brain):
        self.name = name
        self.damage = damage
        self.health = health
        self.brain = brain

    def __sub__(self, damage):
        self.health -= damage
    
    def __add__(self, bonus):
        self.health += bonus

    def __repr__(self):
        return 'I\'m {}, class - {} , my HEALTH = {},'.format(self.name, self.__class__.__name__, self.health)


class Ork(Player):
    def __init__(self, name, damage=5, health=60, brain=0 ):
        super().__init__(name, damage, health, brain)
        

class Warrior(Player):
    def __init__(self, name, damage=4, health=40, brain=1):
        super().__init__(name, damage, health, brain)

nec = Ork('Necromon')
az = Warrior('Azgard')
i = 1
from random import choice
all_list = [nec, az]
while az.health and nec.health:
    first = choice(all_list)
    if first == az:
        nec.health -= az.damage
        print(nec.name, 'got damage! Health - ', end=' ')
        print(nec.health, '\n')
    else:
        az.health -= nec.damage
        print(az.name, 'got damage! Health - ', end=' ')
        print(az.health, '\n')
        if i == 3:
            print('i\'m', az.name, 'got from', nec.name, 'three times in a row in my health', '- Turn on brain!\n')
            bonus = 10
            az.health += bonus
            print('I used my bonus! My health: ', az.health, '\n' )
            i = 0
        else:
            i += 1

if az.health :
    print(az, 'I\'M WIN')
else:
    print(nec, 'I\'M WIN')





