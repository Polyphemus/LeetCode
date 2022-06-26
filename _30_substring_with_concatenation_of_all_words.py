# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# 
# You can return the answer in any order.

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(words[0])
        wordsDict = Counter(words) # not actually a dictionary but a Counter

        # find matches, add to index:word. O(s)
        mtchDct = {}
        for j in range(len(s) - n + 1):
            if s[j:j + n] in wordsDict:
                mtchDct[j] = s[j:j + n]
            
        # precheck for all words, maybe faster?:
        if any(word not in mtchDct.values() for word in words):
            return[]            

        # iterate through match dictionary, see if adjacent matches exist, are complete
        for k, v in mtchDct.items():
            currentN = [] 
            for i in range(k, k + n*len(words), n): # change to a list comp or gen?
                if i in mtchDct:
                    currentN.append(mtchDct[i])
                else:
                    break
            else:
                if Counter(currentN) == wordsDict:
                    ans.append(k)
                            
        return ans
