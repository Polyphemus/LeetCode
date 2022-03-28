# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''This solutions works for all except one very long test case. Not sure how to make this faster, maybe skip to first closer. Time for bed'''

        if s == "":
            return (True)

        openers = ['(', '{', '[']
        closers = [')', '}', ']']

        if s[0] not in openers:
            return (False)

        s_list = list(s)

        i = 0
        while i < len(s_list) - 1:
            if s_list[i] in openers and s_list[i + 1] in closers:
                if openers.index(s_list[i]) != closers.index(s_list[i + 1]):
                    return (False)
                else:
                    s_list.pop(i + 1)
                    s_list.pop(i)
                    if len(s_list) == 0:
                        return (True)
                    else:
                        i = 0

            else:
                i = i + 1

        return (False)