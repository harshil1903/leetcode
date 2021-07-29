
# 169. Majority Element
#
# Source : https://leetcode.com/problems/majority-element/
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        MAX = 0
        res = None
        for key, value in count.items():

            if value > MAX:
                MAX = value
                res = key

        return res

    def majorityElement1(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]

    # Referenced
    def majorityElement2(self, nums: List[int]) -> int:

        numbers = list(set(nums))

        answers = []
        for elements in numbers:
            if nums.count(elements) > len(nums) / 2:
                return elements


if __name__ == '__main__':
    s = Solution();

    print(s.majorityElement([3,2,3]))
    print(s.majorityElement1([2,2,1,1,1,2,2]))