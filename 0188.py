"""
188. Best Time to Buy and Sell Stock IV
description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
"""

"""
Note:
1. DP: O(n*k) time | O(k) space - where n is the length of prices
ref: https://vocus.cc/article/65fd41d2fd897800015721f3
"""




from typing import List
import unittest, collections
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = collections.defaultdict(int)
        HOLD_STOCK, KEEP_CASH = 0, 1
        for tran in range(k+1):
            dp[HOLD_STOCK, tran] = -float("inf")

        for price in prices:
            for tran in range(1, k+1):
                # keep cash and do nothing or sell stock today
                dp[KEEP_CASH, tran] = max(
                    dp[KEEP_CASH, tran],
                    dp[HOLD_STOCK, tran] + price
                )

                # hold stock or buy stock today
                dp[HOLD_STOCK, tran] = max(
                    dp[HOLD_STOCK, tran],
                    dp[KEEP_CASH, tran-1] - price 
                )
        return dp[KEEP_CASH, k]

# Unit Tests
funcs = [Solution().maxProfit]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            k = 2
            prices = [2, 4, 1]
            self.assertEqual(func(k=k, prices=prices), 2)

    def testMaxProfit2(self):
        for func in funcs:
            k = 2
            prices = [3, 2, 6, 5, 0, 3]
            self.assertEqual(func(k=k, prices=prices), 7)


if __name__ == "__main__":
    unittest.main()
