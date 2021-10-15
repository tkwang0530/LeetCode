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
1. recursion + caching: O(n) time | O(n) space
"""

from typing import Dict, List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # <(i, buying), maxProfit>
        return self.dfs(prices, 0, True, cache)

    def dfs(self, prices: List[int], i: int, buying: bool, cache: Dict) -> int:
        if i >= len(prices):
            return 0
        if (i, buying) in cache:
            return cache[(i, buying)]

        # always have cooldown option
        cooldown = self.dfs(prices, i+1, buying, cache)

        # if current run buying, next run selling (not buying)
        if buying:
            buy = self.dfs(prices, i+1, not buying, cache) - prices[i]
            cache[(i, buying)] = max(buy, cooldown)
        else:
            sell = self.dfs(prices, i+2, not buying, cache) + prices[i]
            cache[(i, buying)] = max(sell, cooldown)
        return cache[(i, buying)]

# Unit Tests
import unittest
funcs = [Solution().maxProfit]


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
