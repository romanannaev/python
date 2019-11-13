# with open('dataset_3363_2 (1).txt', 'r') as f, open ('data.txt', 'w') as d:
#     line = f.readline().strip()
#     new_line = []
#     i = 0
#     for l in line:
#         if l.isalpha():
#             new_line.append(l)
#             i += 1
#             continue
#         elif l != line[-1] and line[i].isdigit() and line[i+1].isdigit():
#             new_line.append(line[i-1]*(int(l + line[i+1]) - 1))
#         else:
#             if l.isdigit() and line[i-1].isalpha():
#                 new_line.append(line[i-1]*(int(l)-1))
#         i += 1

#     d.write(''.join(new_line))


# with open('dataset_3363_2.txt', 'r') as f:
#     s = f.readline().strip()
#     i = 0
#     while i < len(s):
#         j = i + 1
#         while j < len(s) and s[j].isdigit():
#             j += 1
#         print(s[i] * int(s[i+1:j]), end='')
#         i = j

s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')
