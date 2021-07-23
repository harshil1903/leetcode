
# 1389. Create Target Array in the Given Order
#
# Source : https://leetcode.com/problems/create-target-array-in-the-given-order/
#
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
#
# It is guaranteed that the insertion operations will be valid.



from typing import List


class Solution:

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            result.insert(index[i], nums[i])

        return result

    def createTargetArray1(self, nums: List[int], index: List[int]) -> List[int]:
        result = [9999] * len(nums)

        for i in range(len(nums)):
            ind = index[i]
            val = nums[i]
            if (result[ind] == 9999):
                result[ind] = val
            else:
                for k in range(len(nums) - 1, ind, -1):
                    result[k] = result[k - 1]
                result[ind] = val

        return result

    def createTargetArray2(self, nums: List[int], index: List[int]) -> List[int]:
        result = [None] * len(nums)

        for i in range(len(nums)):
            if (result[index[i]] is None):
                result[index[i]] = nums[i]
            else:
                for k in range(len(nums) - 1, index[i], -1):
                    result[k] = result[k - 1]
                result[index[i]] = nums[i]

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.createTargetArray([0, 1, 2, 3, 4],[0, 1, 2, 2, 1]))
    print(s.createTargetArray1([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
    print(s.createTargetArray2([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))