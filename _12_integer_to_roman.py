# Given an integer, convert it to a roman numeral.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # list of dictionaries
        pairs = [{0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'},
        {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'},
        {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'},
        {1:'M', 2:'MM', 3:'MMM', 4:'MMMM'}]

        ans = ''

        # convert integer input to list of dictionaryies, opmtimzed w/ map, original: digits = list(str(num))
        digits = list(map(int, str(num)))

        for i in range(len(digits) - 1, -1, -1):
            ans = pairs[len(digits) - 1 - i][int(digits[i])] + ans
        return(ans)