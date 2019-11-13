# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".
# Sample Input:

# \w denotes word character
# No slashes here
# Sample Output:

# \w denotes word character
import sys
import re
pattern = r'\\'
for line in sys.stdin:
    line = line.rstrip()
    search_object = re.search(pattern, line)
    if search_object is not None:
        print(line)

# [print(line.rstrip()) for line in sys.stdin if re.search(r'(.)*\\(.)*', line) is not None]