
# 1313. Decompress Run-Length Encoded List
#
# Source : https://leetcode.com/problems/decompress-run-length-encoded-list/
#
# We are given a list nums of integers representing a list compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val
# concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
#
# Return the decompressed list.



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