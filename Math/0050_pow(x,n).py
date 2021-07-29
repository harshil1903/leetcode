
# 50. Pow(x, n)
#
# Source : https://leetcode.com/problems/powx-n/
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x

        res = 1.0

        neg = False

        if n < 0:
            neg = True
            n = -n

        # Right shifting 1 bit is essentially dividing number by 2
        while n > 0:
            if n % 2 != 0:
                res *= x
            n >>= 1
            x *= x

        if neg:
            res = 1.0 / res

        return res

    def myPow1(self, x: float, n: int) -> float:

        def helper(target, n):
            if n == 0:
                return 1
            half = helper(target, n // 2)   # // is for floor of division
            if n % 2 == 0:
                return half * half
            else:
                return half * half * target

        if n < 0:
            return 1 / helper(x, -n)
        else:
            return helper(x, n)

    def myPow2(self, x: float, n: int) -> float:
        return pow(x, n)

if __name__ == '__main__':
    s = Solution();

    print(s.myPow1(2, 16))
    print(s.myPow2(12, 6))
