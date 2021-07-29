
# 1. Two Sum
#
# Source : https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {}

        # enumerate(nums) gives i index and num as value at that index
        for i, num in enumerate(nums):
            if target - num in container:
                return [container[target - num], i]
            container[num] = i
        return

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            x = target - nums[i]

            # x is the second number needed along with nums[i] to make it equal to target
            # if x is present in dic{} we have out result in form of i and index of x
            if (x in dic):
                return [dic[x], i]
            else:
                dic[nums[i]] = i  # if x is not in disc, save value and index of i for future values


if __name__ == '__main__':
    s = Solution();
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))