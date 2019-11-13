dictionary = {'1' : 1, '2': 2, '3':3 , '4' : 4, '5 ' : 1000, '6' : 1200, '7' : 7, '8' : 9 }
# lst = []
# while len(lst) < 4:
#     max_num = 0
#     max_dict = {}
#     for _ in dictionary:
#         if dictionary[_] >= max_num:
#             max_num = dictionary[_]
#             lst[_] = max_num
            


# for value in sorted(dictionary.values())[-3:]:
#     for key in dictionary:
#         if dictionary[key] == value:
#             print(key)


# result = sorted(dictionary, key=dictionary.get, reverse=True)
# print(result)
# print(result[:3])

# from heapq import nlargest
# result = nlargest(3, dictionary, key=dictionary.get)
# print(result)

st = input().lower().split()
d = {}
for s in st:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
for key in d:
    print(key, d[key])

