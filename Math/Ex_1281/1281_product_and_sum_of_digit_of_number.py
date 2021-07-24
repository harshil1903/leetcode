
# 1281. Subtract the Product and Sum of Digits of an Integer
#
# Source : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
#
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        sm, mul = 0, 1

        for j in digits:
            sm += j
            mul *= j

        return mul - sm

    def subtractProductAndSum1(self, n: int) -> int:
        sm, mul = 0, 1

        for digit in str(n):
            sm += int(digit)
            mul *= int(digit)

        return mul - sm

if __name__ == '__main__':
    s = Solution()
    print(s.subtractProductAndSum(234))
    print(s.subtractProductAndSum1(4421))