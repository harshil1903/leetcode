
# 149. Max Points on a Line
#
# Source : https://leetcode.com/problems/max-points-on-a-line/
#
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight
# line.



import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            slopes = {}
            for j in range(i + 1, len(points)):
                y = points[i][1] - points[j][1]
                x = points[i][0] - points[j][0]
                if x != 0:
                    m = y / x
                else:
                    m = float('inf')
                slopes[m] = slopes.get(m, 0) + 1

            max_slope = max(slopes.values())
            if max_slope > result:
                result = max_slope

        return result + 1

    def maxPoints1(self, points: List[List[int]]) -> int:
        max_points = 0
        for i, start in enumerate(points):
            slope_count, same = collections.defaultdict(int), 1
            for j in range(i + 1, len(points)):
                end = points[j]
                if start[0] == end[0] and start[1] == end[1]:
                    same += 1
                else:
                    slope = float("inf")
                    if start[0] - end[0] != 0:
                        slope = (start[1] - end[1]) * 1.0 / (start[0] - end[0])
                    slope_count[slope] += 1

            current_max = same
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope] + same)

            max_points = max(max_points, current_max)

        return max_points

if __name__ == "__main__":
    s = Solution()
    print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(s.maxPoints1([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))