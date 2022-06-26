# There is an integer array nums sorted in ascending order (with distinct values).
# 
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        l = 0
        r = n - 1     
        m = 0
        
        while l < r:
            m = (r + l) // 2
            
            # if m is greater than right, search right
            if nums[m] > nums[r]:
                l = m + 1
                    
            # if m is less than left, search left
            elif nums[m] < nums[l]:
                r = m
            
            else:
                l -= 1
                
        l = (r + l) // 2
        m = 0
        r = l + n - 1
        
        while l <= r:

            m = (r + l) // 2
            
            # if target is less than m
            if target < nums[m % n]:
                r = m - 1
                    
            # if target is greater than m
            elif target > nums[m % n]:
                l = m + 1
                
            # target is at mid
            else:
                return m % n

        # target not present
        return -1
