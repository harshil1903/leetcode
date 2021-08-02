
# 53. Maximum Subarray
#
# Source : https://leetcode.com/problems/maximum-subarray/
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.



from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum= nums[0]
        cursum = 0
        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            maxsum = max(cursum, maxsum)
        return maxsum

    def maxSubArray1(self, nums: List[int]) -> int:
        result, curr = float("-inf"), float("-inf")
        for x in nums:
            curr = max(curr + x, x)
            result = max(result, curr)
            print(curr, result)
        return result

    def maxSubArray2(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        for i in range(len(nums)):
            memo[i] = max(memo[i - 1] + nums[i], nums[i])
        return max(memo)


if __name__ == '__main__':
    s = Solution();

    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))