from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) <= 2:
            return max(s)

        s.remove(max(s))
        s.remove(max(s))
        return max(s)

    def thirdMax1(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]

    def thirdMax2(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        for i in nums:
            if i > a:
                c, b, a = b, a, i
            elif i < a and i > b:
                c, b = b, i
            elif i < b and i > c:
                c = i

        if c == float('-inf'):
            return a
        return c


if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([3,2,1]))
    print(s.thirdMax1([2,2,3,1]))
    print(s.thirdMax2([1,2]))