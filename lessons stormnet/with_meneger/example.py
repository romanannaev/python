x = open('file.txt', mode='w', encoding='utf-8')
for i in range(10):
    x.write('Hello world\n')
x.close()

y = open('file.txt', mode='r', encoding='utf-8')
z = open('file1.txt', mode='w', encoding='utf-8')
for num, line in enumerate(y, 1):
    z.write(str(num) + ' - ' + line.strip() + '\n')   
y.close()
z.close()



