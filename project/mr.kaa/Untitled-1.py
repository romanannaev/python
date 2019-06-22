from collections import Counter
import random
x = []

for i  in range (1, 50):
    x.append(random.randrange(50))
x.sort()

counter = Counter(x)

print(x)
print (counter)
    
