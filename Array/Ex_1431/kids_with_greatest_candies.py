class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l = []
        for i in candies:
            if ((i + extraCandies) >= max(candies)):
                l.append(True)
            else:
                l.append(False)

        return l

if __name__ == '__main__':
    s = Solution();
    print(s.kidsWithCandies([2,3,5,1,3], 3))
    print(s.kidsWithCandies([4,2,1,1,2], 1))