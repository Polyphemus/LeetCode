# Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        thousands = {'M': 1000, 'MM': 2000, 'MMM': 3000, 'MMMMM': 4000}
        hundreds = {'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900}
        tens = {'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90}
        ones = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
        total = 0
        i = 0

        temp = ''

        while s[i] == 'M':
            temp += s[i]
            if i == len(s)-1:
                break
            else:
                i += 1

        if temp in thousands:
            total += thousands[temp]

        temp = ''

        while s[i] == 'C' or s[i] == 'D' or s[i] == 'M':
            temp += s[i]
            if i == len(s)-1:
                break
            else:
                i += 1

        if temp in hundreds:
            total += hundreds[temp]

        temp = ''

        while s[i] == 'X' or s[i] == 'L' or s[i] == 'C':
            temp += s[i]
            if i == len(s)-1:
                break
            else:
                i += 1

        if temp in tens:
            total += tens[temp]

        temp = ''

        while s[i] == 'I' or s[i] == 'V' or s[i] == 'X':
            temp += s[i]
            if i == len(s)-1:
                break
            else:
                i += 1

        if temp in ones:
            total += ones[temp]

        return(total)