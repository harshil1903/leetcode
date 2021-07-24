
# 1464. Maximum Product of Two Elements in an Array
#
# Source : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
#
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).



class Solution:
    def maxProduct(self, nums) -> int:
        m1 = max(nums[0], nums[1])
        m2 = min(nums[0], nums[1])

        for i in range(2, len(nums)):
            if (nums[i] > m1):
                m2 = m1
                m1 = nums[i]

            elif (nums[i] > m2):
                m2 = nums[i]

        return ((m1 - 1) * (m2 - 1))

    def alternate_maxProduct(self, nums) -> int:

        nums.sort()

        return ((nums[-1] - 1) * (nums[-2] - 1))

if __name__ == '__main__':
    s = Solution();

    print(s.maxProduct([3,4,5,2]))
    print(s.maxProduct([1,5,4,5]))