
# 1431. Kids With the Greatest Number of Candies
#
# Source : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
#
# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
#
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.



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