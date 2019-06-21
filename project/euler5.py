def euler5():
    #используем вложенный цикл for используя доп условие
    c = []
    
    for i in range(2521,1000000):
        b = i
        x = 1
        while x <= 20:
            a = b/x 
            if a == int(a):
                c.append(a)
                if len(c) == 20:
                    return b,c
            else:
                del c[:]
                break
            x +=1
print (euler5())