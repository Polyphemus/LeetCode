# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return("")
        if len(strs) == 1:
            return(strs[0])
        strs.sort(key=len)

        ans = ""

        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return(ans)
                elif strs[j][i] == strs[j+1][i]:
                    if j == len(strs)-2:
                        ans+= strs[j][i]
        return(ans)