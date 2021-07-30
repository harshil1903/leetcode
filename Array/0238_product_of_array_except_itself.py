
# 238. Product of Array Except Self
#
# Source : https://leetcode.com/problems/product-of-array-except-self/
#
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.



from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        product = 1

        # Append i-1 elements' product in ith place
        for i in nums:
            res.append(product)
            product *= i

        product = 1

        # Multiply n - (i + 1) elements' product in ith place
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res


    def productExceptSelf1(self, nums: List[int]) -> List[int]:

        if not nums:
            return

        left = [1] * len(nums)
        right = 1

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            left[i] *= right

        return left

if __name__ == '__main__':
    s = Solution();

    print(s.productExceptSelf1([1,3,4,2]))
    print(s.productExceptSelf([1,3,4,2]))