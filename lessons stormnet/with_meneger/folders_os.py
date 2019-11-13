# create structure of project
# import os
# path = r'D:\project_os'
# project_name = 'project_1'
# folders = [
#     'HTML', 'CSS', 'JS', 'IMG',
#     ]
# # pathFull = path + '\\' + project_name
# # print(pathFull)
# pathFull = os.path.join(path, project_name)
# print(pathFull)

# if not os.path.exists(pathFull):
#     os.mkdir(pathFull)

# for i in folders:
#     folder = os.path.join(pathFull, i)
#     if not os.path.exists(folder):
#         os.mkdir(folder)


'''
the same code and includes folders
'''
import os
# path = 'D:\\project_os'
# for i in os.listdir(path):
#     print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i))
# def get_folders(path, level=1):
#     print('Level=', level, 'Content: ', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\' + i):
#             print('Come down', path + '\\' + i)
#             get_folders(path + '\\' + i, level + 1)
#             print('Returned', path)
# get_folders(path)

# for current_dir, dirs, files in os.walk(path):
#     print(current_dir, dirs, files)

# def create_folders(path):
#     if not os.path.exists(path):
#         os.mkdir(path)

path = r'd:\project_1'
# def buld_main_folder(path):
#     if not os.path.exists(path):
#         os.mkdir(path)

# def build
# folders = [

# ]

# def build(root, data):
#     if data:
#         for d in data:
#             name = d[0]
#             path = os.path.join(root, name)
#             create_folders(path)
#             build(path, d[1])


# path = r'D:\project_os'
# project_name = input('Enter your name project folder: ')
# if project_name:
#     pathFull = os.path.join(path, project_name)
#     if not os.path.exists(pathFull):
#         os.mkdir(pathFull)

# folders = \
#     [['HTML', [
#         ['href', []],
#         ['doc', []], ]
#       ],
#      ['CSS',  []],
#      ['JS',   []],
#      ['IMG',  [
#          ['foto', []],
#          ['page', [
#              ['svg', []],
#              ['png', []]
#          ]]
#      ]]
#      ]
# build(pathFull, folders)


# folders = \
#     [['HTML', [
#         ['href', []],
#         ['doc', []],]
#       ],
#      ['CSS',  [] ],
#      ['JS',   [] ],
#      ['IMG',  [
#          ['foto',[]],
#          ['page',[
#              ['svg',[]],
#              ['png',[]]
#          ]]
#      ] ]
#      ]


# def createFolder(path):
#     if not os.path.exists(path):
#         os.mkdir(path)


# def build(root, data):
#     if data:
#         for d in data:
#             name = d[0]
#             path = os.path.join(root, name)
#             createFolder(path)
#             build(path, d[1])


# nameproject = input('Введите имя проекта : ')
# if nameproject:
#     pathfull = os.path.join(path, nameproject)
#     createFolder(pathfull)
#     build(pathfull, folders)
# a = [1,2,3]
# i = 2
# for _ in a:
#     b = i + 1
#     print(b)
# c = b + 1
# print(c)
# print(i)

path = os.path.realpath('library_db.txt')
print(path)