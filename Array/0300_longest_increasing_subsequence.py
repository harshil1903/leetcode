
# 300. Longest Increasing Subsequence
#
# Source : https://leetcode.com/problems/longest-increasing-subsequence/
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For
# example,
# [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = []

        for num in nums:
            left = bisect.bisect_left(LIS, num)

            # If num is greater than any element in sub
            if left == len(LIS):
                LIS.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                LIS[left] = num

        return len(LIS)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]));