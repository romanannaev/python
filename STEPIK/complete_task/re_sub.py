# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# Sample Input:

# attraction
# buzzzz
# Sample Output:

# atraction
# buz

#(\w{1})\1'

import sys
import re
pattern = r'(\w)\1+'     

for line in sys.stdin:
    line = line.rstrip()
    sub_object = re.sub(pattern, r'\1', line)
    print(sub_object)
    
# line = re.sub(r"(\w)\1+", r"\1", line)
