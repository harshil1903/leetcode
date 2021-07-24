
# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#
# Source : https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
#
# Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from
# the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth
# vertical cut.
#
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts.
# Since the answer can be a huge number, return this modulo 10^9 + 7.



class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        # horizontalCuts.append(h)
        # verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()

        maxh = horizontalCuts[0]
        maxv = verticalCuts[0]

        for i in range(0, len(horizontalCuts) - 1):
            if (horizontalCuts[i + 1] - horizontalCuts[i]) > maxh:
                maxh = horizontalCuts[i + 1] - horizontalCuts[i]

        for i in range(0, len(verticalCuts) - 1):
            if (verticalCuts[i + 1] - verticalCuts[i]) > maxv:
                maxv = verticalCuts[i + 1] - verticalCuts[i]

        if (h - horizontalCuts[-1]) > maxh:
            maxh = h - horizontalCuts[-1]

        if (w - verticalCuts[-1]) > maxv:
            maxv = w - verticalCuts[-1]

        return ((maxh * maxv) % (10 ** 9 + 7))


if __name__ == '__main__':
    s = Solution();

    print(s.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
    print(s.maxArea( h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))

