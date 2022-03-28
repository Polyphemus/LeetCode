# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = {}
        nums.sort
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                idict = {}
                for j in range(len(nums)):
                    if j != i:
                        complement = 0 - (nums[j])
                        if complement in idict and idict[complement] != j:
                            answers[(tuple(sorted([nums[i], nums[j], nums[idict[complement]]])))] = 1
                        else:
                            idict[nums[j] + nums[i]] = j
        answer = []
        for ans in answers.keys():
            answer.append(list(ans))

        return (answer)
