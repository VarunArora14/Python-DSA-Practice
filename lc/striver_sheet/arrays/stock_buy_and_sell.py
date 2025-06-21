"""
https://takeuforward.org/data-structure/stock-buy-and-sell/
Here we have an array representing list of numbers which are stock prices. Now, to maximize the stock amount, we should buy at the lowest and sell at
highest any number of times with aim to maximise the amount (can't use the same element of array again for transaction)

To maximise the profit, we aim to minimize the buying amount and maximise the selling amount. If we have array like [7,6,5,10], we want to buy at 5
and then sell at 10 to maximize the profit.

Interesting case - [7,6,5,10,11] => how to handle the transaction
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minval = float("inf")

        for p in prices:
            if minval < p:
                max_profit = max(max_profit, p - minval)
            minval = min(minval, p)

        return max_profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
