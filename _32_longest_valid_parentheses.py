# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n in (0,1):
            return 0
            
        l, r = 0, 0
        ss_len = 0
        ans = 0
        oc = Counter({'(': 0, ')': 0})
        
        # right pointer traverses while string is good, updates oc with counts, updates ss_len when opens == closes
        while r < n:            
            while r < n and s[r] != '(':
                r += 1
            l = r
                
            while oc['('] >= oc[')'] and r < n:
                oc[s[r]] += 1
                if oc['('] == oc[')']:
                    ss_len = r - l + 1
                r += 1

            ans = ss_len if ss_len > ans else ans
            
            if r < n:
                # reset counters for next potential ss
                oc['('] = 0
                oc[')'] = 0

        ss_len = 0
        oc['('] = 0
        oc[')'] = 0
        l, r = n - 1, n - 1

        while l > 0:
            while l > 0 and s[l] != ')':
                l -= 1
            r = l
            
            while oc['('] <= oc[')'] and l > 0:
                oc[s[l]] += 1
                if oc['('] == oc[')']:
                    ss_len = r - l + 1
                l -= 1
            
            ans = ss_len if ss_len > ans else ans
                
            if l > 0:
                # reached end of good string, store ss_len - 1 if greater, reset counters, move l, r to next (     
                ss_len = 0
                oc['('] = 0
                oc[')'] = 0
            
        return ans
