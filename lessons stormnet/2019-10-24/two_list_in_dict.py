# function returns dictionary out two lists
# def get_dictionary(lst_1, lst_2):
#     dictionary = {}
#     i = 0
#     for key in lst_1:
#         if i < len(lst_2):
#             dictionary[key] = lst_2[i]
#             i += 1
#         else:
#             dictionary[key] = None
#     return dictionary

# lst_1 = [str(i) for i in range(1, 11)]
# lst_2 = [i for i in range(1, 9)]

# print(get_dictionary(lst_1, lst_2))
x = {p: p*p for p in range(10)}

print(x)

y = {q: q*3 for q in range(5,15) if q%2!=0}

print(y)


