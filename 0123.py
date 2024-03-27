"""
123. Best Time to Buy and Sell Stock III
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example4:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
"""

"""
Note:
1. DP: O(n) time | O(1) space - where n is the length of prices
ref: https://vocus.cc/article/65fd41d2fd897800015721f3
"""




from typing import List
import unittest, collections
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # status
        HOLD_STOCK, KEEP_CASH = 0, 1
        dp = collections.defaultdict(int) # <(status, trans)>
        dp[HOLD_STOCK,0] = -float("inf")
        dp[HOLD_STOCK,1] = -float("inf")
        dp[HOLD_STOCK,2] = -float("inf")

        for price in prices:
            # first transaction
            # without stock and donothing or sell stock today
            dp[KEEP_CASH, 1] = max(
                dp[KEEP_CASH,1],
                dp[HOLD_STOCK,1] + price
            )
            # buy stock today or already buy before and keep
            dp[HOLD_STOCK, 1] = max(
                dp[HOLD_STOCK, 1],
                dp[KEEP_CASH,0] - price
            )

            # second transaction
            # without stock and donothing or sell stock today
            dp[KEEP_CASH, 2] = max(
                dp[KEEP_CASH,2],
                dp[HOLD_STOCK,2] + price
            )
            # buy stock today or already buy before and keep
            dp[HOLD_STOCK, 2] = max(
                dp[HOLD_STOCK, 2],
                dp[KEEP_CASH, 1] - price
            )
        return dp[KEEP_CASH, 2]

# Unit Tests
funcs = [Solution().maxProfit]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            prices = [3, 3, 5, 0, 0, 3, 1, 4]
            self.assertEqual(func(prices=prices), 6)

    def testMaxProfit2(self):
        for func in funcs:
            prices = [1, 2, 3, 4, 5]
            self.assertEqual(func(prices=prices), 4)

    def testMaxProfit3(self):
        for func in funcs:
            prices = [7, 6, 4, 3, 1]
            self.assertEqual(func(prices=prices), 0)

    def testMaxProfit4(self):
        for func in funcs:
            prices = [1]
            self.assertEqual(func(prices=prices), 0)


if __name__ == "__main__":
    unittest.main()
