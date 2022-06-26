# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# You may return the answer in any order.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        ans = []
        
        ansDict = {}
        
        numsDict = {}
        for h in range(len(nums)):
            numsDict[nums[h]] = h
        
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                pass
            else:
                for j in range(i+1, len(nums)-1):
                    if j !=i+1 and nums[j] == nums[j-1]:
                        pass
                    else:
                        for k in range(j+1, len(nums)):
                            if k != j+1 and nums[k] == nums[k-1]:
                                pass
                            else:
                                if target - (nums[i] + nums[j] + nums[k]) in numsDict and numsDict[target - (nums[i] + nums[j] + nums[k])] not in (i,j,k):
                                    if tuple(sorted([nums[i], nums[j], nums[k], target - (nums[i] + nums[j] + nums[k])])) not in ansDict:
                                        ansDict[tuple(sorted([nums[i], nums[j], nums[k], target - (nums[i] + nums[j] + nums[k])]))] = None
                                        ans.append([nums[i], nums[j], nums[k], target - (nums[i] + nums[j] + nums[k])])
        return ans
