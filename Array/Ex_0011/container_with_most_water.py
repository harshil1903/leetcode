from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0;
        end = len(height) - 1
        area = 0

        while start < end:
            tmp = min(height[start], height[end]) * (end - start);

            if tmp > area:
                area = tmp
            else:
                if (height[start] > height[end]):
                    tempEnd = height[end]
                    end -= 1
                    while tempEnd > height[end] and start < end:
                        end -= 1
                else:
                    tempStart = height[start]
                    start += 1
                    while tempStart >= height[start] and start < end:
                        start += 1

        return area

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))