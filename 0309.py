"""
309. Best Time to Buy and Sell Stock with Cooldown
description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
"""

"""
Note:
1. dfs+memo: O(n) time | O(n) space
2. dp: O(n) time | O(1) space
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

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        holdStock, keepCash = -float("inf"), 0
        prevKeepCash = 0
        for price in prices:
            prevHoldStock = holdStock
            holdStock = max(
                prevKeepCash - price,
                holdStock
            )

            prevKeepCash = keepCash
            keepCash = max(
                keepCash,
                prevHoldStock + price
            )
        return keepCash

# Unit Tests
import unittest
funcs = [Solution().maxProfit, Solution2().maxProfit]


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
