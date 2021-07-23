from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        ind = 0

        for i in nums:
            res[ind] = nums[i]
            ind += 1

        return res


if __name__ == '__main__':
    s = Solution();
    print(s.buildArray([0,2,1,5,3,4]))
    print(s.buildArray([5,0,1,2,3,4]))