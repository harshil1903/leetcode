class Solution:
    def twoSum(self, nums, target) -> list:
        container = {}

        for i, num in enumerate(nums):
            if target - num in container:
                return [container[target - num], i]
            container[num] = i
        return


if __name__ == '__main__':
    s = Solution();
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))