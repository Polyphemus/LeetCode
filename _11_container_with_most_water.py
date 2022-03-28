# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = min(height[0], height[-1]) * (len(height) -1)
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                i += 1
                if min(height[i], height[j]) * (j - i) > max:
                    max = min(height[i], height[j]) * (j - i)
            else:
                j -= 1
                if min(height[i], height[j]) * (j - i) > max:
                    max = min(height[i], height[j]) * (j - i)
        return(max)
