c = []
x = 2
b = []
while len(c) != 10001:
    for i in range(1,1000):
        y = x / i
        if y == int(y):
            b.append(i)
        elif len(b) == 3:
            del b[:]
            break
        elif i == 999 and len(b) == 2 :
            c.append(x)
        else:
            continue
    del b[:]
    x += 1
print(c[-1])
