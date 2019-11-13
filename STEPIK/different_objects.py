from random import randrange

def return_different_objects(objects):
    
    ans = 0
    new_list = []
    for obj in objects:
        for i in objects:
            if obj is i and obj not in new_list:
                new_list.append(obj)
                ans += 1      

return_different_objects([randrange(x) for x in range(1, 100)])

# ans = []
# for obj in objects:
#     if obj not in ans:
#         ans.append(obj)

# print(len(ans))

# n = len(objects)
# ans = n
# for i in range(n):
#     for j in range(i):
#         if id(objects[i]) == id(objects[j]):
#             ans -= 1
#             break

# print(ans)


# print(len(set(map(id, objects))))

# print(len(set(id(i) for i in objects)))