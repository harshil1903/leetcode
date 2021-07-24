
# 1512. Number of Good Pairs
#
# Source : https://leetcode.com/problems/number-of-good-pairs/
#
# Given an array of integers nums.
#
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
# Return the number of good pairs.



class Solution:
    def numIdenticalPairs(self, nums) -> int:
        k = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]):
                    k += 1

        return k

if __name__ == '__main__':
    s = Solution();
    print(s.numIdenticalPairs([1,2,3,1,1,3]))
    print(s.numIdenticalPairs([1,1,1,1]))