# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ 
# и выведите полученные строки.

# Sample Input:

# I need to understand the human mind
# humanity
# Sample Output:

# I need to understand the computer mind
# computerity
import sys
import re
pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    sub_object = re.sub(pattern, 'computer', line)
    
    print(sub_object)