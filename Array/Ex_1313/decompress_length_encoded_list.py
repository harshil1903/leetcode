from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                result.append(nums[i + 1])

        return result

    def decompressRLElist1(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(0, len(nums) - 1, 2):
            freq = nums[i]
            value = nums[i + 1]
            for j in range(freq):
                output.append(value)
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.decompressRLElist([1, 2, 3, 4]))
    print(s.decompressRLElist1([1, 2, 3, 4]))