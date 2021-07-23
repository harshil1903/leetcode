
# 4. Median of Two Sorted Arrays
#
# Source : https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.



class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        size = len(nums1) + len(nums2)
        num3 = sorted(nums1 + nums2)

        if (size % 2 == 0):
            median = (num3[int(size / 2) - 1] + num3[int(size / 2)]) / 2
        else:
            median = num3[int(size / 2)]

        return median

    def alternate_findMedianSortedArrays(self, nums1, nums2) -> float:
        size = len(nums1) + len(nums2)
        num3 = []
        s1 = len(nums1)
        s2 = len(nums2)
        i, j = 0, 0

        while i < s1 and j < s2:
            if (nums1[i] < nums2[j]):
                num3.append(nums1[i])
                i += 1
            else:
                num3.append(nums2[j])
                j += 1

        num3 = num3 + nums1[i:] + nums2[j:]

        if (size % 2 == 0):
            median = (num3[int(size / 2) - 1] + num3[int(size / 2)]) / 2
        else:
            median = num3[int(size / 2)]

        return median


if __name__ == '__main__':
    s = Solution();

    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))