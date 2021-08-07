
# 33. Search in Rotated Sorted Array
#
# Source : https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,
# 0,1,2].
#
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.



from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # found index
            if nums[mid] == target:
                return mid

            # left to mid is sorted in ascending order
            if nums[left] <= nums[mid]:
                # target is between left and mid
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # left to mid is not sorted
            else:
                # target is between mid and right
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def search1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int (left + (right - left) / 2)

            if nums[mid] == target:
                return mid
            elif (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2],0))