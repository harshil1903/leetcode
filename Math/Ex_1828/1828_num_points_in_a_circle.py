
# 1828. Queries on Number of Points Inside a Circle
#
# Source : https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
#
# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.
#
# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.
#
# For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.
#
# Return an array answer, where answer[j] is the answer to the jth query.



from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for x1, y1, r in queries:
            result.append(0)
            for x, y in points:
                if (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2:
                    result[-1] += 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))