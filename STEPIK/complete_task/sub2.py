# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
# Sample Input:

# this is a text
# "this' !is. ?n1ce,
# Sample Output:

# htis si a etxt
# "htis' !si. ?1nce,

import sys
import re
pattern = r'(\b\w)(\w)'
for line in sys.stdin:
    line = line.rstrip()
    sub_object = re.sub(pattern, r'\2\1', line)
    if sub_object is not None:
        print(sub_object)

# line = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
# pat = re.compile(r'''\b               # Start of the word
#                     (?P<first>\w)     # First letter
#                     (?P<second>\w)    # Second letter
#                     ''', 
#                  re.X)

# for line in sys.stdin:
#     newline = re.sub(pat, r'\g<second>\g<first>', line)
#     print(newline.strip())