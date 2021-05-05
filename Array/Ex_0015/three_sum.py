from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        result = []

        if size < 3:
            return result

        for i in range(size - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                start = i + 1;
                end = size - 1
                while start < end:
                    s = nums[start] + nums[end] + nums[i]
                    if s == 0:
                        result.append([nums[i], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1

                    elif s > 0:
                        end -= 1
                    else:
                        start += 1

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum ([-1,0,1,2,-1,-4]))