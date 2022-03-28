# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == "":
            return ("")

        ans = s[0]

        for j in range(1, len(s)):
            if s[j - 1] == s[j]:
                i = j - 1
                k = j
                while i >= 0 and k < len(s):
                    if s[i] == s[k]:
                        if (k - i + 1) > len(ans):  # aabc 1 - 0 + 1 == len(aa)
                            ans = s[i:k + 1]
                        i -= 1
                        k += 1
                    else:
                        break

            if j == len(s) - 1:
                return (ans)

            if s[j - 1] == s[j + 1]:
                i = k = j
                while i >= 0 and k < len(s):
                    if s[i] == s[k]:

                        if (k - i + 1) > len(ans):  # babad 1 - 3 + 1 == len(babad)
                            ans = s[i:k + 1]

                        i -= 1
                        k += 1
                    else:
                        break

        return (ans)