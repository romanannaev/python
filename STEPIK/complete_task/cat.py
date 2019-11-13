# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так

# import sys

# for line in sys.stdin:
#     line = line.rstrip()
#     # process line

# Sample Input:

# catcat
# cat and cat
# catac
# cat
# ccaatt
# Sample Output:

# catcat
# cat and cat


import sys
import re
pattern = r'cat.*cat'
for line in sys.stdin:
    line = line.rstrip()
    search_object = re.search(pattern, line)
    if search_object is not None:
        print(line)
# pattern = r"(cat.*){2,}"