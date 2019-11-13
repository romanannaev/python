# my_file = open ('input_file.txt', mode='r', encoding='utf-8')
# for line in my_file:
#     print('hi python -', line.strip())

# my_file.close()
out_file = "d.txt"
my_file = open(out_file, mode='w', encoding='utf-8')
password = 'hello'
x = open('input_file.txt', mode='r', encoding='utf-8')
for num, line in enumerate(x, 1):
    if password in line:
        print('id№', str(num), line.strip())
        my_file.write("password: " + str(num) + line.strip() + '\n')
x.close()
my_file.close()