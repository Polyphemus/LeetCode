# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    # struggled to write an algo that only creates valid combos with a recursive function
    # below algo creates all permutations then tests them
    parens = '()'
    
    def parenBuilder(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['()', ')(', '))']
        ans = []
        for i in range(2):
            for j in range(2):
                ans += [self.parens[i] + self.parens[j] + k for k in self.parenBuilder(n-1)]
        #possibly make this set(ans), compare times
        return ans
        
        
    def generateParenthesis(self, n: int) -> List[str]:     
        # this can be avoided by having parenBuilder return [''] for n == 0 but it tested much slower
        if n == 1:
            return['()']
        answer = []
        # call parenBuilder to create all combos for n-1. Test and append to answer inside parens if valid
        for combo in self.parenBuilder(n-1): 
            if combo.count('(') == combo.count(')'):
                l = 1
                r = 0
                for char in combo:  # if right parens exceed left, combo is not valid
                    if char == '(':
                        l += 1
                    else:
                        r += 1                        
                    if r > l:
                        break
                else:  # no invalid combos, append inside
                    answer.append('(' + combo + ')')
        return answer
