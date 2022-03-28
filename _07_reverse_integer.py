# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        answer = ""
        if x >= 0:
            string = str(x)
            for i in range(len(string) - 1, -1, -1):
                answer += string[i]
            a = int(answer)
            if a > 2147483647:
                return (0)
            return (a)

        else:
            string = str(x * -1)
            for i in range(len(string) - 1, -1, -1):
                answer += string[i]
            a = int(answer) * -1
            if a < -2147483648:
                return (0)
            else:
                return (a)
