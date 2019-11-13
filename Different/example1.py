from datetime import datetime

for i in range (6 ):
    if i == 6:
        print(i) 
        break
else:
    print('the end')


flag = False
for i in range(6):
    if i == 6:
        print(i)
        flag = True
        break
if flag:
    print(str(i) +' was found')
