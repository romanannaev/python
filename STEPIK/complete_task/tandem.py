# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

# Sample Input:

# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:

# blabla is a tandem repetition
# 123123 is good too
import sys
import re
pattern = r'\b(\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    
    
    search_object = re.search(pattern, line)
    if search_object is not None :
    
        print(line)

# re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# r"(\b.*\B)\1\b"
# r"\b(.+\B)\1\b"
# r"\b(\w.*)\1\b"