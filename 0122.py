"""
122. Best Time to Buy and Sell Stock II
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.

Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""

"""
Note:
1. DP: O(n) time | O(1) space
if k is positive infinity, then there isn't any difference between k and k-1, 
which implies T[i-1][k-1][0] = T[i-1][k][0] and T[i-1][k-1][1] = T[i-1][k][1]
Therefore,
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-1][k][0] - prices[i])
"""

from typing import List
import unittest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -float("inf") # T[i=-1][k=inf][1]
        idle = 0 # T[i=-1][k=inf][0]
        for price in prices:
            oldIdle = idle
            idle = max(idle, hold + price)
            hold = max(hold, oldIdle - price)
        return idle

# Unit Tests
funcs = [Solution().maxProfit]


class TestMaxProfit(unittest.TestCase):
    def testMaxProfit1(self):
        for func in funcs:
            prices = [7,1,5,3,6,4]
            self.assertEqual(func(prices=prices), 7)

    def testMaxProfit2(self):
        for func in funcs:
            prices = [1, 2, 3, 4, 5]
            self.assertEqual(func(prices=prices), 4)

    def testMaxProfit3(self):
        for func in funcs:
            prices = [7,6,4,3,1]
            self.assertEqual(func(prices=prices), 0)

if __name__ == "__main__":
    unittest.main()
