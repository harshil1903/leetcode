
# 45. Jump Game II
#
# Source : https://leetcode.com/problems/jump-game-ii/
#
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.



from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        l, r = 0, 0
        res = 0

        for i in range(len(nums) - 1):
            l = max(l, i + nums[i])

            if i == r:
                r = l
                res += 1

        return res

    def jump1(self, nums: List[int]) -> int:
        jump_count = 0
        reachable = 0
        curr_reachable = 0

        for i, length in enumerate(nums):
            if i > reachable:
                return -1
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1
            reachable = max(reachable, i + length)
        return jump_count


if __name__ == "__main__":
    s = Solution()
    print(s.jump1([2,3,1,1,4]));