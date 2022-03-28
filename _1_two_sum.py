# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = {}
        for i in range(len(nums)):
            n[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in n and n[complement] != i:
                return[i, n[complement]]