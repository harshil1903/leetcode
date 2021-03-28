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