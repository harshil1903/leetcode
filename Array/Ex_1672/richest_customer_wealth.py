
# 1672. Richest Customer Wealth
#
# Source : https://leetcode.com/problems/richest-customer-wealth/
#
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the
# richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.



class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth = 0

        for cust in accounts:
            x = sum(i for i in cust)
            if (wealth < x):
                wealth = x

        return wealth

if __name__ == '__main__':
    s = Solution();

    print(s.maximumWealth([[1,2,3],[3,2,1]]))
    print(s.maximumWealth([[1,5],[7,3],[3,5]]))