
# 121. Best Time to Buy and Sell Stock
#
# Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = math.inf
        profit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > profit:
                profit = price - minPrice
        return profit

    def maxProfit1(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == '__main__':
    s = Solution();

    print(s.maxProfit([7,1,5,3,6,4]))