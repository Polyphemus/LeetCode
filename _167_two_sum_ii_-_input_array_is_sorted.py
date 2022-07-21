# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# 
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# 
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# 
# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers[0] >= 0:
            L = 0
            r = len(numbers)-1
            m = 0

            while L <= r:                
                m = (r + L)//2
                if numbers[m] == target:
                    break
                elif numbers[m] > target:
                    r = m - 1
                else:
                    L = m + 1
            L = 0
            r = m
            
            while L <= r:
                if numbers[L] + numbers[r] == target:
                    return [L+1, r+1]
                elif numbers[L] + numbers[r] > target:
                    r -= 1
                else: 
                    L += 1
        elif numbers[len(numbers)-1] <= 0:
            L = 0
            r = len(numbers)
            m = 0

            while L <= r:
                m = (r + L)//2
                if numbers[m] == target:
                    break
                elif numbers[m] > target:
                    r = m - 1
                else:
                    L = m + 1
            L = m
            r = len(numbers)-1
            
            while L <= r:
                if numbers[L] + numbers[r] == target:
                    return [L+1, r+1]
                elif numbers[L] + numbers[r] < target:
                    L += 1
                else: 
                    r -= 1
        else:
            L = 0
            r = len(numbers)-1
            
            while L<r:
                if numbers[L] + numbers[r] == target:
                    return[L+1, r+1]
                elif numbers[L] + numbers[r] > target:
                    r-=1
                else:
                    L+=1
