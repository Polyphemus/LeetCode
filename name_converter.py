# Converts LeetCode Problem names, creates python files, writes description and code

import re, sys

leetName = input('Enter problem name:\n').lower()
newNameList = ['_']
mo = re.match(r'(\d*).(.*)', leetName)
newNameList.append(mo.group(1))
for char in mo.group(2):
    if char == ' ':
        newNameList.append('_')
    else:
        newNameList.append(char)
newNameList.append('.py')

leetIntroLines = []
print("Enter problem description, hit enter. Type q then hit enter when done ")
while True:
    line = sys.stdin.readline()
    if line == 'q\n':
        break
    else:
        leetIntroLines.append(line)
leetIntro = '# ' + '# '.join(leetIntroLines)
print(leetIntro)

leetCodeLines = []
print("Enter solution code, hit enter. Type q then hit enter when done ")
while True:
    line = sys.stdin.readline()
    if line == 'q\n':
        break
    else:
        leetCodeLines.append(line)

leetCode = '\n' + ''.join(leetCodeLines)

leetFile = open(''.join(newNameList), 'a')
leetFile.write(leetIntro)
leetFile.write(leetCode)
leetFile.close()