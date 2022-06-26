# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = 0
        
        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
                
            elif target < nums[m]:
                r = m
                
            else:
                return m
        else:
            print(f'-----\nl = {l}\nm = {m}\nr = {r}')
            if target > nums[l]:
                return l + 1
            else: 
                return l
