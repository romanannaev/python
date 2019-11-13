
try:
    n = int(input())
    if 1 <= n <= 100:
        lst = []
        while len(lst) != n:
            x = int(input())
            lst.append(x)
        print(sum(lst))
except:
    None

# print(sum([int(input()) for i in range(int(input()))]))