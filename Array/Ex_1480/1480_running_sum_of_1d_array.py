
# 1480. Running Sum of 1d Array
#
# Source : https://leetcode.com/problems/running-sum-of-1d-array/
#
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.



class Solution:
    def runningSum(self, nums):
        temp = 0
        l = []
        for i in nums:
            temp += i
            l.append(temp)

        return l

if __name__ == '__main__':
    s = Solution();
    print(s.runningSum([1,2,3,4]))
    print(s.runningSum([5,6,7]))
