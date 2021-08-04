
# 540. Single Element in a Sorted Array
#
# Source : https://leetcode.com/problems/single-element-in-a-sorted-array/
#
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.



from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            # exit condition
            if left == right:
                return nums[left]

            # get mid
            mid = left + (right - left) // 2

            # make sure mid is even
            if mid % 2 == 1:
                mid -= 1

            # single value on the left of mid
            if nums[mid] == nums[mid + 1]:
                left = mid + 2

            # single value on the right or is mid
            else:
                right = mid

    def singleNonDuplicate1(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int(left + (right - left) / 2)

            if not (mid % 2 == 0 and mid + 1 < len(nums) and nums[mid] == nums[mid + 1]) and \
                    not (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]));

