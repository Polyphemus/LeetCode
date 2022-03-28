# Converts LeetCode Problem names

import re

LeetName = '\
27. Remove Element\
'.lower()
newNameList = ['_']

nameReg = re.compile(r'\d*')

mo = nameReg.search(LeetName)

newNameList.append(mo.group())

for char in LeetName:
    if char == ' ':
        newNameList.append('_')
    elif char.isdigit():
        pass
    elif char == '.':
        pass
    else:
        newNameList.append(char)

print(''.join(newNameList))