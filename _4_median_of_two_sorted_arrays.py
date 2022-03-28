# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        i = j = 0

        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1

            else:
                ans.append(nums2[j])
                j += 1

        while i < len(nums1):
            ans.append(nums1[i])
            i += 1

        while j < len(nums2):
            ans.append(nums2[j])
            j += 1

        if len(ans) % 2 == 0:
            return ((ans[len(ans) // 2] + ans[len(ans) // 2 - 1]) / 2)

        else:
            return (ans[len(ans) // 2])