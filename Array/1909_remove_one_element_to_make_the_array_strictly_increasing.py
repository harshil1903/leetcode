
# 1909. Remove One Element to Make the Array Strictly Increasing
#
# Source : https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
#
# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array
# is already strictly increasing, return true.
#
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).



from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removal = 0
        increasing1 = True
        previous = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if n <= previous:
                removal += 1
                if removal > 1:
                    increasing1 = False
                    break
            else:
                previous = n

        removal = 0
        increasing2 = True
        previous = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            n = nums[i]
            if n >= previous:
                removal += 1
                if removal > 1:
                    increasing2 = False
                    break
            else:
                previous = n

        return increasing1 or increasing2

    def canBeIncreasing1(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            n = nums[:i] + nums[i + 1:]
            if n == sorted(n) and len(n) == len(set(n)):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canBeIncreasing( [1,2,10,5,7]))