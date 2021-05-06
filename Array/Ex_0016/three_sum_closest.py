from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        result = 99999

        for i in range(size - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                start = i + 1;
                end = size - 1
                while start < end:
                    s = nums[start] + nums[end] + nums[i]

                    if s == target:
                        return s

                    if abs(target - s) < abs(target - result):
                        result = s

                    if s <= target:
                        start += 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                    else:
                        end -= 1
                        while start < end and nums[end + 1] == nums[end]:
                            end -= 1

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))