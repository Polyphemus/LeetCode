# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# No idea what string.digits is, nor how it was accepted as correct. TODO this one again

import re

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if str == '':
            return (0)

        # if there are no number chars in str: return 0. use regex
        regex = re.compile('\d')
        if regex.search(str) == None:
            print('regex no works')
            return (0)

        sign = 1

        temp = []

        for i in range(len(str)):
            if str[i] == ' ':
                continue

            elif str[i] == '+':
                i += 1
                if str[i] not in string.digits:
                    return (0)
                while i < len(str) and str[i] in string.digits:
                    temp.append(str[i])
                    i += 1
                break

            elif str[i] == '-':
                sign = -1
                i += 1
                if str[i] not in string.digits:
                    return (0)
                while i < len(str) and str[i] in string.digits:
                    temp.append(str[i])
                    i += 1
                break

            elif str[i] in string.digits:
                while i < len(str) and str[i] in string.digits:
                    temp.append(str[i])
                    i += 1
                break

            elif str[i] not in string.digits:
                return (0)

            else:
                return (0)

        ans = int(''.join(temp)) * sign

        if ans >= 2147483648:
            return (2147483647)

        elif ans < -2147483648:
            return (-2147483648)

        else:
            return (ans)