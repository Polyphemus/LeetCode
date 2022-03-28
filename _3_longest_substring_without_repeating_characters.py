# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return (0)

        temp = []
        output = 1

        for i in range(len(s)):
            # if output > len(s) - i:  # if longest substring is > remaining # of chars, return output because it won't be exceeded. STILL NEED THIS
            if s[i] in temp:
                del temp[:temp.index(s[i]) + 1]
                temp.append(s[i])

            else:
                temp.append(s[i])
                if len(temp) > output:
                    output = len(temp)

        return (output)