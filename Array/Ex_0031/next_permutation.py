from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        size = len(nums)

        index = -1

        # Find position where you find a decreasing sequence while looping the array in reverse
        for i in range(size - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break

        # Signifies there is no greater permutation possible, so just reverse the array
        if index == -1:
            reverse(nums, 0, size - 1)
            return

        j = size - 1

        # Swap the previously found index with next highest number in the array right of it
        for i in range(size - 1, index, -1):
            if nums[i] > nums[index]:
                j = i
                break
        nums[index], nums[j] = nums[j], nums[index]

        # Sort the remaining array after the index position to get smallest permutation
        reverse(nums, index + 1, size - 1)

    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        nums[i + 1:] = reversed(nums[i + 1:])

        if i < 0:
            return

        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break


if __name__ == "__main__":
    s = Solution()
    test = [1,2,3]
    test1 = [1,2,3]
    s.nextPermutation(test)
    s.nextPermutation1(test)
    print(test);
    print(test1);