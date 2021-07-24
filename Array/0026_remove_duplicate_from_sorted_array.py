
# 26. Remove Duplicates from Sorted Array
#
# Source : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.



from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        i = 0
        for j in range(0, len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]

        return i + 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]));