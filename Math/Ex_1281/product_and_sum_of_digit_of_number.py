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