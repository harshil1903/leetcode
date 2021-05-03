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