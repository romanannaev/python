import random
def look_meh(look_meh):
    return random.choice(look_meh)


spider = ["1 gold", "копыта", "ноги"]
adger = ["10 gold", "mech", "shlem"]
look = [spider, adger, adger]
pocket = []

for i in look:


    pocket.append(look_meh(i))
print (pocket)