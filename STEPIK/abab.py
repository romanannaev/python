# def f(s, a, b):
#     i = 0
#     while i < 1001:
#         if a in s and a in b:
#             return print('Impossible')
#         elif a in s:
#             s = s.replace(a, b)
#             i += 1
#         else:
#             return print(i)
#     else:
#         return print('Impossible')
# s, a, b, i = [input() for i in range(3)] + [0]  
# while a in s:
#     if a in b: i = 'Impossible'; break
#     s, i = s.replace(a, b), i + 1
# print(i)

# s, a, b = (input() for _ in range(3))
# def repl_gen(s, a, b):
#     while a in s: s = s.replace(a, b); yield True
# print('Impossible' if a in b and a in s else sum(repl_gen(s, a, b)))






# s, t = [input() for i in range(2)]
# total = 0
# for i in s:
#     if s.startswith(t):
#         total += 1
# print(total)


# print(sum(1 for i in range(len(s)) if s.startswith(t, i)))


# import re
# s, t = input(), '(?=' + input() + ')'
# print(len(re.findall(t, s)))