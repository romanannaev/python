# dictionary  = {'andrey':27, 'alex':57, 'eugen':47, 'anfisa':37, 'nik':17,}
# dictionary2 = {}
# age = 20
# for i in range(16):
#     dictionary2["name" + str(i)] = age + i
# # print(dictionary2)

# dictionary = dict(minsk=1000, gomel= 500, gomel= 600)
# # print(dictionary)

# a = [['minsk', 1000], ['gomel', 500]]
# f = dict(a)
# # print(f)
# b = dict.fromkeys(['d', 'h', 'g', 't'], 100)
# # print(b)
# # print(dictionary['minsk'])
# dictionary['ecaterina'] = 'second'
# del dictionary['minsk']
# dictionary.setdefault('luda')
# print(dictionary)
# # print(dictionary.pop('luda'))
# print(dictionary.keys())
# print(dictionary.items())
# print(dictionary.pop()


# count_alpha = {}
# st = input('enter string :')
# for i in st:
#     if i in count_alpha:# if i.isalpha():
#         count_alpha[i] += 1  #d[i] = d.get(i, 0) + 1
#     else:
#         count_alpha[i] = 1
# print(count_alpha)
# for i in sorted(count_alpha):
#     print(i, count_alpha[i])
words = {}
while True:
    s = input('enter string:')
    if s in words:
        print('Word', s, 'translated like: ', words[s])
    else:
        print('Enter translated word', s)
        words[s] = input('enter:')

# def flatten(lst):
#     return [y for x in lst for y in x]
# Пример:
# lst = [[1, 2, 3], [4, 5, 6]]
# print(flatten(lst))
# [1, 2, 3, 4, 5, 6]
