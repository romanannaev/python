# lst = [1, 2, 3]
# def f():
#     lst.append(4)
#     lst[0] = 2
#     print('#1')

# def f():
#     lst.append(5)
#     lst[0] = 3
#     print('#2')
#     return lst

# def f():
#     lst.append(6)
#     lst[0] = 4
#     print(lst)
#     print('#3')

# print(lst)
# f()
# print(lst)
# def inc(num):
#     num += 1
#     try:
#         return num 
#     except:
#         pass
#     finally:
#         num += 1
#         print("I changed number after return - ", num)
    
# print(inc(5))

# cmd, namesp, arg = input().split()
# dict_all = {
#     namesp : [arg]
# }
# dict_create = { 
#     'name_children' : lst[1],
#     'parent' : lst[2]
# }

# add_dict = {
#     'parent' : lst[1],
#     'value' : lst[2]
# }

namesp = {
    'global': {
        'parent': None,
        'vars': set('a'),
        'foo': {
            'parent': 'global',
            'vars': set('b'),
            'bar': {
                'parent': 'foo', 
                'vars': set('a')
            }
        }
    }
}
def get(namespace, var):



def add(namespace,var):
    nmsp['vars'].add(var)


def create(namespace, parent):
    nmsp[namespace] = {'parent':parent, 'vars':set()}

n = 10
while n != 0:
    cmd, nmsp, var = input().split()
    if cmd == 'add':
        add(nmsp, var)
    elif cmd == 'create':
        create(nmsp, var)

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b





