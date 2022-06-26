# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0 
        r = n - 1
        m = 0 
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            
            elif target < nums[m]:
                r = m - 1
                
            else: 
                break
        else:
            return [-1, -1]
        
        s = m
        e = m
        t = m

        # target is at m, we need to find first non-m to the right and left
        # search right:
        
        l = t
        r = n - 1
        
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] == target:
                e = m
                l = m + 1
            else:
                r = m - 1
        
        m = (l + r) // 2

        if nums[m] == target:
            e = m

        # search left
        
        r = t
        l = 0
        
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                s = m
                r = m - 1
            
            else:
                l = m + 1

        m = (l + r) // 2
        if m >= 0 and nums[m] == target:
            s = m

        return [s, e]
