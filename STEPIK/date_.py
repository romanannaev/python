# import datetime

# # y, m, d = [int(i) for i in input().split()]
# (y, m, d) = map(int, input().split())
# x = datetime.date(y, m, d)
# y = datetime.timedelta(days = int(input()))

# c = x + y
# print(c.year, c.month, c.day)
# put your python code here
# import datetime
# inp = datetime.datetime.strptime(input(), "%Y %m %d")
# inp += datetime.timedelta(days=int(input())) 
# print(f'{inp.year} {inp.month} {inp.day}')

# import datetime

# y, m, d = map(int, input().split())
# days = int(input())

# current = datetime.date(year=y, month=m, day=d)
# current += datetime.timedelta(days=days)

# print("{} {} {}".format(current.year, current.month, current.day))
