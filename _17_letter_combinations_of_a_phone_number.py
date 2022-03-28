# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    numsDict = {'2' : ('a', 'b', 'c'),
                '3' : ('d', 'e', 'f'),
                '4' : ('g', 'h', 'i'),
                '5' : ('j', 'k', 'l'),
                '6' : ('m', 'n', 'o'),
                '7' : ('p', 'q', 'r', 's'),
                '8' : ('t', 'u', 'v'),
                '9' : ('w', 'x', 'y', 'z')}
    
    def digitAppender(self, nums):
            if len(nums) == 1:
                return list(self.numsDict[nums[0]])
            else: 
                currentLetters = []
                for letter in self.numsDict[nums[0]]:
                    for nextLetter in self.digitAppender(nums[1:]):
                        currentLetters.append(letter + nextLetter)
            return currentLetters
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.digitAppender(digits) 
