
# 1. Two Sum
#
# Source : https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order



class Solution:
    def twoSum(self, nums, target) -> list:
        container = {}

        for i, num in enumerate(nums):
            if target - num in container:
                return [container[target - num], i]
            container[num] = i
        return


if __name__ == '__main__':
    s = Solution();
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))