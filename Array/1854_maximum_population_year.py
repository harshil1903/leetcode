
# 1854. Maximum Population Year
#
# Source : https://leetcode.com/problems/maximum-population-year/
#
# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
#
# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range
# [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
#
# Return the earliest year with the maximum population.



import collections
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop = [0] * 2051
        res = 0
        for l in logs:
            pop[l[0]] += 1
            pop[l[1]] -= 1

        for i in range(1950, 2050):
            pop[i] += pop[i - 1]
            if pop[i] > pop[res]:
                res = i

        return res

    def maximumPopulation1(self, logs: List[List[int]]) -> int:
        dic = collections.defaultdict(int)

        maxi = 0

        for i in logs:
            for j in range(int(i[0]), int(i[1])):
                dic[j] += 1
                if maxi <= dic[j]:
                    maxi = dic[j]

        res = 9999

        for i in dic.keys():
            if dic[i] == maxi and res > i:
                res = i

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maximumPopulation([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]));