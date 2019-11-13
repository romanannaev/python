# import hashlib
# file = open('c:/users/amigos/desktop/roma.txt', 'rb').read()
# h = hashlib.md5(file).hexdigest()
# print(h)
# import time
# b = "«Ма́ленький принц» — аллегорическая повесть-сказка, наиболее известное произведение \
#                 Антуана де Сент-Экзюпери.Впервые опубликована 6 апреля 1943 года в Нью-Йорке. Рисунки \
#                 в книге выполнены самим автором и не менее знамениты,чем сама книга.".split(" ")

# for i in b:
#     print(i)
#     time.sleep(3)
# m_dict = {'a': 3, 'b': 4, 'c':5, 'd':6, 'e':7}
# item = m_dict.popitem()
# print(item)
# print(m_dict)
c = []
n = 11
x = list()
for i in range(1, n):
    for b in range (i):
        
        x.append(b)
    c.append(x)
print(c)
