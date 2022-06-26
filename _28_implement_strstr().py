# Implement strStr().
# 
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    
                    if needle[j] != haystack[i+j]:
                        break
                else:
                    return i
        else:
            return -1
