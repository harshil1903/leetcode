
# 27. Remove Element
#
# Source : https://leetcode.com/problems/remove-element/
#
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.



from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            return 0

        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2], 2));