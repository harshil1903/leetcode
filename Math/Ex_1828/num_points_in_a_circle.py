from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        i = 0;
        print(ans)
        for q in queries:
            for p in points:

                if((q[0] - q[2]) <= p[0] <= (q[0] + q[2])):
                    if((q[1] - q[2]) <= p[1] <= (q[1] + q[2])):

                        if(p[0] == q[0] - q[2] or p[0] == q[0] + q[2]):
                            if(p[1] != q[1] - q[2] and p[1] != q[1] + q[2]):
                                ans[i] += 1
                        elif (p[1] == q[1] - q[2] or p[1] == q[1] + q[2]):
                            if (p[0] != q[0] - q[2] and p[0] != q[0] + q[2]):
                                ans[i] += 1
                        else:
                            ans[i] += 1
            i+=1

        return ans;

if __name__ == '__main__':
    s = Solution()
    print(s.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))