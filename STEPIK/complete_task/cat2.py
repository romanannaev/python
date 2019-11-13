import sys
import re
pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    search_object = re.search(pattern, line)
    if search_object is not None:
        print(line)
# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

# Примечание:
# Для работы со словами используйте группы символов \b и \B.
# Описание этих групп вы можете найти в документации.
# Sample Input:

# cat
# catapult and cat
# catcat
# concat
# Cat
# "cat"
# !cat?
# Sample Output:

# cat
# catapult and cat
# "cat"
# !cat?