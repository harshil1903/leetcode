
# 605. Can Place Flowers
#
# Source : https://leetcode.com/problems/can-place-flowers/
#
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted
# in the flowerbed without violating the no-adjacent-flowers rule.



from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False

        elif len(flowerbed) == 2:
            if (flowerbed[0] == flowerbed[1] == 0) and n <= 1:
                return True
            elif n == 0:
                return True
            else:
                return False

        else:
            if flowerbed[0] == flowerbed[1] == 0:
                n -= 1
                flowerbed[0] = 1

            if flowerbed[-1] == flowerbed[-2] == 0:
                n -= 1
                flowerbed[-1] = 1

            for i in range(1, len(flowerbed) - 1, 1):
                if flowerbed[i] == flowerbed[i + 1] == flowerbed[i - 1] == 0:
                    n -= 1
                    flowerbed[i] = 1

            if n <= 0:
                return True
            else:
                return False

    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1],1))
    print(s.canPlaceFlowers1([1,0,0,0,1],2))