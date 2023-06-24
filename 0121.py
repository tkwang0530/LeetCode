"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

"""
Note:
1. Brute Force: O(n^2) time | O(1) space
2. DP: O(n) time | O(1) space
k=1 case
hold = T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) = max(T[i-1][1][1], -prices[i])
idle = T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
"""

from typing import List
import unittest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                maxPro = max(maxPro, prices[j] - prices[i])
        return maxPro


    def maxProfit2(self, prices: List[int]) -> int:
        hold = -float("inf") # T[i=-1][1][1]
        idle = 0 # T[i=-1][1][0]
        for price in prices:
            hold = max(hold, -price)
            idle = max(idle, hold + price)
        return idle

# Unit Tests
funcs = [Solution().maxProfit,Solution().maxProfit2]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            prices = [7,1,5,3,6,4]
            self.assertEqual(func(prices=prices), 5)

    def testMaxProfit2(self):
        for func in funcs:
            prices = [7,6,4,3,1]
            self.assertEqual(func(prices=prices), 0)

if __name__ == "__main__":
    unittest.main()
