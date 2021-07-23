
# 29. Divide Two Integers
#
# Source : https://leetcode.com/problems/divide-two-integers/
#
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem,
# assume that your function returns 231 − 1 when the division result overflows



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        dividend_sign, divisor_sign = 1, 1

        if divisor == -1 and dividend == -2147483648:
            return 2147483647

        if dividend == 0:
            return 0

        if dividend < 0:
            dividend *= -1
            dividend_sign = -1

        if divisor < 0:
            divisor *= -1
            divisor_sign = -1


        while dividend - divisor >= 0:
            x = 0  # 2^0 = 1
            while (dividend - (divisor << 1 << x)) >= 0:
                x += 1  # divisor shifted over left to multiply it by a factor of 2^x

            result += (1 << x)  # 1 shifted by x to add 2^x to the result
            dividend -= (divisor << x)  # reduce divident value by 2^x times the value of divisor

        return result * divisor_sign * dividend_sign

    def divide1(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor < 0) or dividend < 0 and divisor > 0:
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while divisor <= dividend:

            tmpdiv = divisor
            mul = 1

            while tmpdiv <= dividend:
                result += mul

                dividend -= tmpdiv
                tmpdiv += tmpdiv
                mul += mul

        if sign == -1:
            result = -result

        return max(-2 ** 31, min(2 ** 31 - 1, result))

    def divide2(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i << 1
                temp = temp<< 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


if __name__ == "__main__":
    s = Solution()
    print(s.divide(-467, 3))
    print(s.divide1(25, 6))
    print(s.divide2(25, 6))