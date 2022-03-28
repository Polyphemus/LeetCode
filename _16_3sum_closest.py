# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # basically brute force with optimization
        
        nums.sort()  # O(n log n) time

        # Optimization: if largest three are smaller than target, return largest three. If smaller three are larger than target, return those
        if nums[0] + nums[1] + nums[2] >= target:
            return nums[0] + nums[1] + nums[2]
        
        if nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] <= target:
            return nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3]

        # Because uniquely ordered combos don't matter, we'll skip all nums before parent pointer as those have been checked already
        # i.e. no point in checking 1+3+2 if we've already checked 1+2+3

        # Optimization: if the first three combined are closer to target than the last three, iterate from the beginning
        if abs(target - (nums[0] + nums[1] + nums[2])) < abs(nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3]):
            diff = target - (nums[0] + nums[1] + nums[2])

            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    for k in range(j+1, len(nums)):
                        if target - (nums[i] + nums[j] + nums[k]) == 0:  # Optimization: if target is hit, return target
                            return nums[i] + nums[j] + nums[k]

                        if abs(target - (nums[i] + nums[j] + nums[k])) < abs(diff):  # if current sum is closer to target, save new difference
                            diff = target - (nums[i] + nums[j] + nums[k])

                        # If current sum is further from target than previous nums[k] sum, break because it won't improve moving further along number line
                        elif k != j + 1 and abs(target - (nums[i] + nums[j] + nums[k])) > abs(target - (nums[i] + nums[j] + nums[k - 1])):
                            break
                        else:
                            pass

        # if the last three combined are closer to target than the last three, iterate from the end
        else:
            diff = target - (nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3])
            for i in range(len(nums)-1, -1, -1):
                for j in range(i-1, -1, -1):
                    for k in range(j-1, -1, -1):

                        if target - (nums[i] + nums[j] + nums[k]) == 0:
                            return nums[i] + nums[j] + nums[k]

                        if abs(target - (nums[i] + nums[j] + nums[k])) < abs(diff):
                            diff = target - (nums[i] + nums[j] + nums[k])

                        elif k!= j - 1 and abs(target - (nums[i] + nums[j] + nums[k])) > abs(target - (nums[i] + nums[j] + nums[k + 1])):
                            break

                        else:    
                            pass

        return target - diff      
