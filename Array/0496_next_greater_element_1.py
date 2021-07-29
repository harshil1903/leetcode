
# 496. Next Greater Element I
#
# Source : https://leetcode.com/problems/next-greater-element-i/
#
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next
# greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



from typing import List


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            index = nums2.index(nums1[i])

            for j in range(index, len(nums2)):
                if nums1[i] < nums2[j]:
                    res[i] = nums2[j]
                    break
        return res


    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            for i in range(nums2.index(num), len(nums2)):
                if i == len(nums2) - 1 and nums2[-1] <= num:
                    res.append(-1)
                elif nums2[i] > num:
                    res.append(nums2[i])
                    break
        return res


    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        indices = {val: index for index, val in enumerate(nums2)}

        res = []
        for i, val in enumerate(nums1):
            j = indices[val]
            while j < len(nums2) and nums2[j] <= val:
                j += 1

            if j == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[j])

        return res


if __name__ == '__main__':
    s = Solution();

    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
    print(s.nextGreaterElement1([4,1,2], [1,3,4,2]))
    print(s.nextGreaterElement2([4,1,2], [1,3,4,2]))