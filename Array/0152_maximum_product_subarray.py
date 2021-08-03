
# 152. Maximum Product Subarray
#
# Source : https://leetcode.com/problems/maximum-product-subarray/
#
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
#
# It is guaranteed that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.



from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxi = mini = nums[0]

        for i in range(1, len(nums)):
            temp = max(maxi * nums[i], nums[i], mini * nums[i])
            mini = min(maxi * nums[i], nums[i], mini * nums[i])
            maxi = temp
            res = max(maxi, res)

        return res

    def maxProduct1(self, nums: List[int]) -> int:

        global_max, local_max, local_min = float("-inf"), 1, 1

        for num in nums:
            local_max = max(1, local_max)
            if num > 0:
                local_max = local_max * num
                local_min = local_min * num
            else:
                temp = local_max
                local_max = local_min * num
                local_min = temp * num

            global_max = max(global_max, local_max)

        return global_max

if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]));