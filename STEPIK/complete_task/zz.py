# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
# Sample Input:

# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz
# Sample Output:

# zabcz
# zzxzz
import sys
import re
pattern = r'z...z'
for line in sys.stdin:
    line = line.rstrip()
    search_object = re.search(pattern, line)
    if search_object is not None:
        print(line)

    # if re.search(r'z.{3}z', line):
    #     print(line)
    # [print(line.rstrip()) for line in sys.stdin if re.search(r'z\w{3}z', line)]