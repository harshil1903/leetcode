from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        i = 0
        for j in range(0, len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]

        return i + 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]));