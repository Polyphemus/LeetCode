# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # brute force with some optimization, too slow
        # order doesn't matter so trie doesn't make sense
        # because unique combos don't matter, we'll skip all nums. before parent as those have been checked already
        # if we sort, and largest three are smaller than target, return largest three. If smaller three are larger than target, return those
        # if three largest are closest to target, iterate in reverse
        
        nums.sort()
        print(nums)
        if nums[0] + nums[1] + nums[2] >= target:
            return nums[0] + nums[1] + nums[2]
        
        if nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] <= target:
            return nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3]
        
        # if the first three combined are closer to target than the last three, iterate from the beginning
        if abs(target - (nums[0] + nums[1] + nums[2])) < abs(nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3]):
            diff = target - (nums[0] + nums[1] + nums[2])
    #        print(f'initial diff = {diff}')

            for i in range(len(nums)):
    #            print(f'\ni = {i}')
                for j in range(i+1, len(nums)):                        
    #                print(f'j = {j}')
                    for k in range(j+1, len(nums)):
                        if target - (nums[i] + nums[j] + nums[k]) == 0:
    #                            print(f'Exact match! i = {i}, j = {j}, k = {k}')
                            return nums[i] + nums[j] + nums[k]

                        if abs(target - (nums[i] + nums[j] + nums[k])) < abs(diff): # if current sum is closer to target
                            diff = target - (nums[i] + nums[j] + nums[k])
    #                        print(f'new diff = {diff}')

                        elif k != j + 1 and abs(target - (nums[i] + nums[j] + nums[k])) > abs(target - (nums[i] + nums[j] + nums[k - 1])):
                            # break if current sum is further from target than previous nums[k] sum because it won't improve moving further along number line
    #                        print(f'nums[k-1] = {nums[k-1]}')
    #                        print(f'nums[k] = {nums[k]}')
    #                        print('break')
                            break

                        else:    
    #                        print('passing')
                            pass
        # if the last three combined are closer to target than the last three, iterate from the end
        else:
            diff = target - (nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3])
#            print(f'initial diff = {diff}')
            for i in range(len(nums)-1, -1, -1):
#                print(f'\ni = {i}')
                for j in range(i-1, -1, -1):                        
#                    print(f'j = {j}')
                    for k in range(j-1, -1, -1):
#                        print(f'k = {k}')
#                        print(f'current sum = {nums[i] + nums[j] + nums[k]}')
                        if target - (nums[i] + nums[j] + nums[k]) == 0:
#                            print(f'Exact match! i = {i}, j = {j}, k = {k}')
                            return nums[i] + nums[j] + nums[k]

                        if abs(target - (nums[i] + nums[j] + nums[k])) < abs(diff): # if current sum is closer to target
                            diff = target - (nums[i] + nums[j] + nums[k])
#                            print(f'new diff = {diff}')

                        elif k!= j - 1 and abs(target - (nums[i] + nums[j] + nums[k])) > abs(target - (nums[i] + nums[j] + nums[k + 1])):
                            # break if current sum is further from target than previous nums[k] sum because it won't improve moving further along number line
    #                        print(f'nums[k-1] = {nums[k-1]}')
    #                        print(f'nums[k] = {nums[k]}')
                            print('break')
                            break

                        else:    
#                            print('passing')
                            pass
            
        
        return target - diff      
