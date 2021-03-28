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

