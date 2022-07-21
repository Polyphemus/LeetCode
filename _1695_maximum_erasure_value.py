# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
# 
# Return the maximum score you can get by erasing exactly one subarray.
# 
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Sliding window. Items are inserted into a subarray dict, values added to subtotal
        
        #print(len(nums))
        max_sum = 0
        current_sum = 0
        i = 0
        j = 0
        subarray = {}
        
        # sliding windows extends, adding items to dict, adding values to current_sum
        while j < len(nums):
            #print(i)
            #print(f'    {j}')
            if nums[j] not in subarray:
                current_sum += nums[j]
                subarray[nums[j]] = None
                j += 1
            # when a dupe is encountered, items are removed (and values subtracted) until dupe is removed
            else: 
                if current_sum > max_sum:
                    #print(f'new max sum = {current_sum}')
                    max_sum = current_sum
                while nums[j] in subarray:
                    del subarray[nums[i]]
                    current_sum -= nums[i]
                    i += 1
                subarray[nums[j]] = None
                current_sum += nums[j]
                j += 1
                
        # we're only checking whether current_sum is greater on repeated digits, test here in case j = len(nums)-1
        if current_sum > max_sum:
            max_sum = current_sum
        return(max_sum)
