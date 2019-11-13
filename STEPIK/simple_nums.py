import itertools
import math
# def primes():
#     a = 2
#     b = a - 1
#     while b > 1:
#         if a % b == 0:
#             if a == 2:
#                 yield a
#             break
#         elif b == 2:
#             yield a
#         else:
#             b -= 1
#     a += 1
#     primes()
    
# for i in primes():
#     print(i)
# # Натуральное p>1 является простым тогда и только тогда, когда (p-1)!+1 делится на p

# isSimple = True
# d = n - 1
# while d > 1:
#     if n % d == 0:
#         isSimple = False
#         break
#     d -= 1
        
def primes():
    a = 2 
    while a != 30:
        if (math.factorial(a-1) + 1) % a == 0:
            yield a
        a += 1

gen = primes()
for i in gen:
    print(i)

# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
def primes():
    i = 2
    while True:
        is_prime = True
        divisor = 2
        while divisor ** 2 <= i:
            if i % divisor == 0:
                is_prime = False # non-trivial divisor
                break

            divisor += 1

        if is_prime:
            yield i

        i += 1

def primes():
    x = 2
    while True:
        res = [x % i == 0 for i in range(2, x)]
        if not any(res):
            yield x
        x += 1

def primes():
    current = 2
    while True:
        if not [x for x in range(2, current) if current % x == 0]:
            yield current
        current += 1