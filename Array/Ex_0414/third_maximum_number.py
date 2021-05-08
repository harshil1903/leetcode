from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) <= 2:
            return max(s)

        s.remove(max(s))
        s.remove(max(s))
        return max(s)

if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([3,2,1]))
    print(s.thirdMax([2,2,3,1]))
    print(s.thirdMax([1,2]))