
# 18. 4Sum
#
# Source : https://leetcode.com/problems/4sum/
#
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.



from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):

            size = len(nums)

            if size < k or nums[0] * k > target or nums[-1] * k < target:
                return []
            if k == 2:
                return twoSum(nums, target)
            result = []

            for i in range(size):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                for pair in kSum(nums[i + 1:], target - nums[i], k - 1):
                    result.append([nums[i]] + pair)

            return result

        def twoSum(nums: List[int], target: int) -> List[int]:

            size = len(nums)
            result = []

            start = 0;
            end = size - 1
            while start < end:
                s = nums[start] + nums[end]

                if s == target:
                    result.append([nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1

                elif s > target:
                    end -= 1
                else:
                    start += 1

            return result

        nums = sorted(nums)
        return kSum(nums, target, 4)

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        result = []

        if size < 4:
            return result

        for k in range(size - 3):
            for i in range(k + 1, size - 2):
                # if i==0 or nums[i] != nums[i-1]:
                start = i + 1;
                end = size - 1
                while start < end:
                    s = nums[start] + nums[end] + nums[i] + nums[k]
                    if s == target and [nums[k], nums[i], nums[start], nums[end]] not in result:
                        result.append([nums[k], nums[i], nums[start], nums[end]])

                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1

                    elif s > target:
                        end -= 1
                    else:
                        start += 1

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0));
    print(s.fourSum1([1, 0, -1, 0, -2, 2], 0));