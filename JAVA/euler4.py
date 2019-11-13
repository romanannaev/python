#находим число полиндром из последовательности чисел до 999*999
def euler4():
    for i in range(998001, 10000,-1):
        b = str(i)
        if b == b[::-1] :
            for i in range(999, 101, -1):
                c = int(b)/i
                if c == int(c) and len(str(c)) == 5 :                 
                    return b, c, int(b)/c
print(euler4())
             

              

            
            
         


    


    
    


