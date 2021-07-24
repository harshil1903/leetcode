
# 1365. How Many Numbers Are Smaller Than the Current Number
#
# Source : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of
# valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.



import collections
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)

        for i in range(max(nums) + 1):
            count[i] += count[i - 1]

        return [count[i - 1] for i in nums]

    #bruteforce (unoptimized)
    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length

        for i in range(length):
            for j in range(length):
                if (i == j):
                    pass
                if (nums[i] > nums[j]):
                    result[i] += 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(s.smallerNumbersThanCurrent1([8, 1, 2, 2, 3]))