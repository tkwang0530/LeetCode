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
1. DP: O(n) time | O(1) space
Now we have four variables instead of two on each day:
T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) = max(T[i-1][1][1], -prices[i])
T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - prices[i])
T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + prices[i])
"""




from typing import List
import unittest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstHold = -float("inf")
        firstIdle = 0
        secondHold = -float("inf")
        secondIdle = 0
        for price in prices:
            secondIdle = max(secondIdle, secondHold + price)
            secondHold = max(secondHold, firstIdle - price)
            firstIdle = max(firstIdle, firstHold + price)
            firstHold = max(firstHold, -price)
        return secondIdle


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
