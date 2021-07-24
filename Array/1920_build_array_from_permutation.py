
# 1920. Build Array from Permutation
#
# Source : https://leetcode.com/problems/build-array-from-permutation/
#
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return
# it.
#
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).




from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        ind = 0

        for i in nums:
            res[ind] = nums[i]
            ind += 1

        return res

    def buildArray1(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            res.append(nums[i])

        return res


if __name__ == '__main__':
    s = Solution();
    print(s.buildArray([0,2,1,5,3,4]))
    print(s.buildArray1([5,0,1,2,3,4]))