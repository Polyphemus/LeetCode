# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
# then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is
# not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i-1]:
                # replace nums[i-1] with the smallest digit right of nums
                numsRight = nums[i:]
                x = min(num for num in numsRight if num > nums[i-1])
                numsRight.append(nums[i-1])
                nums[i-1] = x
                numsRight.remove(x)
                nums[i:] = sorted(numsRight)
                break
        else:
            nums.sort()
