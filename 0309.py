"""
309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

"""
Note:
1. dfs+memo: O(n) time | O(n) space
2. dp: O(n) time | O(1) space
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-2][k-1][0] - prices[i])
                = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
"""

from typing import List
import functools
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i, buying) -> int:
            if i >= len(prices):
                return 0
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                return max(sell, cooldown)
        return dfs(0, True)

    def maxProfit2(self, prices: List[int]) -> int:
        hold = float("-inf")
        preIdle = idle = 0
        for price in prices:
            hold = max(hold, preIdle - price)
            preIdle = idle
            idle = max(idle, hold + price)
        return idle

# Unit Tests
import unittest
funcs = [Solution().maxProfit, Solution().maxProfit2]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            prices = [1,2,3,0,2]
            self.assertEqual(func(prices=prices), 3)

    def testMaxProfit2(self):
        for func in funcs:
            prices = [1]
            self.assertEqual(func(prices=prices), 0)

if __name__ == "__main__":
    unittest.main()
