class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.judge = judge
        self.funcs = funcs
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
                
    def count_res(self, a):
        res = [f(a) for f in self.funcs]
        return res.count(True), res.count(False)

        
        

    def __iter__(self):

        for i in self.iterable:
            pos, neg = self.count_res(i)
            if self.judge(pos, neg):
                yield i
    
        # возвращает итератор по результирующей последовательности

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))


# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg

#     def judge_any(pos, neg):
#         return pos > 0

#     def judge_all(pos, neg):
#         return neg == 0

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterator = iter(iterable)
#         self.funcs = funcs
#         self.judge = judge

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while (True):
#             elem = next(self.iterator)
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(elem):
#                     pos += 1
#                 else:
#                     neg += 1

#             if self.judge(pos, neg):
#                 return elem

# class multifilter:
#     judge_any = lambda pos, neg: pos > 0
#     judge_half = lambda pos, neg: pos >= neg
#     judge_all = lambda pos, neg: neg == 0

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge

#     def __iter__(self):
#         for elem in self.iterable:
#             pos = sum([fun(elem) for fun in self.funcs])
#             neg = len(self.funcs) - pos
#             if not self.judge(pos, neg):
#                 continue
#             yield elem