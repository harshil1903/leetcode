
# 384. Shuffle an Array
#
# Source : https://leetcode.com/problems/shuffle-an-array/
#
# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the
# shuffling.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.



import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.num = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.num

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = list(self.num)
        for i in range(len(nums)):
            j = random.randint(i, len(nums) - 1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


    # Other way
    def __init1__(self, nums: List[int]):
        self.nums = nums
        self.og = nums.copy()

    def reset1(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.og

    def shuffle1(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]