
# 11. Container With Most Water
#
# Source : https://leetcode.com/problems/container-with-most-water/
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.



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