# namesp = {
#     'global': {
#         'parent': None,
#         'vars': set('a'),
#         'foo': {
#             'parent': 'global',
#             'vars': set('b'),
#             'bar': {
#                 'parent': 'foo', 
#                 'vars': set('a')}
#         }
#     }
# }

# Sample Input:

# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b
# Sample Output:

# global
# None
# bar
# foo
# dict_1 = {'global' : None, 'Пространство': 'Родитель'}
# dict_2 = {'Пространство': 'Множество переменных'}

scopes = {'global': {'parent': None, 'variables': set()}}

def get(namespace, var):
    if var in scopes[namespace]['variables']:
        return namespace
    else:
        namespace = scopes[namespace]['parent']
        if namespace == None:
            return None
        else:    
            get(namespace, var)


def add(namespace, var):
    scopes[namespace]['variables'].add(var)


def create(namespace, parent):

    scopes[namespace] = {'parent': parent, 'variables' : set()}

amount = int(input())
for _ in range(amount):

    cmd, namesp, arg = input().split()

    if cmd == 'create':
        create(namesp, arg)

    elif cmd == 'add':
        add(namesp, arg)

    elif cmd == 'get':
        get(namesp, arg)


# n = int(input())

# parent = {"global": None}
# vs = {"global": set()}

# for _ in range(n):
#     t, fst, snd = input().split()
#     if t == "create":
#         parent[fst] = snd
#         vs[fst] = set()
#     elif t == "add":
#         vs[fst].add(snd)
#     else:  # t == get
#         while fst is not None:
#             if snd in vs[fst]:
#                 break
#             fst = parent[fst]
#         print(fst)